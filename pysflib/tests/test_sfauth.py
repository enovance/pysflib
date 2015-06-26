#!/usr/bin/env python
#
# Copyright (C) 2014 eNovance SAS <licensing@enovance.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from unittest import TestCase
from mock import patch

from pysflib import sfauth


def fake_send_request(*args, **kwargs):
    class Fake:
        cookies = {'auth_pubtkt': '1234'}
    return Fake()


class FakeJSONResponse(object):
    def __init__(self, dic):
        self.dic = dic

    def json(self):
        return self.dic


class TestSFAuth(TestCase):
    def test_get_cookie(self):
        with patch('pysflib.sfauth.requests.post',
                   new_callable=lambda: fake_send_request):
            self.assertEqual(
                '1234',
                sfauth.get_cookie('auth.tests.dom', 'user1', 'userpass'))
            self.assertEqual(
                '1234',
                sfauth.get_cookie('auth.tests.dom',
                                  github_access_token='abcd'))
            self.assertRaises(ValueError, sfauth.get_cookie, 'auth.tests.dom')

    def test_get_cauth_info(self):
        with patch('pysflib.sfauth.requests.get') as g:
            g.return_value = FakeJSONResponse({'service': {
                'name': 'cauth',
                'version': 'x.y.z',
                'auth_methods': ['password', 'openid']}})
            i = sfauth.get_cauth_info('auth.tests.dom')
            g.assert_called_with('http://auth.tests.dom/auth/about/',
                                 allow_redirects=False)
            self.assertEqual('cauth',
                             i['service']['name'])

    def test_get_managesf_info(self):
        with patch('requests.get') as g:
            g.return_value = FakeJSONResponse({'service': {
                'name': 'managesf',
                'version': 'x.y.z',
                'services': ['gerrit', ]}})
            i = sfauth.get_managesf_info('auth.tests.dom')
            g.assert_called_with('http://auth.tests.dom/about/',
                                 allow_redirects=False)
            self.assertEqual('managesf',
                             i['service']['name'])

# coding: utf-8

"""
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest
import pyfakefs.fake_filesystem_unittest as fake_fs_unittest
import json
from nose.tools import assert_raises, assert_is_instance

from lib_openshift import Wrapper,WrapperException


class TestWrapper(fake_fs_unittest.TestCase):
    """ Wrapper unit test stubs """

    def setUp(self):
        self.setUpPyfakefs()

    def tearDown(self):
        pass


    def test_wrapper_no_args_kubeconfig(self):
        kubeconfig = """
apiVersion: v1
clusters:
- cluster:
    server: http://localhost:8080
  name: local-server
contexts:
- context:
    cluster: local-server
    namespace: the-right-prefix
    user: myself
  name: default-context
current-context: default-context
kind: Config
preferences: {}
users:
- name: myself
  user:
    password: secret
    username: admin"""
        self.fs.CreateFile(os.path.expanduser('~/.kube/config'), contents=kubeconfig)
        self.assertTrue(os.path.exists(os.path.expanduser('~/.kube/config')))
        #wrapper = Wrapper()
        #TODO: finish this test


    def test_wrapper_no_args_no_kubeconfig(self):
        self.assertFalse(os.path.exists(os.path.expanduser('~/.kube/config')))
        assert_raises(WrapperException, Wrapper)
        try:
            Wrapper()
        except WrapperException as e:
            assert_is_instance(json.loads(str(e)), dict)

    def test_wrapper_invalid_auth_args(self):
        self.assertFalse(os.path.exists(os.path.expanduser('~/.kube/config')))
        assert_raises(WrapperException, Wrapper, username="blue")
        assert_raises(WrapperException, Wrapper, password="green")
        assert_raises(WrapperException, Wrapper, client_cert="here")
        assert_raises(WrapperException, Wrapper, client_key="there")
        assert_raises(WrapperException, Wrapper, username="blue", token="orange")
        assert_raises(WrapperException, Wrapper, password="green", token="orange")
        assert_raises(WrapperException, Wrapper, username="green", client_cert="here")
        assert_raises(WrapperException, Wrapper, username="green", client_key="here")
        assert_raises(WrapperException, Wrapper, password="green", client_cert="here")
        assert_raises(WrapperException, Wrapper, password="green", client_key="here")
        assert_raises(WrapperException, Wrapper, token="green", client_cert="here")
        assert_raises(WrapperException, Wrapper, token="green", client_key="here")

if __name__ == '__main__':
    unittest.main()

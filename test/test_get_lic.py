import unittest
import os

from license_adder import add_license


class GetLicTest(unittest.TestCase):
    def setUp(self):
        self.filename = 'mylic.txt'

        self.lic = '''Copyright 2020 Ashim Ghosh

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''

        with open(self.filename, 'w') as f:
            f.write(self.lic)

    def tearDown(self):
        os.remove(self.filename)

    def test_get_lic(self):
        got = add_license.get_lic(self.filename)
        self.assertMultiLineEqual(got, self.lic)

    def test_get_lic2(self):
        got = add_license.get_lic(self.filename)
        self.assertMultiLineEqual(got, self.lic)


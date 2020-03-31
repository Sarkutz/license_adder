import unittest
from license_adder import add_license

class GetFileExtTest(unittest.TestCase):
    def test_get_ext_of_test_txt(self):
        filename = 'test.txt'
        want = 'txt'
        got = add_license.get_file_ext(filename)
        self.assertEqual(want, got)

    def test_get_ext_of_a_b_py(self):
        filename = 'a.b.py'
        want = 'py'
        got = add_license.get_file_ext(filename)
        self.assertEqual(want, got)


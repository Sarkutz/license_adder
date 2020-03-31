import unittest
from license_adder import add_license

class GetCommentParamsTest(unittest.TestCase):
    def test_get_comment_params(self):
        iotab = [{'input': 'py', 'want': ('', '', '# ')},
                {'input': 'scala', 'want': ('/*\n', ' */\n', ' * ')},
                {'input': 'xml', 'want': ('<!--\n', '-->\n', '')},
                {'input': 'invalid', 'want': ('', '', '')}]

        for case in iotab:
            with self.subTest(msg='msg', test_input=case['input']):
                got = add_license.get_comment_params(case['input'])
                self.assertEqual(case['want'], got)


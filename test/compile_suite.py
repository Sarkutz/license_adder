import unittest
# import test.test_get_file_ext

def get_compile_test_suite():
    tests = ['test.test_get_file_ext.GetFileExtTest.test_get_ext_of_a_b_py',
            'test.test_get_file_ext.GetFileExtTest.test_get_ext_of_test_txt',
            'test.test_get_comment_params.GetCommentParamsTest.test_get_comment_params']

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # suite.addTest(loader.loadTestsFromModule(test.test_get_file_ext))
    for test_name in tests:
        suite.addTest(loader.loadTestsFromName(test_name))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_compile_test_suite())


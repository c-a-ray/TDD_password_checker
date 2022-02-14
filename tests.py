import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def try_pwd(self, pwd: str, is_valid: bool):
        self.assertEqual(check_pwd(pwd), is_valid)

    def test_empty_str(self):
        self.try_pwd('', False)
    
    def test_valid_pwd(self):
        self.try_pwd('MyValidPassword123!', True)


if __name__ == '__main__':
    unittest.main()

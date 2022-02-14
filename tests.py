import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def try_pwd(self, pwd: str, is_valid: bool):
        self.assertEqual(check_pwd(pwd), is_valid)


if __name__ == '__main__':
    unittest.main()

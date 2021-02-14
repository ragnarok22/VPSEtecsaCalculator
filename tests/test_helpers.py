import unittest

import helpers


class Test_mb_to_gb(unittest.TestCase):
    def test_int_mb(self):
        result = helpers.mb_to_gb(1024)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

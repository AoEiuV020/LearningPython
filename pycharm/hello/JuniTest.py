import unittest

import App


class MyTestCase(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual("Hello", App.greeting())


if __name__ == '__main__':
    unittest.main()

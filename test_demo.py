import unittest
from demo import show_aggie_pride


# https://docs.python.org/3/library/unittest.html
class MyTestCase(unittest.TestCase):
    def test_show_aggie_pride(self):
        df = show_aggie_pride()

        self.assertEqual(df.loc[0, 'Text'], 'Work today for what you want to achieve tomorrow')
        self.assertEqual(df.loc[1, 'Text'], 'Try and be just 1% better everyday')
        self.assertEqual(df.loc[2, 'Text'], 'A calm mind is the key to sound thinking')


if __name__ == '__main__':
    unittest.main()

import unittest
from demo import show_aggie_pride


# https://docs.python.org/3/library/unittest.html
class MyTestCase(unittest.TestCase):
    def test_show_aggie_pride(self):
        df = show_aggie_pride()

        self.assertEqual(df.loc[0, 'Text'], 'Aggie Pride')
        self.assertEqual(df.loc[1, 'Text'], 'Worldwide')
        self.assertEqual(df.loc[2, 'Text'], 'Hard Work Yields Results')
        self.assertEqual(df.loc[3, 'Text'], 'When One Door Closes Another One Opens')


if __name__ == '__main__':
    unittest.main()

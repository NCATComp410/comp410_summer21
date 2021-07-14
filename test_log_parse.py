# https://docs.python.org/3/library/unittest.html
import unittest
from log_parse import LogParse
import os


class LogParseTest(unittest.TestCase):
    """Unit test structure for LogParse"""
    # https://docs.python.org/3/library/unittest.html#unittest.TestCase

    # Sample syslog file
    fname = 'syslogs.txt'

    # Create a LogParse object and parse the test syslog file
    lp = LogParse()
    # https://pandas.pydata.org/docs/user_guide/index.html
    df = lp.parse_syslog_file(os.path.join(fname))

    def test_log_parse(self):
        """Basic test case to show that LogParse loads OK"""
        self.assertEqual('LogParse', self.lp.log_parse_id())

    def test_syslog_file(self):
        """Checks to make sure the syslog file appears valid"""
        # https://www.cisco.com/c/en/us/td/docs/security/asa/syslog/b_syslog/syslogs-sev-level.html
        fname = 'syslogs.txt'

        # Open the syslog file
        # https://docs.python.org/3/tutorial/inputoutput.html
        with open(os.path.join(fname), encoding='utf-8') as f:
            line_num = 1
            for line in f:
                # create a string with the current file name and line number
                # for use in error messages
                ln = fname+':'+str(line_num)+' '

                # expect all lines to begin with %ASA-
                # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex
                self.assertRegex(line, r'^%ASA-', ln+'does not start with %ASA-')

                # Make sure there are no other %ASA which would indicate a
                # merged line or other problem in the syslog file
                self.assertNotRegex(line, r'.%ASA', ln+'extra %ASA found')

                line_num += 1

    def test_ASA_1_103004(self):
        # %ASA-1-103004: (Primary) Other firewall reports this firewall failed. Reason: reason-string.
        self.assertTrue(self.df.loc[103004, 'Type'] == 'ASA')
        self.assertTrue(self.df.loc[103004, 'Severity'] == 1)
        self.assertTrue(self.df.loc[103004, 'Text'] == '(Primary) Other firewall reports this firewall failed. Reason: '
                                                  'reason-string.')
        self.assertTrue(self.df.loc[103004, 'Reason'] == 'reason-string.')


    def test_ASA_3_114009(self):
        # %ASA-3-114009: Failed to initialize 4GE SSM I/O card (error error_string).
        print(self.df.loc[114009])
        self.assertTrue(self.df.loc[114009, 'Type'] == 'ASA')
        self.assertTrue(self.df.loc[114009, 'Severity'] == 3)
        self.assertTrue(self.df.loc[114009, 'Text'] == 'Failed to initialize 4GE SSM I/O card (error error_string).')
        self.assertTrue(self.df.loc[114009, 'Error'] == 'error_string')



if __name__ == '__main__':
    unittest.main()

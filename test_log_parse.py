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

    def test_ASA_1_114001(self):
        # %ASA-1-114001: Failed to initialize 4GE SSM I/O card (error error_string).
        print(self.df.loc[114001])
        self.assertTrue(self.df.loc[114001, 'Type'] == 'ASA')
        self.assertTrue(self.df.loc[114001, 'Severity'] == 1)
        self.assertTrue(self.df.loc[114001, 'Text'] == 'Failed to initialize 4GE SSM I/O card (error error_string).')
        self.assertTrue(self.df.loc[114001, 'Error'] == 'error_string')

    def test_ASA_3_114010(self):
        # %ASA-3-114010: Failed to set multicast hardware address in 4GE SSM I/O card (error error_string).
        self.assertTrue(self.df.loc[114010, 'Type'] == 'ASA')
        self.assertTrue(self.df.loc[114010, 'Severity'] == 3)
        self.assertTrue(self.df.loc[114010, 'Text'] == 'Failed to set multicast hardware address in 4GE SSM I/O card (error error_string).')
        self.assertTrue(self.df.loc[114010, 'Error'] == 'error_string')

    def test_ASA_3_114012(self):
        # %ASA-3-114012: Failed to delete multicast hardware address in 4GE SSM I/O card (error error_string).
        print(self.df.loc[114012])
        self.assertTrue(self.df.loc[114012, 'Type'] == 'ASA')
        self.assertTrue(self.df.loc[114012, 'Severity'] == 3)
        self.assertTrue(self.df.loc[114012, 'Text'] == 'Failed to delete multicast hardware address in 4GE SSM I/O card'
                                                       ' (error error_string).')
        self.assertTrue(self.df.loc[114012, 'Error'] == 'error_string')


    def test_ASA_3_114013(self):
        # %ASA-3-114013: Failed to set mac address table in 4GE SSM I/O card (error error_string).
        print(self.df.loc[114013])
        self.assertTrue(self.df.loc[114013, 'Type'] == 'ASA')
        self.assertTrue(self.df.loc[114013, 'Severity'] == 3)
        self.assertTrue(self.df.loc[114013, 'Text'] == 'Failed to set mac address table in 4GE SSM I/O card (error '
                                                       'error_string).')
        self.assertTrue(self.df.loc[114013, 'Error'] == 'error_string')

    def test_ASA_3_114017(self):
         # %ASA-3-114017: Failed to get link status in 4GE SSM I/O card (error error_string).
         print(self.df.loc[114017])
         self.assertTrue(self.df.loc[114017, 'Type'] == 'ASA')
         self.assertTrue(self.df.loc[114017, 'Severity'] == 3)
         self.assertTrue(self.df.loc[114017, 'Text'] == 'Failed to get link status in 4GE SSM I/O card (error error_string).')
         self.assertTrue(self.df.loc[114017, 'Error'] == 'error_string')

    def test_ASA_3_114009(self):
        # %ASA-3-114009: Failed to initialize 4GE SSM I/O card (error error_string).
        print(self.df.loc[114009])
        self.assertTrue(self.df.loc[114009, 'Type'] == 'ASA')
        self.assertTrue(self.df.loc[114009, 'Severity'] == 3)
        self.assertTrue(self.df.loc[114009, 'Text'] == 'Failed to set multicast address in 4GE SSM I/O card (error error_string).')
        self.assertTrue(self.df.loc[114009, 'Error'] == 'error_string')

    def test_ASA_3_114011(self):
        # %ASA-3-114011: Failed to delete multicast address in 4GE SSM I/O card (error error_string).
        print(self.df.loc[114011])
        self.assertTrue(self.df.loc[114011, 'Type'] == 'ASA')
        self.assertTrue(self.df.loc[114011, 'Severity'] == 3)
        self.assertTrue(self.df.loc[114011, 'Text'] == 'Failed to delete multicast address in 4GE SSM I/O card (error error_string).')
        self.assertTrue(self.df.loc[114011, 'Error'] == 'error_string')




if __name__ == '__main__':
    unittest.main()

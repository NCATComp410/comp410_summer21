import pandas as pd
import re


class LogParse:
    """Parser for firewall logs"""
    def log_parse_id(self):
        """For testing purposes simply return a text message"""
        return 'LogParse'

    def handle_message(self, df, id):
        """Handles specific syslog messages"""
        # https://regex101.com
        # https://developers.google.com/edu/python/regular-expressions
        # https://www.w3schools.com/python/python_regex.asp
        # https://rosie-lang.org

        # %ASA-1-103004: (Primary) Other firewall reports this firewall failed. Reason: reason-string.
        # Parse the reason out of the text string
        if id == 103004:
            (message, reason) = df.loc[id, 'Text'].split('Reason: ')
            df.loc[id, 'Reason'] = reason.rstrip()
        elif id == 114001:
            # %ASA-1-114001: Failed to initialize 4GE SSM I/O card (error error_string).
            m = re.search(r'card \(error (\w+)\)', df.loc[id, 'Text'])
            if m:
                df.loc[id, 'Error'] = m.group(1)
        elif id == 114010:
            # %ASA-3-114010: Failed to set multicast hardware address in 4GE SSM I/O card (error error_string).
            m = re.search(r'card \(error (\w+)\)', df.loc[id, 'Text'])
            if m:
                df.loc[id, 'Error'] = m.group(1)        
        elif id == 114012:
            # %ASA-3-114012: Failed to delete multicast hardware address in 4GE SSM I/O card (error error_string).
            m = re.search(r'card \(error (\w+)\)', df.loc[id, 'Text'])
            if m:
                df.loc[id, 'Error'] = m.group(1)
        elif id == 114013:
            # %ASA-3-114013: Failed to set mac address table in 4GE SSM I/O card (error error_string).
            m = re.search(r'card \(error (\w+)\)', df.loc[id, 'Text'])
            if m:
                df.loc[id, 'Error'] = m.group(1)

        return df

    def parse_asa_logfile(self, asa_lotfile):
        """Parses an ASA logfile and returns everything in a dataframe"""

        # Will read all the data into this dict and convert to a dataframe leter
        data = {'Date': [],
                'Host': [],
                'Type': [],
                'Severity': [],
                'ID': [],
                'Message': [],
                'IP Address': []}

        with open(asa_lotfile, encoding='utf-8') as f:
            for line in f:
                # Parse an ASA logfile - groups are split as follows
                # 1 - timestamp
                # 2 = host
                # 3 = type
                # 4 = severity
                # 5 = message ID
                # 6 = message
                m = re.search(r'^(\w+ \d+ \d+ \d+:\d+:\d+) (\w+) : %(\w+)-(\d)-(\d+): (.+)', line)
                if m:
                    data['Date'].append(m.group(1))
                    data['Host'].append(m.group(2))
                    data['Type'].append(m.group(3))
                    data['Severity'].append(m.group(4))
                    data['ID'].append(m.group(5))
                    data['Message'].append(m.group(6))

                    # Check for an im address in the error message
                    # this example will use all 10.b.c.d addresses since these
                    # are classified as private addresses
                    # https://en.wikipedia.org/wiki/Private_network
                    m2 = re.search(r'\(error (\d+.\d+.\d+.\d+)\)', m.group(6))
                    if m2:
                        data['IP Address'].append(m2.group(1))

        # Create the dataframe and convert timestamp
        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'])

        return df

    def parse_syslog_file(self, syslog_file):
        """Returns a dataframe of parsed example syslogs"""

        # https://pandas.pydata.org/docs/user_guide/index.html
        df = pd.DataFrame()

        with open(syslog_file, encoding='utf-8') as f:
            for line in f:
                # %(Type)-(Severity)-(id): (Text)
                m = re.search(r'^%(\w+)-(\d)-(\d+): (.+)', line)
                # If the re matched
                if m:
                    id = int(m.group(3))
                    df.loc[id, 'Type'] = m.group(1)
                    df.loc[id, 'Severity'] = int(m.group(2))
                    df.loc[id, 'Text'] = m.group(4).rstrip()

                    df = self.handle_message(df, id)
        return df
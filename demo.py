import pandas as pd
from log_parse import LogParse


def show_aggie_pride():
    # https://pandas.pydata.org/docs/user_guide/index.html

    df = pd.DataFrame(['Aggie Pride', 'Worldwide', 'Hard Work Yields Results',
                       'Work today for what you want to achieve tomorrow', 'Aggies DO!',
                       'Giving Back Every Day, the Aggie Way', 'Aggies Rule', 
                       'When One Door Closes Another One Opens', 'Aggie Pride'], columns=['Text'])

    return df


def parse_logs():
    parser = LogParse()
    df = parser.parse_syslog_file('syslogs.txt')
    print('Total syslog found', end=': ')
    print(len(df))


if __name__ == "__main__":
    print(show_aggie_pride())

    print('\nCalling parse_logs()')
    parse_logs()

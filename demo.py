import pandas as pd
 from log_parse import LogParse


 def show_aggie_pride():
     # https://pandas.pydata.org/docs/user_guide/index.html

     df = pd.DataFrame(['Aggie Pride', 'Worldwide', 'Hard Work Yields Results',
                        'Work today for what you want to achieve tomorrow', 'Aggies DO!',
                        'Giving Back Every Day, the Aggie Way'], columns=['Text'])
                        'Giving Back Every Day, the Aggie Way', 'Aggies Rule',
                        'When One Door Closes Another One Opens', 'Aggie Pride',
                        'Aggies on fire'], columns=['Text'])

     return df


 def parse_logs():
     parser = LogParse()
     df = parser.parse_syslog_file('syslogs.txt')
     print('Total syslog found', end=': ')
     print(len(df))


 def asa_parse():
     # Parse the ASA logfile
     parser = LogParse()
     df = parser.parse_asa_logfile('dmz1_logs.txt')
     print(df.describe())

     # Create a table by hour with the total count of messages seen
     table = df.groupby([pd.Grouper(key='Date', freq='H')]).agg({'ID': 'count'})

     # Create a simple plot and save as a png
     fig = table.plot().get_figure()
     fig.savefig('plot.png')


 if __name__ == "__main__":
     print(show_aggie_pride())

     print('\nCalling parse_logs()')
     parse_logs()

     # Uncomment when we start sprint-4
     # print('\nCalling asa_parse()')
     # asa_parse()

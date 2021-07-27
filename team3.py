import pandas as pd
from log_parse import LogParse

def team3_asa_parse():
    # Parse the ASA logfile
    parser = LogParse()
    df = parser.parse_asa_logfile('dmz1_logs.txt')
    dft3 = df[df['ID'].isin(['114006', '114009', '114014'])]
    print(dft3.describe())

    # Create a table by hour with the total count of messages seen
    table = dft3.groupby([pd.Grouper(key='Date', freq='H')]).agg({'ID': 'count'})

    # Create a simple plot and save as a png
    fig = table.plot().get_figure()
    fig.savefig('team3plot.png')


if __name__ == "__main__":
    

    print('\nCalling parse_logs()')
    

    # Uncomment when we start sprint-4
    print('\nCalling asa_parse()')
    
    print('\nCalling team3_asa_parse')
    team3_asa_parse()
import pandas as pd


def show_aggie_pride():
    # https://pandas.pydata.org/docs/user_guide/index.html
    df = pd.DataFrame(['Aggie Pride', 'Worldwide','Hard Work Yields Results','Work today for what you want to achieve tomorrow',
                       'Aggies DO!', 'Giving Back Every Day, the Aggie Way'], columns=['Text'])

    return df


if __name__ == "__main__":
    print(show_aggie_pride())

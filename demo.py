'import pandas as pd


def show_aggie_pride():
    # https://pandas.pydata.org/docs/user_guide/index.html
    df = pd.DataFrame(['Aggie Pride', 'Worldwide','Aggies Rule'], columns=['Text'])

    return df


if __name__ == "__main__":
    print(show_aggie_pride())

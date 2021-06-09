import pandas as pd


def show_aggie_pride():
    # https://pandas.pydata.org/docs/user_guide/index.html
    df = pd.DataFrame(['Work today for what you want to achieve tomorrow', 'Try and be just 1% better everyday','A calm mind is the key to sound thinking'], columns=['Text'])

    return df


if __name__ == "__main__":
    print(show_aggie_pride())

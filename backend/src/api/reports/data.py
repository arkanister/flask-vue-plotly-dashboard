import pandas as pd
from flask import current_app


def get_data():
    """
    Load dataset and prepare for reports.
    """
    path = current_app.config['BASE_DIR'] / 'data/games.csv'

    # load dataset.
    df = pd.read_csv(path)

    # convert date column into python timestamps
    df['date'] = pd.to_datetime(df['date'], format='%B %d, %Y')
    df['year'] = df['date'].apply(lambda x: x.year)

    # convert user score into float
    df['userscore'] = pd.to_numeric(df['userscore'], errors='coerce')

    # strip platforms text
    df['platforms'] = df['platforms'] \
        .apply(str.strip) \
        .apply(lambda x: x.replace('\n', '')) \
        .apply(lambda x: x.replace('  ', ''))

    # drop invalid values
    df = df.dropna()

    return df

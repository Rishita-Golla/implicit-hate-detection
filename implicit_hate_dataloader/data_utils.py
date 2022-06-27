import pandas as pd

import config


def load_into_dataframe(dataset):
    return pd.read_csv(config.dataset_filename[dataset], delimiter='\t')


if __name__ == '__main__':
    for dataset in [f"stage-{i}" for i in range(1, 4)]:
        dataset_df = load_into_dataframe(dataset)
        print(dataset_df.columns)
        print(dataset_df.head())
        print(dataset_df.describe())
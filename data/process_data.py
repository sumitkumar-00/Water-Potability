# ETL Pipeline
# This python utility loads data and does the pre-processing for model intake

# Import python libraries
import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(filepath):
    """

    This procedure loads data in pandas dataframe and returns the dataframe
    :param filepath: path to the data file
    :return: dataframe
    """

    df = pd.read_csv(filepath)
    print("Data loaded successfully with {} rows and {} columns".format(df.shape[0], df.shape[1]))

    return df


def clean_data(df):
    """
    This procedure removes rows containing NAs from the dataframe
    :param df: dataframe loaded from the flat file
    :return: dataframe after removing NAs
    """
    return df.dropna()


def save_data(df, database_file):
    """
    Export cleaned data to a database that can later be imported by Machine learning utility
    :param df: cleaned dataframe
    :param database_file: sqlite database
    :return: None
    """
    engine = create_engine("sqlite:///" + database_file)
    df.to_sql("water_potability", engine, index=False, if_exists='replace')
    print("Data successfully saved in the database")

    return None


def main():
    """
    This procedure calls other procedures to load and pre-process data save the pre-processed data in sqlite database
    :return: None
    """
    if len(sys.argv) == 3:
        filepath, database_path = sys.argv[1:]

        print("Loading data from flat file...")
        df = load_data(filepath)

        print("Cleaning data ....")
        df = clean_data(df)

        print("Saving data ...")
        save_data(df, database_path)
    else:
        print("Please enter path for both flat file and the database file")


if __name__ == "__main__":
    main()

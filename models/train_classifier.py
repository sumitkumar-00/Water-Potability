# Import Libraries

import sys
import os
import glob
import pandas as pd
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.utils import resample
from sklearn.pipeline import Pipeline
from joblib import dump
from sqlalchemy import create_engine


def load_data(database_file):
    """
    This procedure loads the data from database and returns a dataframe
    :param database_file:
    :return: Predictors and response numpy arrays
    """

    # Load Data
    engine = create_engine("sqlite:///" + database_file)
    df = pd.read_sql_table("water_potability", engine)

    # Convert predictors and response variables into numpy arrays
    X = df.drop(['Potability'], axis=1).to_numpy()
    y = df['Potability'].to_numpy()

    return X, y


def upsample_train_data(X, y, random_state):
    """
    This function upsamples the minority class and returns new numpy arrays for predictor and response. Only works with
    binary classification problems
    :param X: predictors (numpy array)
    :param y: response (numpy array)
    :return: upsampled predictors and response numpy arrays
    """
    df = pd.concat([pd.DataFrame(X), pd.DataFrame(y, columns=['outcome'])], axis=1)

    val_counts = df.outcome.value_counts()
    val_counts = dict(val_counts)

    high_count = max(val_counts, key=val_counts.get)
    low_count = min(val_counts, key=val_counts.get)

    df_high = df[df.outcome == high_count]
    df_low = df[df.outcome == low_count]
    df_low = resample(df_low, n_samples=val_counts.get(high_count), replace=True, random_state=random_state)

    df = pd.concat([df_high, df_low], axis=0, ignore_index=True)
    X = df.drop('outcome', axis=1).to_numpy()
    y = df['outcome'].to_numpy()

    return X, y


def main():
    if len(sys.argv) == 3:
        database_file, model_file = sys.argv[1:]
        X, y = load_data(database_file)

        random_state = 7

        # Split train, test data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state, stratify=y)

        # Our dataset in imbalanced so we will upsample the training data
        X_train, y_train = upsample_train_data(X_train, y_train, random_state)

        # Build Model
        results = {}
        models = [
            ("model_rf", RandomForestClassifier()),
            ("model_ada", AdaBoostClassifier()),
            ("model_knn", KNeighborsClassifier())
        ]

        param_grids = [
            {'model_rf__min_samples_leaf': [2, 4, 6],
             'model_rf__criterion': ['gini', 'entropy'],
             'model_rf__n_estimators': [100, 200],
             'model_rf__random_state': [random_state]},
            {'model_ada__n_estimators': [100, 200],
             'model_ada__random_state': [random_state]},
            {'model_knn__n_neighbors': [4, 10, 20]}
        ]

        for i in range(0, 3):
            pipeline = Pipeline(steps=
            [
                ('scaler', StandardScaler()),
                models[i]
            ])

            grid_search = GridSearchCV(pipeline, param_grid=param_grids[i], cv=5, scoring=make_scorer(accuracy_score),
                                       verbose=1)

            cv = grid_search.fit(X_train, y_train)
            results[i] = accuracy_score(y_test, grid_search.best_estimator_.predict(X_test))
            dump(cv, "models/model_" + str(i) + ".pkl")

        print(results)

        # Save best model file
        save_best_model(results)

    else:
        print("Please pass data file and pickle file name as arguments")

def save_best_model(results):
    """
    This procedure saves the best model and deletes the others from the file system
    :param results: model index with test results
    :return: None
    """

    best_model_index = max(results, key=results.get)
    if os.path.exists("models/model_" + str(best_model_index) + ".pkl"):
        print("Renaming best model file....")
        os.rename("models/model_" + str(best_model_index) + ".pkl", "models/water_potability.pkl")

    # Delete model file we do not need to save
    filelist = glob.glob("models/model*.pkl")
    for file in filelist:
        os.remove(file)


if __name__ == '__main__':
    main()

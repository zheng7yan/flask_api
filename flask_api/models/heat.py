import pandas as pd
import dill as pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import make_pipeline

import warnings

warnings.filterwarnings("ignore")


def build_and_train():
    data = pd.read_csv('data/heat/training.csv')
    pipe = make_pipeline(PreProcessing(),
                         SVC())

    pipe.fit(data, data.Quality.as_matrix())

    return pipe


class PreProcessing(BaseEstimator, TransformerMixin):
    """Custom Pre-Processing estimator for our use-case
    """

    def __init__(self):
        pass

    def transform(self, df):
        return df[['Temperature', 'Value']].as_matrix()

    def fit(self, df, y=None, **fit_params):
        return self


target = 'heat.pk'

if __name__ == '__main__':
    model = build_and_train()

    with open('models/' + target, 'wb') as file:
        pickle.dump(model, file)

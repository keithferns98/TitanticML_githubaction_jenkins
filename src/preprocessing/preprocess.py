import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer


numeric_features = ["Age", "Fare"]
categorical_features = ["Sex", "Embarked", "Pclass", "SibSp", "Parch"]

num_imputer = SimpleImputer(strategy="median")
scaler = StandardScaler()

cat_imputer = SimpleImputer(strategy="most_frequent")
encoder = OneHotEncoder(drop="first", handle_unknown="ignore")


def fit_preprocessor(X):
    """
    Used during training
    """
    num = num_imputer.fit_transform(X[numeric_features])
    num = scaler.fit_transform(num)

    cat = cat_imputer.fit_transform(X[categorical_features])
    cat = encoder.fit_transform(cat).toarray()

    return num, cat


def transform_input(data: dict):
    """
    Used during inference
    """

    df = pd.DataFrame([data])

    num = num_imputer.transform(df[numeric_features])
    num = scaler.transform(num)

    cat = cat_imputer.transform(df[categorical_features])
    cat = encoder.transform(cat).toarray()

    import numpy as np
    X = np.concatenate([num, cat], axis=1)

    return X
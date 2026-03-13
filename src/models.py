from sklearn.ensemble import RandomForestClassifier


def train_random_forest(X_train, y_train):

    model = RandomForestClassifier(
        n_estimators=200,
        max_features="sqrt",
        min_samples_leaf=1,
        oob_score=True,
        n_jobs=-1,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model
import yfinance as yf

from feature_engineering import buat_dataset

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit




df = yf.download("BBCA.JK", period="2y")
df.columns = df.columns.droplevel("Ticker")

dataset = buat_dataset(df)




split = int(len(dataset) * 0.8)

train = dataset.iloc[:split]
test = dataset.iloc[split:]

X_train = train.drop("target", axis=1)
y_train = train["target"]

X_test = test.drop("target", axis=1)
y_test = test["target"]

print(f"Train: {len(train)} baris")
print(f"Test : {len(test)} baris")

print("\nDistribusi train:")
print(y_train.value_counts())

print("\nDistribusi test:")
print(y_test.value_counts())



tscv = TimeSeriesSplit(n_splits=5)



param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}




grid_search = GridSearchCV(
    estimator=RandomForestClassifier(
        class_weight="balanced",
        random_state=42
    ),
    param_grid=param_grid,
    cv=tscv,
    scoring="f1_macro",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)




print("\nBest Parameters:")
print(grid_search.best_params_)

print(f"\nBest CV F1 Macro: {grid_search.best_score_:.3f}")


best_model = grid_search.best_estimator_




y_pred = best_model.predict(X_test)

print("\nClassification Report (Test Set)")
print(classification_report(y_test, y_pred))
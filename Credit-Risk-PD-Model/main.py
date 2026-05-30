from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import create_features
from src.model import train_model
from src.evaluation import evaluate

df = load_data("data/data.csv")
df = clean_data(df)
df = create_features(df)

X = df.drop("target", axis=1)
y = df["target"]

model, X_test, y_test = train_model(X, y)
evaluate(model, X_test, y_test)

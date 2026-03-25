import mlflow
import mlflow.sklearn
import skops.io as sio

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


iris = load_iris()
x = iris.data
y = iris.target
target_names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

mlflow.set_experiment("Iris-classifier")

def train_model():
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, pred)

        mlflow.log_metric("Accuracy", accuracy)
        mlflow.log_param("Estimators", 100)

        mlflow.sklearn.log_model(
            sk_model=model,
            name="model",
            serialization_format="skops"
        )
        print(f"Run Id: {run_id}")
        print(f"Accuracy: {accuracy}")

if __name__=="__main__":
    train_model()
    print(f"Finished Running")

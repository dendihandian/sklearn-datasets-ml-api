import mlflow
import pandas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from pprint import pprint

diabetes = load_iris(as_frame=True).frame
predictors = diabetes.loc[:, ~diabetes.columns.isin(['target'])]
target = diabetes[['target']]

x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size = 0.2, random_state = 1)

def fetch_logged_data(run_id):
    client = mlflow.tracking.MlflowClient()
    data = client.get_run(run_id).data
    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in client.list_artifacts(run_id, "model")]
    return data.params, data.metrics, tags, artifacts

def main():

    mlflow.sklearn.autolog()

    print("\ntraining started")

    decision_tree_model = DecisionTreeClassifier()
    with mlflow.start_run() as run:
        decision_tree_model.fit(x_train, y_train)

    params, metrics, tags, artifacts = fetch_logged_data(run.info.run_id)
    print("\n -------------- params --------------")
    pprint(params)
    print("\n -------------- metrics --------------")
    pprint(metrics)
    print("\n -------------- tags --------------")
    pprint(tags)
    print("\n -------------- artifacts --------------")
    pprint(artifacts)

    print("\ntraining finished")

if __name__ == "__main__":
    main()
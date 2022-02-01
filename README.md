# Sklearn Datasets ML API


## API
### Endpoints
- `POST` /diabetes/predict
- `POST` /iris/predict

## Requirements
- Python 3.6 or above
- Poetry Dependency Manager

## Development Setup

### Installing The Project
```
poetry install
```

### Starting The Server
```
poetry run uvicorn app.main:app --reload
```

## MLFlow

### Train and Tracking Model
```
poetry run python mltracking\diabetes_lr.py
```
```
poetry run python mltracking\iris_dt.py
```

### Running The MLFLow UI
```
poetry run mlflow ui
```

## Deployment

### Exporting The Environment For Production
```
poetry export -f requirements.txt --without-hashes > requirements.txt
```

### Building The Docker Image
```
docker build -t sklearn-datasets-ml-api:latest -f ./docker/0.1.0/python/Dockerfile .
```
```
docker build -t sklearn-datasets-ml-api:latest -f ./docker/0.1.0/alpine/Dockerfile .
```

### Running The Built Image Into Container
```
docker run -d --name sdml-api -p 80:80 sklearn-datasets-ml-api:latest
```

## Appendix

Adding Python Package for Production Example:
```
poetry add fastapi
```

Adding Python Package for Development Example:
```
poetry add mlflow --dev
```

Removing Package From Development Dependencies:
```
poetry remove pandas --dev
```

Exporting Enviroment Including Development Dependencies:
```
poetry export -f requirements.txt --without-hashes > requirements.txt --dev
```
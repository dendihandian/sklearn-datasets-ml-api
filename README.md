# Sklearn Datasets ML API

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
poetry run python diabetes_lr.py
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
docker build -t sklearn-datasets-ml-api:python-3.9 -f ./docker/python/Dockerfile .
```

### Running The Built Image Into Container
```
docker run -d --name sdml-api -p 80:80 sklearn-datasets-ml-api:python-3.9
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

Exporting Enviroment Including Development Dependencies:
```
poetry export -f requirements.txt --without-hashes > requirements.txt --dev
```
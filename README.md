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
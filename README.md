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
poetry run uvicorn main:app --reload
```

## Deployment

### Exporting The Environment For Production
```
poetry export -f requirements.txt --without-hashes > requirements.txt
```
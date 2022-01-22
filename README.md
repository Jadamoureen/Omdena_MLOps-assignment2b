# Omdena_MLOps-assignment2b

### FastAPI

Fast Api - is a modern, high-performance web framework for building APIs with Python based on standard type hints

### Install FastAPI


The first step is to install FastAPI and Uvicorn using pip:

```
$ python -m pip install fastapi uvicorn
```


### Create a First API
A basic FastAPI file looks like this:

```
# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### Run the First API App With Uvicorn

```
$ uvicorn main:app --reload
```

### Check the Response
Open your browser to http://127.0.0.1:8000.

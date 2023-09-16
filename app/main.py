import os

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "hello": "this is a container service",
        "from hostname": f"{os.environ.get('HOSTNAME', 'DEFAULT_ENV')}"
    }
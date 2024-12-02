from fastapi import FastAPI
import pandas as pd

app=FastAPI()

@app.get("test")
def read_root():
    return {'hello':'world'}

@app.get("/")
def read_root():
    return {'hello':'world'}


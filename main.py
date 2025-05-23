from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
  return {"Message" : "Hello World"}

@app.get("/add/{n1}/{n2}")
def add(n1: int, n2: int):
  return {"result" : n1+n2}

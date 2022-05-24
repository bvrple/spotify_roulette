from fastapi import FastAPI, Request
from fastapi.params import Body
from fastapi.templating import Jinja2Template
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    user: str
    title: str
    content: str
    published: bool
    rating: str



@app.get("/")
def root():
    return {"message": "s"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

my_posts = []
@app.post("/createposts")
def create_posts(payload: dict=Body(...)):
    print(payload)
    
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
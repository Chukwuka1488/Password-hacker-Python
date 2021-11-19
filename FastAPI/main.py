# source venv/bin/activate

# pip install -r requirements.txt

# uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"message": "get a post"}


@app.post("/createPosts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}

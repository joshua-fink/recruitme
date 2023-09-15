from typing import Optional

from fastapi import FastAPI, Body
import openai

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/generate_email")
async def generate_email(
    name: str=Body(), 
    email: str=Body(),
    company: str=Body(),
    role: str=Body(),
    comments: str=Body(),
    api_key: str=Body(),
):
    openai.api_key = api_key
    openai.api_key = ""
    return "YAY {name} {email} {company} {role} {comments}"

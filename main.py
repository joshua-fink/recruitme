from typing import Optional

from fastapi import FastAPI, Body
import openai

openai.api_key = "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"

app = FastAPI()

@app.post("/generate_email")
async def generate_email(
    recruiter_name: str=Body(), 
    recruiter_email: str=Body(),
    company: str=Body(),
    role: str=Body(),
    comments: str=Body(),
    api_key: str=Body(),
):
    openai.api_key = api_key
    openai.api_key = ""
    return "YAY"

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
    event: str=Body(),
    company: str=Body(),
    role: str=Body(),
    comments: str=Body(),
    api_key: str=Body(),
):
    openai.api_key = api_key
    
    introduction = "Dear " + name + ",\nMy name is Joshua Fink, and I just quickly wanted to thank you for our conversation today using my ChatGPT-powered job fair follow up application. (See source code at github.com/joshua-fink/recruitme.)"


    #request = 'My name is Joshua Fink, I am a recent University of Michigan computer science graduate looking for work. Write a onb introductory message that I can send on LinkedIn to ' + name.text + ' to see if software engineering or business consulting positions are available. Be sure to emphasize how their experience, especially their current position, would be helpful finding a job. If keyword has abbreviations, do not try to extrapolate what they mean'

    #input = name_string + position_string + most_recent_string + request

    #chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": input}])


    return introduction

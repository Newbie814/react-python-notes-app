from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.


app = FastAPI()

@app.get('/')
def getRoutes():
  return['/notes', '/notes/<pk>']
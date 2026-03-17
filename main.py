from fastapi import FastAPI
import threading
import time

app = FastAPI()

def bot():
    while True:
        print("Rodando bot...")
        time.sleep(10)

@app.get("/")
def home():
    return {"status": "bot rodando"}

@app.get("/start")
def start_bot():
    threading.Thread(target=bot).start()
    return {"message": "bot iniciado"}
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

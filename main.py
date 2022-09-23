from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def my_ip():
    ip_publico = requests.get('https://api.ipify.org/').text
    return {"IP Publico": ip_publico}
    

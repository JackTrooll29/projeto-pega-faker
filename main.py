from fastapi import FastAPI
import requests
import socket

app = FastAPI()


@app.get("/")
def my_ip():
    ip_local = socket.gethostbyname(socket.gethostname())
    ip_publico = requests.get('https://api.ipify.org/').text
    return {"IP Publico": ip_publico, "IP Local": ip_local}
    

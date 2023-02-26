import requests
import json
import time

ESP_URL = "YOUR HTTP URL HERE"
# for example: http://192.168.1.165

res = requests.post(f"{ESP_URL}/control", json={"hello":"world"})
print(res.text)    
        

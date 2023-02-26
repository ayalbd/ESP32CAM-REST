#Preperations
If you are using an ESP32CAM board
Make sure to select the proper board in the arduino
AI Thinker ESP32CAM

If you are using a ESP32-CAM-MB (Motherboard) setup
select the ESP32-WROOM-DA board

---

#Basic Explanation  
The ESP32CAM is the server:
When starting it connects to the WiFi and provides the server address.
Then it sits there waiting for approach from the client
The client may send "- GET" requests - the Sertver sends the data
If the client sends a "control - POST"  request - the server uses the data on the POST to run th cotroller logic.

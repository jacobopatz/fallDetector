# Fall Detection System

This project implements a fall detection system using a **Raspberry Pi** connected to an **IMU sensor**. The system detects excessive acceleration events (falls) and sends notifications via **HTTP requests** to a Django backend. The Django project processes this data, updates a dashboard, and sends alerts to family members or emergency services as needed.

---

## Repository Structure

```text
all-detection-system/
│
├── client program/ # Python scripts to be run on the Raspberry Pi (client)
└── falldetectionapp/ # Django project (server)
```

### **client_program/**

- Contains Python scripts that simulate or interact with the client device (Raspberry Pi + IMU sensor).  
- Capable of sending fall notifications to the server via HTTP requests.  
- For development, the scripts can be run on a local machine before porting to the Raspberry Pi.

### **falldetectionapp/**

- Contains all server-side code (Django project).  
- Runs the backend that receives and processes client data, powers the dashboard, and manages alerts.

---

## Django Apps Overview

### 1. `falldetectionapp`
- Top-level Django project app.  
- Contains `settings.py` and links all other apps together.  
- Imports each app’s URLs so they are accessible from the server.

### 2. `API`
- Handles all incoming data from the Raspberry Pi.  
- Receives, processes, and routes data to the appropriate Django apps.

### 3. `dashBoard`
- Powers the visual dashboard for users.  
- Displays patient status, fall history, and other relevant metrics after login.

### 4. `Alerts`
- Manages alerts to family members and emergency services.  
- Determines who to notify and what message to send upon receiving a fall detection.

---

## How It Works

1. The **Raspberry Pi** monitors the IMU sensor for acceleration above a defined threshold.  
2. When a fall is detected, the client sends a **HTTP request** with fall details to the Django API.  
3. The **API app** processes the incoming data and updates the system accordingly.  
4. The **dashBoard app** reflects the latest status and history for the user.  
5. The **Alerts app** sends notifications to designated recipients.

---

## Technology Stack

**Client:**
- Python  
- Raspberry Pi  
- IMU Sensor  

**Server:**
- Django  
- Django REST Framework (API)  
- SQLite/PostgreSQL (or any configured database)  

**Communication:**
- HTTP requests from client to server  

---

## Notes

- For development, you can simulate the client scripts on a local machine.  
- Deployment to a Raspberry Pi requires installing dependencies and configuring the network for HTTP requests to the Django server.  
- Ensure privacy and ethical considerations when handling user data.  



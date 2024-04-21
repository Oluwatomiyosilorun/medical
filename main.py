from fastapi import FastAPI
from routers import patients, doctors, appointments

app = FastAPI()

app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

@app.get('/')
def home():
    return 'Welcome to your Medical Apponitment'

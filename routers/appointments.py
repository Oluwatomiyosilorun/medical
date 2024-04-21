from fastapi import APIRouter, HTTPException
from typing import List
from models import Appointment
from data import appointments, doctors

import random


router = APIRouter()

@router.post("/appointments/")
def create_appointment(appointment: Appointment):
    appointment.id = random.randint(1, 358721)
    for doctor in doctors:
        if doctor.is_available:
            appointment.doctor_id = doctor.id
            appointments.append(appointment)
            doctor.is_available = False 
            return appointment
    raise HTTPException(status_code=404, detail="Our doctors are currently unavailable")

@router.get("/appointments/", response_model=List[Appointment])
def get_all_appointments():
    return appointments

@router.delete("/appointments/{appointment_id}")
def cancel_appointment(appointment_id: int):
    for index, appointment in enumerate(appointments):
        if appointment.id == appointment_id:
            for doctor in doctors:
                if doctor.id == appointment.doctor_id:
                    doctor.is_available = True
                    break
            del appointments[index]
            return {"status": "appointment canceled"}
    raise HTTPException(status_code=404, detail="Appointment not found")

from fastapi import APIRouter, HTTPException
from typing import List
from models import Doctor, DoctorUpdate
from data import doctors

import random


router = APIRouter()

@router.post("/doctors/", response_model=Doctor, status_code=201)
def create_doctor(doctor: Doctor):
    doctor.id = random.randint(1, 358721)
    doctors.append(doctor)
    return doctor

@router.get("/doctors/", response_model=List[Doctor])
def get_all_doctors():
    return doctors

@router.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor.id == doctor_id:
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

@router.put("/doctors/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, phone: int):
    for doctor in doctors:
        if doctor.id == doctor_id:
            doctor.phone = phone
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

@router.delete("/doctors/{doctor_id}", status_code=204)
def delete_doctor(doctor_id: int):
    for index, doc in enumerate(doctors):
        if doc.id == doctor_id:
            del doctors[index]
            return
    raise HTTPException(status_code=404, detail="Doctor not found")

@router.patch("/doctors/{doctor_id}/availability", response_model=Doctor)
def set_doctor_availability(doctor_id: int, is_available: bool):
    for doctor in doctors:
        if doctor.id == doctor_id:
            doctor.is_available = is_available
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

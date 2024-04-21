from fastapi import APIRouter, HTTPException, status
from models import Patient,PatientUpdate
from data import patients
from typing import List

import random

router = APIRouter()

@router.post("/patients/", status_code=201)
def create_patient(patient: Patient):
    patient.id = random.randint(1, 358721)
    patients.append(patient)
    return patient

@router.get("/get-patients/", response_model=List[Patient])
def get_all_patients():
    return patients

@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@router.put("/patients/{patient_id}")
def update_patient(patient_id: int, updated_patient: PatientUpdate):
    for patient in patients:
        if patient.id == patient_id:
            patient.age = updated_patient.age
            patient.weight = updated_patient.weight
            patient.height = updated_patient.height
            patient.phone = updated_patient.phone
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@router.delete("/patients/{patient_id}", status_code=204)
def delete_patient(patient_id: int):
    for index, patient in enumerate(patients):
        if patient.id == patient_id:
            del patients[index]
            return
    raise HTTPException(status_code=404, detail="Patient not found")

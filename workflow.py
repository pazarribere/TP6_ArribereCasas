from patient import create_patient_resource
from condition import create_condition_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, get_patient_by_dni

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    family_name = "Barry"
    given_name = "Ben"
    birth_date = "1999-08-08"
    gender = "male"
    phone = None
    dni = "41846513"

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, dni)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')
    
    get_patient_by_dni(dni)

    condition_resource = create_condition_resource(
        condition_code="Diabetes tipo 2",
        patient_id="12345",
        condition_status="active",
        onset_date="2020-01-01",  # Usar formato string adecuado
        end_date="2025-01-01",    # Usar formato string adecuado
        condition_id="condition123"
    )
    
    print(condition_resource.json())
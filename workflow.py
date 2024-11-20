from patient import create_patient_resource
from device import create_device_resource
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
    print('\n Creando paciente \n')
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, dni)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')
    print(f"\nID del paciente: {patient_id}")

    print('\nBuscando el paciente por ID')

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')
    
    
    print("\nBuscando paciente por DNI... \n")
    get_patient_by_dni(41846513)

    print("\nCreando un dispositivo: Monitor de Electrocardiograma\n")

    # Parámetros del dispositivo
    device_name = "Monitoreo ECG"
    status = "active"
    manufacturer = "MedTech Corp."
    model_number = "ECG-201"
    manufacture_date = "2020-06-15"
    expiration_date = "2025-06-15"
    id = "2792338"

    # Crear y enviar el recurso de dispositivo
    device = create_device_resource(device_name, status, manufacturer, model_number, manufacture_date, expiration_date, id)
    device_id = send_resource_to_hapi_fhir(device, 'Device')

    # Ver el recurso de dispositivo creado
    if device_id:
        get_resource_from_hapi_fhir(device_id, 'Device')

    print("\n")
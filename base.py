import requests
from patient import create_patient_resource


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f" http://hapi.fhir.org/baseR5/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None

# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f" http://hapi.fhir.org/baseR5/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())

# Buscar el recurso por DNI 
def get_patient_by_dni(dni):
    url = f"http://hapi.fhir.org/baseR5/Patient?identifier={dni}"
    
    # Realizar la solicitud GET
    response = requests.get(url, headers={"Accept": "application/fhir+json"})
    
    # Verificamos si la solicitud fue exitosa
    if response.status_code == 200:
        # Si hay pacientes encontrados, mostramos el primero
        resources = response.json().get('entry', [])
        if resources:
            patient = resources[0]['resource']
            print(f"Paciente encontrado: {patient}")
        else:
            print(f"No se encontró ningún paciente con el documento {dni}.")
    else:
        print(f"Error al buscar el paciente: {response.status_code}")

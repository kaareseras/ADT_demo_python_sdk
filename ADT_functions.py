import json
import os

### delete all models 
def delete_all_models(service_client):
    models = service_client.list_models()
    for model in models:
        service_client.delete_model(model.id)
    return True


# Delete all releationships and subsequent delete all nodes
def del_all_twins(service_client):
    query_expression = 'SELECT * FROM digitaltwins'
    query_result = service_client.query_twins(query_expression)  # get all twins
    for twin in query_result:
        digital_twin_id = twin['$dtId']
        relationships = service_client.list_relationships(digital_twin_id) # list the twins relationships
        for relationship in relationships:
            relationship_id = relationship['$relationshipId']
            service_client.delete_relationship(digital_twin_id, relationship_id) # delete the relationship
            #print(f'Deleted: {relationship} from {digital_twin_id}')

    query_expression = 'SELECT * FROM digitaltwins'
    query_result = service_client.query_twins(query_expression)
    for twin in query_result:
        digital_twin_id = twin['$dtId']
        service_client.delete_digital_twin(digital_twin_id)
        #print(f'Deleted twin: {digital_twin_id}')

### Create all models in the /Model folder
def create_models(service_client):
    directory = './Models'

    new_models = []
 
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
    # checking if it is a file
        if os.path.isfile(f):
            with open(f,'r') as file:
                model = json.load(file)
            new_models.append(model)

    models = service_client.create_models(new_models)
    return models

## add sites
def add_site(service_client, digital_twin_id,name):
    # the necessary metadata of the digital twin
    temp_twin = {
        "$metadata": {
            "$model": "dtmi:com:microsoft:iot:e2e:SmartHouse:Site;1" #give the model's id here
        },
        "$dtId": digital_twin_id,
        "SiteName": name
    }
    created_twin = service_client.upsert_digital_twin(digital_twin_id, temp_twin)
    return True

## add building
def add_building(service_client, digital_twin_id,BuildingName, BuildingArea):
    # the necessary metadata of the digital twin
    temp_twin = {
        "$metadata": {
            "$model": "dtmi:com:microsoft:iot:e2e:SmartHouse:Building;1" #give the model's id here
        },
        "$dtId": digital_twin_id,
        "BuildingName": BuildingName,
        "BuildingArea": BuildingArea
    }
    created_twin = service_client.upsert_digital_twin(digital_twin_id, temp_twin)
    return True

## add area
def add_area(service_client, digital_twin_id,AreaName):
    # the necessary metadata of the digital twin
    temp_twin = {
        "$metadata": {
            "$model": "dtmi:com:microsoft:iot:e2e:SmartHouse:Area;1" #give the model's id here
        },
        "$dtId": digital_twin_id,
        "AreaName": AreaName,
    }
    created_twin = service_client.upsert_digital_twin(digital_twin_id, temp_twin)
    return True

## add floor
def add_floor(service_client, digital_twin_id, FlorName, FloorArea, FloorLevel):
    # the necessary metadata of the digital twin
    temp_twin = {
        "$metadata": {
            "$model": "dtmi:com:microsoft:iot:e2e:SmartHouse:Floor;1" #give the model's id here
        },
        "$dtId": digital_twin_id,
        "FlorName": FlorName,
        "FloorArea": FloorArea,
        "FloorLevel": FloorLevel
    }
    created_twin = service_client.upsert_digital_twin(digital_twin_id, temp_twin)
    return True

## add room
def add_room(service_client, digital_twin_id, RoomName, Temperature, Humidity, Ocupied, RoomArea):
    # the necessary metadata of the digital twin
    temp_twin = {
        "$metadata": {
            "$model": "dtmi:com:microsoft:iot:e2e:SmartHouse:Room;1" #give the model's id here
        },
        "$dtId": digital_twin_id,
        "RoomName": RoomName,
        "Temperature": Temperature,
        "Humidity": Humidity,
        "Ocupied": Ocupied,
        "RoomArea": RoomArea
    }
    created_twin = service_client.upsert_digital_twin(digital_twin_id, temp_twin)
    return True

def add_sensor(service_client, digital_twin_id, Manufacturer, Active, Temperature):
    # the necessary metadata of the digital twin
    temp_twin = {
        "$metadata": {
            "$model": "dtmi:com:microsoft:iot:e2e:SmartHouse:HA_Temp_Sensor;1" #give the model's id here
        },
        "$dtId": digital_twin_id,
        "Manufacturer": Manufacturer,
        "Active": Active,
        "Temperature": Temperature
    }
    created_twin = service_client.upsert_digital_twin(digital_twin_id, temp_twin)
    return True

## add relationship
def add_relationship(service_client, relationshipId, relationshipName, sourceId, targetId):
    # the necessary metadata of the digital twin
    relationship = {
        "$relationshipId": relationshipId + '_' + sourceId + '_' + targetId + ';1',
        "$sourceId": sourceId,
        "$relationshipName": relationshipName,
        "$targetId": targetId
    }
    created_relationship = service_client.upsert_relationship(
        relationship["$sourceId"],
        relationship["$relationshipId"],
        relationship
    )

    return True



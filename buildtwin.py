import os
import random
from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
#from ADT_functions import create_models, delete_all_models, add_site, add_building, add_area, add_floor, add_room, add_relationship, del_all_twins,add_sensor
from ADT_functions import *


# DefaultAzureCredential supports different authentication mechanisms and determines the appropriate credential type based of the environment it is executing in.
# It attempts to use multiple credential types in an order until it finds a working credential.

# - AZURE_URL: The URL to the ADT in Azure
url = os.getenv("AZURE_URL")

# DefaultAzureCredential expects the following three environment variables:
# - AZURE_TENANT_ID: The tenant ID in Azure Active Directory
# - AZURE_CLIENT_ID: The application (client) ID registered in the AAD tenant
# - AZURE_CLIENT_SECRET: The client secret for the registered application
credential = DefaultAzureCredential()
service_client = DigitalTwinsClient(url, credential)

print("Deleting old relations and nodes")
del_all_twins(service_client)

print("Deleting old models")
delete_all_models(service_client)

print("Adding models")
create_models(service_client)

print("Adding sites")
add_site(service_client, 'Skonnertvej', 'Skonnertvej')

print("Adding buildings")
add_building(service_client, 'House', 'House',160)
add_building(service_client, 'Garage_building', 'Garage_building',50)

print("Adding areas")
add_area(service_client, 'Driveway', 'Driveway')

print("Adding floors")
add_floor(service_client, 'GroundLevel', 'GroundLevel',160,0)
add_floor(service_client, 'Basement', 'Basement',160,-1)
add_floor(service_client, 'Attic', 'Attic',160,1)

print("Adding rooms")
add_room(service_client,'Livingroom','Livingroom', 30, 0, False, 0)
add_room(service_client,'Diningroom','Diningroom', 15, 0, False, 0)
add_room(service_client,'Kitchen','Kitchen', 15, 0, False, 0)
add_room(service_client,'Hall','Hall', 12, 0, False, 0)
add_room(service_client,'Utility','Utility', 12, 0, False, 0)
add_room(service_client,'Bedroom','Bedroom', 12, 0, False, 0)
add_room(service_client,'Walkin','Walkin', 8, 0, False, 0)
add_room(service_client,'Bathroom','Bathroom', 8, 0, False, 0)
add_room(service_client,'SmallBathroom','SmallBathroom', 8, 0, False, 0)
add_room(service_client,'Office','Office', 8, 0, False, 0)
add_room(service_client,'Jakobsroom','Jakobsroom', 8, 0, False, 0)
add_room(service_client,'Atticroom','Atticroom', 8, 0, False, 0)
add_room(service_client,'Stairs','Stairs', 8, 0, False, 0)
add_room(service_client,'Workshop','Workshop', 8, 0, False, 0)
add_room(service_client,'Kåres_kontor','Kåres_kontor', 8, 0, False, 0)
add_room(service_client,'Teenage','Teenage', 8, 0, False, 0)
add_room(service_client,'Garage','Garage', 40, 0, False, 0)
add_room(service_client,'Shed','Shed', 10, 0, False, 0)

print("Adding relationships")
relationshipId = "dtmi:com:microsoft:iot:e2e:SmartHouse:site:rel_has_area"
relationshipName = "rel_has_area"
add_relationship(service_client, relationshipId, relationshipName, "Skonnertvej", "Driveway")

relationshipId = "dtmi:com:microsoft:iot:e2e:SmartHouse:site:rel_has_building"
relationshipName = "rel_has_building"
add_relationship(service_client, relationshipId, relationshipName, "Skonnertvej", "House")
add_relationship(service_client, relationshipId, relationshipName, "Skonnertvej", "Garage_building")

relationshipId = "dtmi:com:microsoft:iot:e2e:SmartHouse:Building:rel_has_floor"
relationshipName = "rel_has_floor"
add_relationship(service_client, relationshipId, relationshipName, "House", "GroundLevel")
add_relationship(service_client, relationshipId, relationshipName, "House", "Basement")
add_relationship(service_client, relationshipId, relationshipName, "House", "Attic")

relationshipId = "dtmi:com:microsoft:iot:e2e:SmartHouse:Floor:rel_has_room"
relationshipName = "rel_has_room"
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Livingroom")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Diningroom")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Kitchen")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Hall")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Bedroom")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Walkin")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Office")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Jakobsroom")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Stairs")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Utility")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "Bathroom")
add_relationship(service_client, relationshipId, relationshipName, "GroundLevel", "SmallBathroom")
add_relationship(service_client, relationshipId, relationshipName, "Attic", "Atticroom")
add_relationship(service_client, relationshipId, relationshipName, "Basement", "Stairs")
add_relationship(service_client, relationshipId, relationshipName, "Basement", "Workshop")
add_relationship(service_client, relationshipId, relationshipName, "Basement", "Kåres_kontor")
add_relationship(service_client, relationshipId, relationshipName, "Basement", "Teenage")
add_relationship(service_client, relationshipId, relationshipName, "Garage_building", "Garage")
add_relationship(service_client, relationshipId, relationshipName, "Garage_building", "Shed")

print("adding sensors")

relationshipId = "dtmi:com:microsoft:iot:e2e:SmartHouse:Room:rel_has_HA_Temp_Sensor;1"
relationshipName = "rel_has_HA_Temp_Sensor"

add_sensor(service_client,"sensor.stue_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Livingroom", "sensor.stue_temperature")

add_sensor(service_client,"sensor.stue_temperature_2","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Livingroom", "sensor.stue_temperature_2")
add_relationship(service_client, relationshipId, relationshipName, "Diningroom", "sensor.stue_temperature_2")

add_sensor(service_client,"sensor.kokken_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Kitchen", "sensor.kokken_temperature")

add_sensor(service_client,"sensor.sovevaerelse_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Bedroom", "sensor.sovevaerelse_temperature")

add_sensor(service_client,"sensor.bryggers_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Utility", "sensor.bryggers_temperature")

add_sensor(service_client,"sensor.Walkin_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Walkin", "sensor.Walkin_temperature")

add_sensor(service_client,"sensor.stort_bad_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Bathroom", "sensor.stort_bad_temperature")

add_sensor(service_client,"sensor.stort_bad_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "SmallBathroom", "sensor.stort_bad_temperature")

add_sensor(service_client,"sensor.kontor_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Office", "sensor.kontor_temperature")

add_sensor(service_client,"sensor.jakob_vaerelse_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Jakobsroom", "sensor.jakob_vaerelse_temperature")

add_sensor(service_client,"sensor.kaelderrum_ved_kaelderdor_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Stairs", "sensor.kaelderrum_ved_kaelderdor_temperature")

add_sensor(service_client,"sensor.gang_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Hall", "sensor.gang_temperature")

add_sensor(service_client,"sensor.kaelderrum_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Teenage", "sensor.kaelderrum_temperature")

add_sensor(service_client,"sensor.pool_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Teenage", "sensor.pool_temperature")

add_sensor(service_client,"sensor.kaare_kontor_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Kåres_kontor", "sensor.kaare_kontor_temperature")

add_sensor(service_client,"sensor.workshop_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Workshop", "sensor.workshop_temperature")

relationshipId = "dtmi:com:microsoft:iot:e2e:SmartHouse:Area:rel_has_HA_Temp_Sensor;1"
relationshipName = "rel_has_HA_Temp_Sensor"

add_sensor(service_client,"sensor.83834d_temperature","Aqara",True, random.randint(17, 24))
add_relationship(service_client, relationshipId, relationshipName, "Driveway", "sensor.83834d_temperature")

relationship =  get_relationship(service_client,"Driveway","dtmi:com:microsoft:iot:e2e:SmartHouse:Area:rel_has_HA_Temp_Sensor;1_Driveway_sensor.83834d_temperature;1")
print (relationship)

relationships = list_relationships(service_client,"Driveway")
for relationship in relationships:
    print (relationship)

relationships = list_incoming_relationships(service_client,"Driveway")
for relationship in relationships:
    print (relationship)
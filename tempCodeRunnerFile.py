pest_data = {
    "name": "Caterpillar",
    "species": "Spodoptera litura",
    "pestType": "biting and chewing",
    "severity": "occasionally serious"
}

grapevine_stage_data = {
    "stage": "flowering and fruiting",
    "humidityImpact": "increases during high humidity"
}

vineyard_inspection_data = {
    "inspectionFrequency": "regular"
}

# Insert data into Weaviate
client.data_object.create(pest_data, "Pest")
client.data_object.create(grapevine_stage_data, "GrapevineStage")
client.data_object.create(vineyard_inspection_data, "VineyardInspection")
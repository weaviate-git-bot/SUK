import weaviate

auth_config = weaviate.AuthApiKey(api_key="AihSrsaKkWxquQmbQjYiWEUCihEGjljxnjPU")

client = weaviate.Client(
  url="https://cooptem-iisaxvp2.weaviate.network",
  auth_client_secret=auth_config
)


# schema = {
#     "classes": [
#         {
#             "class": "Pest",
#             "properties": [
#                 {"name": "name", "dataType": ["string"]},
#                 {"name": "species", "dataType": ["string"]},
#                 {"name": "pestType", "dataType": ["string"]},
#                 {"name": "severity", "dataType": ["string"]}
#             ]
#         },
#         {
#             "class": "GrapevineStage",
#             "properties": [
#                 {"name": "stage", "dataType": ["string"]},
#                 {"name": "humidityImpact", "dataType": ["string"]}
#             ]
#         },
#         {
#             "class": "VineyardInspection",
#             "properties": [
#                 {"name": "inspectionFrequency", "dataType": ["string"]}
#             ]
#         }
#     ]
# }

# # Create the schema in Weaviate
# client.schema.create(schema)


# pest_data = {
#     "name": "Caterpillar",
#     "species": "Spodoptera litura",
#     "pestType": "biting and chewing",
#     "severity": "occasionally serious"
# }

# grapevine_stage_data = {
#     "stage": "flowering and fruiting",
#     "humidityImpact": "increases during high humidity"
# }

# vineyard_inspection_data = {
#     "inspectionFrequency": "regular"
# }

# # Insert data into Weaviate
# client.data_object.create(pest_data, "Pest")
# client.data_object.create(grapevine_stage_data, "GrapevineStage")
# client.data_object.create(vineyard_inspection_data, "VineyardInspection")


query = """
{
  Get {
    Pest (
      nearText: {
        concepts: ["vine pests"]
      }
    ) {
      name
      species
    }
  }
}

"""

# Execute query
result = client.query.raw(query)
print(result)
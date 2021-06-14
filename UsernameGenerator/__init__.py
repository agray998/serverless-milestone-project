import logging
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = "insert_endpoint_here"
key = 'insert_primary_key_here'

client = CosmosClient(endpoint, key)

database_name = 'Random_User_Names'
database = client.create_database_if_not_exists(id=database_name)

container_name = 'User_Name_Container'
container = database.create_container_if_not_exists(
    id=container_name, 
    partition_key=PartitionKey(path="/Username"),
    offer_throughput=400
)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    chars = requests.get('https://argra-serverless-milestone-username-gen.azurewebsites.net/api/Service3?code=qm4naxbtsx5asYLW1jZ0wvNYfzRLiy5aJJGIGgbJAbadpdmRTByLHQ==')
    nums = requests.get('https://argra-serverless-milestone-username-gen.azurewebsites.net/api/Service2?code=U25trskQGRAafySm48syo1ilQSHZda/XLoj1FiCWSlGrcKaqLA63KQ==')
    u_name_list = []
    for i in range(5):
        u_name_list.append(chars.text[i])
        u_name_list.append(nums.text[i])
    u_name = ''.join(u_name_list)
    #container.create_item(body={"Username": u_name})
    return func.HttpResponse(f"New username is {u_name}", status_code=200)


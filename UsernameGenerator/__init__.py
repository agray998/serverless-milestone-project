import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    chars = requests.get('https://argra-serverless-milestone-username-gen.azurewebsites.net/api/Service3?code=qm4naxbtsx5asYLW1jZ0wvNYfzRLiy5aJJGIGgbJAbadpdmRTByLHQ==')
    nums = requests.get('https://argra-serverless-milestone-username-gen.azurewebsites.net/api/Service2?code=U25trskQGRAafySm48syo1ilQSHZda/XLoj1FiCWSlGrcKaqLA63KQ==')
    u_name_list = []
    for i in range(5):
        u_name_list.append(chars.text[i])
        u_name_list.append(nums.text[i])
    u_name = ''.join(u_name_list)
    return func.HttpResponse(f"New username is {u_name}")


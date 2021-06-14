import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return func.HttpResponse(''.join(random.choice(letters) for x in range(5)))
    

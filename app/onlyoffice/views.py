from django.shortcuts import render
from django.http import JsonResponse 
import json
import jwt
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def get_csrf_token(request):
    return JsonResponse({
        "token": get_token(request)
    },safe=False)

@csrf_exempt
def payload(request):
    data = json.loads(request.body)
    payload = json.loads(data.get("config"))
    print("payload",payload)
    jwt_secret = "qN7nd9IOwtONlqlTR2h5uOAZZzH6oDfg"
    jwt_token =  jwt.encode(payload, jwt_secret, algorithm='HS256')
    return JsonResponse({
        "token": jwt_token
    },safe=False)


@csrf_exempt
def callback(request):
    print("callback1",request.body.decode())
    data = json.loads(request.body.decode())
    print("callback",data)
    return JsonResponse({
        "error": 0
    },safe=False)


@csrf_exempt
def generate(request):
    from random import randint
    import uuid
    import requests
    response = requests.get("http://host.docker.internal:6080/example/download?fileName=LOREM IPSUM.docx")
    open("/app/data/lib/documentserver-example/files/192.168.65.1/doc.docx","wb").write(response.content)
    template_data = {
        "person_name": "JOSE RIZAL",
        "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "table":{
            "columns":["ID","NAME","VALUE"],
            "data":[
                [randint(0,99999)*100,"JUAN DELA CRUZ",str(uuid.uuid4())],
                [randint(0,99999)*100,"ANDRES BONIFACION",str(uuid.uuid4())],
                [randint(0,99999)*100,"EMILIO AGUINALDO",str(uuid.uuid4())],
                [randint(0,99999)*100,"JOSE RIZAL",str(uuid.uuid4())],
            ]
        }
    }

    return JsonResponse(template_data,safe=False)
from django.test import TestCase
from django.test import Client
import json

# Create your tests here.
class PayloadTestCase(TestCase):

    def test_create_payload(self):
        _client =  Client()
        response = _client.post("/onlyoffice/payload/",{
            "config":json.dumps({
                "document":{
                    "fileType": "docx",
                    "key": "Khirz6zTPdfd7",
                    "title": "LOREM IPSUM.docx",
                    "url": "http://host.docker.internal:6080/example/download?fileName=LOREM IPSUM.docx"
                }
            })
        })
        print("response",response.json())
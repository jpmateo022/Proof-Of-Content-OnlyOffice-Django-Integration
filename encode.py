import jwt

def encode(payload):
    return jwt.encode(payload, "qN7nd9IOwtONlqlTR2h5uOAZZzH6oDfg", algorithm='HS256')


print(encode(
    {
        "document":{
            "fileType": "docx",
            "key": "Khirz6zTPdfd7",
            "title": "LOREM IPSUM.docx",
            "url": "http://host.docker.internal:6080/example/download?fileName=LOREM IPSUM.docx"
        }
    }
))
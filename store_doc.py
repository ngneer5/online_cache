import requests

def store_doc(id, message, base):   
    url = "https://{}/messages/{}".format(base,id)
    if ((type(id) is int and type(message) is str)):
        data = {
            "id": id,
            "message": message,
        }
        return requests.post(url, data=data)
    else:
        return ("Invalid document")

import requests
import requests_cache #caches external API calls --> https://realpython.com/caching-external-api-requests/

requests_cache.install_cache("messages_cache", backend="memory", expire_after=30) #Caches the information

def retrieve_doc(url, id):
    response = requests.get(url+'/messages/{}'.format(id))
    if response.status_code != 200:
        print ("Resource Not Found " + str(response))
    else:
        data = response.json()
        id = data["id"]
        if (type(id) is int):       #Checks to see if id is an integer so that it can be considered valid
            return (data)
        else:
            return("Invalid id")

retrieve_doc('something', 123)
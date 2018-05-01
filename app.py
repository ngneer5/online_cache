from retrieve_doc import retrieve_doc
from store_doc import store_doc
from clear_cache import clear_cache

action = input("What would you like to do?")
if action == 'store':
    id = int(input("what's the id of your message?"))
    message = input("What information would you like to store")
    store_doc(id, message, "website_name")
elif action == 'retrieve':
    retrieve_doc("https://website_name", 2018)
elif action == 'clear':
    clear_cache()
else:
    print ("Invalid action")

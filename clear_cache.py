import requests_cache

def clear_cache():
    requests_cache.core.clear()
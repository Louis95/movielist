import requests
import requests_cache

"""
 All responses with headers and cookies will be transparently cached to movies_cache.sqlite database.
 
Take note of the expire_after option, which is set to 60 seconds. Since the movies API is frequently updated,
 we want to make sure we deliver the most up-to-date results. So, 60 seconds after the initial caching takes place, 
 the request will re-fire and cache a new set of results, delivering updated results.
"""
requests_cache.install_cache(cache_name='movies_cache', backend='sqlite', expire_after=60)


def make_get_request(url):
    """
     A helper function for get requests.

             Parameters:
                 url (string): URL for the new :class:`Request` object

             Returns:
                    response.json()  (json): json
     """
    response = requests.get(url)
    return response.json()

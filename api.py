import requests
import settings
import random
import json


word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
api_key = settings.giphy_api
url = "http://api.giphy.com/v1/gifs/search?q="


# grabs a random word from the freebsd.org dictionary. Then decodes byte to a string. For example:
# b'hilarious' -> hilarious
# Then takes that word and throws it into the giphy api query url.
def get_random_query():
    r = requests.get(word_site)
    words = r.content.splitlines()
    random_word = random.choice(words).decode('utf-8')
    random_query = url + random_word + "&api_key=" + api_key
    return random_query


# the url response will reply with json. we import the json library to parse and grab the url for the image.
def get_image_link(link):
    r = requests.get(link)
    api_response = json.loads(r.text)
    response = api_response['data']
    if not response:
        print('GIPHY API returned no results... finding another word...')
        get_image_link(get_random_query())
    else:
        return response[random.randint(0,24)]['images']['original']['url']


get_image_link(get_random_query())


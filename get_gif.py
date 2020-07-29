import json
import requests
import urllib.request

def get_gif_url (name, cat):

    tenor = []
    giphy = []

    #tenor API
    # set the apikey and limit
    apikey = "KOBZBCHIOB9T" 
    lmt = 5

    search_term = cat

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_5gifs = json.loads(r.content)
    else:
        top_5gifs = None

    # extract tenor GIF
    for GIFs in top_5gifs['results']:
        tenor.append(GIFs['media'][0]['tinygif']['url'])

    #giphy api
    cat_process = cat.replace(' ', '+')
    url = "http://api.giphy.com/v1/gifs/search?q=" + cat_process + "&api_key=g7oEHBRcYKzCSiDBGD5DcLuoB7jF7tW7&limit=5"
    data = json.loads(urllib.request.urlopen(url).read())

    # extract giphy GIF
    for GIFs in data['data']:
        giphy.append(GIFs['images']['original']['url'])

    if name=='tenor':
        return tenor
    else:
        return giphy

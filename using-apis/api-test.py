# Using API Homework
#     This  program can retrive results from GIPHY API, 
#     parse the results (JSON in this case) and manage the potential errors.
#     @author Yuting Su(suy@carelton.edu)
#     @author Starr Wang(wangy3@carleton.edu)
#      2018-09-30

import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import sys

def find_list_of_gifs_by_key():
    '''
    Returns a list of 10 gif image related to key word. 
    The gif images are represented as
    dictionaries of the form
    
       {'id':id_of_gif, 'url':url_of_gif}

    For example, the results for find_list_of_gifs_by_key with keyword 'dog'
    would be:

       [{'url': 'https://giphy.com/gifs/4Zo41lhzKt6iZ8xff9', 'id': '4Zo41lhzKt6iZ8xff9'}, 
       {'url': 'https://giphy.com/gifs/morning-perfect-loops-bbshzgyFQDqPHXBo4c', 'id': 'bbshzgyFQDqPHXBo4c'}...]

    The language parameter must be a 3-letter ISO language code
    (e.g. 'eng', 'fra', 'deu', 'spa', etc.).

    Raises exceptions when errors occur.
    '''
    api_instance = giphy_client.DefaultApi()
    api_key = 'zU47hZF9SKUIc9AtzAhp4sWSZQudHAsU' # str | Giphy API Key.
    limit = 10 # int | The maximum number of records to return. (optional) (default to 25)
    offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    rating = 'g' # str | Filters results by specified rating. (optional)
    lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
    q = sys.argv[2] # str | Search query term or prhase.
    try: 
        # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
        info_list = []
        for image in api_response.data:
          individual_dictionary = {"id": image.id, "url": image.url}
          info_list.append(individual_dictionary)
        print(info_list)

    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
    

def find_details_of_image_by_id():
    '''
    Returns details about one gif image speficied by id. 
    The information are represented as
    dictionaries.

    For example, the results for find_details_of_image_by_id with id 'mCRJDo24UvJMA'
    would be:

       {'frames': '4',
         'height': '362',
         'mp4': 'https://media2.giphy.com/media/mCRJDo24UvJMA/giphy.mp4',
         'mp4_size': '30656',
         'size': '78285',
         'url': 'https://media2.giphy.com/media/mCRJDo24UvJMA/giphy.gif',
         'webp': 'https://media2.giphy.com/media/mCRJDo24UvJMA/giphy.webp',
         'webp_size': '99552',
         'width': '500'}
    '''
    api_instance = giphy_client.DefaultApi()
    api_key = 'zU47hZF9SKUIc9AtzAhp4sWSZQudHAsU' # str | Giphy API Key.
    gif_id = sys.argv[2]
    try: 
        # Get GIF by ID Endpoint
        api_response = api_instance.gifs_gif_id_get(api_key, gif_id)
        pprint(api_response.data.images.original)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_gif_id_get: %s\n" % e)


def main():
    if len(sys.argv) != 3:
        print("This is a program that uses GIPHY API to help you find gifs image.")
        print("If you want to search for details about a specific image using id, use this format: python3 api-test.py id id_example")
        print("If you want to search for a list of 10 images using key word, use this format: python3 api-test.py search key_example")

    else:
        if sys.argv[1] == "search":
            find_list_of_gifs_by_key()

        elif sys.argv[1] == "id": 
            find_details_of_image_by_id()

        else:
            print("This is a program that uses GIPHY API to help you find gifs image.")
            print("If you want to search for details about a specific image using id, use this format: python3 api-test.py id id_example")
            print("If you want to search for a list of 10 images using key word, use this format: python3 api-test.py search key_example")

main()
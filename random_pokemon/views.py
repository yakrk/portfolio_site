from django.shortcuts import render
import requests
import random
from django.contrib import messages


def random_pokemon(request):
    # get pokemon name of the day
    pokemon_id = random.randint(1, 1010)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    try:
        pokemon_response = requests.get(pokemon_url, timeout=2000)
    except requests.exceptions.SSLError:
        messages.error(request, "Exceeded requests for today.")
        return render(request, "random_pokemon/random-pokemon.html")
    pokemon_json = pokemon_response.json()

    pokemon_name = pokemon_json["name"]
    pokemon_type_dict = pokemon_json['types']

    WIKI_URL = "https://en.wikipedia.org/w/api.php"

    # get pokemon image file name if any
    params = {
        "action": "query",
        "format": "json",
        "titles": pokemon_name,
        "prop": "images"
    }

    result = requests.Session().get(url=WIKI_URL, params=params)
    data = result.json()
    pages = data['query']['pages']
    image_list = []
    for value in pages.values():
        try:
            for img in value['images']:
                image_list.append(img)
        except KeyError:
            image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/\
                No_image_available.svg/450px-No_image_available.svg.png"
    # get image url
    if image_list:
        params = {
            "action": "query",
            "format": "json",
            "titles": image_list[0]['title'],
            "prop": "imageinfo",
            "iiprop": "url"
        }
        result = requests.Session().get(url=WIKI_URL, params=params)
        data = result.json()
        pages = data['query']['pages']
        for value in pages.values():
            image_url = value['imageinfo'][0]['url']
    context = {
        "image_url": image_url,
        "pokemon_name": pokemon_name.capitalize(),
        "pokemon_id": pokemon_id,
        "pokemon_types": pokemon_type_dict,
    }
    return render(request, "random_pokemon/random-pokemon.html", context)

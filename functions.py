import requests


def int_in_range(x: int, y: int, z: int):
    """
    returns true, if z in range of [x , y]
    """
    if x <= z <= y:
        return True
    else:
        return False


def get_pokemon_name(Pokémon_number: int):
    """
    returns the name of Pokémon number x.
    """
    url = "https://pokeapi.co/api/v2/pokemon/" + str(Pokémon_number)
    response = requests.get(url)
    data = response.json()
    return data["name"].title()


def get_pokemon_weight(Pokémon_name: str):
    """
    returns the weight of Pokémon named x.
    """
    url = "https://pokeapi.co/api/v2/pokemon/" + Pokémon_name.lower()
    response = requests.get(url)
    data = response.json()
    return data["weight"]


def string_in(x: str, y: str):
    """
    returns true if x contains y.
    """
    if y in x:
        return True
    else:
        return False


def list_of_ints_in_range(l_args: list, min_num: int, max_num: int):
    """
    returns true, if all the elements in the list are in the range of [x, y]
    """
    for num in l_args:
        if not int_in_range(min_num, max_num, int(num)):
            return False
    return True

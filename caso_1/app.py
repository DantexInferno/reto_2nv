from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route("/")
def index():
  
  data = get_pokemon_image()

  return render_template('index.html', pokemones=data)


@app.route("/get_abilities")
def get_abilities():
  pokemon = request.args.get('name')
  
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

  if response.status_code == 200:
      response = response.json()

      abilities = response["abilities"]
  abilities = json.dumps(abilities)

  return abilities


#call to the pokeapi to get the image of the pokemon
def get_pokemon_image():
  
  pokemones = ["SPEAROW", "FEAROW", "EKANS", "ARBOK", "PIKACHU", "RAICHU", "SANDSHREW", "SANDSLASH", "NIDORINA"]

  pokemon_list = []

  for pokemon in pokemones:

    pokemones_dict = {}
    pokemon = pokemon.lower()
    pokemones_dict["name"] = pokemon
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    if response.status_code == 200:
      response = response.json()
      pokemones_dict["image"] = response["sprites"]["other"]["official-artwork"]["front_default"]
      
    pokemon_list.append(pokemones_dict)

  return pokemon_list

if __name__ == '__main__':
  app.run(debug=True)
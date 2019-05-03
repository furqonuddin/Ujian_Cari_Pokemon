from flask import Flask, render_template, jsonify, make_response, request
import json
import requests


app = Flask(__name__)

# =============================================================
@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/hasil', methods = ['POST', 'GET'])
def hasil():
    pokemon = request.form['namapokemon']
    url = 'https://pokeapi.co/api/v2/pokemon/'
    

    try:
        data = requests.get(url + pokemon.lower())
        nama = data.json()['name']
        gambar = data.json()['sprites']['front_default']
        no_id = data.json()['id']
        tinggi = data.json()['height']
        berat = data.json()['weight']

        profil = {
            'nama' : nama,
            'gambar' : gambar,
            'id' : no_id,
            'tinggi' : tinggi,
            'berat' : berat
        }

        return render_template(
            'hasil.html',
            profil = profil
        )

    except:
        return render_template('NotFound.html')        


# not found display
@app.errorhandler(404)
def tidakfound(error):                                                 
    return make_response('<h1>NOT FOUND (404)</h1>')


if __name__ == '__main__':
    app.run(debug = True) 
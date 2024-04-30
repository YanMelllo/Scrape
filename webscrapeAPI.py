from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/webscrape', methods=['GET'])
def scrape():
    url = 'http://www.bianca.com'
    response = requests.get(url)

    sopa = BeautifulSoup(response.text, "html.parser")

    frase_corpo = sopa.find("h1")

    data = frase_corpo.text

    print(data)
    fim = {'data': data}
    
    return jsonify(fim), 200



if __name__ == '__main__':
    app.run()














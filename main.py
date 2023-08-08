import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load cocktail data from JSON file
with open('cocktails.json', 'r') as file:
    cocktails = json.load(file)

# Route to search for cocktails
@app.route('/search', methods=['GET'])
def search_cocktails():
    keyword = request.args.get('q', '')
    result = [cocktail for cocktail in cocktails if keyword.lower() in cocktail['name'].lower()]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

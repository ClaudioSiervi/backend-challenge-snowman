from flask import Flask, jsonify

app = Flask(__name__)

# tourist spot categories = ("Park", "Museum", "Theater", "Monument")
categories = [
        {
            "id": 1,
            "name": "Park",
            "description": "Some symple text..."
        },
        {
            "id": 2,
            "name": "Museum",
            "description": "Some symple text..."
        },
]

# tourist spot filds = (picture, name, geographical location, category) 
tourist_spots = [
    {
        'name': 'Passeio Público',
        'gps' : [],
        'category': categories[0]['name'],
        'pictures' : [
            {
                "name": "name-picture",
                "content": "string-represent-picture"
            }
        ]
    },
    {
        'name': 'Museu Oscar Niemeyer',
        'gps' : [],
        'category': categories[1]['name'],
        'pictures' : [
            {
                "name": "name-picture",
                "content": "string-represent-picture"
            }
        ]
    }
]



# POST /tourist-spots {name:}
@app.route("/tourist-spot", methods = ["POST"])
def create_tourist_spot():
    pass

# GET /tourist-spots
@app.route("/tourist-spot", methods = ["GET"])
def get_tourist_spot():
    return jsonify({"tourist_spots": tourist_spots})


app.run(debug=True, port=4999)
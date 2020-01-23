from flask import Flask, jsonify, request

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



# POST /tourist-spot {name:}
@app.route('/tourist-spot', methods = ['POST'])
def create_tourist_spot():
    # this request creates a new tourist spot into tourist-spot resource
    request_data = request.get_json()
    new_tourist_spot = {
        "name": request_data['name'],
        "gps": request_data['gps'],
        "category": request_data['category'],
        "pictures": [] 
        }
    tourist_spots.append(new_tourist_spot)   
    return jsonify(new_tourist_spot)


# GET /tourist-spots
@app.route("/tourist-spot", methods = ["GET"])
def get_tourist_spots():
    return jsonify({"tourist_spots": tourist_spots})


# GET /tourist-spot/<string:name>
@app.route("/tourist-spot/<string:name>", methods = ["GET"])
def get_tourist_spot(name):
    for tourist_spot in tourist_spots:
        if tourist_spot['name'] == name:
            return jsonify(tourist_spot)
    return jsonify({'messege': "tourist spot not found"})



app.run(debug=True, port=4999)
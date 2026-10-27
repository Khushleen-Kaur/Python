from flask import Flask, jsonify, request

app = Flask(__name__)

songs = {
    1: { "song_name": "Perfect", "singer_name": "Ed Sheeran" },
    2: { "song_name": "Until I Found You", "singer_name": "Stephen Sanchez" }
}

@app.route("/songs", methods=["GET"])
def get_songs():
    return jsonify(songs), 200

@app.route("/songs", methods=["POST"])
def post_song():
    response = request.get_json()
    if "song_name" not in response or "singer_name" not in response:
        print("Json validation error: one (all) field missing.")
        return "Json validation error: one (all) field missing.", 400
    
    if not response["song_name"] or not response["singer_name"]:
        print("Data validation error: one (all) field empty.")
        return "Data validation error: one (all) field empty.", 400

    new_song = {
        "song_name": response["song_name"],
        "singer_name": response["singer_name"]
    }
    id = max(songs.keys(),default=0) + 1
    songs[id] = new_song

    return jsonify(new_song) , 201

@app.route("/songs/<int:id>", methods=["PUT"])
def update_song(id: int):
    response = request.get_json()

    if(id not in songs): 
        print("Id does not exists..")
        return

    updated_song = {
        "song_name": response["song_name"],
        "singer_name": response["singer_name"]
    }

    songs[id] = updated_song

    return jsonify(updated_song) ,200

@app.route("/songs/<int:id>", methods=["PATCH"])
def update_singer_name(id: int):
    response = request.get_json()
    
    if("singer_name" in response): 
        songs[id]["singer_name"] = response["singer_name"]
    elif("song_name" in response): 
        songs[id]["song_name"] = response["song_name"]
    else: 
        print("Invalid request.. Please give song name or singer name..")

    return jsonify(songs[id]) ,200

@app.route("/songs/<int:id>", methods=["DELETE"])
def delete_song(id: int):
    if(id not in songs):
        print("Id dont exist..")
        return
    songs.pop(id)
    return jsonify(songs) ,200
    

if __name__ == "__main__":
    app.run(debug=True)
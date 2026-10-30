import requests
url = "http://127.0.0.1:5000/songs"

def post_songs():
    try:
        song_name = input("Enter Song name: ")
        singer_name = input("Enter Singer name: ")

        response = requests.post(url,  json={
            "song_name": song_name,
            "singer_name": singer_name
        }, timeout=10)

        response.raise_for_status()
        print(response.json())
        print("Status:", response.status_code)
        print("Posted Successfully!")

    except requests.exceptions.Timeout as to:
        print(to)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.RequestException as re:
        print(re)

if __name__ == "__main__":
    post_songs()
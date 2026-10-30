import requests
url = "http://127.0.0.1:5000/songs"

def test_update_song_name():
    try:
        id = int(input("Enter Song ID: "))
        song_name = input("Enter Song name: ")

        response = requests.patch(
            f"{url}/{id}",  
            json={"song_name": song_name}, 
            timeout=10 )

        response.raise_for_status()
        print(response.json())
        print("Status:", response.status_code)
        print("Updated Successfully!")

    except requests.exceptions.Timeout as to:
        print(to)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.RequestException as re:
        print(re)

if __name__ == "__main__":
    test_update_song_name()
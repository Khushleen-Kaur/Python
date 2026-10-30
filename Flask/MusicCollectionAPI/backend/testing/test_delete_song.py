import requests
url = "http://127.0.0.1:5000/songs"
    
def test_delete_song():
    try:
        id = int(input("Enter Song ID: "))
        response = requests.delete(f"{url}/{id}", timeout=10)

        response.raise_for_status()
        print(response.json())
        print("Status:", response.status_code)

    except requests.exceptions.Timeout as to:
        print(to)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.RequestException as re:
        print(re)
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    test_delete_song()
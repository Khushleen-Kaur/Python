import requests

url = "http://127.0.0.1:5000/songs"
def view():
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    print("------ List of Songs -------")
    for id, song in response.json().items():
        print(f"ID: {id}")
        print(f"Song Name: {song.get('song_name')}")
        print(f"Singer Name: {song.get('singer_name')}")

def post():
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

def update_song_name():
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

def update_singer_name():
    id = int(input("Enter Song ID: "))
    singer_name = input("Enter Singer name: ")

    response = requests.patch(
        f"{url}/{id}",  
        json={"singer_name": singer_name}, 
        timeout=10 )

    response.raise_for_status()
    print(response.json())
    print("Status:", response.status_code)
    print("Updated Successfully!")

def update_song():
    id = int(input("Enter Song ID: "))
    song_name = input("Enter Song name: ")
    singer_name = input("Enter Singer name: ")

    response = requests.put(
        f"{url}/{id}",  
        json={
        "song_name": song_name,
        "singer_name": singer_name}, 
        timeout=10)

    response.raise_for_status()
    print(response.json())
    print("Status:", response.status_code)
    print("Updated Successfully!")

def update():
    while(True):
        print("----- Update Music Collection ------")
        print("1. Update Song Name")
        print("2. Update Singer Name")
        print("3. Update Song")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if(choice == 4): break
        match(choice):
            case 1:
                update_song_name()
            case 2:
                update_singer_name()
            case 3:
                update_song()
            case _:
                print("Please, Enter a valid choice..")

def delete():
    id = int(input("Enter Song ID: "))
    response = requests.delete(f"{url}/{id}", timeout=10)

    response.raise_for_status()
    print(response.json())
    print("Status:", response.status_code)

def menu():
    while(True):
        print("----- Music Collection Manager ------")
        print("1. View Songs")
        print("2. Add Song")
        print("3. Update Song")
        print("4. Delete Song")
        print("5. Exit")
        try:
            choice = int(input("Enter choice: "))
            if(choice == 5): break

            match(choice):
                case 1:
                    view()
                case 2:
                    post()
                case 3:
                    update()
                case 4:
                    delete()
                case _:
                    print("Please, enter a valid choice...")

        except ValueError as ve:
            print("Please, Enter a valid data..")
            print(ve)
        except requests.exceptions.Timeout as to:
            print(to)
        except requests.exceptions.HTTPError as e:
            print(e)
        except requests.exceptions.RequestException as re:
            print(re)

if __name__ == "__main__":
    menu()
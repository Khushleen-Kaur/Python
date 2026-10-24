import requests

url = "https://jsonplaceholder.typicode.com/posts"

def getPosts():
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print("------------------ Posts --------------------")
    for user in data:
        print("\nUser ID:", user['userId'])
        print("ID:" , user['id'])
        print("Title:" , user['title'])
        print("Body:" , user['body'])
    
    print("\nAll posts found!")
    print("Status Code:", response.status_code)


def postPosts():
    userId = int(input("Enter User Id: "))
    title = input("Enter Title: ")
    body = input("Enter Body: ")
    post = {
        'userId' : userId,
        'title' : title,
        'body' : body,
    }
    response = requests.post(url, json=post, timeout=10)
    response.raise_for_status()
    print("\nPosted successfully!")
    print("Status Code:", response.status_code)
    

def putPost():
    userId = int(input("Enter User Id: "))
    id = int(input("Enter Id: "))
    title = input("Enter Title: ")
    body = input("Enter Body: ")
    newpost = {
        'userId' : userId,
        'id' : id,
        'title' : title,
        'body' : body,
    }
    response = requests.put(f"{url}/{userId}", json=newpost, timeout=10)
    response.raise_for_status()
    print("\nPost updated successfully!")
    print("Status Code:", response.status_code)

def deletePost():
    userId = int(input("Enter User Id: "))

    response = requests.put(f"{url}/{userId}", timeout=10)
    response.raise_for_status()
    print("\nPost deleted successfully!")
    print("Status Code:", response.status_code)


def patchTitle():
    userId = int(input("Enter User ID: "))
    newTitle = input("Enter new title: ")
    
    response = requests.patch(
        f"{url}/{userId}", 
        json={"title": newTitle},
        timeout=10
    )
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Post Updated successfully!")

def patchBody():
    userId = int(input("Enter User ID: "))
    newBody = input("Enter new body: ")
    
    response = requests.patch(
        f"{url}/{userId}", 
        json={"body": newBody},
        timeout=10
    )
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Post Updated successfully!")



def menu():
    while(True):
        print("------------- Posts Manager ---------------")
        print("1. View Posts")
        print("2. Add Post")
        print("3. Update Post")
        print("4. Update Posts Title")
        print("5. Update Posts Body")
        print("6. Delete Post")
        print("7. Exit")
        try:
            choice = int(input("Enter choice: "))
            if choice == 7:
                print("Exiting...")
                break
            match choice:
                case 1:
                    getPosts()
                case 2:
                    postPosts()
                case 3:
                    putPost()
                case 4:
                    patchTitle()
                case 5:
                    patchBody()
                case 6:
                    deletePost()
                case _:
                    print("Please, Enter a valid choice..")

        except requests.exceptions.HTTPError as e:
            print(e)
        except requests.exceptions.Timeout as to:
            print(to)
        except requests.exceptions.RequestException as re:
            print(re)
        except ValueError as ve:
            print("Please, Enter valid data..", ve)

if __name__ == "__main__":
    menu()
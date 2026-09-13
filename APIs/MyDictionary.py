import requests

word = input("Enter word : ")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(url).json()
print(f"Word - {response[0]['word']}\nMeaning - {response[0]['meanings'][0]['definitions'][0]['definition']}")

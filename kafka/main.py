import requests

URL = "https://official-joke-api.appspot.com/random_joke"

try:
    req = requests.get(URL)
    res = req.json()
    if res:
        print(f"__Setup__\n{res['setup']}\n__Punchline__\n{res['punchline']}")
except Exception as e:
    print(f"Error occured: {e}")
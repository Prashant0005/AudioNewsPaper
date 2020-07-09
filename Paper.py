import requests
import json
from win32com.client import Dispatch
def speak(str):
    sun = Dispatch("SAPI.SpVoice")
    sun.speak(str)

url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=f4b6c5fb93624d51bb3667cbbc619d91')
response = requests.get(url)
r=response.json()
# sun=Dispatch("SAPI.SpVoice")
print("Welcome to the Live News Paper")
speak("Welcome to the Live News Paper")
arts=r['articles']
print("Lets look at the headlines first")
speak("Lets look at the headlines first")
for i in arts:
    print(i['title'])
    speak(i['title'])

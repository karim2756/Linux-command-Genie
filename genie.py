import requests

import json

import sys

import emoji

# Replace with your actual API key

API_KEY = "YOUR_API_KEY"



text=""

if len(sys.argv) > 1:



    text = sys.argv[1]

else : exit()



# Content to send in the request body

content = {

  "contents": [

    {

      "parts": [

        {

            "text":"if the question is related to linux or terminal answer it with 2 different examples usage like this:how to create a new directory? Genie: To create a new directory, you can use the 'mkdir' command.\nExample usage: mkdir ABC \nmkdir A/B/C -p\n. nad if the question is not related to linux or terminal say: I’m sorry, I only answer bash specific questions\n.like this: What is 5 + 5? Genie: I’m sorry, I only answer bash specific questions\n.  now the question is: "+text

        }

      ]

    }

  ]

}



# URL for the generation endpoint

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY



# Set headers for the request

headers = {"Content-Type": "application/json"}



# Send POST request with JSON content

response = requests.post(url, headers=headers, json=content)



# Check for successful response

if response.status_code == 200:

  # Parse the JSON response

  data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')

  print("Genie: "+data)

  print("\n"+emoji.emojize(":heart_suit:")+" "+emoji.emojize(":folded_hands:")+" Thanks for using Genie "+emoji.emojize(":folded_hands:")+emoji.emojize(":heart_suit:")+"\n")

else:

  print("Error:", response.status_code, response.text)


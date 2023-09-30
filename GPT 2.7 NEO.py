# Major part of this code is taken from https://huggingface.co/blog/few-shot-learning-gpt-neo-and-inference-api

import json
import requests


API_TOKEN = "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"

def query(payload='',parameters=None,options={'use_cache': False}):
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    body = {"inputs":payload,'parameters':parameters,'options':options}
    response = requests.request("POST", API_URL, headers=headers, data= json.dumps(body))
    try:
      response.raise_for_status()
    except requests.exceptions.HTTPError:          
        return "Error:"+" ".join(response.json()['error'])
    else:
      return response.json()[0]['generated_text']

parameters = {
    'max_new_tokens':25,  # number of generated tokens
    'temperature': 0.5,   # controlling the randomness of generations
    'end_sequence': "###" # stopping sequence for generation
}

girdi="""
if "uygulama aç" in audio :
    function.open_app()

if "googleda ara" in audio :
    function.open_google()

if "not al" or "not et" in audio :
    function.write_note()

if "telefona bağlan" in audio :
    function.phonecam_connect()
###
Text:if "bugün ne" in audio :
Code:"""            

data = query(girdi, parameters)

print(data)


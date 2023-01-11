import openai
from analysis import save_response

from config import OPENAIKEY, FREEMODE

openai.api_key = OPENAIKEY
FREEQUERYMODE = FREEMODE

# General chat query
def generalQuery(command):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=command,
    temperature=0.5,
    max_tokens=20,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    # Save response
    save_response(response["choices"][0]["text"])

    return None


#Dalle Image query
def imageQuery(command):
    response = openai.Image.create(
    prompt=command,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    save_response(image_url)

    return image_url
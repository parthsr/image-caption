import requests
from gtts import gTTS



subscription_key = "key"
assert subscription_key

vision_analyze_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze"

img_filename = 'simon.jpeg'
with open(img_filename, 'rb') as f:
    img_data = f.read()
headers  = {'Ocp-Apim-Subscription-Key': subscription_key,
    		'Content-Type': 'application/octet-stream',}
params   = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(vision_analyze_url, headers=headers, params=params, data=img_data)
response.raise_for_status()
analysis = response.json()

image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print(image_caption)

tts = gTTS(text=image_caption, lang='en', slow=True)
tts.save("hello.mp3")
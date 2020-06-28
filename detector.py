from io import BytesIO
import os, requests, uuid, json, re
from base64 import b64decode

prediction_key = os.environ['CUSTOM_MODEL_PRED_KEY']
prediction_resource_id = os.environ['CUSTOM_MODEL_ID']
prediction_endpoint = os.environ['CUSTOM_MODEL_PRED_ENDPOINT']

def transform_url(data):
    response = requests.get(data['text'])
    image = BytesIO(response.content)
    return get_diagnosis(image)

def transform_webcam(data):
    image = BytesIO(b64decode(re.sub("data:image/jpeg;base64", '', data['text'])))
    return get_diagnosis(image)

def get_diagnosis(image):
    url = prediction_endpoint,

    headers = {
        'Content-Type': 'application/octet-stream',
        'Prediction-Key': prediction_key,
    }

    body = image

    response = requests.post(url, headers=headers, data=body)
    print(response.json())
    return [(i["tagName"], i["probability"]) for i in response.json()["predictions"]]

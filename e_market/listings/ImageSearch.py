import io
import os

from google.cloud import vision, vision_v1
from google.cloud.vision_v1 import types
import pandas as pd


def get_client():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Youssef\Desktop\e-market-system-token.json'
    client = vision.ImageAnnotatorClient()
    return client


class TextDetection():

    def __init__(self,path):
        self.path = path
        self.client = get_client()

    def get_text_detection(self):
        img_url = 'https://smallbiztrends.com/wp-content/uploads/2019/07/yoda-star-wars-hard-work-quote.png'
        image = vision_v1.types.Image()
        image.source.image_uri = img_url
        response = self.client.text_detection(image=image)
        texts = response.text_annotations

        df = pd.DataFrame(columns=['locale', 'description'])
        for text in texts:
            df = df.append(
                dict(locale=text.locale,
                     description=text.description
                     ),
                ignore_index=True
            )

        descriptions = df['description'][0].split()

        return descriptions



class LogoDetection():

    def __init__(self,path,name):
        self.path = path
        self.name = name
        self.client = get_client()

    def get_logos(self):
        FILE_NAME = self.name
        FOLDER_PATH = self.path

        with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
            content = image_file.read()

        image = vision_v1.types.Image(content=content)

        response = self.client.logo_detection(image=image)
        logos = response.logo_annotations
        search_logos=[]
        for logo in logos:
            search_logos.append(logo.description)

        return search_logos


class ObjectDetection():

    def __init__(self,path):
        self.path = path
        self.client = get_client()


    def get_objects(self):
        FILE_NAME = 'fruits and vegetables.jpg'
        FOLDER_PATH = r'C:\Users\Youssef\Desktop\LAU\Software_Engineering\Project\PHOTOS'

        with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
            content = image_file.read()

        image = vision_v1.types.Image(content=content)
        response = self.client.object_localization(image=image)
        loa = response.localized_object_annotations

        df = pd.DataFrame(columns=['name'])

        for obj in loa:
            df = df.append(
                dict(
                    name=obj.name
                ),
                ignore_index=True
            )

        return df


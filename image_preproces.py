import io
import json
import base64

from PIL import Image
from loguru import logger


def main():

    with open('./images.json', 'r') as hand:
        images = json.load(hand)

    for image in images['images']:

        image_decoded = io.BytesIO(base64.standard_b64decode(image))
        
        image = Image.open(image_decoded)
        image.save("image.png")



if __name__ == '__main__':
    main()
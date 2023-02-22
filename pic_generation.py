from base64 import b64decode
from io import BytesIO
import datetime

from printutils import log
import openai
from PIL import Image, ImageDraw
import numpy
import blend_modes
import cv2
import os


def generate_image(prompt: str, key: str) -> str:
    log("Generating the image...")
    openai.api_key = key
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="b64_json"
    )
    log(done=True)

    return parse_image(response)


def parse_image(response: dict) -> str:
    log("Parsing the image...")
    image = Image.open(BytesIO(b64decode(response["data"][0]["b64_json"])))
    # draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype('fonts/papercut.ttf', 290)
    # draw_text_center(*image.size, draw, "KN", font)

    image = paste_logo(image, Image.open('./images/kn.png'))

    path = "./images/" + datetime.datetime.now().strftime("%d.%m.%Y - %H.%M")
    os.makedirs(f"{path}/sliced", exist_ok=True)

    image.save(f'{path}/img.png')

    log(done=True)
    slice(image, f"{path}/sliced")

    return path


def slice(image: Image, save_path: str):
    log('Slicing...')
    img = numpy.array(image)
    nth = 0

    for r in range(0, 3):
        for c in range(0, 3):
            nth += 1
            file_name = f"{save_path}/img{nth}.png"
            cv2.imwrite(file_name, img[r*341:r*341+341, c*341:c*341+341, :])
    log(done=True)


def draw_text_center(width, height, draw: ImageDraw, text: str, font):
    draw.text((width / 2, height / 2 - 50), text, font=font, anchor="mm")


def paste_logo(image: Image, to_paste: Image) -> Image:
    base = numpy.array(image)
    base = cv2.cvtColor(base, cv2.COLOR_RGB2RGBA)
    base = base.astype(float)

    logo = numpy.array(to_paste)
    logo = cv2.cvtColor(logo, cv2.COLOR_RGB2RGBA)
    logo = logo.astype(float)

    output = blend_modes.difference(base, logo, 1.0)
    output = numpy.uint8(output)

    return Image.fromarray(output)

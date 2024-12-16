import os
from PIL import Image 
from pytesseract import pytesseract
from tqdm import tqdm
import sys

folder = os.path.dirname(os.path.abspath(__file__)) + sys.argv[1]
pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
rewards = []

with open(os.path.dirname(os.path.abspath(__file__)) + sys.argv[2], 'w') as file:
    for image in tqdm(sorted(os.listdir(folder))):
        img = Image.open(folder + image) 
        img = img.crop((0, 0, 169, 25))
        reward = pytesseract.image_to_string(img, config='--psm 10 -c tessedit_char_whitelist=(-.0123456789')
        timestamp = image.split('.')[0]
        if len(reward) == 13 or len(reward) == 14:
            tqdm.write(timestamp + ': ' + reward)
        else:
            reward = '-1.0000000000\n'
        rewards.append(reward)
        file.write(timestamp + ':' + str(reward))

file.close()

#169x25
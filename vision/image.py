import os
import base64

def save_image(image_in_base64, username):
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    IMAGE_ROOT = os.path.join(PROJECT_PATH, 'uploads', username, 'fundus_images' , 'upload.jpg')

    try:
        os.remove(IMAGE_ROOT)
    except:
        pass

    os.makedirs(os.path.join(PROJECT_PATH, 'uploads', username, 'fundus_images'), exist_ok=True)

    image_in_base64
    imgdata = base64.b64decode(image_in_base64)
    filename = os.path.join(PROJECT_PATH, 'uploads', username, 'fundus_images', 'upload.jpg')

    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

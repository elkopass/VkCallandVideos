import vk_api
from PIL import Image, ImageDraw, ImageFont
import os

from urllib.request import urlopen
from conf50 import user_tok, grUpId



videoScenes = []

grUpId = grUpId * -1
grUpId = -45745333
d = vk_api.VkApi(token=user_tok).get_api().video.get(owner_id=grUpId, count=8, v=5.131)
for i in d["items"]:
    videoScenes.append([f'{i["image"][0]["url"]}', f'{i["title"]}', f'{i["views"]}'])

videoScenes.sort(key=lambda x: int(x[2]), reverse=True)

print(videoScenes)

for i in range(len(videoScenes)):
    s = videoScenes[i][0]
    im = Image.open(urlopen(f'{s}'))
    # Откроет изображение в новом окне
    im = im.resize((512, 512))
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype(font='OpenSans-Medium.ttf', size=80)
    draw_text.text(
        (0, 0),
        f'{videoScenes[i][1]}',
        fill=('#1C0606'),
        font=font
    )
    d
    im.save(f'photos/img{i}.png')

import cv2
import os

image_folder = 'photos'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 0.2, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


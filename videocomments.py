import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
from datetime import date
from threading import Thread
import time
import re
answers = dict()

answers["Б.мыч*"] = 0
answers["Нет"] = 0 


from conf40 import owner_id, video_id, user_tok
liveGuys = []
# owner_id = -83906457
# video_id = 456245363
d = vk_api.VkApi(token = user_tok).get_api().video.getComments(owner_id = owner_id, video_id = video_id, v = 5.131)
for i in d["items"]:
    print(i)
    txt = i["text"]
    if((i["from_id"] in liveGuys) == False):
        for j in answers.keys():
            x = re.search(j, txt)
            if x:
                answers[j] += 1
                print(type(i["from_id"]))
                liveGuys.append(i["from_id"])

print(answers)
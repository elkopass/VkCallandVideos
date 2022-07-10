import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import vk_api
from datetime import datetime
from datetime import date
from threading import Thread
import time


from conf30 import user_tok, grUpId
liveStream = []

grUpId = grUpId*-1
d = vk_api.VkApi(token = user_tok).get_api().video.get(owner_id = grUpId, v = 5.131)
for i in d["items"]:
    
    if(((i['id'] in liveStream) == False) and i["type"] == "live"):
        liveStream.append(i['id'])

    

def loop():
    while True:
        d = vk_api.VkApi(token = user_tok).get_api().video.get(owner_id = grUpId, v = 5.131)
        for i in d["items"]:
            if(((i['id'] in liveStream) == False) and i["type"] == "live"):
                liveStream.append(i['id'])
                print("Начался новый стрим!")
                            
        
        time.sleep(1)


for _ in range(1):
    t = Thread(target=loop)
    t.daemon = True
    t.start()


try:
    while True:
        time.sleep(0.05)
except KeyboardInterrupt:
    print("Stop script")
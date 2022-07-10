from email import message
from os import access
import random 
import requests
import vk_api
from pprint import pprint
from vk_api.utils import get_random_id
from config import Opera1_id, Opera2_id, Opera3_id, Opera4_id

vk_session = vk_api.VkApi(token='vk1.a.YES_O15C7mfHWIoEd0CKMVUnLLbBkWoIzg-J84S3vyzotPecNNyYAIaCZMDyXBEuIiNuBHswIHsXbm_BMEwuXfWSRMCNrruyX3JoSPgLUGuZU4BxaojunGe2mToL2YGfkxTvIxrqmfNLX90zXrtsPF6QGTANAe82LZU0v5UENTT4LJcT8CPDc6BYf7Gi8bKn')
tok = "vk1.a.YES_O15C7mfHWIoEd0CKMVUnLLbBkWoIzg-J84S3vyzotPecNNyYAIaCZMDyXBEuIiNuBHswIHsXbm_BMEwuXfWSRMCNrruyX3JoSPgLUGuZU4BxaojunGe2mToL2YGfkxTvIxrqmfNLX90zXrtsPF6QGTANAe82LZU0v5UENTT4LJcT8CPDc6BYf7Gi8bKn"
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()




def wrOpera():
    file = open("opera.txt", "w")
    file.write(f"{Opera1}\n")
def readOpera():
    file = open("opera.txt", "r")
    st = file.readline(1)
    print(int(st))
    global Opera1
    Opera1 = int(st)
    st = file.readline(2)
    # Opera2 = int(st)
    # st = file.readline(3)
    # Opera3 = int(st)
    # st = file.readline(4)
    # Opera4 = int(st)



Opera1 = 0
# Opera2 = 0
# Opera3 = 0
# Opera4 = 0

for event in longpoll.listen():
    
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        
   #Слушаем longpoll, если пришло сообщение то:			
        call_id = 0
        if event.text == 'Привет' or event.text == 'Прив': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    random_id = get_random_id(),
                    message='Хай, клоун')
                
                

            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    random_id = get_random_id(),
                    message='Поздаровайся,пес'
                    
		)
       
        elif event.text == 'Звонок оператору':
            readOpera()
            if(Opera1 == 0):
                Opera1 = 1
                wrOpera()
                d = vk_api.VkApi(token = "vk1.a.c6WFuzdJX216Ns9LIGg43dmwoEZ3zVnbcqRXS4qsrUetULD7CNyNQoLFRKOJSZe6-HQVTNbKquqdyeFC-ffcTUrszUFYu95i63qWdjI0uz3CRRbmWBLqE2b8QCMN5_StTF7fA03p1grkd-4LpvjkPy5WOMrsgKeqHoTSvj5Tj7seQ9YsOsX5qoODLHNGwNGq").get_api().messages.startCall()
                vk.messages.send( #Отправляем собщение
                        user_id=event.user_id,
                        random_id = random.randint(1,100000000),
                        message=f"{d['join_link']}"
                        )
                print(event.user_id)
                vk_api.VkApi(token = "vk1.a.1HwebLuf_5UU2hQKLJ0j0tI-DPJtrHeRCZbDzwV8ULBio3Oa-bdh8sP2B48COyNlJ-qIeZ9VcHzXVSkS1nRM9-R9Q6zQwHz1S7_RZ0S88Gm5Wox8YDxhvohhWtdxF2CGI8-AN5VG30O3Gj5HsvG9zI8zYf23-g1tiDJtcikBjD1ASNlZYBro1oaAwrJZJqNa").get_api().messages.send(
                    user_id = Opera1_id,
                    random_id = random.randint(1,100000000),
                    message=f"{d['join_link']}"
                )
            
        #     d = vk_api.VkApi(token = "vk1.a.c6WFuzdJX216Ns9LIGg43dmwoEZ3zVnbcqRXS4qsrUetULD7CNyNQoLFRKOJSZe6-HQVTNbKquqdyeFC-ffcTUrszUFYu95i63qWdjI0uz3CRRbmWBLqE2b8QCMN5_StTF7fA03p1grkd-4LpvjkPy5WOMrsgKeqHoTSvj5Tj7seQ9YsOsX5qoODLHNGwNGq").get_api().messages.startCall()

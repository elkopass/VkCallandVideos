
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import vk_api

from config import user_tok, oper_tok

def ToMas():
    mas = []
    file = open("query.txt", "r")
    s  = file.read()
    file.close()
    s = s.split('\n')
    for i in range(len(s)):
        s[i] = s[i].split(" ")
    return s

def ToQuery(massiv):
    s = ""
    for i in massiv:
        for k in i:
            s += k + " "
        s = s[:-1]
        s += '\n'
    s = s[:-1]

    file = open("query.txt", "w")
    file.write(s)
    file.close()

def Beg(id, link, isFree):

    massiv = ToMas()
    massiv.append([id, link, isFree])
    ToQuery(massiv)

def Free(id):
    massiv = ToMas()
    flag = 0

    for i in range(len(massiv)):
        if massiv[i][0] == id:
            flag = 1
            massiv[i][2] = "1"
    ToQuery(massiv)
    if flag == 0:
        return 3
        

vk_session = vk_api.VkApi(token=oper_tok)

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()






for event in longpoll.listen():
    
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            
    #Слушаем longpoll, если пришло сообщение то:			
        
        if event.text == 'Привет' or event.text == 'Прив': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    random_id = get_random_id(),
                    message='Хай, клоун')
                
                keyboard = VkKeyboard(one_time=False)

                keyboard.add_button('Начать выступление', color=VkKeyboardColor.SECONDARY)
                keyboard.add_button('Свободная касса', color=VkKeyboardColor.POSITIVE)
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Цирк открылся'
                )
                
    
        elif event.text == 'Начать выступление': 
            d = vk_api.VkApi(token = user_tok).get_api().messages.startCall()
            
            vk.messages.send( #Отправляем собщение
            peer_id=event.user_id,
            random_id = get_random_id(),
            message=f"{d['join_link']}")
            
            Beg(str(event.user_id), d['join_link'], "1" )
    
        elif event.text == 'Свободная касса':
            s = Free(str(event.user_id))
            print(s)
            if s == 3:
                vk.messages.send( #Отправляем собщение
                peer_id=event.user_id,
                random_id = get_random_id(),
                message=f"Начните звонок")
        elif event.text == 'Звонок': 
                d = vk_api.VkApi(token = user_tok).get_api().messages.startCall()
                
                vk.messages.send( #Отправляем собщение
                peer_id=event.user_id,
                random_id = get_random_id(),
                message=f"{d['join_link']}")
                
                

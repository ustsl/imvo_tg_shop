# Базовое и загрузка конфигурации
import os
import json
from yaml import load 
import gc #сборщик мусора
# Зависимости для работы бота
import telegram
# Все статические настройки прячем сюда
from scripts.settings_scripts import Settings

#Внутрянка
from scripts.admins import Imvo_shop_admin
from scripts.users import Imvo_shop_users
from scripts.get_updates import LastMessage # Ищет новых юзеров

"""
Корневой механизм программы
- проверяем обновления
- добавляем новых юзеров
- распределяем юзеров по интерфейсам
- генерим ответ
"""

class SHOP_bot:
    def __init__ (self):
        self.reaction = False
        s = Settings()
        # Работа бота
        bot = telegram.Bot(s.token)
        users = s.users
        admins = s.admins        

        lm = LastMessage (bot)
        data = lm.data
        goods = None


        identify_user = list(data.keys())[0]
        if identify_user not in users.keys():
            self.reaction = True
            print ('new')
            users.update(data)
            with open(os.path.join('files', 'users.json'), 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=4) 
            bot.sendMessage(chat_id = identify_user, text = 'Добавлен новый пользователь')

        if identify_user in admins\
        and data[identify_user][-2] > users[identify_user][-2]:    
            self.reaction = True
            print ('Все условия для взаимодействия с администратором выполнены')
            context = data[identify_user][-1]

            #Если условия админа соблюдены - запускаем админский сервис
            imvo_shop_admin = Imvo_shop_admin (context)
            users.update(data)
            with open(os.path.join('files', 'users.json'), 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=4) 
            bot.sendMessage(chat_id = identify_user, text = imvo_shop_admin.result) 
            

        if identify_user not in admins\
        and data[identify_user][-2] > users[identify_user][-2]:
            self.reaction = True
            print ('Все условия взаимодействия с пользователем выполнены')
            context = data[identify_user][-1]

            #Если условия админа соблюдены - запускаем клиентский сервис
            imvo_shop_users = Imvo_shop_users (context)
            users.update(data)
            with open(os.path.join('files', 'users.json'), 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=4) 
            if imvo_shop_users.result != None:
                user_res = imvo_shop_users.result
                bot.sendMessage(chat_id = identify_user, text = user_res )
            if imvo_shop_users.lot != None:

                for useradmin in admins:
                    bot.sendMessage(chat_id = useradmin, text = imvo_shop_users.lot )
                    if data[identify_user][1] != None\
                    or data[identify_user][2] != None:
                        name = '@'+data[identify_user][1] + ' ' + \
                        data[identify_user][2]
                        second_message = 'Отправлено через бот. Данные пользователя - {}'\
                        .format(name)
                        bot.sendMessage(chat_id = useradmin, text = second_message )  
                    else:
                        second_message =\
                        'Отправлено через закрытую группу. Логин видно в чате'
                        bot.sendMessage(chat_id = useradmin, text = second_message )  
                        
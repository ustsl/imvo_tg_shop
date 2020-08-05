"""
Обращаемся за апдейтом к боту.
Получаем последний апдейт из системы.
Отдаем словарик Data - с ключем в виде ID пользователя и списком основных его параметров.
"""

import time

class LastMessage:
    def __init__ (self, bot):

        self.bot = bot
        self.last_message = []
        try:
            self.lm()
        except:
            None        

    def lm (self):
        bot = self.bot
   
        for last_update in bot.getUpdates(offset=-1):
            
            date = last_update['message']['date']
            timestamp = time.mktime(date.timetuple())
            chatid = last_update['message']['chat']['id']
            username = last_update['message']['chat']['username']
            firstname = last_update['message']['chat']['first_name']
            lastname = last_update['message']['chat']['last_name']
            text = last_update['message']['text']
        self.data = {}   
        self.data[str(chatid)] = [str(chatid), 
                                  username, 
                                  firstname, 
                                  lastname,
                                  timestamp, 
                                  text]
# Базовое и загрузка конфигурации
import os
import json
from yaml import load 

class Settings:
    def __init__ (self):        
        with open(os.path.join('files', 'settings.yaml'), 'r') as f:
            self.config = load(f)
        with open(os.path.join('files', 'users.json'), "r", encoding='utf-8') as read_file:
            self.users = json.load(read_file)
        with open(os.path.join('files', 'goods.json'), "r", encoding='utf-8') as read_file:
            self.goods = json.load(read_file)
        #Неизменное
        self.token = self.config['token']
        self.admins = self.config['admins']
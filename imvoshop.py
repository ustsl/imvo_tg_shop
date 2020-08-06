# Работа с датами
from datetime import datetime, timedelta 
import time
from scripts.mainshop import SHOP_bot

if __name__ == "__main__":
    
    timer = 1
    print ('---')
    print ('IMVO SHOP BOT. MVP VERSION 1')
    print ('---')

    while True:
        
        try:       
            sh = SHOP_bot()
            if sh.reaction == True:
                timer = 1           
        except:
            print ('Масштабная ошибка в блоке бота')
            
        if timer < 4:
            timer += 0.5
            
        time.sleep(timer)
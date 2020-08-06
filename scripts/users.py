import re
from scripts.settings_scripts import Settings

class Imvo_shop_users:
    def __init__ (self, context):
        self.result = None
        self.lot = None
        #Загружаем паттерн
        pattern = '/[0-9]*'
        prog = re.compile(pattern) 
        if re.fullmatch(pattern, context):
            print ('Запрос на товар')
            self.purchase(context)
    def purchase(self, context):
        self.result = 'Товар с заданным номером не найден, или его запасы распроданы'
        s = Settings()
        goods = s.goods
        for good_search in goods:
            if str(context)[1:] == str(good_search):
                lot = goods[good_search]
                
                self.lot = 'Оформлен заказ №' + lot[0]\
                + ' Товар - ' + lot[1] + ' Стоимость - ' + lot[2]
                self.result = self.lot + '. Менеджер с вами свяжется'
                break
            
        print (self.result)
                

        
        
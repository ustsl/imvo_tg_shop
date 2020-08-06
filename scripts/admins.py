import os
import json
from scripts.settings_scripts import Settings


class Imvo_shop_admin:
    def __init__ (self, context):
        self.result = 'Ошибка при публикации товара'
        self.context = context
        self.admin_functions()
        
        
    def admin_functions(self):
        context = self.context
        #Вытаскиваем данные по товару, чтобы записать в JSON-базу
        if 'номер' in context\
        and 'название' in context\
        and 'цена' and context:  
            try:
                self.good = {}
                one_step = context.split('номер')[1].split('название')
                two_step = one_step[1].split('цена')
                self.good[one_step[0].strip()] = [one_step[0].strip()] + \
                [two_step[0].strip()] + \
                [two_step[1].strip()]
                self.go()
            except:
                self.result = \
                'Соблюдайте порядок синтаксиса - номер НОМЕР ЗАКАЗА название НАЗВАНИЕ цена ЦЕНА'
           
    def go(self):
        good = self.good
        s = Settings()
        goods = s.goods
           
        #Обновляем словарь значений
        goods.update(good)
        with open(os.path.join('files', 'goods.json'), 'w', encoding='utf-8') as f:
            json.dump(goods, f, ensure_ascii=False, indent=4) 

        #Условие удаление товара
        if len(list(goods.keys())) > 50:
            delete = list(goods.keys())[0]
            del(goods[delete])

            with open(os.path.join('files', 'goods.json'), 'w', encoding='utf-8') as f:
                json.dump(goods, f, ensure_ascii=False, indent=4)         
        self.result = 'Добавлен новый товар'
        self.goods = goods
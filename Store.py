# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
#
# Шаги:
#
# 1. Создай класс Store:
#
# -Атрибуты класса:
#
# name: название магазина.
#
# address: адрес магазина.
#
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
#
# Методы класса:
#
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
#
# -  метод для добавления товара в ассортимент.
#
# метод для удаления товара из ассортимента.
#
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
#
# метод для обновления цены товара.

class Store:

    def __init__(self, name, address, items=None):
        if items is None:
            items = {}
        self.name = name
        self.address = address
        self.items = items

    def add_item(self, name_of_item, price_of_item):
        self.items[name_of_item] = price_of_item

    def get_price(self, name_of_item):
        price = self.items.get(name_of_item)
        if price:
            return price
        else:
            print("Не найден товар с таким наименованием")


    def set_price(self, name_of_item, price_of_item):
        if self.items.get(name_of_item):
            self.items[name_of_item] = price_of_item
        else:
            print ("Не найден товар с таким наиманоенованием")

    def get_items_and_prices(self):
        print(self.name)
        for key, value in self.items.items():
            print(f"{key} : {value}")

    def delete_item(self, name):
        del self.items[name]

store_lenta = Store("Лента", "Где то за горизонтом")
store_lenta.add_item("Яблоко", 100)
store_lenta.add_item("Колбаса", 400)
store_lenta.add_item("Сыр", 500)
store_lenta.add_item("Яйца", 300)

store_metro = Store("Метро", "Просто адрес")
store_metro.add_item("Билеты в кино", 2000)
store_metro.add_item("Лотерейный билет", 5876)
store_metro.add_item("Подарочный сертификат", 1000)

store_ashan = Store("Ашан", "Точно где то есть")
store_ashan.add_item("Вафли", 286)
store_ashan.add_item("Сгущенка", 800)
store_ashan.add_item("Варенье", 1300)

store_lenta.get_items_and_prices()
store_lenta.set_price("Яблоко", 120)
store_lenta.set_price("Молоко", 120)
print(store_lenta.get_price("Яблоко"))
store_lenta.delete_item("Яблоко")
print(store_lenta.get_price("Яблоко"))
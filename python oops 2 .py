class Product:
    price = 1000

    @classmethod
    def change_price(cls, new_price):
        cls.price = new_price

Product.change_price(1500)

print(Product.price)
class Product:
    price = 1000

    @classmethod
    def change_price(cls, new_price):
        cls.price = new_price

Product.change_price(1500)

print(Product.price)
class App:
    language = "English"

    @classmethod
    def change_language(cls, new_language):
        cls.language = new_language

App.change_language("Kannada")

print(App.language)
class Game:
    level = 1

    @classmethod
    def change_level(cls, new_level):
        cls.level = new_level

Game.change_level(5)

print("Level:", Game.level)
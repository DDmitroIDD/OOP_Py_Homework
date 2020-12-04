class CoffeeMachine:
    water = 100
    grains = 100
    __waste = 0
    __limit_waste = 30

    def make_americano(self, coll):
        if (self.water - 10 * coll) <= 0:
            print('add water please')
            return False
        if (self.grains - 5 * coll) <= 0:
            print('add grains please')
            return False
        if (self.__waste + 2 * coll) <= self.__limit_waste:
            self.__waste += 2 * coll
            self.water -= 10 * coll
            self.grains -= 5 * coll
            print('Please your coffee')
            return
        else:
            print('waste is full')
            return False

    def make_espresso(self, coll):
        if (self.water - 10 * coll) <= 0:
            print('add water please')
            return False
        if (self.grains - 5 * coll) <= 0:
            print('add grains please')
            return False
        if (self.__waste + 5 * coll) <= self.__limit_waste:
            self.__waste += 5 * coll
            self.water -= 10 * coll
            self.grains -= 5 * coll
            print('Please your coffee')
            return
        else:
            print('waste is full')
            return False

    def clean_coffee(self):
        self.__waste = 0
        print('waste removed')

    def add_water(self):
        self.water = 100
        print('water is full')

    def add_grains(self):
        self.grains = 100
        print('grains is full')

    def coffee_to_child(self, coll):
        if (self.water - 10 * coll) <= 0:
            print('add water please')
            return False
        if (self.grains - 5 * coll) <= 0:
            print('add grains please')
            return False
        if (self.__waste + 5 * coll) <= self.__limit_waste:
            self.__waste += 5 * coll
            self.water -= 10 * coll
            self.grains -= 5 * coll
            return True
        else:
            print('waste is full')
            return False


class CoffeeMachineWithMilk(CoffeeMachine):
    milk = 50

    def cappuccino(self, coll):
        if (self.milk - 5 * coll) <= 0:
            print('add milk')
            return False
        elif self.coffee_to_child(coll):
            print('your cappuccino')
            self.milk -= 5 * coll
            return True

    def latte(self, coll):
        if (self.milk - 10 * coll) <= 0:
            print('add milk')
            return False
        elif self.coffee_to_child(coll):
            print('your latte')
            self.milk -= 10 * coll
            return True

    def add_milk(self):
        self.milk = 50
        print('milk added')


class SpecialCoffee(CoffeeMachineWithMilk):
    whiskey = 100

    def americano_with_whiskey(self, coll):
        if (self.whiskey - 5 * coll) <= 0:
            print('add whiskey')
            return
        elif self.make_americano(coll):
            print('with whiskey')
            self.whiskey -= 5 * coll
            return

    def espresso_with_whiskey(self, coll):
        if (self.whiskey - 5 * coll) <= 0:
            print('add whiskey')
            return
        elif self.make_espresso(coll):
            print('with whiskey')
            self.whiskey -= 5 * coll
            return

    def cappuccino_with_whiskey(self, coll):
        if (self.whiskey - 5 * coll) <= 0:
            print('add whiskey')
            return
        elif self.cappuccino(coll):
            print('with whiskey')
            self.whiskey -= 5 * coll
            return

    def latte_with_whiskey(self, coll):
        if (self.whiskey - 5 * coll) <= 0:
            print('add whiskey')
            return
        elif self.latte(coll):
            print('with whiskey')
            self.whiskey -= 5 * coll
            return

    def add_whiskey(self):
        self.whiskey = 100
        print('whiskey added')


make_coffee_with_milk = SpecialCoffee()


make_coffee_with_milk.latte_with_whiskey(4)

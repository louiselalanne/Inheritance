class parent():

    def _init_(self):
        print("This is a parent class")

    def menu(dish):
        if dish == "burguer":
            print("You can add folloeing toppings")
            print("More cheese | More bacon")
        elif dish == "fries":
            print("You can add folloeing toppings")
            print("Add cheese | Add bacon")
        else:
            print("Please, enter valid dish")

    def final_amount(dish, add_ons):
        if dish == "burguer" and add_ons == "cheese1":
            print("You need to pay 12 reais")
        elif dish == "burguer" and add_ons == "bacon1":
            print("You need to pay 13 reais")
        elif dish == "fries" and add_ons == "cheese2":
            print("You need to pay 8 reais")
        elif dish == "fries" and add_ons == "bacon2":
            print("You need to pay 9 reais")

class child1(parent):

    def _init_(self, dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)

class child2(parent):

    def _init_(self,dish,add_ons):
        self.new_dish = dish
        self.add_ons = add_ons

    def get_final_amount(self):
        parent.final_amount(self.new_dish, self.add_ons)

child1obj = child1("burguer")
child1obj.get_menu()

child2obj = child2("burguer", "cheese1")
child2obj.get_final_amount()
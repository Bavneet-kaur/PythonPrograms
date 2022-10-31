# 1: Latte ; 2: Cappinino ; 3: Esppresso 
#ask name >> type of coffee >>add-ons/any other coffee type >> quantity >> display the bill

# importing important libraries
import math
# creating the dictionary of prices for the all the three coffee as mentioned above

price = {
    1: 233.00,
    2: 350.15,
    3: 489.00
}
class Coffeemc:
    global data
    data = {}
    def promptUser(self): 
        print("HELLO! WELCOME TO OUR COFFEE SHOP") 
        name = input("\nWhat is Your name: ")
        
        print("\n\tOUR MENU:\n\n\t1) Latte\n\t2) Cappicino\n\t3) Espresso\n\n")
        order = int(input("Enter Your Coffee Choice: "))

        quantity = int(input("How much quantity do you want: "))

        if order == 1: # Latte
            total =  price[1] * quantity
            data['name'] = name
            data['type'] = 'Latte'
            data['total'] = str(math.floor(total))
        
        elif order == 2: # Cappicino
            total =  price[2] * quantity
            data['name'] = name
            data['type'] = 'Cappicino'
            data['total'] = str(math.floor(total))

        elif order == 3: # Espresso
            total =  price[3] * quantity
            data['name'] = name
            data['type'] = 'Espresso'
            data['total'] = str(math.floor(total))
        return data

    def bill(self, promptUser):
        print("Recipet:")
        name = promptUser['name']
        type = promptUser['type']
        total = promptUser['total']

        print("Name: " + name +"\nCoffee: " + type + "\nTotal:  Rs" + total + "\n")
coffee = Coffeemc()
coffee.bill(coffee.promptUser()) 
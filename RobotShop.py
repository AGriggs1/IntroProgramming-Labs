#Intro to Programming
#Author: Anthony Griggs
#11/17/2017


##===========================================================================================
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def isInStock(self):
        return self.stock > 0

    def getTotalCost(self, qtyDemanded):
        return self.price * qtyDemanded

    def diminishStock(self, qty):
       #Make sure there is enough in stock to take away before taking away the defined amount
       if self.stock - qty > 0: self.stock -= qty
##===========================================================================================

products = []
ultrasonic = Product("Ultrasonic ranger finder", 2.50, 4)
products.append(ultrasonic)
servo = Product("Servo motor", 14.99, 10)
products.append(servo)
microcont = Product("Microcontroller Board", 44.95, 5)
products.append(microcont)
laser = Product("Laser range finder", 149.99, 7)
products.append(laser)
lithium = Product("Lithium polymer battery", 8.99, 8)
products.append(lithium)

def printStock():
    print()
    print("Available Products")
    print("------------------")
    i = 0
    for p in products:
        if p.isInStock: print(str(i) + ")", p.name, "$", p.price)
           # print(str(i)+")", productNames[i], "$", productPrices[i])
        i += 1
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodID = int(vals[0]) 
        count = int(vals[1])

        if products[prodID].stock >= count:
            if cash >= products[prodID].price:
                products[prodID].diminishStock(count)
                cash -= products[prodID].price * count
                print("You purchased", count, products[prodID].name + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("You cannot afford that product. Getouttaa mah shop ya freeloader!")
        else:
            print("Sorry, we are sold out of", products[prodID].name)

main()

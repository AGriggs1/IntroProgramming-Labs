#Intro to Programming
#Author: Anthony Griggs
#11/17/2017

productNames = [ "Ultrasonic range finder",
                 "Servo motor",
                 "Microcontroller Board",
                 "Laser range finder",
                 "Lithium polymer battery"
                 ]
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

    def setStock(self, qty):
       #Make sure there is enough in stock to take away before taking away the defined amount
       if self.Stock - qty > 0: self.Stock -= qty
##===========================================================================================
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]

ultrasonic = Product("Ultrasonic ranger finder", 2.50, 4)
servo = Product("Servo motor" 14.99, 10)
microcont = Product("Microcontroller Board", 44.95, 5)
laser = Product("Laser range finder", 149.99, 7)
lithium = Product("Lithium polymer battery", 8.99, 8)

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0, len(productNames)):
        if productQuantities[i] > 0:
            print(str(i)+")", productNames[i], "$", productPrices[i])
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodID = int(vals[0]) 
        count = int(vals[1]) 

        if productQuantities[prodID] >= count:
            if cash >= productPrices[prodID]:
                productQuantities[prodID] -= count
                cash -= productPrices[prodID] *count
                print("You purchased", count, productNames[prodID] + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("You cannot afford that product. Getouttaa mah shop ya freeloader!")
        else:
            print("Sorry, we are sold out of", productNames[prodID])

main()

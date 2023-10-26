class sportmart:
    def __init__ (self):
        self.inventory = {}
        self.orders = {}

    def createOrder(self, OrderID, ItemName, Quantity, Price, Total):
        temp = {
            "OrderID": OrderID,
            "Item Name": ItemName,
            "Quantity": Quantity,
            "Price": Price,
            "Total": Total
        }

        self.orders[OrderID] = temp

    def createInventoryItem(self, ProductID, ProductName, Quantity):
        temp = {
            "ProductID": ProductID,
            "ProductName": ProductName,
            "Quantity": Quantity
        }

        self.orders[ProductID] = temp

    def printOrders(self):
        print(self.orders)

    def printInventory(self):
        print(self.inventory)

trinity = sportmart()
orders = open("MyThirdClass(ORDER_SHEET).csv", "r")
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(",")
    trinity.createOrder(temp[0], temp[1], temp[2], temp[3], temp[4])

trinity.printOrders()

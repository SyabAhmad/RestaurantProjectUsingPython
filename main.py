print("Restaurant Project using Python Programming\n Language For Noobs")


# TO Display all manu at once

class AllVariablesDeclaredHere:

    ChickenPolao = 1500
    ChickenTikka = 2000
    Mutton = 2500
    Haleem = 700
    Rice = 1800


class ManuItemsToDisplay:
    def displayItems(self):
        print("1: Chicken Polao")
        print("2: Chicken Tikka")
        print("3: Mutton")
        print("4: Haleem")
        print("5: Rice")


class ManuPanels():

    def ChickenPolaoPanel(self):
        variables = AllVariablesDeclaredHere()
        print("********* || __Chicken Polao panel__ || *********")
        print(" Chicken Polao Selected : Price is ", variables.ChickenPolao)
        quantityInNumbers = int(input("Enter Quantity: "))
        priceWithDis = (variables.ChickenPolao/100)*2
        billWithDis = quantityInNumbers * variables.ChickenPolao
        FinalBillWithDis = priceWithDis - billWithDis
        print(" You Bill is: " ,FinalBillWithDis)

    def ChicekTikkaPanel(self):
        variables = AllVariablesDeclaredHere()
        print("********* || __Chicken Tikka panel__ || *********")
        print(" Chicken Tikka Selected : Price is ", variables.ChickenTikka)
        quantityInNumbers = int(input("Enter Quantity: "))
        priceWithDis = (variables.ChickenTikka / 100) * 2
        billWithDis = quantityInNumbers * variables.ChickenTikka
        FinalBillWithDis = priceWithDis - billWithDis
        print(" You Bill is: " ,FinalBillWithDis)

    def MuttonPanel(self):
        variables = AllVariablesDeclaredHere()
        print("********* || __Mutton Panel panel__ || *********")
        print(" Mutton Selected : Price is ", variables.Mutton)
        quantityInNumbers = int(input("Enter Quantity: "))
        priceWithDis = (variables.Mutton / 100) * 2
        billWithDis = quantityInNumbers * variables.Mutton
        FinalBillWithDis = priceWithDis - billWithDis
        print(" You Bill is: " ,FinalBillWithDis)

    def HaleemPanel(self):
        variables = AllVariablesDeclaredHere()
        print("********* || __Haleem panel__ || *********")
        print(" Haleem Selected : Price is ", variables.Haleem)
        quantityInNumbers = int(input("Enter Quantity: "))
        priceWithDis = (variables.Haleem / 100) * 2
        billWithDis = quantityInNumbers * variables.Haleem
        FinalBillWithDis = priceWithDis - billWithDis
        print(" You Bill is: " ,FinalBillWithDis)

    def RicePanel(self):
        variables = AllVariablesDeclaredHere()
        print("********* || __Rice panel__ || *********")
        print(" Rice Selected : Price is ", variables.Rice)
        quantityInNumbers = int(input("Enter Quantity: "))
        priceWithDis = (variables.Rice / 100) * 2
        billWithDis = quantityInNumbers * variables.Rice
        FinalBillWithDis = priceWithDis - billWithDis
        print(" You Bill is: " ,FinalBillWithDis)


class GettingOrder:
    def GettingOrderFromUser(self):
        panel = ManuPanels()
        orderInputForOrder = int(input("Enter you Desire Input: "))
        if orderInputForOrder == 1:
            panel.ChickenPolaoPanel()
        elif orderInputForOrder == 2:
            panel.ChicekTikkaPanel()
        elif orderInputForOrder == 3:
            panel.MuttonPanel()
        elif orderInputForOrder == 4:
            panel.HaleemPanel()
        elif orderInputForOrder == 5:
            panel.RicePanel()


# ----------------------------------------------------------------
# Main Method
# we should call alla the methods here
objectForItemsManu = ManuItemsToDisplay()
order = GettingOrder()
objectForItemsManu.displayItems()
order.GettingOrderFromUser()

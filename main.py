print("Restaurant Project using Python Programming\n Language For Noobs")

# TO Display all manu at once

class ManuItemsToDisplay:
    def displayItems(self):
        print("1: Chicken Polao")
        print("2: Chicken Tikka")
        print("3: Mutton")
        print("4: Haleem")
        print("5: Rice")

class ManuPanels:
    def ChickenPolaoPanel(self):
        print("1: Chicken Polao panel")
    def ChicekTikkaPanel(self):
        print("2: Chicken Tikka panel")
    def MuttonPanel(self):
        print("3: Mutton panel")
    def HaleemPanel(self):
        print("4: Haleem panel")
    def RicePanel(self):
        print("5: Rice panel")


class GettingOrder:
    def GettingOrderFromUser(self):
        panel = ManuPanels()
        orderInputForOrder = input("Enter you Desire Input: ")
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


#----------------------------------------------------------------
# Main Method
# we should call alla the methods here
objectForItemsManu = ManuItemsToDisplay()
order = GettingOrder()
objectForItemsManu.displayItems()
order.GettingOrderFromUser()
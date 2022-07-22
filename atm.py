class Atm(object):
    def __init__(self,users,atmcardnumber,pinnumber):
        self.users=users
        self.atmcardnumber=atmcardnumber
        self.pinnumber=pinnumber
    def userName(self):
        print("Type in your name")
    def userAtmCardNumber(self):
        print("Type in your atm card number")
    def userPinNumber(self):
        print("Type in your 4-digit pin number")
    def cashWithDrawal(self):
        print("Amount of money wanted")
    def balanceInquiry(self):
        print("Balance on credit card")


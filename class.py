class Atm:
    def __init__(self,CardNumber,Pin):
        self.Cardnumber=CardNumber
        self.Pin=Pin
        
        
    def checkBalance(self):
        print("YOUR BALANCE IS 500000")
        
    def withdrawl(self,amount):
        newAmt=500000-amount
        print('YOU HAVE WITHDRWL AMOUNT '+str(amount)+".YOUR REMANING BALANCE IS "+str(newAmt))
        
def main():
    CardNumber=input("Insert your card number:- ")
    Pin=input("Insert your Pin number:- ")
        
    newUser = Atm(CardNumber,Pin)
        
    print("Select your Activity ")
    print("1.Balance Enquriy  2.Withdrawl")
    activity=int(input("Enter Activity Number"))
        
    if (activity==1):
        newUser.checkBalance()
    elif (activity==2):
        amount=int(input("Enter the amount"))
        newUser.withdrawl(amount)
    else:
        print("Enter a valid number only")
            
if __name__=="__main__":
        main()

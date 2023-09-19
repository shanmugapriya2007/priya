class bankaccount:
  def __init__(self,accno,accholdername,initialamount=0.0):
     self.__accno=accno
     self.__accholdername=accholdername
     self.__accbalance=initialamount
  def deposit(self,amount):
     if amount>0:
       self.__accbalance +=amount
       print("Deposited ₹{}.Newbalance:₹{}".format(amount,self.__accbalance))
     else:
       print("Invalid deposit \t amount.please deposit the positive amount")
  def withdrawl(self,amount):
     if amount>0 and amount<=self.__accbalance:
        self.__accbalance -=amount
        print("Withdrawal ₹{}.Newbalance ₹{}".format(amount,self.__accbalance))
     else:
        print("Invalid withdrawal amount of Insufficient balance")
  def displaybalance(self):
     print("Account balance for {}(Account ₹{}:₹ {}".format
          (self.__accholdername,self.__accno,self.__accbalance))

account=bankaccount(accno="12345678",accholdername="priya",initialamount=5000.0)
account.displaybalance()
account.deposit(500.0)
account.withdrawl(500.0)
       
   

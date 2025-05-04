# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name.
#  Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.


class Bank:
    bank_name = 'habib metro'

    @classmethod
    def change_bank_name(cls,name):
     
     cls.bank_name =   name 
 



bankk = Bank.change_bank_name('UBL')
print(Bank.bank_name)
'''
Created on Jun 10, 2014

@author: mike
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
sum_three = [0, 1, 2]
        
def appendsums(sum_three):
    for i in range(25):
        listLenght = len(sum_three)
        mySum = 0
        mySum = sum_three[listLenght-1] + sum_three[listLenght-2] + sum_three[listLenght-3]
        sum_three.insert(listLenght,mySum)
        
    print sum_three
    
     

appendsums(sum_three)
print sum_three[20]

import BankAccount

my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()

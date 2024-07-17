'''
STATEMENT=
pooja would like to withdraw x usd from ATM
atm will accept only if the amount(x) is in multiple of 5
pooja has enough balance to carry out transaction
for each withdrawl bank charges 0.50 usd
calculate pooja's account balance after an attempted transaction

Input
positive integer 0< x <=2000 the amount which pooja wish to withdraw.
non-negative number 0 <= y <=2000 with two digits of precision- pooja's 
initial account balance

output
account balance after attempted transaction, a no. with 2 digits after decimal

'''


x=int(input())
y=float(input())

if x%5==0 and x<=y:
    t=y-(x+0.5)
    print(f'%.2f'%t)

else:
    print(f'%.2f'%y) 
 
'''
STATEMENT-
You are given 2 integers, say M and N 
you must check whether M is an exact multiple of N, without using loops
you have to output 0 if M is not multiple of N
you have to output M/N if M is multiple of N
'''

m=int(input())
n=int(input())

if(m%n==0):
    print(int(m/n))   #typecasting converting float to integer
else:
    print(0)    

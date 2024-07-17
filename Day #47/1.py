
'''
 write a py program to trsnslate a msg into secret code language. use rules below

 coding:
 If the word contains atleast 3 characters, remove the first letter and append it at end.
 Now append three random characters at starting and end.
 else simply reverse the string.

 Decoding:
 If word contains less thsn 3 characters reverse it ,
 else:
 remove three characters at starting and end and, remove last letter & append it to start

'''
st= input("Enter the secret message:")
words = st.split(" ")
# coding= True   #true for generating & False for decoding 
coding= input("1 for coding & 0 for decoding")
coding= True if (coding=="1") else False

if(coding):
    nwords =[]  #we make nwords as a empty list
    for word in words:
     
     if(len(word)>=3):
        r1="sdf"  # take random characters to add at starting and ending in stnew
        r2="jzq"
        stnew= r1 + word[1:] + word[0] + r2 
         #word=[1:]- this will print all characters without 1st, after that
         #word[0]- this will print the first character at end
        nwords.append(stnew)   
     else:
        nwords.append(word[::-1]) # in nwords append the word in reverse if it is <3

    print(" ".join(nwords))

else:
   nwords=[]
   for word in words:
      if(len(word)>=3):
         stnew= word[3:-3] # this will remove the first & last 3 random characters
         stnew= stnew[-1] + stnew[:-1]
         # will print last letter (from stnew) + all letters - last letter (fromstnew)
         nwords.append(stnew)
        
      else:
          nwords.append(word[::-1]) # apply the same to reverse the string again
   print(" ".join(nwords))
         
         




        
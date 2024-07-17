#-------------various METHODS in STRINGS-----------------------------------

#note_________________________ STRINGS ARE IMMUTABLE________________________________-

a="!!pratik!!!!!!!! pratik ok !!"

print(len(a))
print(a)
print(a.upper())  #--capital letters
print(a.lower())

print(a.rstrip("!")) #removes !

print(a.replace("pratik","omkar"))  # all pratik relaced with omkar

print(a.split(" ")) #converts to tupule where there is space



heading="introduction to python"
print(heading.capitalize()) # first letter to Capital



# b="welcome to console!!!"
# print(b.centre(50))

print(a.count("pratik"))  # counts pratik occurance in string a

str1 = "welcome to console !!"
print(str1.endswith("!"))  #if yes returns True...
print(str1.endswith("a"))  #if no returns False...
print(str1.endswith("to",4,10))  #can check for specific letters..
print(str1.startswith("w"))  #if yes returns true...

str2 ="He's name is dan, he is an honest man"
print(str2.find("is"))  # will give index of is i.e 10

str3 ="WelcomeToConsole30"
print(str3.isalnum())  # checks all are A-Z or a-z or 0-9, then True
print(str3.isalpha())  # checks only letters not numbers,so here it is False

print(str3.islower())  # if all letters are lower
print(str3.isupper())  # if all letters are Upper

str4 ="Wish yoy a very happy birthday\n"
print(str4.isprintable())  # false becoz \n is not printable


j="      "      #space by spacebar
print(j.isspace())
k="     "      #space by Tab
print(k.isspace())

ok="To kill a Mocking bird"
print(ok.istitle())  #True if all words first letter are Capital 
print(ok.title())  #converts all words first letter to Capital

f="Python iS a Interpreted language"
print(f.swapcase())  #swaps upper to lower case and vise-versa
print(f.title())   






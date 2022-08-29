#Strings in action
Temp='abc'+'def'    #concatenation: a new string
print(Temp)
Temp1='Jeng!' * 4   #Repeat the string for n time
print(Temp1)

#Indexing and slicing 
S='spam'
Temp3=S[0], S[-2]   #Indexing from or end
print(Temp3)
Temp4=S[1:3], S[1:], S[:-1] #Slicing: extract section
print(Temp4)

#Changing and formatting
S = S +'Spam!'      #to change a string, make a new one
print(S)

#Common string tools
S="spammify"
print(S.upper())    #convert to uppercase
print(S.find("mm")) #return index of substring
print(int("42"), str(42))   #convert from/to string

print(S.split("mm"))        #Splitting and joining
Temp5='XX'.join(S.split("mm"))
print(Temp5)


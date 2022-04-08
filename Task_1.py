
# Get first name, lastname, mobile number, and email id
fname = input()

lname=input()

mob = input()

gmail = input()

#Capitalize the names and lowercase email id
fname = fname.capitalize()

lname = lname.capitalize()

gmail = gmail.lower()

#Verify mobile number and email Id

if mob.isdigit()==True and len(mob)==10:
  
  if gmail.endswith("@gmail.com") and gmail[:-10].isalnum()==True:
    print(fname)
    print(fname)
    print(mob)
    print(gmail)
    
else:
  print("Please enter the inputs again.")
  print("""Make sure that:
    1. You don't have any constrains to input name.
    2.Your mobile number consists of numbers only and the maximum length must be exactly 10.
    3. Your gmail must be made out of a combination of alphabets and numbers,as well as must end with\\'@gmail.com\\'""")
  
  
  # Create a file
file=open("answer_Guvi.txt","a")

# Take user input
file.write("\n")

text=input().split()                                                            

# Capitalize each word and add to file
temp=list(map(lambda x: x.capitalize()+ " ",text))                                

file.writelines(temp)                                                             

file.write("\n")                                                                


# Mobile number as input
number=input()                                                                     

# Verify mobile number
if len(number)==10 and number.isnumeric()==True:                                      
  file.writelines(number)                                                          

file.close()                                                                    


# Open file in read mode, Print lines, Close the file
file1=open("answer_Guvi.txt","r")                                                     
print(file1.read())                                                             
file.close()     

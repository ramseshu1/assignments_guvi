
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

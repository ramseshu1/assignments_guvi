
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

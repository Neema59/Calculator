# This program is a calculator that perform simple operations
# Users must input two numbers and the operatior to display the result
while True :
      try :
           num1= int(input("Please enter a number : "))
           num2= int(input("Please enter a number : "))
          
# Exception to prevent error like invalid input    
      except ValueError: 
     
       print("Oops! Invalid input, please try again!")
       continue
        
      opr = input("Please select the operation you want to perform : ")

# Selecting the wanted operation to perform  
      if opr == "+" :        
       equ = num1 + num2
      elif opr == "-" :
       equ = num1 - num2
      elif opr == "*" :
       equ = num1 * num2
      elif opr == "/" :
       try :
        equ = num1 / num2

# Exception to prevent error of dividing by zero
       except ZeroDivisionError: 
         
         print("Error, please try again! You cannot divide by 0")
         continue
         
      else :
        equ = "Error"
        
        print("Error operator! Please try again")
        continue

# Saving the equations as a text file    
      with open ("equ.txt","a") as file:  
       file.write((f"equ={equ}\n"))

# Print the equation        
      print(f"equ={equ}") 

# Asking users what they want to do next
      print("Do you want to continue calculating or do you want to read all the equations ?") 
      answer = input("Please,type continue or read : ")

# To detect wrong input
      if answer != "read" and  answer != "continue" : 
         print ("Oops, you entered a wrong answer. Please try again.")
        
# Statement to continue calculations or reading equations
      elif answer == "read":   
          while True :
            try:                 
# Users create a new file to read the equation        
              namefile = input("Please, enter a file name ending by .txt : ") 
              namefile = "equ.txt"
              with open (namefile ,"r") as file:
               lines = file.readlines()
               for line in lines :
                                               
                print(line.strip())
                                                                                               
            except FileNotFoundError :
              print("File not found")
            break
                                                                                                                                   
      else :
          if answer == "continue":
           continue
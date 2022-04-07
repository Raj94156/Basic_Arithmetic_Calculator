from art import logo
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multi(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
arithmetic = {
  "+":add,
  "-":subtract,
  "*":multi,
  "/":div
  }
def calculator():
  print(logo)
  num1 = int(input("Enter your first number:-"))
  for operator in arithmetic:
    print(operator)
  is_countinue=True
  while is_countinue == True:
    pickup=input("Pickup your operator from above operation:-")
    num2 = int(input("Enter  the next  number:-"))    
    operator = arithmetic[pickup]
    answer=operator(num1,num2)
    print(f"{num1} {pickup} {num2} is {answer}")
    if input("Enter 'y' if you want to continue with {answer},Otherwise type 'n' to exit") == 'y':
      num1=answer
    else:
      is_countinue = False
      print("Thank you for using calculator")
      
      
calculator()
    

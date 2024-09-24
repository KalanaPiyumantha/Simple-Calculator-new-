def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("""                           _
   ____      _            _        | |_       ____     
  / ___|__ _| | ___ _   _| | __ _| | _ |__    | __|
 | |   / _` | |/ __| | | | |/ _` | | |/  _  ) | |
 | |__| (_| | | (__| |_| | | (_| | | (_ | |  || |
  \____\__,_|_|\___|\__,_|_|\__,_|_|_|\__ __) |_|
    """)
print("Select Operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

while True:
    choice  = input("Enter Choice( 1 / 2 / 3 / 4):")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter Your First Number : "))
            num2 = float(input("Enter Your Second Number : "))
            
        except ValueError:
            print("Invalid input. Please Enter a Number :")
            continue

        if choice == '1':
              print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice =='2':
            print(num1, "-", num2, "=", sub(num1, num2))
            
        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))
            
        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
            
            
        next_calculation = input("Let's Do the Next Calculation? (yes/no): ")
        if next_calculation == 'yes':
            continue
        if next_calculation == "no":
         print ("Thank you.........! Come Again")
         break
        
            
        else:
            print("Invalid input")

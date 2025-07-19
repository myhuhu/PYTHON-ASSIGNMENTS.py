def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
   
        result = num1 / num2

    except ValueError:
       
        print("Error: Please enter valid integers.")

    except ZeroDivisionError:
       
        print("Error: Cannot divide by zero.")

    else:
        
        print(f"The result of dividing {num1} by {num2} is: {result}")

    finally:
       
        print("Operation complete.")


divide_numbers()

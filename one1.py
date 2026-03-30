try:
    number1=int(input("Enter first number: "))
    number2=int(input("Enter second number: "))
    result=number1/number2

except ZeroDivisionError:
    print("Error: Cannot divide by zero!.")

except ValueError:
    print("Error: Invalid input! Please enter a valid number.")

else:
    print("Division successful! The result is:", result)

finally:
    print("This block always run.")
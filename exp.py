try:
    x = int(input("Enter x:"))
    ans = 10/x

except ZeroDivisionError:
    print("Division by zero is not allowed")

except ValueError:
    print("Invalid Input")

else:
    print(f"Ans = {ans}")

finally:
    print("End of our program")

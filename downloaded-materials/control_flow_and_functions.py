# Author: Nazrul Ismail
# Description: Template code for live demo of Python Basics (Control flow and functions)
# Date: 08/05/2024

# === Control flow: Branching ===
print("\n" + "="*30)
print("Section: Control flow - Branching")
print("="*30 + "\n")

# === if and logic operations on bools===
a = True 
b = False 
if a and b: 
    print("Both are True")

print(f"a: {a}, b: {b}\n")
print("and logic | a and b:", a and b)
print("or logic | a or b:", a or b)
print("not logic | not a:", not b)

"""
Write an if statement to check if variable x is even or odd
if <condition>:
    print x is even
else:
    print x is odd
"""
x = 0 #place in your value here

if x > 0:
    print("x is a positive number")
elif x ==  0:
    print("X is zero")
else:
    print("X is a negative number")
    
# === CONTROL FLOW: while, for loops===
print("\n" + "="*30)
print("Section: CONTROL FLOW - while, for loops ")
print("="*30 + "\n")

#while loop
condition = None
while condition:
    print("[while loop] while loop is running...")
print()

#for loop
#range -> (start, end, step)
for i in range(0, 10):
    print(f"{i}")
print()

# === break statement===#
#From slides
mysum = 0
for i in range(0, 10):
    print(f"mysum: {mysum}")
    if mysum == 5:
        break
        mysum += 1 #Can you spot whats wrong here?
    mysum+=1

# === CONTROL FLOW: functions===
print("\n" + "="*30)
print("Section: Functions ")
print("="*30 + "\n")

# There's 2-ways on writing functions first one is with type hints
def add_numbers(a: int, b: int) -> int:
    pass

def greet_user(name):
    pass

# === Main execution of code goes here ===
#  Code here will only run when this script is executed as the main program
if __name__ == "__main__":
    # Functions with Function Annotations (Type Hints)
    sum_result = add_numbers(10, 20)
    print("Result of addition:", sum_result)

    greeting = greet_user("Alice")
    print(greeting)

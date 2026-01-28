import sys

def add():
    final_result = 0
    while True:
        try:
            num_of_numbers = int(input("How many numbers do you want to add?(Must a number greater than 0, don't type the whole number, just the number. e.g: 0, 1, 2, etc.): "))
            if num_of_numbers <= 0:
                print("Number is equal or lower than 0")
                continue
            break
        except Exception as e:
             print(f"Invalid input, an error occured. Error message:{e}")
    if num_of_numbers == 0:
         print()
    while True:
        if num_of_numbers == 0:
            break
        for i in range(num_of_numbers):
            try:
                i = int(input("Type a number to be added:").strip())
            except:
                continue
            final_result = final_result + i
            num_of_numbers -= 1
        print(f"The result is: {final_result}")

def sub():
    final_result = 0
    while True:
        try:
            num_of_numbers = int(input("How many numbers do you want to subract?(Must a number greater than 0, don't type the whole number, just the number. e.g: 0, 1, 2, etc.): "))
            if num_of_numbers <= 0:
                print("Number is equal or lower than 0")
                continue
            break
        except Exception as e:
             print(f"Invalid input, an error occured. Error message:{e}")
    if num_of_numbers == 0:
         print()
    while True:
        if num_of_numbers == 0:
            break
        for i in range(num_of_numbers):
            try:
                i = int(input("Type a number to be added:").strip())
            except:
                continue
            final_result = final_result + i
            num_of_numbers -= 1
        print(f"The result is: {final_result}")


            
            


def quit():
    print("Quitting...")
    sys.exit()
add()


import data_fetcher

def temp():
    choice_1 = input("Hello! What city do you wish to know the temperature? (Type it without punctuation. e.g.: Sao Paulo)\n").strip().lower()
    
    
    info = data_fetcher.data()
    
    
    if choice_1 in info:
        result = info[choice_1] 
    else:
        result = None

    if result is not None:
        choice_2 = input("Would you like to see the temperature on celsius or fahrenheit? (c/f) ").strip().lower()
        
        if choice_2 == "f":
            
            converted_temp = fahrenheit(result)
            
            print(f"The temperature in {choice_1.title()} is {converted_temp:.1f}ºF")
            return
            
        elif choice_2 == "c":
            print(f"The temperature in {choice_1.title()} is {result}ºC")
            return
            
        else:
            print("Invalid unit selection. Defaulting to Celsius.")
            print(f"The temperature in {choice_1.title()} is {result}ºC")
            return
            
    else:
        print("City not found in the database. Would you like to try again? (y/n)")
        while True:
            continue_option = input("").strip().lower()
            if continue_option == "y":
                temp() 
                break
            elif continue_option == "n":
                print("Okay, returning to the main menu...")
                break
            else:
                print("Invalid option. The valid options are 'y' and 'n'. ")

def fahrenheit(value):
    value = (value * 1.8) + 32
    return value


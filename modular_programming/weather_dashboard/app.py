import data_fetcher
import formatter

def menu():
  print("=== WEATHER DASHBOARD APPLICATION ===") 
  print("Choose an option:")
  print("1- See the database to check for available cities to check temperature")
  print("2- Check a city temperature")
  print("3- Quit")
  while True:
    choice = input("")
    if choice == "1":
        value = data()
        print(value).strip("[]")
        break
    elif choice == "2":
        check()
        break
    elif choice == "3":
        quit()
    else:
        print("Invalid option")
    
    while True:
       menu()
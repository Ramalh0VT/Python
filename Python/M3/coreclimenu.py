import os
import shutil

def organize_folder():
    base = input("Folder to organize(type the whole path): ")
    while True:
        try:
               if not os.path.exists(base):
                   print("Folder not found.")
                   return
               print("The way the organizer works is that it puts image files on a specific folder, documents on a specific folder, and so on and so forth. Do you want to proceed?(y/N)")
               choice = input("")
               if choice.lower()  == "y":
     
                   folders = {
                       "Images": [".jpg", ".png", ".jpeg"],
                       "Documents": [".pdf", ".txt", ".docx"],
                       "Videos": [".mp4", ".mov"],
                       "Music": [".mp3"],
                       "Spreadsheets": [".csv", ".xlsx"]
                       }
                   for folder in folders:
                       path = os.path.join(base, folder)
                       if not os.path.exists(path):
                           os.mkdir(path)

                   moved = 0

                   for file in os.listdir(base):
                       file_path = os.path.join(base, file)

                       if os.path.isfile(file_path):
                           _, ext = os.path.splitext(file)

                           for folder, extensions in folders.items():
                               if ext.lower() in extensions:
                                   shutil.move(file_path, os.path.join(base, folder))
                                   moved += 1
                                   break

                   print(f"Done. {moved} files organized.")       
               elif choice.lower() == "n":
                print("Okay, going back to the main menu...")
               else:
                   print("Invalid answer, but going back to main menu anyway due to safety reasons")
    
        except Exception as e:
            print("Error:", e)

        input("Press Enter to return to menu")
        break
def bulk_rename():

    folder = input("Type the folder to rename files: ")
    while True:
        try:
            if not os.path.exists(folder)
                print("Folder not found.")
                return
            base_name = input("Base name (e.g. image, report): ")
            start = int(input("Starting number: "))

        
            count = start
            renamed = 0
            count_preview = count
            numerator_for_confirmation = 1
            renamed_preview = 0

            for file in os.listdir(folder):
                old_path_preview = os.path.join(folder, file)

                if os.path.isfile(old_path_preview)
                    _, ext_preview = os.path.splitext(file
                    new_name_preview  = f"{base_name}{count_preview}{ext_preview}"
                    new_path_preview = os.path.join(folder, new_name_preview)
                    print(f"{numerator_for_confirmation} {old_path_preview} -> {new_path_preview}")

            confirmation = input("Do you to proceed with described changes?(y/N)")

            if confirmation.lower() == "y":

                for file in os.listdir(folder):
                    old_path = os.path.join(folder, file)

                    if os.path.isfile(old_path):
                        _, ext = os.path.splitext(file)
                        new_name = f"{base_name}_{count}{ext}
                        new_path = os.path.join(folder, new_name)

                        os.rename(old_path, new_path)
                        count += 1
                        renamed +=1

            print(f"Done. {renamed} files renamed.")
            input("Press Enter to return to menu")
            break            

while True:
    print("\n=== File utility Tool ===")
    print("1 - Organize Folder")
    print("2 - Bulk rename files")
    print("3 - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Organizer selected")
        organize_folder()

    elif choice == "2":
        print("Renamer selected")
        bulk_rename()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")

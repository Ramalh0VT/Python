import os

folder = input("Folder(type the entire path):")

files = os.lisdir(folder)

count=1
for file in files:
	print(count, file)
	count += 1

listNames = [] # Empty list to store the names

# Store a name to list
def storeName(name):
 name = name.strip().title()
 if name in listNames:
  return False
 else:
  listNames.append(name)
  return True
 
# List all names
def printNames():
 print("-" * 30)
 for name in listNames:
  print(name)
print("-" * 30)

# Function to search for a name
def searchName(name):
 name = name.strip().title()
 flag = False
 for item in listNames:
  if name == item:
   flag = True
   break
 if flag == True:
  print("NAME IS PRESENT IN THE LIST")
 else:
  print("NAME IS NOT PRESENT IN THE LIST")

while True:
 print("Menu Options:")
 print("*" * 30)
 print("1. Enter a name: ")
 print("2. Search a name: ")
 print("3. List all names: ")
 print("4. EXIT")
 
 choice = int(input("Enter your choice: "))

 if choice == 1:
  userInp = input("Enter a name")
  retVal = storeName(userInp)
  if retVal == True:
   print("NAME ADDED SUCCESSFULLY")
  else:
   print("NAME EXISTS IN THE LIST")
 elif choice == 2:
  userInp = input("ENTER THE NAME TO BE SEARCHED")
  searchName(userInp)
 elif choice == 3:
  printNames()
 elif choice == 4:
  exit()
 else:
  print("INVALID OPTION, PLEASE CHOOSE A CORRECT OPTION!")
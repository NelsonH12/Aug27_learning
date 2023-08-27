pw_mster = input('Please enter your master password: ')

def view():
  with open('passwords.txt', 'r') as f:
    for line in f.readlines():
      print(line.rstrip()) #prevents the \n from being added while reading

def add():
  name = input('Account Name: ')
  pwd = input("Password: ")

  with open('passwords.txt', 'a') as f: #this opens the file and closes it when done
    f.write(name + '|' + pwd + '\n') #linebreak

while True:
    mode = input("Press a for new password, b to view, q to quit. ").lower()
    if mode == "q":
        break

    if mode == "b":
        view()
    elif mode == "a":
        add()
    else:
        print("Invalid entry.  Learn to read.")
        continue
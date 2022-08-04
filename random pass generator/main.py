import random as r
import string




def password_generator(count, u, l, n, s):
    password=""
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    special_chars = list(string.punctuation)

    
    for i in range(count):
        array =[]
        if u.lower()=="y":
            array.append(r.choice(upper_case))
        if l.lower()=="y":
            array.append(r.choice(lower_case))
        if n.lower()=="y":
            array.append(r.randint(0,9))
        if s.lower()=="y":
            array.append(r.choice(special_chars))   

        num = str(r.choice(array))
        password+=num

    return password 
   





print("Welcome to password generator")

numofchar = int(input("Enter the length of password you want: "))

upper = input("Do you want to include upper case characters, type y for yes and n for no: ")
lower = input("Do you want to include lower case characters, type y for yes and n for no: ")
number = input("Do you want to include numbers, type y for yes and n for no: ")
special = input("Do you want to include special characters, type y for yes and n for no: ")

if upper=="n" and lower=="n" and number=="n" and special=="n":
    print("Select at least one option")
    quit()

print("Your Password is: ")
print(password_generator(numofchar, upper, lower, number, special))

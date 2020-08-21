import os
import pyttsx3
pass1=0000
database={'Suyash':123}
def admin_account(m,n):
    if m in database:
        pyttsx3.speak("Great")
        pyttsx3.speak("Logic Successful")
        print("Logic Successful")
        print("---------------------------------------------------------------")
        print("I am your personal assistance Alex")
        print("Developed by Suyash Choudhari in 2020 in labs")
        pyttsx3.speak("How can I help. Below are the set of instructions.")
        print("---------------------------------------------------------------")
       
        while True:
            print("---------------------------------------------------------------")
            ls=print("List of instruction:\nPress * to Logout \nPress @ to access database \nPress < to know about myself \nPress # for chrome \nPress $ for notepad")
            print("---------------------------------------------------------------")
            s=input("what you want to know: ")
            print("---------------------------------------------------------------")
            if "your" in s and "name" in s or "<" in s:
                pyttsx3.speak("I am your personal assistance. Developed by Suyash in 2020")
                print("I am your personal assistance. Developed by Suyash in 2020")
                continue
           
            if "*" in s:
                pyttsx3.speak("Hope You Have Enjoyed with assistance.Thank you see you again")
                print("--------------------------")
                print("--------THANK YOU---------")
                print("--------------------------")
                loginpage()
                break
                
            if "#" in s:
                pyttsx3.speak("Redirecting You to the Chrome Browser")
                os.system("chrome")
                continue
            if "@" in s:
                pyttsx3.speak("Plz enter password to access Database")
                pas=int(input("Enter password: "))
                if pas==pass1:
                    pyttsx3.speak("Below is your Database")
                    print(database)
                continue
    
    if m not in database:
        print("Your not resgistered with us")
        pyttsx3.speak("Please follow below procedure to registered with us")
        new_name=input("Enter your First Name: ")
        password=input("Enter your Password : ")
        mo=int(input("Mobile no: "))
        database[new_name] = password
        pyttsx3.speak("Thank you For registration. Directing You to the login page")
        loginpage()


def loginpage():
    pyttsx3.speak("Plz login with your name and password: ")
    print("------------------------")
    print("_______Login-Page_______")
    print("------------------------")
    m=input("Name: ")
    n=input("Password: ")
    q=admin_account(m,n)

loginpage()



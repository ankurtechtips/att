# ATM
accbal=9000
atmbal=8000
trans = list()
def atm():
    global accbal
    global atmbal
    global trans
    global w
    
    print("Enter an amount to withdraw: ", end="")
    w = int(input())
    if w > accbal:
        print("Low account balance")
    elif w > atmbal:
        print("Amount cannot be disbursed. ATM low on cash")
    elif w % 100==0:
        accbal=accbal-w
        atmbal=atmbal-w
        print("Amount withdrawled = ",w)
        print("Account balance = ",accbal)
        trans.append(w)
        print("Do you want to withdraw again (Y/N) : ", end="")
        b = input("")
        if b == "Y":
            mon()
        else:
            print("Thankyou for using ATM")
    else:
        print("Please enter valid amount")
    
    print("Do you want to see last 3 transactions (Y/N) : ", end="")
    a = input("")
    if (a == "Y"):
        print(trans[-3:])
    elif (a == "N"):
        print("Thankyou for using ATM")
atm()

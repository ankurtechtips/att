# ATM with PIN
accbal=9000
atmbal=8000
c=0
trans = list()
def atm():
    global accbal
    global atmbal
    global trans
    global w
    global c
    print("Enter your ATM PIN: ", end="")
    q = int(input())
    if q == 9999:
        c=0
        print("Press 1 for withdrawl: \tPress 2 for Deposit: \tPress 3 for Mini Statement: ", end="")
        x = int(input())
        if x==1:
            print("Enter an amount to withdrawl: ", end="")
            w = int(input())
            if w > accbal:
                print("Low account balance")
            elif w > atmbal:
                print("Amount cannot be disbursed. ATM low on cash")
            elif w % 100==0:
                accbal=accbal-w
                atmbal=atmbal-w
                print("Amount withdrawled = ", w)
                print("Account balance = ", accbal)
                trans.append(w)
                print("Do you want to withdrawl again (Y/N) : ", end="")
                a = input("")
                if a == "Y":
                    atm()
                else:
                    print("Do you want to see last 3 transactions (Y/N) : ", end="")
                    b = input("")
                    if b == "Y":
                        print(trans[-3:])
                        print("Thankyou for using ATM")
                    else:
                        print("Thankyou for using ATM")
            else:
                print("Please enter valid amount")
        elif x==2:
            print("Enter an amount to deposit: ", end="")
            d = int(input())
            accbal=accbal+d
            print("Account balance: ", accbal)
            atmbal=atmbal+d
            print("Thankyou for using ATM")
        elif x==3:
            print("MINI STATEMENT: ")
            print(trans[-10:])
            print("Thankyou for using ATM")
        else:
            print("Invalid option")
    else:
        if c < 2:
            print("Invalid PIN")
            c += 1
            atm()
        elif c == 2:
            print("ATM Card blocked. Please visit nearest branch")
        else:
            pass
atm()

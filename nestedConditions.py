def atm():
    balance = 5000 
    pin = 1234
    print("welcome,please type in your pin number:")
    user pin = int(input())
    if userPin = pin:
        print("what would you like to do?")
        print("1. Withdraw money")
        print("2. Deposit money")
        print("3. Check Balance ")
        select= int(input("please select an option:"))
        if select == 1:
            print("how much would you like to withdraw?")
            amount = int (input())
            if amount > balance:
                print("Overdraft alert")
            else:
                newBalance = balance - amount 
                print("you are takimg out: " + str(amount))
                print("you have this amount left" + str (newBalance))

            elif select == 2:
            print('how much money do you want to deposit?')
            amount = int())
            newBalance + amount
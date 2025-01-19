name = input("please enter your name : ") 
print("Hello ",name)

message = """
Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL.
"""
print(message)
available_amount = 5000
task = int(input("enter your option : "))
if task >= 1 and task <=3:
    print("welcome to you in virtual bank")
    if task == 1:
        print("Your available balance is  : ",available_amount)
    elif task == 2 :
        deposit_amont = int(input("plz enter deposite amount : "))
        if deposit_amont >= 500:
            available_amount += deposit_amont
            print("your money is successfully deposited : ",deposit_amont)
            print("Your available balance is  : ",available_amount)
        else:
            print("plz enter atleast 500 INR")
    else:
        print('withdrawl program')
        withdrawl_amount =int(input("please inter witdrowal_amount : "))
        if withdrawl_amount <= available_amount:
            available_amount -= withdrawl_amount
            print("your money is succesfully withdrawaled : ",withdrawl_amount)
            print("your availablebalence is :",available_amount)
        else:
            print("no suffiecint balance")

    

else:
    print("plz enter valid input in btwn 1 to 3")







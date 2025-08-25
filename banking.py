print("enter your name :", end='')
name = input()

print("enter your account id :", end='')
id = input()

print("enter your account type (savings(1), current(2)) :", end='')
accounttyp = float(input())

print("enter your account balance :", end='')
balance = float(input())

print("hello", name)
print("your id is", id)
print("your account type is", accounttyp)
print("your account balance is", balance)

if accounttyp == 1:
    withdraw_amount = int(input("enter the withdraw amount :"))
    new_balance = balance - withdraw_amount

    if new_balance < 500:
        print("insufficient balance")
    elif withdraw_amount > balance:
        print("withdraw limit exceeded")
    else:
        print("your new balance is :", new_balance)
        print("thank you for using our services")
elif accounttyp == 2:
    withdraw_amount = int(input("enter the withdraw amount :"))
    new_balance = balance - withdraw_amount
    if new_balance < 0:
        print("insufficient balance")
    elif withdraw_amount > balance:
        print("withdraw limit exceeded")
    else:
        print("your new balance is :", new_balance)
        print("thank you for using our services")
else:
    print("invalid account")
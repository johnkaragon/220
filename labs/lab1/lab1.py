def interest_calc():
    print("This is a program that will calculate the interest due on a credit account.")
    AIR = eval(input("what is the annual interest rate? "))
    bill_days = eval(input("How many days are in the billing cycle? "))
    balance = eval(input("What is the net balance of the account? $"))
    pay = eval(input("How much was paid? $"))
    pay_day = eval(input("on what day of the billing cycle? "))
    fin = ((bill_days * balance) - (pay * (bill_days - pay_day))) / bill_days
    interest = fin * (AIR / 100)
    print("Your interest due is: ", interest)

interest_calc()
bill_amount = float(input("Enter your Bill Amount: "))

if bill_amount >= 50000:
    print(f"You got 30% discount")
    final_bill = bill_amount - ((bill_amount*30)/100)
    print(f"Your final bill is RS. {final_bill}")
elif bill_amount >= 40000 and bill_amount <= 49999:
    print(f"You got 25% discount")
    final_bill = bill_amount - ((bill_amount*25)/100)
    print(f"Your final bill is RS. {final_bill}")
elif bill_amount >= 30000 and bill_amount <= 39999:
    print(f"You got 20% discount")
    final_bill = bill_amount - ((bill_amount*20)/100)
    print(f"Your final bill is RS. {final_bill}")
elif bill_amount >= 10000 and bill_amount <= 29999:
    print(f"You got 10% discount")
    final_bill = bill_amount - ((bill_amount*10)/100)
    print(f"Your final bill is RS. {final_bill}")
else:
    print(f"Sorry! You haven't got any discount!")
    print(f"Your final bill is RS. {bill_amount}")

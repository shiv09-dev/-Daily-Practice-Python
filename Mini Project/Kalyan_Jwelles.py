name = input("Enter your name : ")
gender = input("Enter your gender : ('M' for Male and 'F' for Female ) : ")
age = int(input("Enter your age : "))

product = input("Enter the Product you want to buy : ")
weight = int(input("Enter the weight of product you want in grams : "))

gold_price = 5752

making_charges = 845

total_gold_rate = weight * gold_price

total_making_charges = weight * making_charges

if gender == 'M' or gender == 'm':

    if age >= 65:

        if total_gold_rate >= 21000 and total_gold_rate < 31000:
            discount  = 0.20
        elif  total_gold_rate >= 31000 and total_gold_rate < 51000:
            discount = 0.30
        elif total_gold_rate >= 51000:
            discount = 0.35

    else:
        if total_gold_rate >= 21000 and total_gold_rate < 31000:
            discount  = 0.10
        elif  total_gold_rate >= 31000 and total_gold_rate < 51000:
            discount = 0.20
        elif total_gold_rate >= 51000:
            discount = 0.25

elif gender == 'F' or gender == 'f':

    if age >= 65:

        if total_gold_rate >= 21000 and total_gold_rate < 31000:
            discount  = 0.25
        elif  total_gold_rate >= 31000 and total_gold_rate < 51000:
            discount = 0.35
        elif total_gold_rate >= 51000:
            discount = 0.40

    else:
        if total_gold_rate >= 21000 and total_gold_rate < 31000:
            discount  = 0.15
        elif  total_gold_rate >= 31000 and total_gold_rate < 51000:
            discount = 0.25
        elif total_gold_rate >= 51000:
            discount = 0.30
else:
    discount = 0.25

print()
print("Name : ", name)
print("Gender :  ", gender)
print("Age : ", age)
print("Your Selected Product is : ", product)
print("Your Selected weight of the Jwellery : ", weight , "grams")
print()

print("Total Gold Rate after adding selected weight : ", total_gold_rate)
print()

print("Total Making Charges : ", total_making_charges)
print()

total_amount = total_gold_rate + total_making_charges
print("Total Amount of the Jwellery : ", total_amount)
print()

total_discount = total_gold_rate * discount
print("Total discount Applied is : ", total_discount)
print()

final_price = total_amount - total_discount
print("Final Discounted Price : ", final_price)
print()







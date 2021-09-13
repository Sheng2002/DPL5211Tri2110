# Student ID: 1201200814
# Student Name: Tan Zhi Sheng
bananacomb = 1.5
grapes = 5.6
print("Invoice for Fruits Purchase")
print("---------------------------------")
print("")

banana = float(input("Enter the quantity (comb) of banana bought: "))
grape = float(input("Enter the amount (kg) of grapes bought : "))

print("Item \t\t Qty \t Price \t Total")
print("Banana (combs) \t ",banana," \t RM{} \t RM{}".format(bananacomb,bananacomb*banana))
print("Grapes (kg) \t ",grape," \t RM{} \t RM{}".format(grapes,grapes*grape))
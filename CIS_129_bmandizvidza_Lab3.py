#Define prices

Coffee_Price=5
Muffins_Price=4
Tax_Rate=0.06

#Get User Input


Coffees=float(input("Enter the number of Coffees"))
Muffins=float(input("Enter the number of Muffins"))

#Calculation


Coffee_cost=Coffees*Coffee_Price
Muffin_cost=Muffins*Muffins_Price
subtotal= Coffee_cost+Muffin_cost
tax=Tax_Rate*subtotal
total=subtotal+tax

#Display results
print("*****************************")
print("Brendo's Coffee&Muffin Shop \nReceipt")
print("******************************")
print("Number of Coffees selected at $5 each: ",Coffees)
print("Number of Muffins selected at $8 each:",Muffins)
print("******************************")
print("COFFEE.....",Coffees * Coffee_Price)
print("MUFFINS....",Muffins*Muffins_Price)
print("TOTAL....",total)

print("Thanks for shopping!")
print('Have a nice day!')
print("************THANK YOU!!!!*****************")

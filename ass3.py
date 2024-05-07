def calculateDiscount(price, discountPercent):
    if discountPercent>=20:
        discountedPrice=price-(price*discountPercent/100)
        return discountedPrice
    else:
        return price
    
#prompting the user for input
originalPrice=float(input("Enter the original price of the item: "))
discountPercent=float(input("Enter the discount percentage: "))

#calculating the final price
finalPrice=calculateDiscount(originalPrice,discountPercent)

#printing final price
print("Final price after applying the discount:ksh"+ str(finalPrice))
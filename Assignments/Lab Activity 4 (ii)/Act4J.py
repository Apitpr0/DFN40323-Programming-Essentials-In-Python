#create a tuple of your wishlist item
myWishlist = ("Heaven", "Lots of money", "Happiness")
print(myWishlist)

#access the third item in a tuple
print(myWishlist[2])  #direct access and display

thirdel = myWishlist[2]  #access & store in another variable
print(thirdel)

#change the 2nd element to a new item
wishListNew = list(myWishlist)  #convert the tuple into list first
wishListNew[1] = "Married"  #change the element in the list
myWishlist = tuple(wishListNew)  #convert the list into tuple
print(myWishlist)

#add on a new wishlist to the last element of tuple
wishListNew = list(myWishlist)  #convert the tuple into list first
wishListNew.append("big house")  #add the element in the list using list method
myWishlist = tuple(wishListNew)  #convert the list into tuple
print(myWishlist)

#add on a new wishlist to the last element of tuple
wishListNew1 = list(myWishlist)  #convert the tuple into list first
wishListNew1.insert(
    2, "big family")  #insert the element in the lis using list method
myWishlist = tuple(wishListNew1)  #convert the list into tuple
print(myWishlist)

#remove the last element in the tuple
wishListNew2 = list(myWishlist)  #convert the tuple into list first
wishListNew2.pop()  #remove the element in the list using list method
myWishlist = tuple(wishListNew2)  #convert the list into tuple
print(myWishlist)

#delete the tuple
del myWishlist
print(myWishlist)

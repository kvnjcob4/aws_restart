# print("-------If-else-------")
# userReply = input("Do you need to ship package ? - (enter yes or no) - ")
# if userReply == "yes":
#     print("We can help you ship that package.")
# else:
#     print("Please come back when you are ready to ship the package.")
   
    
print("-------elif----------")

userReply = input("Would you like to buy stamps, buy an envelope or make a copy? - (Enter stamps, envelope or copy) - \n") 
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like to take ? - (Enter the number) - ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
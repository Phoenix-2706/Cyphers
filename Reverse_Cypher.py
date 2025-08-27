message=input("Enter the message: ")
a=len(message)-1
translated=''

#Concatinate the message one by one from reverse
while a>=0:  
    translated+=message[a]
    a-=1

print("Your reversed message is: %s" % (translated))
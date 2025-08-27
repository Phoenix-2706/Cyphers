message=input("Enter the message: ")
a=len(message)-1
translated=''

while a>=0:
    translated+=message[a]
    a-=1

print("Your reversed message is: %s" % (translated))
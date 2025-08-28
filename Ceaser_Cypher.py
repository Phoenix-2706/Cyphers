alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encryption(message,key):
    global alphabets
    print(alphabets)
    final_message=''
    message=message.upper()
    for i in message:
        print(i)
        m=alphabets.find(i)
        m+=key
        if m>len(alphabets)-1:
            m-=len(alphabets)
        else:
            m=m
        final_message+=alphabets[m]
    print("Your encrypted message is:\t%s"%(final_message))    

def decryption(message):
    message=message.upper()
    for key in range(len(alphabets)):
        final_message=''
        for i in message:
            m=alphabets.find(i)
            m-=key
            if m<0:
                m+=len(alphabets)
            else:
                m=m
            final_message+=alphabets[m]
        print("Decrypted message using key%s:\t%s"%(key,final_message))
        
    

if __name__ =='__main__':
    mode=input("(e) for encryption : (d) for decryption -->\t")
    if mode=='e':
        encrypted_message=input("Enter the message to be encrypted:\t")
        key=int(input("Enter the key (0-25):\t"))
        encryption(encrypted_message,key)
    elif mode=='d':
        decrypted_message=input("Enter the message to be decrypted:\t")
        decryption(decrypted_message)
    else:
        print("Please enter the correctly")
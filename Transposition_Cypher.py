def encryption(message,key):
    a=['']
    j=0
    a*=key
    for i in range(key):
        while j<len(message):
            a[i]+=message[j]
            j+=key
        j= i+1
    translate = ''.join(a)
    print("Encrypted Message is:\t%s|" % (translate))

#This still needs some fixing
def decryption(message):
    for i in range(1,len(message)+1):
        a=['']
        k=0
        rounded = round(len(message)/i)
        a*=rounded
        for j in range(rounded):
            while k<len(message):
                a[j]+=message[k]
                k+=rounded
            k=j+1
        translate=''.join(a)
        print("Decrypted message using key%s :\t%s" % (i,translate))


if __name__ =='__main__':
    mode=input("(e) for encryption : (d) for decryption -->\t")
    if mode=='e':
        encrypted_message=input("Enter the message to be encrypted:\t")
        key=int(input("Enter the key:\t"))
        encryption(encrypted_message,key)
    elif mode=='d':
        decrypted_message=input("Enter the message to be decrypted:\t")
        decryption(decrypted_message)
    else:
        print("Please enter the letter correctly")

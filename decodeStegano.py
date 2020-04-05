import cv2

def decrypt(msg,password):
    msgList = list(msg)
    pswdList = list(password)
    msglen = len(msgList)
    pswdlen = len(pswdList)

    pswdPos = 0
    for i in range(msglen):
        if(pswdPos==len(pswdList)):
            pswdPos=0
        msgList[i]= chr(ord(msgList[i])-ord(pswdList[pswdPos]))
        pswdPos+=1

    return (''.join(msgList))

def decode(password,inputImg = 'output.png'):
    img = cv2.imread(inputImg)

    height,width,channels = img.shape

    def jointomsg(imgbit):
        ans = ((imgbit[0]&7)<<5)|((imgbit[1]&7)<<2)|(imgbit[2]&3)
        return ans

    msglen = jointomsg(img[0,0])

    c=0
    f=0
    msg=''
    for i in range(height):
        for j in range(1,width):
            if(c==msglen):
                f=1
                break
            msg+=chr(jointomsg(img[i,j]))
            c+=1
        if(f==1):
            break

    finalMsg = decrypt(msg,password)
    return(finalMsg)

def main():
    password = input('Enter password: ')
    print('hidden message is :',decode(password))

if __name__ == '__main__':
    main()
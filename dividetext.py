def devideMessage(message, divnum):
    out ={}
    for m in range(0,divnum):
        out[m]=""


    for i in range(0,divnum):
        for j in range(0,len(message)):
            if(j%divnum==i):
                out[i]+=message[j]

    for i in range(0,divnum):
        print(out[i])

if __name__=="__main__":
    devideMessage("dasdas",2)
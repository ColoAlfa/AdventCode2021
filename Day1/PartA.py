def read():
    with open("input.txt","r") as f:
        data=f.read()
    clearData=data.split('\n')
    print(clearData, "Before POP")
    clearData.pop()
    intData=[]
    for number in clearData:
        intData.append(int(number))
    print(intData)
    return intData

def problemA():
    data=read()
    result=[]
    count=0
    for i in range(len(data)):

        if i >0:
            if data[i]<data[i-1]:
                result.append(str(data[i])+ " (decreased)")
            else:
                count+=1
                result.append(str(data[i])+ " (increased)")
        else:
            result.append(str(data[i])+ " (N/A - no previous measurement)")
    print(result)
    print("INCREASES: ",count)
    resultFile=open('result.txt','x')
    for lecture in result:
        resultFile.writelines(lecture + "\n")
    resultFile.close

def problemB():
    data=read()
    result=[]
    count=0
    for i in range(len(data)-3):
        Comp1=data[i]+data[i+1]+data[i+2]
        Comp2=data[i+1]+data[i+2]+data[i+3]
        if Comp2>Comp1:
            count+=1
            result.append(str(Comp1)+ " (increased)")
    print(result)
    print("INCREASES: ",count)
    resultFile=open('resultB.txt','x')
    for lecture in result:
        resultFile.writelines(lecture + "\n")
    resultFile.close


problemB()
problemA()
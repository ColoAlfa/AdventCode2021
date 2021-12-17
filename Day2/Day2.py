def read():
    with open("input.txt","r") as f:
        data=f.read()
    clearData=data.split('\n')
    #print(clearData, "Before POP")
    clearData.pop()
    separatedData=[]
    for pair in clearData:
        separatedData.append(pair.split(' '))
    #print(separatedData)
    for index in range(len(separatedData)):
        separatedData[index]=[separatedData[index][0],int(separatedData[index][1])]
    #print(separatedData)
    return separatedData

def partA():
    data=read()
    horizontal=0
    depth=0
    for pair in data:
        if pair[0]=='forward':
            horizontal= horizontal+ pair[1]
        elif pair[0]=='up':
            depth= depth- pair[1]
        elif pair[0]=='down':
            depth= depth+ pair[1]
    result=horizontal*depth
    print("\n RESULT of PartA: ",result)

def partB():
    data=read()
    horizontal=0
    depth=0
    aim=0
    for pair in data:
        if pair[0]=='forward':
            horizontal= horizontal+ pair[1]
            depth=depth+aim*pair[1]
        elif pair[0]=='up':
            aim= aim- pair[1]
        elif pair[0]=='down':
            aim= aim+ pair[1]
    result=horizontal*depth
    print("\n RESULT of PartB: ",result)

partA()
partB()

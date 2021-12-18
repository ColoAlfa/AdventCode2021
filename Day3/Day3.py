def read():
    with open('input.txt', 'r') as file:
        data = file.read()
    clearData = data.split('\n')
    clearData.pop()
    numberList = []
    for number in clearData:
        numberList.append(list(number))
    #print(numberList)
    return numberList


def problemA():
    data = read()
    maxCount = []
    minCount = []
    counter1 = 0
    counter0 = 0
    gammaRate = 0
    epsilonRate = 0
    valor = 11
    for bit in range(len(data[0])):
        for number in data:
            if number[bit] == '1':
                counter1 = counter1+1
            if number[bit] == '0':
                counter0 = counter0+1
        if counter1 > counter0:
            print("The result of counter 1 is: ", counter1,
                  "The result of counter 0 is: ", counter0)
            maxCount.append(1)
            minCount.append(0)
        elif counter1 < counter0:
            print("The result of counter 1 is: ", counter1,
                  "The result of counter 0 is: ", counter0)
            maxCount.append(0)
            minCount.append(1)
        counter0 = 0
        counter1 = 0
    print('MaxCount is: ', maxCount,
          'MinCount is: ', minCount)

    for index in range(len(maxCount)):
        gammaRate = gammaRate + 2**valor*maxCount[index]
        epsilonRate = epsilonRate + 2**valor*minCount[index]
        valor -= 1
    powerConsumption = gammaRate*epsilonRate
    print('Valor de gamma: ', gammaRate, 'valor de epsilon: ',
          epsilonRate, '\n Total PowerConsumption: ', powerConsumption)

def problemB():
    
    """"
    Tenemos que detectar el valor de bit mas común, una vez lo tenemos nos quedaremos
    con los numeros que tengan ese valor en ese mismo bit, y así hasta que solo quede uno.

    OXYGEN GENERATOR RATING
    """
    #Variables Zone:
    data=read()
    count1=0
    count0=0
    oxygenGeneratorRating=[]
    CO2ScrubberRating=[]
    valor=11
    oxygenVal=0
    CO2Val=0

    #Maximum
    for index in range(len(data[0])):
        for number in data:
            if number[index]=='1':
                count1+=1
            else:
                count0+=1
        if count1>=count0:
            for number in data:
                if number[index]=='1':
                    oxygenGeneratorRating.append(number)
        else:
            for number in data:
                if number[index]=='0':
                    oxygenGeneratorRating.append(number)
        data=oxygenGeneratorRating
        oxygenGeneratorRating=[]
        count0=0
        count1=0
    print("The Oxygen Generator Rating is: ",data)
    oxygenGeneratorRating=data
    data=read()
    #print(data)
    #Minimun
    for index in range(len(data[0])):
        if(len(data)==1):#Aquí nos aparece un error que antes no debido  aque cuando solo quede uno
            break        #El valor que queremos sera ese uno que queda no el que tenga menos pork no hay. 
        for number in data:
            if number[index]=='1':
                count1+=1
            else:
                count0+=1
        
        if count1<count0:
            for number in data:
                if number[index]=='1':
                    CO2ScrubberRating.append(number)
        else:
            for number in data:
                if number[index]=='0':
                    CO2ScrubberRating.append(number)
        
        #print("loop:", index, "value",data)
        data=CO2ScrubberRating
        CO2ScrubberRating=[]
        count0=0
        count1=0
        
    CO2ScrubberRating=data  
    print(CO2ScrubberRating)
    print(oxygenGeneratorRating) 

    for index in range(len(CO2ScrubberRating[0])):
        oxygenVal=oxygenVal+int(oxygenGeneratorRating[0][index])*2**valor
        CO2Val=CO2Val+int(CO2ScrubberRating[0][index])*2**valor
        valor-=1
    
    print("The CO2 Scrubber Rating is: ",CO2Val, "\n the Oxygen Generator Rating is: ", oxygenVal)
    result=oxygenVal*CO2Val
    print("The result is: ",result)
problemB()



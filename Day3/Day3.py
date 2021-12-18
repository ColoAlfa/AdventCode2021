def read():
    with open('input.txt', 'r') as file:
        data = file.read()
    clearData = data.split('\n')
    clearData.pop()
    numberList = []
    for number in clearData:
        numberList.append(list(number))
    print(numberList)
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


problemA()

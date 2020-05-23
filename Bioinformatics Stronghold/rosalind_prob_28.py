import math

def RandomString(strRandomString, stringArray):
    strRandomString = strRandomString.upper()
    cg = len(strRandomString.replace('A', '').replace('T', ''))
    at = len(strRandomString.replace('C', '').replace('G', ''))
    inputArray = stringArray.split()
    outputArray = []
    for i in range(0, len(inputArray)):
        prob = cg * math.log10(float(inputArray[i]) / 2) + at * math.log10((1 - float(inputArray[i])) / 2)
        outputArray.append(round(prob, 3))
    return outputArray


result = ' '.join(map(str, RandomString('GCGCCTCCTACATCTTATACCACTCGAGGAGCTCCTTAATATCCCAGTTGTGAGTTCATTCAACGTCAAATCACTGCAGATGAT', '0.075 0.133 0.184 0.215 0.299 0.348 0.387 0.465 0.501 0.527 0.596 0.661 0.711 0.755 0.832 0.851 0.923')))

f = open('output.txt', 'w')
f.write(result)  
f.close()
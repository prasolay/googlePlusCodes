import pandas as pd
import math

def codeDigit(inputNmuber):
    google_plus_code_dict = {
        0: '2',
        1: '3',
        2: '4',
        3: '5',
        4: '6',
        5: '7',
        6: '8',
        7: '9',
        8: 'C',
        9: 'F',
        10: 'G',
        11: 'H',
        12: 'J',
        13: 'M',
        14: 'P',
        15: 'Q',
        16: 'R',
        17: 'V',
        18: 'W',
        19: 'X'
    }
    outputnumber = google_plus_code_dict[inputNmuber]

    return outputnumber

def calculateNmuber(inputY, inputX):
    yo = inputY + 90
    xo = inputX + 180

    y1 = math.floor(yo/20)
    y2 = math.floor((yo-y1*20)/1)
    y3 = math.floor(((yo-y1*20)-y2*1)/0.05)
    y4 = math.floor((((yo-y1*20)-y2*1-y3*0.05)/0.0025))
    y5 = math.floor((((yo-y1*20)-y2*1-y3*0.05-y4*0.0025)/0.000125))

    x1 = math.floor(xo/20)
    x2 = math.floor((xo-x1*20)/1)
    x3 = math.floor(((xo-x1*20)-x2*1)/0.05)
    x4 = math.floor((((xo-x1*20)-x2*1-x3*0.05)/0.0025))
    x5 = math.floor((((xo-x1*20)-x2*1-x3*0.05-x4*0.0025)/0.000125))

    numberDict = {
        "zoom1":x1,
        "x2":x2,
        "x3":x3,
        "x4":x4,
        "x5":x5,
        "y1":y1,
        "y2":y2,
        "y3":y3,
        "y4":y4,
        "y5":y5
    }

    numberList = [[y1, x1], [y2, x2], [y3, x3], [y4, x4], [y5, x5]]

    return numberList   

def finalGooglePlusCode(numberList):
    googlePlusCode = ""
    for i in numberList:
        y = codeDigit(i[0])
        x = codeDigit(i[1])
        googlePlusCode = googlePlusCode + y + x
    
    return googlePlusCode
    






if __name__ == '__main__':
    print("hello world!")
    print("-----------------------------")

    y = 1.2867970586693043
    x = 103.85451499941605

    numberList = calculateNmuber(1.2867970586693043, 103.85451499941605)
    googlePlusCode = finalGooglePlusCode(numberList)
    print(googlePlusCode)


    #測試區域-魚尾獅噴泉 (北緯1.286785°，東經103.854503°。）
    #1.2867970586693043, 103.85451499941605
    #正確的回傳資料：6PH57VP3+PR
    # yo = 1.2867970586693043
    # xo = 103.8545149994160

    # y1 = (math.floor((90+yo)/20))
    # print("y1:")
    # print(y1)
    # print("-----------------------------")
    # x1 = (math.floor((180+xo)/20))
    # print("x1:")
    # print(x1)

    # print("-----------------------------")
    # print("y2:")
    # y2 = math.floor(((90+yo)-y1*20)/1)
    # print(y2)

    # print("-----------------------------")
    # print("y3:")
    # y3 = math.floor((((90+yo)-y1*20)-y2*1)/0.05)
    # print(y3)

    # print("-----------------------------")
    # print("y4:")
    # y4 = math.floor(((((90+yo)-y1*20)-y2*1-y3*0.05)/0.0025))
    # print(y4)

    # print("-----------------------------")
    # print("y5:")
    # y5 = ((((90+yo)-y1*20)-y2*1-y3*0.05-y4*0.0025)/0.000125)
    # print(y5)

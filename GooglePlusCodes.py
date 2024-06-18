import pandas as pd

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







if __name__ == '__main__':
    print("hello world!")

def string(msg, digit=""):
    while True:
        try:
            while digit == "" or digit.isnumeric():
                digit = str(input(msg)).title().strip()
                if digit == "" or digit.isnumeric():
                    print("\033[1;31mInvalid value \033[4;31m{digit}\033[m")
        except:
            print("\033[1;31mValor inválido\033[m")
        else:
            return digit
def value(msg):
    while True:
        try:
            value = float(input(msg))
        except:
            print("\033[1;31mInvalid value \033[4;31m{value}\033[m")
        else:
            return value


def enum(msg):
    while True:
            sex = str(input(msg)).strip().title()[0]
            if sex == "" or sex != "M" or sex != "F":
                print("\033[1;31mInvalid value \033[4;31m{sex}\033[m")
            else:    
                return sex           


def date(msg):
    while True:
        birth = str(input(msg)).strip()
        if birth[4] == "-" and birth[7] == "-":
            return birth
        else:
            print("\033[1;31mInvalid value \033[4;31m{birth}\033[m")
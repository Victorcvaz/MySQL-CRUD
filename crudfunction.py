def product(msg, digit=""):
    while True:
        try:
            while digit == "" or digit.isnumeric():
                digit = str(input(msg)).capitalize().strip()
                if digit == "" or digit.isnumeric():
                    print("\033[1;31mValor inválido\033[m")
        except:
            print("\033[1;31mValor inválido\033[m")
        else:
            return digit
def value(msg):
    while True:
        try:
            valor = float(input(msg))
        except:
            print("\033[1;31mValor inválido\033[m")
        else:
            return valor
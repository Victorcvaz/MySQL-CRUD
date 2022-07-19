import crudfunctions.valid as valid


def init():
    print()
    comands = ["INSERT INTO", "SELECT", "UPDATE", "DELETE", "0"]
    print('\033[1;34m_\033[m' *18)
    for i, v in enumerate(comands):
        print(f"\033[1;34m{i+1:<4}\033[m-> \033[1;36m{v}\033[m")
    print('\033[1;34m_\033[m' *18)
    while True:
        print()
        comand = valid.value("\033[4;32mType an option for the operation you want \033[m")
        print()
        if comand >= 0 and comand < 5:
            return comand


def create(pointer, conect):
    name = valid.product("\033[1;34mEnter the product name: \033[m")
    value = valid.value("\033[1;36mEnter the product value: \033[m")
    comand = f'INSERT INTO products (product, value) VALUES ("{name}", {value})'
    pointer.execute(comand)
    conect.commit() # edit the database
    print(f"Product \033[1;32m{name}\033[m in the value of \033[1;32m{value}\033[mR$ added successfully!")


def select(pointer):
    comand = f"SELECT * FROM products"
    pointer.execute(comand)
    result = pointer.fetchall()
    print('\033[1;32m_\033[m' *30)
    print(f"\033[7;33m{'ID':<2}\033[m\033[7;32m{'Name':^20}\033[m\033[7;37m{'Price'}\033[m")
    print()
    for i, v in enumerate(result):
        for g, u in enumerate(v):
            if g == 0:
                print(f"\033[7;33m{u:<2}\033[m", end="")
            if g == 1:
                print(f"\033[7;32m{u:^20}\033[m", end="")
            if g == 2:
                print(f"\033[7;37m{u:.2f}\033[m", end="") 
        print()
    print('\033[1;32m_\033[m' *30)


def update(pointer, conect):
    ask = valid.product("\033[1;32mYou want change name or value? type [Name(N), Value(V)] \033[m")
    if ask[0] == 'N':
        name = valid.product("\033[1;34mEnter the product name to update: \033[m")
        changename = valid.product("\033[1;34mEnter the new name: \033[m")
        comand = f'UPDATE products SET product = "{changename}" WHERE product = "{name}"'
        print(f"\033[1;32m{name}\033[m set to \033[1;31m{changename}\033[m successfully!")
    else:
        name = valid.product("\033[1;36mEnter the product name to update: \033[m")
        changevalue = valid.value("\033[1;36mEnter the new value: \033[m")
        comand = f'UPDATE products SET value = {changevalue} WHERE product = "{name}"'
        print(f"\033[1;32m{name}\033[m set to \033[1;32m{changevalue}\033[m successfully!")
    pointer.execute(comand)
    conect.commit() 


def delete(pointer, conect):
    ask = valid.product("\033[1;32mEnter the name of the product a be delete \033[m")
    comand = f'DELETE FROM products WHERE product = "{ask}"'
    print(f"\033[1;31m{ask}\033[m delete successfully!")
    pointer.execute(comand)
    conect.commit() 


    


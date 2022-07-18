import crudfunctions.valid as valid

def create(pointer, conect):
    name = valid.product("\033[1;34mEnter the product name: \033[m")
    value = valid.value("\033[1;36mEnter the product value: \033[m")
    comand = f'INSERT INTO products (product, value) VALUES ("{name}", {value})'
    pointer.execute(comand)
    conect.commit() # edit the database
    print(f"\033[1;32mProduct {name} in the value of {value}R$ added successfully!\033[m")


def select(pointer):
    comand = f"SELECT * FROM products"
    pointer.execute(comand)
    result = pointer.fetchall()
    print(f"\033[1;34m{result}\033[m")


def update(pointer, conect, ask=""):
    ask = valid.product("\033[1;32mYou want change name or value? type [Name(N), Value(V)] \033[m")
    if ask[0] == 'N':
        name = valid.product("\033[1;34mEnter the product name to update: \033[m")
        changename = valid.product("\033[1;34mEnter the new name: \033[m")
        comand = f'UPDATE products SET product = "{changename}" WHERE product = "{name}"'
    else:
        name = valid.product("\033[1;36mEnter the product name to update: \033[m")
        changevalue = valid.value("\033[1;36mEnter the new value: \033[m")
        comand = f'UPDATE products SET value = {changevalue} WHERE product = "{name}"'
    pointer.execute(comand)
    conect.commit() 
    

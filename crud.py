import mysql.connector
import crudfunction


while True:
    conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bullshit'
)
    cursor = conexao.cursor()

    # CRUD
    nomeproduto = crudfunction.product("\033[1;34mDigite o nome do produto: \033[m")
    valor = crudfunction.value("\033[1;36mDigite o valor do produto: \033[m")
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nomeproduto}", {valor})'
    cursor.execute(comando)
    conexao.commit() # edit the database
    # resultado = cursor.fetchall() # read database



    cursor.close()
    conexao.close()
    print(f"\033[1;32mProduto {nomeproduto} no valor de {valor}R$ adicionado com sucesso!\033[m")
    msg = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if msg == 'N':
        break

# CREATE
# READ
# UPDATE
# DELETE

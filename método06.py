import os
os.system('cls')

produtos = ['tv','smartphone', 'geladeira','mouse','teclado']
estoque = [200, 350, 200, 120, 55]

produto_usuário = input('Digite aqui o nome do produto que você deseja:').lower()

if produto_usuário in produtos:

     i = produtos.index (produto_usuário) 
     qtedeEstoque= estoque [i]

     print ('No estoque eu tenho {} unidades do produto {}'.format(qtedeEstoque, produtos[i]))

else:
    print('Esse produto não está na nossa lista.')

    
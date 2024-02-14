from POO_Mercado import *

# Criar instâncias
mercado_instancia = Mercado()
fornecedor1 = Fornecedor('Mercadao', 145879654, 'lfjururfkf')
cliente1 = Cliente('Fulano', 12345678, 'Rua Brasil')
produto1 = Produto('Alimentos', 'Arroz', 10, fornecedor1)

# Adicionar produto ao estoque
mercado_instancia.cadastrar_produto(produto1, 20)
print(f'Estoque em {datetime.now().strftime("%d/%m/%Y")}\n{produto1.nome_produto}: {mercado_instancia.estoque[produto1.nome_produto]} unidades\n')

# Realizar venda para um cliente
produto1.processar_venda(5, mercado_instancia)
print(f'Estoque atual de {produto1.nome_produto}: {mercado_instancia.estoque[produto1.nome_produto]} unidades\n')

# Realizar compra de um fornecedor
produto1.processar_compra(10, mercado_instancia)
print(f'Estoque atual de {produto1.nome_produto}: {mercado_instancia.estoque[produto1.nome_produto]} unidades\n')

# Projeto 02 - Banco de Dados para o Gerenciamento de um Mercado  - Squad Rita Levi Montalcini




1. CRIAÇÃO DAS TABELAS:

    - Tabela Categoria: Cria uma tabela para armazenar as categorias dos produtos.
    - Tabela Produto: Cria uma tabela para armazenar os produtos, incluindo nome, quantidade, preço e uma chave estrangeira para a categoria.
    - Tabela Cliente: Cria uma tabela para armazenar informações dos clientes, como nome e e-mail.
    - Tabela Venda: Cria uma tabela para armazenar informações sobre as vendas, incluindo a data da venda e uma chave estrangeira para o cliente.
    - Tabela Detalhes da Venda: Cria uma tabela para armazenar os detalhes de cada venda, incluindo a quantidade e o preço de cada produto vendido, juntamente com chaves estrangeiras para a venda e o produto.
    - Tabela Fornecedor: Cria uma tabela para armazenar informações dos fornecedores, como nome, contato e telefone.
    - Tabela Produto Fornecedor: Cria uma tabela para relacionar produtos a fornecedores.

2. INSERIR DADOS:

    - Inserção de dados na tabela Categoria: Insere dados de exemplo na tabela de categorias.
    - Inserção de dados na tabela Fornecedor: Insere dados de exemplo na tabela de fornecedores.
    - Inserção de dados na tabela Cliente: Insere dados de exemplo na tabela de clientes.
    - Inserção de dados na tabela Produto: Insere dados de exemplo na tabela de produtos.
    - Inserção de dados na tabela Produto Fornecedor: Relaciona produtos a fornecedores.
    - Inclusão de dados na tabela Venda: Insere dados de exemplo na tabela de vendas.
    - Inclusão de dados na tabela DetalhesVenda: Insere os detalhes das vendas, como a quantidade e o preço de cada produto vendido.

3. CONSULTAS:

    - Listar todos os produtos em estoque: Retorna todos os registros da tabela de produtos.
    - Encontrar as vendas realizadas por um cliente específico: Retorna informações sobre as vendas realizadas por um cliente específico, incluindo o nome do cliente, a data da venda, o nome do produto vendido, a quantidade vendida e o preço.
    - Identificar os produtos mais vendidos: Retorna as categorias de produtos e a quantidade total vendida de cada categoria, ordenadas em ordem decrescente pela quantidade total.
    - Calcular o total de vendas por categoria de produto: Retorna as categorias de produtos e o valor total das vendas de cada categoria, ordenadas em ordem decrescente pelo valor total das vendas.

4. ATUALIZAÇÕES E EXCLUSÕES:

    - Atualizar a quantidade em estoque após uma venda: 
    Diminue a quantidade em estoque de um produto após uma venda.
    - Remover um cliente: 
    Remove um cliente específico do banco de dados.

##### Este script SQL foi desenvolvido para criar um Banco de Dados para o Gerenciamento de um Mercado, inserir dados de exemplo e realizar consultas básicas sobre vendas e estoque. As consultas fornecem informações úteis para análise de vendas e gerenciamento de estoque.

-    [Script SQL](BD_Mercado.txt)

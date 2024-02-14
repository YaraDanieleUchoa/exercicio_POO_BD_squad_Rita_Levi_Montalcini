# Projeto 02 - Sistema Orientado a Objeto (POO) para o Gerenciamento de um Mercado  - Squad Rita Levi Montalcini


#### Este código implementa um sistema de mercado orientado a objetos em Python. Ele permite a interação entre clientes, fornecedores e produtos, gerenciando transações de compra e venda, controlando o estoque e registrando todas as atividades no mercado.

1. CLASSES DO SISTEMA

O código consiste em seis classes principais

    Classe Participante: 
Representa um participante do mercado, como cliente ou fornecedor.

-   Atributos:

nome: Nome do participante (string).   
telefone: Número de telefone do participante (string).   
endereco: Endereço do participante (string).  

    Classe Fornecedor (Herda de Participante):    
Representa um fornecedor que fornece produtos para o mercado.

-   Métodos:   

fornecimento(produto, qtde_fornecida, mercado): Realiza o fornecimento de um produto para o mercado.

    Classe Cliente (Herda de Participante):   
Representa um cliente que compra produtos no mercado.

-   Métodos:   

realizar_compra(mercado, produto, qtde): Realiza a compra de um produto no mercado.

    Classe Produto
Representa um produto disponível para compra no mercado.

-   Atributos:   

categoria: Categoria do produto (string).   
nome_produto: Nome do produto (string).   
qtde_estoque: Quantidade disponível em estoque do produto (int).   
fornecedor: Fornecedor do produto (objeto da classe Fornecedor).   
-   Métodos:   

comprar(qtde_comprada): Adiciona uma quantidade específica do produto ao estoque.     
processar_venda(qtde_venda, mercado): Processa uma venda do produto no mercado.      
processar_compra(qtde, mercado): Processa uma compra do produto no mercado.        

    Classe Transacao
Representa uma transação de compra ou venda de produtos no mercado.

-   Atributos:

data: Data/hora da transação.    
tipo: Tipo da transação ('cliente' ou 'fornecedor').    
participante: Participante envolvido na transação (cliente ou fornecedor).    
produtos: Lista de objetos da classe Produto envolvidos na transação.     
quantidades: Lista de quantidades correspondentes aos produtos da transação.     

    Classe Mercado
Representa o mercado onde ocorrem as transações de compra e venda.

-   Atributos:

transacoes: Lista de objetos da classe Transacao, registrando todas as transações no mercado.    
estoque: Dicionário contendo o nome do produto como chave e a quantidade em estoque como valor.     

-   Métodos:

registrar_transacao(transacao): Registra uma nova transação no mercado.     
cadastrar_produto(produto, quantidade): Adiciona um produto ao estoque do mercado.      

2. FUNCIONALIDADES DO SISTEMA

O sistema permite as seguintes funcionalidades

-   Cadastro de clientes e fornecedores.
-   Registro de produtos com suas respectivas categorias e fornecedores.
-   Realização de transações de compra por clientes e fornecimento por fornecedores.
-   Controle de estoque e atualização automática após transações.
-   Registro detalhado de todas as transações realizadas.

3. EXEMPLO DE USO

Um exemplo de uso do sistema é apresentado no final do código, demonstrando como criar instâncias, adicionar produtos ao estoque, realizar vendas para clientes e comprar produtos de fornecedores.


##### Este código fornece uma estrutura robusta para implementar um sistema de mercado eficiente em Python, com recursos completos de gerenciamento de clientes, fornecedores, produtos e transações. Ele pode ser estendido e personalizado conforme necessário para atender a requisitos específicos do projeto.






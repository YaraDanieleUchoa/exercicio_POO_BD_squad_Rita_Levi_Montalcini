# MODELAGEM DO SISTEMA PARA GERENCIAMENTO DE MERCADO

## Identificação das pincipais entidades:

- Pessoa: como classe abstrata 
- Cliente 
- Fornecedor
- Produto
- Transação

## Identificação das Propriedades de Cada Classe:

- Pessoa: nome, telefone
- Cliente: nome, telefone, endereço
- Fornecedor: nome, telefone
- Produto: nome, categorias, estoque, preço, fornecedores
- Transação: cliente, produtos, data

## Estabelecimento das Relações:

- Produto pode ter um ou mais fornecedores, então, há uma relação de composição/agregação entre Produto e Fornecedor.
- Mercado mantém um registro de transações, então, há uma relação de composição/agregação entre Mercado e Transação.

### Herança:

- Criação de uma classe abstrata chamada Pessoa que contém propriedades como nome e telefone. As classes Cliente e Fornecedor podem herdar dessa classe.

### Encapsulamento:

- Utilização de encapsulamento (propriedades privadas, getters e setters) para proteger o acesso direto a certas propriedades.

### Classe Abstrata:

- Criação de uma classe abstrata chamada Transacao que contém métodos para registrar uma transação e detalhes associados.

### Lógica de Compra:

- Considere como será feita a lógica de compra e como a quantidade disponível em estoque será atualizada.
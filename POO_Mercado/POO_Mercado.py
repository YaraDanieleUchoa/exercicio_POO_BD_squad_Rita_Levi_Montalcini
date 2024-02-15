from datetime import datetime

class Participante:
    def __init__(self, nome, telefone, endereco):
        self._nome = nome
        self._telefone = telefone
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone
        
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco

class Fornecedor(Participante):
    def fornecimento(self, produto, qtde_fornecida, mercado):
        transacao = Transacao('fornecedor', self, [produto], [qtde_fornecida])
        mercado.registrar_transacao(transacao)

class Cliente(Participante):
    def realizar_compra(self, mercado, produto, qtde):
        transacao = Transacao('cliente', self, [produto], [qtde])
        mercado.registrar_transacao(transacao)

class Produto:
    def __init__(self, categoria, nome_produto, qtde_estoque, fornecedor):
        self._categoria = categoria
        self._nome_produto = nome_produto
        self._qtde_estoque = qtde_estoque
        self._fornecedor = fornecedor

    @property
    def categoria(self):
        return self._categoria

    @property
    def nome_produto(self):
        return self._nome_produto

    @property
    def qtde_estoque(self):
        return self._qtde_estoque

    @property
    def fornecedor(self):
        return self._fornecedor

    @qtde_estoque.setter
    def qtde_estoque(self, nova_quantidade):
        if nova_quantidade >= 0:
            self._qtde_estoque = nova_quantidade
        else:
            print("Quantidade de estoque deve ser não negativa.")

    def comprar(self, qtde_comprada):
        if qtde_comprada > 0:
            self.qtde_estoque += qtde_comprada
            return True
        else:
            print(f'A quantidade comprada deve ser maior que zero.')
            return False

    def processar_venda(self, qtde_venda, mercado):
        if self.comprar(qtde_venda):
            transacao = Transacao('cliente', None, [self], [qtde_venda])
            mercado.registrar_transacao(transacao)
            self.qtde_estoque -= qtde_venda
            print(f'Produto {self.nome_produto} {qtde_venda} unids vendido para o cliente.')

    def processar_compra(self, qtde, mercado):
        self.qtde_estoque += qtde
        transacao = Transacao('fornecedor', self.fornecedor, [self], [qtde])
        mercado.registrar_transacao(transacao)
        print(f'Compra de {qtde} unidades de {self.nome_produto} realizada com sucesso.')

class Transacao:
    def __init__(self, tipo, participante, produtos, quantidades):
        self.data = datetime.now()
        self.tipo = tipo
        self.participante = participante
        self.produtos = produtos
        self.quantidades = quantidades

class Mercado:
    def __init__(self):
        self.transacoes = []
        self.estoque = {}

    def registrar_transacao(self, transacao):
        self.transacoes.append(transacao)
        for produto, qtde in zip(transacao.produtos, transacao.quantidades):
            if transacao.tipo == 'cliente':
                self.estoque[produto.nome_produto] -= qtde
            elif transacao.tipo == 'fornecedor':
                self.estoque[produto.nome_produto] += qtde

    def cadastrar_produto(self, produto, quantidade):
        self.estoque[produto.nome_produto] = quantidade

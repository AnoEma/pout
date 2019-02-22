class Pessoa:
    classe = 'manífero'


    def __init__(self, nome, cor_olhos, cor_cabelo, cor_pele, altura):

        self.nome = nome
        self.cor_olhos = cor_olhos
        self.cor_cabelo = cor_cabelo
        self.cor_pele = cor_pele
        self.altura = altura

    def cadastrar(self):
         print(f'{self.nome} foi cadastrado (a) no sistema.') 
    def excluir(self):
        print(f'{self.nome} foi excluido (a) do sistema.')
    def atualizar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f'O nome foi atualizado. Agora é : {self.nome}')

class Crianca(Pessoa):
    def __init__(self, desenho_favorito, brinquedo_favorito, nome, cor_olhos):
        self.desenho_favorito = desenho_favorito   
        self.brinquedo_favorito = brinquedo_favorito
    Pessoa.__init__( nome, cor_cabelo)

henrique = Crianca('Boleto', 'azul', 'roxo', 'vermelho', '0.50')
print(henrique.nome, henrique.altura)

fulano = Pessoa('João', 'castanhos', 'azul', 'amarelo', '1.97')
cicrano = Pessoa('Camilo', 'preto', 'roxo', 'verde', '1.50')











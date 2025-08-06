# class é o método para estruturar e criar objetos.
class cadastro:
    def __init__(self,nome,preco,estoque,data_validade,venda):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.validade = data_validade
        self.venda = venda
        
    # função para mostra todos os itens da classe cadastro.
    def mostrar_infor(self):
        print('-='*20)
        print(f'produto: {self.nome}')
        print(f'preço: {self.preco}')
        print(f'quantidade: {self.estoque}')
        
    # função de calcular o valor dos produtos no estoque.
    def valor_total_estoque(self):
        valor_Total = (self.preco * self.estoque)
        print(f'o valor total de todo o estoque é :{valor_Total}')
        
    # função de mostrar o vencimento do produto.
    def mostrar_validade(self):
        print(f'o produto vence {self.validade}')
        
    # função de mostrar o quanto vendeu.
    def vendas(self):
        print(f'foi vendido {self.venda}')
        
    # função de mostrar se bateu a meta ou não.
    def metas_vendas(self):
        if (self.venda > 100):
            print(f'bateu a meta!')
        else:
            print('não bateu a meta!')
            
    # função de mostrar a rentabilidade.
    def rentabilidade(self):
        rentabilidades = self.preco * self.estoque
        print(f' rendeu {rentabilidades} reais ')
        
    # função de criar um registro e salvar em formato de arquivo.txt
    def registro_produto(self):
            with open('cadastro_produto.txt',"a+",encoding="utf-8") as dados_produto:
                dados_produto.write(f'produto: {self.nome}\n')
                dados_produto.write(f'preço: {self.preco}\n')
                dados_produto.write(f'estoque: {self.estoque}\n')
                dados_produto.write(f'validade: {self.validade}\n')
                dados_produto.write(f'vendido: {self.venda}\n')
                dados_produto.write(f'rentabilidade:{self.preco * self.estoque}\n')  
                dados_produto.write("-=" *20 + "\n")
                      
# criar uma variavel para definir o método e as informações onde eles vão ser mostrado.
produto1 = cadastro("garrafa de agua",3,50,"25/12/2000",50) 
produto1.mostrar_infor()        # mostre apenas informação.
produto1.valor_total_estoque()  # apenas o valor do estoque.
produto1.mostrar_validade()     # mostre o vencimento.
produto1.vendas()               # apenas as vendas. 
produto1.metas_vendas()         # apenas as metas de vendas.
produto1.rentabilidade()        # apenas a rentabilidade.
produto1.registro_produto()     # quando chama, ele cria o arquivo e mostra dentro todos os produtos de cada um e a descrição.

produto2 = cadastro("Sabao em Pedra",10,200,'15/06/2007',140)
produto2.mostrar_infor()
produto2.valor_total_estoque() 
produto2.mostrar_validade()
produto2.vendas()
produto2.metas_vendas()
produto2.rentabilidade()
produto2.registro_produto()

produto3 = cadastro("Refrigerante",6,100,'21/10/2010',60)
produto3.mostrar_infor()
produto3.valor_total_estoque() 
produto3.mostrar_validade()
produto3.vendas()
produto3.metas_vendas()
produto3.rentabilidade()
produto3.registro_produto()

produto4 = cadastro("Shampoo", 18, 500, "14/07/2023", 100)
produto4.mostrar_infor()
produto4.valor_total_estoque()
produto4.mostrar_validade()
produto4.vendas()
produto4.metas_vendas()
produto4.rentabilidade()
produto4.registro_produto()

produto5 = cadastro("Caixa de Sabonete",15,300,"30/11/2002",500)
produto5.mostrar_infor()
produto5.valor_total_estoque()
produto5.mostrar_validade()
produto5.vendas()
produto5.metas_vendas()
produto5.rentabilidade()
produto5.registro_produto()
# ESTRUTURA DE DADOS COM PRODUTOS UTILIZANDO A LINGUAGEM PYTHON.<br>:snake:

## Descrição:<br>

### Estrutura de dados ele é baseado em POO (Programação Orientado a Objeto) onde é um paradigma que ajuda a organizar e estruturar melhor o código. No Python, o POO é uma abordagem fundamental para criar códigos modulares, reutilizáveis e mais fáceis de manter.<br>:game_die:

# O que são Classes e Objetos?<br><br>

## Uma classe é um modelo que define a estrutura de um objeto. Ela contém:<br><br>

+ **Atributos**: Variáveis que armazenam características do objeto.<br>
+ **Métodos**: Funções que definem o comportamento do objeto.<br><br>

### Já o objeto é uma instância dessa classe. Cada objeto criado a partir de uma classe herda os atributos e métodos definidos por ela, mas pode ter valores e estados específicos.<br>

### Em resumo, as classes no Python representam um conjunto de objetos com características e ações semelhantes. Para entender melhor o conceito de classes e objetos, vamos usar um exemplo com cadastro de produtos.<br><br>

## Como Funciona:💻:computer:<br>

### A **classe cadastro** vai ser o inicializador.<br>

### 📝:pencil: **Mostrar_Infor**: O objeto vai salvar toda a informação adicionado<br>

### :package: A função **valor_total_estoque** mostra todos os itens da classe cadastro.<br>

### 📆:calendar: A função **mostrar_validade** mostrar quando o produto vai vencer.<br>

### A função **vendas** mostrar o quanto vendeu.<br>

### 📈:chart_with_upwards_trend: A função **metas_vendas** define a condição de se bateu a meta ou não.<br>

### :money_with_wings: A função **rentabilidade** mostrar o quando de valor daria sobre o preço e a quantidade de estoque.<br>

### 📁:file_folder: A função **registro_produto** criar um registro e salvar em formato de arquivo onde será armazenado  todos os itens na classe cadasttro.

## Funcionalidade:<br> 

### O usuário informar todas as informações do produto para inseri-ló como nome, preço, quantidade, validade, e metas que deseja inserir sobre o item do produto.<br>
´´´
produto1 = cadastro("Nome do Produto",preço,estoque,"Data-de-validade",Rentabilidade) 
produto1.mostrar_infor()        # mostre apenas informação.
produto1.valor_total_estoque()  # apenas o valor do estoque.
produto1.mostrar_validade()     # mostre o vencimento.
produto1.vendas()               # apenas as vendas. 
produto1.metas_vendas()         # apenas as metas de vendas.
produto1.rentabilidade()        # apenas a rentabilidade.
produto1.registro_produto()     # quando chama, ele cria o arquivo e mostra dentro todos os produtos de cada um e a descrição.
´´´ <br><br>

## OBSERVAÇÃO:<br>
### Esse código server como base ao entendimento sobre estrutura de dados, mas não se baseando totalmente na Programação Orientado a Objeto, já que requer um nivel atenção profunda do conteúdo e mais tempo para o aprendizado para o desenrolar de códigos mais complexos.
# product_recommender
Sistema de recomendação e categorização de produtos.

## Sobre
Nesse projeto temos uma sistema de recomendação e classificação de produtos. Esse sistema será treinado
com base em dados de produtos comercializados em um marketplace digital. Ao todo, temos 38.507 registros
distribuídos em 5 categorias (**Bebê**, **Bijuteriais e Jóias**, **Decoração**, **Lembrancinhas**,
**Papel e Cia** e **Outros**). Cada registro corresponde a um clique em um produto a partir de um termo
de busca no site. No dataset é composto das seguintes variáveis:
- `product_id` - identificação de produto
- `seller_id` - identificação do vendedor
- `query` - termo de busca inserido pelo usuário
- `search_page` - número da página que o produto apareceu nos resultados de busca (mín 1 e máx 5)
- `position` - número da posição que o produto apareceu dentro da página de busca (mín 0 e máx 38)
- `title` - título do produto
- `concatenated_tags` - tags do produto inseridas pelo vendedor (as tags estão concatenadas por espaço)
- `creation_date` - data de criação do produto na plataforma do Elo7
- `price` - preço do produto em reais
- `weight` - peso em gramas da unidade do produto reportado pelo vendedor
- `express_delivery` - indica se o produto é pronta entrega (1) ou não (0)
- `minimum_quantity` - quantidade de unidades mínima necessária para compra
- `view_counts` - número de cliques no produto nos últimos três meses
- `order_counts` - número de vezes que o produto foi comprado nos últimos três meses
- `category` - categoria do produto

### Sistema de Classificação

O modelo de classificação é realizado por um modelo de `RandomForestClassifer`
do `scikit-learn`. Ele é utilizado através do script `main.py`. Para utilizar
o classificador devemos utilizar o parâmetro `-c` ou `--category` junto com
um string como se fosse um dicionário, com as chaves **title**, **concatenated_tags**,
**price**, **weight** e **minimum_quantity**. Essas são as variáveis dos dados
originais que foram utilizadas para treinar o modelo. Exemplificando a
utilização o modelo:

```python main.py --category "{'title': 'Saída de maternidade masculino', 'concatenated_tags': 'bebe menino maternidade roupa', 'price': 70, 'weight': 30, 'minimum_quantity': 1}"```

### Sistema de Recomendação

O sistema de recomendação gera 10 produtos a partir de uma query. Os produtos
selecionados são aquele cujo os títulos são os de menor distância de edição em
relação à query. De uma certa forma pode ser considerado como um sistema de
recomendação baseado no conteúdo dos itens.

Além de selecionar os produtos mais parecidos com a query, essa funcionalidade
aplica o modelo de classificação de categorias aos registros selecionados pela
query e identifica a categoria majoritária. Como resultado são printados, a
categoria majoritária e série de ids e títulos recomendados. A utilização pode
ser feita com o seguinte comando:

````main.py --recommendation "<produto>"``
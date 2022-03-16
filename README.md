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


### Sistema de Recomendação

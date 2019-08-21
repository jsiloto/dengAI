# Predição de Número de Casos de Dengue

Para o projeto da disciplina de "Dados, Inferência e Aprendizagem" 
ministrada no 2o Semestre de 2019 pelos professores 
José Cândido Silveira Santos Filho e Flavio du Pin Calmon, 
escolhemos um desafio público de predição do número de casos de dengue
baseado na série histórica das cidades de San Juan, Porto Rico e Iquitos, Peru.
O desafio é oferecido pela plataforma [DrivenData](https://arxiv.org/abs/1606.07781)
e a descrição completa do desafio está disponivel no 
seu [site oficial](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/)

Consideramos que apesar de se tratar de uma competição, em que não temos
acesso aos dados de saída de teste e que estamos sujeitos aos 
[regulamentos da competição](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/rules/),
a escolha deste desafio está de acordo
com a filosofia da disciplina, pois provê aos alunos 
uma ótima oportunidade de aplicar ferramentas de inferência
em um problema real e de relação direta às suas vidas cotidianas,
visto que de janeiro a junho de 2019 já foram confirmados
[mais de 18,000 casos de dengue na cidade de Campinas](https://g1.globo.com/sp/campinas-regiao/noticia/2019/06/03/campinas-confirma-4a-morte-por-dengue-e-numero-de-infectados-pelo-virus-aumenta-12percent.ghtml)


## Dados 
Os dados são representados por uma série temporal com resolução semanal
e 21 atributos contendo localização, dados meteorológicos
e de vegetação, agregando 4 fontes distintas.

San Juan, Puerto Rico      |  Iquitos, Peru
:-------------------------:|:-------------------------:
![](san_juan.png)          |  ![](iquitos.png)


## Modelo
O problema proposto utiliza a métrica de erro absoluto médio (norma $l_1$)

Tradicionalmente a análise de séries temporais utiliza modelos 
auto-regressivos da família [ARMA (Autoregressive–moving-average)](https://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model),
a partir de uma [pesquisa preliminar](#revisão-literária) de estudos
preditivos em séries temporais de dengue e malária, temos que os modelos mais comuns são
os modelos (S)ARIMA com método de otimização [Box-Jenkins](https://en.wikipedia.org/wiki/Box%E2%80%93Jenkins_method).
Porém, estes modelos dependem de suposições fortes de estacionariedade 
dos dados e requerem estratégias manuais de agregação dos atributos,
o que cresce combinatorialmente em complexidade com o número de atributos
(21 no nosso caso).

Também é do interesse do grupo a exploração de modelos baseados em redes neurais,
trabalhos mais recentes apontam o uso mas sem consenso sobre arquitetura e em geral
sem dados de hiperparametros para garantir reproducibilidade, portanto mais análise é necessária

# Revisão Literária
| Doença       | Outros Atributos                                                          | Modelo                                         | Algoritimo                               | Obs                                                                                                  |
|--------------|---------------------------------------------------------------------------|------------------------------------------------|------------------------------------------|------------------------------------------------------------------------------------------------------|
| Dengue, Zica | Não                                                                       | Vários                                         | Vários                                   | Tese de Mestrado com nosso dataset                                                                   |
| Dengue       | Não                                                                       | ARIMA                                          | Box Jenkins                              |                                                                                                      |
| Influenza    | Não                                                                       | ARMA-like, Processos Gaussianos, Deep Learning | Não Especificado                         |                                                                                                      |
| Dengue       | Temperatura, Precipitação, Humidade Relativa, Pesquisas no Baidu          | Vários                                         | Vários                                   | Support Vector Regression teve os melhores resultados                                                |
| Malaria      | Temperatura, Precipitação, Humidade Relativa, Indice de Vegetação         | ARIMA                                          | Box Jenkins                              | Trabalha com escala logaritimica dos dados.                                                          |
| Malaria      | Temperatura do chão, Precipitação, Indice de Vegetação, EvapoTranspiração | SARIMA                                         | Não Especificado                         | Trabalha com escala logaritimica dos dados.                                                          |
| Dengue       | Temperatura Max/Min/Avg, Precipitação, Humidade Relativa                  | SARIMA                                         | Box Jenkins                              | Variavel com lag de 3 meses e Temperatura são os atributos mais preditivo.                           |
| Malaria      | Temperatura Max/Min/Avg, Precipitação, Humidade Relativa                  | ARIMAX                                         | Não Especificado                         | Variáveis não eram transferiveis para diferentes localizações                                        |
| Dengue       | Temperatura Max/Min, Precipitação, humidade relativa, vento               | Regressão de Poisson Multivariada              | GEE/QICu                                 | Temperatura minima/ Humidade são positivamente correlacionadas, vento é negativamente correlacionado |
| Dengue       | Não                                                                       | SARIMA                                         | Normalized Bayesian Information Criteria |                                                                                                      |
| Dengue       | Temperatura Max/Min, Precipitação diaria e anual                          | ARIMA                                          | Box Jenkins                              | Trabalha com escala logaritimica dos dados                                                           |
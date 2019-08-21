# Predição de Número de Casos de Dengue

Para o projeto da disciplina de "Dados, Inferência e Aprendizagem" 
ministrada no 2o Semestre de 2019 pelos professores 
José Cândido Silveira Santos Filho e Flavio du Pin Calmon, 
escolhemos um desafio público de predição do número de casos de dengue
baseado na série histórica das cidades de San Juan, Porto Rico e Iquitos, Peru.
O desafio é oferecido pela plataforma DrivenData <sup>[1](#drivendata)</sup> 
e a descrição completa do desafio está disponivel no 
seu [site oficial](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/)

Consideramos que apesar de se tratar de uma competição, em que não temos
acesso aos dados de saída de teste e que estamos sujeitos aos 
[regulamentos da competição](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/rules/),
a escolha deste desafio está de acordo
com a filosofia da disciplina, pois provê aos alunos 
uma ótima oportunidade de aplicar ferramentas de inferência
em um problema real e de relação direta às suas vidas cotidianas,
visto que de janeiro a junho de 2019 já foram confirmados mais de 18,000 casos
de dengue na cidade de Campinas<sup>[2](#denguecampinas)</sup>


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
auto-regressivos da família ARMA (Autoregressive–moving-average)<sup>[3](#modelosautoregressivos)</sup>,
a partir de uma [pesquisa preliminar](#revisão-literária) de estudos
preditivos em séries temporais de dengue e malária, temos que os modelos mais comuns são
os modelos (S)ARIMA com método de otimização Box-Jenkins<sup>[4](#boxjenkins)</sup>.
Porém, estes modelos dependem de suposições fortes de estacionariedade 
dos dados e os exemplos encontrados lidam com um espaço
de atributos muito menor (até 4) do que o nosso (21 atributos).

Também é do interesse do grupo a exploração de modelos baseados em redes neurais,
mas devido ao grande número de opções ainda não temos candidatos específicos.


# Revisão Literária

|  Doença |    Anos   | Resolução Temporal |                              Outros Atributos                             |             Cidades            | Modelo                            | Algoritimo                               | Obs                                                                                                  | Trabalho                                                                            | Ano (Citações) |
|:-------:|:---------:|:------------------:|:-------------------------------------------------------------------------:|:------------------------------:|-----------------------------------|------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------|
|  Dengue | 2001-2014 | Mensal             |                                    Não                                    |     Recife/Goiania, Brasil     | ARIMA                             | Box Jenkins                              |                                                                                                      | [link](https://www.arca.fiocruz.br/bitstream/icict/26315/2/oswaldoG_cruz_etal_IOC_2018.pdf) | 2018 (9)       |
|  Dengue | 2001-2006 | Mensal             |        Temperatura Max/Min, Precipitação, humidade relativa, vento        |        Guangzhou, China        | Regressão de Poisson Multivariada | GEE/QICu                                 | Temperatura minima/ Humidade são positivamente correlacionadas, vento é negativamente correlacionado | [link](https://bmcpublichealth.biomedcentral.com/articles/10.1186/1471-2458-9-395)          | 2009 (181)     |
|  Dengue | 2000-2006 | Semanal            |         Temperatura Max/Min/Avg, Precipitação, Humidade Relativa          | Guadeloupe, French West Indies | SARIMA                            | Box Jenkins                              | Variavel com lag de 3 meses e Temperatura são os atributos mais preditivo.                           | [link](https://bmcinfectdis.biomedcentral.com/articles/10.1186/1471-2334-11-166)            | 2011 (170)     |
| Dengue  | 1997-2004 | Mensal             | Temperatura Max/Min, Precipitação diaria e anual                          | Rio de Janeiro, Brasil         | ARIMA                             | Box Jenkins                              | Trabalha com escala logaritimica dos dados                                                           | [link](https://www.ajtmh.org/content/journals/10.4269/ajtmh.2008.79.933)                    | 2008 (160)     |
| Dengue  | 2000-2007 | Mensal             | Não                                                                       | Dhaka, Bangladesh              | SARIMA                            | Normalized Bayesian Information Criteria |                                                                                                      | [link](https://apps.who.int/iris/handle/10665/170465)                                       | 2008 (45)      |
| Malaria | 2001-2008 | Mensal             | Temperatura do chão, Precipitação, Indice de Vegetação, EvapoTranspiração | Ethiopia (Várias localidades)  | SARIMA                            | Não Especificado                         | Trabalha com escala logaritimica dos dados.                                                          | [link](https://malariajournal.biomedcentral.com/articles/10.1186/1475-2875-9-251)           | 2012 (85)      |
| Malaria | 2005-2015 | Mensal             | Temperatura, Precipitação, Humidade Relativa, Indice de Vegetação         | Afeganistão                    | ARIMA                             | Box Jenkins                              | Trabalha com escala logaritimica dos dados.                                                          | [link](https://malariajournal.biomedcentral.com/articles/10.1186/s12936-016-1602-1)         | 2016 (16)      |
| Malaria | 1994-2006 | Mensal             | Temperatura Max/Min/Avg, Precipitação, Humidade Relativa                  | Butão                          | ARIMAX                            | Não Especificado                         | Variáveis não eram transferiveis para diferentes localizações                                        | [link](https://malariajournal.biomedcentral.com/articles/10.1186/1475-2875-9-251)           | 2010 (106)     |


# Referências

<a name="drivendata">1</a>: Bull, Peter, Isaac Slavitt, and Greg Lipstein.
"Harnessing the power of the crowd to increase capacity for data science in the social sector."
 arXiv preprint arXiv:1606.07781 (2016).

<a name="denguecampinas">2</a>: https://g1.globo.com/sp/campinas-regiao/noticia/2019/06/03/campinas-confirma-4a-morte-por-dengue-e-numero-de-infectados-pelo-virus-aumenta-12percent.ghtml

<a name="modelosautoregressivos">3</a>:https://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model

<a name="boxjenkins">4</a>:https://en.wikipedia.org/wiki/Box%E2%80%93Jenkins_method

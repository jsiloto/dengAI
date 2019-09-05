# Data Analysis README

Este relatório reporta os principais resultados e conclusões da nossa exploração
dos dados.

Em primeiro lugar explicamos qual a origem dos dados e seu signifcado. Aqui, para
uma melhor compreensão, descrevemos brevemente as cidades dos quais os dados foram
extraídos, isto é, Iquitos no Peru e San Juan em Porto Rico.

Após fazemos análise do comportamento da série temporal. Nesse aspecto damos destaque
a diferença entre as duas cidades e explicitamos a sazionalidade existente em ambas as
séries.

Por fim, fazemos diversas análise de correlação desde a autocorrelação da própria série
temporal à correlação entre todas as features e entre essas e a série temporal. Com isso,
conseguimos detectar a forte presença de correlação entre as features, determinar quais
features são mais representativas ao problema.

## Breve introdução, terminologias e conceitos

Uma série temporal pode ser entendida como uma sequência de observações de uma variável
feitas ao longo do tempo. Em nosso caso, a variável observada é o número de casos de
dengue ocorridos em frequência de observações semanais nas cidades de Iquitos no Peru e
San Juan em Porto Rico, conforme ilustrado na Figura 1.

**Por imagem aqui**

As séries temporais são composta por combinações de quatro padrões: tendência, ciclos, sazonalidade e irreguaridades. Os modelos clássicos de estimadores para séries temporais buscam, em geral, detectar a existência destes padrões.

A tendência refere-se ao comportamento a longo prazo da série, por exemplo um indicativo de que o número de casos de dengue tende a diminuir com o passar dos anos. Assim um série pode possuir tendência
crescente, descrescente ou mesmo não possuir tendência. Nesse último caso defini-se as chamdas séries estacionárias em que, de forma simplificada, seu comportamento não se altera com o passar do tempo, ou seja, propriedades estatísticas de sequencias de observações em tempos distintos são semelhantes.

Ciclos e sazonalidade são comportamentos que se repetem com certa periodicidade. A diferença entre ciclo e sazonalidade está relacionada ao tempo de observação e sua previsibilidade. A sazonalidade são comportamentos períodicos observados dentro de um ano, por exemplo, o aumento dos casos de dengue durante o verão. Os ciclos, em contrapartida, não possuem sua peridiocidade tão bem definida e, em geral, possuem tempo de observação superior a um ano, um exemplo hipotético seria a ocorrência de grandes epidemias de dengue em intervalos de tempo aproximado de 3 a 4 anos.  

As variações irregulares são as alterações inexplicáveis ou não esperadas. Normalmente ocorrem devido a fatores externos, como catástrofes naturais e atentados terroristas.

## Data analysis

O conjunto de dados da competição é constituido por uma série temporal com resolução semanal dos casos reportados de dengue, aĺem de 20 atributos contendo localiza̧ção, dados meteorologicos e de vegetação, agregando 4 fontes distintas. Ele considera dados da cidade de San Juan por aproximadamente 19 anos (1990 a 2008) e da cidade de Iquitos por cerca de 11 anos (2000 a 2010).

As cidades de San Juan e Iquitos são bem distintas. A cidade de San Juan é a capital e o município mais populoso de Porto Rico, cerca de 347 mil habitantes (dados de 2016). É uma cidade litorânea localizada no Caribe sendo o centro industrial, financeiro, cultural e turístico da ilha de Porto Rico. Por sua vez, a cidade de Iquitos destaca-se por ser a cidade com maior número de habitantes no mundo que não pode ser alcançada por rotas terrestres. São cerca de 466 mil habitantes (dados de 2015) citados no meio da floresta Amazônica sendo conhecida como Capital da Amazônia Peruana. Devido a isso, possui o mais importante porto fluvial do Peru no qual se comunica com outras cidades situadas na floresta Amazônica como Letícia na Colombia e Manaus no Brasil.

Na Figura 2 observar-se o histograma do número de casos de dengue para esses duas cidades. Pode-se notar que o comportamento das séries temporais para cada cidade são bem distintos, tendo a cidade de San Juan um maior número de ocorrências. Ao todo foram observados 936 pontos na cidade de San Juan contra 520 de Iquitos.

**Por Imagem aqui**

Além do número de ocorrências da doença, a base de dados possui informações sobre outros 20 atributos associados a doença. Esses
atributos consideram principalmente as condições climáticas, como
temperatura, nível de precipitação e humid ade, e o indíce de diferença na vegetação. Esses dados foram obtidos através de 4 fontes, sendo elas: 

- a GHCN (Global Historical Climatology Network) da NOAA (National Oceanic and Atmospheric Administration) ue é uma base de dados estações metereológicas terrestres com medições diárias;
- dos dados da reanálise do sistema de previsão climática do NOAA NCEP (National Centers for Environmental Prediction) nos Estados Unidos que possui dados globais de tempo, água, clima, previsões entre outros;
- do programa NOAA CDR (Climate Data Record) que constitui-se de um conjunto de dados temporais obtidos por satellites e entre eles medições do Índice de Vegetação da Diferença Normalizada (NDVI) por região da cidade (nororoeste, nordeste, sudeste e sudoeste);
- do PERSIANN-CDR (Precipitation Estimation from Remotely Sensed Information using Artificial Neural Networks-CDR) que constitui-se de conjunto dados formados por de estimativas da quantidade de chuva diária;

Na Tabela 1 está descrito os 20 atributos presentes no banco de dados, sua unidade de medida e sua fonte de origem. Já na tabela 2 é informado a quantidade de dados faltantes e uma breve descrição estatística (média e desvio padrão) para a cidade de San Juan e na Tabela 3 para a cidade de Iquitos. Entende-se por dados faltantes quando o valor do atributo não foi medido ou informado para uma determinada observação da série temporal. Na Tabela 1 o indíce de vegetação NDVI é uma medida diferencial normalizada entre -1 e 1 no qual quanto mais próximo de 1 maior a quantidade de vegetação no local. A temperatura do ponto orvalho corresponde a temperatura em que o vapor de água presente no ar passa para o estado líquido.

**Tabela 1: Descrição dos atributos**
| Id              	| Descrição                                       	| Unidade de medida             	| Fonte         	|
|-----------------	|-------------------------------------------------	|-------------------------------	|---------------	|
| ndvi_ne         	| NDVI da região nordeste                         	| valor entre -1 e 1            	| NOAA CDR NDVI 	|
| ndvi_nw         	| NDVI da região noroeste                         	| valor entre -1 e 1            	| NOAA CDR NDVI 	|
| ndvi_se         	| NDVI da região sudeste                          	| valor entre -1 e 1            	| NOAA CDR NDVI 	|
| ndvi_sw         	| NDVI da região sudoeste                         	| valor entre -1 e 1            	| NOAA CDR NDVI 	|
| prec_amt        	| Índice de precipitação                          	| milímetros                    	| PERSIANN      	|
| reanal_air_temp 	| Temperatura média do ar                         	| Kelvin                        	| NOAA NCEP     	|
| reanal_avg_temp 	| Temperatura média do ar                         	| Kelvin                        	| NOAA NCEP     	|
| reanal_max_temp 	| Temperatura máxima do ar                        	| Kelvin                        	| NOAA NCEP     	|
| reanal_min_temp 	| Temperatura mínima do ar                        	| Kelvin                        	| NOAA NCEP     	|
| reanal_tdtr     	| Amplitude térmica diurna                        	| Kelvin                        	| NOAA NCEP     	|
| reanal_dew_temp 	| Temperatura do ponto de orvalho                 	| Kelvin                        	| NOAA NCEP     	|
| reanal_sat_prec 	| Índice de precipitação determinado por satélite 	| milímetros                    	| NOAA NCEP     	|
| reanal_prec     	| Índice de precipitação                          	| quilograma por metro quadrado 	| NOAA NCEP     	|
| reanal_rel_hum  	| Umidade relativa média                          	| porcentagem                   	| NOAA NCEP     	|
| reanal_spec_hum 	| Umidade especifíca média                        	| gramas por quilograma         	| NOAA NCEP     	|
| st_avg_temp     	| Temperatura média da estação                    	| Celsius                       	| NOAA GHCN     	|
| st_max_temp     	| Temperatura máxima                              	| Celsius                       	| NOAA GHCN     	|
| st_min_temp     	| Temperatura mínima                              	| Celsius                       	| NOAA GHCN     	|
| st_tdtr         	| Amplitude térmica diurna                        	| Celsius                       	| NOAA GHCN     	|
| st_prec         	| Índice de precipitação                          	| milímetros                    	| NOAA GHCN     	|



**Tabela 2: Descrição dos estatística dos atributos para a cidade de San Juan**
| Id              	| Número de dados faltantes 	| Média 	| Desvio Padrão 	| Mediana 	| Minímo 	| Máximo 	|
|-----------------	|---------------------------	|-------	|---------------	|---------	|--------	|--------	|
| ndvi_ne         	| 191                       	| 0,06  	| 0,11          	| 0,06    	| -0,41  	| 0,49   	|
| ndvi_nw         	| 49                        	| 0,07  	| 0,09          	| 0,07    	| -0,46  	| 0,44   	|
| ndvi_se         	| 19                        	| 0,18  	| 0,06          	| 0,18    	| -0,01  	| 0,39   	|
| ndvi_sw         	| 19                        	| 0,17  	| 0,06          	| 0,17    	| -0,06  	| 0,38   	|
| prec_amt        	| 9                         	| 35,5  	| 44,6          	| 20,8    	| 0      	| 391    	|
| reanal_air_temp 	| 6                         	| 299,2 	| 1,24          	| 299,2   	| 296    	| 302    	|
| reanal_avg_temp 	| 6                         	| 299,3 	| 1,22          	| 299,4   	| 296    	| 302    	|
| reanal_max_temp 	| 6                         	| 301,4 	| 1,26          	| 301,5   	| 297    	| 304    	|
| reanal_min_temp 	| 6                         	| 297,3 	| 1,29          	| 297,5   	| 293    	| 300    	|
| reanal_tdtr     	| 6                         	| 2,52  	| 0,5           	| 2,46    	| 1,36   	| 4,43   	|
| reanal_dew_temp 	| 6                         	| 295,1 	| 1,57          	| 295,46  	| 290    	| 298    	|
| reanal_sat_prec 	| 6                         	| 35,5  	| 44,6          	| 20,8    	| 0      	| 391    	|
| reanal_prec     	| 6                         	| 30,5  	| 35,6          	| 21,3    	| 0      	| 570    	|
| reanal_rel_hum  	| 6                         	| 78,6  	| 3,4           	| 78,7    	| 66,7   	| 87,6   	|
| reanal_spec_hum 	| 6                         	| 16,5  	| 1,6           	| 16,8    	| 11,7   	| 19,4   	|
| st_avg_temp     	| 6                         	| 27    	| 1,4           	| 27,2    	| 22,8   	| 30,1   	|
| st_max_temp     	| 6                         	| 31,6  	| 1,7           	| 31,7    	| 26,7   	| 35,6   	|
| st_min_temp     	| 6                         	| 22,6  	| 1,5           	| 22,8    	| 17,8   	| 25,6   	|
| st_tdtr         	| 6                         	| 6,76  	| 0,83          	| 6,76    	| 4,53   	| 9,91   	|
| st_prec         	| 6                         	| 26,8  	| 29,3          	| 17,75   	| 0      	| 306    	|



**Tabela 3: Descrição dos estatística dos atributos para a cidade de Iquitos**
| Id              	| Número de dados faltantes 	| Média 	| Desvio Padrão 	| Mediana 	| Minímo 	| Máximo 	|
|-----------------	|---------------------------	|-------	|---------------	|---------	|--------	|--------	|
| ndvi_ne         	| 3                       	| 0,26  	| 0,08          	| 0,26    	| 0,06  	| 0,51   	|
| ndvi_nw         	| 3                        	| 0,24  	| 0,08          	| 0,23    	| 0,04  	| 0,45   	|
| ndvi_se         	| 3                        	| 0,25  	| 0,08          	| 0,25    	| 0,03  	| 0,54   	|
| ndvi_sw         	| 3                        	| 0,27  	| 0,09          	| 0,26    	| 0,06  	| 0,55   	|
| prec_amt        	| 4                         	| 64,2  	| 35,2          	| 60,5    	| 0      	| 211    	|
| reanal_air_temp 	| 4                         	| 297,9 	| 1,17          	| 297,8   	| 294    	| 302    	|
| reanal_avg_temp 	| 4                         	| 299,1 	| 1,33          	| 299,1   	| 295    	| 303    	|
| reanal_max_temp 	| 4                         	| 307,1 	| 2,38          	| 307   	| 300    	| 314    	|
| reanal_min_temp 	| 4                         	| 292,9 	| 1,66          	| 293   	| 287    	| 296    	|
| reanal_tdtr     	| 4                         	| 9,21  	| 2,45           	| 8,96    	| 3,71   	| 16    	|
| reanal_dew_temp 	| 4                         	| 295,5 	| 1,42          	| 295,8  	| 290    	| 298    	|
| reanal_sat_prec 	| 4                         	| 64,2  	| 35,2          	| 60,5    	| 0      	| 211    	|
| reanal_prec     	| 4                         	| 57,6  	| 50,3          	| 46,4    	| 0      	| 362    	|
| reanal_rel_hum  	| 4                         	| 88,6  	| 7,58           	| 90,9    	| 57,8   	| 98,6   	|
| reanal_spec_hum 	| 4                         	| 17,1  	| 1,45           	| 17,4    	| 12,1   	| 20,5   	|
| st_avg_temp     	| 37                         	| 27,5    	| 0,92           	| 27,6    	| 21,4   	| 30,8   	|
| st_max_temp     	| 14                         	| 34    	| 1,32           	| 34    	| 30,1   	| 42,2   	|
| st_min_temp     	| 8                         	| 21,2  	| 1,26           	| 21,3    	| 14,7   	| 24,2   	|
| st_tdtr         	| 37                         	| 10,57  	| 1,54          	| 10,62    	| 5,2   	| 15,8   	|
| st_prec         	| 16                         	| 62,5  	| 63,25          	| 45,3   	| 0      	| 543    	|


### Análise de corelação

A análise dos dados têm por objetivo determinar se a série temporal é estacionária, perceber a ocorrência de sazonalidades, determinar a existência de atributos redundantes, isto é, muito correlacionados e  descobrir quais atributos são os mais preditivos em relação ao número de casos de dengue. Nesse estudo, os dados referentes a cada cidade foram separados e serão tratados como séries temporais distintas. Para realizar essa etapa utilizou-se principalmente do cálculo de correlação entre as variáveis.

Séries temporais estacionárias possuem um menor grau de complexidade para a criação de um estimador, uma vez que seus dados estatísticos se mantém semelhantes com o passar do tempo. Existem alguns testes que podem ser realizados para determinar se uma série é ou não estacionária, entre eles o teste de Dickey-Fuller. Nesse teste ambas séries discutidas foram consideradas estacionárias.

Ao observar a série temporal nas Figuras 1 e 2 percebe-se a existência de um possível ciclo períodico em torno de 3 a 4 anos para a cidade de San Juan e de 2 em 2 anos para a cidade de Iquitos. Uma explicação plausível para esse comportamento é a imunização da população após uma epidemia, levando a redução do número de casos nos anos seguintes. Além disso, os estudos em cima do ciclo de vida do mosquito transmissor da dengue revelam que durante as estações mais quentes os mosquitos se reproduzem mais elevando o número de casos. Em ambas as cidades esse período ocorre no segundo semestre e dura até Feveiro do ano seguinte. Na Figura 3-a a série temporal para cada uma das citadas está ilustrada na forma de um gráfico de barras por ano facilitando a visualização dos possíveis ciclos. Enquanto, que na Figura 3-b observa-se o somatório do número de casos de dengue por mês do ano para todos os anos presentes no banco de dados. Nota-se que em ambas as localidades o número de casos de dengue se eleva no segundo semestre e no primeiro bimestre de cada ano. Em San Juan essa sazonalidade é mais marcante, enquanto em Iquitos ocorre de forma mais timida.

**Por Figura aqui**

O cálculo da autocorrelação da variável a ser predita permitiu a confirmação da existência de uma sazonalidade anual nas duas série temporais observadas. Na Figura 4 podemos observar que em ambas as séries possuem picos de autocorrelação em intervalos de aproximadamente 50 meses ou seja um ano. Além disso, destacou a diferença de comportamento entre as duas séries uma vez que a cidade de San Juan apresentou uma autocorrelação mais comportada.

**Por Figura aqui**

A partir das explorações representadas pelo teste de Dickey-Fuller e pelas Figuras 3 e 4, concluiu-se que as séries temporais apresentadas são estacionárias e possuem sazonalidade anual, podendo ainda apresentar um possível ciclo a cada entre 2 e 4 anos. O último padrão presente em séries temporais ainda não explorado é a presença de irregularidades, entretanto esse tipo de comportamento não será tratado. Vale ressaltar que na cidade de San Juan pode ter ocorrido uma irregularidade no ano de 1994 devido a elevado número de casos de dengue em comparação com os demais anos do período observado.

A próxima etapa da análise dos dados consiste em observar a correlação entre os atributos. Essa medida serve para identificar dados estatisticamente semelhantes que podem ocasionar sobreajuste em nossos modelos. Assim os atributos mais correlacionados deverão ser agregados em um novo atributo de modo a reduzir a dimensionalidade dos dados. 

Na Figura 5 está apresentado o diagrama de correlação entre os atributos para cada uma das cidades. Neles podemos observar que os atributos relacionados a vegetação aparentemente possuem pouca relação com os demais atributos. Em contrapartida, os atributos relacionados a temperatura apresentam uma alta correlação.

**Por Figura aqui**

Interessante destacar a diferença entre os diagramas das duas cidades, mostrando que o problema da predição do número de casos de dengue será melhor abordado sobre o preceito de que os dados de cada cidade não devem ser misturados. Observa-se também que a correlação entre os dados de vegetação e os dados climáticos estão mais correlacionados na cidade de Iquitos. De fato, essa cidade se localiza no meio da floresta Amazônica e, portanto,
a floresta influência nas medidas climáticas do local.

Nessa Figura o número de casos de dengue (variável a ser predita) também foi considerado. Da análise do diagrama percebemos que nenhum dos atributos possuem elevada correlação com essa variável, ou seja, nenhum deles é excepcionalmente bom em predizer os dados. A correlação entre os atributos e a variável a ser predita permite determinar quais são os atributos mais relevantes para os modelos de predição. Na Figura 6 observa-se os valores de correlação entre os atributos e o número de ocorrência de casos de dengue.

**Por Figura aqui**

Da Figura 6 tem-se que os atributos mais preditivos foram: a umidade específica, a temperatura do ponto de orvalho,seguids de outras atributos de temperatura. No caso de Iquitos a umidade relativa também possui algum destaque. Em ambos os indíces de vegetação possuem as mais baixas correlações com o número de casos de dengue.
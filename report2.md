# Relatorio 2 - Outline

## Introdução
- Objetivos são principalmente de analise exploratória do problema, 
qual a natureza das variáveis e do problema.
- Iremos apresentar os resultados com um modelo Baseline (SARIMA), 
fazendo uma revisão teórica e analise das qualidades e limitações
- Esse modelo não se diferencia do que é tradicionalmente usado na literatura,
optamos em ter um baseline embasado para focar na aplicação de diferentes modelos
na próxima etapa do projeto.


## Analise Exploratória

- Uma linha sobre cada cidade (montanha/praia/etc).

- Explicar quais são os dados e as fontes
    - imagem da série temporal (relatorio 1) / Histograma
    - Lista dos dados com fonte e descrição, média e std
    
- Analise de correlação
    - Apontar obvia sasonalidade da série temporal
        - Comentar que sasonalidade além de ano a ano, ocorre a cada 3ou4 
        anos provavelmente devido a imunizacao da populaçao apos uma epidemia
    - Tabela de cross-corelation
        - citar que alguns dados são redundantes (varias temps) e provavelmente serao agregados
    - Falar que dados das duas cidades tem comportamentos diferentes
    - Apontar quais features são mais preditivos em cada caso

- Conclusoes

## Modelagem

Levando em consideração as referências levantadas durante a primeira parte do projeto fizemos explorações com modelos (S)ARIMA em comparação com uma alternativa "ingênua" de Regressão Linear com o enfoque em estabelecimento de baselines e entendimento de práticas comuns de ciência de dados. 

### Regressão linear

- Descrição de regressão Linear
- Regressão Linear no tempo

### Sarima

- Descrição do modelo

### Consideracoes praticas

Por questões pragmáticas, a implementação das análises e modelos foi realizada em **python** e o código se encontra disponível em: https://github.com/jsiloto/dengAI. 
O modelo de regressão linear foi implementado usando a biblioteca `sklearn`que implementa utilizando o algorítimo de mínimos quadrados para minimização da norma $l_2$. Os modelos SARIMA foram implementados utilizando a biblioteca `statsmodels`, que utiliza necessáriamente o critério de máxima verossimilhança baseado em filtros de Kalman, e [por consequência otimiza a norma $l_2$](http://web.mit.edu/kirtley/kirtley/binlustuff/literature/control/Kalman%20filter.pdf). Foi utilizado o  otimizador padrão `LBFGS`, baseado em descida de gradiente de segunda ordem, foram testados outros otimizadores sem sucesso.


## Experimentos

### Features e hyperparametros



Valores 111, 111 foram escolhidos por?



### Resultados


- a maior parte dos tratamentos dos dados não resultou em grandes diferencas
- regressão linear muito bons mas é extremamente sensivel ao parametro de LAG
- Sasonalidade de um ano é clara, mas existe uma sasonalidade de 3 anos que não é levada em conta ( Ver residual 3)
- Dynamic harmonic regression? (https://otexts.com/fpp2/complexseasonality.html)
- Decidimos usar modelos separados para as duas cidades
- Variaveis foram escolhidas por criterio de cross-correlation

Tabela
- Variaveis exogenas | Log | Normalização | San Juan | Iquitos


#### Resultados nos testes
Fazer uma submissão ao challenge e reportar os resultados


## Próximos Passos

Consideramos que concluída a faze exploratória do projeto e para os próximos passos esperamos ter um foco no aprimoramento dos modelos existentes e desenvolvimento e teste de modelos alternativos. Em específico pretendemos atacar os três pontos a seguir:
    - Melhor engenharia de features para os modelos SARIMA
    - Testes com redes neurais MLP e redes convolucionais causais.


# Nota de Transparencia
Deixamos claro que estamos cientes da existência de diversas outras implementações públicas para o mesmo desafio(footnote) e que fizemos uso desse recurso para aprendizado, além da utilização de pequenos trechos de código para análise dos dados, porém nenhum desses recursos foi utilizado para escolha ou desenvolvimento dos modelos preditivos.


footnote: Em 03/09/2019 a pesquisa por dengai no github retorna 194 repositórios.

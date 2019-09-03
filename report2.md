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

## Modelo

### Descrição teórica do modelo

- ARMA
- ARIMA
- SARIMA

## Experimentos

### Feature Engineering
- Normalização
    - log vs nao log
- Agregação


### Consideracoes praticas

- Qual biblioteca foi utilizada
- Onde está o código fonte
- Box Jenkins não está disponivel no statsmodels, segundo a documentação da biblioteca
o metodo utilizado é LBFGS minimizando MLE por filtro de Kalman (whatever that means)
- Testes com outros metodos de otimização e parametros da biblioteca foram utilizados sem
sucesso.



### Resultados
- Regressão linear sem dados temporais
- Regressão linear temporal/ sem outros dados
- SARIMA
- SARIMAX
    - Todos os Dados
    - Feature Engineering
    
- Sasonalidade de um ano é clara, mas existe uma
 sasonalidade de 3 anos que não é levada em conta ( Ver residual 3)
 Dynamic harmonic regression? (https://otexts.com/fpp2/complexseasonality.html)


#### Resultados nos testes
Fazer uma submissão ao challenge e reportar os resultados

## Nota de Transparencia


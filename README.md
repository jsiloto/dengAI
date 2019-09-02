# Predição de Número de Casos de Dengue

Repositorio do projeto da disciplina de "Dados, Inferência e Aprendizagem" 
ministrada no 2o Semestre de 2019 pelos professores 
José Cândido Silveira Santos Filho e Flavio du Pin Calmon

Alunos:
Antonio José Pinheiro Prado
Juliano Siloto Assine
Luiz Eduardo Pita Mercês Almeida

[Relatorio 1](report1.pdf)

[Planos para Relatorio 2](report2.md)

## Links Uteis
https://github.com/miguelTorresPorta/TimeSeries/blob/master/timeSeries.ipynb
https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/
https://machinelearningmastery.com/make-sample-forecasts-arima-python/
https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
https://arxiv.org/pdf/1709.01907.pdf
https://github.com/philipperemy/keras-tcn
http://www.dca.fee.unicamp.br/~lboccato/EFC1_IA006_1s2019.pdf

## How-To
```bash
docker build -t dengai .
docker run --rm -it --name dengai -v $PWD:/tf dengai
```


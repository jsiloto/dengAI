# RNN e LSTM

As Redes Neurais Recorrentes são uma família de redes neurais capazes de lidar com sequências de dados. Elas são arquitetadas de modo a compartilhar informações entre o evento atual e os anteriores. Nessa arquitetura as informações persistem devido a realimentação (*loop*) dos dados passados. Assim são muito utilizadas no processamento de dados de fala, texto, vídeo e séries temporais.

As redes recorrentes são formadas por uma cadeia de unidades repetitivas de rede neural. A unidade recorrente atua como uma espécie de memória uma vez que recebe como entrada os dados do evento atual e dos seus predecessores. Assim, durante o treinamento devido ao grande número de derivações, as arquitetura clássica de RNN (Vanilla) sofre com o problema de saturação do gradiente: sumiço (*vanishing*) e explosão (*explosion*). Além disso, essa arquitetura é muito sucetível a dados ruidosos e valores atípicos (*outliers*) por guardar todos os dados sem nenhum tipo de seleção.

Buscando resolver esses problemas, surgiu a arquitetura LSTM (*Long Short-Term Memory*), definida por  Hochreiter e Schmidhuber em 1997. Ela introduz na unidade recorrente três portões (*gates*): portão de esquecimento (*forget gate*), portão de entrada (*input gate*) e portão de saída (*output gate*). A LSTM introduz também o conceito de estado da célula que representa a informação a ser mantida. 

Cada portão atua sobre o estado da célula de uma forma distinta. Enquanto portão do esquecimento remove informações que não são mais úteis do estado da célula, o portão da entrada adiciona novas informações úteis. Por sua vez, o portão de saída tem a função de extrair do estado da célula as informações que serão apresentadas como saída. 

Cada portão, de forma distinta, é formulado com pesos que são atualizados durante o treinamento. Esses juntamente com as funções de ativação, levam a LSTM a aprender quais informações devem ser excluídas, adicionadas e mantidas para obtenção das respostas que reduzem o erro do treinamento. 


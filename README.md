# Dengue Epidemic Forecasting

This repository contains the code and reports(in portuguese) for the 
final project in the course: "Dados, Inferência e Aprendizagem" taught at
UNICAMP on September 2019.

The project team is composed by:
- Antonio José Pinheiro Prado
- Juliano Siloto Assine
- Luiz Eduardo Pita Mercês Almeida


## Reports
- [Report 1](report1.pdf)
- [Report 2](report2.pdf)
- Report 3 in progress

## How-To
```bash
docker build -t dengai .
nvidia-docker run --rm -it -p 8888:8888 --name dengai -v $PWD:/tf dengai
```


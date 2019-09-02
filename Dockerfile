FROM tensorflow/tensorflow:1.14.0-gpu-py3-jupyter

RUN apt-get update && apt-get install -y \
    wget \
    aria2

RUN pip install \
    numpy \
    pandas \
    sklearn \
    scipy \
    pandas \
    statsmodels
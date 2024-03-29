FROM tensorflow/tensorflow:1.14.0-gpu-py3-jupyter

RUN apt-get update && apt-get install -y \
    wget \
    aria2 \
    git

RUN pip install \
    numpy \
    pandas \
    sklearn \
    scipy \
    pandas \
    statsmodels \
    sklearn \
    pandas \
    statsmodels \
    seaborn \
    keras-tcn \
    keras-rectified-adam

RUN pip install git+https://github.com/drivendataorg/drivendata-submission-validator.git
# Report 3 Outline

## Introduction

Describe our objectives:
- Further analysis and understanding of the problem
- Consolidate software approach with a standard procedure for any model (see repo)
- Make one good submission
- Syntethize previous work

## The Data
- Data from 2 cities and meteorological data
- Statistics from 2 cities are very different
- Correlation analysis
    - Autocorrelation
    - Cross Correlation(Tables) and Spearman correlation
    - Delayed Correlation and Thresold correlation
        (pick a value threshold and divide 2 groups: peak and no peak)
    - Try Delayed Correlation divided by feature autocorrelation

## The Problem
- Time Series Forecasting, Talk about basics
- Describe autoregression as basis for all forecasting
- Describe the challenge format
- Differentiate from traditional forecasting. Although the concept of
exogenous variables exist, it is not expected to have sensor data of the future
- Describing forecasting loop
- Long term Forecasting is very difficult (cite other works) (Cite master
    thesis with 12 weeks forecasting vs our problem: 180 weeks forecasting),
    talk about positive feedback loop and the need to use the features.
- Peaks are particularly difficult to forecast, is there a trigger?
- Augument data with peak classification?
- Describe our approaches:
Feature Regression vs Feature Autoregression

Picture of window matrix

## The model
- First attempts with temporal autoregression had no success, 
but made clear that the autoregression window size and train/validation split
sizes can influence heavily the results. Good models should be invariant to those.
- Attempts with causal convolution networks \cite{wavenet} were made, but although
it could halucinate "realistic looking peaks" it didn't match the validation data.
- For its generality in usage we used MLP networks.
# MLP
# RNN

## Results

- Choose a window based on data analysis (See delayed correlation)
- Mention the and repo and standard way to implement more models (maybe?)

## Discussion and Conclusion

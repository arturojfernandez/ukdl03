# Exercise
## Introduction

The goal of this exercise is to evaluate the familiarity of the candidate with pandas, applying data transformations and manipulations.

You have to build a transformation `pipeline` that will look as follows:

1. read data
1. perform join with normative source to add feature
1. run time series function over time series columns to add feature
1. run model
1. perform banding of results
1. save results

More detail is given on each step below. Steps 2 and 3 can be performed in any order.

You are provided with:
* data.csv - dataset in CSV with a header and no index
* normative.csv - normative source (two column CSV key, value with a header and no index)
* model.pkl - sklearn model in pickle format
* demo.py - example script demonstrating how to run model on a two-row array
* requirements.txt - python libraries to install using pip

The duration of the exercise is 1.5h, however it is not necessary to complete the exercise in this time.
You should explain the approach and the ideas to the reviewer in a pair programming exercise.
The approach must be **object oriented** and **tested** using the unittest framework or any other testing framework with which you feel comfortable.**

## Setup environment
Clone the code, Source a python 3.8 environment and create a feature branch in order to PR this exercise later.
Install the requirements in `requirements.txt` using pip.

# Tasks
Design and implement an abstract class called `BaseTask` based in the fact that we are going to execute tasks sequentially and the output of one will be the intput of the next one.

## 1. Read data

In the data directory you'll find two CSV files: `data.csv` and `normative.csv`.
Create a data access class that reads these CSVs via pandas and retrieves DataFrames per each file.

## 2. Run time series function over time series columns to add feature

Create a `TimeSeriesSummaryTask` task that runs `EWMA` over the time series columns `[balance_0, balance_1, balance_2]`.
There is a `pandas` function for this.
Hint: `df[columns].ewm(alpha=1.).mean().values[:, -1]`
Save the result in a new column.

## 3. Perform join with normative source to add feature

Create a Join class called JoinTask whose responsibility is to merge the normative and the data features, to add a column to the data.

## 4. Run model

Create an InferenceTask whose responsibility is to run the model on the relevant columns of the dataframe.
Those columns are EWMA and INCOME, that you generated as part of the pipeline.

## 5. Perform banding of the results

Create a PostprocessTask whose responsibility it is to band the outputs of the model into a categorical variable.
The banding is defined as follows:
* `[0.0, 0.002) = A`
* `[0.002, 0.7) = B`
* `[0.7, 1.0] = C`

N.B.: Range notation above means that square brackets are inclusive and round brackets are exclusive.
i.e. `0.0 in [0.0, 0.002) = True`
i.e. `0.002 in [0.0, 0.002) = False`

## 6. Save results

Create a SaveTask that saves the output column as a csv.

## 7. Create a run script

Create a script to run the pipeline from start to finish.

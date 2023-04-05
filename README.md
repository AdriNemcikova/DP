# Using deep learning to analyze light curves of variable stars
## Adriana Nemcikova - Diploma thesis
### 2023, HI, KKUI, FEI TUKE

## Datasets
We used next dataset for our experiments:
* synthetic over-contact data - available [here](https://mega.nz/file/5m43WQyK#G2WuLjqAkQT0OxQ4j-rZarCnmbtEx1rDQppiFNX8GdM)
* synthetic detached data - available [here](https://mega.nz/file/g3hVAKaT#NYCF7TzrOvn11laTDz5rTz3_dHnKClOfwhFzACepnig)
* observed over-contact - created with [script](https://github.com/AdriNemcikova/DP/blob/master/observed/create_over.ipynb) available [here](https://github.com/AdriNemcikova/DP/blob/master/observed/observed_over.csv)
* observed detached - created with [script](https://github.com/AdriNemcikova/DP/blob/master/observed/create_det.ipynb) available [here](https://github.com/AdriNemcikova/DP/blob/master/observed/observed_det.csv)

## Exploratory analysis.
In this script we worked on exploratory analysis of each dataset we were provided with.
* [Exploratory_analysis.ipynb](https://github.com/AdriNemcikova/DP/blob/master/Exploratory_analysis.ipynb)

## Experiments with observed data
### Scripts for creating csv files of observed binary systems data. 
In this two script we create csv files that contains data about observed binary systems. We loaded all data from JSON files in the same directory.
* [observed/create_det.ipynb](https://github.com/AdriNemcikova/DP/blob/master/observed/create_det.ipynb)
* [observed/create_det.ipynb](https://github.com/AdriNemcikova/DP/blob/master/observed/create_over.ipynb)

## Experiments with overcontact data
### Scripts with experiments, where we trained NN models to predict physical parameters of **over-contact** binary systems.
In those script we worked on experiments, where we trained neural network models to predict physical parameters of over-contact binary systems. Output of each script 
is one trained model in format *.hdf5*.
* [over_all_parameters_model.ipynb](https://github.com/AdriNemcikova/DP/blob/master/over_all_parameters_model.ipynb)
* [NORM_over_all_params.ipynb](https://github.com/AdriNemcikova/DP/blob/master/NORM_over_all_params.ipynb)
* [NORM_over_selected_params.ipynb](https://github.com/AdriNemcikova/DP/blob/master/NORM_over_selected_params.ipynb)

## Experiments with detached data
### Scripts with experiments, where we trained simple combined NN model architectures to predict physical parameters of **detached** binary systems.
In those script we worked on experiments, where we trained neural network models to predict physical parameters of **detached** binary systems. Output of each script 
is one trained model in format *.hdf5*.
* [DET_all_parameters_model.ipynb](https://github.com/AdriNemcikova/DP/blob/master/DET_all_parameters_model.ipynb)
* [NORM_detached_all_params.ipynb](https://github.com/AdriNemcikova/DP/blob/master/NORM_detached_all_params.ipynb)

In the next script we created experiment, where we trained different architectures to predict attributes of detached data on smaller data set. After evaluating each 
model on test set, we decided to train best architecture on bigger data set.
* [DET_models_architectures.ipynb](https://github.com/AdriNemcikova/DP/blob/master/DET_models_architectures.ipynb)

### Script, where we worked on experiments to create multi NN model to predict different combination of physical attributes.
* [MultiNN_norm.ipynb](https://github.com/AdriNemcikova/DP/blob/master/MultiNN_norm.ipynb) - predicting normed values of attributes *inclination, mass ratio, 
temperature ratio, omega 1, omega 2*
* [MultiNN_radius.ipynb](https://github.com/AdriNemcikova/DP/blob/master/MultiNN_radius.ipynb) - predicting normed values of attributes *inclination, mass ratio, 
temperature ratio, primary radius, secondary radius*

While still working with detached synthetic data, we decided to create **script, where we compared all trained models, or models we were provided with from other 
experiments**.
* [DET_all_model_comparison.ipynb](https://github.com/AdriNemcikova/DP/blob/master/DET_all_model_comparison.ipynb)

### Script, where we used best models to predict attributes of observed data. 
* [OBSERVED_predictions.ipynb](https://github.com/AdriNemcikova/DP/blob/master/OBSERVED_predictions.ipynb)

### Script we used to create subset of data
Since we wanted to back-plot light curves from predicted values, we need to create subset of data, which contains true and predicted values.
* [create_subsets_to_plot.ipynb](https://github.com/AdriNemcikova/DP/blob/master/create_subsets_to_plot.ipynb)

## Sensitivity analysis
We created experiment of sensitivity analysis fo **detached** data, where we shifted predicted values, 1 value, up, 2 values up and 1 value down. We saved shifted 
predictions in specified [folders](https://github.com/AdriNemcikova/DP/tree/master/Detached_sensitivity_analysis). Second script contains code to merge plotted 
predictions. All plotted shifted predictions and its comparison can be find [here](https://mega.nz/file/ICg0kZqL#ay_nBvzu0Xy1ydGZ6C6bSzPqB3-ZJ5RVGIw0hGNUV0Y) in zip file.
* [DET_sensitivity_analysis_all.ipynb](https://github.com/AdriNemcikova/DP/blob/master/DET_sensitivity_analysis_all.ipynb)
* [comparison_prediction.py](https://github.com/AdriNemcikova/DP/blob/master/ml_predictor_evaluator/src/comparison_prediction.py)

## Back-plotting of light curves
Since we wanted to analyze light curves of true and predicted values of physical attributes, we worked with next scripts:
* [Main script](https://github.com/AdriNemcikova/DP/blob/master/ml_predictor_evaluator/src/main.py) - which we used to get plotted light curves
* [Config file](https://github.com/AdriNemcikova/DP/blob/master/ml_predictor_evaluator/src/config.py) - where are defined physical properties to calculate light curve
from provided true and predicted values.

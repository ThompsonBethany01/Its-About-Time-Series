![Readme-Header](https://i.pinimg.com/originals/13/c2/8a/13c28a37e6742c5a981e182467acf2ee.png)  

## Table of contents
- [About the Project](https://github.com/ThompsonBethany01/Its-About-Time-Series#About-the-Project)
- [Data](https://github.com/ThompsonBethany01/Its-About-Time-Series#Data)
- [Project Steps](https://github.com/ThompsonBethany01/Its-About-Time-Series#Project-Steps)
- [How to Reproduce](https://github.com/ThompsonBethany01/Its-About-Time-Series#How-to-Reproduce)
- [Author](https://github.com/ThompsonBethany01/Its-About-Time-Series#Author)

# About the Project
## Background
Here at Big Research Co.®, we love data so much - everyone wears Fitbits, even our employees! We believe these watches are the next step in the Big Data Industry and help enhance our current research. Our research spans from fitness equiptment and drug trials to ~very ethical~ human experimentation.

## Goals
Everybody makes mistakes, even here at B.R.Co.®! Someone in a lab coat mixed up the labels for our Fitbit data, and one was left out. This Dr. Lab Coat handed me a usb containing the data in question. I need to determine what characteristics belong to the person wearing the Fitbit (did I mention it could be an employee or test subject?). That's not all, Dr. Lab Coat obscurley asked for predictions on the next two weeks of data that will be missing - missing because of the mix-up? Who knows, I just started here a week ago.

<details>
  <summary>Deliverables</summary> 
  
   - Predictions.csv  
      - a file of predictions for the missing two weeks of data  
   - Analysis.ipynb  
      - notebook detailing the process to obtain my predictions and conclusions
   - Prepare.ipynb   
      - notebook detailing the process to clean the data from raw to finished
   - Summary of the data   
      - what was the individual like?
   - Presentation  
      - two content slides  
      - at least one visual
  
</details>  

## Data 
### The USB
Are you dying to know what's in the usb yet? Here's the low down below.  
![USB-Files](https://i.pinimg.com/originals/d8/6f/22/d86f2200de039786ecec46658534e186.png)  
### Data Dictionary
After using the Prepare.py module, the data frame will contain the columns as described below. Only the first two tables from the files were included, as a majority of the food log table had no data.   

| Column Name         | Description                                               |
|---------------------|-----------------------------------------------------------|
| date                | yyyy-mm-dd, df index                                      |
| cals_burned         | calories burned for the day                               |
| steps               | steps taken in the day                                    |
| dist                | distance walked, possibly in miles                        |
| floors              | uncertain, possible floors walked up or down              |
| mins_sedentary      | minutes of the day sedentary                              |
| mins_lightly_active | minutes of the day lightly active                         |
| mins_fairly_active  | minutes of the day fairly active                          |
| mins_very_active    | minutes of the day vary active                            |
| activity_cals       | uncertain, possibly calories burned due to active minutes |
| month               | month of the observation                                  |
| weekday             | weekday of the observation                                |  

# Project Steps
## Acquire
Data within the usb came in eight seperate files - one for a month's worth of observations. To join the files together, each file was uploaded into one google sheets document with each file in its own sheet. The data was added all together in one sheet as well. The final sheet to be exported as a csv file did not include the food log as it contained more than 95% of zero values. Columns with numbers containing commas (like 2,345) were converted to integers with no commas. To look at this google sheet, click [here](https://docs.google.com/spreadsheets/d/1ZjPl1BCtA8K_U5_0DT94LAOfqYanNKf2_9_B4tespWA/edit?usp=sharing).
## Prepare
The function to prep the data is within the Prepare.py module. After using the function, the data:
- date column is converted to a datetime type.  
- index is set to the date column.  
- contains additional columns for the observation month and weekday.  

A seperate function in the Prepare.py module splits the data by:
- making index to split based off 70% point of index
- setting train to every data point up to this index
- setting test to every data point starting at this index and on
-returns the train and test dfs

Additional prep was not neccessary, as the raw data was fairly clean. There were no nulls, and the only column with possible outliers is floors. More features may be added later during the explore and model process.
## Explore
Univariate analysis was done on the whole dataframe to determine distributions of the individual features. Further analysis was completed on the train df with time series. Data was resampled by weekly, bi-weekly, and monthly periods to visualize trends, if any. Made conclusions on the individual based on this exploration.

## Model
Five different models were created and tested on the split dataframes. There was a:  
- Simple average, the baseline
  - predicts each future observation as the overall average
- Weekly rolling average
  - predicts each future obsrvation as the most recent weekly average
- Monthly rolling average
  - predicts each future observation as the most recent monthly average
- Holt's Linear Trend
  - exponential smoothing applied to both the average and the trend
  - one model with optimized = true
  - one model with alpha = .1 and beta = .1
  
To determine which model was best for each feature (df column):
1. Predicted Validate by fitting models on Train.
2. Calculated RMSE. Created an evaluation df to hold the feature RMSE with the model name.
3. Combined Train and Validate. Predicted Test by fitting models on the Train+Validate df.
4. Calculated RMSE and added as new column in the evaluation df.  

An example of the evaluation df:
| Target Name   | Model Name   | rmse | test rmse |  
|---------------|--------------|------|-----------|
|calories burned|simple average|123.45|234.56     |

5. Evaluated models for each feature with the eval_df, taking into consideration both rmse
6. Once the models were choosen, predicted the next two weeks of unkown data fit on the whole df
7. Combined the predictions in one dataframe to save as a .csv file

## Conclusions 
![Individual-Characteristics](https://i.pinimg.com/originals/29/90/84/299084d50764c7338477fd3c2355d234.png)  

The final models chosen to predict the next two weeks of the data was a rolling 7-day average and Holt Optimized. These predictions are uploaded to this repo in the file titled Predictions.csv.

## Next Steps
Create functions for modeling in a Model.py file to clean up the final notebook used.

# How to Reproduce
- [x] Read this Readme
- [ ] Download <kbd>Prepare.py</kbd> and <kbd>Analysis.ipynb</kbd> in your working directory
- [ ] Run the notebook or do your own exploration and modeling

# Author
[Bethany Thompson](https://github.com/ThompsonBethany01)   
Feel free to reach out to me for any questions, comment, or suggestions!

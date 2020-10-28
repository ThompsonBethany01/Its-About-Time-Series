import pandas as pd

def prep_data():
    '''
    Prepare the fitbit data by reading the csv file as the df,
    setting index to datetime column, and creating new date columns.
    '''
    df = pd.read_csv('Fitbit_Joined.csv')
    
    # converting date column to datetime
    df.date = pd.to_datetime(df.date)

    # setting date column to index
    df = df.set_index("date").sort_index()
    
    # Adding columns for date categories of weekday and month
    # month of the observation
    df['month'] = df.index.month

    # weekday name of the observation
    df['weekday'] = df.index.day_name()
    
    return df
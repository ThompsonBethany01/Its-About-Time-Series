import pandas as pd

######################################################################################

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

######################################################################################

def split_data(df):
    '''
    Takes a df and splits by the index, 70% for train and 30% for test
    '''
    # determining index for splitting the data
    train_size = .70
    n = df.shape[0]
    test_start_index = round(train_size * n)

    train = df[:test_start_index] # everything up (not including) to the test_start_index
    test = df[test_start_index:] # everything from the test_start_index to the end

    return train, test
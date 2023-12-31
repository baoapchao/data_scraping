import os
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# get min date
def get_min_date_year (df_all, column_name, datetime_format):
    df_all['Date_standardized'] = df_all[column_name].apply(lambda x: datetime.strptime(x, datetime_format))
    min_date = df_all['Date_standardized'].min()
    min_year = int(min_date.strftime('%Y'))
    return min_date, min_year

# get min max month to be api parameters
def get_formatted_start_end_month(year, month, datetime_format):
    start_month = datetime(year, month, 1)
    start_month = start_month.strftime(datetime_format)
    if month < 12:
        start_next_month = datetime(year, month + 1, 1)
        end_month = start_next_month - timedelta(days = 1)
        end_month = end_month.strftime(datetime_format)
    elif month == 12: 
        end_month = datetime(year, 12, 31)
        end_month = end_month.strftime(datetime_format)
    return start_month, end_month

# get min max month to be api parameters
def get_formatted_start_end_year(year, datetime_format):
    start_year = datetime(year, 1, 1)
    start_year = start_year.strftime(datetime_format)
    end_year = datetime(year, 12, 31)
    end_year = end_year.strftime(datetime_format)

    return start_year, end_year

# filtering 

def add_standard_datetime_column(df, datetime_column, datetime_format):
    df[datetime_column + '_standard'] = df[datetime_column].apply(lambda x: datetime.strptime(x, datetime_format))
    return df

def filter_datetime(df, datetime_column, datetime_format, filter_type, year, month=1):
    start_date = datetime(year, month, 1, 0 , 0)
    if filter_type == 'year':
        end_date = datetime(year, 12, 31, 23 , 59) 
    elif filter_type == 'month':
        end_date = datetime(year, month, 1, 23 , 59) + relativedelta(day=31)

    df = add_standard_datetime_column(df, datetime_column, datetime_format)
    df_filtered = df.loc[(df[datetime_column + '_standard'] >= start_date) & (df[datetime_column + '_standard'] <= end_date)]
    return df_filtered


# export dataframe to csv

def df_to_csv(df, *args):
    args = [str(arg) for arg in args]
    path = os.path.join('data', *args)
    file = os.path.join(path, '-'.join([str(arg) for arg in args]) + '.csv')
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    df.to_csv(file)
    print(f"Successfully export csv for {'-'.join([str(arg) for arg in args])}")

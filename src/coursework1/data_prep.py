# Data preparation and understanding code
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
## Data Preparation

#Define a function to gather the information of target dataframe
def print_df_information(Dataframe):
    print("\nNumber of rows and columns:\n")
    print(Dataframe.shape)
    print("\nFirst 7 rows:\n")
    print(Dataframe.head(7))
    print("\nLast 6 rows:\n")
    print(Dataframe.tail(6))
    print("\nColumn labels:\n")
    print(Dataframe.columns)
    print("\nColumn labels, datatypes and value counts:\n")
    print(Dataframe.info())
    print("\nColumn data types:\n")
    print(Dataframe.dtypes)
    print("\nStatistics:\n")
    print(Dataframe.describe())

# Define a function to read the Excel file and output a certain sheet as Dataframe
def create_dataframe_xlsx(xlsx_file, sheet_name):
    df = pd.read_excel(xlsx_file, sheet_name=sheet_name)

    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    return df


# Define a function that allows to insert one dataframe into another at specific position
def dataframe_insert(df1, df2, position):
    # Define the position where to insert df2 (between rows)
    # Split df1 into two parts and insert df2 in between
    part1 = df1.iloc[:position]
    part2 = df1.iloc[position:]
    # Concatenate the parts with df2 in the middle
    result = pd.concat([part1, df2, part2], ignore_index=True)

    return result


# Define a function to check the missing value
def missingvaule_check(Dataframe, name=None):
    missing_rows = Dataframe[Dataframe.isna().any(axis=1)]
    print(f"Missing Value check for the DataFrame:{name}\n")
    print(missing_rows)

# Define a function to save the prepared data
def save_CSVfile(dataframe,name):
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath("coursework1").joinpath("Prepared Data").joinpath(
        f"{name}.csv")
    dataframe.to_csv(prepared_csv_filepath, index=False)


if __name__ == '__main__':
    raw_data_file_aposw = Path(__file__).parent.parent.joinpath("coursework1").joinpath("dataset").joinpath(
        "access-public-open-space-ward.xls")

    # Obtain the Dataframe for 4 sheets in the Excel file
    df_Open_space_2013_wards = create_dataframe_xlsx(raw_data_file_aposw, 'Open space 2013 wards')
    df_Open_space_2014_wards = create_dataframe_xlsx(raw_data_file_aposw, 'Open space 2014 wards')
    df_Access_to_open_space_2013_wards = create_dataframe_xlsx(raw_data_file_aposw, 'Access to open space 2013 wards')
    df_Access_to_open_space_2014_wards = create_dataframe_xlsx(raw_data_file_aposw, 'Access to open space 2014 wards')

    #the information of dataframe above can be obtianed by function print_df_information(Dataframe)
    print_df_information(df_Open_space_2013_wards)
    print_df_information(df_Open_space_2014_wards)
    print_df_information(df_Access_to_open_space_2013_wards)
    print_df_information(df_Access_to_open_space_2014_wards)


    # Remove three wards (Hackney, Tower Hamlets, and Kensington and Chelsea) from df_Open_space_2013_wards,
    # because they changed in 2014
    df_Open_space_2013_wards_without_changed_wards = df_Open_space_2013_wards
    # Remove Hackney
    for num in range(18 + 1):
        df_Open_space_2013_wards_without_changed_wards = df_Open_space_2013_wards_without_changed_wards.drop(
            [205 + num])
    # Remove Tower Hamlets
    for num in range(16 + 1):
        df_Open_space_2013_wards_without_changed_wards = df_Open_space_2013_wards_without_changed_wards.drop(
            [547 + num])
    # Remove Kensington and Chelsea
    for num in range(17 + 1):
        df_Open_space_2013_wards_without_changed_wards = df_Open_space_2013_wards_without_changed_wards.drop(
            [356 + num])
    # Add the data of Open space 2014 wards to df_Open_space_2013_wards_without_changed_wards
    df_Open_space_2013_wards_without_changed_wards.reset_index(drop=True, inplace=True)

    # Rename the columns of df_Open_space_2014_wards and ensure the column names are the same as them in df_Open_space_2013_wards_without_changed_wards
    df_Open_space_2014_wards.columns = df_Open_space_2013_wards_without_changed_wards.columns
    # Use the dataframe_insert() defined above, to obtain the combination of df_Open_space_2013_wards_without_changed_wards and df_Open_space_2014_wards
    df_Open_space_wards = dataframe_insert(df_Open_space_2013_wards_without_changed_wards, df_Open_space_2014_wards,
                                           570)

    # Check that any missing values
    # missingvaule_check(df_Open_space_wards, name='Open_space_wards')
    # The vaules that shows NaN are okay for this dataset, some of them are the boroughs which do not have a ward name,
    # the rest of them is Intentionally blank, to better differentiate the data

    # Remove three wards (Hackney, Tower Hamlets, and Kensington and Chelsea) from df_Access_to_open_space_2013_wards,
    # because they changed in 2014
    df_Access_to_open_space_2013_wards_without_changed_wards = df_Access_to_open_space_2013_wards
    for num in range(18 + 1):
        df_Access_to_open_space_2013_wards_without_changed_wards = df_Access_to_open_space_2013_wards_without_changed_wards.drop(
            [207 + num])
    for num in range(16 + 1):
        df_Access_to_open_space_2013_wards_without_changed_wards = df_Access_to_open_space_2013_wards_without_changed_wards.drop(
            [549 + num])
    for num in range(17 + 1):
        df_Access_to_open_space_2013_wards_without_changed_wards = df_Access_to_open_space_2013_wards_without_changed_wards.drop(
            [358 + num])

    # Rename the columns of df_Open_space_2014_wards and ensure the column names are the same as them in df_Open_space_2013_wards_without_changed_wards
    df_Access_to_open_space_2014_wards.columns = df_Access_to_open_space_2013_wards_without_changed_wards.columns
    # Use the dataframe_insert() defined above, to obtain the combination of df_Open_space_2013_wards_without_changed_wards and df_Open_space_2014_wards
    df_Access_to_open_space_wards = dataframe_insert(df_Access_to_open_space_2013_wards_without_changed_wards,
                                                     df_Access_to_open_space_2014_wards, 572)
    # Use the first row as column names and remove the current column names (at this stage, the column names are N.A.)
    df_Access_to_open_space_wards.columns = df_Access_to_open_space_wards.iloc[0]
    df_Access_to_open_space_wards = df_Access_to_open_space_wards[1:]
    # Add 'Percentage of households with access to:' to the column names from 4 to 8
    new_columns = df_Access_to_open_space_wards.columns[:3].tolist() + [
        f'Percentage of households with access to: {col}' for col in
        df_Access_to_open_space_wards.columns[3:8]]
    df_Access_to_open_space_wards.columns = new_columns

    # Check that any missing values
    # missingvaule_check(df_Access_to_open_space_wards, name='Access_to_open_space_wards')
    # The vaules that shows NaN are okay for this dataset, they are Intentionally blank, to better differentiate the data

    # Save to CSV file
    #save_CSVfile(df_Open_space_wards,'Open Space Wards')
    #save_CSVfile(df_Access_to_open_space_wards, 'Access to Open Space Wards')

    #Data Exploration

    #for Open Space Wards

    #Draw a scatter graph of % of open space that has access (Open Space with access/All Open Space)
    target_data = df_Open_space_wards.iloc[1:654,:]
    ax1 = df_Open_space_wards.iloc[1:654,:].plot.scatter(x='All Open Space',y='Open Space with access',c='DarkBlue')
    plt.show()

    # Draw a scatter graph of % Open Space with access (Open Space with access/Total area of ward)
    ax2 = df_Open_space_wards.iloc[1:654, :].plot.scatter(x='Total area of ward (sq m)',y='Open Space with access',c='DarkBlue')
    plt.show()

    # Use hist() to represent the distribution of data
    hist = df_Open_space_wards.iloc[1:654,:]['% open space'].hist()
    hist.plot()
    plt.show()

    # Use dp.plot.bar to plot a bar graph of Ward name vs. % open space for all the ward data
    ax = df_Open_space_wards.iloc[1:654, :].plot.bar(x='Ward_NAME', y='% open space', rot=0,figsize=(200, 20))
    plt.show()

    # for Access to Open Space Wards
    # Use dp.plot.bar to plot a bar graph of Ward name vs. Percentage of households with access to: Open Space of the first 50 data
    ax = df_Access_to_open_space_wards.iloc[0:49, :].plot.bar(x='Ward name', y='Percentage of households with access to: Open Space', rot=0,figsize=(100, 20))
    plt.show()

    #pd.set_option('display.max_rows', df_Access_to_open_space_wards.shape[0] + 1)
    #pd.set_option('display.max_columns', df_Access_to_open_space_wards.shape[1] + 1)
    # print(df_Open_space_wards.isna())
    #print(df_Access_to_open_space_wards)

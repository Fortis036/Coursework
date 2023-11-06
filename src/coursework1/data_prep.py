# Data preparation and understanding code
from pathlib import Path
import pandas as pd


# Define a function to read the Excel file and output a certain sheet as Dataframe
def create_dataframe_xlsx(xlsx_file, sheet_name):
    df = pd.read_excel(xlsx_file, sheet_name=sheet_name)

    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    return df

# Define a function that allows to insert one dataframe into another at specific position
def dataframe_insert(df1,df2,position):
    # Define the position where to insert df2 (between rows)
    # Split df1 into two parts and insert df2 in between
    part1 = df1.iloc[:position]
    part2 = df1.iloc[position:]
    # Concatenate the parts with df2 in the middle
    result = pd.concat([part1, df2, part2], ignore_index=True)

    return result

if __name__ == '__main__':
    raw_data_file_aposw = Path(__file__).parent.parent.joinpath("coursework1").joinpath("dataset").joinpath(
        "access-public-open-space-ward.xls")

    # Obtain the Dataframe for 4 sheets in the Excel file
    df_Open_space_2013_wards = create_dataframe_xlsx(raw_data_file_aposw, 'Open space 2013 wards')
    df_Open_space_2014_wards = create_dataframe_xlsx(raw_data_file_aposw, 'Open space 2014 wards')
    df_Access_to_open_space_2013_wards = create_dataframe_xlsx(raw_data_file_aposw, 'Access to open space 2013 wards')
    df_Access_to_open_space_2014_wards = create_dataframe_xlsx(raw_data_file_aposw, 'Access to open space 2014 wards')

    # Remove three wards (Hackney, Tower Hamlets, and Kensington and Chelsea) from df_Open_space_2013_wards,
    # because they changed in 2014
    df_Open_space_2013_wards_without_changed_wards = df_Open_space_2013_wards
    # Remove Hackney
    for num in range(18 + 1):
        df_Open_space_2013_wards_without_changed_wards = df_Open_space_2013_wards_without_changed_wards.drop([205 + num])
    # Remove Tower Hamlets
    for num in range(16 + 1):
        df_Open_space_2013_wards_without_changed_wards = df_Open_space_2013_wards_without_changed_wards.drop([547 + num])
    # Remove Kensington and Chelsea
    for num in range(17 + 1):
        df_Open_space_2013_wards_without_changed_wards = df_Open_space_2013_wards_without_changed_wards.drop([356 + num])
    # Add the data of Open space 2014 wards to df_Open_space_2013_wards_without_changed_wards
    df_Open_space_2013_wards_without_changed_wards.reset_index(drop=True, inplace=True)

    # Rename the columns of df_Open_space_2014_wards and ensure the column names are the same as them in df_Open_space_2013_wards_without_changed_wards
    df_Open_space_2014_wards.columns = df_Open_space_2013_wards_without_changed_wards.columns
    # Use the dataframe_insert() defined above, to obtain the combination of df_Open_space_2013_wards_without_changed_wards and df_Open_space_2014_wards
    df_Open_space_wards = dataframe_insert(df_Open_space_2013_wards_without_changed_wards, df_Open_space_2014_wards, 570)




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
    df_Access_to_open_space_wards = dataframe_insert(df_Access_to_open_space_2013_wards_without_changed_wards, df_Access_to_open_space_2014_wards,626)
    # Use the first row as column names and remove the current column names
    df_Access_to_open_space_wards.columns = df_Access_to_open_space_wards.iloc[0]
    df_Access_to_open_space_wards = df_Access_to_open_space_wards[1:]

    prepared_csv_filepath = Path(__file__).parent.parent.joinpath("coursework1").joinpath("dataset").joinpath(
        "test3.csv")
    df_Access_to_open_space_wards.to_csv(prepared_csv_filepath, index=False)






    pd.set_option('display.max_rows', df_Access_to_open_space_2013_wards_without_changed_wards.shape[0] + 1)
    pd.set_option('display.max_columns', df_Access_to_open_space_2013_wards_without_changed_wards.shape[1] + 1)
    print(df_Access_to_open_space_2013_wards_without_changed_wards)

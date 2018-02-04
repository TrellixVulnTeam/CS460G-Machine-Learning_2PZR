import csv

# ---------------------------------------------------- Functions ---------------------------------------------------- #

# input --> synthetic csv file
# outputs an array --> index 0 = boundary for A column; index 1 = boundary for B column
def find_boundary(file_name):

    boundary1 = 0
    boundary2 = 0
    boundaries = []

    if file_name == 'synthetic-1.csv':
        boundary1 = 4.6121
        boundary2 = 2.91305
        boundaries.append(boundary1)
        boundaries.append(boundary2)
    elif file_name == 'synthetic-2.csv':
        boundary1 = 0.0878
        boundary2 = 2.61845
        boundaries.append(boundary1)
        boundaries.append(boundary2)
    elif file_name == 'synthetic-3.csv':
        boundary1 = 1.96091
        boundary2 = 0.6424
        boundaries.append(boundary1)
        boundaries.append(boundary2)
    elif file_name == 'synthetic-4.csv':
        boundary1 = 4.05485
        boundary2 = 0.6385
        boundaries.append(boundary1)
        boundaries.append(boundary2)

    return boundaries


# take original data and convert decimals to categorical data
# first column --> if below boundary, convert to x1; if above boundary, convert to x2
# second column --> below, y1; above, y2
# output new 'rows' and 'columns' lists with decimals replaced with strings
def convert_to_categorical_data(rows, columns, file_name):

    boundaries = find_boundary(file_name)

    # CONVERT ROW DATA
    for row in rows:

        # create categorical data for column A
        if float(row[0]) <= boundaries[0]:
            row[0] = 'x1'
        else:
            row[0] = 'x2'

        # create categorical data for column B
        if float(row[1]) <= boundaries[1]:
            row[1] = 'y1'
        else:
            row[1] = 'y2'

    # CONVERT COLUMN DATA
    # create categorical data for column A
    for j in range(len(columns[0])):
        if float(columns[0][j]) <= boundaries[0]:
            columns[0][j] = 'x1'
        else:
            columns[0][j] = 'x2'

    # create categorical data for column B
    for k in range(len(columns[1])):
        if float(columns[1][k]) <= boundaries[1]:
            columns[1][k] = 'y1'
        else:
            columns[1][k] = 'y2'

    return rows, columns


# ---------------------------------------------------- Main ---------------------------------------------------- #

# read in .csv file
file_name = 'synthetic-1.csv'
file = open(file_name)

# store each row of data in 'rows' list (each row is stored in an index of 'rows')
reader = csv.reader(file, delimiter=',')
rows = list(reader)

num_rows = len(rows)
num_cols = 3

# store each column of data in 'columns' list (each column is stored in an index or 'columns')
columns = []
for i in range(num_cols):
    attribute = []
    for row in rows:
        attribute.append(row[i])
    columns.append(attribute)

categorical_rows, categorical_columns = convert_to_categorical_data(rows, columns, file_name)


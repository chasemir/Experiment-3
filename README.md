# Experiment-3

## I. The Experiment 

This experiment emphasizes the ability of a programmer to work with Python's Pandas Library to load, explore, and manipulate an automobile dataset. It achieves data visualization and indexing examples in a Jupyter Notebook, providing an interactive dataset entry. This experiment is anticipated to demonstrate how Pandas can access and filter specific rows and columns. In this respect, it allows for the possible efficient dataset analysis. This leads the programmer toward inspecting data, selecting subsets, and refining data to focus on specific areas of interest. 

The programmer used Anaconda to launch the Juyter Notebook, primarily for coding, and GitHub to store and share the code.

## II. Intended Outcomes

- To determine the different codes and functions present in the Pandas Library.
- To apply the codes and functions in the Pandas Library to make a Python program.

## III. Problem 1

  ### I. Guidelines
  
    - Save the file name as Surname_Pandas-P1.py
    - Upload the given .csv file to a data frame named cars using the Pandas Library.
    - To display the first and last five rows of the resulting cars.
  
  ### II. Problem 1: Discussion 
  
     Uploading of .csv file
     - The program was started by uploading Pandas as pd
     - The given .csv file is loaded to a data frame named 'cars' using the function pd.read_csv()
       which stores the given data as a Pandas data frame. This also makes calling for the data set
       easier since 'cars' will be the new command for the .csv file, which makes filtering, indexing 
       and summarizing easier.

       The first and last five rows of the car data
       - The function .head() will view the first five rows of the data frame, which is why there is
         no need to specify the number of rows if the needed rows are equivalent to 5; however, for clarity, 
         it is better to specify the number. Any number less than or greater than five will need to be 
         specified and inputted inside the parenthesis.

       - The function .tail() has a default setting of 5 rows if not specified, so there is no need
         to input five inside the parenthesis, except for using it for a more understandable code.
         The number must be inputted inside the parenthesis if a specified amount, not 5, is needed.


### III. Guidelines

    - Save the file name as Surname_Pandas-P2.py
    - Upload the given .csv file to a data frame named cars using the Pandas Library.
    - Display the first five rows with odd-numbered columns (1,3,5,7,...) of cars
    - Display the row with the 'Model' of 'Mazda RX4'
    - Find how many cylinders or 'cyl' does the car model 'Camero Z28' have
    - Find out how many cylinders or 'cyl' and what type of gears the car models 'Mazda XR4 Wag',
      'Ford Pantera L' and 'Honda Civic' have.
    
### IV. Problem 2: Discussion 

    Uploading of .csv file
    * same with Problem 1 *
    
     - The program was started by uploading Pandas as pd
     - The given .csv file is loaded to a data frame named 'cars' using the function pd.read_csv()
       which stores the given data as a Pandas data frame. This also makes calling for the data set
       easier since 'cars' will be the new command for the .csv file, which makes filtering, indexing 
       and summarizing easier.

    Find the first five rows with odd-numbered columns (1,3,5,7,...) of cars
      - The function .iloc[] is used to select the index of the data frame by inputting the first code 
        as 0:5, the number rows 0,1,3 and 4 will be displayed. For the columns, 1:10:2 was used. The 
        last input:2 is used to skip every other column, which guarantees the odd numbers while the index
        1:10 makes sure the number of columns will be equal to 5. 

    Display the row with the 'Model' of 'Mazda RX4'
      - The model display function is .iloc[], which finds the data using the index input. 
        'Mazda RX4' is placed in the second row, which is why an index one was placed. Note that the index
        numbering always starts at 0, meaning 0 --> 1 and 1 ---> 2.

    Find how many cylinders or 'cyl' does the car model 'Camero Z28' have
      - The row and column can be specified to extract a single value using the function .iloc[].
        The row is the first digit inside the parenthesis, while the second digit will be the column.
        .iloc[23,2], Camero Z28 is in row 23, and cyl is in row 2.

    Find out how many cylinders or 'cyl' and what type of gears the car models 'Mazda XR4 Wag',
        'Ford Pantera L' and 'Honda Civic' have.
      - By creating a list with all the needed models, 'Mazda XR4 Wag',' Ford Pantera L' and 'Honda Civic'
        the coding will look cleaner and more readable. 
      - The function .loc is used to access the data using the labels where the row is first indicated
        and the column next. The .isin() function was used for the row to filter out only the specified ones.
        The columns needed were typed out one by one.
      


       
        



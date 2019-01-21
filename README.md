# Making-Table-v2
comes equipped with more functionalities, like adding rows and columns updating them, displaying columns and rows of user choice

The program comes equipped with various functions that can be used for making tables.

main_col :- is a 1d list and contains the column names.
main_row :- is a 2d list 

1. makeTable(col_info, row_info) :- This function is used for making the initial table. col_info is a 1d list where the user can pass column names and row_info is a 2d list where the user can pass row information for every columns.

     e.g. If one want to make a table having names, roll numbers and age of the student then the user have to create the two lists as :-

     col_info = ['Name', 'Roll Number', 'Age'] and
     
     row_info = [['A', 1001, 18], ['B', 1002, 18], ['C', 1003, 19]]
     
     and so to create the initial table user has to pass both the list into the function : makeTable(col_info, row_info)
     
   
2. displayTable(col_info=None, row_info=None) :- This function is used for displaying the table on to the screen. col_info and row_info parameters are used for another function to display table as user says(i.e. either all columns or few or all rows or few of them).

3. addRow(row_info, position=-1) :- This function is used for adding row into the table. position has value 1 as default that means as default the program will add the passed row at the end of the table, row_info should be in 2d. If the user want to add row at any other position then the user can pass the position(integer value).

4. addColumn(col_info, position=-1, row_info=None) :- This function is used for adding columns in the table. col_info should be in 1d and should contain the column names, position should be an integer(default value -1, adding column at the end) and should contain where the column names should be added in the table, the position can be determined by the index value from the main_col list. row_info is set to None(as default) i.e. if only the column names are passed to the function the program will create rquired columns and the row information of those columns will be set to 'NaN' when row_info is not passed and if the row_info(a 2d list) is passed the program will fill up the row information as well.

5. updateColumnName(col_info) :- This function is used for updating the column names in the table. col_info(here) is a dict which will take the new names of columns as per this format :- col_info = {<index_of_column_name / column_name> : <new_name>}
e.g. Taking the example of table we formed in first function, let's say we want to update Name to Student Name and Roll Number to Student Id so to make it happen we have to pass col_info to the required function as :-
                               col_info = {0 : 'Student Name', 1 : 'Student Id'}    (using indices)
                                                     or 
                               col_info = {'Name' : 'Student Name', 'Roll Number' : 'Student Id'}    (using column names)
                               updateColumnName(col_info)                               

6. updateRowInfo(row_info) :- This function is used for updating the row information. row_info(here) is a dict which will take the old and new information of a particular row as per this format :- 
row_info = {<index_of_row> : {<index/name_of_row[0]> : <new_info>, <index/name_of_row[1]> : <new_info>, ....}}
e.g Taking the example of table we formed in first function, let's say we want to update row1 and row3, the update will be in row1 name 'A' and age 18 will changed to 'Z' and 19 respectively and in row3 roll number 1003 and age 19 will be changed to 1004 and 18 respectively, so to make it happen we have to pass row_info to the required function as :-
                                row_info = {0 : {'A' : 'Z', 18 : 19}, 2 : {1003 : 1004, 19 : 18}} (using column names)
                                                                   or
                                row_info = {0 :{0 : 'Z', 2 : 19}, 2 : {1 : 1004, 2 : 18}}  (using indices)                                                               updateRowInfo(row_info)
                                
7. displayHeadTail(choice) :- This function will display either top 5 rows or bottom 5 rows(number of rows can be changed based on the rows present in the table, max number of rows will be 5 that will be shown). choice is a string(rather character) only two characters are valid for choice variable - 'h' and 't'.
displayHeadTail(choice='h')     will show top rows
displayHeadTail(choice='t')     will show bottom rows

8. displayColumnChoice(choice_col, num_rows=None) :- This function will display columns of user's choice. choice_col is a 1d list which will contain either column names or their indices(these will be the columns that will be displayed on to the screen) and num_rows is an integer(set to None as default) which will take number of rows user want to display to the screen.
e.g. Taking the example of the table we formed in first function, let's say we want to display only name and roll number on to the screen to do it we have to pass the parameter as :-
                                  choice_col = ['Name', 'Roll Number'] (using column names)
                                                        or
                                  choice_col = [0,1]                   (using indices)
                                  displayColumnChoice(choice_col)      (will display all rows and only name and roll number as columns)
                                  displayColumnChoice(choice_col,2)    (will display only 2 rows and name and roll number as columns)
                                                                    
9. deleteColumn(choice_col) :- This function will delete the columns(as per the user) present in the table. choice_col is a 1d list which either contains column names or their indices.
e.g. Let's say we want to delete Roll Number and Age from the table so to do so we have to pass the argument like this :-
                                             choice_col = ['Roll Number', 'Age']     (using column names)
                                                            or
                                             choice_col = [1,2]                      (using indices)
                                             deleteColumn(choice_col)                (will delete the required columns)

10. deleteRow(choice, choice_row) :-This function will delete the rows(as per the user) present in the table. choice is a string(rather character) the choice variable takes three character :- 's', 'c', 'r' and choice_row will either be an integer or a list depending on the choice variable. Let's walkthrough all the choices :-
               i) 's' :- for deleting single row, choice_row(for this choice) will be an integer, and the value of choice_row will be                            the index of the row that is to be deleted.
               ii) 'c' :- for deleting multiple and consequent row(i.e. if you want to delete rows from 3 to 7), choice_row(for this                               choice) will be a 1d list, and the list will contain starting and ending rows, i.e. if you want to delete rows 
                          from 3 to 7 choice_row will be equal to : choice_row = [2,6] (2 and 6 are the indices)
               iii) 'r' :- for deleting multiple and random rows(i.e. if you want to delete rows 3,6,7,9), choice_row(for this choice) 
                           will be a 1d list, and the list will contain all the indices of rows that are to be deleted. To delete the                              rows specified above we will pass : choice_row = [2,5,6,8] (indices are passed).
                           
To-do :- functions for searching and displaying rows as per user choice.

'''
__init__.py
----------

This Python module will help user to make a simple 
table structure just by passing row and column values 
as the parameters of defined functions.

This module comes equipped with many more functionalities, like
adding rows and columns, updating them, displaying rows and columns of 
your own choice.
'''

import helper_functions as hf

class pytables:
    '''
    Class named pytables, contains methods for making a table structure. 
    '''

    def __init__(self):
        '''
        Function to initialize pytables class objects.

        Arguments:
        self -- represents the object of the class.
        '''
        self.main_col = []          ## will contain column values
        self.main_row = []          ## will contain row values

    def make_table(self, col_info, row_info):
        '''
        Function to make a table structure based on the 
        column and row values.

        Arguments:
        self -- represents the object of the class.
        col_info -- list, containing columns names.
        row_indo -- list, containing row names.
        '''
        if type(col_info) == list and type(row_info) == list:
            ## if col_info and row_info both are in list format

            if(hf.length_do_not_match(col_info, row_info) == True):
                ## function defined in helper_functions.py
                print('Length do not match')

            else:
                ## appending all the rows and column values to their respective lists
                self.main_col = col_info
                self.main_row = row_info

        else:
            print('Parameter passed are not list')

    def display_table(self):
        '''
        Function to display a tabular structure on the screen.

        Argument:
        self -- represents the object of the class.
        '''
        
        if self.main_col == [] or self.main_row == []:
            ## if any of the list is empty
            print('Empty list found')
            return

        if hf.length_do_not_match(self.main_col, self.main_row) == True: 
            ## function defined in helper_functions.py
            print('Length do not match')
            return
        
        max_length = hf.find_max_length(self.main_col, self.main_row)
        ## function defined in helper_functions.py

        ## printing columns
        dashes, c = 0, 0
        ## dashes will store the length of dashes required to fill up the table
        ## c will be used to access the data in max_length list

        for item in self.main_col:
            dashes += len('| ' + str(item) + ' ' * (max_length[c] - len(str(item))) + ' |')
            ## computing the length of dashes

            print('| ' + str(item) + ' ' * (max_length[c] - len(str(item))) + ' |', end='')
            ## printing the column names

            c += 1
            ## incrementing c so that we can access next value of max_length list
        print()

        print('-' * dashes)
        ## printing dashes after the columns names has been displayed

        ## printing rows
        for item1 in range(0,len(self.main_row)):

            for item2 in range(0,len(self.main_col)):
                data = str(self.main_row[item1][item2])   
                ## our row data according to the index

                print('| ' + data + ' ' * (max_length[item2] - len(str(data))) + ' |', end='')
                ## printing out the row data one by one

                if(item2 == len(self.main_col) - 1):
                    print()
                    ## jump to next row as the present row has been finished

    def add_row(self, row_info, position=-1):
        '''
        Function for adding new rows to the table.

        Arguments:
        self -- represents the object of the class.

        row_info -- list, containing our new row values

        position -- int, index number defining position where the 
                    new row will be appended.
                    Default value: -1, represents row will be added
                    to the last
        '''

        if position == -1:
            ## when no position argument is passed by the user
            ## we will consider the data should be appended at last
            position = len(self.main_row)

        if type(row_info) == list and hf.length_do_not_match(self.main_col, row_info) == False:

            if(position == 0 or (position >0 and position <= len(self.main_row))):
                ## checking the position and using the position to add the row in the main_row list
                
                for item in range(len(row_info)-1,-1,-1):
                    self.main_row.insert(position, row_info[item])

            else:
                print('Indexing Problem')

        else:
            print('Either row_info is not a list or length not matching')

    def add_columns(self, col_info, position=-1, row_info=None):
        '''
        Function for adding new columns to the table.

        Arguments:
        self -- represents the object of the class.

        col_info -- list, representing the column values.

        position -- int, index number defining position where the 
                    new column will be appended.
                    Default value: -1, represents column will be added
                    to the last.

        row_info -- list, represents the row values that will be added 
                    to the new columns being made.
                    Default value: -1, repersents NaN will be filled in
                    the new columns being made
        '''

        if position == -1:
            ## when no position argument is passed by the user
            ## we will consider the data should be appended at last
            position = len(self.main_col)

        if type(col_info) == list:

            if position == 0 or (position >0 and position <= len(self.main_col)):
                ## chcking the position and using the position to add the column name in the main_col list
                for item in range(len(col_info)-1,-1,-1):
                    self.main_col.insert(position,col_info[item])

                ## appending info for new column names in main_row
                if row_info == None:
                    ## if no row_info data is passed by the user
                    for item1 in range(0,len(self.main_row)):
                        for item2 in range(0, len(col_info)):
                            self.main_row[item1].insert(position, 'NaN')

                elif type(row_info) == list:
                    ## if row_info data is passed by the user
                    for i in range(0, len(row_info)):
                        for j in range(len(col_info)-1,-1,-1):
                            try:
                                # try-except block to catch IndexError
                                self.main_row[i].insert(position, row_info[i][j])

                            except IndexError:
                                self.main_row[i].insert(position, 'NaN')

                    for j in range(i+1, len(self.main_row)):
                        for k in range(0, len(col_info)):
                            self.main_row[j].insert(position, 'NaN')

            else:
                ## if the conditions are not met
                print('Cannot add row to your table')

        else:
            print('Either col_info is not a list or length not matching')

    def updateColumnName(self, col_info):
        ## updateColumnName will update the names of the columns
        if(type(col_info) == dict):
            ## the function will only work if the col_info data-type is dict
            correct = 1
            for item in col_info:
                if(type(item) == int and (0<=item<len(self.main_col))):
                    pass
                elif((type(item) == int or type(item) == str or type(item) == float) and (item in self.main_col)):
                    pass
                else:
                    correct=0
                    break
            ## condition to check if key is passed as index or column name and checking it is present in main_col or not

            if(correct == 1):
                ## when correct value does not change
                for item in col_info:
                    if(type(item) == int and (0<=item<len(self.main_col))):
                        ## if index is given as key
                        self.main_col[item] = col_info[item]
                    else:
                        ## if column name is given as key
                        pos = self.main_col.index(item)
                        self.main_col[pos] = col_info[item]
            else:
                ## when the value changes to 0
                print('Updation cannot happen')

        else:
            ## if col_info passed is not dict type
            print('Passed parameter is not dict type')

    def updateRowInfo(self, row_info):
        ## updateRowInfo will update the row information as per row_info parameter passed by the user
        if(type(row_info) == dict):
            ## updation will only happen iff row_info is dict type
            correct = 1

            for i in row_info:
                if(0<=i<len(self.main_row)):
                    pass
                else:
                    correct=0
                    break
                for j in row_info[i]:
                    if(type(j) == int and (0<=j<len(self.main_col))):
                        pass
                    elif((type(j) == int or type(j) == str or type(j) == float) and (True in [j in k for k in self.main_row])):
                        pass
                    else:
                        correct=0
                        break

            if(correct==1):
                for i in row_info:
                        for j in row_info[i]:
                            if(type(j) == int and (0<=j<len(self.main_col))):
                                self.main_row[i][j] = row_info[i][j]
                            elif((type(j) == int or type(j) == str or type(j) == float) and (True in [j in k for k in self.main_row])):
                                pos = self.main_row[i].index(j)
                                self.main_row[i][pos] = row_info[i][j]

            else:
                ## if correct value changes
                print('Updation cannot happen')

        else:
            ## if row_info is not dict type
            print('Passed parrameter is not dict type')


    def displayHeadTail(self,choice):
        ## function to display either top rows or bottom rows
        ## two choices available - 'h' and 't' (h for head and t for tail)
        ## head refers to top columns and tails refers to bottom columns
        if(len(self.main_row) <= 3):
            limit = 1
        elif(len(self.main_row) <= 5):
            limit = 2
        elif(len(self.main_row) <= 10):
            limit = 3
        else:
            limit = 5
        ## setting limit
        ## limit is the number of rows to be displayed
        if(choice == 'h'):
            ## if user choose to see top columns
            self.displayTable(col_info=self.main_col, row_info=self.main_row[0:limit])
        elif(choice == 't'):
            ## if user choose to see bottom columns
            self.displayTable(col_info=self.main_col, row_info=self.main_row[len(self.main_row)-limit:len(self.main_row)])
        else:
            ## if neither 'h' not 't' is the choice
            print('Invalid Choice Entered')

    def displayColumnChoice(self, choice_col, num_rows=None):
        ## this function will display column of user choice
        ## and the number of rows user wish to be displayed
        if(num_rows == None):
            num_rows = len(self.main_row)
        ## if num_rows is not passed as parameter
        ## then num_rows will be equal to the length of main_row
        if(reuseIsList1d(choice_col) == True and (0<num_rows<=len(self.main_row))):
            ## when passed parameter choice_col is in 1d
            for item in choice_col:
                if(type(item) == int and (0<=item<len(self.main_col))):
                    pass
                elif((type(item) == int or type(item) == str or type(item) == float) and (item in self.main_col)):
                    pass
                else:
                    print('Parameter passed is in incorrect form')
            ## to check whether passed choice_col is in correct form or not
            col_info = []
            row_info = [[]]

            ## col_info will contain all the columns to be displayed and
            ## row_info will contain infomation for corresponding columns
            for item in range(0,len(choice_col)):
                if((type(choice_col[item]) == int or type(choice_col[item]) == str or type(choice_col[item]) == float) and (choice_col[item] in self.main_col)):
                    pos = self.main_col.index(choice_col[item])
                    choice_col[item] = pos
            ## if indices are not given, i.e. when column names are given directly the above code will append their indices to choice_col list
            for item in choice_col:
                col_info.append(self.main_col[item])
            ## appending column name to col_info list
            for i in range(0,num_rows):
                if(num_rows == i+1):
                    pass
                else:
                    row_info.append([])
                for j in range(0,len(choice_col)):
                    row_info[i].append(self.main_row[i][choice_col[j]])
            ## the above nested loop will append inforamtion to row_info list according to the columns passed by user in choice_col
            self.displayTable(col_info,row_info)
            ## displaying the required table

        else:
            ## if condition is not satisfied
            print('Cannot Display Table')

    def deleteColumn(self, choice_col):
        ## this function will delete the columns as chosen by the user
        if(reuseIsList1d(choice_col) == True):
            ## for function to run choice_col should be in 1d
            correct = 1
            ## correct is a variable set to 1
            ## if the further code changes it's value to 0 that means either column name is not correct or index passed is not valid
            for i in choice_col:
                if((type(i) is int) and (0<=i<len(self.main_col))):
                        pass
                        continue
                for j in self.main_col:
                    if(((type(i) is str) or (type(i) is int) or (type(i) is float)) and i == j):
                        choice_col[choice_col.index(i)] = self.main_col.index(j)
                        break
                else:
                    correct = 0
            ## above code will change column name to it's respective index
            ## and either column name or the index is not correctly passed the correct value changes to 0
            ## and if the value changes to 0 then deletion will not happen
            if(correct == 1):
                ## if correct value do not changes
                ## then deletion will happen
                for index in sorted(choice_col, reverse=True):
                    del self.main_col[index]

                for i in range(0,len(self.main_row)):
                    for index in sorted(choice_col, reverse=True):
                        del self.main_row[i][index]
            ## the code written inside if block will delete the chosen columns from main_col and their required information form main_row
            else:
                ## if correct value changes value to 0
                ## then deletion won't happen
                print('Either index or column name is not correct')

        else:
            ## if the choice_col list is not in 1d
            print('Passed parameter is not in 1d')

    def deleteRow(self, choice, choice_row):
        ## this function will delete row/s chosen by the user
        ## choice variable has three choices available -
        ## 's' for single row, 'c' for multiple consequent rows and 'r' for multiple random rows
        ## choice_row will either be an integer or a list depending on the choice variable

        correct = 1
        ## to check index exist or not in case of 'c' and 'r'

        if(choice == 's' and (type(choice_row) == int)):
            ## if user want to delete single row
            ## choice will be 's' and data-type of choice_row will be an integer
            if(0<=choice_row<len(self.main_row)):
                del self.main_row[choice_row]
            else:
                print('Index not valid')
        ## will delete single row from the table

        elif(choice == 'c' and (reuseIsList1d(choice_row) == True)):
            ## if user want to delete multiple consequent rows
            ## choice will be 'c' and data-type of choice_row will be 1d list
            ## choice_row = [a,b] , a is start and b is end
            for i in choice_row:
                if(0<=i<len(self.main_row)):
                    pass
                else:
                    correct = 0
            ## for loop code to see whether index exist or not
            if(correct == 1):
                choice_row.sort()
                ## if not passed in a sorted order
                for index in range(choice_row[1], choice_row[0]-1, -1):
                    del self.main_row[index]
            else:
                print('Index not valid')
        ## will delete multiple consequent rows from the table

        elif(choice == 'r' and (reuseIsList1d(choice_row) == True)):
            ## if user want to delete multiple random rows
            ## choice will be 'r' and data-type of choice_row will be 1d list
            ## choice_row = [a,b,c,..] , a,b,c... are the index number
            for i in choice_row:
                if(0<=i<len(self.main_row)):
                    pass
                else:
                    correct = 0
            ## for loop code to see whether index exist or not
            if(correct == 1):
                for index in sorted(choice_row, reverse=True):
                    del self.main_row[index]
            else:
                print('Index not Valid')

        else:
            ## when the choices entered are not correct
            print('One of the parameter is not valid')


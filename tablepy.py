## this is the python3.6 code
## Project Name :- making table v2

def reuseIsList1d(col_info):
    ## to check whether the list is in 1d or not
    ## mainly for column info list passed
    ## function will return True if the list is in 1d
    ## else it will return False
    if(isinstance(col_info, list) == True):
        return True
    else:
        return False

def reuseIsList2d(row_info):
    ## to check whether the list is in 2d or not
    ## mainly for row info list passed
    ## function will return True if the list is in 2d
    ## else it will return False
    if(isinstance(row_info, list) == True):
        return True
    else:
        return False

def reuseLengthNotMatch(col_info, row_info):
    ## function to chcek whether both the list are in their required length or not
    ## i.e. length of col_info should be equal to length of row_info[0,1,....]
    for items in row_info:
        if(len(col_info) != len(items)):
            ## return True is length do not match
            return True
    else:
        return False

def reuseFindMaxLength(col_info, row_info):
     ## findMaxLength will find out the maximum length of data available in the either of the two list(col_info, row_info)

    maxLength = []  ## maxLength will store
    jump = 0        ## for jumping over from one list to another in main_row

    for item_col in range(0,len(col_info)):
        temp = len(str(col_info[item_col]))
        for item_row in range(0,len(row_info)):
            if(len(str(row_info[item_row][jump])) > temp):
                temp =len(str(row_info[item_row][jump]))
        maxLength.append(temp)
        jump += 1

    return maxLength        ## maxLength will contain required maximum length for each columns

class makingTable:
    ## class name makingTable will contain functions to perform addition of rows and columns into a table

    def __init__(self, main_col, main_row):
        ## using init function to initilize the data-members needed in the program
        ## main_col will take all the columns of the table
        ## main_row will take all the rows of the table
        self.main_col = main_col
        self.main_row = main_row

    def displayTest(self):
        print(self.main_col)
        print(self.main_row)

    def makeTable(self,col_info, row_info):
        ## makeTable function will add specified row and columns into the table.
        if(reuseIsList1d(col_info) == True and reuseIsList2d(row_info) == True):
            ## if both the conditions are true than only table can be made
            ## col_info should be a 1d list and row_info should be a 2d list
            if(reuseLengthNotMatch(col_info, row_info) == True):
                ## if the condition is true
                print("Length do not match")
            else:
                ## if the condition is false
                ## appending all the rows and column info to their repective lists
                ## col_info will go to main_col
                ## row_info will go to main_row
                self.main_col += col_info
                self.main_row += row_info

        else:
            ## if the condition fails
            print("Dimesnion Error")

    def displayTable(self, col_info=None, row_info=None):
        ## displayTable function will display the table on the screen

        if(col_info == None and row_info == None):
            col_info = self.main_col
            row_info = self.main_row

        if(reuseLengthNotMatch(col_info, row_info) == True):
            print('Problem in your row/column data')

        else:
            maxLength = reuseFindMaxLength(col_info, row_info)   ## maxLength will store the data return by the reusefindMaxLength function

            ## printing columns
            dashes = c = 0
            ## dashes will store the length of dashes required to fill up the table
            ## c will be used to axcess the data in maxLength list

            for item in col_info:
                dashes += len('| ' + str(item) + ' ' * (maxLength[c] - len(str(item))) + ' |')
                ## computing the length of dashes
                print('| ' + str(item) + ' ' * (maxLength[c] - len(str(item))) + ' |', end='')
                ## printing the column names
                c += 1
                ## incrementing c so that we can access next value of maxLength list

            print(end='\n')

            print('-' * dashes)

            ## printing rows
            for item1 in range(0,len(row_info)):
                for item2 in range(0,len(col_info)):
                    data = str(row_info[item1][item2])   ## our row data according to the index
                    print('| ' + data + ' ' * (maxLength[item2] - len(str(data))) + ' |', end='')
                    ## printing out the row data one by one
                    if(item2 == len(col_info) - 1):
                        print(end='\n')
                        ## jump to next line as the present data line has finished

    def addRow(self, row_info, position=-1):
        ## function for adding rows to the table
        ## it will pick up the list from row_info passed by the user and will append it in main_row list
        if(position == -1):
            ## when no position argument is passed by the user
            ## we will consider the data should be appended at last
            position = len(self.main_row)

        if(reuseIsList2d(row_info) == True and reuseLengthNotMatch(self.main_col, row_info) == False):
            ## if the conditon is true
            ## condition being the row_info passed should be in 2d
            if(position == 0 or (position >0 and position <= len(self.main_row))):
                ## checking the position and using the position to add the row in the main_row list
                for item in range(len(row_info)-1,-1,-1):
                    self.main_row.insert(position, row_info[item])

            else:
                ## if the condition not met
                print('Cannot add row to your table')

        else:
            print('Either dimension problem or length not matching')

    def addColumn(self, col_info, position=-1, row_info=None):
        ## function for adding columns to the table
        ## it will pick up the list from col_info passed by the user and will append it in main_col list
        if(position == -1):
            ## when no position argument is passed by the user
            ## we will consider the data should be appended at last
            position = len(self.main_col)

        if(reuseIsList1d(col_info) == True and (row_info == None or reuseIsList2d(row_info) == True)):
            ## if the condition is true
            ## the following block will be executed
            ## condition being the col_info passed should be in 1d
            if(position == 0 or (position >0 and position <= len(self.main_col))):
                ## chcking the position and using the position to add the column name in the main_col list
                for item in range(len(col_info)-1,-1,-1):
                    self.main_col.insert(position,col_info[item])

                ## appending info of new column names in main_row
                if(row_info == None):
                    ## if no row_info data is passed by the user
                    for item1 in range(0,len(self.main_row)):
                        for item2 in range(0, len(col_info)):
                            self.main_row[item1].insert(position, 'NaN')

                else:
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
            print('Either dimension problem or length not matching')

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

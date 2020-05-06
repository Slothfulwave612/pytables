'''
helper_functions.py
-------------------

In this Python module we have defined some of the 
functions that will be used by our main module file
__init__.py. The functions defined here are used by 
our main module file to check various conditions.
'''

def length_do_not_match(col_info, row_info):
    '''
    Function to check whether both the lists are in their
    required length or not.
    i.e. length of col_info should be equal to the length of
    each element of the row_info(which basically represents our row).

    Arguments:
    col_info -- list, containing column values.
    row_info -- list, containing row values.

    Returns:
    True -- if length do not match.
    False -- otherwise
    '''
    
    for items in row_info:
        if(len(col_info) != len(items)):
            ## return True is length do not match
            return True
    else:
        return False

def find_max_length(col_info, row_info):
    '''
    Function to find out the maximum length for each columns.

    Arguments:
    col_info -- list, containing column values.
    row_info -- list, containing row values.

    Returns:
    max_length -- list, containing maximum length for each columns.
    '''

    max_length = []  ## max_length will store maximum length for each columns
    jump = 0        ## for jumping over from one list to another in main_row

    for item_col in range(0,len(col_info)):
        temp = len(str(col_info[item_col]))

        for item_row in range(0,len(row_info)):

            if len(str(row_info[item_row][jump])) > temp:
                temp =len(str(row_info[item_row][jump]))

        max_length.append(temp)
        jump += 1

    return max_length        ## max_length will contain required maximum length for each columns

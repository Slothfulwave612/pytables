from ex import pytables as pt

table_1 = pt()

columns = ['Name', 'Age', 'Gender']
rows = [['Anmol', 10, 'M'], ['Sam', 20, 'M'], ['Carol', 19, 'F'], ['Malcom', 21, 'M'], ['Oliver', 25, 'M'], ['Mellisa', 21, 'F'], ['Minreva', 18, 'F'], ['Bruce', 23, 'M'], ['Clarke', 24, 'M'], ['Zuck', 22, 'M'], ['Slade', 23, 'M'], ['Wade', 21, 'M'], ['Felicity', 22, 'F'], ['Selena', 23, 'F'], ['Ra\'s Al Gul', 200, 'M']]

table_1.make_table(columns, rows)

print()
table_1.display_table()

columns = ['Price']
row_info = [[1,2,3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
table_1.add_columns(columns, row_info=row_info)

print()
table_1.display_table()
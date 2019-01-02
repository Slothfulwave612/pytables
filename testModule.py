from tablepy import *

obj1 = makingTable([], [])

columns = ['Name', 'Age', 'Gender']
rows = [['Anmol', 10, 'M'], ['Sam', 20, 'M'], ['Carol', 19, 'F'], ['Malcom', 21, 'M'], ['Oliver', 25, 'M'], ['Mellisa', 21, 'F'], ['Minreva', 18, 'F'], ['Bruce', 23, 'M'], ['Clarke', 24, 'M'], ['Zuck', 22, 'M'], ['Slade', 23, 'M'], ['Wade', 21, 'M'], ['Felicity', 22, 'F'], ['Selena', 23, 'F'], ['Ra\'s Al Gul', 200, 'M']]

obj1.makeTable(columns, rows)

print()
obj1.displayTable()

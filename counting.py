#making sure everyone signed up for exactly two classes
import csv
count=0
too_much = []
not_enough = []
han=open('Responses.csv')
file = csv.reader(han, delimiter=';')
for row in file:
    for cell in row:
        try:
            cell= int(cell)
            if cell==1:
                count= count + cell
        except:
            continue
                
    if count == 2:
        #print (row)
        count=0
    elif count > 2:
        too_much.append(row)
        count= 0
    elif count < 2:
        not_enough.append(row)
        count= 0
for line in too_much:
    print('too many classes marked')
    print (line)
for line in not_enough:
    print('not enough classes')
    print (line)

            
            

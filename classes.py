import csv
han=open('Responses.csv')
file = csv.reader(han, delimiter=';')

#lists
amclist=[]
pmclist=[]
am_full_name=[]
pm_full_name=[]
repeated_names=[]

def amget_name(entry):
    first_name = entry[0]
    last_name = entry[1]
    name = first_name + ' ' + last_name
    am_full_name.append(name)

def pmget_name(entry):
    first_name = entry[0]
    last_name = entry[1]
    name = first_name + ' ' + last_name
    pm_full_name.append(name)

#trimming classes

classes= next(file)
for title in classes[2:7] :
    amclist.append([title])
for title in classes[7:] :
    pmclist.append([title])


#looping through file

for row in file:
    if row[2]== '81':
        continue
    if row[2]== '1':
        amclist[0].append(row)
    if row[3] == '1':
        amclist[1].append(row)
    if row[4] == '1':
        amclist[2].append(row)
    if row[5] == '1':
        amclist[3].append(row)
    if row[6] == '1':
        amclist[4].append(row)  
    if row[7] == '1':
        pmclist[0].append(row)
    if row[8] == '1':
        pmclist[1].append(row)
    if row[9] == '1':
        pmclist[2].append(row)
    if row[10] == '1':
        pmclist[3].append(row)
    if row[11] == '1':
        pmclist[4].append(row)

    #check to see if everyone is signed up for 2 classes

    check=0
    for cell in row[2:]:
        if cell != '1':
            check= check + 1
    if check > 8:
        print(row)

#creating a list of AM names and PM names to see if they signed up for multiple AM classes or PM classes. 
for sublist in amclist:
    for entry in sublist[1:]:
        amget_name(entry)
for sublist in pmclist:
    for entry in sublist[1:]:
        pmget_name(entry)
am_full_name= sorted(am_full_name)
pm_full_name=sorted(pm_full_name)

#check to see if people have signed up for multiple AM or PM classes

goob= None
boog= None

for name in am_full_name:
    if name != goob:
        goob = name
    else:
        repeated_names.append(name)
for name in pm_full_name:
    if name != boog:
        boog = name
    else:
        repeated_names.append(name)

#the names are symettric meaning the same people signed up twices(assuming they dont have the same name)



    







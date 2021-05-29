import csv #load module csv
file="Resources/budget_data.csv" 
profit=[] 
mnths=[] 
with open(file,newline='') as rf: #open the file
    read=csv.DictReader(rf)
    for rows in read: 
        mnths.append((rows["Date"])) 
        profit.append(rows["Profit/Losses"]) 
total=0 #start count from zero
for i in profit:
    total+=int(i) 
change_list=[] 
for i in profit:
    change_list.append(int(profit[0])-int(i))
average_change=sum(change_list)/len(change_list)#calculate the average change
#lists to store decrease and increase changes
decrease=[]
increase=[]
for i in change_list:#loop over the list containing changes
#check whether the change is negative or postive and load it to the respective list
    if i>0:
        increase.append(i)
    elif i<0:
        decrease.append(i)
#obtain the maximum increase change and decrease change
greatest_decrease=max(decrease)
greatest_increase=max(increase)
#print out the results
print("------------Financial Analysis--------------")
print("-------------------------------------------")
print("total month:            ",len(mnths))
print("net amount profit/loss: ",total)
print("average change:         ",average_change)
print("greatest increase:       ",greatest_increase)
print("greatest decrease:      ",greatest_decrease)
#export results in text file
dir="analysis/pybank.txt"
with open(dir,'a') as fil:
    print("\n------------Financial Analysis--------------",file=fil)
    print("\n-------------------------------------------",file=fil)
    print("\ntotal month:            ",len(mnths),file=fil)
    print("\nnet amount profit/loss: ",total,file=fil)
    print("\naverage change:         ",average_change,file=fil)
    print("\ngreatest increase:       ",greatest_increase,file=fil)
    print("\ngreatest decrease:      ",greatest_decrease,file=fil)
    
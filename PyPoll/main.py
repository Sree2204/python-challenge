import csv #load module csv
file="Resources/election_data.csv"
candidates=[] 
votes=[]
with open(file,newline='') as fi: #opening the files
    read=csv.DictReader(fi)
    for row in read: #loop over the dictionaries
        candidates.append(row["Candidate"])
        votes.append(row["Voter ID"]) 
total=len(votes)
uniq=set(candidates)#get the names of candidates wothout repetition
names=[] 
for name in uniq: #loop over the unque names
    names.append(name) 
#list to store each candidates votes
fst_cand_votes=[]
sknd_cand_votes=[]
thd_cand_votes=[]
fth_cand_votes=[]
#loop over the candidates and store names that matches each candidate in a separate list
for cand in candidates:
    if cand==names[0]:
        fst_cand_votes.append(cand)
    elif cand==names[1]:
        sknd_cand_votes.append(cand)
    elif cand==names[2]:
        thd_cand_votes.append(cand)
    elif cand==names[3]:
        fth_cand_votes.append(cand)
#get the number of votes for each candidate
fst_total=len(fst_cand_votes)
sknd_total=len(sknd_cand_votes)
thd_total=len(thd_cand_votes)
fth_total=len(fth_cand_votes)
#get candidate with highest votes
total_list=[fst_total,sknd_total,thd_total,fth_total]
#get the index of the candidate with highest votes
index=total_list.index(max(total_list))
winner=names[index]
#calculate the percentage votes for each candidate
fst_per=(len(fst_cand_votes)/len(candidates))*100
sknd_per=(len(sknd_cand_votes)/len(candidates))*100
thd_per=(len(thd_cand_votes)/len(candidates))*100
fth_per=(len(fth_cand_votes)/len(candidates))*100
#print out the results
print("---------------------------------------")
print("-------Election Results----------------")
print("Total Votes: ",total)
print("---------------------------------------")
print("Name         votes%             total votes")
print(names[0]," :",fst_per,"% ",(fst_total))
print(names[1]," :",sknd_per,"% ",(sknd_total))
print(names[2]," :",thd_per,"% ",(thd_total))
print(names[3]," :",fth_per,"% ",(fth_total))
print("-------------------------------------------")
print("the winner is: ",winner)
#export the output in a text file.
dir="analysis/pyroll.txt"
with open(dir,'a') as exp:
    print("\n---------------------------------------",file=exp)
    print("\n-------Election Results----------------",file=exp)
    print("\nTotal Votes: ",total,file=exp)
    print("\n---------------------------------------",file=exp)
    print("\nName         votes%             total votes",file=exp)
    print("\n",names[0]," :",fst_per,"% ",(fst_total),file=exp)
    print("\n",names[1]," :",sknd_per,"% ",(sknd_total),file=exp)
    print("\n",names[2]," :",thd_per,"% ",(thd_total),file=exp)
    print("\n",names[3]," :",fth_per,"% ",(fth_total),file=exp)
    print("\n-------------------------------------------",file=exp)
    print("\nthe winner is: ",winner,file=exp)
    


    

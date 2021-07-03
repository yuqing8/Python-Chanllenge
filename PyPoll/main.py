import os
import csv

csvpath=os.path.join("Resources","election_data.csv")
summary={}

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    for row in csvreader:    
        if row[2] in summary:
            summary[row[2]]+=1
        else:
            summary[row[2]]=1
        vote_counts={k:summary[k] for k in summary}

        percentage_list=[]
        name_list=[]
        total_value=0
        for value in summary.values():
            total_value+=value
        for value in summary.values():
            percentage_list.append(round((value/total_value)*100))
        for key in summary.keys():
            name_list.append(key)
        summary_percentage=dict(zip(name_list,percentage_list))
        vote_percentage={k:summary_percentage[k] for k in summary_percentage}
        combined_votes=[(vote_counts[k],vote_percentage[k],k) for k in vote_counts]
        combined_votes_sorted=sorted(combined_votes,reverse=True)

lines_text=[]
title="Election Results"
divider="---------------------"
title_total_votes=(f'Total Votes: {total_value}')
winner=(f'winner:{combined_votes_sorted[0][2]}')

lines_text.append(title)
print(title)
lines_text.append(divider)
print(divider)
lines_text.append(title_total_votes)
print(title_total_votes)
lines_text.append(divider)

print(divider)
 
for sub_tuple in combined_votes_sorted:
    print(f'{sub_tuple[2]}:{sub_tuple[1]}% ({sub_tuple[0]})')
    lines_text.append((f'{sub_tuple[2]}:{sub_tuple[1]}% ({sub_tuple[0]})'))

lines_text.append(divider)
print(divider)
lines_text.append(winner)
print(winner)
lines_text.append(divider)
print(divider)

textpath=os.path.join("PyPoll_result.txt")
with open('PyPoll_result.text','w') as f:
    for line in lines_text:
        f.write(line)
        f.write('\n')
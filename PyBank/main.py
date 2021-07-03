import os
import csv

month=[]
profit_and_loss=[]
profit_and_loss_diff=[]
total_pl=0
total_diff=0
lines_text=[]
title="Financial Analysis \n---------------------------------"
csvpath=os.path.join("Resources","PyBank.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        month.append(row[0])
        profit_and_loss.append(row[1])
    "print(len(month))"
    

    for i in range((len(profit_and_loss))-1):
        diff=int(profit_and_loss[i+1])-int(profit_and_loss[i])
        profit_and_loss_diff.append(diff)
    #unsupported operand type(s) for -: 'str' and 'str'"

    for i in range(len(profit_and_loss_diff)):
        total_diff+=int(profit_and_loss_diff[i])
        'print(total_diff/(len(profit_and_loss_diff)))'
    
    for i in range(len(profit_and_loss)):
        total_pl+=int(profit_and_loss[i])
        'print(total_pl)'

month.pop(0)
average_change=round((total_diff/(len(profit_and_loss_diff))),2)
pl_diff_dict=dict(zip(month,profit_and_loss_diff))
sorted_pl_diff=sorted([(pl_diff_dict[k],k)for k in pl_diff_dict],reverse=True)
i=len(sorted_pl_diff)-1
great_increase=(f"Greatest Increase in Profits:{sorted_pl_diff[0][1]} (${sorted_pl_diff[0][0]})")
great_decrease=(f"Greatest Decrease in Profits:{sorted_pl_diff[i][1]} (${sorted_pl_diff[i][0]})")

print(title)
lines_text.append(title)
print(f'Total Months : {len(month)}')
lines_text.append(f'Total Months : {len(month)}')
print(f'Average Change : ${average_change}')
lines_text.append(f'Average Change : ${average_change}')
print(great_increase)
lines_text.append(great_increase)
print(great_decrease)
lines_text.append(great_decrease)

textpath=os.path.join("PyBank_result.txt")
with open('PyBank.text','w') as f:
    for line in lines_text:
        f.write(line)
        f.write('\n')
        
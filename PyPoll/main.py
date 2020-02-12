import os
import csv 




# f = open(r'C:\My-Repo\python-challenge\python-challenge\PyPoll\election_data.csv')
# csv = csv.reader(f)
csvpath = os.path.join("election_data.csv")


with open(csvpath, newline="") as csvfile:
    csv = csv.reader(csvfile, delimiter=',')


header = next(csv)
votes = 0
candidate = set()
vote4khan = 0
vote4correy = 0
vote4li = 0
vote4tooley = 0

for vote in csv:
    votes += 1

    candidate.add(vote[2])

    if (vote[2] == "Khan"):
        vote4khan += 1
    elif (vote[2] == "Correy"):
        vote4correy += 1
    elif (vote[2] == "Li"):
        vote4li += 1
    else:
        vote4tooley += 1

per_won_khan = (vote4khan / votes)
per_won_correy = vote4correy / votes
per_won_li = vote4li / votes
per_won_tooley = vote4tooley / votes
Candidates = ["Khan", "Correy", "Li", "O'Tooley"]
Total_votes = [vote4khan, vote4correy, vote4li, vote4tooley]
vote_dict = dict(zip(Candidates, Total_votes))
key = max(vote_dict, key=vote_dict.get)


print("     Election Results")
print("--------------------------")
print(f' Total Votes: {str(votes)}')
print("--------------------------")
print(" Khan: " + "{:.3%}".format(per_won_khan) + " " + (str(vote4khan)))
print(" Correy: " + "{:.3%}".format(per_won_correy) + " " + (str(vote4correy)))
print(" Li: " + "{:.3%}".format(per_won_li) + " " + (str(vote4li)))
print(" O'Tooley: " + "{:.3%}".format(per_won_tooley) + " " + (str(vote4tooley)))
print("--------------------------")
print(" Winner: " + key)
print("--------------------------")


# Specify the file and location to write to

output_path = os.path.join(r'C:\My-Repo\python-challenge\python-challenge\PyPoll\Election-Results.txt')
with open(output_path,"w") as file:

 
    file.write("     Election Results")
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    file.write(f"Total Votes: {votes}")
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    file.write(" Khan: " + "{:.3%}".format(per_won_khan) + " " + (str(vote4khan)))
    file.write("\n")
    file.write(" Correy: " + "{:.3%}".format(per_won_correy) + " " + (str(vote4correy)))
    file.write("\n")
    file.write(" Li: " + "{:.3%}".format(per_won_li) + " " + (str(vote4li)))
    file.write("\n")
    file.write(" O'Tooley: " + "{:.3%}".format(per_won_tooley) + " " + (str(vote4tooley)))
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write("--------------------------")
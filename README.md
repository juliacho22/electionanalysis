# electionanalysis

## Project Overview 
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidates won. 
5. Determine the winner of the election based on popular vote. 

## Resources 
- Data Srouce: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary 
The analysis of the election show that: 
-  There were 639,711 votes cast in the election. 
-  The candidates were
    - Charles Casper Stockham 
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were: 
    - Charles Casper Stockham  received 23.0% of the votes and 85,213 number of votes. 
    - Diana DeGette received 73.8% of the votes and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
- The winner of the election was 
    - Diana DeGette, who received 73.8% of the votes and 272,892 number of votes.

## Challenge Overview 
This project analyzes the election turnout and results for a Colorado election between three counties: Jefferson County, Denver Couty and Arapahoe County.
[PyPoll_Challenge.py](https://github.com/juliacho22/electionanalysis/blob/main/PyPoll_Challenge.py). 

## Challenge Summary 
## Election Audit Results
### County Turnout 
Out of the three counties, Denver County had the largest turnout of 306,055 votes, which is 82.8% of the voter population. Jefferson County and Arapahoe County brought in 38,855 (10.5%) and 24,801 (6.7%) voters turn out.\ 
![VoterTurnout](https://github.com/juliacho22/electionanalysis/blob/main/Resources/VoterTurnout.PNG)

### Candidate Results  
- Charles Casper Stockham received 85,213 of the votes, which made up 23.0% of the total
- Diana DeGette received 272,892 of the votes, which made up 73.8% of the total
- Raymon Anthony Doane received 11,606 of the votes, which made up 3.1%  of the total
Therefore, Diana DeGette is the winning candidate in this election.\
![ElectionResult](https://github.com/juliacho22/electionanalysis/blob/main/Resources/ElectionResult.PNG)

### Election Audit Summary 
This script could potentially be used for any election with small edits. One of the changes that would need to change is the path to the file. Every time the scripot is used, the path would need to be update to reference the correct results. Additionally, a county reference would not always work; some elections would need to focus on different parameters such as citie or states. 

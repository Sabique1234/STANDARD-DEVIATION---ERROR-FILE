import random
import statistics
import plotly.express as px
import plotly.figure_factory as ff


diceResult = []

for i in range (0,1000):
   dice1 = random.randint(1,6)
   dice2 = random.randint(1,6)
   diceResult.append(dice1+dice2)

mean = sum(diceResult)/len(diceResult)
std_deviation = statistics.stdev(diceResult)

median = statistics.median(diceResult)
mode = statistics.mode(diceResult)

fig = ff.create_distplot([diceResult],["result"],show_hist=False)

#fig.show()

#DEVIATION : CHECKING HOW THE NUMBERS ARE SPREADING, METHOD TO CHECK THE VARIATIONS IN A GIVEN DATA

#1st DEVIATION
first_std_deviation_start, first_standard_deviation_end = mean - std_deviation, mean + std_deviation
#2nd DEVIATION
second_std_deviation_start, second_standard_deviation_end = mean - (2*std_deviation), mean + (2*std_deviation)
list_of_data_within_1_std_deviation = [result for result in diceResult if result > first_std_deviation_start and result < first_standard_deviation_end]

print("{}% of data lies within 1 standard deviation",format(len(first_std_deviation_start)*100.0/len(diceResult)))

import csv
import pandas as pd 
import statistics 
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go 

df=pd.read_csv('data.csv')
data=df['reading_time'].tolist()

data1=statistics.stdev(data)
print (data1)

population_mean=statistics.mean(data)
print(population_mean)


def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean 

mean_list=[]
for i in range(0,1000):
     set_of_means=random_set_of_mean(100)
     mean_list.append(set_of_means)

mean1=statistics.mean(mean_list)
print(mean1)

stdev1=statistics.stdev(mean_list)
print(stdev1)

fig=ff.create_distplot([mean_list], ['reading_time'],show_curve=True)
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,40],mode='lines',name='mean'))
fig.show()
#calculate mean of the population data

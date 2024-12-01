from statistics import pstdev,pvariance
from math import sqrt

#function for getting variance
def population_variance(population):
    """Calculating population variance"""
    mean=sum(population)/len(population)
    sub_mean=0
    mean_of_squared=0
    for i in population:
        sub_mean+=(i-mean)**2
        mean_of_squared=sub_mean/len(population)
    return mean_of_squared

pop=[1,3,4,2,6,5,3,4,5,2]
print(population_variance(pop))

"""Using python inbuilt modules to calculate variance and dispersion"""
#Getting variance with inbuilt
print(pvariance(pop))

#Calculating standard deviation from our function
stddev=sqrt(population_variance(pop))
print(stddev)


#Getting Standard deviation with the inbuilt
print(pstdev(pop))


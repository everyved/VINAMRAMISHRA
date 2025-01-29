# A. Compare the temperature and humidity requirements of the following pair of crops using 2 sample t-test
# 1.Rice and jute
# 2.Banana and grapes
#
# Declare the Null and alternate hypothesis and write the inferences.
#
# B. Test the Ph requirement of Mango crop and write the inference if the PH is same as 7.5(ph. of the population) Use 1 sample t-test.
import pandas as pd
from scipy.stats import ttest_ind
import scipy.stats as stats

file_path='Crop.csv'
data=pd.read_csv(file_path)
# print(data.head())
# label=data['label'].unique()
# print('\n',label)
print(data.columns)

print('A.a1')
#A(1.a)--> null_hypo--> the temprature requirments of rice and jute are the same
#A(1.a)--> alt_hypo--> temprature requirments of rice and jute are different 
rice=data[data['label']=='rice']['temperature']
jute=data[data['label']=='jute']['temperature']
# print(rice)
# print(jute)

t_stat, p_value = ttest_ind(rice, jute)
print('temp: rice and jute (t_stat):', t_stat,'\nthe p_value is: ',p_value)
alpha = 0.05 

if p_value < alpha:
    print("we reject the null hypothesis: The temprature requirments for rice and jute are different")
else:
    print("we fail to reject the null hypothesis: The temprature requirments for rice and jute are the same")

print('A.b2')
#A(1.b)--> null_hypo--> the humidity requirments of rice and jute are the same
#A(1.b)--> alt_hypo--> the humidity requirments of rice and jute are different 
rice=data[data['label']=='rice']['humidity']
jute=data[data['label']=='jute']['humidity']
# print(rice)
# print(jute)

t_stat, p_value = ttest_ind(rice, jute)
print('humidity: rice and jute(t_stat)', t_stat,'\nthe p_value is: ',p_value)
alpha = 0.05 

if p_value < alpha:
    print("we reject the null hypothesis: The humidity requirments for rice and jute are different")
else:
    print("we fail to reject the null hypothesis: The humidity requirments for rice and jute are the same")

print('A.a2')
#A(2.a)--> null_hypo--> the temprature requirments of Banana and grapes are the same
#A(2.a)--> alt_hypo--> temprature requirments of Banana and grapes are different 
grapes=data[data['label']=='banana']['temperature']
banana=data[data['label']=='grapes']['temperature']
# print(banana)
# print(grapes)

t_stat, p_value = ttest_ind(banana, grapes)
print('temp: rice and jute (t_stat):', t_stat,'\nthe p_value is: ',p_value)
alpha = 0.05 

if p_value < alpha:
    print("we reject the null hypothesis: The temprature requirments for banana and grapes are different")
else:
    print("we fail to reject the null hypothesis: The temprature requirments for banana and grapes are the same")

print('A.b2')
#A(2.b)--> null_hypo--> the humidity requirments of banana and grapes are the same
#A(2.b)--> alt_hypo--> the humidity requirments of banana and grapes are different 
grapes=data[data['label']=='grapes']['humidity']
banana=data[data['label']=='banana']['humidity']
# print(grapes)
# print(banana)

t_stat, p_value = ttest_ind(grapes, banana)
print('humidity: rice and jute(t_stat)', t_stat,'\nthe p_value is: ',p_value)
alpha = 0.05 

if p_value < alpha:
    print("we reject the null hypothesis: The humidity requirments for banana and grapes are different")
else:
    print("we fail to reject the null hypothesis: The humidity requirments for banana and grapes are the same")


print('B:')
#B-->null hypotheses--> the ph requirment for mango crop is 7.5
#B-->alt_hypo-->the the ph requirment for mango crop is not equal to 7.5
mango=data[data['label']=='mango']['ph']
population_mean=7.5
t_stat, p_value = ttest_ind(mango, population_mean)
print('(t_stat) for mango:', t_stat,'\nthe p_value is: ',p_value)
if p_value < alpha:
    print("We reject the null hypo: the ph requirment for mango crop is different from 7.5")
else:
    print("we fail to reject the null hypothesis: the temprature requirment for mango crop is 7.5")
    

#ANOVA
# Creating three sample lists (groups)
group1 = [23, 21, 25, 22, 20, 24, 26]
group2 = [30, 28, 32, 31, 29, 27, 33]
group3 = [40, 42, 39, 41, 43, 44, 38]

# Performing one-way ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)

# Displaying results
print("ANOVA Results:")
print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Checking significance level (α = 0.05)
if p_value < 0.05:
    print("Result: Significant difference between the groups.")
else:
    print("Result: No significant difference between the groups.")

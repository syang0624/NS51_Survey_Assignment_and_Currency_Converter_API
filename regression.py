import pandas as pd #used to get summary statistics
import numpy as np #used to calculate specific stats like median and standard deviation
from scipy import stats #used to calculate p-value
import matplotlib.pyplot as plt #used to create histograms
import statsmodels.api as statsmodels #used to calculate and analyze regression
import seaborn as sns #this was recommended as a good package for visualizing data
sns.set_style("whitegrid")
sns.set(color_codes=True, font_scale = 1.2)
sns.set_style("whitegrid")

plt.rcParams.update({'font.size':14})

#question list:
#How many reusable bags do you own?
#I store my plastic bags and reuse them on a daily basis.
#When I go shopping, I make sure I bring my own reusable bags instead of using plastic bags.
#I think plastic bags are harmful to the environment.
#I want to use reusable bags more often.
#I do my own research on how to use less plastic bags.
#My income is enough for me to purchase reusable bags.


#individual income and response average:
cebu_income = [18000,0,17000,20000,30000,17000,25000,17000,18000,18000,18000,0,
              16000,18000,20000,8000,18000,5600,15000,30000,22000,6000,15000,20000,25000,
              30000,15000,23000,23000,0,5000,15000,15000,13500,0]
cebu_reusable = [4.333333333,4.166666667,4.666666667,3.666666667,4.666666667,5,5,4.166666667,4.333333333,4,3.5,
                4.333333333,4.833333333,4.666666667,3.833333333,3.833333333,4,4.666666667,4.5,4.666666667,3.166666667,
                3.666666667,4.166666667,3.833333333,4.333333333,4.333333333,5,3.333333333,5,4.166666667,4,4.5,4.666666667,5,5]
seoul_income = [0,500000,0,2500000,0,550000,0,12000000,1000000,400000,0,0,400000,0,1000000,80000000,350000,1500000]
seoul_reusable = [4,3.833333333,3.5,4.333333333,3.833333333,3,4.166666667,4.333333333,3.666666667,3.5,3.833333333,
                 3.333333333,3.666666667,4.166666667,3.833333333,3.666666667,3.666666667,3.833333333]
ub_income = [0,0,0,1000000,500000,0,1100000,1100000,400000,1400000,0,500000,400000,1200000,300000,
            2000000,0,0,1200000,1200000,8000000,1500000,1200000,1000000,0,1200000]
ub_reusable = [4.833333333,3.166666667,3.666666667,4.666666667,3.5,2.666666667,4.666666667,3.666666667,3.333333333,3.666666667,
              4.166666667,4.333333333,5,4,4.166666667,3.666666667,4.5,3.166666667,4.833333333,4.166666667,4,3.833333333,
              3.833333333,4.666666667,4.333333333,3.833333333]

# plotting a histogram for the living areas by stting the range and number of bins
#because the data are such that the automatic Python histogram is not the best for visualizing the data
range_hist=(0,5)
bins = 50
#plotting the data on top of each other and making the bars transparent for better assessment
plt.hist(cebu_reusable,bins, range_hist,alpha=0.7, label="Cebu (Philippines)")
plt.hist(seoul_reusable, bins, range_hist,alpha=0.7, label ="Seoul (South Korea)")
plt.hist(ub_reusable, bins, range_hist,alpha=0.7, label ="Ulaanbaatar(Mongolia)")


# x-axis label
plt.xlabel('Figure 2. The aggregggate distribution of opinions and pratices on using reusable bags.')
# frequency label
plt.ylabel('Frequencies (absolute)')
# plot title
#plotting a histogram for the years built, no needs to specify parameters here
plt.legend()
plt.show()


# THIS CODE WAS TAKEN DIRECTLY FROM CLASS TEMPLATES and REVISED BY STEVEN YANG '24

def regression_model(x, y):
   # this function uses built in library functions to create a scatter plot,
   # plots of the residuals, compute R-squared, and display the regression eqn

   # create the regression line:
   X = statsmodels.add_constant(x)  # this makes the intercept accurate, not 0
   Y = y
   regressionmodel = statsmodels.OLS(Y, X).fit()

   # extract regression parameters from model, rounded to 3 decimal places:
   Rsquared = round(regressionmodel.rsquared, 3)
   slope = round(regressionmodel.params[1], 3)
   intercept = round(regressionmodel.params[0], 3)

   # make plots:
   fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, figsize=(12, 4))
   ax1.set(xlabel='Income in PHP', ylabel='Response Level')
   ax1.set_title('R-squared: ' + str(Rsquared))
   sns.regplot(x, y, marker="+", ax=ax1)  # scatter plot

   # QQ plot:
   qqplot = statsmodels.qqplot(regressionmodel.resid, fit=True, line='45')
   qqplot.suptitle("Normal Probability (\"QQ\") Plot for Residuals", fontweight='bold', fontsize=14)

   # print the results:
   print("R-squared = ", Rsquared)
   print("Regression equation: ", "Response Average", "=", slope, "*", "Income in PHP", "+", intercept)

regression_model(cebu_income, cebu_reusable)

def regression_model2(x,y):
   # this function uses built in library functions to create a scatter plot,
   # plots of the residuals, compute R-squared, and display the regression eqn

   # create the regression line:
   X = statsmodels.add_constant(x) #this makes the intercept accurate, not 0
   Y = y
   regressionmodel = statsmodels.OLS(Y,X).fit()

   # extract regression parameters from model, rounded to 3 decimal places:
   Rsquared = round(regressionmodel.rsquared,3)
   slope = round(regressionmodel.params[1],3)
   intercept = round(regressionmodel.params[0],3)

   # make plots:
   fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, figsize=(12,4))
   ax1.set(xlabel='Income in KRW', ylabel='Response Level')
   ax1.set_title('R-squared: ' + str(Rsquared))
   sns.regplot(x, y, marker="+", ax=ax1) # scatter plot

   # QQ plot:
   qqplot = statsmodels.qqplot(regressionmodel.resid,fit=True,line='45')
   qqplot.suptitle("Normal Probability (\"QQ\") Plot for Residuals",fontweight='bold',fontsize=14)

   # print the results:
   print("R-squared = ",Rsquared)
   print("Regression equation: ", "Response Average", "=",slope,"*","Income in KRW","+",intercept)

regression_model2(seoul_income,seoul_reusable)

def regression_model3(x,y):
   # this function uses built in library functions to create a scatter plot,
   # plots of the residuals, compute R-squared, and display the regression eqn

   # create the regression line:
   X = statsmodels.add_constant(x) #this makes the intercept accurate, not 0
   Y = y
   regressionmodel = statsmodels.OLS(Y,X).fit()

   # extract regression parameters from model, rounded to 3 decimal places:
   Rsquared = round(regressionmodel.rsquared,3)
   slope = round(regressionmodel.params[1],3)
   intercept = round(regressionmodel.params[0],3)

   # make plots:
   fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, figsize=(12,4))
   ax1.set(xlabel='Income in MNT', ylabel='Response Level')
   ax1.set_title('R-squared: ' + str(Rsquared))
   sns.regplot(x, y, marker="+", ax=ax1) # scatter plot

   # residual plot:
   residualplot = sns.residplot(x=regressionmodel.predict(), y=regressionmodel.resid, color='green')
   residualplot.set(xlabel='Fitted values for ', ylabel='Residuals')
   residualplot.set_title('Residuals vs Fitted values',fontweight='bold',fontsize=14)

   # print the results:
   print("R-squared = ",Rsquared)
   print("Regression equation: ", "Response Average", "=",slope,"*","Income in MNT","+",intercept)

regression_model3(ub_income,ub_reusable)

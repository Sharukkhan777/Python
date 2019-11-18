# NORMALITY TEST

# MEAN AND SD
# HISTOGRAM
# QQ PLOT
# SHAPIRO TEST

# calculating mean and sd
# generate gaussian data
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# summarize
print('mean=%.3f stdv=%.3f' % (mean(data), std(data)))

# Visual Normality Checks
# histogram plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# histogram plot
pyplot.hist(data,bins=100)
pyplot.show()



# QQ Plot
from numpy.random import seed
from numpy.random import randn
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
# q-q plot
qqplot(data, line='s')
pyplot.show()

#``````````````````````````````````````````````````````````````````````````````

### Statistical Normality Tests
# Shapiro-Wilk Test
from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro
# seed the random number generator
seed(1)
# generate univariate observations
data = 5 * randn(100) + 50
#---------------------------------------------
# normality test
stat, p = shapiro(data)
# Example 
#
# >>> stats.shapiro(x)
# (0.9772805571556091, 0.08144091814756393)
#
# so we can put like stat,p so that it assign 
# first value for stat
# second value for p
#---------------------------------------------
print('the test statistic=%.3f, p-value=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')
    


















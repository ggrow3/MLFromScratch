def mean(values):
    return sum(values) / float(len(values))

#define variance
def variance(values, mean):
    return sum([(x-mean)**2 for x in values])

dataset = [[1,1],[2,3],[4,3],[3,2],[5,5]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
mean_x, mean_y = mean(x), mean(y)

x = [row[0] for row in dataset]
y = [row[1] for row in dataset]

mean_x, mean_y = mean(x), mean(y)
var_x,var_y = variance(x,mean_x),variance(y, mean_y)
print('x stats: mean=%.3f variance=%.3f' % (mean_x, var_x))
print('y stats: mean=%.3f variance=%.3f' % (mean_y, var_y))

#what exaclty is covariance
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)


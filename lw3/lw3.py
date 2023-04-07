import math

beta2 = 1.7

alpha1 = math.sin(0.18)
beta1 = pow(math.e, alpha1)
alpha2 = math.log(0.05) + beta2

d = (alpha1 * beta1) - (alpha2 * beta2)
n = alpha1 - pow(alpha2, 2)

result = d / n

print(result)

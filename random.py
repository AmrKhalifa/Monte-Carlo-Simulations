import numpy as np
from scipy.stats import truncnorm
import matplotlib.pyplot as plt

scale = 3.
range = 10
size = 100000

X = truncnorm(a=-range/scale, b=+range/scale, scale=scale).rvs(size=size)
X = X.round().astype(int)
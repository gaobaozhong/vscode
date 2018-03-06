#coding:utf

import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(6,4))

print data[data[3]>1]


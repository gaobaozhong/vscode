import pandas as pd
ages = [20,22,25,27,21,23,37,31,61,35,41,32]
bins = [18,25,35,60,100]
cats = pd.cut(ages,bins)
print cats
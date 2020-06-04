import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
from progress.bar import Bar

f = open("q", "r")
df = pd.DataFrame(columns=["num", "ms"])
bar = Bar('Processing', max=38)

x = 0
for s in f:
    df.loc[x] = [x] + [float(s)]
    x += 1
    if(x > 38):
        break
    bar.next()
bar.finish()

plt.plot(df['num'], df['ms'])
plt.show()

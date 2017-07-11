from pandas import DataFrame,Series
import numpy as np
frame = DataFrame(np.arange(8).reshape((2,4)), index=['three','one'],columns=['d','a','b','c'])
s = frame[frame["d"]==0]
ids = s.loc[s.last_valid_index(), "c"]
print(ids)

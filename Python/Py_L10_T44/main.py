import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(random.sample(['robot', 'human']*10, 10))
data.head()

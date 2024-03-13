import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
#новый словарь для замены значений
mapping = {'robot': 0, 'human': 1}
#использование oneHot
data['one_hot'] = data['whoAmI'].map(mapping)

print(data.head())

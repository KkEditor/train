import pandas as pd
num=pd.read_csv("labels.csv")['num']
label=pd.read_csv("labels.csv")['label']
print(num)
print(label)
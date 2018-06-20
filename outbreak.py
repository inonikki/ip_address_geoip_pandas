import pandas as pd
import datetime as dt


#data_frame = pd.read_csv('modified_table.csv', encoding="ISO-8859-1")
#data_frame_inonikki = data_frame[['last_ip', 'code', 'country', 'region', 'city', 'lastlogin']]
#data_frame_inonikki.to_csv('modified_table_inonikki.csv')
#data_frame_inonikki = pd.read_csv('modified_table_inonikki.csv')

#data_frame_inonikki_sort = data_frame_inonikki.sort_values(by=['country', 'city'], ascending=[True, False])

dataset_all = pd.read_csv('modified_table_inonikki.csv', encoding="ISO-8859-1", index_col=['lastlogin'], parse_dates=['lastlogin'], dayfirst=True)
data_frame_inonikki_sort_all = dataset_all.sort_values(by=['country', 'city'], ascending=[True, False])
print(data_frame_inonikki_sort_all)

dataset_2017 = dataset_all[dataset_all.index >= '2017-01-01 00:00:00']
data_frame_inonikki_sort_2017 = dataset_2017.sort_values(by=['country', 'city'], ascending=[True, False])
print(data_frame_inonikki_sort_2017)
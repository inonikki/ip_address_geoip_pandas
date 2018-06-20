import pandas as pd

from function import get_code, get_country, get_region, get_city

df_source = pd.read_csv('ip.csv')
df_ended = df_source

df_ended['code'] = df_ended['last_ip'].apply(get_code)
df_ended['country'] = df_ended['last_ip'].apply(get_country)
df_ended['region'] = df_ended['last_ip'].apply(get_region)
df_ended['city'] = df_ended['last_ip'].apply(get_city)

df_ended.to_csv('modified_table.csv')

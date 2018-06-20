import geoip2.database

reader = geoip2.database.Reader('bd.mmdb')
response = reader.city('128.101.101.101')

print(response.country.iso_code)
print(response.country.name)
print(response.subdivisions.most_specific.name)
print(response.city.name)

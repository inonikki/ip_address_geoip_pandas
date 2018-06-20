import geoip2.database
import pandas as pd
from geoip2.errors import AddressNotFoundError


def get_code(ip):
    try:
        reader = geoip2.database.Reader('bd.mmdb')
        response = reader.city(ip)
        code = response.country.iso_code
        reader.close()
        return code
    except ValueError:
        return pd.np.nan
    except AddressNotFoundError:
        return pd.np.nan


def get_country(ip):
    try:
        reader = geoip2.database.Reader('bd.mmdb')
        response = reader.city(ip)
        country = response.country.name
        reader.close()
        return country
    except ValueError:
        return pd.np.nan
    except AddressNotFoundError:
        return pd.np.nan


def get_region(ip):
    try:
        reader = geoip2.database.Reader('bd.mmdb')
        response = reader.city(ip)
        region = response.subdivisions.most_specific.name
        reader.close()
        return region
    except ValueError:
        return pd.np.nan
    except AddressNotFoundError:
        return pd.np.nan


def get_city(ip):
    try:
        reader = geoip2.database.Reader('bd.mmdb')
        response = reader.city(ip)
        city = response.city.name
        reader.close()
        return city
    except ValueError:
        return pd.np.nan
    except AddressNotFoundError:
        return pd.np.nan

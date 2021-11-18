import time
import random
import pycountry

import pandas as pd

from geopy.geocoders import Nominatim

df = pd.DataFrame()

# Add your user agent here (e.g: your_email@your_server.your_domain)
geolocator = Nominatim(user_agent='')

df_dict = {
    'country_name': [],
    'country_alpha_2': [],
    'country_alpha_3': [],
    'country_lat': [],
    'country_lon': []
}

for country in pycountry.countries:

    print(f'{country.name}: {country.alpha_2}')

    df_dict['country_name'].append(country.name)
    df_dict['country_alpha_2'].append(country.alpha_2)
    df_dict['country_alpha_3'].append(country.alpha_3)

    time.sleep(random.randrange(1, 10))

    loc = geolocator.geocode(country.alpha_2, timeout=10)

    df_dict['country_lat'].append(loc.latitude) if loc is not None else df_dict['country_lat'].append(None)
    df_dict['country_lon'].append(loc.longitude) if loc is not None else df_dict['country_lon'].append(None)


df = pd.DataFrame.from_dict(df_dict)
df.to_csv('./data/countries.csv', index=False)
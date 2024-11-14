from geopy.geocoders import Nominatim


regions = ['Fiji region',
           'Rat Islands, Aleutian Islands, Alaska',
           'West Chile Rise',
           'Easter Island region',
           'western Xizang',
           'Kermadec Islands, New Zealand',
           'northern Mid-Atlantic Ridge',
           'Kuril Islands',
           'Kermadec Islands region',
           'Pagan region, Northern Mariana Islands',
           'Arctic Ocean',
           'Maug Islands region, Northern Mariana Islands',
           'Prince Edward Islands region',
           'South Sandwich Islands region',
           'Volcano Islands, Japan region',
           'Galapagos Triple Junction region',
           'Revilla Gigedo Islands region',
           'central East Pacific Rise',
           'Kepulauan Babar, Indonesia',
           'Izu Islands, Japan region',
           'southeast Indian Ridge',
           'Banda Sea',
           'North Indian Ocean',
           'Mariana Islands region',
           'Pacific-Antarctic Ridge',
           'Balleny Islands region',
           'Southwest Indian Ridge',
           'Carlsberg Ridge',
           'Bonin Islands, Japan region',
           'Greenland Sea',
           'southern East Pacific Rise',
           'Tristan da Cunha region',
           'South Indian Ocean',
           'southern Mid-Atlantic Ridge',
           'Mid-Indian Ridge',
           'central Mid-Atlantic Ridge',
           'Chagos Archipelago region',
           'South Atlantic Ocean']

geolocator = Nominatim(user_agent="earthquake_finder_nathan")
for i, region in enumerate(regions):
    location = geolocator.geocode(region)
    if location:
        print(i, "Before: ", region, "After: ", location.address)
    else:
        print(i, region)

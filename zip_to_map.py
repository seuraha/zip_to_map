import pgeocode
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

def zipcode_to_map(
        zipcode_array,
        us_map=True,
        lat_bounds=10,
        lon_bounds=10):
    """
    Plot the locations of zipcodes on a map.

    Parameters:
    - zipcode_array (list): List of zipcodes to plot.
    - us_map (bool): Whether to plot the whole US map.
    - lat_bounds (int): Latitude bounds for the map.
    - lon_bounds (int): Longitude bounds for the map.
    """
    zipcode_df = pd.DataFrame({'zipcode': zipcode_array})
    nomi = pgeocode.Nominatim('us')

    def get_coordinates(zipcode):
        location = nomi.query_postal_code(zipcode)
        return (location.latitude, location.longitude) if not pd.isnull(location.latitude) else (None, None)

    zipcode_df['coordinates'] = zipcode_df['zipcode'].apply(get_coordinates)
    zipcode_df[['latitude', 'longitude']] = pd.DataFrame(zipcode_df['coordinates'].tolist(), index=zipcode_df.index)

    if us_map:
        llcrnrlat=24; urcrnrlat=50; llcrnrlon=-125; urcrnrlon=-66;
    else:
        assert lat_bounds is not None and lon_bounds is not None, "lat_bounds and lon_bounds not provided."
        llcrnrlat=zipcode_df['latitude'].min() - lat_bounds
        urcrnrlat=zipcode_df['latitude'].max() + lat_bounds
        llcrnrlon=zipcode_df['longitude'].min() - lon_bounds
        urcrnrlon=zipcode_df['longitude'].max() + lon_bounds

    fig, ax = plt.subplots(figsize=(10, 6))
    m = Basemap(
        projection='merc', 
        llcrnrlat=llcrnrlat,
        urcrnrlat=urcrnrlat, 
        llcrnrlon=llcrnrlon,
        urcrnrlon=urcrnrlon, 
        resolution='i',
        ax=ax)
    m.drawcoastlines()
    m.drawstates()

    x, y = m(zipcode_df['longitude'].values, zipcode_df['latitude'].values)
    m.scatter(x, y, marker='o', color='blue', zorder=5, facecolors='none')

    plt.title("Zipcode Locations")
    plt.show()

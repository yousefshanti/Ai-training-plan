# %%
import pandas as pd
import geopandas as gpd
from geodatasets import get_path

# %%
path_to_data = get_path("nybb")
gdf = gpd.read_file(path_to_data)
gdf

# %%
print(type(gdf))
print(gdf.geometry.name)
print(gdf.crs)

# %%
gdf.to_file("my_file.geojson", driver="GeoJSON")

# %%
gdf = gdf.set_index("BoroName")
gdf["area"] = gdf.area
gdf["boundary"] = gdf.boundary
gdf["centroid"] = gdf.centroid
gdf[["area", "boundary", "centroid"]]

# %%
first_point = gdf["centroid"].iloc[0]
gdf["distance"] = gdf["centroid"].distance(first_point)
print(gdf["distance"])
print(gdf["distance"].mean())

# %%
gdf.plot("area", legend=True)

# %%
m = gdf.explore("area", legend=False)
m.save("boroughs_map.html")

# %%
gdf = gdf.set_geometry("centroid")
gdf.plot("area", legend=True)

# %%
gdf = gdf.set_geometry("geometry")
ax = gdf["geometry"].plot()
gdf["centroid"].plot(ax=ax, color="black")

# %%
gdf["convex_hull"] = gdf.convex_hull
ax = gdf["convex_hull"].plot(alpha=0.5)
gdf["boundary"].plot(ax=ax, color="white", linewidth=0.5)

# %%
gdf["buffered"] = gdf.buffer(10000)
gdf["buffered_centroid"] = gdf["centroid"].buffer(10000)
ax = gdf["buffered"].plot(alpha=0.5)
gdf["buffered_centroid"].plot(ax=ax, color="red", alpha=0.5)
gdf["boundary"].plot(ax=ax, color="white", linewidth=0.5)

# %%
brooklyn = gdf.loc["Brooklyn", "geometry"]
print(type(brooklyn))
print(gdf["buffered"].intersects(brooklyn))

# %%
gdf["within"] = gdf["buffered_centroid"].within(gdf)
print(gdf["within"])

# %%
gdf = gdf.set_geometry("buffered_centroid")
ax = gdf.plot("within", legend=True, categorical=True, legend_kwds={"loc": "upper left"})
gdf["boundary"].plot(ax=ax, color="black", linewidth=0.5)
gdf = gdf.set_geometry("geometry")

# %%
print(gdf.crs)
boroughs_4326 = gdf.to_crs("EPSG:4326")
print(boroughs_4326.crs)
boroughs_4326.plot()

# %%
print(gdf.area.sum())
print(boroughs_4326.area.sum())

# %%
boroughs = gdf[["geometry"]].reset_index()

df_places = pd.DataFrame({
    "name": ["Times Square", "Brooklyn Bridge Park", "JFK Airport", "Yankee Stadium", "St. George Ferry"],
    "lon": [-73.9855, -73.9969, -73.7781, -73.9262, -74.0736],
    "lat": [40.7580, 40.7003, 40.6413, 40.8296, 40.6437],
})

points = gpd.GeoDataFrame(
    df_places,
    geometry=gpd.points_from_xy(df_places["lon"], df_places["lat"]),
    crs="EPSG:4326",
).to_crs(boroughs.crs)

points

# %%
joined = gpd.sjoin(points, boroughs, predicate="within")
joined[["name", "BoroName"]]

# %%
joined.groupby("BoroName").size()

# %%
ax = boroughs.plot(color="lightgrey", edgecolor="white")
points.plot(ax=ax, color="red")

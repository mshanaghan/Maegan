# Coding Challenge 5
# For this coding challenge, I want you to practice the heatmap generation that we went through in class,
# but this time obtain your own input data, and I want you to generate heatmaps for TWO species.
# You can obtain species data from a vast array of different sources, for example:
# obis - Note: You should delete many columns (keep species name, lat/lon) as OBIS adds some really long strings
# that don't fit the Shapefile specification.
# GBIF
# Maybe something on RI GIS
# Or just Google species distribution data
# My requirements are:
# The two input species data must be in a SINGLE CSV file, you must process the input data to separate out the species
# (Hint: You can a slightly edited version of our CSV code from a previous session to do this),
# I recommend downloading the species data from the same source so the columns match.
# Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer,
# and you provide the species data along with your Python code.
# The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
# You leave no trace of execution, except the resulting heatmap files.
# You provide print statements that explain what the code is doing, e.g. Fishnet file generated.

# "combined_csv.csv" contains location data for 2 fish species
import arcpy
arcpy.env.overwriteOutput = True
# Set workspace
arcpy.env.workspace = r"E:\ShanaghanPythonGIS\Class_Files\Class06"
# # Set spatial reference of output
spRef = arcpy.SpatialReference(4326)
# Convert .csv to a shapefile
in_Table = r"combined_csv.csv"
x_coords = "decimallongitude"
y_coords = "decimallatitude"
z_coords = ""
out_Layer = "fish_locations"
saved_Layer = r"fish_locations_output.shp"
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
arcpy.CopyFeatures_management(lyr, saved_Layer)
if arcpy.Exists(saved_Layer):
     print("Created file successfully!")

# Use select to extract data for hippoglossus stenolepis only
arcpy.env.workspace = r"E:\ShanaghanPythonGIS\Class_Files\Class06"
in_features = "fish_locations_output.shp"
out_feature_class = r"E:\ShanaghanPythonGIS\Class_Files\Class06\Hipposten.shp"
where_clause = '"scientific" = \'Hippoglossus stenolepis\''
arcpy.Select_analysis(in_features, out_feature_class, where_clause)
if arcpy.Exists(out_feature_class):
     print("Created subset successfully!")
# Use select to extract data for Morone saxatilis only
arcpy.env.workspace = r"E:\ShanaghanPythonGIS\Class_Files\Class06"
in_features = "fish_locations_output.shp"
out_feature_class = r"E:\ShanaghanPythonGIS\Class_Files\Class06\Moronesax.shp"
where_clause = '"scientific" = \'Morone saxatilis\''
arcpy.Select_analysis(in_features, out_feature_class, where_clause)
if arcpy.Exists(out_feature_class):
     print("Created subset two successfully!")

# # Extract the Extent, i.e. XMin, XMax, YMin, YMax of Hipposten.shp.
desc = arcpy.Describe("Hipposten.shp")
XMin1 = desc.extent.XMin
XMax1 = desc.extent.XMax
YMin1 = desc.extent.YMin
YMax1 = desc.extent.YMax
print(float(XMin1))
print(float(XMax1))
print(float(YMin1))
print(float(YMax1))

# # Extract the Extent, i.e. XMin, XMax, YMin, YMax of Moronesax.shp.
desc = arcpy.Describe("Moronesax.shp")
XMin2 = desc.extent.XMin
XMax2 = desc.extent.XMax
YMin2 = desc.extent.YMin
YMax2 = desc.extent.YMax
print(float(XMin2))
print(float(XMax2))
print(float(YMin2))
print(float(YMax2))

# Generate Fishnet for Hipposten.shp
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
# Name output fishnet
outFeatureClass = "Hipposten_fishnet.shp"
# Set the origin of the fishnet
originCoordinate = str(XMin1) + " " + str(YMin1)
yAxisCoordinate = str(XMin1) + " " + str(YMin1 + 1)
cellSizeWidth = "0.5"
cellSizeHeight = "0.5"
numRows = ""
numColumns = ""
oppositeCorner = str(XMax1) + " " + str(YMax1)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"
arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)
if arcpy.Exists(outFeatureClass):
    print("Created Fishnet file 1 successfully!")

# Generate Fishnet for Moronesax.shp
# set environment
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
# Name output fishnet
outFeatureClass = "Moronesax_fishnet.shp"
# Set the origin of the fishnet
originCoordinate = str(XMin2) + " " + str(YMin2)
yAxisCoordinate = str(XMin2) + " " + str(YMin2 + 1)
cellSizeWidth = "0.5"
cellSizeHeight = "0.5"
numRows = ""
numColumns = ""
oppositeCorner = str(XMax2) + " " + str(YMax2)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"
arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)
if arcpy.Exists(outFeatureClass):
    print("Created Fishnet file 2 successfully!")

# # 4. Undertake a Spatial Join to join the Hipposten fishnet to the observed points.
target_features = "Hipposten_fishnet.shp"
join_features = "Hipposten.shp"
out_feature_class = "Hipposten_HeatMap.shp"
join_operation = "JOIN_ONE_TO_ONE"
join_type = "KEEP_ALL"
field_mapping = ""
match_option = "INTERSECT"
search_radius = ""
distance_field_name = ""
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)
if arcpy.Exists(out_feature_class):
    print("Created Heatmap 1 successfully!")

# # 4. Undertake a Spatial Join to join the Moronesax fishnet to the observed points.
target_features = "Moronesax_fishnet.shp"
join_features = "Moronesax.shp"
out_feature_class = "Moronesax_HeatMap.shp"
join_operation = "JOIN_ONE_TO_ONE"
join_type = "KEEP_ALL"
field_mapping = ""
match_option = "INTERSECT"
search_radius = ""
distance_field_name = ""
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)
if arcpy.Exists(out_feature_class):
    print("Created Heatmap 2 successfully!")




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
import os
import csv
arcpy.env.overwriteOutput = True
# Set workspace
arcpy.env.workspace = "E:\ShanaghanPythonGIS\Class_Files\Class06\Challenge_05"
input_directory = "E:\ShanaghanPythonGIS\Class_Files\Class06\Challenge_05"
# # Set spatial reference of output
spRef = arcpy.SpatialReference(4326)
# Convert .csv to a shapefile which contains both species
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

# Use csv to extract a list of unique species. Call it species_list
species_list = []
with open("combined_csv.csv") as species_csv:
    next(species_csv) #skip first line
    for row in csv.reader(species_csv):
        if row[2] not in species_list:
            species_list.append(row[2])
print(len(species_list))

# Use select by attribute tool to extract each species from "fish_locations_output.shp"
for species in species_list:
     query = "scientific = " + "'" + str(species) + "'"
     print(query)
     selection = arcpy.management.SelectLayerByAttribute("fish_locations_output.shp", "NEW_SELECTION", query)
     arcpy.CopyFeatures_management(selection, "Species" + str(species) + ".shp")
# # # Extract the Extent, i.e. XMin, XMax, YMin, YMax
     desc = arcpy.Describe("Species" + str(species) + ".shp")
     XMin = desc.extent.XMin
     XMax = desc.extent.XMax
     YMin = desc.extent.YMin
     YMax = desc.extent.YMax
# # # Generate fishnet using extent details
     spRef = arcpy.SpatialReference(4326)
     outFeatureClass = "Species_fishnet_" + str(species) + ".shp"
     originCoordinate = str(XMin) + " " + str(YMin)
     yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
     cellSizeWidth = "0.5"
     cellSizeHeight = "0.5"
     numRows = ""
     numColumns = ""
     oppositeCorner = str(XMax) + " " + str(YMax)
     labels = "NO_LABELS"
     templateExtent = "#"
     geometryType = "POLYGON"
     arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                                     cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                     oppositeCorner, labels, templateExtent, geometryType)
     if arcpy.Exists(outFeatureClass):
         print("Created Fishnet file successfully for" + str(species))
# Use spatial join to create heat maps
     target_features = "Species_fishnet_" + str(species) + ".shp"
     join_features = "Species" + str(species) + ".shp"
     out_feature_class = "Species_heatmap_" + str(species) + ".shp"
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
         print("Created Heatmap file successfully for" + str(species))







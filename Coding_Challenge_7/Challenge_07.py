# Our coding challenge this week should make use of temporary folders,
# output folders and file management.
# Convert your Coding Challenge 5 exercise to work with temporary folders, os.path.join and glob.glob.
# Do not take too much time on this and if you do not have a working Challenge 5, talk to the instructor.

import glob
import os
# "combined_csv.csv" contains location data for 2 fish species
import arcpy
import csv
import glob

####
# User changable
####

arcpy.env.overwriteOutput = True
# Set workspace
input_directory = "C:\Data\Students_2022\Shanaghan\Coding_Challenge_7"
arcpy.env.workspace = input_directory

# Create temporary and output file folder using os.path.join
if not os.path.exists(os.path.join(input_directory, "temporary_files")):
    os.mkdir(os.path.join(input_directory, "temporary_files"))
if not os.path.exists(os.path.join(input_directory, "output_files")):
    os.mkdir(os.path.join(input_directory, "output_files"))

species_file_list = glob.glob("*.csv") # I am assuming only the one csv file here.

temporary_files = os.path.join(input_directory, "temporary_files")
# # Set spatial reference of output
spRef = arcpy.SpatialReference(4326)
# Convert .csv to a shapefile which contains both species

in_Table = os.path.join(input_directory, species_file_list[0])
x_coords = "decimallongitude"
y_coords = "decimallatitude"
z_coords = ""
out_Layer = "fish_locations"
saved_Layer = os.path.join(input_directory, "temporary_files", r"fish_locations_output.shp")
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
arcpy.CopyFeatures_management(lyr, saved_Layer)
if arcpy.Exists(saved_Layer):
     print("Created file successfully!")

# Use csv to extract a list of unique species. Call it species_list
species_list = []
with open(os.path.join(input_directory, species_file_list[0])) as species_csv:
    next(species_csv) #skip first line
    for row in csv.reader(species_csv):
        if row[2] not in species_list:
            species_list.append(row[2])
print(len(species_list))

# Use select by attribute tool to extract each species from "fish_locations_output.shp"

for species in species_list:
     query = "scientific = " + "'" + str(species) + "'"
     print(query)
     selection = arcpy.management.SelectLayerByAttribute(saved_Layer, "NEW_SELECTION", query)
     arcpy.CopyFeatures_management(selection, os.path.join(input_directory, "temporary_files", "Species" + str(species) + ".shp"))

# # # Extract the Extent, i.e. XMin, XMax, YMin, YMax
     desc = arcpy.Describe(os.path.join(input_directory, "temporary_files", "Species" + str(species) + ".shp"))
     XMin = desc.extent.XMin
     XMax = desc.extent.XMax
     YMin = desc.extent.YMin
     YMax = desc.extent.YMax
# # # Generate fishnet using extent details

     spRef = arcpy.SpatialReference(4326)
     outFeatureClass = os.path.join(input_directory, "temporary_files", "Species_fishnet_" + str(species) + ".shp")
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

     target_features = os.path.join(input_directory, "temporary_files", "Species_fishnet_" + str(species) + ".shp")
     join_features = os.path.join(input_directory, "temporary_files", "Species" + str(species) + ".shp")
     out_feature_class = os.path.join(input_directory, "output_files", "Species_heatmap_" + str(species) + ".shp")
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


# Our coding challenge this week follows from the last exercise that we did
# in class during Week 8 where we worked with functions.
# Convert some of your earlier code into a function.
# The only rules are:
# 1) You must do more than one thing to your input to the function, and
# 2) the function must take two arguments or more.
# 3) provide a zip file of example data within your repo.
# Plan the task to take an hour or two, so use one of the simpler examples from our past classes.

# Converting challenge 4 into a function
# import packages
import arcpy, os
# allow overwrite
arcpy.env.overwriteOutput = True
# define function - all geoprocessing code within function
def towns_LC(towns_file, nlcd_file):
    # define directory
    directory = "E:\ShanaghanPythonGIS\Class_Files\Class09"
    in_features = os.path.join(directory, r"Municipalities__1997_.shp")
    out_feature_class = os.path.join(directory, r"SK_Selected.shp")
    where_clause = '"NAME" = \'SOUTH KINGSTOWN\''
    # execute select
    arcpy.Select_analysis(in_features, out_feature_class, where_clause)
    print("Selected town from..." + towns_file)
    from arcpy.sa import ExtractByMask
    inRaster = os.path.join(directory, r"NLCD_2016.img")
    inMaskData = os.path.join(directory, r"SK_Selected.shp")
    outExtractByMask = ExtractByMask(inRaster, inMaskData)
    outExtractByMask.save(os.path.join(directory, r"NLCD_SK.img"))
    print("Clipped" + " " + nlcd_file + " " "to selected town.")
towns_LC("E:\ShanaghanPythonGIS\Class_Files\Class09\Municipalities__1997_.shp", r"E:\ShanaghanPythonGIS\Class_Files\Class09\NLCD_2016.img")

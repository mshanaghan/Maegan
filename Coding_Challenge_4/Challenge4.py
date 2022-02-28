# Coding Challenge 4
# I will use 2 data sets for this challenge:
# RI municipalities 1997 and NLCD 2016
# I will clip the NLCD to the town of South Kingstown
import arcpy
# First, select the town of SK from the municipalities data set
# Set local variables
# in_features = r"E:\ShanaghanPythonGIS\Class_Files\Class04\Municipalities__1997_.shp"
# out_feature_class = r"E:\ShanaghanPythonGIS\Class_Files\Class04\SK_Selected2.shp"
# where_clause = '"NAME" = \'SOUTH KINGSTOWN\''
# Weird syntax! Do not like
# # Execute Select
# arcpy.Select_analysis(in_features, out_feature_class, where_clause)
#
# # Now use extract by mask tool to clip the NLCD to the town of SK
from arcpy import env
from arcpy.sa import ExtractByMask

# # Set local variables
inRaster = r"E:\ShanaghanPythonGIS\Class_Files\Class04\NLCD_2016.img"
inMaskData = r"E:\ShanaghanPythonGIS\Class_Files\Class04\SK_Selected2.shp"
# Execute extract by mask
outExtractByMask = ExtractByMask(inRaster, inMaskData)
# Save the output
outExtractByMask.save(r"E:\ShanaghanPythonGIS\Class_Files\Class04\NLCD_SK2.img")
# Success!
# I had to make the output file .img - would not work as .shp
# Outputs have a 2 after them because I did it wrong the first time, and it wouldn't let me overwrite the (incorrect) existing files.







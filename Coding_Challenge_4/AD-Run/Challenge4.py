# Coding Challenge 4
# I will use 2 data sets for this challenge:
# RI municipalities 1997 and NLCD 2016
# I will clip the NLCD to the town of South Kingstown
import arcpy, os
# # First, select the town of SK from the municipalities data set
# # Set local variables
directory = "C:\Data\Students_2022\Shanaghan\Coding_Challenge_4\AD-Run\Challenge_4_Data"

in_features = os.path.join(directory, r"Municipalities__1997_.shp")
out_feature_class = os.path.join(directory, r"SK_Selected3.shp")
where_clause = '"NAME" = \'SOUTH KINGSTOWN\''
# Weird syntax! Do not like
# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)

# # Now use extract by mask tool to clip the NLCD to the town of SK

#
# # # Set local variables
inRaster = r"C:\Data\Students_2022\Shanaghan\Coding_Challenge_4\AD-Run\Challenge_4_Data\NLCD_2016.img"
inMaskData = r"C:\Data\Students_2022\Shanaghan\Coding_Challenge_4\AD-Run\Challenge_4_Data\SK_Selected3.shp"
# Execute extract by mask
outExtractByMask = arcpy.sa.ExtractByMask(inRaster, inMaskData)
# Save the output
outExtractByMask.save(r"C:\Data\Students_2022\Shanaghan\Coding_Challenge_4\AD-Run\Challenge_4_Data\NLCD_SK3.img")
# Success!
# I had to make the output file .img - would not work as .shp
# Outputs have a 3 after them because I did it wrong the first 2 times,
# and it wouldn't let me overwrite the (incorrect) existing files.







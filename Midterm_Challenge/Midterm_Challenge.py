# Midterm Tool Challenge (due Friday 19th March 17.30pm)
# In this assignment, you are instructed to produce a small script tool that takes advantage
# of arcpy and Python. You will need to provide example data, and the code should run on all
# PC's. The tool needs to manipulate a dataset across three different processes, for example,' \
# 'extracting, modifying and exporting data. The exact workflow is entirely up to yourself.' \
# ' You are expected to take 3-4 hours on this coding assignment, and you should deposit your ' \
#   'code and example files within a Github repository for feedback and grading.

# My coding challenge consists of the following tasks:
# Select the town of South Kingstown from RI municipalities dataset,
# Clip land cover dataset to town of South Kingstown,
# Select residential areas from clipped land cover dataset
# Buffer residential areas by 500 meters.

# Import modules
import arcpy
arcpy.env.overwriteOutput = True
# Set workspace
arcpy.env.workspace = "C:\ShanaghanNRS528\Midterm_Challenge"
# Set local variables
in_features = "Municipalities__1997_.shp"
out_feature_class = "C:\ShanaghanNRS528\Midterm_Challenge\SK_selected.shp"
where_clause = '"NAME" = \'SOUTH KINGSTOWN\''
# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)

# Clip land cover to South Kingstown
# Set local variables
in_features = "Land_Use_and_Land_Cover_(2011).shp"
clip_features = "SK_selected.shp"
out_feature_class = "C:\ShanaghanNRS528\Midterm_Challenge\SK_landcover.shp"
# Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

# Select residential land cover from land cover dataset
# Set local variables
in_features = "SK_landcover.shp"
out_feature_class = "C:\ShanaghanNRS528\Midterm_Challenge\SK_residential.shp"
where_clause = '"Descr_2011" = \'High Density Residential (<1/8 acre lots)\''
# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)

# Buffer residential land cover by 500 yards
in_features = "C:\ShanaghanNRS528\Midterm_Challenge\SK_residential.shp"
out_feature_class = "C:\ShanaghanNRS528\Midterm_Challenge\SK_residential_buffer.shp"
buffer_distance_or_field = "500 yards"
line_side = "#"
line_end_type = "#"
dissolve_option = "#"
dissolve_field = "#"
method = "#"
arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)
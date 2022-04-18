# Our coding challenge this week follows from the last exercise that we did in class
# during Week 6 and improve our practice with rasters from Week 10.

# Task 1 - Use what you have learned to process the Landsat files provided,
# this time, you know you are interested in the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir)
# from the Landsat 8 imagery, see here for more info about the bands:
# https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites.

# Data provided are monthly (a couple are missing due to cloud coverage)
# during the year 2015 for the State of RI, and stored in the file Landsat_data_lfs.zip.

# Before you start, here is a suggested workflow:
# Extract the Landsat_data_lfs.zip file into a known location.
# For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index.
# Consider using the Raster Calculator Tool in ArcMap and using "Copy as Python Snippet" for the first calculation.

# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided.
# As part of your code submission, you should also provide a visualization document (e.g. an ArcMap layout in PDF format),
# showing the patterns for an area of RI that you find interesting.

# Import mods
import arcpy, os
arcpy.env.overwriteOutput = True

# Using code from week 6, composite the bands for the 6 months in the dataset
listMonths = ["02", "04", "05", "07", "10", "11"]
outputDirectory = "E:\ShanaghanPythonGIS\Class_Files\Class11\Challenge_10\Landsat_data\Composites"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)
# Use a for loop to run through the list of months and composite bands for each month
for month in listMonths:
    arcpy.env.workspace = "E:\ShanaghanPythonGIS\Class_Files\Class11\Challenge_10\Landsat_data\LS_2015_" + month
    listRasters = arcpy.ListRasters("*", "TIF")
    print("For month: " + month + ", there are: " + str(len(listRasters)) + " bands to process.")
    listRasters = [x for x in listRasters if "_BQA.tif" not in x]
    print("Compositing Bands for " + month)
    arcpy.CompositeBands_management(in_rasters=listRasters, out_raster=os.path.join(outputDirectory, "2015" + month + ".tif"))
    print("Compositing Bands for " + month + " finished.")




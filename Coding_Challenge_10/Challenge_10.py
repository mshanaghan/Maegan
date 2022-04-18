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
import arcpy
arcpy.env.overwriteOutput = True

# Make list of months
listMonths = ["02", "04", "05", "07", "10", "11"]
# Use a for loop to run through the list of months and pull out B4 and B5
for month in listMonths:
    arcpy.env.workspace = "E:\ShanaghanPythonGIS\Class_Files\Class11\Challenge_10\Landsat_data\LS_2015_" + month
    listRasters_B4 = arcpy.ListRasters("*_B4.tif", "TIF")
    listRasters_B5 = arcpy.ListRasters("*_B5.tif", "TIF")
    # Print to check if pulled correct items
    print(listRasters_B4)
    print(listRasters_B5)
    # Make rasters out of the pulled items
    vis = arcpy.Raster(listRasters_B4)
    nir = arcpy.Raster(listRasters_B5)
    # Do the calculation
    ndvi = (nir - vis) / (nir + vis)
    # Save the calculation results as .tif files located in each month's folder
    ndvi.save("NDVI_" + month + ".tif")





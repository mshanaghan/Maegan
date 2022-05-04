# In this coding challenge, your objective is to utilize the arcpy.da module to undertake some basic partitioning of your dataset.
# In this coding challenge, I want you to work with the Forest Health Works dataset from RI GIS (I have provided this as a downloadable ZIP file in this repository).
# Using the arcpy.da module (yes, there are other ways and better tools to do this),
# I want you to extract all sites that have a photo of the invasive species (Field: PHOTO) into a new Shapefile,
# and do some basic counts of the dataset. In summary, please addressing the following:
# Count how many individual records have photos, and how many do not (2 numbers), print the results.
# Count how many unique species there are in the dataset, print the result.
# Generate two shapefiles, one with photos and the other without.

# import modules
import arcpy, os
arcpy.env.overwriteOutput = True
# Set input, fields, and expression
outfolder = r'C:\ShanaghanNRS528\NRS_528_Coding_Challenges\Challenge_09'
input_shp = os.path.join(outfolder, r'\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp')

fields = ['id', 'photo']
expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " = 'y'"
# print expression
print("Executing UpdateCursor using Expression: " + expression)
# Set count
count = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        print(u'{0}, {1}'.format(row[0], row[1]))
        count = count + 1
    print("There are" +" "+ str(count) +" "+ "records with pictures.")
# Generate new shapefile called yes_pic_shp with only records that have pics
    arcpy.Select_analysis(in_features=input_shp,
                          out_feature_class=os.path.join(outfolder, 'yes_pics_shp'.format(row[0])),
                          where_clause=expression)
# Records without pics
expression_2 = arcpy.AddFieldDelimiters(input_shp, "photo") + " <> 'y'"
# print expression_2
print("Executing UpdateCursor using Expression: " + expression_2)
# Set count_2
count_2 = 0
with arcpy.da.SearchCursor(input_shp, fields, expression_2) as cursor:
    for row in cursor:
        print(u'{0}, {1}'.format(row[0], row[1]))
        count_2 = count_2 + 1
    print("There are" +" "+ str(count) +" "+ "records without pictures.")
# Generate new shapefile called no_pics_shp with only records that don't have pics
    arcpy.Select_analysis(in_features=input_shp,
                          out_feature_class=os.path.join(outfolder, 'no_pics_shp'.format(row[0])),
                          where_clause=expression_2)

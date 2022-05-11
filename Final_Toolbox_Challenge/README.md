**Final Toolbox Challenge!**

My toolbox is located within the "Final_Toolbox.zip" file in this repository. It is called "Final_Toolbox.pyt" and it consists of three tools: Buffer, Select, and Clip. Example data is located in the folder called "Final_Challenge_Data". All example data was downloaded from RIGIS.org. 

**Buffer**

Parameters 

| Parameter | Data Type | Direction | Required? |
|-----------|-----------|-----------|-----------|
| Input Features | Shapefile | Input | Yes |
| Output Feature Class | Feature Class | Output | Yes|
| Distance | Linear Unit | Input | Yes |

Parameters for the Buffer tool include input features, output features, and buffer distance. You can add a buffer of any distance and unit to the input dataset. I provided "Historic_Sites.shp" for this operation. Add a 100 m buffer to this dataset. 

Parameters for the Select tool include input features, output feature class, and expression. The expression parameter requires a python SQL expression as the input. I provided "Municipalities_1997_.shp" for this operation. Write an expression to select the town of North Kingstown from this dataset.  

Parameters for the Clip tool include input features, clip features, and output feature class. Input features are the features you want to clip. Clip features are the features used to clip the input dataset. Clip "RIDOT_Roads_2016_.shp" to "Town_of_NK.shp" to only see roads within the town of North Kingstown.

Thank you for a great semester!

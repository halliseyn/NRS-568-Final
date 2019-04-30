# NRS-568-Final
**Final project for NRS 568 ArcGIS_Python (URI)**

Author: Noah Hallisey, 4/30/2019

All tools released under MIT licesnse, and no warranty is implied

This ArcGIS 10.x toolbox takes point data and clips it to a geographic boundary, identifies intersection of point data to a shapefile, and then calculates the density of the points to create a raster surface. Intended uses of this toolbox could include identifying coastal structures at riok of binge inundated from sea level rise or storm events using a polygon sufrace for predicted sea level rise or storm surge. 

Included is sample data for the town of Charlestown, RI. Datasets include coastal structres, the town polygon, and 7 ft sea level rise inundation shapefile. 

The tools include in the toolbox are:
* Clip Tool
  * Clips feature to the boundary of another feature.
* Intersect Tool
  * Calculates intersection of two features.
* Point Density Tool 
  * Calculates density of points and creates a raster surface with density around each cell.


**Data Sources**
* RIGIS(http://www.rigis.org/)

# NRS-568-Final
**Final project for NRS 568 ArcGIS_Python (URI)**

Author: Noah Hallisey, 4/30/2019

All tools released under MIT license, and no warranty is implied.

This ArcGIS 10.x toolbox takes point data and clips it to a geographic boundary, identifies intersection of point data to a shapefile, and then calculates the density of the points to create a raster surface. Intended uses of this toolbox could include identifying coastal structures at risk of being inundated from sea level rise (SLR) or storm events using a polygon sufrace for predicted sea level rise or storm surge. 

Included is sample data for the town of Charlestown, Rhode Island. 
Datasets include:
* Coastal structures (E911 Sites)
* Charlestown boundry
* 7 ft SLR

 Tools included in the toolbox:
* Clip: 
  * Clips feature to the boundary of another feature.
* Intersect: 
  * Calculates intersection of two features.
* Point Density: 
  * Calculates density of points and creates a raster surface with density around each cell.


**Data Sources**
* RIGIS(http://www.rigis.org/)

import arcpy

# The code below is designed to clip points to a boundary, identify where points intersect a polygon (Sea level rise predictions), and calculate the point denity.


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "ToolBoxFinal"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool1, Tool2, Tool3]


# Clipping Tool
class Tool1(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clipping tool"
        self.description = "Clips feature to the boundary of another feature"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        # Input points
        # Do not chage
        input_point = arcpy.Parameter(name="input_point",
                                      displayName="Input Point",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",  # Required|Optional|Derived
                                      direction="Input",  # Input|Output
                                      )
        params.append(input_point)
        # Input polygon
        #Do not change
        input_polygon = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_polygon)
        # Output feature
        #Do not change
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_point = parameters[0].valueAsText
        input_polygon = parameters[1].valueAsText
        output = parameters[2].valueAsText
        # Clipping Tool
        # Do not change
        arcpy.Clip_analysis(input_point, input_polygon, output)

        return


# Intersect Tool
class Tool2(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Intersect Tool"
        self.description = "Identifies intersect of two features"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        # Input feature
        # Do not change
        input_feature = arcpy.Parameter(name="input_feature",
                                        displayName="Input feature",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_feature)
        # Input polygon
        # Do not change
        input_polygon = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_polygon)
        # Output feature
        # Do not change
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_point = parameters[0].valueAsText
        input_polygon = parameters[1].valueAsText
        output = parameters[2].valueAsText
        # Intersect tool
        arcpy.Intersect_analysis([input_point, input_polygon], output)

        return


# Point Density Tool
class Tool3(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Density"
        self.description = "Calculates point density"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        # input data points
        # Do not change
        input_points = arcpy.Parameter(name="input_points",
                                       displayName="input points",
                                       datatype="DEShapefile",
                                       parameterType="Required",  # Required|Optional|Derived
                                       direction="Input",  # Input|Output
                                       )
        params.append(input_points)

        # output raster surface
        # Do not change
        output_raster = arcpy.Parameter(name="output_raster",
                                        displayName="output raster",
                                        datatype="DERasterDataset",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Output",  # Input|Output
                                        )
        params.append(output_raster)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_points = parameters[0].valueAsText
        output_raster = parameters[1].valueAsText

        # turns on spatial analysis extension
        arcpy.CheckOutExtension("Spatial")

        # Point Density tool
        outPdens = arcpy.sa.PointDensity(input_points, "None", 30, "", "SQUARE_MILES")
        outPdens.save(output_raster)


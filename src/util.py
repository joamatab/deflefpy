"""_summary_
An utilities file containing data structures and other data
that is used both in LEF parsing and DEF parsing.
"""

from collections import defaultdict
from enum import Enum
from pickletools import uint8
import numpy as np

class Unsupported(object):
    """_summary_
    A class that represents an unsupported feature.
    """
    def __init__(self, feature):
        self.feature = feature
    def __str__(self):
        return "Unsupported feature: {}".format(self.feature)

"""
List of possible LFEF keywords
"""
LEF_STATEMENTS = [
    "VERSION",
    "DIVIDERCHAR",
    "BUSBITCHARS",
    "DESIGN",
    "UNITS",
    "FREQUENCY",
    "TIME",
    "OHMS",
    "NANOSECONDS",
    "PICOFARADS",
    "DATABASE",
    "MICRONS",
    "MANUFACTURINGGRID",
    "SYMMETRY",
    "CLASS",
    "CORE",
    "SIZE",
    "END",
    "PROPERTY",
    "LAYER",
    "ROW",
    "SITE",
    "VIA",
    "VIARULE",
    "SPACING",
    "ORIGIN",
    "PITCH",
    "OFFSET",
    "MASK",
    "PATTERN",
    "MACRO",
    "PIN",
    "GATE",
    "GENERATE",
    "SPACINGTABLE",
    "ARRAYSPACING",
    "WIDTH",
    "LENGTH",
    "ENCLOSURE",
    "PREFERENCLOSURE",
    "RESISTANCE",
    "RPERSQ",
    "CAPACITANCE",
    "CPERSQDIST",
    "EDGECAPACITANCE",
    "NET",
    "DCCURRENTDENSITY",
    "VOLTAGE",
    "ACCURRENTDENSITY",
    "ANTENNAMODEL",
    "ANTENNAAREARATIO",
    "ANTENNADIFFAREARATIO",
    "ANTENNACUMAREARATIO",
    "ANTENNACUMDIFFAREARATIO",
    "ANTENNAAREAFACTOR",
    "ANTENNACUMROUTINGPLUSCUT",
    "ANTENNAGATEPLUSDIFF",
    "ANTENNAAREAMINUSDIFF",
    "ANTENNAAREADIFFREDUCEPWL",
    "CUT",
    "ROUTING",
    "PWL",
    "RECT",
    "POLYGON",
    "OVERLAP",
    "MASTERSLICE",
    "BUMP",
    "DIELECTRIC",
    "DIRECTION",
    "MINWIDTH",
    "MINENCLOSEDAREA",
    "PARALLELRUNLENGTH",
    "THICKNESS",
    "AVERAGE",
    "PEAK",
    "RMS",
]

class LefDecimal:
    """_summary_
    A special LEF decimal representation.
    Args:
        object (LefDecimal): LefDecimal class object
    """
    def __init__(self, value:float):
        """_summary_
        The class object constructor.
        Args:
            value (float) : decimal value.
        """
        self.value = value
    
    def __str__(self):
        """_summary_
        The class object string description.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return "{}".format(self.value)

    def __add__(self, other):
        """_summary_
        The class object addition operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(self.value + other.value)
    
    def __sub__(self, other):
        """_summary_
        The class object subtraction operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(self.value - other.value)
    def __mult__(self, other):
        """_summary_
        The class object multiplication operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(self.value * other.value)
    def __truediv__(self, other):
        """_summary_
        The class object division operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(self.value / other.value)
    def __floordiv__(self, other):
        """_summary_
        The class object division operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(self.value // other.value)
    def __mod__(self, other):
        """_summary_
        The class object modulus division operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(self.value % other.value)

    def __eq__(self, other):
        """_summary_
        The class object equality operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return self.value == other.value

    def __ne__(self, other):
        """_summary_
        The class object inequality operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return self.value != other.value
    
    def __lt__(self, other):
        """_summary_
        The class object less than operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return self.value < other.value
    
    def __le__(self, other):
        """_summary_
        The class object less than or equal operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return self.value <= other.value
    
    def __gt__(self, other):
        """_summary_
        The class object greater than operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return self.value > other.value
    
    def __ge__(self, other):
        """_summary_
        The class object greater than or equal operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return self.value >= other.value
    
    def __neg__(self):
        """_summary_
        The class object negation operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(-self.value)
    
    def __abs__(self):
        """_summary_
        The class object absolute value operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(abs(self.value))
    
    def __round__(self, ndigits=None):
        """_summary_
        The class object rounding operator.
        Args:
            object (LefDecimal): LefDecimal class object
        """
        return LefDecimal(round(self.value, ndigits))
    
    
class LefPoint:
    """_summary_
    A point for LEF geometries.
    
    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    def __init__(self, x:float, y:float):
        self.x = LefDecimal(x)
        self.y = LefDecimal(y)
    def __add__(self, other):
        return LefPoint(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return LefPoint(self.x - other.x, self.y - other.y)
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class LefStepPattern(object):
    """_summary_

    Args:
        xCount (int): _description_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    def __init__(   self, 
                    xCount: uint8,
                    yCount: uint8, 
                    xStep:  LefDecimal, 
                    yStep:  LefDecimal
                ):
        self.xCount = xCount
        self.yCount = yCount
        self.xStep = xStep
        self.yStep = yStep
    def __str__(self):
        """_summary_
        A string representation of the object.
        Args:
            object (LefStepPattern): LefStepPattern object
        """
        return "DO {} BY {} STEP {} {}".format(self.xCount, self.yCount, self.xStep, self.yStep)

class LefGeometryClass(Enum):
    """_summary_
    LEF geometry statement types.
    Args:
        RECT    : Rectangle
        PATH    : Path
        POLYGON : Polygon
        VIA     : Via
    """
    LAYER   = 0
    RECT    = 1
    PATH    = 2
    POLYGON = 3
    VIA     = 4
    

class LefGeometry(object):
    """_summary_
    A geometry parent class for LEF geometries.
    """
    def __init__(self, type):
        """_summary_
        The class object constructor.
        Args:
            type (LefGeometryClass): The geometry type.
            points (list): 
        """
        self.type = type
        self.mask = None
        self.iterate = False
        self.points = None
        self.stepPattern = None
        
    def __str__(self):
        rets = ""
        points = "{}".format(" ".join([str(p) for p in self.points]))
        if self.type != LefGeometryClass.VIA:
            rets = "{} ".format(self.type.name)
            if self.mask != None:
                rets += "MASK {} ".format(str(self.mask))
            if self.iterate:
                rets += "ITERATE "
            rets += points
            if self.stepPattern != None:
                rets += " {}".format(str(self.stepPattern))
        else:
            rets = "{} ".format(self.type.name)
            if self.iterate:
                rets += "ITERATE "
            if self.mask != None:
                rets += "MASK {} ".format(str(self.mask))
            rets += points
            if self.stepPattern != None:
                rets += " {}".format(str(self.stepPattern))
        return rets
    
    def parse_data(self, data):
        """_summary_
        Parse the geometry data into the geometry object fields.
        Args:
            data (list): data[0] = statement name, data[1] = geometry data
        """
        statement = data[0]
        value = data[1]
        if statement == "MASK":
            if type(value) != uint8:
                raise TypeError("MASK value must be an unsigned 8-bit integer")
            self.mask = value
        elif statement == "ITERATE":
            if type(value) != bool:
                raise TypeError("ITERATE value must be a boolean")
            self.iterate = True
        else:
            raise TypeError("Unknown geometry statement: {}".format(statement))
    
    def add_points(self, points: list):
        """_summary_
        Adds the points to the LEF geometry object.
        Args:
            points (list): _description_
            pathWidth (float, optional): _description_. Defaults to None.
        Raises:
            TypeError
        """
        if self.points is None:
            raise TypeError("Points must be added")
        if self.type == LefGeometryClass.PATH:
            if len(points) < 2:
                raise TypeError("Path must have at least 2 points")
        if self.type == LefGeometryClass.POLYGON:
            if len(points) < 3:
                raise TypeError("Polygon must have at least 3 points")
        if self.type == LefGeometryClass.VIA:
            if len(points) != 1:
                raise TypeError("Via must have exactly 1 point")
        if self.type == LefGeometryClass.RECT:
            if len(points) != 2:
                raise TypeError("Rectangle must have exactly 2 points")
        self.points = np.ndarray([LefPoint(p[0], p[1]) for p in points])
        
    def add_stepPattern(self, stepPattern: LefStepPattern):
        """_summary_
        Adds the step pattern to the LEF geometry object.
        Args:
            stepPattern (list): _description_
        Raises:
            TypeError
        """
        if self.stepPattern is None:
            raise TypeError("Step pattern is None")
        self.stepPattern = stepPattern
    
class LefRect(LefGeometry):
    """_summary_
    A child class for LEF RECT geometries.
    """
    def __init__(self, type):
        super().__init__(LefGeometryClass.RECT)
        self.density = None
        
    def __str__(self):
        ret = super().__str__()
        if self.density != None:
            ret += " {}".format(self.density)
        return ret

    
    def add_points(self, points: list):
        return super().add_points(points)
    
    def add_stepPattern(self, stepPattern: LefStepPattern):
        return super().add_stepPattern(stepPattern)
    
    def add_density(self, density):
        """_summary_
        Adds the density to the LEF geometry object.
        Args:
            density (float): density of the rect in DENSITY statements
        Raises:
            TypeError
        """
        if self.density != None:
            raise TypeError("Density already set")
        if type(density) == LefDecimal:
            self.density = density
        elif type(density) == float:
            self.density = LefDecimal(density)
        else:
            raise TypeError("Density must be a float or LefDecimal")
        
    
    
class LefPath(LefGeometry):
    """_summary_
    A child class for LEF PATH geometries.
    """
    def __init__(self, type):
        super().__init__(LefGeometryClass.PATH)
        self.pathWidth = None
        
    def __str__(self):
        return super().__str__()
    
    def add_points(self, points: list):
        return super().add_points(points)
    
    def add_pathWidth(self, pathWidth):
        """_summary_
        Adds the path width to the geometry object.
        Args:
            pathWidth (float): _description_
        Raises:
            TypeError
        """
        if self.points is None:
            raise TypeError("Points must be added")
        if type(pathWidth) == float:
            self.pathWidth = LefDecimal(pathWidth)
        elif type(pathWidth) == LefDecimal:
            self.pathWidth = pathWidth
        else:
            raise TypeError("Path width must be a float or LefDecimal")
        
    def add_stepPattern(self, stepPattern: LefStepPattern):
        return super().add_stepPattern(stepPattern)

class LefDesignRuleWidth(object):
    def __init__(self, value):
        if type(value) == float:
            self.value = LefDecimal(value)
        elif type(value) == LefDecimal:
            self.value = value
        else:
            raise TypeError("Design rule width must be a float or LefDecimal")
    def __str__(self):
        return "DESIGNRULEWIDTH {}".format(str(self.value))


class LefViaGeom(LefGeometry):
    """_summary_
    A child class for LEF VIA geometries.
    """
    def __init__(self):
        super().__init__(LefGeometryClass.VIA)
        self.viaWidth = None
        
    def __str__(self):
        return super().__str__()
    
    def add_points(self, points: list):
        return super().add_points(points)
    
    def add_viaWidth(self, viaWidth: float):
        """_summary_
        Adds the via width to the geometry object.
        Args:
            viaWidth (float): _description_
        Raises:
            TypeError
        """
        if self.points is None:
            raise TypeError("Points must be added")
        if type(viaWidth) != float:
            raise TypeError("Via width must be a float")
        self.viaWidth = LefDecimal(viaWidth)

    def add_stepPattern(self, stepPattern: LefStepPattern):
        return super().add_stepPattern(stepPattern)
        
class LefLayerGeom(LefGeometry):
    def __init__(self, name: str):
        super().__init__(LefGeometryClass.LAYER)
        self.name = name
        self.exceptPgNet = False
        self.designRule = None
        self.width = None
        self.geometries = []
        
    def __str__(self):
        ret = "LAYER {}\n".format(self.name)
        if self.exceptPgNet:
            ret += "\tEXCEPTPGNET\n"
        if self.spacing is not None:
            ret += "\t{} ;\n".format(str(self.spacing))
        if self.width is not None:
            ret += "{} ;\n".format(str(self.width))
        for g in self.geometries:
            ret += "\t{} ;\n".format(str(g))
        return ret

    def parse_data(self, data):
        """_summary_
        Parse the geometry data into the geometry object fields.
        Args:
            data (list): data[0] = statement name, data[1] = geometry data
        """
        statement = data[0]
        value = data[1]
        if statement == "EXCEPTPGNET":
            self.exceptPgNet = True
        elif statement == "SPACING":
            if type(value) != LefSpacing:
                raise TypeError("SPACING value must be a LefSpacing object")
            self.designRule = value
        elif statement == "DESIGNRULEWIDTH":
            if type(value) == LefDesignRuleWidth:
                self.designRule = value
            elif type(value) == LefDecimal or type(value) == float:
                self.designRule = LefDesignRuleWidth(value)
            else:    
                raise TypeError("DESIGNRULEWIDTH value must be a LefDesignRuleWidth object")
        elif statement == "WIDTH":
            if type(value) == float:
                self.width = LefDecimal(value)
            elif type(value) == LefDecimal:
                self.width = value
            else:
                raise TypeError("WIDTH value must be a float or LefDecimal object")
        elif statement == "RECT":
            if type(value) != LefRect:
                raise TypeError("RECT value must be a LefRect object")
            self.geometries.append(value)
        elif statement == "PATH":
            if type(value) != LefPath:
                raise TypeError("PATH value must be a LefPath object")
            self.geometries.append(value)
        elif statement == "POLYGON":
            if type(value) != LefPolygon:
                raise TypeError("POLYGON value must be a LefPolygon object")
            self.geometries.append(value)
        else:
            raise TypeError("Unknown geometry statement: {}".format(statement))
        

class LefPolygon(LefGeometry):
    """_summary_
    A child class for LEF RECT geometries.
    """
    def __init__(self):
        super().__init__(LefGeometryClass.POLYGON)
        
    def __str__(self):
        return super().__str__()
    
    def add_points(self, points: list):
        return super().add_points(points)
    
    def add_stepPattern(self, stepPattern: LefStepPattern):
        return super().add_stepPattern(stepPattern)

class LefSpacingValType(Enum):
    """_summary_
    Possible LEF SPACING statement values.
    Args:
        LAYER           : Secondary layer statement
        ADJACENTCUTS    : Adjacent cuts statement
        PARALLELOVERLAP : Parallel overlap statement
        AREA            : Area statement
    """
    LAYER           = 1
    ADJACENTCUTS    = 2
    PARALLELOVERLAP = 3
    AREA            = 4

class LefSecondaryLayer(object):
    """_summary_
    A LEF secondary layer object to use as a SPACING statement value.
    Args:
        object (_type_): _description_
    """
    def __init__(self, layerName: str, stack: bool):
        self.layerName = layerName
        self.stack = stack
        
    def __str__(self):
        ret = "LAYER {}".format(self.layerName)
        if self.stack:
            ret += " STACK"
        return ret

class LefAdjacentCuts(object):
    """_summary_
    A LEF ADJACENTCUTS object to use as a SPACING statement value.
    Args:
        object (_type_): _description_
    """
    def __init__(self, numVia: uint8, cutWithin: float, exceptSamePgNet: bool):
        if numVia not in [2, 3, 4]:
            raise ValueError("Number of vias must be 2, 3, or 4")
        self.numVia = numVia
        self.cutWithin = LefDecimal(cutWithin)
        self.exceptSamePgNet = exceptSamePgNet

    def __str__(self):
        ret = "ADJACENTCUTS {} WITHIN {}".format(self.numVia, self.cutWithin)
        if self.exceptSamePgNet:
            ret += " EXCEPTSAMEPGNET"
        return ret
    
class LefSpacing(object):
    """_summary_
    An LEF Spacing table.
    Args:
        object (_type_): _description_
    """
    def __init__(self, cutSpacing: float):
        self.cutSpacing = LefDecimal(cutSpacing)
        self.centerToCenter = False
        self.sameNet = False
        self.valueType = None
        self.value = None
    def __str__(self) -> str:
        ret = "SPACING {}".format(self.cutSpacing)
        if self.centerToCenter:
            ret += "\n\tCENTERTOCENTER"
        if self.sameNet:
            ret += "\n\tSAMENET"
        if self.valueType is not None:
            if self.valueType == LefSpacingValType.LAYER:
                ret += "\n\t{}".format(str(self.value))
            elif self.valueType == LefSpacingValType.ADJACENTCUTS:
                ret += "\n\t{}".format(str(self.value))
            elif self.valueType == LefSpacingValType.PARALLELOVERLAP:
                ret += "\n\t{}".format(self.valueType.name)
            elif self.valueType == LefSpacingValType.AREA:
                ret += "\n\t{} {}".format(self.valueType.name, str(self.value))
            else:
                raise ValueError("Unknown value type")
        ret += "\n;"
        return ret
    def parse_data(self, data):
        statement = data[0]
        value = data[1]
        if statement == "CENTERTOCENTER":
            self.centerToCenter = True
        elif statement == "SAMENET":
            self.sameNet = True
        elif statement == "LAYER":
            if type(value) is not LefSecondaryLayer:
                raise TypeError("Value must be a LefLayerGeom object")
            self.valueType = LefSpacingValType.LAYER
            self.value = value # value is a LefSecondaryLayer object
        elif statement == "ADJACENTCUTS":
            if type(value) is not LefAdjacentCuts:
                raise TypeError("Value must be a LefAdjacentCuts object")
            self.valueType = LefSpacingValType.ADJACENTCUTS
            self.value = value # value is a LefAdjacentCuts object
        elif statement == "PARALLELOVERLAP":
            self.valueType = LefSpacingValType.PARALLELOVERLAP
        elif statement == "AREA":
            self.valueType = LefSpacingValType.AREA
            if type(value) is float:
                self.value = LefDecimal(value)
            elif type(value) is LefDecimal:
                self.value = value
            else:
                raise TypeError("Value must be a float or LefDecimal object")
        else:
            raise ValueError("Unknown statement")
        


#TODO: develop LayerGeometry Class as part of layer geometries
class LefLayerGeometry(object):
    """_summary_
    A LEF LAYER GEOMETRY statement for MACROs.
    Args:
        object (_type_): _description_
    """
    def __init__(self, name: str):
        """_summary_
        Class constructor.
        Args:
            name (str)              : name of the layer geometry
        """
        self.geometries = [] 
        
    def __str__(self):
        """_summary_
        Returns a string representation of the object.
        Args:
            object (_type_): LefLayerGeometry object
        Returns:
            str : string representation of the object
        """
        ret = ""
        for geom in self.geometries:
            ret += "\t{} ;\n".format(str(geom))
        return ret

    def add_geometry(self, geom):
        """_summary_
        Adds a geometry to the layer geometry.
        Args:
            geom (LefGeometry) : geometry to add
        """
        if type(geom) is LefLayerGeom:
            self.geometries.append(geom)
        elif type(geom) is LefViaGeom:
            self.geometries.append(geom)
        else:
            raise TypeError("Layer Geometry must be a LefLayerGeom or LefViaGeom object")
    
class LefDensity(object):
    def __init__(self):
        """_summary_
        Class constructor.
        Args:
            object (_type_): LefDensity object
        """
        self._currentLayer = "" # state variable to know
                                # to which layer the rect 
                                # will be declared in
        self.layerRectDict = defaultdict(list)
        
    def __str__(self):
        """_summary_
        String representation of the object.
        Args:
            object (_type_): LefDensity object
        Returns:
            str : string representation of the object
        """
        ret = "DENSITY\n"
        for layer in self.layerRectDict.keys():
            ret += "\tLAYER {} ;\n".format(layer)
            for rect in self.layerRectDict[layer]:
                ret += "\t\t{} ;\n".format(str(rect))
        ret += "END"
        return ret
    def parse_data(self, data):
        """_summary_
        Parses the data and adds the rectangles to the 
        respective layer in the DENSITY statement.
        Args:   
            data (Tuple): (statement, value) 
        Raises:
            TypeError: Value must be a nust be a string
            TypeError: Value must be a LefRect object
            ValueError: Unknown statement
        """
        statement = data[0]
        value = data[1]
        if statement == "LAYER":
            if type(value) is not str:
                raise TypeError("Value following LAYER statement must be a string")
            self._currentLayer = value
        elif statement == "RECT":
            if type(value) is not LefRect:
                raise TypeError("Value following RECT statement must be a LefRect object")
            self.layerRectDict[self._currentLayer].append(value)
        else:
            raise ValueError("Unknown statement")

class LefPieceWiseLinearInterpol(object):
    """_summary_
    LEF Piecewise Linear interpolation data struct (PWL).
    """
    def __init__(self, points):
        """_summary_
        The class object constructor.
        Args:
            points (list): list of points
        """
        self.points = np.ndarray([LefPoint(p[0], p[1]) for p in points])
    def __str__(self):
        """_summary_
        A str representation of the LEF PWL statement value.
        Args:
            object (LefPieceWiseLinearInterpol): LEF PWL value
        """
        points ="".join([" ( {} ) ".format(str(p)) for p in self.points])
        return "PWL ({})".format(points)

class LefAntennaFieldType(Enum):
    """_summary_
    An enum class for antenna field types.
    Args:
        ANTENNAMODEL : ANTENNAMODEL statement
        ANTENNAPARTIALMETALAREA : ANTENNAPARTIALMETALAREA statement
        ...
    """
    ANTENNAMODEL = 1
    ANTENNAPARTIALMETALAREA = 2
    ANTENNAPARTIALMETALSIDEAREA = 3
    ANTENNAPARTIALCUTAREA = 4
    ANTENNADIFFAREA = 5
    ANTENNAGATEAREA = 6
    ANTENNAMXAAREACAR = 7
    ANTENNAMAXSIDEAREACAR = 8
    ANTENNAMAXCUTCAR = 9
    ANTENNAAREARATIO = 10
    ANTENNADIFFAREARATIO = 11
    ANTENNACUMAREARATIO = 12
    ANTENNACUMDIFFAREARATIO = 13
    ANTENNAAREAFACTOR = 14
    ANTENNACUMROUTINGPLUSCUT = 15
    ANTENNAGATEPLUSDIFF = 16
    ANTENNAAREAMINUSDIFF = 17
    ANTENNAAREADIFFREDUCEPWL = 18

class LefAntennaModel(Enum):
    """_summary_
    Enumeration of possible antenna model types.
    Args:
        OXIDE1 : oxide1 antenna type
        OXIDE2 : oxide2 antenna type
        OXIDE3 : oxide3 antenna type
        OXIDE4 : oxide4 antenna type
    """
    OXIDE1 = 1
    OXIDE2 = 2
    OXIDE3 = 3
    OXIDE4 = 4

class LefAntennaField(object):
    """_summary_
    A LEF ANTENNA FIELD statement data structure
    """
    def __init__(   self,
                    fieldType: LefAntennaFieldType,
                ):
        """_summary_
        The class object constructor.
        Args:
            name (str)               : property name
            value (str/LefDecimal)   : property value
        Raises:
            TypeError
        """
        if type(fieldType) != LefAntennaFieldType:
            raise TypeError("LefAntennaField: fieldType must be LefAntennaFieldType")
        self.fieldType = fieldType
        self.layerName = ""
        self.value = None # can either be LefDecimal or PWL class object, or a antenna model
        self.diffuseOnly = False
        
    def __str__(self):
        """_summary_
        str representation of the LEF ANTENNA FIELD statement value.
        Returns:
            ret (str): str representation of the LEF ANTENNA FIELD statement
        """
        ret = "{}".format(self.fieldType.name)
        if self.value != None:
            ret += " {}".format(str(self.value))
        if self.layerName != "":
            ret += " LAYER {}".format(self.layerName)
        if self.diffuseOnly:
            ret += " DIFFUSEONLY"
        return ret
    
    def parse_data(self, data):
        """_summary_
        Parses the data for the LEF ANTENNA FIELD statement.
        Args:
            data (Tuple): (statment : str, value: Generic Type)
        Raises:
            TypeError: Unknown statement
        """
        statement = data[0]
        value = data[1]
        if statement == "LAYER":
            self.layerName = value
        elif statement == "PWL":
            if type(value) != LefPieceWiseLinearInterpol:
                raise TypeError("LefAntennaField: PWL needs to be LefPieceWiseLinearInterpol object")
            self.value = value
        elif statement == "DIFFUSEONLY":
            self.diffuseOnly = True
        elif statement == "OXIDE1":
            self.value = LefAntennaModel.OXIDE1
        elif statement == "OXIDE2":
            self.value = LefAntennaModel.OXIDE2
        elif statement == "OXIDE3":
            self.value = LefAntennaModel.OXIDE3
        elif statement == "OXIDE4":
            self.value = LefAntennaModel.OXIDE4
        else:
            raise TypeError("LefAntennaField: {} is not a valid statement".format(statement))
        
class LefPort(object):
    """_summary_
    A LEF PORT statement data structure
    """
    def __init__(self):
        self.name = None
        self.type = LefStatementType.PORT
        self.portClass = None
        self.layerGeometries = []    
    def __str__(self):
        ret = "PORT\n".format(self.name)
        if self.portClass != None:
            ret += "CLASS {} ;\n".format(self.portClass.name)
        for layerGeometry in self.layerGeometries:
            ret += "{}\n".format(layerGeometry)         
        return ret

# create macro enumerations
class LefStatementType(Enum):
    """_summary_: LefStatementType
    Types of possible LEF super statements.
    Args:
        MACRO   : Macro statement.
        LAYER   : Layer statement.
        SITE    : Site statement.
        VIA     : Via statement.
        VIARULE : Via rule statement.
        OBS     : Obstruction statement.
        PIN     : Pin statement.
        PORT    : Port statement.
    """
    MACRO   = 1
    LAYER   = 2
    SITE    = 3
    VIA     = 4
    VIARULE = 5
    OBS     = 6
    PIN     = 7
    PORT    = 8
    
class LefStatement(object):
    """_summary_
    A parent class for all LEF statements.
    Args:
        object (_type_): LefStatement class object
    """
    def __init__ (self, name:str, type:LefStatementType):
        """_summary_
        The class object constructor.
        Args:
            name (str)           : str representation of the name of the  statement.
            type (LefStatementType) : type of the LEF statement.
        """
        self.type = type
        self.name = name
    
    def __str__(self):
        """_summary_
        The class object str description.
        Args:
            object (LefStatement): statement object
        """
        return "LefStatement: {} {}".format(self.type.name, self.name)
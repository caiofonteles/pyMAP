#   Copyright (C) 2014 mdm                                     
#   map[dot]plus[dot]plus[dot]help[at]gmail                     
#                                                              
# Licensed to the Apache Software Foundation (ASF) under one   
# or more contributor license agreements.  See the NOTICE file 
# distributed with this work for additional information        
# regarding copyright ownership.  The ASF licenses this file   
# to you under the Apache License, Version 2.0 (the            
# "License"); you may not use this file except in compliance   
# with the License.  You may obtain a copy of the License at   
#                                                              
#   http://www.apache.org/licenses/LICENSE-2.0                 
#                                                              
# Unless required by applicable law or agreed to in writing,   
# software distributed under the License is distributed on an  
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY       
# KIND, either express or implied.  See the License for the    
# specific language governing permissions and limitations            
# under the License.                                             

from __future__ import print_function

import sys
from ctypes import *
import os
import six

from distutils.sysconfig import get_config_var

from sys import platform

libext = get_config_var('EXT_SUFFIX')
if libext is None or libext == '':
    if platform == "linux" or platform == "linux2":
        libext = '.so'
    elif platform == "darwin":
        #libext = '.dyld'
        libext = '.so'
    elif platform == "win32":
        #libext = '.dll'
        libext = '.pyd'
    elif platform == "cygwin":
        libext = '.dll'

maplib = '_libmap' + libext

libpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.path.sep + maplib

"""A collection of methods for the MAP++ program"""
libexec = cdll.LoadLibrary(libpath)

'''
# these are the fortran derived types created by the FAST registry.
f_type_init = None
f_type_initout = None
f_type_d = None
f_type_u = None
f_type_x = None
f_type_y = None
f_type_z = None
f_type_p = None

ierr = c_int(0)
status = create_string_buffer(1024)
summary_file = c_char_p
val = c_double
'''

class ModelData_Type(Structure):
    _fields_ = []


# void * object ;
# double gravity ;
# double seaDensity ;
# double depth ;
# char fileName[255] ;
# char summaryFileName[255] ;
# char libraryInputLine[255] ;
# char nodeInputLine[255] ;
# char elementInputLine[255] ;
# char optionInputLine[255] ;
class InitializationData_Type(Structure):
    _fields_= [("object",c_void_p),
               ("gravity",c_double),
               ("seaDensity",c_double),
               ("depth",c_double),
               ("fileName",c_char*255),
               ("summaryFileName",c_char*255),
               ("libraryInputLine",c_char*255),
               ("nodeInputLine",c_char*255),
               ("elementInputLine",c_char*255),
               ("optionInputLine",c_char*255)]



# void * object ;
# char progName[99] ;
# char version[99] ;
# char compilingData[24] ;
# char * writeOutputHdr ;     int writeOutputHdr_Len ;
# char * writeOutputUnt ;     int writeOutputUnt_Len ;

class InitializationOutputData_Type(Structure):
    _fields_ = [("object",c_void_p),
                ("progName",c_char*99),
                ("version",c_char*99),
                ("CompilingData",c_char*99),
                ("writeOutputHdr",c_char_p),
                ("writeOutputHdr_Len",c_int),
                ("writeOutputUnt",c_char_p),
                ("writeOutputUnt_Len",c_int)]

class InputData_Type(Structure):
    _fields_ = []


class OutputData_Type(Structure):
    _fields_ = []



# void * object ;
# double g ;
# double depth ;
# double rhoSea ;

class ParameterData_Type(Structure):
    _fields_ = [("object",c_void_p),
                ("g",c_double),
                ("depth",c_double), 
                ("rhoSea", c_double)]


class ConstraintData_Type(Structure):
    _fields_ = []


class ContinuousData_Type(Structure):
    _fields_ = []

# fields for the fortran types
# 
# MAP_EXTERNCALL MAP_InitInputType_t* map_create_init_type( char* msg, MAP_ERROR_CODE* status );
# MAP_EXTERNCALL MAP_InitOutputType_t* map_create_initout_type( char* msg, MAP_ERROR_CODE* status );
# MAP_EXTERNCALL MAP_InputType_t* map_create_input_type( char* msg, MAP_ERROR_CODE* status );
# MAP_EXTERNCALL MAP_ParameterType_t* map_create_parameter_type( char* msg, MAP_ERROR_CODE* status );
# MAP_EXTERNCALL MAP_ConstraintStateType_t* map_create_constraint_type( char* msg, MAP_ERROR_CODE* status );
# MAP_EXTERNCALL MAP_OtherStateType_t* map_create_other_type( char* msg, MAP_ERROR_CODE* status );
# MAP_EXTERNCALL MAP_OutputType_t* map_create_output_type( char* msg, MAP_ERROR_CODE* status );
# MAP_EXTERNCALL MAP_ContinuousStateType_t* map_create_continuous_type( char* msg, MAP_ERROR_CODE* status );

MapData_Type       = POINTER(ModelData_Type)
MapInit_Type       = POINTER(InitializationData_Type)
MapInitOut_Type    = POINTER(InitializationOutputData_Type)
MapInput_Type      = POINTER(InputData_Type)
MapOutput_Type     = POINTER(OutputData_Type)
MapParameter_Type  = POINTER(ParameterData_Type)
MapConstraint_Type = POINTER(ConstraintData_Type)
MapContinuous_Type = POINTER(ContinuousData_Type)

# read file stuff
libexec.set_init_to_null.argtype=[MapInit_Type, c_char_p, POINTER(c_int) ]
libexec.map_set_summary_file_name.argtype=[MapInit_Type, c_char_p, POINTER(c_int) ]
libexec.map_add_cable_library_input_text.argtype=[MapInit_Type]
libexec.map_add_node_input_text.argtype=[MapInit_Type]
libexec.map_add_line_input_text.argtype=[MapInit_Type]
libexec.map_add_options_input_text.argtype=[MapInit_Type]

libexec.map_create_init_type.argtype       = [ c_char_p, POINTER(c_int) ]
libexec.map_create_initout_type.argtype    = [ c_char_p, POINTER(c_int) ]
libexec.map_create_input_type.argtype      = [ c_char_p, POINTER(c_int) ]
libexec.map_create_parameter_type.argtype  = [ c_char_p, POINTER(c_int) ]
libexec.map_create_constraint_type.argtype = [ c_char_p, POINTER(c_int) ]
libexec.map_create_other_type.argtype      = [ c_char_p, POINTER(c_int) ]
libexec.map_create_output_type.argtype     = [ c_char_p, POINTER(c_int) ]
libexec.map_create_continuous_type.argtype = [ c_char_p, POINTER(c_int) ]
libexec.map_create_continuous_type.argtype = [ MapData_Type ]

libexec.map_create_init_type.restype       = MapInit_Type
libexec.map_create_initout_type.restype    = MapInitOut_Type
libexec.map_create_input_type.restype      = MapInput_Type
libexec.map_create_parameter_type.restype  = MapParameter_Type
libexec.map_create_constraint_type.restype = MapConstraint_Type
libexec.map_create_other_type.restype      = MapData_Type
libexec.map_create_output_type.restype     = MapOutput_Type
libexec.map_create_continuous_type.restype = MapContinuous_Type


libexec.map_set_sea_depth.argtypes   = [ MapParameter_Type, c_double ]
libexec.map_set_gravity.argtypes     = [ MapParameter_Type, c_double ]
libexec.map_set_sea_density.argtypes = [ MapParameter_Type, c_double ]

libexec.map_size_lines.restype = c_int

# numeric routines
libexec.map_residual_function_length.restype = c_double
libexec.map_residual_function_height.restype = c_double
libexec.map_jacobian_dxdh.restype            = c_double
libexec.map_jacobian_dxdv.restype            = c_double
libexec.map_jacobian_dzdh.restype            = c_double
libexec.map_jacobian_dzdv.restype            = c_double

libexec.map_residual_function_length.argtypes = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
libexec.map_residual_function_height.argtypes = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
libexec.map_jacobian_dxdh.argtypes            = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
libexec.map_jacobian_dxdv.argtypes            = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
libexec.map_jacobian_dzdh.argtypes            = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]
libexec.map_jacobian_dzdv.argtypes            = [ MapData_Type, c_int, c_char_p, POINTER(c_int) ]


libexec.map_get_fairlead_force_2d.argtypes = [POINTER(c_double), POINTER(c_double), MapData_Type, c_int, c_char_p, POINTER(c_int)]


# plot routines
libexec.map_plot_x_array.argtypes = [ MapData_Type, c_int, c_int, c_char_p, POINTER(c_int) ]
libexec.map_plot_x_array.restype  = POINTER(c_double)
libexec.map_plot_y_array.argtypes = [ MapData_Type, c_int, c_int, c_char_p, POINTER(c_int) ]
libexec.map_plot_y_array.restype  = POINTER(c_double)
libexec.map_plot_z_array.argtypes = [ MapData_Type, c_int, c_int, c_char_p, POINTER(c_int) ]
libexec.map_plot_z_array.restype  = POINTER(c_double)
libexec.map_plot_array_free.argtypes = [ POINTER(c_double) ]



# modifyers
libexec.map_offset_vessel.argtypes = [MapData_Type, MapInput_Type, c_double, c_double, c_double, c_double, c_double, c_double, c_char_p, POINTER(c_int)]        
libexec.map_linearize_matrix.argtypes = [MapInput_Type, MapParameter_Type, MapData_Type, MapOutput_Type, MapConstraint_Type, c_double, POINTER(c_int), c_char_p]        
libexec.map_linearize_matrix.restype  = POINTER(POINTER(c_double))
libexec.map_free_linearize_matrix.argtypes = [POINTER(POINTER(c_double))]

libexec.map_init.argtypes = [ MapInit_Type,
                          MapInput_Type,
                          MapParameter_Type,
                          MapContinuous_Type,
                          MapConstraint_Type,
                          MapData_Type,
                          MapOutput_Type,
                          MapInitOut_Type,
                          POINTER(c_int),
                          c_char_p]


libexec.map_update_states.argtypes = [ c_float,
                                   c_int,
                                   MapInput_Type,
                                   MapParameter_Type,
                                   MapContinuous_Type,
                                   MapConstraint_Type,
                                   MapData_Type,
                                   POINTER(c_int),
                                   c_char_p]

libexec.map_end.argtypes = [ MapInput_Type,
                         MapParameter_Type,
                         MapContinuous_Type,
                         MapConstraint_Type,
                         MapData_Type,
                         MapOutput_Type,
                         POINTER(c_int),
                         c_char_p]


libexec.map_initialize_msqs_base.argtypes = [MapInput_Type,
                                         MapParameter_Type,
                                         MapContinuous_Type,
                                         MapConstraint_Type,
                                         MapData_Type,
                                         MapOutput_Type,
                                         MapInitOut_Type]


libexec.map_size_lines.argtypes = [ MapData_Type,
                                POINTER(c_int),
                                c_char_p]



class pyMAP(object):

    def __init__( self ) :
        self.ierr = c_int(0)
        self.status = create_string_buffer(1024)
        
        self.f_type_d       = self.CreateDataState()
        self.f_type_u       = self.CreateInputState( )
        self.f_type_x       = self.CreateContinuousState( )
        self.f_type_p       = self.CreateParameterState( )
        self.f_type_y       = self.CreateOutputState( )
        self.f_type_z       = self.CreateConstraintState( )
        self.f_type_init    = self.CreateInitState( )
        self.f_type_initout = self.CreateInitoutState( )
        libexec.set_init_to_null(self.f_type_init, self.status, pointer(self.ierr) )
        libexec.map_initialize_msqs_base(self.f_type_u, self.f_type_p, self.f_type_x, self.f_type_z, self.f_type_d, self.f_type_y, self.f_type_initout)
        self.summary_file(six.b('outlist.map.sum'))


    def init( self ):
        libexec.map_init( self.f_type_init, self.f_type_u, self.f_type_p, self.f_type_x, self.f_type_z, self.f_type_d, self.f_type_y, self.f_type_initout, pointer(self.ierr), self.status )
        if self.ierr.value != 0 : print(self.status.value)


    def size_lines(self):
        size = libexec.map_size_lines(self.f_type_d, pointer(self.ierr), self.status )
        if self.ierr.value != 0 : print(self.status.value)
        return size


    def update_states(self, t, interval):
        libexec.map_update_states(c_float(t), c_int(interval), self.f_type_u, self.f_type_p, self.f_type_x, self.f_type_z, self.f_type_d, pointer(self.ierr), self.status )
        if self.ierr.value != 0 : print(self.status.value)


    # Calls function in main.c and fordatamanager.c to delete insteads of c structs. First, the malloc'ed arrays need to vanish
    # gracefully; we accomplish this by calling MAP_End(...) routine. Then, the structs themself are deleted. Order is important.
    # 
    # MAP_EXTERNCALL int MAP_End ( InputData *u, ParameterData *p, ContinuousData *x, ConstraintData *z, ModelData *data, OutputData *y, char *map_msg, MAP_ERROR_CODE *ierr )
    # MAP_EXTERNCALL void MAP_Input_Delete( InputData* u )
    # MAP_EXTERNCALL void MAP_Param_Delete( ParameterData* p )
    # MAP_EXTERNCALL void MAP_ContState_Delete( InputData* x )
    # MAP_EXTERNCALL void MAP_ConstrState_Delete( InputData* z )
    # MAP_EXTERNCALL void MAP_Output_Delete( InputData* y )
    # MAP_EXTERNCALL void MAP_OtherState_Delete( ModelData* data )
    def end(self):
        libexec.map_end(self.f_type_u, self.f_type_p, self.f_type_x, self.f_type_z, self.f_type_d, self.f_type_y, pointer(self.ierr), self.status)



    # Set a name for the MAP summary file. Does not need to be called. If not called, the default name is 'outlist.sum.map'
    def summary_file(self, echo_file):
        self.f_type_init.contents.summaryFileName = echo_file
        libexec.map_set_summary_file_name(self.f_type_init, self.status, pointer(self.ierr) )



    # Calls function in fortdatamanager.c to create instance of c structs
    # MAP_EXTERNCALL InitializationData* MAP_InitInput_Create( char* map_msg, MAP_ERROR_CODE* ierr )
    def CreateInitState( self ) :
        obj = libexec.map_create_init_type( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 : print(self.status.value)
        return obj

    # Calls function in fortdatamanager.c to create instance of c structs
    # MAP_EXTERNCALL void MAP_InitOutput_Delete( InputData* io )
    def CreateInitoutState( self ) :
        obj = libexec.map_create_initout_type( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 : print(self.status.value)
        return obj


    # Calls function in fortdatamanager.c to create instance of c structs
    # MAP_EXTERNCALL ModelData *MAP_OtherState_Create( char *map_msg, MAP_ERROR_CODE *ierr )
    def CreateDataState( self ) :
        obj = libexec.map_create_other_type( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 : print(self.status.value)
        return obj


    # Calls function in fortdatamanager.c to create instance of c structs
    # MAP_EXTERNCALL InputData* MAP_Input_Create( char* map_msg, MAP_ERROR_CODE *ierr )
    def CreateInputState( self ) :
        obj = libexec.map_create_input_type( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 : print(self.status.value)
        return obj


    # Calls function in fortdatamanager.c to create instance of c structs
    # MAP_EXTERNCALL ContinuousData* MAP_ContState_Create( char* map_msg, MAP_ERROR_CODE *ierr )
    def CreateContinuousState( self ) :
        obj = libexec.map_create_continuous_type( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 : print(self.status.value)
        return obj

    # Calls function in fortdatamanager.c to create instance of c structs
    # MAP_EXTERNCALL OutputData *MAP_Output_Create( char *map_msg, MAP_ERROR_CODE *ierr )
    def CreateOutputState( self ) :
        obj = libexec.map_create_output_type( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 : print(self.status.value)
        return obj


    # Calls function in fortdatamanager.c to create instance of c structs
    # MAP_EXTERNCALL ConstraintData* MAP_ConstrState_Create( char* map_msg, MAP_ERROR_CODE *ierr )
    def CreateConstraintState( self ) :
        obj = libexec.map_create_constraint_type( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 : print(self.status.value)
        return obj


    # Calls function in fortdatamanager.c to create instance of c structs
    # MAP_EXTERNCALL ParameterData* MAP_Param_Create( char* map_msg, MAP_ERROR_CODE *ierr )
    def CreateParameterState( self ) :
        obj = libexec.map_create_parameter_type( self.status, pointer(self.ierr) )
        if self.ierr.value != 0 : print(self.status.value)
        return obj


    def map_set_sea_depth( self, depth ):
         libexec.map_set_sea_depth( self.f_type_p, depth )

    def map_set_gravity( self, g ):
        libexec.map_set_gravity( self.f_type_p, g )

    def map_set_sea_density( self, rho ):
        libexec.map_set_sea_density( self.f_type_p, rho )

    def plot_x( self, lineNum, length ) :
        arr = [None]*length
        array = POINTER(c_double)
        array = libexec.map_plot_x_array( self.f_type_d, lineNum, length, self.status, pointer(self.ierr) )        
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            libexec.map_plot_array_free( array )        
            sys.exit('MAP terminated premature.')
        arr = [array[j] for j in range(length)]        
        libexec.map_plot_array_free( array )        
        return arr 

    def plot_y( self, lineNum, length ) :
        arr = [None]*length
        array = POINTER(c_double)
        array = libexec.map_plot_y_array( self.f_type_d, lineNum, length, self.status, pointer(self.ierr) )        
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            libexec.map_plot_array_free( array )        
            sys.exit('MAP terminated premature.')
        arr = [array[j] for j in range(length)]        
        libexec.map_plot_array_free( array )        
        return arr 


    def plot_z( self, lineNum, length ) :
        arr = [None]*length
        array = POINTER(c_double)
        array = libexec.map_plot_z_array( self.f_type_d, lineNum, length, self.status, pointer(self.ierr) )        
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            libexec.map_plot_array_free( array )        
            sys.exit('MAP terminated premature.')
        arr = [array[j] for j in range(length)]        
        libexec.map_plot_array_free( array )        
        return arr 


    def get_fairlead_force_2d(self, index):
        """Gets the horizontal and vertical fairlead force in a 2D plane along the 
        straight-line line. Must ensure update_states() is called before accessing 
        this function. The function will not solve the forces for a new vessel position
        if it updated. , otherwise the fairlead forces are not updated with the new 
        vessel position. Called C function:
        
        MAP_EXTERNCALL void map_get_fairlead_force_2d(double* H, double* V, MAP_OtherStateType_t* other_type, int index, char* map_msg, MAP_ERROR_CODE* ierr);
    
        :param index: The line number the fairlead forces are being requested for. Zero indexed
        :returns: horizontal and vertical fairlead force [N]
    
        >>> H,V = print get_fairlead_force_2d(1)        
        """
        H_ref = c_double(-999.9)
        V_ref = c_double(-999.9)
        libexec.map_get_fairlead_force_2d( pointer(H_ref), pointer(V_ref),self.f_type_d, index, self.status, pointer(self.ierr))
        return H_ref.value, V_ref.value
    
    
    def get_fairlead_force_3d(self, index):
        """Gets the horizontal and vertical fairlead force in a 3D frame along relative 
        referene global axis. Must ensure update_states() is called before accessing 
        this function. The function will not solve the forces for a new vessel position
        if it updated. , otherwise the fairlead forces are not updated with the new 
        vessel position. Called C function:
        
        MAP_EXTERNCALL void map_get_fairlead_force_3d(double* fx, double* fy, double* fz, MAP_OtherStateType_t* other_type, int index, char* map_msg, MAP_ERROR_CODE* ierr);
    
        :param index: The line number the fairlead forces are being requested for. Zero indexed
        :returns: horizontal and vertical fairlead force [N]
    
        >>> fx,fy,fz = get_fairlead_force_3d(1)        
        """
        fx = c_double(-999.9)
        fy = c_double(-999.9)
        fz = c_double(-999.9)
        libexec.map_get_fairlead_force_3d( pointer(fx), pointer(fy), pointer(fz), self.f_type_d, index, self.status, pointer(self.ierr))
        return fx.value, fy.value, fz.value
        









    def funcl( self, i ) :
        self.val = libexec.map_residual_function_length(self.f_type_d, i, self.status, pointer(self.ierr))
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            sys.exit('MAP terminated premature.')
        return self.val


    def funch( self, i ) :
        self.val = libexec.map_residual_function_height(self.f_type_d, i, self.status, pointer(self.ierr))
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            sys.exit('MAP terminated premature.')
        return self.val


    def dxdh( self, i ) :
        self.val = libexec.map_jacobian_dxdh( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            sys.exit('MAP terminated premature.')
        return self.val


    def dxdv( self, i ) :
        self.val = libexec.map_jacobian_dxdv( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            sys.exit('MAP terminated premature.')
        return self.val


    def dzdh( self, i ) :
        self.val = libexec.map_jacobian_dzdh( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            sys.exit('MAP terminated premature.')
        return self.val


    def dzdv( self, i ) :
        self.val = libexec.map_jacobian_dzdv( self.f_type_d, i, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            sys.exit('MAP terminated premature.')
        return self.val

    def linear( self, epsilon ) :
        """Insert a function and its arguments in process pool.
    
        Input is inserted in queues using a round-robin fashion. Every job is
        identified by and index that is returned by function. Not all parameters
        of original multiprocessing.Pool.apply_aync are implemented so far.
    
        :param func: Function to process.
        :type func: Callable.
        :param args: Arguments for the function to process.
        :type args: Tuple.
        :returns: Assigned job id.
        :rtype: Int.
        """ 
        array = POINTER(POINTER(c_double))
        array = libexec.map_linearize_matrix( self.f_type_u, self.f_type_p, self.f_type_d, self.f_type_y, self.f_type_z, epsilon, pointer(self.ierr), self.status)        
        if self.ierr.value != 0 :
           print(self.status.value)
           self.end( )
           sys.exit('MAP terminated premature.')
        arr = [[array[j][i] for i in range(6)] for j in range(6)]
        libexec.map_free_linearize_matrix(array)        
        return arr
    

    def displace_vessel(self,x,y,z,phi,the,psi) :
        libexec.map_offset_vessel(self.f_type_d, self.f_type_u, x,y,z,phi,the,psi, self.status, pointer(self.ierr) )
        if self.ierr.value != 0 :
            print(self.status.value)
            self.end( )
            sys.exit('MAP terminated premature.')    

    def read_file( self, fileName ):
        f           = open(fileName, 'r')
        charptr     = POINTER(c_char)
        line_offset = []
        temp_str    = []
        offset      = 0
    
        for line in f:
            line_offset.append(offset)
            offset += len(line)    
        f.seek(0)
        
        i = 0
        for line in f:
            words = line.split()
            if words[0] == "LineType":
                next(f)
                LineType_ref = i
            elif words[0] == "Node":
                next(f)
                Node_ref = i
            elif words[0] == "Line":
                next(f)
                Line_ref = i 
            elif words[0] == "Option":
                next(f)
                Option_ref = i     
            i+=1
        
        f.seek(line_offset[LineType_ref+2])         
        for line in f:
            if line[0] == "-":
                break
            else:
                # create_string_buffer(line, 255).raw
                self.f_type_init.contents.libraryInputLine =  line+'\0'
                libexec.map_add_cable_library_input_text(self.f_type_init)
   
        f.seek(line_offset[Node_ref+3])
        for line in f:
            if line[0] == "-":
                break
            else:
                self.f_type_init.contents.nodeInputLine = line+'\0'
                libexec.map_add_node_input_text(self.f_type_init)

        f.seek(line_offset[Line_ref+4])
        for line in f:
            if line[0] == "-":
                break
            else:
                self.f_type_init.contents.elementInputLine = line+'\0'
                libexec.map_add_line_input_text(self.f_type_init)
                 
        f.seek(line_offset[Option_ref+5])
        for line in f:
            if line[0]=="-":
                break
            elif line[0]=="!":
                None
            else:
                self.f_type_init.contents.optionInputLine = line+'\0'
                libexec.map_add_options_input_text(self.f_type_init)            

                    
    def read_list_input(self, listIn):
        assert isinstance(listIn, list), 'Must input a python list of strings'
        assert len(listIn) >= 8, 'Must have at least 4 sections, 3 lines per section'
        assert type(listIn[0]) == type(''), 'List elements must be strings'
        charptr = POINTER(c_char)

        dictFlag = nodeFlag = propFlag = solvFlag = False
        listIter = iter(listIn)
        for line in listIter:
            if "LINE DICTIONARY" in line.upper():
                dictFlag = True
                nodeFlag = propFlag = solvFlag = False
                for _ in range(2): next(listIter) # Process header
                continue;
            elif "NODE PROPERTIES" in line.upper():
                nodeFlag = True
                dictFlag = propFlag = solvFlag = False
                for _ in range(2): next(listIter) # Process header
                continue;
            elif "LINE PROPERTIES" in line.upper():
                propFlag = True
                dictFlag = nodeFlag = solvFlag = False
                for _ in range(2): next(listIter) # Process header
                continue;
            elif "SOLVER OPTIONS" in line.upper():
                solvFlag = True
                dictFlag = nodeFlag = propFlag = False
                for _ in range(2): next(listIter) # Process header
                continue;

            if dictFlag:
                self.f_type_init.contents.libraryInputLine =  six.b(line+'\n\0')
                libexec.map_add_cable_library_input_text(self.f_type_init)                    

            if nodeFlag:
                self.f_type_init.contents.nodeInputLine = six.b(line+'\n\0')
                libexec.map_add_node_input_text(self.f_type_init)

            if propFlag:
                self.f_type_init.contents.elementInputLine = six.b(line+'\n\0')
                libexec.map_add_line_input_text(self.f_type_init)

            if solvFlag:
                self.f_type_init.contents.optionInputLine = six.b(line+'\n\0')
                libexec.map_add_options_input_text(self.f_type_init)            
                


""" Classes and functions for 2D and 3D matrix/vector math.
    This file defines:
   
"""

    # ~ * :class:`vec2` 2D vector
    # ~ * :class:`vec3` 3D vector
    # ~ * :class:`vec4` 4D vector
    # ~ * :class:`ivec2` 2D integer vector
    # ~ * :class:`mat2` 2x2 matrix
    # ~ * :class:`mat3` 3x3 matrix
    # ~ * :class:`mat4` 4x4 matrix
    # ~ * :meth:`axisRotation`
    # ~ * :meth:`cross`
    # ~ * :meth:`dot`
    # ~ * :meth:`inverse`
    # ~ * :meth:`length`
    # ~ * :meth:`normalize`
    # ~ * :meth:`rotation`
    # ~ * :meth:`rotation2`
    # ~ * :meth:`rotation3`
    # ~ * :meth:`scaling`
    # ~ * :meth:`scaling2`
    # ~ * :meth:`scaling3`
    # ~ * :meth:`translation`
    # ~ * :meth:`translation2`
    # ~ * :meth:`translation3`
    # ~ * :meth:`transpose`
    
# ~ Some of these functions (individually noted) are based on code from TDL.
# ~ The TDL copyright is as follows:
 
# ~ Copyright 2009, Google Inc.
# ~ All rights reserved.

# ~ Redistribution and use in source and binary forms, with or without
# ~ modification, are permitted provided that the following conditions are
# ~ met:

# ~ *  Redistributions of source code must retain the above copyright
# ~ notice, this list of conditions and the following disclaimer.
# ~ *  Redistributions in binary form must reproduce the above
# ~ copyright notice, this list of conditions and the following disclaimer
# ~ in the documentation and/or other materials provided with the
# ~ distribution.
# ~ *  Neither the name of Google Inc. nor the names of its
# ~ contributors may be used to endorse or promote products derived from
# ~ this software without specific prior written permission.

# ~ THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ~ "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# ~ LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# ~ A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# ~ OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# ~ SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# ~ LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# ~ DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# ~ THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# ~ (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# ~ OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import array,math
import typing
from typing import Union, overload, Tuple, Any, List, Sequence, Iterator
import sys

if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 9):
    raise RuntimeError("This file requires Python 3.9 or newer")

__all__ = ["vec2","ivec2","vec3","vec4","mat2","mat3","mat4",
    "dot","cross","length","normalize","transpose",
    "inverse","axisRotation","scaling", "rotation",
    "translation",
    "rotation2","scaling2","translation2",
    "rotation3","scaling3","translation3",
]

class mat4:
    """4x4 matrix. Constructor takes either no arguments or 16 scalars.
        If called with no arguments, initialize the matrix to all zeros. 
        If called with scalars, they are loaded into the matrix, in row-major order.
        
        Example::
        
            M = mat4()
            M = mat4( 1,0,0,0,
                      0,1,0,0,
                      0,0,1,0,
                      0,0,0,1)
    """
        
    @overload
    def __init__(self): pass
    @overload
    def __init__(self, 
        m00: Union[int,float], m01: Union[int,float], m02: Union[int,float], m03: Union[int,float],
        m10: Union[int,float], m11: Union[int,float], m12: Union[int,float], m13: Union[int,float],
        m20: Union[int,float], m21: Union[int,float], m22: Union[int,float], m23: Union[int,float],
        m30: Union[int,float], m31: Union[int,float], m32: Union[int,float], m33: Union[int,float]
    ): pass
    
    def __init__(self,*args):
        
        self.nr=4
        self.nc=4
        if len(args) == 0:
            self._M = array.array("f",[0]*16)
        elif len(args) == 16:
            self._M = array.array("f",args)
        else:
            raise RuntimeError("Bad number of arguments")

    @staticmethod
    def identity() -> "mat4":
        """
            Return the identity matrix. Example::
            
                M = mat4.identity()
                
            Returns:
                :class:`mat4`: Ones on the main diagonal; zeros everywhere else.
        """
        return mat4(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1)
    def __add__(self,m2: "mat4" ) -> "mat4" :
        """
        Return the sum of two matrices. Example (assuming m1 and m2 are both mat4)::
        
            m3 = m1 + m2
        
        Args:
            m2: mat4
        Returns:
            mat4
        """
        if type(self) != type(m2):
            return NotImplemented
        r = type(self)()
        for i in range(len(self._M)):
            r._M[i] = self._M[i] + m2._M[i]
        return r
        
    def __sub__(self,m2: "mat4") -> "mat4" :
        """
        Return the difference of two matrices. Example (assuming m1 and m2 are both mat4)::
        
            m3 = m1 - m2
        
        Args:
            m2: mat4
        Returns:
            mat4
        """
        if type(self) != type(m2):
            return NotImplemented
        r = type(self)()
        for i in range(len(self._M)):
            r._M[i] = self._M[i] - m2._M[i]
        return r
        
    @overload 
    def __mul__(self,o: Union[float,int,"mat4"] ) -> "mat4": pass
    @overload
    def __mul__(self,o: "vec4" ) -> "vec4": pass
    #not annotated since the overloads above handled that
    def __mul__(self,o):
        """
        Return matrix-matrix, matrix-vector, or matrix-scalar product.
        Example (assuming f is a float, m and n are mat4, and v is vec4::
        
            r = m*f     #r is a mat4 (scalar multiplication)
            r = m*v     #r is a vec4 (matrix-vector multiplication)
            r = m*n     #r is a vec4 (matrix-matrix product)
            
        Args:
            o (int, float, :class:`vec4`, :class:`mat4`)
        Returns:
            :class:`vec4` or :class:`mat4`
        """

        if type(o) == type(self):
            #mat * mat
            R=type(self)()
            for i in range(self.nr):
                for j in range(o.nc):
                    total=0
                    for k in range(self.nc):
                        total += self[i][k] * o[k][j]
                    #all matrices are padded to 4 columns
                    R._M[i*4+j] = total
            return R
        
        if type(o) == float or type(o) == int:
            #mat * scalar
            R = type(self)()
            for i in range(len(self._M)):
                R._M[i] = self._M[i] * o
            return R
        
        #mat * vector or mat*list
        if self.nc != len(o):
            return NotImplemented
        R = vec4()
        for i in range(self.nr):
            total=0
            for j in range(self.nc):
                total += self[i][j] * o[j]
            R[i]=total
        return R
        
    @overload 
    def __rmul__(self,o: "mat4" ) -> "mat4" : pass
    @overload 
    def __rmul__(self,o: Union[float,int] ) -> "mat4": pass
    @overload
    def __rmul__(self,o: "vec4" ) -> "vec4": pass
    def __rmul__(self,o):
        """
        Return matrix-matrix, matrix-vector, or matrix-scalar product.
        Example (assuming f is a float, m and n are mat4, and v is vec4::
        
            r = f*m     #r is a mat4 (scalar multiplication)
            r = v*m     #r is a vec4 (matrix-vector multiplication)
            r = n*m     #r is a vec4 (matrix-matrix product)
            
        Args:
            o (int, float, :class:`vec4`, :class:`mat4`)
        Returns:
            :class:`vec4` or :class:`mat4`
        """

        if type(o) == float or type(o) == int:
            return self*o
        else:
            return transpose(self)*o

    def __neg__(self) -> "mat4":
        """
        Return negated matrix. Example::
        
            m2 = -m
            
        Returns:
            :class:`mat4`
        """
        return -1*self

    def __pos__(self) -> "mat4":
        """
        Return copy of matrix. Example::
        
            m2 = +m
            
        Returns:
            :class:`mat4`
        """
        #make a copy
        return 1*self
        
    def tobytes(self) -> bytes:
        """Return byte array for underlying matrix data.
        Returns: 
            bytes 
        """
        return self._M.tobytes()
        
    def __bytes__(self) -> bytes:
        return self.tobytes()
        
    class MatRow:
        def __init__(self,m,i):
            self.m=m
            self.i=i
        def __getitem__(self,j):
            #each row is padded out to be a vec4
            assert j < self.m.nc
            return self.m._M[self.i*4 + j]
        def __setitem__(self,j,v):
            #each row is padded out to be a vec4
            assert j < self.m.nc
            assert type(v) == int or type(v) == float
            self.m._M[self.i*4+j]=v

    @overload
    def __getitem__(self,i: tuple[int,int]) -> float:
        pass
        
    @overload
    def __getitem__(self,i: int) -> "mat4.MatRow":
        pass

    def __getitem__(self,i):
        """ Get matrix item. Indices are always row (first thing) then column.
            Example usage::
            
                q = m[i][j]
                q = m[i,j]
                
            Returns:
                float
        """
        
        if type(i) == int or type(i) == float:
            return mat4.MatRow(self,i)
        else:
            r,c = i
            return self._M[r*4+c]
    
    def __setitem__(self,tpl: tuple[int,int],v: Union[int,float]):
        """ Set matrix item. Indices are always row (first thing) then column.
            Example usage::
            
                m[i][j] = 42
                m[i,j] = 42


        """
        r,c = tpl
        assert type(v) == int or type(v) == float
        self._M[r*4+c] = v
        
    def __eq__(self,o: object) -> bool:
        """
        Return True if two matrices are equal; False otherwise.
        Returns:
            bool
        """
        if type(o) != type(self):
            return False
        o = typing.cast("mat4",o)
        for i in range(len(self._M)):
            if self._M[i] != o._M[i]:
                return False
        return True
        
    def __ne__(self,o: object) -> bool:
        """
        Return True if two matrices are unequal; False otherwise.
        Returns:
            bool
        """

        return not self==o
        
    def __str__(self) -> str:
        """Return printable representation of matrix.
        Returns: str
        """
        s=""
        for i in range(self.nr):
            s += "["
            for j in range(self.nc):
                s += "%-4.6f" % self[i][j]
                s += "   "
            s += "]\n"
        return s
        
    def __repr__(self) -> str:
        """Return printable representation of matrix.
        Returns: str"""
        return str(self)
       
    def transpose(self) -> "mat4" :
        """Return transposed matrix.
        Returns: mat4
        """
        R=type(self)()
        for i in range(self.nr):
            for j in range(self.nc):
                R[i][j] = self[j][i]
        return R

    
class mat3:
    """
        3x3 matrix
        Constructor takes either no arguments or 9 scalars.
        If called with no arguments, initialize the matrix to all zeros. 
        If called with scalars, they are loaded into the matrix, in row-major order.
        
        Example::
        
            M = mat3()
            M = mat3( 1,0,0,
                      0,1,0,
                      0,0,1)
    """    
    @overload
    def __init__(self): pass
    @overload
    def __init__(self, 
        m00: Union[int,float], m01: Union[int,float], m02: Union[int,float], 
        m10: Union[int,float], m11: Union[int,float], m12: Union[int,float], 
        m20: Union[int,float], m21: Union[int,float], m22: Union[int,float]
    ): pass
    
    def __init__(self,*args):
        """Initialize the mat3. If called with no arguments,
        initialize matrix to all zeros. If called with
        arguments, there must be 9 scalars. They are will
        be loaded into the matrix, in row-major order."""
        self.nr=3
        self.nc=3
        if len(args) == 0:
            self._M = array.array("f",[0]*12)
        elif len(args) == 9:
            tmp = [ args[0], args[1], args[2], 0,
                    args[3], args[4], args[5], 0,
                    args[6], args[7], args[8], 0 ]
            self._M = array.array("f",tmp )
        else:
            raise RuntimeError("Bad number of arguments")
        
    @staticmethod
    def identity() -> "mat3":
        """
            Return the identity matrix. Example:
            
                M = mat3.identity()
                
            Returns:
                :class:`mat3`: Ones on the main diagonal; zeros everywhere else.
        """
        return mat3(1,0,0,0,1,0,0,0,1)
    def __add__(self,m2: "mat3" ) -> "mat3" :
        """
        Return the sum of two matrices. Example (assuming m1 and m2 are both mat3)::
        
            m3 = m1 + m2
        
        Args:
            m2: mat3
        Returns:
            mat3
        """
        if type(self) != type(m2):
            return NotImplemented
        r = type(self)()
        for i in range(len(self._M)):
            r._M[i] = self._M[i] + m2._M[i]
        return r
        
    def __sub__(self,m2: "mat3") -> "mat3" :
        """
        Return the difference of two matrices. Example (assuming m1 and m2 are both mat3)::
        
            m3 = m1 - m2
        
        Args:
            m2: mat3
        Returns:
            mat3
        """
        if type(self) != type(m2):
            return NotImplemented
        r = type(self)()
        for i in range(len(self._M)):
            r._M[i] = self._M[i] - m2._M[i]
        return r
        
    @overload 
    def __mul__(self,o: Union[float,int,"mat3"] ) -> "mat3": pass
    @overload
    def __mul__(self,o: "vec3" ) -> "vec3": pass
    #not annotated since the overloads above handled that
    def __mul__(self,o):
        """
        Return matrix-matrix, matrix-vector, or matrix-scalar product.
        Example (assuming f is a float, m and n are mat3, and v is vec3::
        
            r = m*f     #r is a mat3 (scalar multiplication)
            r = m*v     #r is a vec3 (matrix-vector multiplication)
            r = m*n     #r is a vec3 (matrix-matrix product)
            
        Args:
            o (int, float, :class:`vec3`, :class:`mat3`)
        Returns:
            :class:`vec3` or :class:`mat3`
        """

        if type(o) == type(self):
            #mat * mat
            R=type(self)()
            for i in range(self.nr):
                for j in range(o.nc):
                    total=0
                    for k in range(self.nc):
                        total += self[i][k] * o[k][j]
                    #all matrices are padded to 4 columns
                    R._M[i*4+j] = total
            return R
        
        if type(o) == float or type(o) == int:
            #mat * scalar
            R = type(self)()
            for i in range(len(self._M)):
                R._M[i] = self._M[i] * o
            return R
        
        #mat * vector or mat*list
        if self.nc != len(o):
            return NotImplemented
        R = vec3()
        for i in range(self.nr):
            total=0
            for j in range(self.nc):
                total += self[i][j] * o[j]
            R[i]=total
        return R
        
    @overload 
    def __rmul__(self,o: "mat3" ) -> "mat3" : pass
    @overload 
    def __rmul__(self,o: Union[float,int] ) -> "mat3": pass
    @overload
    def __rmul__(self,o: "vec3" ) -> "vec3": pass
    def __rmul__(self,o):
        """
        Return matrix-matrix, matrix-vector, or matrix-scalar product.
        Example (assuming f is a float, m and n are mat3, and v is vec3::
        
            r = f*m     #r is a mat3 (scalar multiplication)
            r = v*m     #r is a vec3 (matrix-vector multiplication)
            r = n*m     #r is a vec3 (matrix-matrix product)
            
        Args:
            o (int, float, :class:`vec3`, :class:`mat3`)
        Returns:
            :class:`vec3` or :class:`mat3`
        """

        if type(o) == float or type(o) == int:
            return self*o
        else:
            return transpose(self)*o

    def __neg__(self) -> "mat3":
        """
        Return negated matrix. Example::
        
            m2 = -m
            
        Returns:
            :class:`mat3`
        """
        return -1*self

    def __pos__(self) -> "mat3":
        """
        Return copy of matrix. Example::
        
            m2 = +m
            
        Returns:
            :class:`mat3`
        """
        #make a copy
        return 1*self
        
    def tobytes(self) -> bytes:
        """Return byte array for underlying matrix data.
        Returns: 
            bytes 
        """
        return self._M.tobytes()
        
    def __bytes__(self) -> bytes:
        return self.tobytes()
        
    class MatRow:
        def __init__(self,m,i):
            self.m=m
            self.i=i
        def __getitem__(self,j):
            #each row is padded out to be a vec4
            assert j < self.m.nc
            return self.m._M[self.i*4 + j]
        def __setitem__(self,j,v):
            #each row is padded out to be a vec4
            assert j < self.m.nc
            assert type(v) == int or type(v) == float
            self.m._M[self.i*4+j]=v

    @overload
    def __getitem__(self,i: tuple[int,int]) -> float:
        pass
        
    @overload
    def __getitem__(self,i: int) -> "mat3.MatRow":
        pass

    def __getitem__(self,i):
        """ Get matrix item. Indices are always row (first thing) then column.
            Example usage::
            
                q = m[i][j]
                q = m[i,j]
                
            Returns:
                float
        """
        
        if type(i) == int or type(i) == float:
            return mat3.MatRow(self,i)
        else:
            r,c = i
            return self._M[r*4+c]
    
    def __setitem__(self,tpl: tuple[int,int],v: Union[int,float]):
        """ Set matrix item. Indices are always row (first thing) then column.
            Example usage::
            
                m[i][j] = 42
                m[i,j] = 42


        """
        r,c = tpl
        assert type(v) == int or type(v) == float
        self._M[r*4+c] = v
        
    def __eq__(self,o: object) -> bool:
        """
        Return True if two matrices are equal; False otherwise.
        Returns:
            bool
        """
        if type(o) != type(self):
            return False
        o = typing.cast("mat3",o)
        for i in range(len(self._M)):
            if self._M[i] != o._M[i]:
                return False
        return True
        
    def __ne__(self,o: object) -> bool:
        """
        Return True if two matrices are unequal; False otherwise.
        Returns:
            bool
        """

        return not self==o
        
    def __str__(self) -> str:
        """Return printable representation of matrix.
        Returns: str
        """
        s=""
        for i in range(self.nr):
            s += "["
            for j in range(self.nc):
                s += "%-4.6f" % self[i][j]
                s += "   "
            s += "]\n"
        return s
        
    def __repr__(self) -> str:
        """Return printable representation of matrix.
        Returns: str"""
        return str(self)
       
    def transpose(self) -> "mat3" :
        """Return transposed matrix.
        Returns: mat3
        """
        R=type(self)()
        for i in range(self.nr):
            for j in range(self.nc):
                R[i][j] = self[j][i]
        return R

class mat2:
    """ 2x2 matrix
        Constructor takes either no arguments or 4 scalars.
        If called with no arguments, initialize the matrix to all zeros. 
        If called with scalars, they are loaded into the matrix, in row-major order.
        
        Example::
        
            M = mat2()
            M = mat2( 1,0,
                      0,1,)
    """
    @overload
    def __init__(self): pass
    @overload
    def __init__(self, 
        m00: Union[int,float], m01: Union[int,float], 
        m10: Union[int,float], m11: Union[int,float] 
    ): pass
    def __init__(self,*args):
        """Initialize the mat2. If called with no arguments,
        initialize matrix to all zeros. If called with
        arguments, there must be 4 scalars. They are will
        be loaded into the matrix, in row-major order."""
        self.nr=2
        self.nc=2
        if len(args) == 0:
            self._M = array.array("f",[0]*8)
        elif len(args) == 4:
            tmp = [args[0],args[1],0,0, args[2],args[3], 0,0 ]
            self._M = array.array("f",tmp)
        else:
            raise RuntimeError("Bad number of arguments")

    @staticmethod
    def identity() -> "mat2":
        """
            Return the identity matrix. Example:
            
                M = mat2.identity()
                
            Returns:
                :class:`mat2`: Ones on the main diagonal; zeros everywhere else.
        """
        return mat2(1,0,0,1)
    def __add__(self,m2: "mat2" ) -> "mat2" :
        """
        Return the sum of two matrices. Example (assuming m1 and m2 are both mat2)::
        
            m3 = m1 + m2
        
        Args:
            m2: mat2
        Returns:
            mat2
        """
        if type(self) != type(m2):
            return NotImplemented
        r = type(self)()
        for i in range(len(self._M)):
            r._M[i] = self._M[i] + m2._M[i]
        return r
        
    def __sub__(self,m2: "mat2") -> "mat2" :
        """
        Return the difference of two matrices. Example (assuming m1 and m2 are both mat2)::
        
            m3 = m1 - m2
        
        Args:
            m2: mat2
        Returns:
            mat2
        """
        if type(self) != type(m2):
            return NotImplemented
        r = type(self)()
        for i in range(len(self._M)):
            r._M[i] = self._M[i] - m2._M[i]
        return r
        
    @overload 
    def __mul__(self,o: Union[float,int,"mat2"] ) -> "mat2": pass
    @overload
    def __mul__(self,o: "vec2" ) -> "vec2": pass
    #not annotated since the overloads above handled that
    def __mul__(self,o):
        """
        Return matrix-matrix, matrix-vector, or matrix-scalar product.
        Example (assuming f is a float, m and n are mat2, and v is vec2::
        
            r = m*f     #r is a mat2 (scalar multiplication)
            r = m*v     #r is a vec2 (matrix-vector multiplication)
            r = m*n     #r is a vec2 (matrix-matrix product)
            
        Args:
            o (int, float, :class:`vec2`, :class:`mat2`)
        Returns:
            :class:`vec2` or :class:`mat2`
        """

        if type(o) == type(self):
            #mat * mat
            R=type(self)()
            for i in range(self.nr):
                for j in range(o.nc):
                    total=0
                    for k in range(self.nc):
                        total += self[i][k] * o[k][j]
                    #all matrices are padded to 4 columns
                    R._M[i*4+j] = total
            return R
        
        if type(o) == float or type(o) == int:
            #mat * scalar
            R = type(self)()
            for i in range(len(self._M)):
                R._M[i] = self._M[i] * o
            return R
        
        #mat * vector or mat*list
        if self.nc != len(o):
            return NotImplemented
        R = vec2()
        for i in range(self.nr):
            total=0
            for j in range(self.nc):
                total += self[i][j] * o[j]
            R[i]=total
        return R
        
    @overload 
    def __rmul__(self,o: "mat2" ) -> "mat2" : pass
    @overload 
    def __rmul__(self,o: Union[float,int] ) -> "mat2": pass
    @overload
    def __rmul__(self,o: "vec2" ) -> "vec2": pass
    def __rmul__(self,o):
        """
        Return matrix-matrix, matrix-vector, or matrix-scalar product.
        Example (assuming f is a float, m and n are mat2, and v is vec2::
        
            r = f*m     #r is a mat2 (scalar multiplication)
            r = v*m     #r is a vec2 (matrix-vector multiplication)
            r = n*m     #r is a vec2 (matrix-matrix product)
            
        Args:
            o (int, float, :class:`vec2`, :class:`mat2`)
        Returns:
            :class:`vec2` or :class:`mat2`
        """

        if type(o) == float or type(o) == int:
            return self*o
        else:
            return transpose(self)*o

    def __neg__(self) -> "mat2":
        """
        Return negated matrix. Example::
        
            m2 = -m
            
        Returns:
            :class:`mat2`
        """
        return -1*self

    def __pos__(self) -> "mat2":
        """
        Return copy of matrix. Example::
        
            m2 = +m
            
        Returns:
            :class:`mat2`
        """
        #make a copy
        return 1*self
        
    def tobytes(self) -> bytes:
        """Return byte array for underlying matrix data.
        Returns: 
            bytes 
        """
        return self._M.tobytes()
        
    def __bytes__(self) -> bytes:
        return self.tobytes()
        
    class MatRow:
        def __init__(self,m,i):
            self.m=m
            self.i=i
        def __getitem__(self,j):
            #each row is padded out to be a vec4
            assert j < self.m.nc
            return self.m._M[self.i*4 + j]
        def __setitem__(self,j,v):
            #each row is padded out to be a vec4
            assert j < self.m.nc
            assert type(v) == int or type(v) == float
            self.m._M[self.i*4+j]=v

    @overload
    def __getitem__(self,i: tuple[int,int]) -> float:
        pass
        
    @overload
    def __getitem__(self,i: int) -> "mat2.MatRow":
        pass

    def __getitem__(self,i):
        """ Get matrix item. Indices are always row (first thing) then column.
            Example usage::
            
                q = m[i][j]
                q = m[i,j]
                
            Returns:
                float
        """
        
        if type(i) == int or type(i) == float:
            return mat2.MatRow(self,i)
        else:
            r,c = i
            return self._M[r*4+c]
    
    def __setitem__(self,tpl: tuple[int,int],v: Union[int,float]):
        """ Set matrix item. Indices are always row (first thing) then column.
            Example usage::
            
                m[i][j] = 42
                m[i,j] = 42


        """
        r,c = tpl
        assert type(v) == int or type(v) == float
        self._M[r*4+c] = v
        
    def __eq__(self,o: object) -> bool:
        """
        Return True if two matrices are equal; False otherwise.
        Returns:
            bool
        """
        if type(o) != type(self):
            return False
        o = typing.cast("mat2",o)
        for i in range(len(self._M)):
            if self._M[i] != o._M[i]:
                return False
        return True
        
    def __ne__(self,o: object) -> bool:
        """
        Return True if two matrices are unequal; False otherwise.
        Returns:
            bool
        """

        return not self==o
        
    def __str__(self) -> str:
        """Return printable representation of matrix.
        Returns: str
        """
        s=""
        for i in range(self.nr):
            s += "["
            for j in range(self.nc):
                s += "%-4.6f" % self[i][j]
                s += "   "
            s += "]\n"
        return s
        
    def __repr__(self) -> str:
        """Return printable representation of matrix.
        Returns: str"""
        return str(self)
       
    def transpose(self) -> "mat2" :
        """Return transposed matrix.
        Returns: mat2
        """
        R=type(self)()
        for i in range(self.nr):
            for j in range(self.nc):
                R[i][j] = self[j][i]
        return R

class vec4:
    """
        4D vector.
        Any number of parameters may be specified in the constructor as long as there
        is a total of 4 data items. Alternately, if no parameters are specified,
        a zero vector is constructed. For example, all of these are valid::
        
            v = vec4()          #same as v=vec4(0,0,0,0)
            v = vec4(1,2,3,0)
            v = vec4( vec3(1,2,3), 1 )
            v = vec4( vec2(1,2), vec2(3,4) )
    """
        
    @overload
    def __init__(self): pass
    @overload
    def __init__(self,x:Union[int,float],y:Union[int,float],z:Union[int,float],w:Union[int,float]): pass
    
    def __init__(self,*args):
        self._v = array.array("f",[0,0,0,0])
        self.construct(args)
    

    
    def construct(self, args: Any):
        if len(args) == 0:
            return
        tmp=[]
        for item in args:
            if type(item) == int or type(item) == float:
                tmp.append(float(item))
            else:
                for q in item:
                    tmp.append(q)
        if len(tmp) != 4:
            raise RuntimeError("Expected "+str(4)+" items for constructor")
        for i in range(4):
            self._v[i] = tmp[i]

    def tobytes(self) -> bytes:
        """
        Return raw byte array for vector data.
        Returns: 
            bytes
        """
        return self._v.tobytes()
    
    def __bytes__(self)-> bytes:
        """
        Return raw byte array for vector data.
        Returns: 
            bytes
        """
        return self.tobytes()
        
    def __getitem__(self,key: int) -> "float":
        """
        Return item from vector. Example:::
           
            y = v[1]
        
        Args:
            key (int): Index of component. x=0, y=1, ...
        Returns:
            The (scalar) value.
        """
        return self._v[key]
            
    def __setitem__(self,key:int,value:Union[int,float]):
        """
        Set item in vector. Example:::
        
            v[1] = 1.2
        
        Args:
            key (int): Index of component. x=0, y=1, ...
        
        """
        self._v[key]=float(value)
        
    def __str__(self) -> str:
        """Return printable representation of vector.
        Returns: str"""
        return "vec{}({})".format(len(self), ",".join([str(q) for q in self._v]))
        
    def copy(self) -> "vec4":
        """
        Return a copy of this vector.
        Returns: vec4
        """
        return 1*self
        
    def __repr__(self) -> str:
        """Return printable representation of vector.
        Returns: str"""
        return str(self)
      
    def __len__(self) -> int:
        """Return number of components in the :class:`vec4`.
           This is always 4.
        """
        return len(self._v)

    def __add__(self,o: "vec4") -> "vec4":
        """
        Vector addition. Example (assuming v and w are two vec4's)::
        
            s = v + w
            
        Args:
            o: :class:`vec4`
        Returns:
            :class:`vec4`
        """
        if len(self) != len(o):
            raise ValueError("Dimension mismatch")
        L=type(self)()
        for i in range(len(self._v)):
            L._v[i] =  self._v[i]+o[i]
        return L

    def __sub__(self,o:"vec4") -> "vec4":
        """
        Vector subtraction. Example (assuming v and w are two vec4's)::
        
            s = v - w
            
        Args:
            o: :class:`vec4`
        Returns:
            :class:`vec4`
        """
        L=type(self)()
        if len(self) != len(o):
            return NotImplemented
        for i in range(len(self._v)):
            L._v[i] =  self._v[i]-o[i]
        return L

    @overload
    def __mul__(self,o: "mat4") -> "vec4" : pass
    @overload
    def __mul__(self,o: "vec4") -> "vec4" : pass
    @overload
    def __mul__(self,o: Union[float,int]) -> "vec4" : pass
    
    def __mul__(self,o):
        """
        Vector multiplication. Example (assuming f is a float, m is a mat4, and v and w are two vec4's)::
        
            r = v*f     #r is a vec4 (scalar multiplication)
            r = v*m     #r is a mat4 (vector-matrix multiplication)
            r = v*w     #r is a vec4 (component-wise or Hadamard product)
            
        Args:
            o (int, float, :class:`vec4`, :class:`mat4`)
        Returns:
            :class:`vec4` or :class:`mat4`
        """
        if isinstance(o,mat4):
            if len(self) != o.nr:
                return NotImplemented
            R=type(self)()
            for i in range(o.nc):
                total=0
                for j in range(len(self)):
                    total += self[j]*o[j][i]
                R[i]=total
            return R
        elif type(o) == float or type(o) == int:
            R=type(self)()
            for i in range(len(self)):
                R[i] = self._v[i]*o
            return R
        elif type(o) == vec4: #len(o) == len(self):
            #component-wise multiply (Hadamard product)
            R=type(self)()
            for i in range(len(self)):
                R[i] = self[i]*o[i]
            return R
        else:
            return NotImplemented
    
    @overload
    def __rmul__(self,o: "mat4") -> "vec4" : pass
    @overload
    def __rmul__(self,o: "vec4") -> "vec4" : pass
    @overload
    def __rmul__(self,o: Union[float,int]) -> "vec4" : pass
    
    def __rmul__(self,o):
        """
        Vector multiplication. Example (assuming f is a float, m is a mat4, and v and w are two vec4's)::
        
            r = f*v     #r is a vec4 (scalar multiplication)
            r = m*v     #r is a mat4 (matrix-vector multiplication)
            r = v*w     #r is a vec4 (component-wise or Hadamard product)
            
        Args:
            o (int, float, :class:`vec4`, :class:`mat4`)
        Returns:
            :class:`vec4` or :class:`mat4`

        """
        return self.__mul__(o)


    def __neg__(self) -> "vec4":
        """
        Return negated copy of vec4. Example::
        
            w = -v
            
        Returns:
            vec4
        """
        return -1*self

    def __pos__(self) -> "vec4":
        """
        Return copy of vec4. Example::
            
            w = +v
            
        Returns:
            vec4
        """
        return 1*self
     
    def __iter__(self) -> Iterator[float]:
        return self._v.__iter__()
      
    def __eq__(self,o: object) -> bool:
        """
        Test for equality. Ex::
        
            v == w
        
        Args:
            o (object)
        Returns:
            bool
        """

        if type(o) != type(self):
            return False
        o = typing.cast("vec4",o)
        for i in range(len(self._v)):
            if self._v[i] != o[i]:
                return False
        return True
        
    def __ne__(self,o: object)->bool:
        """
        Test for inequality. Ex::
        
            v = w
        
        Args:
            o (object)
        Returns:
            bool
        """
        return not self==o
    
    def _getmagnitude(self) -> float:
        return length(self)
    magnitude = property( _getmagnitude, None )     #: length of vector
    
    def _getmagnitudeSq(self) -> float:       
        return dot(self,self)
    magnitudeSq = property( _getmagnitudeSq, None ) #: squared length of vector. Faster to compute than actual length.
    
    def _isZero(self) -> bool:
        return dot(self,self) == 0
    isZero = property(_isZero,None)         #: True if all components of vector are zero.

    
    def _getnormalized(self) -> "vec4":
        return normalize(self)
    normalized = property(_getnormalized,None)      #: Unit length copy of vector
    


    def _getx(self) -> float:
        return self._v[ 0 ]
    def _setx(self,v: Union[float,int]):
        self._v[ 0 ]=float(v)
    def _gety(self) -> float:
        return self._v[ 1 ]
    def _sety(self,v:  Union[float,int]):
        self._v[ 1 ]=v
    def _getxy(self) -> "vec2":           
        return vec2(self._v[0],self._v[1])
    def _setxy(self,v: "vec2"):         
        self._v[0]=v[0]; self._v[1]=v[1]
    x = property(_getx , _setx )        #: Get the x coordinate
    y = property(_gety , _sety )        #: Get the y coordinate
    xy = property(_getxy , _setxy )     #: Get a vec2 consisting of the x and y coordinates
    

    def _getz(self) -> float:            
        return self._v[ 2 ]
    def _setz(self,v: Union[float,int]):          
        self._v[ 2 ]=v
    def _getxyz(self) -> "vec3":          
        return vec3(self._v[0],self._v[1],self._v[2])
    def _setxyz(self,v: "vec3"):        
        self._v[0]=v[0]; self._v[1]=v[1]; self._v[2]=v[2]
    z = property(_getz , _setz )        #: Get the z coordinate
    xyz = property(_getxyz , _setxyz )  #: Get a vec3 consisting of the x, y, and z coordinates

    def _getw(self)-> float:            
        return self._v[ 3 ]
    def _setw(self,v: Union[float,int]):          
        self._v[ 3 ]=v
    def _getxyzw(self) -> "vec4":         
        return vec4(self._v[0],self._v[1],self._v[2],self._v[3])
    def _setxyzw(self,v: "vec4"):       
        self._v[0]=v[0]; self._v[1]=v[1]; self._v[2]=v[2]; self._v[3]=v[3]
    w = property(_getw , _setw )        #: Get the w coordinate
    xyzw = property(_getxyzw , _setxyzw )   #: Get a vec4 consisting of the x, y, z, and w coordinates

class vec3:
    """
        3D vector.
        Any number of parameters may be specified in the constructor as long as there
        is a total of 3 data items. Alternately, if no parameters are specified,
        a zero vector is constructed. For example, all of these are valid::
        
            v = vec3()          #same as v=vec3(0,0,0)
            v = vec3(1,2,3)
            v = vec3( vec2(1,2), 1 )
    """
    
    @overload
    def __init__(self): pass
    @overload
    def __init__(self,x:Union[int,float],y:Union[int,float],z:Union[int,float]): pass
    
    def __init__(self,*args):
        self._v = array.array("f",[0,0,0])
        self.construct(args)
    
    
    def construct(self, args: Any):
        if len(args) == 0:
            return
        tmp=[]
        for item in args:
            if type(item) == int or type(item) == float:
                tmp.append(float(item))
            else:
                for q in item:
                    tmp.append(q)
        if len(tmp) != 3:
            raise RuntimeError("Expected "+str(3)+" items for constructor")
        for i in range(3):
            self._v[i] = tmp[i]

    def tobytes(self) -> bytes:
        """
        Return raw byte array for vector data.
        Returns: 
            bytes
        """
        return self._v.tobytes()
    
    def __bytes__(self)-> bytes:
        """
        Return raw byte array for vector data.
        Returns: 
            bytes
        """
        return self.tobytes()
        
    def __getitem__(self,key: int) -> "float":
        """
        Return item from vector. Example:::
           
            y = v[1]
        
        Args:
            key (int): Index of component. x=0, y=1, ...
        Returns:
            The (scalar) value.
        """
        return self._v[key]
            
    def __setitem__(self,key:int,value:Union[int,float]):
        """
        Set item in vector. Example:::
        
            v[1] = 1.2
        
        Args:
            key (int): Index of component. x=0, y=1, ...
        
        """
        self._v[key]=float(value)
        
    def __str__(self) -> str:
        """Return printable representation of vector.
        Returns: str"""
        return "vec{}({})".format(len(self), ",".join([str(q) for q in self._v]))
        
    def copy(self) -> "vec3":
        """
        Return a copy of this vector.
        Returns: vec3
        """
        return 1*self
        
    def __repr__(self) -> str:
        """Return printable representation of vector.
        Returns: str"""
        return str(self)
      
    def __len__(self) -> int:
        """Return number of components in the :class:`vec3`.
           This is always 3.
        """
        return len(self._v)

    def __add__(self,o: "vec3") -> "vec3":
        """
        Vector addition. Example (assuming v and w are two vec3's)::
        
            s = v + w
            
        Args:
            o: :class:`vec3`
        Returns:
            :class:`vec3`
        """
        if len(self) != len(o):
            raise ValueError("Dimension mismatch")
        L=type(self)()
        for i in range(len(self._v)):
            L._v[i] =  self._v[i]+o[i]
        return L

    def __sub__(self,o:"vec3") -> "vec3":
        """
        Vector subtraction. Example (assuming v and w are two vec3's)::
        
            s = v - w
            
        Args:
            o: :class:`vec3`
        Returns:
            :class:`vec3`
        """
        L=type(self)()
        if len(self) != len(o):
            return NotImplemented
        for i in range(len(self._v)):
            L._v[i] =  self._v[i]-o[i]
        return L

    @overload
    def __mul__(self,o: "mat3") -> "vec3" : pass
    @overload
    def __mul__(self,o: "vec3") -> "vec3" : pass
    @overload
    def __mul__(self,o: Union[float,int]) -> "vec3" : pass
    
    def __mul__(self,o):
        """
        Vector multiplication. Example (assuming f is a float, m is a mat3, and v and w are two vec3's)::
        
            r = v*f     #r is a vec3 (scalar multiplication)
            r = v*m     #r is a mat3 (vector-matrix multiplication)
            r = v*w     #r is a vec3 (component-wise or Hadamard product)
            
        Args:
            o (int, float, :class:`vec3`, :class:`mat3`)
        Returns:
            :class:`vec3` or :class:`mat3`
        """
        if isinstance(o,mat3):
            if len(self) != o.nr:
                return NotImplemented
            R=type(self)()
            for i in range(o.nc):
                total=0
                for j in range(len(self)):
                    total += self[j]*o[j][i]
                R[i]=total
            return R
        elif type(o) == float or type(o) == int:
            R=type(self)()
            for i in range(len(self)):
                R[i] = self._v[i]*o
            return R
        elif type(o) == vec3: #len(o) == len(self):
            #component-wise multiply (Hadamard product)
            R=type(self)()
            for i in range(len(self)):
                R[i] = self[i]*o[i]
            return R
        else:
            return NotImplemented
    
    @overload
    def __rmul__(self,o: "mat3") -> "vec3" : pass
    @overload
    def __rmul__(self,o: "vec3") -> "vec3" : pass
    @overload
    def __rmul__(self,o: Union[float,int]) -> "vec3" : pass
    
    def __rmul__(self,o):
        """
        Vector multiplication. Example (assuming f is a float, m is a mat3, and v and w are two vec3's)::
        
            r = f*v     #r is a vec3 (scalar multiplication)
            r = m*v     #r is a mat3 (matrix-vector multiplication)
            r = v*w     #r is a vec3 (component-wise or Hadamard product)
            
        Args:
            o (int, float, :class:`vec3`, :class:`mat3`)
        Returns:
            :class:`vec3` or :class:`mat3`

        """
        return self.__mul__(o)


    def __neg__(self) -> "vec3":
        """
        Return negated copy of vec3. Example::
        
            w = -v
            
        Returns:
            vec3
        """
        return -1*self

    def __pos__(self) -> "vec3":
        """
        Return copy of vec3. Example::
            
            w = +v
            
        Returns:
            vec3
        """
        return 1*self
     
    def __iter__(self) -> Iterator[float]:
        return self._v.__iter__()
      
    def __eq__(self,o: object) -> bool:
        """
        Test for equality. Ex::
        
            v == w
        
        Args:
            o (object)
        Returns:
            bool
        """

        if type(o) != type(self):
            return False
        o = typing.cast("vec3",o)
        for i in range(len(self._v)):
            if self._v[i] != o[i]:
                return False
        return True
        
    def __ne__(self,o: object)->bool:
        """
        Test for inequality. Ex::
        
            v = w
        
        Args:
            o (object)
        Returns:
            bool
        """
        return not self==o
    
    def _getmagnitude(self) -> float:
        return length(self)
    magnitude = property( _getmagnitude, None )     #: length of vector
    
    def _getmagnitudeSq(self) -> float:       
        return dot(self,self)
    magnitudeSq = property( _getmagnitudeSq, None ) #: squared length of vector. Faster to compute than actual length.
    
    def _isZero(self) -> bool:
        return dot(self,self) == 0
    isZero = property(_isZero,None)         #: True if all components of vector are zero.

    
    def _getnormalized(self) -> "vec3":
        return normalize(self)
    normalized = property(_getnormalized,None)      #: Unit length copy of vector
    


    def _getx(self) -> float:
        return self._v[ 0 ]
    def _setx(self,v: Union[float,int]):
        self._v[ 0 ]=float(v)
    def _gety(self) -> float:
        return self._v[ 1 ]
    def _sety(self,v:  Union[float,int]):
        self._v[ 1 ]=v
    def _getxy(self) -> "vec2":           
        return vec2(self._v[0],self._v[1])
    def _setxy(self,v: "vec2"):         
        self._v[0]=v[0]; self._v[1]=v[1]
    x = property(_getx , _setx )        #: Get the x coordinate
    y = property(_gety , _sety )        #: Get the y coordinate
    xy = property(_getxy , _setxy )     #: Get a vec2 consisting of the x and y coordinates
    

    def _getz(self) -> float:            
        return self._v[ 2 ]
    def _setz(self,v: Union[float,int]):          
        self._v[ 2 ]=v
    def _getxyz(self) -> "vec3":          
        return vec3(self._v[0],self._v[1],self._v[2])
    def _setxyz(self,v: "vec3"):        
        self._v[0]=v[0]; self._v[1]=v[1]; self._v[2]=v[2]
    z = property(_getz , _setz )        #: Get the z coordinate
    xyz = property(_getxyz , _setxyz )  #: Get a vec3 consisting of the x, y, and z coordinates

class vec2:
    """
        2D vector.
        Any number of parameters may be specified in the constructor as long as there
        is a total of 2 data items. Alternately, if no parameters are specified,
        a zero vector is constructed. For example, all of these are valid::
        
            v = vec2()          #same as v=vec2(0,0)
            v = vec2(1,2)
            v = vec2( vec2(1,2) )
    """
    
    @overload
    def __init__(self): pass
    @overload
    def __init__(self,x:Union[int,float],y:Union[int,float]): pass
    
    def __init__(self,*args):
        """
        """
        
        self._v = array.array("f",[0,0])
        self.construct(args)
        
    def _radians(self) -> float:
        """Returns the angle (in radians) between this vector and the vector (1,0).
            Angles are between -π and π. Positive angles are measured counterclockwise.
        """
        return math.atan2(self.y,self.x)
    def _degrees(self) -> float:
        """Returns the angle (in degrees) between this vector and the vector (1,0).
        Angles are between -π and π. Positive angles are measured counterclockwise.
        """
        return 180*math.atan2(self.y,self.x)/math.pi
    radians = property(_radians,None)
    degrees = property(_degrees,None)

    
    
    def construct(self, args: Any):
        if len(args) == 0:
            return
        tmp=[]
        for item in args:
            if type(item) == int or type(item) == float:
                tmp.append(float(item))
            else:
                for q in item:
                    tmp.append(q)
        if len(tmp) != 2:
            raise RuntimeError("Expected "+str(2)+" items for constructor")
        for i in range(2):
            self._v[i] = tmp[i]

    def tobytes(self) -> bytes:
        """
        Return raw byte array for vector data.
        Returns: 
            bytes
        """
        return self._v.tobytes()
    
    def __bytes__(self)-> bytes:
        """
        Return raw byte array for vector data.
        Returns: 
            bytes
        """
        return self.tobytes()
        
    def __getitem__(self,key: int) -> "float":
        """
        Return item from vector. Example:::
           
            y = v[1]
        
        Args:
            key (int): Index of component. x=0, y=1, ...
        Returns:
            The (scalar) value.
        """
        return self._v[key]
            
    def __setitem__(self,key:int,value:Union[int,float]):
        """
        Set item in vector. Example:::
        
            v[1] = 1.2
        
        Args:
            key (int): Index of component. x=0, y=1, ...
        
        """
        self._v[key]=float(value)
        
    def __str__(self) -> str:
        """Return printable representation of vector.
        Returns: str"""
        return "vec{}({})".format(len(self), ",".join([str(q) for q in self._v]))
        
    def copy(self) -> "vec2":
        """
        Return a copy of this vector.
        Returns: vec2
        """
        return 1*self
        
    def __repr__(self) -> str:
        """Return printable representation of vector.
        Returns: str"""
        return str(self)
      
    def __len__(self) -> int:
        """Return number of components in the :class:`vec2`.
           This is always 2.
        """
        return len(self._v)

    def __add__(self,o: "vec2") -> "vec2":
        """
        Vector addition. Example (assuming v and w are two vec2's)::
        
            s = v + w
            
        Args:
            o: :class:`vec2`
        Returns:
            :class:`vec2`
        """
        if len(self) != len(o):
            raise ValueError("Dimension mismatch")
        L=type(self)()
        for i in range(len(self._v)):
            L._v[i] =  self._v[i]+o[i]
        return L

    def __sub__(self,o:"vec2") -> "vec2":
        """
        Vector subtraction. Example (assuming v and w are two vec2's)::
        
            s = v - w
            
        Args:
            o: :class:`vec2`
        Returns:
            :class:`vec2`
        """
        L=type(self)()
        if len(self) != len(o):
            return NotImplemented
        for i in range(len(self._v)):
            L._v[i] =  self._v[i]-o[i]
        return L

    @overload
    def __mul__(self,o: "mat2") -> "vec2" : pass
    @overload
    def __mul__(self,o: "vec2") -> "vec2" : pass
    @overload
    def __mul__(self,o: Union[float,int]) -> "vec2" : pass
    
    def __mul__(self,o):
        """
        Vector multiplication. Example (assuming f is a float, m is a mat2, and v and w are two vec2's)::
        
            r = v*f     #r is a vec2 (scalar multiplication)
            r = v*m     #r is a mat2 (vector-matrix multiplication)
            r = v*w     #r is a vec2 (component-wise or Hadamard product)
            
        Args:
            o (int, float, :class:`vec2`, :class:`mat2`)
        Returns:
            :class:`vec2` or :class:`mat2`
        """
        if isinstance(o,mat2):
            if len(self) != o.nr:
                return NotImplemented
            R=type(self)()
            for i in range(o.nc):
                total=0
                for j in range(len(self)):
                    total += self[j]*o[j][i]
                R[i]=total
            return R
        elif type(o) == float or type(o) == int:
            R=type(self)()
            for i in range(len(self)):
                R[i] = self._v[i]*o
            return R
        elif type(o) == vec2: #len(o) == len(self):
            #component-wise multiply (Hadamard product)
            R=type(self)()
            for i in range(len(self)):
                R[i] = self[i]*o[i]
            return R
        else:
            return NotImplemented
    
    @overload
    def __rmul__(self,o: "mat2") -> "vec2" : pass
    @overload
    def __rmul__(self,o: "vec2") -> "vec2" : pass
    @overload
    def __rmul__(self,o: Union[float,int]) -> "vec2" : pass
    
    def __rmul__(self,o):
        """
        Vector multiplication. Example (assuming f is a float, m is a mat2, and v and w are two vec2's)::
        
            r = f*v     #r is a vec2 (scalar multiplication)
            r = m*v     #r is a mat2 (matrix-vector multiplication)
            r = v*w     #r is a vec2 (component-wise or Hadamard product)
            
        Args:
            o (int, float, :class:`vec2`, :class:`mat2`)
        Returns:
            :class:`vec2` or :class:`mat2`

        """
        return self.__mul__(o)


    def __neg__(self) -> "vec2":
        """
        Return negated copy of vec2. Example::
        
            w = -v
            
        Returns:
            vec2
        """
        return -1*self

    def __pos__(self) -> "vec2":
        """
        Return copy of vec2. Example::
            
            w = +v
            
        Returns:
            vec2
        """
        return 1*self
     
    def __iter__(self) -> Iterator[float]:
        return self._v.__iter__()
      
    def __eq__(self,o: object) -> bool:
        """
        Test for equality. Ex::
        
            v == w
        
        Args:
            o (object)
        Returns:
            bool
        """

        if type(o) != type(self):
            return False
        o = typing.cast("vec2",o)
        for i in range(len(self._v)):
            if self._v[i] != o[i]:
                return False
        return True
        
    def __ne__(self,o: object)->bool:
        """
        Test for inequality. Ex::
        
            v = w
        
        Args:
            o (object)
        Returns:
            bool
        """
        return not self==o
    
    def _getmagnitude(self) -> float:
        return length(self)
    magnitude = property( _getmagnitude, None )     #: length of vector
    
    def _getmagnitudeSq(self) -> float:       
        return dot(self,self)
    magnitudeSq = property( _getmagnitudeSq, None ) #: squared length of vector. Faster to compute than actual length.
    
    def _isZero(self) -> bool:
        return dot(self,self) == 0
    isZero = property(_isZero,None)         #: True if all components of vector are zero.

    
    def _getnormalized(self) -> "vec2":
        return normalize(self)
    normalized = property(_getnormalized,None)      #: Unit length copy of vector
    


    def _getx(self) -> float:
        return self._v[ 0 ]
    def _setx(self,v: Union[float,int]):
        self._v[ 0 ]=float(v)
    def _gety(self) -> float:
        return self._v[ 1 ]
    def _sety(self,v:  Union[float,int]):
        self._v[ 1 ]=v
    def _getxy(self) -> "vec2":           
        return vec2(self._v[0],self._v[1])
    def _setxy(self,v: "vec2"):         
        self._v[0]=v[0]; self._v[1]=v[1]
    x = property(_getx , _setx )        #: Get the x coordinate
    y = property(_gety , _sety )        #: Get the y coordinate
    xy = property(_getxy , _setxy )     #: Get a vec2 consisting of the x and y coordinates
    

class ivec2:
    """
        2D integer vector.
        Any number of items may be specified in the constructor as long as there
        are 2 data items. Alternately, if no parameters are specified,
        a zero vector is constructed. For example, all of these are valid::
        
            v = ivec2()
            v = ivec2(1,2)
            v = ivec2( ivec2(1,2) )
    """
    
    @overload
    def __init__(self): pass
    @overload
    def __init__(self,x:Union[int,float],y:Union[int,float]): pass
    
    def __init__(self,*args):
        self._v = array.array("i",[0,0])
        self.construct(args)
    
    def construct(self, args: Any):
        if len(args) == 0:
            return
        tmp=[]
        for item in args:
            if type(item) == int or type(item) == float:
                tmp.append(float(item))
            else:
                for q in item:
                    tmp.append(q)
        if len(tmp) != 2:
            raise RuntimeError("Expected "+str(2)+" items for constructor")
        for i in range(2):
            self._v[i] = tmp[i]

    def tobytes(self) -> bytes:
        """
        Return raw byte array for vector data.
        Returns: 
            bytes
        """
        return self._v.tobytes()
    
    def __bytes__(self)-> bytes:
        """
        Return raw byte array for vector data.
        Returns: 
            bytes
        """
        return self.tobytes()
        
    def __getitem__(self,key: int) -> "int":
        """
        Return item from vector. Example:::
           
            y = v[1]
        
        Args:
            key (int): Index of component. x=0, y=1, ...
        Returns:
            The (scalar) value.
        """
        return self._v[key]
            
    def __setitem__(self,key:int,value:Union[int,float]):
        """
        Set item in vector. Example:::
        
            v[1] = 1.2
        
        Args:
            key (int): Index of component. x=0, y=1, ...
        
        """
        self._v[key]=int(value)
        
    def __str__(self) -> str:
        """Return printable representation of vector.
        Returns: str"""
        return "vec{}({})".format(len(self), ",".join([str(q) for q in self._v]))
        
    def copy(self) -> "ivec2":
        """
        Return a copy of this vector.
        Returns: ivec2
        """
        return 1*self
        
    def __repr__(self) -> str:
        """Return printable representation of vector.
        Returns: str"""
        return str(self)
      
    def __len__(self) -> int:
        """Return number of components in the :class:`ivec2`.
           This is always 2.
        """
        return len(self._v)

    def __add__(self,o: "ivec2") -> "ivec2":
        """
        Vector addition. Example (assuming v and w are two ivec2's)::
        
            s = v + w
            
        Args:
            o: :class:`ivec2`
        Returns:
            :class:`ivec2`
        """
        if len(self) != len(o):
            raise ValueError("Dimension mismatch")
        L=type(self)()
        for i in range(len(self._v)):
            L._v[i] =  self._v[i]+o[i]
        return L

    def __sub__(self,o:"ivec2") -> "ivec2":
        """
        Vector subtraction. Example (assuming v and w are two ivec2's)::
        
            s = v - w
            
        Args:
            o: :class:`ivec2`
        Returns:
            :class:`ivec2`
        """
        L=type(self)()
        if len(self) != len(o):
            return NotImplemented
        for i in range(len(self._v)):
            L._v[i] =  self._v[i]-o[i]
        return L

    @overload
    def __mul__(self,o: "mat2") -> "ivec2" : pass
    @overload
    def __mul__(self,o: "ivec2") -> "ivec2" : pass
    @overload
    def __mul__(self,o: Union[float,int]) -> "ivec2" : pass
    
    def __mul__(self,o):
        """
        Vector multiplication. Example (assuming f is a float, m is a mat2, and v and w are two ivec2's)::
        
            r = v*f     #r is a ivec2 (scalar multiplication)
            r = v*m     #r is a mat2 (vector-matrix multiplication)
            r = v*w     #r is a ivec2 (component-wise or Hadamard product)
            
        Args:
            o (int, float, :class:`ivec2`, :class:`mat2`)
        Returns:
            :class:`ivec2` or :class:`mat2`
        """
        if isinstance(o,mat2):
            if len(self) != o.nr:
                return NotImplemented
            R=type(self)()
            for i in range(o.nc):
                total=0
                for j in range(len(self)):
                    total += self[j]*o[j][i]
                R[i]=total
            return R
        elif type(o) == float or type(o) == int:
            R=type(self)()
            for i in range(len(self)):
                R[i] = self._v[i]*o
            return R
        elif type(o) == ivec2: #len(o) == len(self):
            #component-wise multiply (Hadamard product)
            R=type(self)()
            for i in range(len(self)):
                R[i] = self[i]*o[i]
            return R
        else:
            return NotImplemented
    
    @overload
    def __rmul__(self,o: "mat2") -> "ivec2" : pass
    @overload
    def __rmul__(self,o: "ivec2") -> "ivec2" : pass
    @overload
    def __rmul__(self,o: Union[float,int]) -> "ivec2" : pass
    
    def __rmul__(self,o):
        """
        Vector multiplication. Example (assuming f is a float, m is a mat2, and v and w are two ivec2's)::
        
            r = f*v     #r is a ivec2 (scalar multiplication)
            r = m*v     #r is a mat2 (matrix-vector multiplication)
            r = v*w     #r is a ivec2 (component-wise or Hadamard product)
            
        Args:
            o (int, float, :class:`ivec2`, :class:`mat2`)
        Returns:
            :class:`ivec2` or :class:`mat2`

        """
        return self.__mul__(o)


    def __neg__(self) -> "ivec2":
        """
        Return negated copy of ivec2. Example::
        
            w = -v
            
        Returns:
            ivec2
        """
        return -1*self

    def __pos__(self) -> "ivec2":
        """
        Return copy of ivec2. Example::
            
            w = +v
            
        Returns:
            ivec2
        """
        return 1*self
     
    def __iter__(self) -> Iterator[float]:
        return self._v.__iter__()
      
    def __eq__(self,o: object) -> bool:
        """
        Test for equality. Ex::
        
            v == w
        
        Args:
            o (object)
        Returns:
            bool
        """

        if type(o) != type(self):
            return False
        o = typing.cast("ivec2",o)
        for i in range(len(self._v)):
            if self._v[i] != o[i]:
                return False
        return True
        
    def __ne__(self,o: object)->bool:
        """
        Test for inequality. Ex::
        
            v = w
        
        Args:
            o (object)
        Returns:
            bool
        """
        return not self==o
    
    def _getmagnitude(self) -> float:
        return length(self)
    magnitude = property( _getmagnitude, None )     #: length of vector
    
    def _getmagnitudeSq(self) -> float:       
        return dot(self,self)
    magnitudeSq = property( _getmagnitudeSq, None ) #: squared length of vector. Faster to compute than actual length.
    
    def _isZero(self) -> bool:
        return dot(self,self) == 0
    isZero = property(_isZero,None)         #: True if all components of vector are zero.

    


    def _getx(self) -> float:
        return self._v[ 0 ]
    def _setx(self,v: Union[float,int]):
        self._v[ 0 ]=float(v)
    def _gety(self) -> float:
        return self._v[ 1 ]
    def _sety(self,v:  Union[float,int]):
        self._v[ 1 ]=v
    def _getxy(self) -> "vec2":           
        return vec2(self._v[0],self._v[1])
    def _setxy(self,v: "vec2"):         
        self._v[0]=v[0]; self._v[1]=v[1]
    x = property(_getx , _setx )        #: Get the x coordinate
    y = property(_gety , _sety )        #: Get the y coordinate
    xy = property(_getxy , _setxy )     #: Get a vec2 consisting of the x and y coordinates
    

        
@overload
def dot(v: vec2, w: vec2) -> float: pass
@overload
def dot(v: vec3, w: vec3) -> float: pass
@overload
def dot(v: vec4, w: vec4) -> float: pass
@overload
def dot(v: ivec2, w: ivec2) -> float: pass

def dot(v,w):
    """
    Return vector dot product.
    Args:
        v (vec2, vec3, or vec4)
        w (vec2, vec3, or vec4)
    Returns:
        float
    """
    assert len(v) == len(w)
    return sum( [v[i]*w[i] for i in range(len(v)) ] )
    
@overload
def cross(v:vec3,w:vec3) -> vec3: pass
@overload
def cross(v:vec4,w:vec4) -> vec4: pass
def cross(v,w):
    """
    Return vector cross product. Note that the arguments
    must both be vec3 or else both be vec4.
    Args:
        v (vec3 or vec4): If a vec4, w is ignored.
        w (vec3 or vec4): If a vec4, w is ignored.
    Returns:
        vec3 or vec4, depending on the type of the arguments.
        
    @type v: vec3, vec4 (w is ignored), or list of scalar
    @type w: vec3, vec4 (w is ignored), or list of scalar
    """
    if type(v) != type(w):
        raise RuntimeError("Type mismatch: Arguments to cross() must be the same type")
    if type(v) == vec3:
        return vec3(
            v[1]*w[2] - w[1]*v[2],
            w[0]*v[2] - v[0]*w[2],
            v[0]*w[1] - w[0]*v[1]
        )
    elif type(v) == vec4:
        return vec4(
            v[1]*w[2] - w[1]*v[2],
            w[0]*v[2] - v[0]*w[2],
            v[0]*w[1] - w[0]*v[1],
            0
        )
    else:
        raise RuntimeError("Bad types for cross(): Must be vec3 or vec4: Got {} and {}".format(type(v),type(w)))

@overload
def length(v:vec2) -> float : pass
@overload
def length(v:vec3) -> float : pass
@overload
def length(v:vec4) -> float : pass
@overload
def length(v:ivec2) -> float : pass

def length(v):
    """
    Return length of the vector.
    Args:
        v (vec2, vec3, or vec4)
    Returns:
        float
    """
    return dot(v,v)**0.5
   
@overload
def normalize(v:vec2) -> vec2: pass
@overload
def normalize(v:vec3) -> vec3: pass
@overload
def normalize(v:vec4) -> vec4: pass

def normalize(v):
    """Return normalized (unit length) copy of the vector.
    Args:
        v (vec2, vec3, or vec4)
    Returns:
        Same type as input argument
    """
    L=len(v)
    le=1/length(v)
    return le*v
@overload
def transpose(v:mat2) -> mat2: pass
@overload
def transpose(v:mat3) -> mat3: pass
@overload
def transpose(v:mat4) -> mat4: pass

def transpose(m):
    """
    Returns transposed copy of the matrix.
    Args:
        m: mat2, mat3, or mat4
    Returns:
        Same type as input
    """
    return m.transpose()

def rotation3(axis: Union[vec3,vec4,List[float]],angle: Union[float,int]) -> mat4:
    """
    Compute 3D rotation matrix.
    Args:
        axis (vec3 or vec4): Axis of rotation. Must be unit length.
        angle (float): Angle, in radians.
    Returns:
        :class:`mat4`
    """
    return axisRotation(axis,angle)
    
def rotation(axis: Union[vec3,vec4,List[float]],angle: Union[float,int]) -> mat4:
    """
    Compute 3D rotation matrix.
    Args:
        axis (vec3 or vec4): Axis of rotation. Must be unit length.
        angle (float): Angle, in radians.
    Returns:
        :class:`mat4`
    """
    return axisRotation(axis,angle)
    
def axisRotation(axis:Union[vec3,vec4,List[float]],angle: Union[float,int]) -> mat4:
    """
    Compute 3D rotation matrix.
    Args:
        axis (vec3 or vec4): Axis of rotation. Must be unit length.
        angle (float): Angle, in radians.
    Returns:
        :class:`mat4`
    """
    #code is from TDL.
    #axis=normalize(axis)
    x = axis[0]
    y = axis[1]
    z = axis[2]
    xx = x * x
    yy = y * y
    zz = z * z
    c = math.cos(angle)
    s = math.sin(angle)
    oneMinusCosine = 1 - c
    zs = z*s
    xs = x*s
    ys = y*s
    xy = x*y
    xz = x*z
    yz = y*z
    return mat4(
        xx + (1 - xx) * c,
        xy * oneMinusCosine + zs,
        xz * oneMinusCosine - ys,
        0,
        xy * oneMinusCosine - zs,
        yy + (1 - yy) * c,
        yz * oneMinusCosine + xs,
        0,
        xz * oneMinusCosine + ys,
        yz * oneMinusCosine - xs,
        zz + (1 - zz) * c,
        0,
        0, 0, 0, 1
    )
    
@overload
def scaling3(v:vec3) -> mat4: pass
@overload
def scaling3(v:vec4) -> mat4: pass
@overload
def scaling3(sx: Union[int,float], sy: Union[int,float], sz: Union[int,float]) -> mat4: pass
@overload
def scaling3(s: Sequence[ Union[int,float] ]) -> mat4: pass

def scaling3(*v):
    """
        Return scaling matrix. Should be passed a vec3, a vec4, a list of 3 scalars,
        or 3 scalars.
        Example: All of these are legal::
        
            scaling3( vec3(2,2,2) )
            scaling3( vec4(4,2,1) )
            scaling3( [2,2,2] )
            scaling3( 2,2,2 )
    
        Returns:
            :class:`mat4`
            
    """    
    return scaling(*v)
   
@overload
def scaling(v:vec3) -> mat4: pass
@overload
def scaling(v:vec4) -> mat4: pass
@overload
def scaling(sx: Union[int,float], sy: Union[int,float], sz: Union[int,float]) -> mat4: pass
@overload
def scaling(s: Sequence[ Union[int,float] ]) -> mat4: pass

def scaling(*args):
    """
        Return scaling matrix. Should be passed a vec3, a vec4, a list of 3 scalars,
        or 3 scalars.
        Example: All of these are legal::
        
            scaling( vec3(2,2,2) )
            scaling( vec4(4,2,1) )
            scaling( [2,2,2] )
            scaling( 2,2,2 )
    
        Returns:
            :class`mat4`
            
    """
        
    if len(args) == 3:
        #called as: scaling(x,y,z)
        sx = args[0]
        sy = args[1]
        sz = args[2]
    elif len(args) == 1:
        #called with vector or list argument
        sx = args[0][0]
        sy = args[0][1]
        sz = args[0][2]
    else:
        raise RuntimeError("Bad type for scaling()")

    return mat4( sx,0,0,0,   0,sy,0,0,   0,0,sz,0,   0,0,0,1 )


 
@overload
def translation3(v:vec3) -> mat4: pass
@overload
def translation3(v:vec4) -> mat4: pass
@overload
def translation3(sx: Union[int,float], sy: Union[int,float], sz: Union[int,float]) -> mat4: pass
@overload
def translation3(s: Sequence[ Union[int,float] ]) -> mat4: pass

def translation3(*v):
    """
        Return translation matrix. Should be passed a vec3, a vec4, a list of 3 scalars,
        or 3 scalars.
        Example: All of these are legal::
        
            translation3( vec3(2,2,2) )
            translation3( vec4(4,2,1) )
            translation3( [2,2,2] )
            translation3( 2,2,2 )
    
        Returns:
            :class:`mat4`
            
    """
    return translation(*v)
   
@overload
def translation(v:vec3) -> mat4: pass
@overload
def translation(v:vec4) -> mat4: pass
@overload
def translation(sx: Union[int,float], sy: Union[int,float], sz: Union[int,float]) -> mat4: pass
@overload
def translation(s: Sequence[ Union[int,float] ]) -> mat4: pass

def translation(*args):
    """
        Return translation matrix. Should be passed a vec3, a vec4, a list of 3 scalars,
        or 3 scalars.
        Example: All of these are legal::
        
            translation( vec3(2,2,2) )
            translation( vec4(4,2,1) )
            translation( [2,2,2] )
            translation( 2,2,2 )
    
        Returns:
            :class:`mat4`
            
    """
    
    if len(args) == 3:
        #called as: translation(x,y,z)
        tx = args[0]
        ty = args[1]
        tz = args[2]
    elif len(args) == 1:
        #called with vector or list argument
        tx = args[0][0]
        ty = args[0][1]
        tz = args[0][2]
    else:
        raise RuntimeError("Bad type for translation()")
        
    return mat4( 1,0,0,0,   0,1,0,0,   0,0,1,0,   tx,ty,tz,1)

 
def translation2(v: Union[list[float],"vec2"]) -> mat3:
    """
        Returns a 2D translation matrix. Should be passed a vec2 or a list of two items.
        Examples::
        
            translation2( vec2(4,4) )
            translation2( [4,4] )
    
        Returns:
            :class`mat3`
            
    """
    return mat3(
        1,0,0,
        0,1,0,
        v[0],v[1],1)

def scaling2(v: Union[list[float],"vec2"]) -> mat3:
    """
        Returns a 2D scaling matrix. Should be passed a vec2 or a list of two items.
        Examples::
        
            scaling2( vec2(4,4) )
            scaling2( [4,4] )
    
        Returns:
            :class:`mat3`
            
    """
    return mat3(v[0],0,0,
                0,v[1],0,
                0,0,1)
                
def rotation2(angle: Union[float,int]) -> mat3:
    """
        Returns a 2D rotation matrix
        Args:
            angle (float): The angle in **radians**
        Returns:
            :class:`mat3`: The rotation matrix
    """
    
    c=math.cos(angle)
    s=math.sin(angle)
    return mat3( c,s,0,     -s,c,0,     0,0,1 )
 
@overload
def inverse(m: "mat2") -> "mat2": pass
@overload
def inverse(m: "mat3") -> "mat3": pass
@overload
def inverse(m: "mat4") -> "mat4": pass

def inverse(m):
    """
        Compute matrix inverse.
        Args:
            m (mat2, mat3, or mat4): The matrix
        Returns:
            Matrix inverse. If the matrix is not invertible, 
            the result is meaningless.
    """
    if type(m) == mat2:
        d = 1.0 / (m[0][0] * m[1][1] - m[0][1] * m[1][0])
        return mat2(d * m[1][1], -d * m[0][1], -d * m[1][0], d * m[0][0])
    elif type(m) == mat3:
        t00 = m[1][1] * m[2][2] - m[1][2] * m[2][1]
        t10 = m[0][1] * m[2][2] - m[0][2] * m[2][1]
        t20 = m[0][1] * m[1][2] - m[0][2] * m[1][1]
        d = 1.0 / (m[0][0] * t00 - m[1][0] * t10 + m[2][0] * t20)
        return mat3( d * t00, -d * t10, d * t20,
              -d * (m[1][0] * m[2][2] - m[1][2] * m[2][0]),
               d * (m[0][0] * m[2][2] - m[0][2] * m[2][0]),
              -d * (m[0][0] * m[1][2] - m[0][2] * m[1][0]),
               d * (m[1][0] * m[2][1] - m[1][1] * m[2][0]),
              -d * (m[0][0] * m[2][1] - m[0][1] * m[2][0]),
               d * (m[0][0] * m[1][1] - m[0][1] * m[1][0]) )
    elif type(m) == mat4:
        tmp_0 = m[2][2] * m[3][3]
        tmp_1 = m[3][2] * m[2][3]
        tmp_2 = m[1][2] * m[3][3]
        tmp_3 = m[3][2] * m[1][3]
        tmp_4 = m[1][2] * m[2][3]
        tmp_5 = m[2][2] * m[1][3]
        tmp_6 = m[0][2] * m[3][3]
        tmp_7 = m[3][2] * m[0][3]
        tmp_8 = m[0][2] * m[2][3]
        tmp_9 = m[2][2] * m[0][3]
        tmp_10 = m[0][2] * m[1][3]
        tmp_11 = m[1][2] * m[0][3]
        tmp_12 = m[2][0] * m[3][1]
        tmp_13 = m[3][0] * m[2][1]
        tmp_14 = m[1][0] * m[3][1]
        tmp_15 = m[3][0] * m[1][1]
        tmp_16 = m[1][0] * m[2][1]
        tmp_17 = m[2][0] * m[1][1]
        tmp_18 = m[0][0] * m[3][1]
        tmp_19 = m[3][0] * m[0][1]
        tmp_20 = m[0][0] * m[2][1]
        tmp_21 = m[2][0] * m[0][1]
        tmp_22 = m[0][0] * m[1][1]
        tmp_23 = m[1][0] * m[0][1]

        t0 = (tmp_0 * m[1][1] + tmp_3 * m[2][1] + tmp_4 * m[3][1]) -        (tmp_1 * m[1][1] + tmp_2 * m[2][1] + tmp_5 * m[3][1])
        t1 = (tmp_1 * m[0][1] + tmp_6 * m[2][1] + tmp_9 * m[3][1]) -        (tmp_0 * m[0][1] + tmp_7 * m[2][1] + tmp_8 * m[3][1])
        t2 = (tmp_2 * m[0][1] + tmp_7 * m[1][1] + tmp_10 * m[3][1]) -        (tmp_3 * m[0][1] + tmp_6 * m[1][1] + tmp_11 * m[3][1])
        t3 = (tmp_5 * m[0][1] + tmp_8 * m[1][1] + tmp_11 * m[2][1]) -        (tmp_4 * m[0][1] + tmp_9 * m[1][1] + tmp_10 * m[2][1])
        d = 1.0 / (m[0][0] * t0 + m[1][0] * t1 + m[2][0] * t2 + m[3][0] * t3)

        return mat4(d * t0, d * t1, d * t2, d * t3,
           d * ((tmp_1 * m[1][0] + tmp_2 * m[2][0] + tmp_5 * m[3][0]) -
              (tmp_0 * m[1][0] + tmp_3 * m[2][0] + tmp_4 * m[3][0])),
           d * ((tmp_0 * m[0][0] + tmp_7 * m[2][0] + tmp_8 * m[3][0]) -
              (tmp_1 * m[0][0] + tmp_6 * m[2][0] + tmp_9 * m[3][0])),
           d * ((tmp_3 * m[0][0] + tmp_6 * m[1][0] + tmp_11 * m[3][0]) -
              (tmp_2 * m[0][0] + tmp_7 * m[1][0] + tmp_10 * m[3][0])),
           d * ((tmp_4 * m[0][0] + tmp_9 * m[1][0] + tmp_10 * m[2][0]) -
              (tmp_5 * m[0][0] + tmp_8 * m[1][0] + tmp_11 * m[2][0])),
           d * ((tmp_12 * m[1][3] + tmp_15 * m[2][3] + tmp_16 * m[3][3]) -
              (tmp_13 * m[1][3] + tmp_14 * m[2][3] + tmp_17 * m[3][3])),
           d * ((tmp_13 * m[0][3] + tmp_18 * m[2][3] + tmp_21 * m[3][3]) -
              (tmp_12 * m[0][3] + tmp_19 * m[2][3] + tmp_20 * m[3][3])),
           d * ((tmp_14 * m[0][3] + tmp_19 * m[1][3] + tmp_22 * m[3][3]) -
              (tmp_15 * m[0][3] + tmp_18 * m[1][3] + tmp_23 * m[3][3])),
           d * ((tmp_17 * m[0][3] + tmp_20 * m[1][3] + tmp_23 * m[2][3]) -
              (tmp_16 * m[0][3] + tmp_21 * m[1][3] + tmp_22 * m[2][3])),
           d * ((tmp_14 * m[2][2] + tmp_17 * m[3][2] + tmp_13 * m[1][2]) -
              (tmp_16 * m[3][2] + tmp_12 * m[1][2] + tmp_15 * m[2][2])),
           d * ((tmp_20 * m[3][2] + tmp_12 * m[0][2] + tmp_19 * m[2][2]) -
              (tmp_18 * m[2][2] + tmp_21 * m[3][2] + tmp_13 * m[0][2])),
           d * ((tmp_18 * m[1][2] + tmp_23 * m[3][2] + tmp_15 * m[0][2]) -
              (tmp_22 * m[3][2] + tmp_14 * m[0][2] + tmp_19 * m[1][2])),
           d * ((tmp_22 * m[2][2] + tmp_16 * m[0][2] + tmp_21 * m[1][2]) -
              (tmp_20 * m[1][2] + tmp_23 * m[2][2] + tmp_17 * m[0][2])))
    else:
        raise RuntimeException("Bad type for inverse()")


if __name__ == "__main__":
    #test harness

    def v4():
        la = [3,-1,4,6]
        lb = [2,5,8,9]
        a = vec4(*la)
        b = vec4(*lb)
        assert a+b == vec4(5,4,12,15)
        assert a+lb == a+b
        # ~ assert la+b == a+b
        assert a-b == vec4(1,-6,-4,-3)
        assert a-lb == a-b
        # ~ assert la-b == a-b
        assert a != b
        assert a*b ==   vec4(6,-5,32,54)
        # ~ assert a*lb ==  vec4(6,-5,32,54)
        # ~ assert la*b ==  vec4(6,-5,32,54)
        assert 2*a == vec4(6,-2,8,12)
        assert a*2 == 2*a
        assert -a == vec4(-3,1,-4,-6)
        assert a == +a
        assert id(a) != id(+a)
        str(a)
        repr(a)
        assert a.copy() == a
        assert id(a.copy()) != a
        c=vec4()
        assert c.isZero
        assert c == vec4(0,0,0,0)
        assert c[0] == 0
        assert c[1] == 0
        assert c[2] == 0
        assert c[3] == 0
        assert not a.isZero
        c[0]=1
        c[1]=3
        c[2]=5
        c[3]=9
        assert c == vec4(1,3,5,9)
        assert c != vec4(2,4,6,8)
        assert c[0] == 1
        assert c.x == 1
        assert c[1] == 3
        assert c.y == 3
        assert c[2] == 5
        assert c.z == 5
        assert c[3] == 9
        assert c.w == 9
        assert c.xy == vec2(1,3)
        assert c.xyz == vec3(1,3,5)
        c.x = 8
        c.y = 9
        c.z= -8
        c.w = -7
        assert c == vec4(8,9,-8,-7)
        c.xy = vec2(3,2)
        assert c == vec4(3,2,-8,-7)
        c.xyz = vec3(13,12,11)
        assert c == vec4(13,12,11,-7)
        c.xyzw = vec4(13,12,11,10)
        assert c == vec4(13,12,11,10)
        assert len(a) == 4
        tmp=[]
        for x in a:
            tmp.append(x)
        assert vec4(tmp) == vec4(la)
        assert vec4(vec2(1,2),3,4) == vec4(1,2,3,4)
        assert vec4(vec3(1,2,3),4) == vec4(1,2,3,4)
        assert vec4(vec2(1,2),vec2(3,4)) == vec4(1,2,3,4)
        assert length(a) == a.magnitude
        a.tobytes()
        n=a.normalized
        n2=normalize(a)
        assert n==n2
        n3 = [0.381,-0.127, 0.508, 0.762]
        for i in range(len(n3)):
            assert abs(n3[i] - n[i]) < 0.001
        assert length(a) == a.magnitude
        assert abs(length(a)-7.874) < 0.001
        assert dot(a,b) == 87
     
    ###
    def v3():
        la = vec3(3,-1,4)
        lb = vec3(2,5,8)
        a = vec3(*la)
        b = vec3(*lb)
        assert a+b == vec3(5,4,12)
        assert a+lb == a+b
        # ~ assert la+b == a+b
        assert a-b == vec3(1,-6,-4)
        assert a-lb == a-b
        assert la-b == a-b
        assert a != b
        assert a*b == vec3(6,-5,32)
        # ~ assert a*lb == vec3(6,-5,32)
        # ~ assert la*b == vec3(6,-5,32)
        assert 2*a == vec3(6,-2,8)
        assert a*2 == 2*a
        assert -a == vec3(-3,1,-4)
        assert a == +a
        assert id(a) != id(+a)
        str(a)
        repr(a)
        assert a.copy() == a
        assert id(a.copy()) != a
        c=vec3()
        assert c.isZero
        assert c == vec3(0,0,0)
        assert c[0] == 0
        assert c[1] == 0
        assert c[2] == 0
        assert not a.isZero
        c[0]=1
        c[1]=3
        c[2]=5
        assert c == vec3(1,3,5)
        assert c == vec3(1,3,5)
        assert c != vec3(2,4,6)
        assert c[0] == 1
        assert c.x == 1
        assert c[1] == 3
        assert c.y == 3
        assert c[2] == 5
        assert c.z == 5
        assert c.xy == vec2(1,3)
        assert c.xyz == vec3(1,3,5)
        c.x = 8
        c.y = 9
        c.z= -8
        assert c == vec3(8,9,-8)
        c.xy = vec2(3,2)
        assert c == vec3(3,2,-8)
        c.xyz = vec3(13,12,11)
        assert c == vec3(13,12,11)
        assert len(a) == 3
        tmp=[]
        for x in a:
            tmp.append(x)
        # ~ assert tmp == la
        assert length(a) == a.magnitude
        a.tobytes()
        n=a.normalized
        n2=normalize(a)
        assert n==n2
        n3 = vec3(0.58834, -0.196116, 0.7844)
        for i in range(len(n3)):
            assert abs(n3[i] - n[i]) < 0.001
        assert abs(length(a)-5.099) < 0.001
        assert dot(a,b) == 33
        
    
    #############################
    def v2():
        la = vec2(3,-1)
        lb = vec2(2,5)
        a = vec2(*la)
        b = vec2(*lb)
        assert a+b == vec2(5,4)
        assert a+lb == a+b
        # ~ assert la+b == a+b
        assert a-b == vec2(1,-6)
        assert a-lb == a-b
        assert la-b == a-b
        assert a != b
        assert a*b == vec2(6,-5)
        # ~ assert a*lb == vec2(6,-5)
        # ~ assert la*b == vec2(6,-5)
        assert 2*a == vec2(6,-2)
        assert a*2 == 2*a
        assert -a == vec2(-3,1,)
        assert a == +a
        assert id(a) != id(+a)
        str(a)
        repr(a)
        assert a.copy() == a
        assert id(a.copy()) != a
        c=vec2()
        assert c.isZero
        assert c == vec2(0,0)
        assert c[0] == 0
        assert c[1] == 0
        assert not a.isZero
        c[0]=1
        c[1]=3
        assert c == vec2(1,3)
        assert c == vec2(1,3)
        assert c != vec2(2,4)
        assert c[0] == 1
        assert c.x == 1
        assert c[1] == 3
        assert c.y == 3
        assert c.xy == vec2(1,3)
        c.x = 8
        c.y = 9
        assert c == vec2(8,9)
        c.xy = vec2(3,2)
        assert c == vec2(3,2)
        assert len(a) == 2
        tmp=[]
        for x in a:
            tmp.append(x)
        # ~ assert tmp == la
        assert length(a) == a.magnitude
        a.tobytes()
        n=a.normalized
        n2=normalize(a)
        assert n==n2
        n3 = vec2(0.94868,-0.31622)
        for i in range(len(n3)):
            assert abs(n3[i] - n[i]) < 0.001
        assert abs(length(a)-3.162277) < 0.001
        assert dot(a,b) == 1
        
    ##################
    def m4():
        
        a = mat4( 3,1,4,5,
                  9,2,6,7,
                  8,-3,-1,-4,
                  -5,-2,-7,-6)
                  
        b = mat4( -2,-7,3,8,
                  -1,-5,-10,12,
                  -4,7,2,4,
                  5,-8,1,-3)
        assert a*b == mat4(
            2,-38,12,37,
            -9,-87,26,99,
            -29,-16,48,36,
            10,44,-15,-74)
        assert a != b
        c=mat4()
        c2=mat4()
        for i in range(4):
            for j in range(4):
                assert c[i][j] == 0
                
        x=[     [3,1,4,5],
                [9,2,6,7],
                [8,-3,-1,-4],
                [-5,-2,-7,-6]
        ]
        for i in range(4):
            for j in range(4):
                c[i][j] = x[i][j]
                c2[i,j] = x[i][j]
        assert c == a
        assert c2 == a
        for i in range(4):
            for j in range(4):
                assert c[i][j] == x[i][j]
                assert c2[i,j] == x[i][j]
                
        assert a+b == mat4(1,-6,7,13,8,-3,-4,19,4,4,1,0,0,-10,-6,-9)
        assert a-b == a+-1*b
        assert 2*a == mat4(6,2,8,10,18,4,12,14,16,-6,-2,-8,-10,-4,-14,-12)
        assert 2*a == a*2        
        
        c=+a
        assert id(c) != id(a)
        assert c == a
        assert -a == -1*a
        c = -a
        assert c == mat4( 
                    -3,-1,-4,-5,
                    -9,-2,-6,-7,
                    -8,3,1,4,
                    5,2,7,6)
        a.tobytes()
        str(a)
        repr(a)
        assert transpose(a) == mat4( 3,9,8,-5, 1,2,-3,-2, 4,6,-1,-7, 5,7,-4,-6)
        
        x = inverse(a) * a 
        y = a * inverse(a)
        for i in range(4):
            for j in range(4):
                assert abs(x[i][j] - y[i][j] < 0.001)
                if i == j:
                    assert abs(x[i][j] - 1) < 0.001
                else:
                    assert abs(x[i][j]) < 0.001
                    
        assert a*vec4(0.5,1.5,2.5,4.5) == vec4(35.5,54,-21,-50)
        assert vec4(0.5,1.5,2.5,4.5)*a == vec4(12.5,-13,-23,-24)
        assert a*(0.5,1.5,2.5,4.5) == vec4(35.5,54,-21,-50)
        assert (0.5,1.5,2.5,4.5)*a == vec4(12.5,-13,-23,-24)
        assert a*[0.5,1.5,2.5,4.5] == vec4(35.5,54,-21,-50)
        assert [0.5,1.5,2.5,4.5]*a == vec4(12.5,-13,-23,-24)
        
    
    ###################
    def m3():
        
        a = mat3( 3,1,4,
                  9,2,6,
                  8,-3,-1)
        b = mat3( -2,-7,3,
                  -1,-5,-10,
                  -4,7,2)
        assert a*b == mat3(
            -23,2,7,  -44,-31,19,  -9,-48,52 )
        assert a != b
        c=mat3()
        c2=mat3()
        for i in range(3):
            for j in range(3):
                assert c[i][j] == 0
                
        x=[     [3,1,4],
                [9,2,6],
                [8,-3,-1] 
        ]
        for i in range(3):
            for j in range(3):
                c[i][j] = x[i][j]
                c2[i,j] = x[i][j]
        assert c == a
        assert c2 == a
        for i in range(3):
            for j in range(3):
                assert c[i][j] == x[i][j]
                assert c2[i,j] == x[i][j]
                
        assert a+b == mat3(1,-6,7,8,-3,-4,4,4,1)
        assert a-b == a+-1*b
        assert 2*a == mat3(6,2,8,   18,4,12,    16,-6,-2)
        assert 2*a == a*2        
        
        c=+a
        assert id(c) != id(a)
        assert c == a
        assert -a == -1*a
        c=-a
        assert c == mat3( 
                    -3,-1,-4,
                    -9,-2,-6,
                    -8,3,1)
        a.tobytes()
        str(a)
        repr(a)
        assert transpose(a) == mat3( 3,9,8, 1,2,-3,   4,6,-1 )
        
        x = inverse(a) * a 
        y = a * inverse(a)
        for i in range(3):
            for j in range(3):
                assert abs(x[i][j] - y[i][j] < 0.001)
                if i == j:
                    assert abs(x[i][j] - 1) < 0.001
                else:
                    assert abs(x[i][j]) < 0.001
                    
        assert a*vec3(0.5,1.5,2.5) == vec3(13,22.5,-3)
        assert vec3(0.5,1.5,2.5)*a == vec3(35,-4,8.5)
        assert a*(0.5,1.5,2.5) == vec3(13,22.5,-3)
        assert (0.5,1.5,2.5)*a == vec3(35,-4,8.5)
        
    #################################

    def m2():
        a = mat2( 3,1,
                  9,2 )
        b = mat2( -2,-7,
                  -1,-5 )
        assert a*b == mat2( -7,-26, -20, -73 )
        assert a != b
        c=mat2()
        c2=mat2()
        for i in range(2):
            for j in range(2):
                assert c[i][j] == 0
                
        x=[     [3,1],
                [9,2]
        ]
        for i in range(2):
            for j in range(2):
                c[i][j] = x[i][j]
                c2[i,j] = x[i][j]
        assert c == a
        assert c2 == a
        for i in range(2):
            for j in range(2):
                assert c[i][j] == x[i][j]
                assert c[i,j] == x[i][j]
        assert a+b == mat2(1,-6,    8,-3  )
        assert a-b == a+-1*b
        assert 2*a == mat2(6,2,  18,4  )
        assert 2*a == a*2        
        
        c=+a
        assert id(c) != id(a)
        assert c == a
        assert -a == -1*a
        c=-a
        assert c == mat2( -3,-1, -9,-2 )
        a.tobytes()
        str(a)
        repr(a)
        assert transpose(a) == mat2( 3,9, 1,2 )
        
        x = inverse(a) * a 
        y = a * inverse(a)
        for i in range(2):
            for j in range(2):
                assert abs(x[i][j] - y[i][j] < 0.001)
                if i == j:
                    assert abs(x[i][j] - 1) < 0.001
                else:
                    assert abs(x[i][j]) < 0.001
                    
        assert a*vec2(0.5,1.5) == vec2(3,7.5)
        assert vec2(0.5,1.5)*a == vec2(15,3.5)
        assert a*(0.5,1.5) == vec2(3,7.5)
        assert (0.5,1.5)*a == vec2(15,3.5)
    
    ##################
    def cr():
        c = cross( vec3(2,5,9), vec3(0.5,1.5,3.5) )
        assert c == vec3(4,-2.5,.5)
        
        c = cross( vec4(2,5,9,0), vec4(0.5,1.5,3.5,0) )
        assert c.xyz == vec3(4,-2.5,.5)

        #c = cross( (2,5,9,0), (0.5,1.5,3.5,0) )
        #assert c.xyz == vec3(4,-2.5,.5)

    def trm():
        
        #axisRotation, scaling,
        #translation,
         
        v2a=vec2(2,4)
        v2b=vec2(10,11)
        
        assert v2a+v2b == vec2(12,15)
        assert v2a-v2b == vec2(-8,-7)
        assert v2a+v2b != vec2(12,3)
        assert v2a+v2b != vec2(3,15)
        assert v2a*v2b == vec2(20,44)
        assert 5*v2a == vec2(10,20)
        assert v2a*5 == vec2(10,20)
        
        assert v2a.xy == v2a
        
        v3a=vec3(2,4,6)
        v3b=vec3(10,11,12)
        
        assert v3a+v3b == vec3(12,15,18)
        assert v3a-v3b == vec3(-8,-7,-6)
        assert v3a+v3b != vec3(12,3,18)
        assert v3a+v3b != vec3(3,15,18)
        assert v3a+v3b != vec3(12,3,0)
        assert v3a*v3b == vec3(20,44,72)
        assert 5*v3a == vec3(10,20,30)
        assert v3a*5 == vec3(10,20,30)
        
        assert v3a.xyz == v3a
        
        m4=mat4(3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3)
        v4=vec4(2,4,6,7)
        va = v4*m4
        vb = m4*v4
        assert transpose(m4) != m4
        assert transpose(transpose(m4)) == m4
        
        m4i = inverse(m4)
        p=m4*m4i
        p2=m4i*m4
        
        for i in range(4):
            for j in range(4):
                if i == j:
                    t=1
                else:
                    t=0
                assert abs(p[i][j]-t) < 0.001
                assert abs(p2[i][j]-t) < 0.001
                assert abs(p2[i,j]-t) < 0.001
        
        M=axisRotation(vec3(0,1,0),math.radians(90))
        v=vec4(0,0,1,0)*M
        assert abs(dot(v,vec4(0,0,1,0))) < 0.01
        assert abs(dot(v,vec4(1,0,0,0))-1) < 0.01
        
        v1=vec3(3,1,4)
        v2=vec3(-5,2,9)
        v1=normalize(v1)
        v2=normalize(v2)
        v3 = cross(v1,v2)
        assert abs(dot(v1,v3)) < 0.01
        assert abs(dot(v2,v3)) < 0.01
        
        assert translation(vec3(4,2,3)) == mat4( 1,0,0,0,  0,1,0,0,  0,0,1,0,  4,2,3,1 )
        assert translation(vec3(4.0,2,3)) == mat4( 1,0,0,0,  0,1,0,0,  0,0,1,0,  4,2,3,1 )
        assert translation((4,2,3)) == mat4( 1,0,0,0,  0,1,0,0,  0,0,1,0,  4,2,3,1 )
        assert translation([4,2,3]) == mat4( 1,0,0,0,  0,1,0,0,  0,0,1,0,  4,2,3,1 )
        assert translation(vec4(4,2,3,7)) == mat4( 1,0,0,0,  0,1,0,0,  0,0,1,0,  4,2,3,1 )
        assert translation(4,2,3) == mat4( 1,0,0,0,  0,1,0,0,  0,0,1,0,  4,2,3,1 )
        assert translation(4,2.0,3) == mat4( 1,0,0,0,  0,1,0,0,  0,0,1,0,  4,2,3,1 )


        assert scaling(vec3(4,2,3)) == mat4( 4,0,0,0,  0,2,0,0,  0,0,3,0,  0,0,0,1 )
        assert scaling(vec3(4,2.0,3)) == mat4( 4,0,0,0,  0,2,0,0,  0,0,3,0,  0,0,0,1 )
        assert scaling((4,2,3)) == mat4( 4,0,0,0,  0,2,0,0,  0,0,3,0,  0,0,0,1 )
        assert scaling([4,2,3]) == mat4( 4,0,0,0,  0,2,0,0,  0,0,3,0,  0,0,0,1 )
        assert scaling(vec4(4,2,3,7)) == mat4( 4,0,0,0,  0,2,0,0,  0,0,3,0,  0,0,0,1 )
        assert scaling(4,2,3) == mat4( 4,0,0,0,  0,2,0,0,  0,0,3,0,  0,0,0,1 )
        assert scaling(4.0,2,3) == mat4( 4,0,0,0,  0,2,0,0,  0,0,3,0,  0,0,0,1 )

    
    v4()
    v3()
    v2()
    m4()
    m3()
    m2()
    cr()
    trm()
    
    print("All tests OK")

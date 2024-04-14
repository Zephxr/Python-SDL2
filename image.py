
#written by jh 2018
# windows test: OK: 01-jul-2018

from ctypes import *
import sys
import array
import io
import typing

__all__ = ["decode","encodePNG","encodeBMP","flipY"]

pngHeader=[137,80,78,71,13,10,26,10]
jpgHeader = [0xff, 0xd8, 0xff, 0xe0]

  
def compare(l1,l2):
    le = min([len(l1),len(l2)])
    if le == 0:
        return False
    for i in range(le):
        if l1[i] != l2[i] :
            return False
    return True
    
#need to hide the windows ctypes functions from linux...
def Win32():
    from ctypes.wintypes import HANDLE, HGLOBAL, BOOL,UINT,LARGE_INTEGER,ULARGE_INTEGER,ULONG
    
    
    CLSID_WICImagingFactory = (c_ubyte*16)(232, 6, 125, 49, 36, 95, 61, 67, 189, 247, 121, 206, 104, 216, 171, 194)
    IID_IWICImagingFactory = (c_ubyte*16)(169, 200, 94, 236, 149, 195, 20, 67, 156, 119, 84, 215, 169, 53, 255, 112)

    #this one is from the documentation at
    #https://msdn.microsoft.com/en-us/library/windows/desktop/ee690110(v=vs.85).aspx
    CLSID_WICPngEncoder = (c_ubyte*16)(0x69, 0x99, 0x94, 0x27, 0x6a, 0x87, 0xd7, 0x41, 0x94, 0x47, 0x56,0x8f, 0x6a,0x35,0xa4, 0xdc)

    #GUID_WICPixelFormat24bppBGR
    GUID_BGR8 = [36,195,221,111,3,78,254,75,177,133,61,119,118,141,201,12]
    #GUID_WICPixelFormat32bppBGRA
    GUID_BGRA8 = [36,195,221,111,3,78,254,75,177,133,61,119,118,141,201,15 ]
    #GUID_WICPixelFormat64bppRGBA
    GUID_RGBA16 = [36,195,221,111,3,78,254,75,177,133,61,119,118,141,201,22]
    #GUID_WICPixelFormat32bppRGBA
    GUID_RGBA8 = [45,173,199,245,141,106,221,67,167,168,162,153,53,38,26,233]
    #GUID_WICPIxelFormat64bppBGRA
    GUID_BGRA16 = [124,255,98,21,82,211,249,70,151,158,66,151,107,121,34,70]
    #GUID_ContainerFormatPng
    GUID_PNG = [244,250,124,27,63,113,60,71,187,205,97,55,66,95,174,175]
    
    #functions for IStream
    class IStream_functions(Structure):
        _fields_ = [
            ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
            ("Read",WINFUNCTYPE(c_long, c_void_p, c_void_p, c_uint, POINTER(ULONG))),
            ("junk32",c_voidp),
            ("Seek",WINFUNCTYPE(c_long, c_void_p, LARGE_INTEGER, c_uint, POINTER(ULARGE_INTEGER)) )
        ]        

    class IStream(Structure):
        _fields_ = [ ("lpVtbl", POINTER(IStream_functions))]
    
     #functions for IWICStream
    class IWICStream_functions(Structure):
        _fields_ = [
            ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
            ("junk24", c_void_p),
            ("junk32", c_void_p),
            ("junk40", c_void_p),
            ("junk48", c_void_p),
            ("junk56", c_void_p),
            ("junk64", c_void_p),
            ("junk72", c_void_p),
            ("junk80", c_void_p),
            ("junk88", c_void_p),
            ("junk96", c_void_p),
            ("junk104", c_void_p),
            ("InitializeFromIStream", WINFUNCTYPE(c_long,c_void_p,c_void_p)),
            ("junk120", c_void_p),
            ("InitializeFromMemory" , WINFUNCTYPE(c_long,c_void_p,c_void_p,c_int))
        ]        

    class IWICStream(Structure):
        _fields_ = [ ("lpVtbl", POINTER(IWICStream_functions))]
    
    
    class IWICFormatConverter_functions(Structure):
         _fields_ = [
             ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
             ("junk24", c_void_p),
            ("junk32", c_void_p),
            ("junk40", c_void_p),
            ("junk48", c_void_p),
            ("CopyPixels", WINFUNCTYPE(c_long,c_void_p,c_void_p,UINT,UINT,c_void_p)),
            ("Initialize", WINFUNCTYPE(c_long,c_void_p,c_void_p,c_ubyte*16,c_uint,c_void_p,c_double,c_uint)),
            ("junk72", c_void_p),
            ("junk80", c_void_p),
            ("junk88", c_void_p),
            ("junk96", c_void_p),
            
        ]
        
    class IWICFormatConverter(Structure):
        _fields_ = [ ("lpVtbl", POINTER(IWICFormatConverter_functions))]
        

    #vtable for the decoder class (IWICBitmapDecoder)
    class IWICBitmapDecoder_functions(Structure):
        _fields_ = [
            ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
            ("junk24", c_void_p),
            ("junk32", c_void_p),
            ("junk40", c_void_p),
            ("junk48", c_void_p),
            ("junk56", c_void_p),
            ("junk64", c_void_p),
            ("junk72", c_void_p),
            ("junk80", c_void_p),
            ("junk88", c_void_p),
            ("junk96", c_void_p),
            ("GetFrame", WINFUNCTYPE(c_long,c_void_p,UINT,c_void_p)),

            ]
            
    #the  class description (IWICBitmapDecoder)
    class IWICBitmapDecoder(Structure):
        _fields_ = [ ("lpVtbl", POINTER(IWICBitmapDecoder_functions))]




    #vtable for the decoder class (IWICBitmapDecoder)
    class IWICBitmap_functions(Structure):
        _fields_ = [
            ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
            ("junk24", c_void_p),
            ("junk32", c_void_p),
            ("junk40", c_void_p),
            ("junk48", c_void_p),
            ("junk56", c_void_p),
            ("junk64", c_void_p),
            ("junk72", c_void_p),
            ("junk80", c_void_p),
            ("junk88", c_void_p),
            ("junk96", c_void_p),
            ]
            
    #the  class description (IWICBitmapDecoder)
    class IWICBitmap(Structure):
        _fields_ = [ ("lpVtbl", POINTER(IWICBitmap_functions))]


    










   #vtable for the decoder class (IWICBitmapDecoder)
    class IWICBitmapEncoder_functions(Structure):
        _fields_ = [
            ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
            ("Initialize", WINFUNCTYPE(c_long, c_void_p, c_voidp, UINT) ),
            ("junk32",c_void_p),
            ("junk40",c_void_p),
            ("junk48",c_void_p),
            ("junk56",c_void_p),
            ("junk64",c_void_p),
            ("junk72",c_void_p),
            ("CreateNewFrame",WINFUNCTYPE( c_long, c_void_p, c_void_p,c_void_p) ),
            ("Commit",WINFUNCTYPE( c_long, c_void_p))
        ]
            
    #the  class description (IWICBitmapDecoder)
    class IWICBitmapEncoder(Structure):
        _fields_ = [ ("lpVtbl", POINTER(IWICBitmapEncoder_functions))]





    class IWICBitmapFrameEncode_functions(Structure):
        _fields_ = [
            ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
            ("Initialize",WINFUNCTYPE(c_long,c_void_p,c_void_p)),
            ("SetSize",WINFUNCTYPE(c_long,c_void_p,c_uint,c_uint)),
            ("junk40",c_void_p),
            ("SetPixelFormat",WINFUNCTYPE(c_long,c_void_p,c_ubyte*16)),
            ("junk56",c_void_p),
            ("junk64",c_void_p),
            ("junk72",c_void_p),
            ("junk80",c_void_p),
            ("WriteSource",WINFUNCTYPE(c_long,c_void_p,c_void_p,c_void_p)),
            ("Commit",WINFUNCTYPE(c_long,c_void_p))
        ]
        
    class IWICBitmapFrameEncode(Structure):
        _fields_ = [ ("lpVtbl", POINTER(IWICBitmapFrameEncode_functions))]
        








    #vtable for the bitmap class (IWICBitmapFrameDecode)
    class IWICBitmapFrameDecode_functions(Structure):
        _fields_ = [
            ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
            ("GetSize" ,
                 WINFUNCTYPE(
                    c_long,
                    c_void_p,
                    POINTER(c_int),
                    POINTER(c_int)
                )
             ),
            ("GetPixelFormat" ,
                 WINFUNCTYPE(
                     c_long,
                     c_void_p,
                     POINTER(c_ubyte)
                )
            ),
            ("junk40",c_void_p),
            ("junk48",c_void_p),
            ("CopyPixels" , WINFUNCTYPE(c_long,
                                        c_void_p,
                                        c_void_p,
                                        c_int,
                                        c_int,
                                        c_void_p))
        ]
        
    #the bitmap class
    class IWICBitmapFrameDecode(Structure):
        _fields_ = [ ("lpVtbl", POINTER(IWICBitmapFrameDecode_functions))]
        
            
    #WICImagingFactory vtable functions
    class WICImagingFactory_functions(Structure):
        _fields_ = [
            ("junk0", c_void_p),
            ("junk8", c_void_p),
            ("Release", WINFUNCTYPE(c_long, c_void_p) ),
            ("CreateDecoderFromFilename" , WINFUNCTYPE( c_long,
                                               c_void_p,
                                               c_wchar_p,
                                               c_void_p,
                                               c_int,
                                               c_int,
                                               c_void_p)  ),
            ("CreateDecoderFromStream" , WINFUNCTYPE( c_long,
                                               c_void_p,
                                               c_void_p,
                                               c_void_p,
                                               c_int,
                                               c_void_p)  ),
            ("junk40",c_void_p),
            ("junk48",c_void_p),
            ("junk56",c_void_p),
            ("CreateEncoder",WINFUNCTYPE(c_long,c_void_p,c_ubyte*16,c_void_p,c_void_p)),
            ("junk72",c_void_p),
            ("CreateFormatConverter",WINFUNCTYPE(c_long,c_void_p,c_void_p)),
            ("junk88",c_void_p),
            ("junk96",c_void_p),
            ("junk104",c_void_p),
            ("CreateStream" , WINFUNCTYPE( c_long, c_void_p, c_void_p) ),
            ("junk120",c_void_p),
            ("junk128",c_void_p),
            ("junk136",c_void_p),
            ("junk144",c_void_p),
            ("junk152",c_void_p),
            ("CreateBitmapFromMemory",WINFUNCTYPE(c_long,c_void_p,c_uint,c_uint,c_ubyte*16,c_uint,c_uint,c_voidp,c_voidp))            
            ]
        
    #WICImagingFactory
    class WICImagingFactory(Structure):
        _fields_ = [ ("lpVtbl", POINTER(WICImagingFactory_functions) ) ]

    def mkguid(values):
        g=(c_ubyte*16)()
        for i in range(16):
            g[i] = values[i]
        return g



    ole32 = OleDLL("ole32.dll")
    hr = ole32.CoInitialize(c_void_p(0))
    if hr != 0:
        raise RuntimeError("Could not CoInitialize OLE32")
    
    kernel32 = WinDLL("kernel32.dll")
    GlobalLock = WINFUNCTYPE(c_void_p, HGLOBAL)(("GlobalLock",kernel32))

    factory = POINTER(WICImagingFactory)()

    hr = ole32.CoCreateInstance(
        CLSID_WICImagingFactory,
        c_void_p(0),
        c_int(1),          #enum CLSCTX_INPROC_SERVER
        IID_IWICImagingFactory,
        byref(factory)
    )
    if hr != 0:
        raise RuntimeError("Could not create WICImagingFactory")
        
    def savePng(w,h,fmt,data):
        
        if type(data) == bytearray:
            data = create_string_buffer(bytes(data),len(data))
        elif type(data) == bytes:
            data = create_string_buffer(data,len(data))
        else:
            raise RuntimeError("Must pass bytes or bytearray to savePng")
        
        stream = POINTER(IStream)()
        hr = ole32.CreateStreamOnHGlobal(None, BOOL(1), byref(stream))
        if hr != 0:
            raise RuntimeError("Could not create HGlobal stream")
        try:
            encoder = POINTER(IWICBitmapEncoder)()
            hr = factory.contents.lpVtbl.contents.CreateEncoder( factory, (c_ubyte*16)(*GUID_PNG) , 
                    c_void_p(0), byref(encoder))
            if hr != 0:
                raise RuntimeError("Could not create encoder")
            try:
                #2=no cache
                hr = encoder.contents.lpVtbl.contents.Initialize(encoder, stream, 2)
                if hr != 0:
                    raise RuntimeError("Could not create encoder")
    
                frame = POINTER(IWICBitmapFrameEncode)()
                props = c_void_p()
                hr = encoder.contents.lpVtbl.contents.CreateNewFrame(encoder,byref(frame), byref(props))
                if hr != 0:
                    raise RuntimeError("Could not create encoder")
                try:
                    hr = frame.contents.lpVtbl.contents.Initialize(frame,props)
                    if hr != 0:
                        raise RuntimeError("Could not initialize frame")
    
                    hr = frame.contents.lpVtbl.contents.SetSize(frame,w,h)
                    if hr != 0:
                        raise RuntimeError("Could not set size")
    
                    if fmt == "RGB8":
                        stride=w*3
                        pf = (GUID_RGBA8)
                    elif fmt == "RGBA8":
                        stride=w*4
                        pf = (GUID_RGBA8)
                    elif fmt == "RGB16":
                        stride=w*6
                        pf=(GUID_RGBA16)
                    elif fmt == "RGBA16":
                        stride=w*8
                        pf=(GUID_RGBA16)
                    else:
                        raise RuntimeError("Unknown pixel format: Must be RGB8, RGBA8, RGB16, or RGBA16")
                    
                    bmp = POINTER(IWICBitmap)()
                    tmp=(c_ubyte*16)()
                    for i in range(len(pf)):
                        tmp[i]=pf[i]
                    pf = tmp
                    
                    hr = factory.contents.lpVtbl.contents.CreateBitmapFromMemory(
                            factory,w,h,pf,stride,h*stride,data,byref(bmp))
                    if hr != 0:
                        raise RuntimeError("Cannot create bitmap")
                    try:
                        hr = frame.contents.lpVtbl.contents.SetPixelFormat(frame,pf)
                        if hr != 0:
                            raise RuntimeError("Cannot set pixel format")
                        conv = POINTER(IWICFormatConverter)()
                        hr = factory.contents.lpVtbl.contents.CreateFormatConverter(factory,byref(conv))
                        if hr != 0:
                            raise RuntimeError("Cannot create converter")
                        try:
                            hr = conv.contents.lpVtbl.contents.Initialize(conv,bmp,pf,0,
                                c_void_p(0),0.0,0)
                            if hr != 0:
                                raise RuntimeError("Cannot initialize converter")
                            hr = frame.contents.lpVtbl.contents.WriteSource(frame,bmp,c_void_p(0))
                            if hr != 0:
                                raise RuntimeError("Cannot write source")
                            hr = frame.contents.lpVtbl.contents.Commit(frame)
                            if hr != 0:
                                raise RuntimeError("Cannot commit frame")
                            hr = encoder.contents.lpVtbl.contents.Commit(encoder)
                            if hr != 0:
                                raise RuntimeError("Cannot commit encoder")
                            
                            pos = ULARGE_INTEGER(0)
                            zero = LARGE_INTEGER(0)
                            hr = stream.contents.lpVtbl.contents.Seek(stream,zero,1,byref(pos))
                            if hr != 0:
                                raise RuntimeError("Cannot seek end")
                            buffSize = pos.value
                            numLeft=buffSize
                            pngDataBuffer = (c_byte * numLeft )()
                            p = addressof(pngDataBuffer)
                            hr = stream.contents.lpVtbl.contents.Seek(stream,zero,0,byref(pos))
                            if hr != 0:
                                raise RuntimeError("Cannot seek start")
                            while numLeft > 0:
                                numRead = ULONG()
                                hr = stream.contents.lpVtbl.contents.Read(stream, p, numLeft,byref(numRead))
                                if hr != 0:
                                    raise RuntimeError("Could not read")
                                numLeft -= numRead.value
                                p += numRead.value
                            return string_at(pngDataBuffer,buffSize)
                        finally:
                            conv.contents.lpVtbl.contents.Release(conv)
                    finally:
                        bmp.contents.lpVtbl.contents.Release(bmp)
                finally:
                    frame.contents.lpVtbl.contents.Release(frame)
            finally:
                encoder.contents.lpVtbl.contents.Release(encoder)
        finally:
            stream.contents.lpVtbl.contents.Release(stream)
        
    def load(data):
        if not compare(pngHeader, data) and not compare(jpgHeader,data):
            raise RuntimeError("Image is neither PNG nor JPEG")

        stream = POINTER(IWICStream)()
        hr = factory.contents.lpVtbl.contents.CreateStream(factory,byref(stream))
        if hr != 0:
            raise RuntimeError("Could not create IWICStream")
        try:
            hr = stream.contents.lpVtbl.contents.InitializeFromMemory( stream, data, len(data))
            if hr != 0:
                raise RuntimeError("Could not create initialize stream from memory")

            dec = POINTER(IWICBitmapDecoder)()
            hr = factory.contents.lpVtbl.contents.CreateDecoderFromStream(
                    factory, stream, c_void_p(0), 0, byref(dec) )
            if hr != 0:
                raise RuntimeError("Could not create decoder from stream")
            try:
                bmp = POINTER(IWICBitmapFrameDecode)()
                hr = dec.contents.lpVtbl.contents.GetFrame(dec,0,byref(bmp))
                if hr != 0:
                    raise RuntimeError("Could not get frame")
                try:
                    w=c_int()
                    h=c_int()
                    bmp.contents.lpVtbl.contents.GetSize(bmp, byref(w), byref(h) )
                    w=w.value
                    h=h.value

                    pfmt = (c_ubyte * 16)()
                    hr = bmp.contents.lpVtbl.contents.GetPixelFormat(bmp,pfmt)
                    if hr != 0:
                        raise RuntimeError("Could not get pixel format")
                    convertFmt = (c_ubyte * 16)()
                    
                    tmp = [q for q in pfmt]
                    if tmp == GUID_RGBA16 or tmp == GUID_BGRA16:
                        convertFmt = GUID_RGBA16
                        fmt="RGBA16"
                        Bpp=8
                    else:
                        convertFmt = GUID_RGBA8
                        Bpp=4
                        fmt="RGBA8"
                    
                    conv = POINTER(IWICFormatConverter)()
                    hr = factory.contents.lpVtbl.contents.CreateFormatConverter(factory,byref(conv))
                    if hr != 0:
                        raise RuntimeError("Cannot create converter")
                    try:
                        tmp = (c_ubyte*16)()
                        for i in range(len(convertFmt)):
                            tmp[i] = convertFmt[i]
                        hr = conv.contents.lpVtbl.contents.Initialize(conv,bmp,tmp,0,
                                c_void_p(0),0.0,0)
                        if hr != 0:
                            raise RuntimeError("Cannot initialize converter")
                        returnedImage = create_string_buffer(w*h*Bpp)
                        hr = conv.contents.lpVtbl.contents.CopyPixels(conv,c_void_p(0),
                            w*Bpp,w*h*Bpp,returnedImage)
                        if hr != 0:
                            raise RuntimeError("Cannot copy pixels")
                        return (w,h,fmt,string_at(returnedImage,w*h*Bpp))
                        
                    finally:
                        conv.contents.lpVtbl.contents.Release(conv)
                finally:
                    bmp.contents.lpVtbl.contents.Release(bmp)
            finally:
                dec.contents.lpVtbl.contents.Release(dec)
        finally:
            stream.contents.lpVtbl.contents.Release(stream)

        return (w,h,fmt,data)

    return (load,savePng)

def Linux():
    
    libpng = cdll.LoadLibrary("libpng.so")
    libjpeg = cdll.LoadLibrary("libturbojpeg.so")

    png_create_read_struct = libpng.png_create_read_struct
    png_create_read_struct.argtypes = [c_char_p, c_void_p,c_void_p,c_void_p ]
    png_create_read_struct.restype = c_void_p
    
    png_create_write_struct = libpng.png_create_write_struct
    png_create_write_struct.argtypes = [c_char_p, c_void_p,c_void_p,c_void_p ]
    png_create_write_struct.restype = c_void_p


    png_create_info_struct = libpng.png_create_info_struct 
    png_create_info_struct.argtypes = [c_void_p]
    png_create_info_struct.restype = c_void_p 
    
    png_init_io = libpng.png_init_io
    png_init_io.argtypes = [c_void_p,c_void_p]
    
    png_set_bgr = libpng.png_set_bgr
    png_set_bgr.argtypes = [c_void_p]
    
    ReadCallback_t = CFUNCTYPE(None, c_void_p, POINTER(c_ubyte), c_size_t)
    png_set_read_fn = libpng.png_set_read_fn
    png_set_read_fn.argtypes = [c_void_p, c_void_p, ReadCallback_t]
    
    png_read_info = libpng.png_read_info
    png_read_info.argtypes = [ c_void_p, c_void_p ]
    
    png_destroy_read_struct = libpng.png_destroy_read_struct 
    png_destroy_read_struct.argtypes = [c_void_p,c_void_p,c_void_p]
    
    png_read_row = libpng.png_read_row
    png_read_row.argtypes = [ c_void_p, c_void_p, c_void_p ]
    
    png_get_bit_depth = libpng.png_get_bit_depth 
    png_get_bit_depth.argtypes = [c_void_p,c_void_p]
    png_get_bit_depth.restype = c_ubyte
    
    png_get_color_type = libpng.png_get_color_type 
    png_get_color_type.argtypes = [c_void_p,c_void_p]
    png_get_color_type.restype = c_ubyte 
    
    png_get_image_width = libpng.png_get_image_width
    png_get_image_width.argtypes = [c_void_p,c_void_p]
    png_get_image_width.restype = c_uint32
    
    png_get_image_height = libpng.png_get_image_height
    png_get_image_height.argtypes = [c_void_p,c_void_p]
    png_get_image_height.restype = c_uint32
    
    png_get_libpng_ver = libpng.png_get_libpng_ver 
    png_get_libpng_ver.argtypes = [c_void_p]
    png_get_libpng_ver.restype = c_char_p
    
    
    WriteCallback_t = CFUNCTYPE(None, c_void_p, POINTER(c_ubyte), c_size_t)
    FlushCallback_t = CFUNCTYPE(None, c_void_p)
    png_set_write_fn = libpng.png_set_write_fn
    png_set_write_fn.argtypes = [c_void_p, c_void_p, WriteCallback_t, FlushCallback_t ]
    
    png_set_IHDR = libpng.png_set_IHDR
    png_set_IHDR.argtypes = [ c_void_p, c_void_p, c_int, c_int, c_int, c_int,
        c_int, c_int, c_int]
     
    png_write_info = libpng.png_write_info
    png_write_info.argtypes = [c_void_p, c_void_p ]

    png_set_bgr = libpng.png_set_bgr
    png_set_bgr.argtypes = [c_void_p]
    
    png_set_swap = libpng.png_set_swap
    png_set_swap.argtypes = [c_void_p]
    
    png_set_tRNS_to_alpha = libpng.png_set_tRNS_to_alpha
    png_set_tRNS_to_alpha.argtypes = [c_void_p]
    
    png_set_expand = libpng.png_set_expand
    png_set_expand.argtypes = [c_void_p]
    
    png_set_add_alpha = libpng.png_set_add_alpha
    png_set_add_alpha.argtypes = [c_void_p,c_uint,c_int]
    
    png_set_expand_gray_1_2_4_to_8 = libpng.png_set_expand_gray_1_2_4_to_8
    png_set_expand_gray_1_2_4_to_8.argtypes = [c_void_p]
    
    png_set_palette_to_rgb = libpng.png_set_palette_to_rgb
    png_set_palette_to_rgb.argtypes = [c_void_p]

    png_set_gray_to_rgb = libpng.png_set_gray_to_rgb
    png_set_gray_to_rgb.argtypes = [c_void_p]

    
    
    png_write_row = libpng.png_write_row
    png_write_row.argtypes = [c_void_p, c_void_p] 

    png_write_end = libpng.png_write_end
    png_write_end.argtypes = [c_void_p, c_void_p]
        
    png_destroy_write_struct = libpng.png_destroy_write_struct
    png_destroy_write_struct.argtypes = [c_void_p, c_void_p]
           
    PNG_INTERLACE_NONE = 0
    PNG_COMPRESSION_TYPE_DEFAULT = 0
    PNG_FILTER_TYPE_DEFAULT = 0
    
    #tmp.PNG_TRANSFORM_IDENTITY = 0
    #tmp.PNG_TRANSFORM_STRIP_16 = 1  #16 bit to 8 bit
    #tmp.PNG_TRANSFORM_PACKING = 4    #samples of 1/2/4 bits -> 8 bits
    #tmp.PNG_TRANSFORM_EXPAND = 16     #palette -> truecolor, grayscale to 8 bits
    PNG_COLOR_MASK_COLOR = 2
    PNG_COLOR_MASK_ALPHA = 4
    PNG_COLOR_TYPE_RGB = PNG_COLOR_MASK_COLOR
    PNG_COLOR_TYPE_RGB_ALPHA = PNG_COLOR_MASK_COLOR | PNG_COLOR_MASK_ALPHA
    #PNG_TRANSFORM_BGR = 0x80


    tjInitDecompress = libjpeg.tjInitDecompress
    tjInitDecompress.argtypes = []
    tjInitDecompress.restype = c_void_p
    
    tjDecompressHeader3 = libjpeg.tjDecompressHeader3
    tjDecompressHeader3.argtypes = [c_void_p,
        c_void_p, c_long, POINTER(c_int),
        POINTER(c_int), POINTER(c_int), POINTER(c_int) ]
    tjDecompressHeader3.restype = c_int
    
    tjDestroy = libjpeg.tjDestroy
    tjDestroy.argtypes = [c_void_p]
    tjDestroy.restype = c_int
    
    tjDecompress2 = libjpeg.tjDecompress2
    tjDecompress2.argtypes = [c_void_p, c_void_p, c_long,
        c_void_p, c_int, c_int, c_int, c_int, c_int]
    tjDecompress2.restype = c_int
    
    TJPF_RGBA = 7
    
    def loadJpeg(data):
    
        #cinfo.out_color_space = JCS_EXT_BGR
        #jpeg_mem_src
        
        handle = tjInitDecompress()
        
        w=c_int()
        h=c_int()
        subsamp = c_int()
        colorspace = c_int()
        
        rv = tjDecompressHeader3( handle , data, len(data), 
            byref(w), byref(h), byref(subsamp), byref(colorspace) )
        if rv != 0:
            raise RuntimeError("Cannot decompress JPEG header")
            
        w=w.value
        h=h.value

        pix = bytearray(w*h*4)
        
        rv = tjDecompress2( handle, data, len(data), 
            (c_uint8*len(pix)).from_buffer(pix), 
            w,w*4,h,
            TJPF_RGBA, 0 )
        if rv != 0:
            raise RuntimeError("Cannot decompress JPEG")
        
        tjDestroy(handle)
        return w,h,"RGBA8",pix

    def load(data):
        if compare( data, pngHeader ):
            return loadPng(data)
        if compare( data, jpgHeader):
            return loadJpeg(data)
        raise RuntimeError("No codec")
    
    def loadPng(data):
        ps = png_create_read_struct(png_get_libpng_ver(0),None,None,None)
        ip = png_create_info_struct(ps)
        dataBuff = (c_ubyte * len(data))(*data)
        soffset=0
        def loadCallback(ps, out, numToRead):
            #first = png_struct pointer
            #second = png_bytep
            #third = png_size_t
            nonlocal soffset
            #copy numToRead bytes from data[dataIndex:] to out
            #which is a void pointer
            tmp = byref(dataBuff,soffset)
            for i in range(numToRead):
                out[i] = dataBuff[soffset+i]
            soffset += numToRead
            
        noGarbageCollectPlz = ReadCallback_t( loadCallback )
        png_set_read_fn(ps, c_void_p(0), noGarbageCollectPlz )
        png_read_info(ps,ip)
        colorType = png_get_color_type(ps,ip)
        bitDepth = png_get_bit_depth(ps,ip)
        
        #png_set_bgr(ps)
        png_set_swap(ps)
        png_set_tRNS_to_alpha(ps)
        png_set_palette_to_rgb(ps)
        png_set_add_alpha(ps,0xffffff,1)
        #png_set_expand_gray_1_2_4_to_8(ps);
        png_set_gray_to_rgb(ps)
        png_set_expand(ps);
        
        if bitDepth <= 8:
            #we do gray -> rgb and palette -> rgb above
            Bpp = 4
            fmt="RGBA8"
        elif bitDepth == 16:
            Bpp = 8
            fmt="RGBA16"
        else:
            raise RuntimeError("Bad bit depth")
            
        w = png_get_image_width(ps,ip)
        h = png_get_image_height(ps,ip)
        
        pix = bytearray(w*h*Bpp)
        buff = (c_uint8*len(pix)).from_buffer(pix)

        for i in range(h):
            loc = (i)*w*Bpp
            png_read_row(ps,byref(buff,loc),c_void_p(0))
            
        png_destroy_read_struct(ps, ip, c_void_p(0) )
        return (w,h,fmt,pix)
    
    def savePng(w,h,fmt,data):
        ps = png_create_write_struct(png_get_libpng_ver(0),None,None,None)
        ip = png_create_info_struct(ps)
        if fmt == "RGB8":
            bitDepth=8
            colorType = PNG_COLOR_TYPE_RGB
            incr = 3*w
        elif fmt == "RGBA8":
            bitDepth=8
            colorType = PNG_COLOR_TYPE_RGB_ALPHA
            incr = 4*w
        elif fmt == "RGB16":
            bitDepth=16
            colorType = PNG_COLOR_TYPE_RGB
            incr = 6*w
        elif fmt == "RGBA16":
            bitDepth=16
            colorType = PNG_COLOR_TYPE_RGB_ALPHA
            incr = 8*w
        else:
            raise RuntimeError("Unknown format: "+fmt)
            
        outio = io.BytesIO()
        def writeCallback(ps, out, numToWrite):
            tmp = out[0:numToWrite]
            tmp = bytes(tmp)
            outio.write( tmp )
        def flushCallback(ps):
            pass
            
        wc = WriteCallback_t(writeCallback)
        fc = FlushCallback_t(flushCallback)
        png_set_write_fn(ps, c_void_p(0), wc, fc )

        #png_set_swap(ps)
            
        png_set_IHDR( ps, ip, w,h, bitDepth, colorType, 
            PNG_INTERLACE_NONE, 
            PNG_COMPRESSION_TYPE_DEFAULT, 
            PNG_FILTER_TYPE_DEFAULT)
                
                

        png_write_info( ps, ip )
        #png_set_bgr(ps)

        #byteswap
        if fmt == "RGBA16" or fmt == "RGB16":
            #the png_set_swap doesn't have any effect...
            data = bytearray(data)
            for i in range(0,len(data),2):
                tmp=data[i]
                data[i]=data[i+1]
                data[i+1]=tmp
                
        buff = create_string_buffer(bytes(data),len(data))
        addr = addressof(buff)
        cc=0
        for y in range(h):  
            png_write_row(ps, addr)
            addr += incr
        png_write_end(ps,ip)
        png_destroy_write_struct(ps,ip)
        
        return outio.getbuffer()
        
    return (load,savePng)
    
def OSX():
    if not typing.TYPE_CHECKING:
        import pngpyglet
        def load(data):
            if type(data) != bytes and type(data) != bytearray:
                raise Exception("Need bytes or bytearray for PNG decode")
            p = pngpyglet.Reader(bytes=data)
            #w,h,pix,meta = p.read_flat() 
            w,h,rows,meta = p.asDirect() 

            tmp = bytearray(w*h*4)
            j=0
            if meta["greyscale"]:
                if meta["alpha"]:
                    for row in rows:
                        i=0
                        while i < len(row):
                            val = row[i]
                            alpha = row[i+1]
                            i+=2
                            tmp[j] = val
                            tmp[j+1] = val
                            tmp[j+2] = val
                            tmp[j+3] = alpha
                            j+=4
                else:
                    for row in rows:
                        i=0
                        while i < len(row):
                            val = row[i]
                            i+=1
                            tmp[j] = val
                            tmp[j+1] = val
                            tmp[j+2] = val
                            tmp[j+3] = 255
                            j+=4
            else:
                if meta["alpha"]:
                    for row in rows:
                        i=0
                        while i < len(row):
                            r = row[i]
                            g = row[i+1]
                            b = row[i+2]
                            a = row[i+3]
                            i+=4
                            tmp[j] = r
                            tmp[j+1] = g
                            tmp[j+2] = b
                            tmp[j+3] = a
                            j+=4        
                else:
                    for row in rows:
                        i=0
                        while i < len(row):
                            r = row[i]
                            g = row[i+1]
                            b = row[i+2]
                            i+=3
                            tmp[j] = r
                            tmp[j+1] = g
                            tmp[j+2] = b
                            tmp[j+3] = 255
                            j+=4
            
            return w,h,"RGBA8",tmp

        def save(w,h,fmt,data):
            if fmt == "RGBA8":
                wr = pngpyglet.Writer(width=w,height=h,alpha=True)
                tmpf = io.BytesIO()
                wr.write_array(tmpf,data)
                return tmpf.getvalue()
            else:
                assert 0
        return (load,save)
        
        
        
def unimplemented(*x):
    raise RuntimeError("Not implemented")
def decodeStub(data: bytearray) -> typing.Tuple[int,int,str,bytearray] :
    return (0,0,"",bytearray(0))
def encodePNGStub(w:int, h:int, fmt: str, data: typing.Union[bytes,bytearray]) -> bytes:
    pass
    
decode = decodeStub
encodePNG = encodePNGStub

def initialize():
    global decode, encodePNG
    if sys.platform == "linux":
        decode, encodePNG = Linux()
    elif sys.platform == "win32":
        decode, encodePNG = Win32()    
    else:
        decode, encodePNG = OSX()


def encodeBMP(w: int,h: int,fmt: str,pix: typing.Union[bytes,bytearray]):
    fp = io.BytesIO()
    
    class BitmapHeader(Structure):
        _pack_ = 1
        _fields_ = [
            ("sig",c_ushort),               #BM
            ("size",c_uint),                #size of whole file
            ("reserved",c_uint),
            ("offset",c_uint),            #size of header
            ("header_size",c_uint),       #size of rest of header
            ("width",c_uint),             #bitmap size
            ("height",c_uint),           #ditto
            ("planes",c_ushort),            #always 1
            ("bpp",c_ushort),               #24 = true color
            ("compression",c_uint),       #0 = none
            ("img_size",c_uint),          #bytes in the image
            ("ppm_x",c_uint),             #pixels per meter, x
            ("ppm_y",c_uint),             #same for y dimension
            ("ncolors",c_uint),           #how many colors?
            ("icolors",c_uint)           #important ones
        ]
    rowsize = w*3
    if rowsize % 4 == 0:
        padding=0
    else:
        padding = 4-(rowsize%4)
    pitch = rowsize + padding
    hdr = BitmapHeader()
    hdr.sig = 0x4d42
    hdr.size = pitch*h+sizeof(BitmapHeader)
    hdr.reserved = 0
    hdr.offset = sizeof(BitmapHeader)
    hdr.header_size = 40 #sizeof(BitmapHeader)
    hdr.width = w
    hdr.height = h
    hdr.planes = 1
    hdr.bpp = 24
    hdr.compression = 0
    hdr.img_size = 3*w*h
    hdr.ppm_x = 2834
    hdr.ppm_y = 2834
    hdr.ncolors = 0
    hdr.icolors = 0
    #there should be a more efficient way to do this...
    tmp = ((c_ubyte)*sizeof(hdr))()    
    memmove((tmp),byref(hdr),sizeof(hdr))
    bb=bytearray(sizeof(hdr))
    for i in range(len(bb)):
        v = tmp[i]
        bb[i] = v
    fp.write(bb)
    pd = bytearray(padding)

    if fmt == "RGBA8":
        tmp2 = bytearray(w*3)
        i=0
        for y in range(h):
            j=0
            for x in range(w):
                tmp2[j] = pix[i+2]   #blue
                tmp2[j+1]=pix[i+1]   #green
                tmp2[j+2]=pix[i]     #red
                i+=4
                j+=3
            fp.write(tmp2)
            fp.write(pd)
            
    elif fmt == "RGBA16":
        tmp2 = bytearray(w*3)
        i=0
        for y in range(h):
            j=0
            for x in range(w):
                tmp2[j] = pix[i+5]   #blue, msb
                tmp2[j+1]=pix[i+3]   #green
                tmp2[j+2]=pix[i+1]     #red
                i+=8
                j+=3
            fp.write(tmp2)
            fp.write(pd)
    else:
        raise RuntimeError("Bad format: "+fmt)
        
    
    return fp.getbuffer()

def flipY(w:int,h:int,pix:typing.Union[bytearray,bytes]) -> bytearray:
    pitch=w*4
    j=pitch*(h-1)
    outpix=bytearray(w*h*4)
    i=0
    while j >= 0:
        outpix[i:i+pitch] = pix[j:j+w*4]
        i += pitch
        j -= pitch
    return outpix
        
initialize()

def test(fn):        
    print("=====",fn,"======")
    data = open(fn,"rb").read()
    w,h,fmt,pix = decode(data)
    print(w,"x",h,"fmt=",fmt)
            
    fp=open(fn+".bmp","wb")    
    fp.write(encodeBMP(w,h,fmt,pix))
    fp.close()
    print("Wrote",fn+".bmp")
    
    fp=open(fn+".png", "wb")
    fp.write(encodePNG(w,h,fmt,pix))
    fp.close()
    print("Wrote",fn+".png")


    if fmt == "RGBA8":
        incr=4
    elif fmt == "RGBA16":
        incr=8
    else:
        print(fmt)
        assert 0
    
    
    i=0
    for j in range(4):
        if fmt == "RGBA8":
            r=pix[i]
            g=pix[i+1]
            b=pix[i+2]
            a=pix[i+3]
            i+=4
        elif fmt == "RGBA16":
            r=pix[i] | (pix[i+1]<<8)
            g=pix[i+2] | (pix[i+3]<<8)
            b=pix[i+4] | (pix[i+5]<<8)
            a=pix[i+6] | (pix[i+7]<<8)
            i+=8
        else:
            assert 0
     
        print(r,g,b,a,end=" | ")
        
        try:
            if "grey" not in fn and ".jpg" not in fn:
                if j == 0:
                    assert r>g and r>b
                elif j == 1:
                    assert g>r and g>b
                elif j==2:
                    assert b>r and b>g
        except AssertionError:
            print()
            print()
            print(j)
            print(r,g,b)
            print()
            raise
        
        assert (a == 255 or a == 65535)

    print()

if __name__ == "__main__":
    files= ["grey8.png","palette.png","rgb16.png","rgb8.png","rgba8.png",
            "greynoalpha.png","rgb8.jpg","rgba16.png"]
    
    for fn in files:
        try:
            test(fn)
        except Exception as e:
            print("FAILED:",fn,e)

    print(".-.-.-.-.-.")
    w=200
    h=100
    pix=bytearray(w*h*4)
    i=0
    j=0
    for i in range(10):
        pix[j] = 255; j+=1
        pix[j] = 0; j+=1
        pix[j] = 0; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
    for i in range(10):
        pix[j] = 0; j+=1
        pix[j] = 255; j+=1
        pix[j] = 0; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
    for i in range(10):
        pix[j] = 0; j+=1
        pix[j] = 0; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
        pix[j] = 255; j+=1
    
    tmp = encodePNG(w,h,"RGBA8",pix)
    fp=open("synthetic.png.png", "wb")
    fp.write(tmp)
    fp.close()
    print("Wrote synthetic.png.png")

    
    print("\n------------------")
    

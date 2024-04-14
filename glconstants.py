# This file is based on gl.xml, which has
# the following copyright:
# 
# Copyright (c) 2013-2019 The Khronos Group Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# ------------------------------------------------------------------------
# 
# This file, gl.xml, is the OpenGL and OpenGL API Registry. The canonical
# version of the registry, together with documentation, schema, and Python
# generator scripts used to generate C header files for OpenGL and OpenGL ES,
# can always be found in the Khronos Registry at
#         https://github.com/KhronosGroup/OpenGL-Registry
#     
glgroups= {'AccumOp': ['GL_ACCUM', 'GL_LOAD', 'GL_RETURN', 'GL_MULT', 'GL_ADD'],
 'AlphaFunction': ['GL_ALWAYS',
                   'GL_EQUAL',
                   'GL_GEQUAL',
                   'GL_GREATER',
                   'GL_LEQUAL',
                   'GL_LESS',
                   'GL_NEVER',
                   'GL_NOTEQUAL'],
 'ArrayObjectPNameATI': [],
 'ArrayObjectUsageATI': [],
 'AtomicCounterBufferPName': ['GL_ATOMIC_COUNTER_BUFFER_BINDING',
                              'GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE',
                              'GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS',
                              'GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES',
                              'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER',
                              'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER',
                              'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER',
                              'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER',
                              'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER',
                              'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER'],
 'AttribMask': ['GL_ACCUM_BUFFER_BIT',
                'GL_ALL_ATTRIB_BITS',
                'GL_COLOR_BUFFER_BIT',
                'GL_CURRENT_BIT',
                'GL_DEPTH_BUFFER_BIT',
                'GL_ENABLE_BIT',
                'GL_EVAL_BIT',
                'GL_FOG_BIT',
                'GL_HINT_BIT',
                'GL_LIGHTING_BIT',
                'GL_LINE_BIT',
                'GL_LIST_BIT',
                'GL_MULTISAMPLE_BIT',
                'GL_MULTISAMPLE_BIT_3DFX',
                'GL_MULTISAMPLE_BIT_ARB',
                'GL_MULTISAMPLE_BIT_EXT',
                'GL_PIXEL_MODE_BIT',
                'GL_POINT_BIT',
                'GL_POLYGON_BIT',
                'GL_POLYGON_STIPPLE_BIT',
                'GL_SCISSOR_BIT',
                'GL_STENCIL_BUFFER_BIT',
                'GL_TEXTURE_BIT',
                'GL_TRANSFORM_BIT',
                'GL_VIEWPORT_BIT'],
 'AttributeType': ['GL_FLOAT_VEC2',
                   'GL_FLOAT_VEC2_ARB',
                   'GL_FLOAT_VEC3',
                   'GL_FLOAT_VEC3_ARB',
                   'GL_FLOAT_VEC4',
                   'GL_FLOAT_VEC4_ARB',
                   'GL_INT_VEC2',
                   'GL_INT_VEC2_ARB',
                   'GL_INT_VEC3',
                   'GL_INT_VEC3_ARB',
                   'GL_INT_VEC4',
                   'GL_INT_VEC4_ARB',
                   'GL_BOOL',
                   'GL_BOOL_ARB',
                   'GL_BOOL_VEC2',
                   'GL_BOOL_VEC2_ARB',
                   'GL_BOOL_VEC3',
                   'GL_BOOL_VEC3_ARB',
                   'GL_BOOL_VEC4',
                   'GL_BOOL_VEC4_ARB',
                   'GL_FLOAT_MAT2',
                   'GL_FLOAT_MAT2_ARB',
                   'GL_FLOAT_MAT3',
                   'GL_FLOAT_MAT3_ARB',
                   'GL_FLOAT_MAT4',
                   'GL_FLOAT_MAT4_ARB',
                   'GL_FLOAT_MAT2x3',
                   'GL_FLOAT_MAT2x4',
                   'GL_FLOAT_MAT3x2',
                   'GL_FLOAT_MAT3x4',
                   'GL_FLOAT_MAT4x2',
                   'GL_FLOAT_MAT4x3'],
 'BindTransformFeedbackTarget': ['GL_TRANSFORM_FEEDBACK'],
 'BinormalPointerTypeEXT': ['GL_BYTE_EXT',
                            'GL_SHORT_EXT',
                            'GL_FLOAT_EXT',
                            'GL_DOUBLE_EXT'],
 'BlendEquationModeEXT': ['GL_FUNC_ADD',
                          'GL_FUNC_ADD_EXT',
                          'GL_FUNC_REVERSE_SUBTRACT',
                          'GL_FUNC_REVERSE_SUBTRACT_EXT',
                          'GL_FUNC_SUBTRACT',
                          'GL_FUNC_SUBTRACT_EXT',
                          'GL_MAX',
                          'GL_MAX_EXT',
                          'GL_MIN',
                          'GL_MIN_EXT'],
 'BlendingFactor': ['GL_ZERO',
                    'GL_ONE',
                    'GL_SRC_COLOR',
                    'GL_ONE_MINUS_SRC_COLOR',
                    'GL_DST_COLOR',
                    'GL_ONE_MINUS_DST_COLOR',
                    'GL_SRC_ALPHA',
                    'GL_ONE_MINUS_SRC_ALPHA',
                    'GL_DST_ALPHA',
                    'GL_ONE_MINUS_DST_ALPHA',
                    'GL_CONSTANT_COLOR',
                    'GL_ONE_MINUS_CONSTANT_COLOR',
                    'GL_CONSTANT_ALPHA',
                    'GL_ONE_MINUS_CONSTANT_ALPHA',
                    'GL_SRC_ALPHA_SATURATE',
                    'GL_SRC1_COLOR',
                    'GL_ONE_MINUS_SRC1_COLOR',
                    'GL_SRC1_ALPHA',
                    'GL_ONE_MINUS_SRC1_ALPHA'],
 'BlitFramebufferFilter': ['GL_NEAREST', 'GL_LINEAR'],
 'Boolean': ['GL_FALSE', 'GL_TRUE'],
 'Buffer': ['GL_COLOR', 'GL_DEPTH', 'GL_STENCIL'],
 'BufferAccessARB': ['GL_READ_ONLY', 'GL_WRITE_ONLY', 'GL_READ_WRITE'],
 'BufferBitQCOM': [],
 'BufferPNameARB': ['GL_BUFFER_SIZE_ARB',
                    'GL_BUFFER_USAGE_ARB',
                    'GL_BUFFER_ACCESS_ARB',
                    'GL_BUFFER_MAPPED_ARB',
                    'GL_BUFFER_SIZE',
                    'GL_BUFFER_USAGE',
                    'GL_BUFFER_ACCESS',
                    'GL_BUFFER_ACCESS_FLAGS',
                    'GL_BUFFER_IMMUTABLE_STORAGE',
                    'GL_BUFFER_MAPPED',
                    'GL_BUFFER_MAP_OFFSET',
                    'GL_BUFFER_MAP_LENGTH',
                    'GL_BUFFER_STORAGE_FLAGS'],
 'BufferPointerNameARB': ['GL_BUFFER_MAP_POINTER_ARB', 'GL_BUFFER_MAP_POINTER'],
 'BufferStorageMask': ['GL_CLIENT_STORAGE_BIT',
                       'GL_CLIENT_STORAGE_BIT_EXT',
                       'GL_DYNAMIC_STORAGE_BIT',
                       'GL_DYNAMIC_STORAGE_BIT_EXT',
                       'GL_MAP_COHERENT_BIT',
                       'GL_MAP_COHERENT_BIT_EXT',
                       'GL_MAP_PERSISTENT_BIT',
                       'GL_MAP_PERSISTENT_BIT_EXT',
                       'GL_MAP_READ_BIT',
                       'GL_MAP_READ_BIT_EXT',
                       'GL_MAP_WRITE_BIT',
                       'GL_MAP_WRITE_BIT_EXT',
                       'GL_SPARSE_STORAGE_BIT_ARB',
                       'GL_LGPU_SEPARATE_STORAGE_BIT_NVX'],
 'BufferStorageTarget': ['GL_ARRAY_BUFFER',
                         'GL_ATOMIC_COUNTER_BUFFER',
                         'GL_COPY_READ_BUFFER',
                         'GL_COPY_WRITE_BUFFER',
                         'GL_DISPATCH_INDIRECT_BUFFER',
                         'GL_DRAW_INDIRECT_BUFFER',
                         'GL_ELEMENT_ARRAY_BUFFER',
                         'GL_PIXEL_PACK_BUFFER',
                         'GL_PIXEL_UNPACK_BUFFER',
                         'GL_QUERY_BUFFER',
                         'GL_SHADER_STORAGE_BUFFER',
                         'GL_TEXTURE_BUFFER',
                         'GL_TRANSFORM_FEEDBACK_BUFFER',
                         'GL_UNIFORM_BUFFER'],
 'BufferTargetARB': ['GL_ARRAY_BUFFER',
                     'GL_ATOMIC_COUNTER_BUFFER',
                     'GL_COPY_READ_BUFFER',
                     'GL_COPY_WRITE_BUFFER',
                     'GL_DISPATCH_INDIRECT_BUFFER',
                     'GL_DRAW_INDIRECT_BUFFER',
                     'GL_ELEMENT_ARRAY_BUFFER',
                     'GL_PIXEL_PACK_BUFFER',
                     'GL_PIXEL_UNPACK_BUFFER',
                     'GL_QUERY_BUFFER',
                     'GL_SHADER_STORAGE_BUFFER',
                     'GL_TEXTURE_BUFFER',
                     'GL_TRANSFORM_FEEDBACK_BUFFER',
                     'GL_UNIFORM_BUFFER',
                     'GL_PARAMETER_BUFFER'],
 'BufferUsageARB': ['GL_STREAM_DRAW',
                    'GL_STREAM_READ',
                    'GL_STREAM_COPY',
                    'GL_STATIC_DRAW',
                    'GL_STATIC_READ',
                    'GL_STATIC_COPY',
                    'GL_DYNAMIC_DRAW',
                    'GL_DYNAMIC_READ',
                    'GL_DYNAMIC_COPY'],
 'CheckFramebufferStatusTarget': ['GL_DRAW_FRAMEBUFFER',
                                  'GL_READ_FRAMEBUFFER',
                                  'GL_FRAMEBUFFER'],
 'ClampColorModeARB': ['GL_FIXED_ONLY_ARB',
                       'GL_FALSE',
                       'GL_TRUE',
                       'GL_TRUE',
                       'GL_FALSE',
                       'GL_FIXED_ONLY'],
 'ClampColorTargetARB': ['GL_CLAMP_VERTEX_COLOR_ARB',
                         'GL_CLAMP_FRAGMENT_COLOR_ARB',
                         'GL_CLAMP_READ_COLOR_ARB',
                         'GL_CLAMP_READ_COLOR'],
 'ClearBufferMask': ['GL_ACCUM_BUFFER_BIT',
                     'GL_COLOR_BUFFER_BIT',
                     'GL_DEPTH_BUFFER_BIT',
                     'GL_STENCIL_BUFFER_BIT'],
 'ClientAttribMask': ['GL_CLIENT_ALL_ATTRIB_BITS',
                      'GL_CLIENT_PIXEL_STORE_BIT',
                      'GL_CLIENT_VERTEX_ARRAY_BIT'],
 'ClipControlDepth': ['GL_NEGATIVE_ONE_TO_ONE', 'GL_ZERO_TO_ONE'],
 'ClipControlOrigin': ['GL_LOWER_LEFT', 'GL_UPPER_LEFT'],
 'ClipPlaneName': ['GL_CLIP_DISTANCE0',
                   'GL_CLIP_DISTANCE1',
                   'GL_CLIP_DISTANCE2',
                   'GL_CLIP_DISTANCE3',
                   'GL_CLIP_DISTANCE4',
                   'GL_CLIP_DISTANCE5',
                   'GL_CLIP_DISTANCE6',
                   'GL_CLIP_DISTANCE7',
                   'GL_CLIP_PLANE0',
                   'GL_CLIP_PLANE1',
                   'GL_CLIP_PLANE2',
                   'GL_CLIP_PLANE3',
                   'GL_CLIP_PLANE4',
                   'GL_CLIP_PLANE5'],
 'ColorBuffer': ['GL_NONE',
                 'GL_FRONT_LEFT',
                 'GL_FRONT_RIGHT',
                 'GL_BACK_LEFT',
                 'GL_BACK_RIGHT',
                 'GL_FRONT',
                 'GL_BACK',
                 'GL_LEFT',
                 'GL_RIGHT',
                 'GL_FRONT_AND_BACK',
                 'GL_COLOR_ATTACHMENT0',
                 'GL_COLOR_ATTACHMENT1',
                 'GL_COLOR_ATTACHMENT2',
                 'GL_COLOR_ATTACHMENT3',
                 'GL_COLOR_ATTACHMENT4',
                 'GL_COLOR_ATTACHMENT5',
                 'GL_COLOR_ATTACHMENT6',
                 'GL_COLOR_ATTACHMENT7',
                 'GL_COLOR_ATTACHMENT8',
                 'GL_COLOR_ATTACHMENT9',
                 'GL_COLOR_ATTACHMENT10',
                 'GL_COLOR_ATTACHMENT11',
                 'GL_COLOR_ATTACHMENT12',
                 'GL_COLOR_ATTACHMENT13',
                 'GL_COLOR_ATTACHMENT14',
                 'GL_COLOR_ATTACHMENT15',
                 'GL_COLOR_ATTACHMENT16',
                 'GL_COLOR_ATTACHMENT17',
                 'GL_COLOR_ATTACHMENT18',
                 'GL_COLOR_ATTACHMENT19',
                 'GL_COLOR_ATTACHMENT20',
                 'GL_COLOR_ATTACHMENT21',
                 'GL_COLOR_ATTACHMENT22',
                 'GL_COLOR_ATTACHMENT23',
                 'GL_COLOR_ATTACHMENT24',
                 'GL_COLOR_ATTACHMENT25',
                 'GL_COLOR_ATTACHMENT26',
                 'GL_COLOR_ATTACHMENT27',
                 'GL_COLOR_ATTACHMENT28',
                 'GL_COLOR_ATTACHMENT29',
                 'GL_COLOR_ATTACHMENT30',
                 'GL_COLOR_ATTACHMENT31'],
 'ColorMaterialFace': ['GL_BACK', 'GL_FRONT', 'GL_FRONT_AND_BACK'],
 'ColorMaterialParameter': ['GL_AMBIENT',
                            'GL_AMBIENT_AND_DIFFUSE',
                            'GL_DIFFUSE',
                            'GL_EMISSION',
                            'GL_SPECULAR'],
 'ColorPointerType': ['GL_BYTE',
                      'GL_DOUBLE',
                      'GL_FLOAT',
                      'GL_INT',
                      'GL_SHORT',
                      'GL_UNSIGNED_BYTE',
                      'GL_UNSIGNED_INT',
                      'GL_UNSIGNED_SHORT'],
 'ColorTableParameterPNameSGI': ['GL_COLOR_TABLE_BIAS', 'GL_COLOR_TABLE_SCALE'],
 'ColorTableTarget': ['GL_COLOR_TABLE',
                      'GL_POST_CONVOLUTION_COLOR_TABLE',
                      'GL_POST_COLOR_MATRIX_COLOR_TABLE'],
 'ColorTableTargetSGI': ['GL_COLOR_TABLE',
                         'GL_POST_COLOR_MATRIX_COLOR_TABLE',
                         'GL_POST_CONVOLUTION_COLOR_TABLE',
                         'GL_PROXY_COLOR_TABLE',
                         'GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE',
                         'GL_PROXY_POST_CONVOLUTION_COLOR_TABLE'],
 'CombinerBiasNV': ['GL_NONE'],
 'CombinerComponentUsageNV': [],
 'CombinerMappingNV': [],
 'CombinerParameterNV': [],
 'CombinerPortionNV': [],
 'CombinerRegisterNV': ['GL_TEXTURE0_ARB', 'GL_TEXTURE1_ARB'],
 'CombinerScaleNV': ['GL_NONE'],
 'CombinerStageNV': [],
 'CombinerVariableNV': [],
 'ConditionalRenderMode': ['GL_QUERY_WAIT',
                           'GL_QUERY_NO_WAIT',
                           'GL_QUERY_BY_REGION_WAIT',
                           'GL_QUERY_BY_REGION_NO_WAIT',
                           'GL_QUERY_WAIT_INVERTED',
                           'GL_QUERY_NO_WAIT_INVERTED',
                           'GL_QUERY_BY_REGION_WAIT_INVERTED',
                           'GL_QUERY_BY_REGION_NO_WAIT_INVERTED'],
 'ContextFlagMask': ['GL_CONTEXT_FLAG_DEBUG_BIT',
                     'GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT',
                     'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT',
                     'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB',
                     'GL_CONTEXT_FLAG_PROTECTED_CONTENT_BIT_EXT',
                     'GL_CONTEXT_FLAG_NO_ERROR_BIT'],
 'ContextProfileMask': ['GL_CONTEXT_COMPATIBILITY_PROFILE_BIT',
                        'GL_CONTEXT_CORE_PROFILE_BIT'],
 'ConvolutionBorderModeEXT': ['GL_REDUCE', 'GL_REDUCE_EXT'],
 'ConvolutionParameterEXT': ['GL_CONVOLUTION_BORDER_MODE',
                             'GL_CONVOLUTION_BORDER_MODE_EXT',
                             'GL_CONVOLUTION_FILTER_BIAS',
                             'GL_CONVOLUTION_FILTER_BIAS_EXT',
                             'GL_CONVOLUTION_FILTER_SCALE',
                             'GL_CONVOLUTION_FILTER_SCALE_EXT'],
 'ConvolutionTarget': ['GL_CONVOLUTION_1D', 'GL_CONVOLUTION_2D'],
 'ConvolutionTargetEXT': ['GL_CONVOLUTION_1D',
                          'GL_CONVOLUTION_1D_EXT',
                          'GL_CONVOLUTION_2D',
                          'GL_CONVOLUTION_2D_EXT'],
 'CopyBufferSubDataTarget': ['GL_ARRAY_BUFFER',
                             'GL_ATOMIC_COUNTER_BUFFER',
                             'GL_COPY_READ_BUFFER',
                             'GL_COPY_WRITE_BUFFER',
                             'GL_DISPATCH_INDIRECT_BUFFER',
                             'GL_DRAW_INDIRECT_BUFFER',
                             'GL_ELEMENT_ARRAY_BUFFER',
                             'GL_PIXEL_PACK_BUFFER',
                             'GL_PIXEL_UNPACK_BUFFER',
                             'GL_QUERY_BUFFER',
                             'GL_SHADER_STORAGE_BUFFER',
                             'GL_TEXTURE_BUFFER',
                             'GL_TRANSFORM_FEEDBACK_BUFFER',
                             'GL_UNIFORM_BUFFER'],
 'CopyImageSubDataTarget': ['GL_RENDERBUFFER',
                            'GL_TEXTURE_1D',
                            'GL_TEXTURE_2D',
                            'GL_TEXTURE_3D',
                            'GL_TEXTURE_RECTANGLE',
                            'GL_TEXTURE_CUBE_MAP',
                            'GL_TEXTURE_CUBE_MAP_ARRAY',
                            'GL_TEXTURE_1D_ARRAY',
                            'GL_TEXTURE_2D_ARRAY',
                            'GL_TEXTURE_2D_MULTISAMPLE',
                            'GL_TEXTURE_2D_MULTISAMPLE_ARRAY'],
 'CullFaceMode': ['GL_BACK', 'GL_FRONT', 'GL_FRONT_AND_BACK'],
 'CullParameterEXT': ['GL_CULL_VERTEX_EYE_POSITION_EXT',
                      'GL_CULL_VERTEX_OBJECT_POSITION_EXT'],
 'DataType': [],
 'DataTypeEXT': ['GL_SCALAR_EXT', 'GL_VECTOR_EXT', 'GL_MATRIX_EXT'],
 'DebugSeverity': ['GL_DEBUG_SEVERITY_LOW',
                   'GL_DEBUG_SEVERITY_MEDIUM',
                   'GL_DEBUG_SEVERITY_HIGH',
                   'GL_DEBUG_SEVERITY_NOTIFICATION',
                   'GL_DONT_CARE'],
 'DebugSource': ['GL_DEBUG_SOURCE_API',
                 'GL_DEBUG_SOURCE_WINDOW_SYSTEM',
                 'GL_DEBUG_SOURCE_SHADER_COMPILER',
                 'GL_DEBUG_SOURCE_THIRD_PARTY',
                 'GL_DEBUG_SOURCE_APPLICATION',
                 'GL_DEBUG_SOURCE_OTHER',
                 'GL_DONT_CARE'],
 'DebugType': ['GL_DEBUG_TYPE_ERROR',
               'GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR',
               'GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR',
               'GL_DEBUG_TYPE_PORTABILITY',
               'GL_DEBUG_TYPE_PERFORMANCE',
               'GL_DEBUG_TYPE_MARKER',
               'GL_DEBUG_TYPE_PUSH_GROUP',
               'GL_DEBUG_TYPE_POP_GROUP',
               'GL_DEBUG_TYPE_OTHER',
               'GL_DONT_CARE'],
 'DepthFunction': ['GL_ALWAYS',
                   'GL_EQUAL',
                   'GL_GEQUAL',
                   'GL_GREATER',
                   'GL_LEQUAL',
                   'GL_LESS',
                   'GL_NEVER',
                   'GL_NOTEQUAL'],
 'DrawBufferMode': ['GL_AUX0',
                    'GL_AUX1',
                    'GL_AUX2',
                    'GL_AUX3',
                    'GL_BACK',
                    'GL_BACK_LEFT',
                    'GL_BACK_RIGHT',
                    'GL_FRONT',
                    'GL_FRONT_AND_BACK',
                    'GL_FRONT_LEFT',
                    'GL_FRONT_RIGHT',
                    'GL_LEFT',
                    'GL_NONE',
                    'GL_RIGHT',
                    'GL_COLOR_ATTACHMENT0',
                    'GL_COLOR_ATTACHMENT1',
                    'GL_COLOR_ATTACHMENT2',
                    'GL_COLOR_ATTACHMENT3',
                    'GL_COLOR_ATTACHMENT4',
                    'GL_COLOR_ATTACHMENT5',
                    'GL_COLOR_ATTACHMENT6',
                    'GL_COLOR_ATTACHMENT7',
                    'GL_COLOR_ATTACHMENT8',
                    'GL_COLOR_ATTACHMENT9',
                    'GL_COLOR_ATTACHMENT10',
                    'GL_COLOR_ATTACHMENT11',
                    'GL_COLOR_ATTACHMENT12',
                    'GL_COLOR_ATTACHMENT13',
                    'GL_COLOR_ATTACHMENT14',
                    'GL_COLOR_ATTACHMENT15',
                    'GL_COLOR_ATTACHMENT16',
                    'GL_COLOR_ATTACHMENT17',
                    'GL_COLOR_ATTACHMENT18',
                    'GL_COLOR_ATTACHMENT19',
                    'GL_COLOR_ATTACHMENT20',
                    'GL_COLOR_ATTACHMENT21',
                    'GL_COLOR_ATTACHMENT22',
                    'GL_COLOR_ATTACHMENT23',
                    'GL_COLOR_ATTACHMENT24',
                    'GL_COLOR_ATTACHMENT25',
                    'GL_COLOR_ATTACHMENT26',
                    'GL_COLOR_ATTACHMENT27',
                    'GL_COLOR_ATTACHMENT28',
                    'GL_COLOR_ATTACHMENT29',
                    'GL_COLOR_ATTACHMENT30',
                    'GL_COLOR_ATTACHMENT31'],
 'DrawBufferModeATI': [],
 'DrawElementsType': ['GL_UNSIGNED_BYTE',
                      'GL_UNSIGNED_SHORT',
                      'GL_UNSIGNED_INT'],
 'ElementPointerTypeATI': [],
 'EnableCap': ['GL_ALPHA_TEST',
               'GL_AUTO_NORMAL',
               'GL_BLEND',
               'GL_CLIP_DISTANCE0',
               'GL_CLIP_DISTANCE1',
               'GL_CLIP_DISTANCE2',
               'GL_CLIP_DISTANCE3',
               'GL_CLIP_DISTANCE4',
               'GL_CLIP_DISTANCE5',
               'GL_CLIP_DISTANCE6',
               'GL_CLIP_DISTANCE7',
               'GL_CLIP_PLANE0',
               'GL_CLIP_PLANE1',
               'GL_CLIP_PLANE2',
               'GL_CLIP_PLANE3',
               'GL_CLIP_PLANE4',
               'GL_CLIP_PLANE5',
               'GL_COLOR_ARRAY',
               'GL_COLOR_LOGIC_OP',
               'GL_COLOR_MATERIAL',
               'GL_CONVOLUTION_1D_EXT',
               'GL_CONVOLUTION_2D_EXT',
               'GL_CULL_FACE',
               'GL_DEBUG_OUTPUT',
               'GL_DEBUG_OUTPUT_SYNCHRONOUS',
               'GL_DEPTH_CLAMP',
               'GL_DEPTH_TEST',
               'GL_DITHER',
               'GL_EDGE_FLAG_ARRAY',
               'GL_FOG',
               'GL_FRAMEBUFFER_SRGB',
               'GL_HISTOGRAM_EXT',
               'GL_INDEX_ARRAY',
               'GL_INDEX_LOGIC_OP',
               'GL_LIGHT0',
               'GL_LIGHT1',
               'GL_LIGHT2',
               'GL_LIGHT3',
               'GL_LIGHT4',
               'GL_LIGHT5',
               'GL_LIGHT6',
               'GL_LIGHT7',
               'GL_LIGHTING',
               'GL_LINE_SMOOTH',
               'GL_LINE_STIPPLE',
               'GL_MAP1_COLOR_4',
               'GL_MAP1_INDEX',
               'GL_MAP1_NORMAL',
               'GL_MAP1_TEXTURE_COORD_1',
               'GL_MAP1_TEXTURE_COORD_2',
               'GL_MAP1_TEXTURE_COORD_3',
               'GL_MAP1_TEXTURE_COORD_4',
               'GL_MAP1_VERTEX_3',
               'GL_MAP1_VERTEX_4',
               'GL_MAP2_COLOR_4',
               'GL_MAP2_INDEX',
               'GL_MAP2_NORMAL',
               'GL_MAP2_TEXTURE_COORD_1',
               'GL_MAP2_TEXTURE_COORD_2',
               'GL_MAP2_TEXTURE_COORD_3',
               'GL_MAP2_TEXTURE_COORD_4',
               'GL_MAP2_VERTEX_3',
               'GL_MAP2_VERTEX_4',
               'GL_MINMAX_EXT',
               'GL_MULTISAMPLE',
               'GL_NORMALIZE',
               'GL_NORMAL_ARRAY',
               'GL_POINT_SMOOTH',
               'GL_POLYGON_OFFSET_FILL',
               'GL_POLYGON_OFFSET_LINE',
               'GL_POLYGON_OFFSET_POINT',
               'GL_POLYGON_SMOOTH',
               'GL_POLYGON_STIPPLE',
               'GL_PRIMITIVE_RESTART',
               'GL_PRIMITIVE_RESTART_FIXED_INDEX',
               'GL_PROGRAM_POINT_SIZE',
               'GL_RASTERIZER_DISCARD',
               'GL_RESCALE_NORMAL_EXT',
               'GL_SAMPLE_ALPHA_TO_COVERAGE',
               'GL_SAMPLE_ALPHA_TO_ONE',
               'GL_SAMPLE_COVERAGE',
               'GL_SAMPLE_MASK',
               'GL_SAMPLE_SHADING',
               'GL_SCISSOR_TEST',
               'GL_SEPARABLE_2D_EXT',
               'GL_SHARED_TEXTURE_PALETTE_EXT',
               'GL_STENCIL_TEST',
               'GL_TEXTURE_1D',
               'GL_TEXTURE_2D',
               'GL_TEXTURE_3D_EXT',
               'GL_TEXTURE_COORD_ARRAY',
               'GL_TEXTURE_CUBE_MAP_SEAMLESS',
               'GL_TEXTURE_GEN_Q',
               'GL_TEXTURE_GEN_R',
               'GL_TEXTURE_GEN_S',
               'GL_TEXTURE_GEN_T',
               'GL_VERTEX_ARRAY'],
 'ErrorCode': ['GL_INVALID_ENUM',
               'GL_INVALID_FRAMEBUFFER_OPERATION',
               'GL_INVALID_FRAMEBUFFER_OPERATION_EXT',
               'GL_INVALID_OPERATION',
               'GL_INVALID_VALUE',
               'GL_NO_ERROR',
               'GL_OUT_OF_MEMORY',
               'GL_STACK_OVERFLOW',
               'GL_STACK_UNDERFLOW',
               'GL_TABLE_TOO_LARGE',
               'GL_TABLE_TOO_LARGE_EXT',
               'GL_TEXTURE_TOO_LARGE_EXT'],
 'EvalMapsModeNV': [],
 'EvalTargetNV': [],
 'ExternalHandleType': ['GL_HANDLE_TYPE_OPAQUE_FD_EXT',
                        'GL_HANDLE_TYPE_OPAQUE_WIN32_EXT',
                        'GL_HANDLE_TYPE_OPAQUE_WIN32_KMT_EXT',
                        'GL_HANDLE_TYPE_D3D12_TILEPOOL_EXT',
                        'GL_HANDLE_TYPE_D3D12_RESOURCE_EXT',
                        'GL_HANDLE_TYPE_D3D11_IMAGE_EXT',
                        'GL_HANDLE_TYPE_D3D11_IMAGE_KMT_EXT',
                        'GL_HANDLE_TYPE_D3D12_FENCE_EXT'],
 'FeedBackToken': ['GL_BITMAP_TOKEN',
                   'GL_COPY_PIXEL_TOKEN',
                   'GL_DRAW_PIXEL_TOKEN',
                   'GL_LINE_RESET_TOKEN',
                   'GL_LINE_TOKEN',
                   'GL_PASS_THROUGH_TOKEN',
                   'GL_POINT_TOKEN',
                   'GL_POLYGON_TOKEN'],
 'FeedbackType': ['GL_2D',
                  'GL_3D',
                  'GL_3D_COLOR',
                  'GL_3D_COLOR_TEXTURE',
                  'GL_4D_COLOR_TEXTURE'],
 'FenceConditionNV': [],
 'FenceParameterNameNV': [],
 'FfdMaskSGIX': [],
 'FfdTargetSGIX': [],
 'FogCoordinatePointerType': ['GL_FLOAT', 'GL_DOUBLE'],
 'FogMode': ['GL_EXP', 'GL_EXP2', 'GL_LINEAR'],
 'FogPName': ['GL_FOG_MODE',
              'GL_FOG_DENSITY',
              'GL_FOG_START',
              'GL_FOG_END',
              'GL_FOG_INDEX',
              'GL_FOG_COORD_SRC'],
 'FogParameter': ['GL_FOG_COLOR',
                  'GL_FOG_DENSITY',
                  'GL_FOG_END',
                  'GL_FOG_INDEX',
                  'GL_FOG_MODE',
                  'GL_FOG_START'],
 'FogPointerTypeEXT': ['GL_FLOAT', 'GL_DOUBLE'],
 'FogPointerTypeIBM': ['GL_FLOAT', 'GL_DOUBLE'],
 'FragmentLightModelParameterSGIX': [],
 'FragmentLightNameSGIX': [],
 'FragmentLightParameterSGIX': [],
 'FragmentOpATI': [],
 'FramebufferAttachment': ['GL_COLOR_ATTACHMENT0',
                           'GL_COLOR_ATTACHMENT0_EXT',
                           'GL_COLOR_ATTACHMENT1',
                           'GL_COLOR_ATTACHMENT1_EXT',
                           'GL_COLOR_ATTACHMENT2',
                           'GL_COLOR_ATTACHMENT2_EXT',
                           'GL_COLOR_ATTACHMENT3',
                           'GL_COLOR_ATTACHMENT3_EXT',
                           'GL_COLOR_ATTACHMENT4',
                           'GL_COLOR_ATTACHMENT4_EXT',
                           'GL_COLOR_ATTACHMENT5',
                           'GL_COLOR_ATTACHMENT5_EXT',
                           'GL_COLOR_ATTACHMENT6',
                           'GL_COLOR_ATTACHMENT6_EXT',
                           'GL_COLOR_ATTACHMENT7',
                           'GL_COLOR_ATTACHMENT7_EXT',
                           'GL_COLOR_ATTACHMENT8',
                           'GL_COLOR_ATTACHMENT8_EXT',
                           'GL_COLOR_ATTACHMENT9',
                           'GL_COLOR_ATTACHMENT9_EXT',
                           'GL_COLOR_ATTACHMENT10',
                           'GL_COLOR_ATTACHMENT10_EXT',
                           'GL_COLOR_ATTACHMENT11',
                           'GL_COLOR_ATTACHMENT11_EXT',
                           'GL_COLOR_ATTACHMENT12',
                           'GL_COLOR_ATTACHMENT12_EXT',
                           'GL_COLOR_ATTACHMENT13',
                           'GL_COLOR_ATTACHMENT13_EXT',
                           'GL_COLOR_ATTACHMENT14',
                           'GL_COLOR_ATTACHMENT14_EXT',
                           'GL_COLOR_ATTACHMENT15',
                           'GL_COLOR_ATTACHMENT15_EXT',
                           'GL_COLOR_ATTACHMENT16',
                           'GL_COLOR_ATTACHMENT17',
                           'GL_COLOR_ATTACHMENT18',
                           'GL_COLOR_ATTACHMENT19',
                           'GL_COLOR_ATTACHMENT20',
                           'GL_COLOR_ATTACHMENT21',
                           'GL_COLOR_ATTACHMENT22',
                           'GL_COLOR_ATTACHMENT23',
                           'GL_COLOR_ATTACHMENT24',
                           'GL_COLOR_ATTACHMENT25',
                           'GL_COLOR_ATTACHMENT26',
                           'GL_COLOR_ATTACHMENT27',
                           'GL_COLOR_ATTACHMENT28',
                           'GL_COLOR_ATTACHMENT29',
                           'GL_COLOR_ATTACHMENT30',
                           'GL_COLOR_ATTACHMENT31',
                           'GL_DEPTH_ATTACHMENT',
                           'GL_DEPTH_STENCIL_ATTACHMENT',
                           'GL_DEPTH_ATTACHMENT_EXT',
                           'GL_STENCIL_ATTACHMENT',
                           'GL_STENCIL_ATTACHMENT_EXT'],
 'FramebufferAttachmentParameterName': ['GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING',
                                        'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME',
                                        'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT',
                                        'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SCALE_IMG',
                                        'GL_FRAMEBUFFER_ATTACHMENT_LAYERED',
                                        'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB',
                                        'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT'],
 'FramebufferFetchNoncoherent': [],
 'FramebufferParameterName': ['GL_FRAMEBUFFER_DEFAULT_WIDTH',
                              'GL_FRAMEBUFFER_DEFAULT_HEIGHT',
                              'GL_FRAMEBUFFER_DEFAULT_LAYERS',
                              'GL_FRAMEBUFFER_DEFAULT_SAMPLES',
                              'GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS'],
 'FramebufferStatus': ['GL_FRAMEBUFFER_COMPLETE',
                       'GL_FRAMEBUFFER_UNDEFINED',
                       'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT',
                       'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT',
                       'GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER',
                       'GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER',
                       'GL_FRAMEBUFFER_UNSUPPORTED',
                       'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE',
                       'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE',
                       'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS'],
 'FramebufferTarget': ['GL_FRAMEBUFFER',
                       'GL_DRAW_FRAMEBUFFER',
                       'GL_READ_FRAMEBUFFER'],
 'FrontFaceDirection': ['GL_CCW', 'GL_CW'],
 'GetColorTableParameterPNameSGI': ['GL_COLOR_TABLE_BIAS',
                                    'GL_COLOR_TABLE_SCALE',
                                    'GL_COLOR_TABLE_FORMAT',
                                    'GL_COLOR_TABLE_WIDTH',
                                    'GL_COLOR_TABLE_RED_SIZE',
                                    'GL_COLOR_TABLE_GREEN_SIZE',
                                    'GL_COLOR_TABLE_BLUE_SIZE',
                                    'GL_COLOR_TABLE_ALPHA_SIZE',
                                    'GL_COLOR_TABLE_LUMINANCE_SIZE',
                                    'GL_COLOR_TABLE_INTENSITY_SIZE'],
 'GetConvolutionParameter': ['GL_CONVOLUTION_BORDER_MODE_EXT',
                             'GL_CONVOLUTION_FILTER_BIAS_EXT',
                             'GL_CONVOLUTION_FILTER_SCALE_EXT',
                             'GL_CONVOLUTION_FORMAT_EXT',
                             'GL_CONVOLUTION_HEIGHT_EXT',
                             'GL_CONVOLUTION_WIDTH_EXT',
                             'GL_MAX_CONVOLUTION_HEIGHT_EXT',
                             'GL_MAX_CONVOLUTION_WIDTH_EXT',
                             'GL_CONVOLUTION_BORDER_MODE',
                             'GL_CONVOLUTION_BORDER_COLOR',
                             'GL_CONVOLUTION_FILTER_SCALE',
                             'GL_CONVOLUTION_FILTER_BIAS',
                             'GL_CONVOLUTION_FORMAT',
                             'GL_CONVOLUTION_WIDTH',
                             'GL_CONVOLUTION_HEIGHT',
                             'GL_MAX_CONVOLUTION_WIDTH',
                             'GL_MAX_CONVOLUTION_HEIGHT'],
 'GetFramebufferParameter': ['GL_FRAMEBUFFER_DEFAULT_WIDTH',
                             'GL_FRAMEBUFFER_DEFAULT_HEIGHT',
                             'GL_FRAMEBUFFER_DEFAULT_LAYERS',
                             'GL_FRAMEBUFFER_DEFAULT_SAMPLES',
                             'GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS',
                             'GL_DOUBLEBUFFER',
                             'GL_IMPLEMENTATION_COLOR_READ_FORMAT',
                             'GL_IMPLEMENTATION_COLOR_READ_TYPE',
                             'GL_SAMPLES',
                             'GL_SAMPLE_BUFFERS',
                             'GL_STEREO'],
 'GetHistogramParameterPNameEXT': ['GL_HISTOGRAM_ALPHA_SIZE_EXT',
                                   'GL_HISTOGRAM_BLUE_SIZE_EXT',
                                   'GL_HISTOGRAM_FORMAT_EXT',
                                   'GL_HISTOGRAM_GREEN_SIZE_EXT',
                                   'GL_HISTOGRAM_LUMINANCE_SIZE_EXT',
                                   'GL_HISTOGRAM_RED_SIZE_EXT',
                                   'GL_HISTOGRAM_SINK_EXT',
                                   'GL_HISTOGRAM_WIDTH_EXT',
                                   'GL_HISTOGRAM_WIDTH',
                                   'GL_HISTOGRAM_FORMAT',
                                   'GL_HISTOGRAM_RED_SIZE',
                                   'GL_HISTOGRAM_GREEN_SIZE',
                                   'GL_HISTOGRAM_BLUE_SIZE',
                                   'GL_HISTOGRAM_ALPHA_SIZE',
                                   'GL_HISTOGRAM_LUMINANCE_SIZE',
                                   'GL_HISTOGRAM_SINK',
                                   'GL_HISTOGRAM_ALPHA_SIZE_EXT',
                                   'GL_HISTOGRAM_BLUE_SIZE_EXT',
                                   'GL_HISTOGRAM_FORMAT_EXT',
                                   'GL_HISTOGRAM_GREEN_SIZE_EXT',
                                   'GL_HISTOGRAM_LUMINANCE_SIZE_EXT',
                                   'GL_HISTOGRAM_RED_SIZE_EXT',
                                   'GL_HISTOGRAM_SINK_EXT',
                                   'GL_HISTOGRAM_WIDTH_EXT'],
 'GetMapQuery': ['GL_COEFF', 'GL_DOMAIN', 'GL_ORDER'],
 'GetMinmaxParameterPNameEXT': ['GL_MINMAX_FORMAT',
                                'GL_MINMAX_FORMAT_EXT',
                                'GL_MINMAX_SINK',
                                'GL_MINMAX_SINK_EXT',
                                'GL_MINMAX_FORMAT',
                                'GL_MINMAX_SINK'],
 'GetMultisamplePNameNV': ['GL_SAMPLE_POSITION',
                           'GL_SAMPLE_LOCATION_ARB',
                           'GL_PROGRAMMABLE_SAMPLE_LOCATION_ARB'],
 'GetPName': ['GL_ACCUM_ALPHA_BITS',
              'GL_ACCUM_BLUE_BITS',
              'GL_ACCUM_CLEAR_VALUE',
              'GL_ACCUM_GREEN_BITS',
              'GL_ACCUM_RED_BITS',
              'GL_ACTIVE_TEXTURE',
              'GL_ALIASED_LINE_WIDTH_RANGE',
              'GL_ALIASED_POINT_SIZE_RANGE',
              'GL_ALPHA_BIAS',
              'GL_ALPHA_BITS',
              'GL_ALPHA_SCALE',
              'GL_ALPHA_TEST',
              'GL_ALPHA_TEST_FUNC',
              'GL_ALPHA_TEST_REF',
              'GL_ARRAY_BUFFER_BINDING',
              'GL_ATTRIB_STACK_DEPTH',
              'GL_AUTO_NORMAL',
              'GL_AUX_BUFFERS',
              'GL_BLEND',
              'GL_BLEND_COLOR',
              'GL_BLEND_COLOR_EXT',
              'GL_BLEND_DST',
              'GL_BLEND_DST_ALPHA',
              'GL_BLEND_DST_RGB',
              'GL_BLEND_EQUATION_ALPHA',
              'GL_BLEND_EQUATION_EXT',
              'GL_BLEND_EQUATION_RGB',
              'GL_BLEND_SRC',
              'GL_BLEND_SRC_ALPHA',
              'GL_BLEND_SRC_RGB',
              'GL_BLUE_BIAS',
              'GL_BLUE_BITS',
              'GL_BLUE_SCALE',
              'GL_CLIENT_ATTRIB_STACK_DEPTH',
              'GL_CLIP_PLANE0',
              'GL_CLIP_PLANE1',
              'GL_CLIP_PLANE2',
              'GL_CLIP_PLANE3',
              'GL_CLIP_PLANE4',
              'GL_CLIP_PLANE5',
              'GL_COLOR_ARRAY',
              'GL_COLOR_ARRAY_COUNT_EXT',
              'GL_COLOR_ARRAY_SIZE',
              'GL_COLOR_ARRAY_STRIDE',
              'GL_COLOR_ARRAY_TYPE',
              'GL_COLOR_CLEAR_VALUE',
              'GL_COLOR_LOGIC_OP',
              'GL_COLOR_MATERIAL',
              'GL_COLOR_MATERIAL_FACE',
              'GL_COLOR_MATERIAL_PARAMETER',
              'GL_COLOR_WRITEMASK',
              'GL_COMPRESSED_TEXTURE_FORMATS',
              'GL_CONTEXT_FLAGS',
              'GL_CONVOLUTION_1D_EXT',
              'GL_CONVOLUTION_2D_EXT',
              'GL_CULL_FACE',
              'GL_CULL_FACE_MODE',
              'GL_CURRENT_COLOR',
              'GL_CURRENT_INDEX',
              'GL_CURRENT_NORMAL',
              'GL_CURRENT_PROGRAM',
              'GL_CURRENT_RASTER_COLOR',
              'GL_CURRENT_RASTER_DISTANCE',
              'GL_CURRENT_RASTER_INDEX',
              'GL_CURRENT_RASTER_POSITION',
              'GL_CURRENT_RASTER_POSITION_VALID',
              'GL_CURRENT_RASTER_TEXTURE_COORDS',
              'GL_CURRENT_TEXTURE_COORDS',
              'GL_DEBUG_GROUP_STACK_DEPTH',
              'GL_DEPTH_BIAS',
              'GL_DEPTH_BITS',
              'GL_DEPTH_CLEAR_VALUE',
              'GL_DEPTH_FUNC',
              'GL_DEPTH_RANGE',
              'GL_DEPTH_SCALE',
              'GL_DEPTH_TEST',
              'GL_DEPTH_WRITEMASK',
              'GL_DEVICE_LUID_EXT',
              'GL_DEVICE_NODE_MASK_EXT',
              'GL_DEVICE_UUID_EXT',
              'GL_DISPATCH_INDIRECT_BUFFER_BINDING',
              'GL_DITHER',
              'GL_DOUBLEBUFFER',
              'GL_DRAW_BUFFER',
              'GL_DRAW_BUFFER_EXT',
              'GL_DRAW_FRAMEBUFFER_BINDING',
              'GL_DRIVER_UUID_EXT',
              'GL_EDGE_FLAG',
              'GL_EDGE_FLAG_ARRAY',
              'GL_EDGE_FLAG_ARRAY_COUNT_EXT',
              'GL_EDGE_FLAG_ARRAY_STRIDE',
              'GL_ELEMENT_ARRAY_BUFFER_BINDING',
              'GL_FEEDBACK_BUFFER_SIZE',
              'GL_FEEDBACK_BUFFER_TYPE',
              'GL_FOG',
              'GL_FOG_COLOR',
              'GL_FOG_DENSITY',
              'GL_FOG_END',
              'GL_FOG_HINT',
              'GL_FOG_INDEX',
              'GL_FOG_MODE',
              'GL_FOG_START',
              'GL_FRAGMENT_SHADER_DERIVATIVE_HINT',
              'GL_FRONT_FACE',
              'GL_GREEN_BIAS',
              'GL_GREEN_BITS',
              'GL_GREEN_SCALE',
              'GL_HISTOGRAM_EXT',
              'GL_IMPLEMENTATION_COLOR_READ_FORMAT',
              'GL_IMPLEMENTATION_COLOR_READ_TYPE',
              'GL_INDEX_ARRAY',
              'GL_INDEX_ARRAY_COUNT_EXT',
              'GL_INDEX_ARRAY_STRIDE',
              'GL_INDEX_ARRAY_TYPE',
              'GL_INDEX_BITS',
              'GL_INDEX_CLEAR_VALUE',
              'GL_INDEX_LOGIC_OP',
              'GL_INDEX_MODE',
              'GL_INDEX_OFFSET',
              'GL_INDEX_SHIFT',
              'GL_INDEX_WRITEMASK',
              'GL_LAYER_PROVOKING_VERTEX',
              'GL_LIGHT0',
              'GL_LIGHT1',
              'GL_LIGHT2',
              'GL_LIGHT3',
              'GL_LIGHT4',
              'GL_LIGHT5',
              'GL_LIGHT6',
              'GL_LIGHT7',
              'GL_LIGHTING',
              'GL_LIGHT_MODEL_AMBIENT',
              'GL_LIGHT_MODEL_COLOR_CONTROL',
              'GL_LIGHT_MODEL_LOCAL_VIEWER',
              'GL_LIGHT_MODEL_TWO_SIDE',
              'GL_LINE_SMOOTH',
              'GL_LINE_SMOOTH_HINT',
              'GL_LINE_STIPPLE',
              'GL_LINE_STIPPLE_PATTERN',
              'GL_LINE_STIPPLE_REPEAT',
              'GL_LINE_WIDTH',
              'GL_LINE_WIDTH_GRANULARITY',
              'GL_LINE_WIDTH_RANGE',
              'GL_LIST_BASE',
              'GL_LIST_INDEX',
              'GL_LIST_MODE',
              'GL_LOGIC_OP',
              'GL_LOGIC_OP_MODE',
              'GL_MAJOR_VERSION',
              'GL_MAP1_COLOR_4',
              'GL_MAP1_GRID_DOMAIN',
              'GL_MAP1_GRID_SEGMENTS',
              'GL_MAP1_INDEX',
              'GL_MAP1_NORMAL',
              'GL_MAP1_TEXTURE_COORD_1',
              'GL_MAP1_TEXTURE_COORD_2',
              'GL_MAP1_TEXTURE_COORD_3',
              'GL_MAP1_TEXTURE_COORD_4',
              'GL_MAP1_VERTEX_3',
              'GL_MAP1_VERTEX_4',
              'GL_MAP2_COLOR_4',
              'GL_MAP2_GRID_DOMAIN',
              'GL_MAP2_GRID_SEGMENTS',
              'GL_MAP2_INDEX',
              'GL_MAP2_NORMAL',
              'GL_MAP2_TEXTURE_COORD_1',
              'GL_MAP2_TEXTURE_COORD_2',
              'GL_MAP2_TEXTURE_COORD_3',
              'GL_MAP2_TEXTURE_COORD_4',
              'GL_MAP2_VERTEX_3',
              'GL_MAP2_VERTEX_4',
              'GL_MAP_COLOR',
              'GL_MAP_STENCIL',
              'GL_MATRIX_MODE',
              'GL_MAX_3D_TEXTURE_SIZE',
              'GL_MAX_3D_TEXTURE_SIZE_EXT',
              'GL_MAX_ARRAY_TEXTURE_LAYERS',
              'GL_MAX_ATTRIB_STACK_DEPTH',
              'GL_MAX_CLIENT_ATTRIB_STACK_DEPTH',
              'GL_MAX_CLIP_DISTANCES',
              'GL_MAX_CLIP_PLANES',
              'GL_MAX_COLOR_TEXTURE_SAMPLES',
              'GL_MAX_COMBINED_ATOMIC_COUNTERS',
              'GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS',
              'GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS',
              'GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS',
              'GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS',
              'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS',
              'GL_MAX_COMBINED_UNIFORM_BLOCKS',
              'GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS',
              'GL_MAX_COMPUTE_ATOMIC_COUNTERS',
              'GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS',
              'GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS',
              'GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS',
              'GL_MAX_COMPUTE_UNIFORM_BLOCKS',
              'GL_MAX_COMPUTE_UNIFORM_COMPONENTS',
              'GL_MAX_COMPUTE_WORK_GROUP_COUNT',
              'GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS',
              'GL_MAX_COMPUTE_WORK_GROUP_SIZE',
              'GL_MAX_CUBE_MAP_TEXTURE_SIZE',
              'GL_MAX_DEBUG_GROUP_STACK_DEPTH',
              'GL_MAX_DEPTH_TEXTURE_SAMPLES',
              'GL_MAX_DRAW_BUFFERS',
              'GL_MAX_DUAL_SOURCE_DRAW_BUFFERS',
              'GL_MAX_ELEMENTS_INDICES',
              'GL_MAX_ELEMENTS_VERTICES',
              'GL_MAX_ELEMENT_INDEX',
              'GL_MAX_EVAL_ORDER',
              'GL_MAX_FRAGMENT_ATOMIC_COUNTERS',
              'GL_MAX_FRAGMENT_INPUT_COMPONENTS',
              'GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS',
              'GL_MAX_FRAGMENT_UNIFORM_BLOCKS',
              'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS',
              'GL_MAX_FRAGMENT_UNIFORM_VECTORS',
              'GL_MAX_FRAMEBUFFER_HEIGHT',
              'GL_MAX_FRAMEBUFFER_LAYERS',
              'GL_MAX_FRAMEBUFFER_SAMPLES',
              'GL_MAX_FRAMEBUFFER_WIDTH',
              'GL_MAX_GEOMETRY_ATOMIC_COUNTERS',
              'GL_MAX_GEOMETRY_INPUT_COMPONENTS',
              'GL_MAX_GEOMETRY_OUTPUT_COMPONENTS',
              'GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS',
              'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS',
              'GL_MAX_GEOMETRY_UNIFORM_BLOCKS',
              'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS',
              'GL_MAX_INTEGER_SAMPLES',
              'GL_MAX_LABEL_LENGTH',
              'GL_MAX_LIGHTS',
              'GL_MAX_LIST_NESTING',
              'GL_MAX_MODELVIEW_STACK_DEPTH',
              'GL_MAX_NAME_STACK_DEPTH',
              'GL_MAX_PIXEL_MAP_TABLE',
              'GL_MAX_PROGRAM_TEXEL_OFFSET',
              'GL_MAX_PROJECTION_STACK_DEPTH',
              'GL_MAX_RECTANGLE_TEXTURE_SIZE',
              'GL_MAX_RENDERBUFFER_SIZE',
              'GL_MAX_SAMPLE_MASK_WORDS',
              'GL_MAX_SERVER_WAIT_TIMEOUT',
              'GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS',
              'GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS',
              'GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS',
              'GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS',
              'GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS',
              'GL_MAX_TEXTURE_BUFFER_SIZE',
              'GL_MAX_TEXTURE_IMAGE_UNITS',
              'GL_MAX_TEXTURE_LOD_BIAS',
              'GL_MAX_TEXTURE_SIZE',
              'GL_MAX_TEXTURE_STACK_DEPTH',
              'GL_MAX_UNIFORM_BLOCK_SIZE',
              'GL_MAX_UNIFORM_BUFFER_BINDINGS',
              'GL_MAX_UNIFORM_LOCATIONS',
              'GL_MAX_VARYING_COMPONENTS',
              'GL_MAX_VARYING_FLOATS',
              'GL_MAX_VARYING_VECTORS',
              'GL_MAX_VERTEX_ATOMIC_COUNTERS',
              'GL_MAX_VERTEX_ATTRIBS',
              'GL_MAX_VERTEX_ATTRIB_BINDINGS',
              'GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET',
              'GL_MAX_VERTEX_OUTPUT_COMPONENTS',
              'GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS',
              'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS',
              'GL_MAX_VERTEX_UNIFORM_BLOCKS',
              'GL_MAX_VERTEX_UNIFORM_COMPONENTS',
              'GL_MAX_VERTEX_UNIFORM_VECTORS',
              'GL_MAX_VIEWPORTS',
              'GL_MAX_VIEWPORT_DIMS',
              'GL_MINMAX_EXT',
              'GL_MINOR_VERSION',
              'GL_MIN_MAP_BUFFER_ALIGNMENT',
              'GL_MIN_PROGRAM_TEXEL_OFFSET',
              'GL_MODELVIEW0_MATRIX_EXT',
              'GL_MODELVIEW0_STACK_DEPTH_EXT',
              'GL_MODELVIEW_MATRIX',
              'GL_MODELVIEW_STACK_DEPTH',
              'GL_NAME_STACK_DEPTH',
              'GL_NORMALIZE',
              'GL_NORMAL_ARRAY',
              'GL_NORMAL_ARRAY_COUNT_EXT',
              'GL_NORMAL_ARRAY_STRIDE',
              'GL_NORMAL_ARRAY_TYPE',
              'GL_NUM_COMPRESSED_TEXTURE_FORMATS',
              'GL_NUM_DEVICE_UUIDS_EXT',
              'GL_NUM_EXTENSIONS',
              'GL_NUM_PROGRAM_BINARY_FORMATS',
              'GL_NUM_SHADER_BINARY_FORMATS',
              'GL_PACK_ALIGNMENT',
              'GL_PACK_CMYK_HINT_EXT',
              'GL_PACK_IMAGE_HEIGHT',
              'GL_PACK_IMAGE_HEIGHT_EXT',
              'GL_PACK_LSB_FIRST',
              'GL_PACK_ROW_LENGTH',
              'GL_PACK_SKIP_IMAGES',
              'GL_PACK_SKIP_IMAGES_EXT',
              'GL_PACK_SKIP_PIXELS',
              'GL_PACK_SKIP_ROWS',
              'GL_PACK_SWAP_BYTES',
              'GL_PERSPECTIVE_CORRECTION_HINT',
              'GL_PIXEL_MAP_A_TO_A_SIZE',
              'GL_PIXEL_MAP_B_TO_B_SIZE',
              'GL_PIXEL_MAP_G_TO_G_SIZE',
              'GL_PIXEL_MAP_I_TO_A_SIZE',
              'GL_PIXEL_MAP_I_TO_B_SIZE',
              'GL_PIXEL_MAP_I_TO_G_SIZE',
              'GL_PIXEL_MAP_I_TO_I_SIZE',
              'GL_PIXEL_MAP_I_TO_R_SIZE',
              'GL_PIXEL_MAP_R_TO_R_SIZE',
              'GL_PIXEL_MAP_S_TO_S_SIZE',
              'GL_PIXEL_PACK_BUFFER_BINDING',
              'GL_PIXEL_UNPACK_BUFFER_BINDING',
              'GL_POINT_FADE_THRESHOLD_SIZE',
              'GL_POINT_SIZE',
              'GL_POINT_SIZE_GRANULARITY',
              'GL_POINT_SIZE_RANGE',
              'GL_POINT_SMOOTH',
              'GL_POINT_SMOOTH_HINT',
              'GL_POLYGON_MODE',
              'GL_POLYGON_OFFSET_BIAS_EXT',
              'GL_POLYGON_OFFSET_FACTOR',
              'GL_POLYGON_OFFSET_FILL',
              'GL_POLYGON_OFFSET_LINE',
              'GL_POLYGON_OFFSET_POINT',
              'GL_POLYGON_OFFSET_UNITS',
              'GL_POLYGON_SMOOTH',
              'GL_POLYGON_SMOOTH_HINT',
              'GL_POLYGON_STIPPLE',
              'GL_POST_CONVOLUTION_ALPHA_BIAS_EXT',
              'GL_POST_CONVOLUTION_ALPHA_SCALE_EXT',
              'GL_POST_CONVOLUTION_BLUE_BIAS_EXT',
              'GL_POST_CONVOLUTION_BLUE_SCALE_EXT',
              'GL_POST_CONVOLUTION_GREEN_BIAS_EXT',
              'GL_POST_CONVOLUTION_GREEN_SCALE_EXT',
              'GL_POST_CONVOLUTION_RED_BIAS_EXT',
              'GL_POST_CONVOLUTION_RED_SCALE_EXT',
              'GL_PRIMITIVE_RESTART_INDEX',
              'GL_PROGRAM_BINARY_FORMATS',
              'GL_PROGRAM_PIPELINE_BINDING',
              'GL_PROGRAM_POINT_SIZE',
              'GL_PROJECTION_MATRIX',
              'GL_PROJECTION_STACK_DEPTH',
              'GL_PROVOKING_VERTEX',
              'GL_READ_BUFFER',
              'GL_READ_BUFFER_EXT',
              'GL_READ_FRAMEBUFFER_BINDING',
              'GL_RED_BIAS',
              'GL_RED_BITS',
              'GL_RED_SCALE',
              'GL_RENDERBUFFER_BINDING',
              'GL_RENDER_MODE',
              'GL_RESCALE_NORMAL_EXT',
              'GL_RGBA_MODE',
              'GL_SAMPLER_BINDING',
              'GL_SAMPLES',
              'GL_SAMPLE_BUFFERS',
              'GL_SAMPLE_COVERAGE_INVERT',
              'GL_SAMPLE_COVERAGE_VALUE',
              'GL_SCISSOR_BOX',
              'GL_SCISSOR_TEST',
              'GL_SELECTION_BUFFER_SIZE',
              'GL_SEPARABLE_2D_EXT',
              'GL_SHADER_COMPILER',
              'GL_SHADER_STORAGE_BUFFER_BINDING',
              'GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT',
              'GL_SHADER_STORAGE_BUFFER_SIZE',
              'GL_SHADER_STORAGE_BUFFER_START',
              'GL_SHADE_MODEL',
              'GL_SHARED_TEXTURE_PALETTE_EXT',
              'GL_SMOOTH_LINE_WIDTH_GRANULARITY',
              'GL_SMOOTH_LINE_WIDTH_RANGE',
              'GL_SMOOTH_POINT_SIZE_GRANULARITY',
              'GL_SMOOTH_POINT_SIZE_RANGE',
              'GL_STENCIL_BACK_FAIL',
              'GL_STENCIL_BACK_FUNC',
              'GL_STENCIL_BACK_PASS_DEPTH_FAIL',
              'GL_STENCIL_BACK_PASS_DEPTH_PASS',
              'GL_STENCIL_BACK_REF',
              'GL_STENCIL_BACK_VALUE_MASK',
              'GL_STENCIL_BACK_WRITEMASK',
              'GL_STENCIL_BITS',
              'GL_STENCIL_CLEAR_VALUE',
              'GL_STENCIL_FAIL',
              'GL_STENCIL_FUNC',
              'GL_STENCIL_PASS_DEPTH_FAIL',
              'GL_STENCIL_PASS_DEPTH_PASS',
              'GL_STENCIL_REF',
              'GL_STENCIL_TEST',
              'GL_STENCIL_VALUE_MASK',
              'GL_STENCIL_WRITEMASK',
              'GL_STEREO',
              'GL_SUBPIXEL_BITS',
              'GL_TEXTURE_1D',
              'GL_TEXTURE_2D',
              'GL_TEXTURE_3D_BINDING_EXT',
              'GL_TEXTURE_3D_EXT',
              'GL_TEXTURE_BINDING_1D',
              'GL_TEXTURE_BINDING_1D_ARRAY',
              'GL_TEXTURE_BINDING_2D',
              'GL_TEXTURE_BINDING_2D_ARRAY',
              'GL_TEXTURE_BINDING_2D_MULTISAMPLE',
              'GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY',
              'GL_TEXTURE_BINDING_3D',
              'GL_TEXTURE_BINDING_BUFFER',
              'GL_TEXTURE_BINDING_CUBE_MAP',
              'GL_TEXTURE_BINDING_RECTANGLE',
              'GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT',
              'GL_TEXTURE_COMPRESSION_HINT',
              'GL_TEXTURE_COORD_ARRAY',
              'GL_TEXTURE_COORD_ARRAY_COUNT_EXT',
              'GL_TEXTURE_COORD_ARRAY_SIZE',
              'GL_TEXTURE_COORD_ARRAY_STRIDE',
              'GL_TEXTURE_COORD_ARRAY_TYPE',
              'GL_TEXTURE_GEN_Q',
              'GL_TEXTURE_GEN_R',
              'GL_TEXTURE_GEN_S',
              'GL_TEXTURE_GEN_T',
              'GL_TEXTURE_MATRIX',
              'GL_TEXTURE_STACK_DEPTH',
              'GL_TIMESTAMP',
              'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING',
              'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE',
              'GL_TRANSFORM_FEEDBACK_BUFFER_START',
              'GL_UNIFORM_BUFFER_BINDING',
              'GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT',
              'GL_UNIFORM_BUFFER_SIZE',
              'GL_UNIFORM_BUFFER_START',
              'GL_UNPACK_ALIGNMENT',
              'GL_UNPACK_CMYK_HINT_EXT',
              'GL_UNPACK_IMAGE_HEIGHT',
              'GL_UNPACK_IMAGE_HEIGHT_EXT',
              'GL_UNPACK_LSB_FIRST',
              'GL_UNPACK_ROW_LENGTH',
              'GL_UNPACK_SKIP_IMAGES',
              'GL_UNPACK_SKIP_IMAGES_EXT',
              'GL_UNPACK_SKIP_PIXELS',
              'GL_UNPACK_SKIP_ROWS',
              'GL_UNPACK_SWAP_BYTES',
              'GL_VERTEX_ARRAY',
              'GL_VERTEX_ARRAY_BINDING',
              'GL_VERTEX_ARRAY_COUNT_EXT',
              'GL_VERTEX_ARRAY_SIZE',
              'GL_VERTEX_ARRAY_STRIDE',
              'GL_VERTEX_ARRAY_TYPE',
              'GL_VERTEX_BINDING_DIVISOR',
              'GL_VERTEX_BINDING_OFFSET',
              'GL_VERTEX_BINDING_STRIDE',
              'GL_VIEWPORT',
              'GL_VIEWPORT_BOUNDS_RANGE',
              'GL_VIEWPORT_INDEX_PROVOKING_VERTEX',
              'GL_VIEWPORT_SUBPIXEL_BITS',
              'GL_ZOOM_X',
              'GL_ZOOM_Y'],
 'GetPixelMap': ['GL_PIXEL_MAP_A_TO_A',
                 'GL_PIXEL_MAP_B_TO_B',
                 'GL_PIXEL_MAP_G_TO_G',
                 'GL_PIXEL_MAP_I_TO_A',
                 'GL_PIXEL_MAP_I_TO_B',
                 'GL_PIXEL_MAP_I_TO_G',
                 'GL_PIXEL_MAP_I_TO_I',
                 'GL_PIXEL_MAP_I_TO_R',
                 'GL_PIXEL_MAP_R_TO_R',
                 'GL_PIXEL_MAP_S_TO_S'],
 'GetPointervPName': ['GL_COLOR_ARRAY_POINTER',
                      'GL_COLOR_ARRAY_POINTER_EXT',
                      'GL_EDGE_FLAG_ARRAY_POINTER',
                      'GL_EDGE_FLAG_ARRAY_POINTER_EXT',
                      'GL_FEEDBACK_BUFFER_POINTER',
                      'GL_INDEX_ARRAY_POINTER',
                      'GL_INDEX_ARRAY_POINTER_EXT',
                      'GL_NORMAL_ARRAY_POINTER',
                      'GL_NORMAL_ARRAY_POINTER_EXT',
                      'GL_SELECTION_BUFFER_POINTER',
                      'GL_TEXTURE_COORD_ARRAY_POINTER',
                      'GL_TEXTURE_COORD_ARRAY_POINTER_EXT',
                      'GL_VERTEX_ARRAY_POINTER',
                      'GL_VERTEX_ARRAY_POINTER_EXT',
                      'GL_DEBUG_CALLBACK_FUNCTION',
                      'GL_DEBUG_CALLBACK_USER_PARAM'],
 'GetTexBumpParameterATI': [],
 'GetTextureParameter': ['GL_TEXTURE_ALPHA_SIZE',
                         'GL_TEXTURE_BLUE_SIZE',
                         'GL_TEXTURE_BORDER',
                         'GL_TEXTURE_BORDER_COLOR',
                         'GL_TEXTURE_COMPONENTS',
                         'GL_TEXTURE_DEPTH_EXT',
                         'GL_TEXTURE_GREEN_SIZE',
                         'GL_TEXTURE_HEIGHT',
                         'GL_TEXTURE_INTENSITY_SIZE',
                         'GL_TEXTURE_INTERNAL_FORMAT',
                         'GL_TEXTURE_LUMINANCE_SIZE',
                         'GL_TEXTURE_MAG_FILTER',
                         'GL_TEXTURE_MIN_FILTER',
                         'GL_TEXTURE_PRIORITY',
                         'GL_TEXTURE_RED_SIZE',
                         'GL_TEXTURE_RESIDENT',
                         'GL_TEXTURE_WIDTH',
                         'GL_TEXTURE_WRAP_R_EXT',
                         'GL_TEXTURE_WRAP_S',
                         'GL_TEXTURE_WRAP_T'],
 'GetVariantValueEXT': ['GL_VARIANT_VALUE_EXT',
                        'GL_VARIANT_DATATYPE_EXT',
                        'GL_VARIANT_ARRAY_STRIDE_EXT',
                        'GL_VARIANT_ARRAY_TYPE_EXT'],
 'GlslTypeToken': ['GL_FLOAT',
                   'GL_FLOAT_VEC2',
                   'GL_FLOAT_VEC3',
                   'GL_FLOAT_VEC4',
                   'GL_DOUBLE',
                   'GL_DOUBLE_VEC2',
                   'GL_DOUBLE_VEC3',
                   'GL_DOUBLE_VEC4',
                   'GL_INT',
                   'GL_INT_VEC2',
                   'GL_INT_VEC3',
                   'GL_INT_VEC4',
                   'GL_UNSIGNED_INT',
                   'GL_UNSIGNED_INT_VEC2',
                   'GL_UNSIGNED_INT_VEC3',
                   'GL_UNSIGNED_INT_VEC4',
                   'GL_BOOL',
                   'GL_BOOL_VEC2',
                   'GL_BOOL_VEC3',
                   'GL_BOOL_VEC4',
                   'GL_FLOAT_MAT2',
                   'GL_FLOAT_MAT3',
                   'GL_FLOAT_MAT4',
                   'GL_FLOAT_MAT2x3',
                   'GL_FLOAT_MAT2x4',
                   'GL_FLOAT_MAT3x2',
                   'GL_FLOAT_MAT3x4',
                   'GL_FLOAT_MAT4x2',
                   'GL_FLOAT_MAT4x3',
                   'GL_DOUBLE_MAT2',
                   'GL_DOUBLE_MAT3',
                   'GL_DOUBLE_MAT4',
                   'GL_SAMPLER_1D',
                   'GL_SAMPLER_2D',
                   'GL_SAMPLER_3D',
                   'GL_SAMPLER_CUBE',
                   'GL_SAMPLER_1D_SHADOW',
                   'GL_SAMPLER_2D_SHADOW',
                   'GL_SAMPLER_1D_ARRAY',
                   'GL_SAMPLER_2D_ARRAY',
                   'GL_SAMPLER_CUBE_MAP_ARRAY',
                   'GL_SAMPLER_1D_ARRAY_SHADOW',
                   'GL_SAMPLER_2D_ARRAY_SHADOW',
                   'GL_SAMPLER_2D_MULTISAMPLE',
                   'GL_SAMPLER_2D_MULTISAMPLE_ARRAY',
                   'GL_SAMPLER_CUBE_SHADOW',
                   'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW',
                   'GL_SAMPLER_BUFFER',
                   'GL_SAMPLER_2D_RECT',
                   'GL_SAMPLER_2D_RECT_SHADOW',
                   'GL_INT_SAMPLER_1D',
                   'GL_INT_SAMPLER_2D',
                   'GL_INT_SAMPLER_3D',
                   'GL_INT_SAMPLER_CUBE',
                   'GL_INT_SAMPLER_1D_ARRAY',
                   'GL_INT_SAMPLER_2D_ARRAY',
                   'GL_INT_SAMPLER_CUBE_MAP_ARRAY',
                   'GL_INT_SAMPLER_2D_MULTISAMPLE',
                   'GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY',
                   'GL_INT_SAMPLER_BUFFER',
                   'GL_INT_SAMPLER_2D_RECT',
                   'GL_UNSIGNED_INT_SAMPLER_1D',
                   'GL_UNSIGNED_INT_SAMPLER_2D',
                   'GL_UNSIGNED_INT_SAMPLER_3D',
                   'GL_UNSIGNED_INT_SAMPLER_CUBE',
                   'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY',
                   'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY',
                   'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY',
                   'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE',
                   'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY',
                   'GL_UNSIGNED_INT_SAMPLER_BUFFER',
                   'GL_UNSIGNED_INT_SAMPLER_2D_RECT',
                   'GL_IMAGE_1D',
                   'GL_IMAGE_2D',
                   'GL_IMAGE_3D',
                   'GL_IMAGE_2D_RECT',
                   'GL_IMAGE_CUBE',
                   'GL_IMAGE_BUFFER',
                   'GL_IMAGE_1D_ARRAY',
                   'GL_IMAGE_2D_ARRAY',
                   'GL_IMAGE_CUBE_MAP_ARRAY',
                   'GL_IMAGE_2D_MULTISAMPLE',
                   'GL_IMAGE_2D_MULTISAMPLE_ARRAY',
                   'GL_INT_IMAGE_1D',
                   'GL_INT_IMAGE_2D',
                   'GL_INT_IMAGE_3D',
                   'GL_INT_IMAGE_2D_RECT',
                   'GL_INT_IMAGE_CUBE',
                   'GL_INT_IMAGE_BUFFER',
                   'GL_INT_IMAGE_1D_ARRAY',
                   'GL_INT_IMAGE_2D_ARRAY',
                   'GL_INT_IMAGE_CUBE_MAP_ARRAY',
                   'GL_INT_IMAGE_2D_MULTISAMPLE',
                   'GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY',
                   'GL_UNSIGNED_INT_IMAGE_1D',
                   'GL_UNSIGNED_INT_IMAGE_2D',
                   'GL_UNSIGNED_INT_IMAGE_3D',
                   'GL_UNSIGNED_INT_IMAGE_2D_RECT',
                   'GL_UNSIGNED_INT_IMAGE_CUBE',
                   'GL_UNSIGNED_INT_IMAGE_BUFFER',
                   'GL_UNSIGNED_INT_IMAGE_1D_ARRAY',
                   'GL_UNSIGNED_INT_IMAGE_2D_ARRAY',
                   'GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY',
                   'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE',
                   'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY',
                   'GL_UNSIGNED_INT_ATOMIC_COUNTER'],
 'GraphicsResetStatus': ['GL_NO_ERROR',
                         'GL_GUILTY_CONTEXT_RESET',
                         'GL_INNOCENT_CONTEXT_RESET',
                         'GL_UNKNOWN_CONTEXT_RESET'],
 'HintMode': ['GL_DONT_CARE', 'GL_FASTEST', 'GL_NICEST'],
 'HintTarget': ['GL_CLIP_VOLUME_CLIPPING_HINT_EXT',
                'GL_FOG_HINT',
                'GL_FRAGMENT_SHADER_DERIVATIVE_HINT',
                'GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB',
                'GL_GENERATE_MIPMAP_HINT',
                'GL_LINE_SMOOTH_HINT',
                'GL_PACK_CMYK_HINT_EXT',
                'GL_PERSPECTIVE_CORRECTION_HINT',
                'GL_PHONG_HINT_WIN',
                'GL_POINT_SMOOTH_HINT',
                'GL_POLYGON_SMOOTH_HINT',
                'GL_PROGRAM_BINARY_RETRIEVABLE_HINT',
                'GL_TEXTURE_COMPRESSION_HINT',
                'GL_TEXTURE_COMPRESSION_HINT_ARB',
                'GL_UNPACK_CMYK_HINT_EXT'],
 'HintTargetPGI': [],
 'HistogramTargetEXT': ['GL_HISTOGRAM',
                        'GL_HISTOGRAM_EXT',
                        'GL_PROXY_HISTOGRAM',
                        'GL_PROXY_HISTOGRAM_EXT'],
 'IglooFunctionSelectSGIX': [],
 'ImageTransformPNameHP': ['GL_IMAGE_SCALE_X_HP',
                           'GL_IMAGE_SCALE_Y_HP',
                           'GL_IMAGE_TRANSLATE_X_HP',
                           'GL_IMAGE_TRANSLATE_Y_HP',
                           'GL_IMAGE_ROTATE_ANGLE_HP',
                           'GL_IMAGE_ROTATE_ORIGIN_X_HP',
                           'GL_IMAGE_ROTATE_ORIGIN_Y_HP',
                           'GL_IMAGE_MAG_FILTER_HP',
                           'GL_IMAGE_MIN_FILTER_HP',
                           'GL_IMAGE_CUBIC_WEIGHT_HP'],
 'ImageTransformTargetHP': ['GL_IMAGE_TRANSFORM_2D_HP'],
 'IndexFunctionEXT': ['GL_NEVER_EXT',
                      'GL_ALWAYS_EXT',
                      'GL_LESS_EXT',
                      'GL_LEQUAL_EXT',
                      'GL_EQUAL_EXT',
                      'GL_GEQUAL_EXT',
                      'GL_GREATER_EXT',
                      'GL_NOTEQUAL_EXT'],
 'IndexMaterialParameterEXT': ['GL_INDEX_OFFSET'],
 'IndexPointerType': ['GL_DOUBLE', 'GL_FLOAT', 'GL_INT', 'GL_SHORT'],
 'InterleavedArrayFormat': ['GL_C3F_V3F',
                            'GL_C4F_N3F_V3F',
                            'GL_C4UB_V2F',
                            'GL_C4UB_V3F',
                            'GL_N3F_V3F',
                            'GL_T2F_C3F_V3F',
                            'GL_T2F_C4F_N3F_V3F',
                            'GL_T2F_C4UB_V3F',
                            'GL_T2F_N3F_V3F',
                            'GL_T2F_V3F',
                            'GL_T4F_C4F_N3F_V4F',
                            'GL_T4F_V4F',
                            'GL_V2F',
                            'GL_V3F'],
 'InternalFormat': ['GL_ALPHA12',
                    'GL_ALPHA16',
                    'GL_ALPHA4',
                    'GL_ALPHA8',
                    'GL_INTENSITY',
                    'GL_INTENSITY12',
                    'GL_INTENSITY16',
                    'GL_INTENSITY4',
                    'GL_INTENSITY8',
                    'GL_LUMINANCE12',
                    'GL_LUMINANCE12_ALPHA12',
                    'GL_LUMINANCE12_ALPHA4',
                    'GL_LUMINANCE16',
                    'GL_LUMINANCE16_ALPHA16',
                    'GL_LUMINANCE4',
                    'GL_LUMINANCE4_ALPHA4',
                    'GL_LUMINANCE6_ALPHA2',
                    'GL_LUMINANCE8',
                    'GL_LUMINANCE8_ALPHA8',
                    'GL_RED',
                    'GL_RED_EXT',
                    'GL_R8',
                    'GL_R8_EXT',
                    'GL_R8_SNORM',
                    'GL_R16',
                    'GL_R16_EXT',
                    'GL_R16_SNORM',
                    'GL_R16_SNORM_EXT',
                    'GL_R16F',
                    'GL_R16F_EXT',
                    'GL_R32F',
                    'GL_R32F_EXT',
                    'GL_R8I',
                    'GL_R16I',
                    'GL_R32I',
                    'GL_R8UI',
                    'GL_R16UI',
                    'GL_R32UI',
                    'GL_RG',
                    'GL_RG8',
                    'GL_RG8_EXT',
                    'GL_RG8_SNORM',
                    'GL_RG16',
                    'GL_RG16_EXT',
                    'GL_RG16_SNORM',
                    'GL_RG16_SNORM_EXT',
                    'GL_RG16F',
                    'GL_RG16F_EXT',
                    'GL_RG32F',
                    'GL_RG32F_EXT',
                    'GL_RG8I',
                    'GL_RG16I',
                    'GL_RG32I',
                    'GL_RG8UI',
                    'GL_RG16UI',
                    'GL_RG32UI',
                    'GL_RGB',
                    'GL_RGB2_EXT',
                    'GL_RGB4',
                    'GL_RGB4_EXT',
                    'GL_RGB5',
                    'GL_RGB5_EXT',
                    'GL_RGB8',
                    'GL_RGB8_EXT',
                    'GL_RGB8_SNORM',
                    'GL_RGB10',
                    'GL_RGB10_EXT',
                    'GL_RGB12',
                    'GL_RGB12_EXT',
                    'GL_RGB16',
                    'GL_RGB16_EXT',
                    'GL_RGB16F',
                    'GL_RGB16F_ARB',
                    'GL_RGB16F_EXT',
                    'GL_RGB16_SNORM',
                    'GL_RGB16_SNORM_EXT',
                    'GL_RGB32F',
                    'GL_RGB8I',
                    'GL_RGB16I',
                    'GL_RGB32I',
                    'GL_RGB8UI',
                    'GL_RGB16UI',
                    'GL_RGB32UI',
                    'GL_SRGB',
                    'GL_SRGB_EXT',
                    'GL_SRGB_ALPHA',
                    'GL_SRGB_ALPHA_EXT',
                    'GL_SRGB8',
                    'GL_SRGB8_EXT',
                    'GL_SRGB8_ALPHA8',
                    'GL_SRGB8_ALPHA8_EXT',
                    'GL_R3_G3_B2',
                    'GL_R11F_G11F_B10F',
                    'GL_R11F_G11F_B10F_EXT',
                    'GL_RGB9_E5',
                    'GL_RGB9_E5_EXT',
                    'GL_RGBA',
                    'GL_RGBA4',
                    'GL_RGBA4_EXT',
                    'GL_RGB5_A1',
                    'GL_RGB5_A1_EXT',
                    'GL_RGBA8',
                    'GL_RGBA8_EXT',
                    'GL_RGBA8_SNORM',
                    'GL_RGB10_A2',
                    'GL_RGB10_A2_EXT',
                    'GL_RGBA12',
                    'GL_RGBA12_EXT',
                    'GL_RGBA16',
                    'GL_RGBA16_EXT',
                    'GL_RGBA16F',
                    'GL_RGBA16F_ARB',
                    'GL_RGBA16F_EXT',
                    'GL_RGBA32F',
                    'GL_RGBA32F_ARB',
                    'GL_RGBA32F_EXT',
                    'GL_RGBA8I',
                    'GL_RGBA16I',
                    'GL_RGBA32I',
                    'GL_RGBA8UI',
                    'GL_RGBA16UI',
                    'GL_RGBA32UI',
                    'GL_RGB10_A2UI',
                    'GL_DEPTH_COMPONENT',
                    'GL_DEPTH_COMPONENT16',
                    'GL_DEPTH_COMPONENT16_ARB',
                    'GL_DEPTH_COMPONENT24_ARB',
                    'GL_DEPTH_COMPONENT32_ARB',
                    'GL_DEPTH_COMPONENT32F',
                    'GL_DEPTH_STENCIL',
                    'GL_DEPTH_STENCIL_EXT',
                    'GL_DEPTH24_STENCIL8',
                    'GL_DEPTH24_STENCIL8_EXT',
                    'GL_DEPTH32F_STENCIL8',
                    'GL_STENCIL_INDEX',
                    'GL_STENCIL_INDEX1',
                    'GL_STENCIL_INDEX1_EXT',
                    'GL_STENCIL_INDEX4',
                    'GL_STENCIL_INDEX4_EXT',
                    'GL_STENCIL_INDEX8',
                    'GL_STENCIL_INDEX8_EXT',
                    'GL_STENCIL_INDEX16',
                    'GL_STENCIL_INDEX16_EXT',
                    'GL_COMPRESSED_RED',
                    'GL_COMPRESSED_RG',
                    'GL_COMPRESSED_RGB',
                    'GL_COMPRESSED_RGBA',
                    'GL_COMPRESSED_SRGB',
                    'GL_COMPRESSED_SRGB_ALPHA',
                    'GL_COMPRESSED_RED_RGTC1',
                    'GL_COMPRESSED_RED_RGTC1_EXT',
                    'GL_COMPRESSED_SIGNED_RED_RGTC1',
                    'GL_COMPRESSED_SIGNED_RED_RGTC1_EXT',
                    'GL_COMPRESSED_R11_EAC',
                    'GL_COMPRESSED_SIGNED_R11_EAC',
                    'GL_COMPRESSED_RG_RGTC2',
                    'GL_COMPRESSED_SIGNED_RG_RGTC2',
                    'GL_COMPRESSED_RGBA_BPTC_UNORM',
                    'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM',
                    'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT',
                    'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT',
                    'GL_COMPRESSED_RGB8_ETC2',
                    'GL_COMPRESSED_SRGB8_ETC2',
                    'GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2',
                    'GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2',
                    'GL_COMPRESSED_RGBA8_ETC2_EAC',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC',
                    'GL_COMPRESSED_RG11_EAC',
                    'GL_COMPRESSED_SIGNED_RG11_EAC',
                    'GL_COMPRESSED_RGB_S3TC_DXT1_EXT',
                    'GL_COMPRESSED_SRGB_S3TC_DXT1_EXT',
                    'GL_COMPRESSED_RGBA_S3TC_DXT1_EXT',
                    'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT',
                    'GL_COMPRESSED_RGBA_S3TC_DXT3_EXT',
                    'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT',
                    'GL_COMPRESSED_RGBA_S3TC_DXT5_EXT',
                    'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT',
                    'GL_COMPRESSED_RGBA_ASTC_4x4',
                    'GL_COMPRESSED_RGBA_ASTC_5x4',
                    'GL_COMPRESSED_RGBA_ASTC_5x5',
                    'GL_COMPRESSED_RGBA_ASTC_6x5',
                    'GL_COMPRESSED_RGBA_ASTC_6x6',
                    'GL_COMPRESSED_RGBA_ASTC_8x5',
                    'GL_COMPRESSED_RGBA_ASTC_8x6',
                    'GL_COMPRESSED_RGBA_ASTC_8x8',
                    'GL_COMPRESSED_RGBA_ASTC_10x10',
                    'GL_COMPRESSED_RGBA_ASTC_10x5',
                    'GL_COMPRESSED_RGBA_ASTC_10x6',
                    'GL_COMPRESSED_RGBA_ASTC_10x8',
                    'GL_COMPRESSED_RGBA_ASTC_12x10',
                    'GL_COMPRESSED_RGBA_ASTC_12x12',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10',
                    'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12'],
 'InternalFormatPName': ['GL_NUM_SAMPLE_COUNTS',
                         'GL_SAMPLES',
                         'GL_INTERNALFORMAT_SUPPORTED',
                         'GL_INTERNALFORMAT_PREFERRED',
                         'GL_INTERNALFORMAT_RED_SIZE',
                         'GL_INTERNALFORMAT_GREEN_SIZE',
                         'GL_INTERNALFORMAT_BLUE_SIZE',
                         'GL_INTERNALFORMAT_ALPHA_SIZE',
                         'GL_INTERNALFORMAT_DEPTH_SIZE',
                         'GL_INTERNALFORMAT_STENCIL_SIZE',
                         'GL_INTERNALFORMAT_SHARED_SIZE',
                         'GL_INTERNALFORMAT_RED_TYPE',
                         'GL_INTERNALFORMAT_GREEN_TYPE',
                         'GL_INTERNALFORMAT_BLUE_TYPE',
                         'GL_INTERNALFORMAT_ALPHA_TYPE',
                         'GL_INTERNALFORMAT_DEPTH_TYPE',
                         'GL_INTERNALFORMAT_STENCIL_TYPE',
                         'GL_MAX_WIDTH',
                         'GL_MAX_HEIGHT',
                         'GL_MAX_DEPTH',
                         'GL_MAX_LAYERS',
                         'GL_COLOR_COMPONENTS',
                         'GL_COLOR_RENDERABLE',
                         'GL_DEPTH_RENDERABLE',
                         'GL_STENCIL_RENDERABLE',
                         'GL_FRAMEBUFFER_RENDERABLE',
                         'GL_FRAMEBUFFER_RENDERABLE_LAYERED',
                         'GL_FRAMEBUFFER_BLEND',
                         'GL_READ_PIXELS',
                         'GL_READ_PIXELS_FORMAT',
                         'GL_READ_PIXELS_TYPE',
                         'GL_TEXTURE_IMAGE_FORMAT',
                         'GL_TEXTURE_IMAGE_TYPE',
                         'GL_GET_TEXTURE_IMAGE_FORMAT',
                         'GL_GET_TEXTURE_IMAGE_TYPE',
                         'GL_MIPMAP',
                         'GL_GENERATE_MIPMAP',
                         'GL_AUTO_GENERATE_MIPMAP',
                         'GL_COLOR_ENCODING',
                         'GL_SRGB_READ',
                         'GL_SRGB_WRITE',
                         'GL_FILTER',
                         'GL_VERTEX_TEXTURE',
                         'GL_TESS_CONTROL_TEXTURE',
                         'GL_TESS_EVALUATION_TEXTURE',
                         'GL_GEOMETRY_TEXTURE',
                         'GL_FRAGMENT_TEXTURE',
                         'GL_COMPUTE_TEXTURE',
                         'GL_TEXTURE_SHADOW',
                         'GL_TEXTURE_GATHER',
                         'GL_TEXTURE_GATHER_SHADOW',
                         'GL_SHADER_IMAGE_LOAD',
                         'GL_SHADER_IMAGE_STORE',
                         'GL_SHADER_IMAGE_ATOMIC',
                         'GL_IMAGE_TEXEL_SIZE',
                         'GL_IMAGE_COMPATIBILITY_CLASS',
                         'GL_IMAGE_PIXEL_FORMAT',
                         'GL_IMAGE_PIXEL_TYPE',
                         'GL_IMAGE_FORMAT_COMPATIBILITY_TYPE',
                         'GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST',
                         'GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST',
                         'GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE',
                         'GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE',
                         'GL_TEXTURE_COMPRESSED',
                         'GL_TEXTURE_COMPRESSED_BLOCK_WIDTH',
                         'GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT',
                         'GL_TEXTURE_COMPRESSED_BLOCK_SIZE',
                         'GL_CLEAR_BUFFER',
                         'GL_TEXTURE_VIEW',
                         'GL_VIEW_COMPATIBILITY_CLASS',
                         'GL_CLEAR_TEXTURE'],
 'InvalidateFramebufferAttachment': ['GL_COLOR_ATTACHMENT0',
                                     'GL_COLOR_ATTACHMENT0_EXT',
                                     'GL_COLOR_ATTACHMENT1',
                                     'GL_COLOR_ATTACHMENT1_EXT',
                                     'GL_COLOR_ATTACHMENT2',
                                     'GL_COLOR_ATTACHMENT2_EXT',
                                     'GL_COLOR_ATTACHMENT3',
                                     'GL_COLOR_ATTACHMENT3_EXT',
                                     'GL_COLOR_ATTACHMENT4',
                                     'GL_COLOR_ATTACHMENT4_EXT',
                                     'GL_COLOR_ATTACHMENT5',
                                     'GL_COLOR_ATTACHMENT5_EXT',
                                     'GL_COLOR_ATTACHMENT6',
                                     'GL_COLOR_ATTACHMENT6_EXT',
                                     'GL_COLOR_ATTACHMENT7',
                                     'GL_COLOR_ATTACHMENT7_EXT',
                                     'GL_COLOR_ATTACHMENT8',
                                     'GL_COLOR_ATTACHMENT8_EXT',
                                     'GL_COLOR_ATTACHMENT9',
                                     'GL_COLOR_ATTACHMENT9_EXT',
                                     'GL_COLOR_ATTACHMENT10',
                                     'GL_COLOR_ATTACHMENT10_EXT',
                                     'GL_COLOR_ATTACHMENT11',
                                     'GL_COLOR_ATTACHMENT11_EXT',
                                     'GL_COLOR_ATTACHMENT12',
                                     'GL_COLOR_ATTACHMENT12_EXT',
                                     'GL_COLOR_ATTACHMENT13',
                                     'GL_COLOR_ATTACHMENT13_EXT',
                                     'GL_COLOR_ATTACHMENT14',
                                     'GL_COLOR_ATTACHMENT14_EXT',
                                     'GL_COLOR_ATTACHMENT15',
                                     'GL_COLOR_ATTACHMENT15_EXT',
                                     'GL_COLOR_ATTACHMENT16',
                                     'GL_COLOR_ATTACHMENT17',
                                     'GL_COLOR_ATTACHMENT18',
                                     'GL_COLOR_ATTACHMENT19',
                                     'GL_COLOR_ATTACHMENT20',
                                     'GL_COLOR_ATTACHMENT21',
                                     'GL_COLOR_ATTACHMENT22',
                                     'GL_COLOR_ATTACHMENT23',
                                     'GL_COLOR_ATTACHMENT24',
                                     'GL_COLOR_ATTACHMENT25',
                                     'GL_COLOR_ATTACHMENT26',
                                     'GL_COLOR_ATTACHMENT27',
                                     'GL_COLOR_ATTACHMENT28',
                                     'GL_COLOR_ATTACHMENT29',
                                     'GL_COLOR_ATTACHMENT30',
                                     'GL_COLOR_ATTACHMENT31',
                                     'GL_DEPTH_ATTACHMENT',
                                     'GL_DEPTH_STENCIL_ATTACHMENT',
                                     'GL_DEPTH_ATTACHMENT_EXT',
                                     'GL_STENCIL',
                                     'GL_STENCIL_ATTACHMENT_EXT',
                                     'GL_COLOR',
                                     'GL_DEPTH',
                                     'GL_STENCIL'],
 'LightEnvModeSGIX': ['GL_ADD', 'GL_MODULATE', 'GL_REPLACE'],
 'LightEnvParameterSGIX': [],
 'LightModelColorControl': ['GL_SEPARATE_SPECULAR_COLOR',
                            'GL_SEPARATE_SPECULAR_COLOR_EXT',
                            'GL_SINGLE_COLOR',
                            'GL_SINGLE_COLOR_EXT'],
 'LightModelParameter': ['GL_LIGHT_MODEL_AMBIENT',
                         'GL_LIGHT_MODEL_COLOR_CONTROL',
                         'GL_LIGHT_MODEL_COLOR_CONTROL_EXT',
                         'GL_LIGHT_MODEL_LOCAL_VIEWER',
                         'GL_LIGHT_MODEL_TWO_SIDE'],
 'LightName': ['GL_LIGHT0',
               'GL_LIGHT1',
               'GL_LIGHT2',
               'GL_LIGHT3',
               'GL_LIGHT4',
               'GL_LIGHT5',
               'GL_LIGHT6',
               'GL_LIGHT7'],
 'LightParameter': ['GL_AMBIENT',
                    'GL_CONSTANT_ATTENUATION',
                    'GL_DIFFUSE',
                    'GL_LINEAR_ATTENUATION',
                    'GL_POSITION',
                    'GL_QUADRATIC_ATTENUATION',
                    'GL_SPECULAR',
                    'GL_SPOT_CUTOFF',
                    'GL_SPOT_DIRECTION',
                    'GL_SPOT_EXPONENT'],
 'LightTextureModeEXT': ['GL_FRAGMENT_MATERIAL_EXT',
                         'GL_FRAGMENT_NORMAL_EXT',
                         'GL_FRAGMENT_DEPTH_EXT',
                         'GL_FRAGMENT_COLOR_EXT'],
 'LightTexturePNameEXT': ['GL_ATTENUATION_EXT', 'GL_SHADOW_ATTENUATION_EXT'],
 'ListMode': ['GL_COMPILE', 'GL_COMPILE_AND_EXECUTE'],
 'ListNameType': ['GL_2_BYTES',
                  'GL_3_BYTES',
                  'GL_4_BYTES',
                  'GL_BYTE',
                  'GL_FLOAT',
                  'GL_INT',
                  'GL_SHORT',
                  'GL_UNSIGNED_BYTE',
                  'GL_UNSIGNED_INT',
                  'GL_UNSIGNED_SHORT'],
 'ListParameterName': [],
 'LogicOp': ['GL_AND',
             'GL_AND_INVERTED',
             'GL_AND_REVERSE',
             'GL_CLEAR',
             'GL_COPY',
             'GL_COPY_INVERTED',
             'GL_EQUIV',
             'GL_INVERT',
             'GL_NAND',
             'GL_NOOP',
             'GL_NOR',
             'GL_OR',
             'GL_OR_INVERTED',
             'GL_OR_REVERSE',
             'GL_SET',
             'GL_XOR'],
 'MapAttribParameterNV': [],
 'MapBufferAccessMask': ['GL_MAP_COHERENT_BIT',
                         'GL_MAP_COHERENT_BIT_EXT',
                         'GL_MAP_FLUSH_EXPLICIT_BIT',
                         'GL_MAP_FLUSH_EXPLICIT_BIT_EXT',
                         'GL_MAP_INVALIDATE_BUFFER_BIT',
                         'GL_MAP_INVALIDATE_BUFFER_BIT_EXT',
                         'GL_MAP_INVALIDATE_RANGE_BIT',
                         'GL_MAP_INVALIDATE_RANGE_BIT_EXT',
                         'GL_MAP_PERSISTENT_BIT',
                         'GL_MAP_PERSISTENT_BIT_EXT',
                         'GL_MAP_READ_BIT',
                         'GL_MAP_READ_BIT_EXT',
                         'GL_MAP_UNSYNCHRONIZED_BIT',
                         'GL_MAP_UNSYNCHRONIZED_BIT_EXT',
                         'GL_MAP_WRITE_BIT',
                         'GL_MAP_WRITE_BIT_EXT'],
 'MapParameterNV': [],
 'MapQuery': ['GL_COEFF', 'GL_ORDER', 'GL_DOMAIN'],
 'MapTarget': ['GL_MAP1_COLOR_4',
               'GL_MAP1_INDEX',
               'GL_MAP1_NORMAL',
               'GL_MAP1_TEXTURE_COORD_1',
               'GL_MAP1_TEXTURE_COORD_2',
               'GL_MAP1_TEXTURE_COORD_3',
               'GL_MAP1_TEXTURE_COORD_4',
               'GL_MAP1_VERTEX_3',
               'GL_MAP1_VERTEX_4',
               'GL_MAP2_COLOR_4',
               'GL_MAP2_INDEX',
               'GL_MAP2_NORMAL',
               'GL_MAP2_TEXTURE_COORD_1',
               'GL_MAP2_TEXTURE_COORD_2',
               'GL_MAP2_TEXTURE_COORD_3',
               'GL_MAP2_TEXTURE_COORD_4',
               'GL_MAP2_VERTEX_3',
               'GL_MAP2_VERTEX_4'],
 'MapTextureFormatINTEL': [],
 'MapTypeNV': [],
 'MaterialFace': ['GL_BACK', 'GL_FRONT', 'GL_FRONT_AND_BACK'],
 'MaterialParameter': ['GL_AMBIENT',
                       'GL_AMBIENT_AND_DIFFUSE',
                       'GL_COLOR_INDEXES',
                       'GL_DIFFUSE',
                       'GL_EMISSION',
                       'GL_SHININESS',
                       'GL_SPECULAR'],
 'MatrixIndexPointerTypeARB': ['GL_UNSIGNED_BYTE_ARB',
                               'GL_UNSIGNED_SHORT_ARB',
                               'GL_UNSIGNED_INT_ARB'],
 'MatrixMode': ['GL_MODELVIEW',
                'GL_MODELVIEW0_EXT',
                'GL_PROJECTION',
                'GL_TEXTURE'],
 'MemoryBarrierMask': ['GL_ALL_BARRIER_BITS',
                       'GL_ALL_BARRIER_BITS_EXT',
                       'GL_ATOMIC_COUNTER_BARRIER_BIT',
                       'GL_ATOMIC_COUNTER_BARRIER_BIT_EXT',
                       'GL_BUFFER_UPDATE_BARRIER_BIT',
                       'GL_BUFFER_UPDATE_BARRIER_BIT_EXT',
                       'GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT',
                       'GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT_EXT',
                       'GL_COMMAND_BARRIER_BIT',
                       'GL_COMMAND_BARRIER_BIT_EXT',
                       'GL_ELEMENT_ARRAY_BARRIER_BIT',
                       'GL_ELEMENT_ARRAY_BARRIER_BIT_EXT',
                       'GL_FRAMEBUFFER_BARRIER_BIT',
                       'GL_FRAMEBUFFER_BARRIER_BIT_EXT',
                       'GL_PIXEL_BUFFER_BARRIER_BIT',
                       'GL_PIXEL_BUFFER_BARRIER_BIT_EXT',
                       'GL_QUERY_BUFFER_BARRIER_BIT',
                       'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT',
                       'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT_EXT',
                       'GL_SHADER_STORAGE_BARRIER_BIT',
                       'GL_TEXTURE_FETCH_BARRIER_BIT',
                       'GL_TEXTURE_FETCH_BARRIER_BIT_EXT',
                       'GL_TEXTURE_UPDATE_BARRIER_BIT',
                       'GL_TEXTURE_UPDATE_BARRIER_BIT_EXT',
                       'GL_TRANSFORM_FEEDBACK_BARRIER_BIT',
                       'GL_TRANSFORM_FEEDBACK_BARRIER_BIT_EXT',
                       'GL_UNIFORM_BARRIER_BIT',
                       'GL_UNIFORM_BARRIER_BIT_EXT',
                       'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT',
                       'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT_EXT'],
 'MemoryObjectParameterName': ['GL_DEDICATED_MEMORY_OBJECT_EXT',
                               'GL_PROTECTED_MEMORY_OBJECT_EXT'],
 'MeshMode1': ['GL_LINE', 'GL_POINT'],
 'MeshMode2': ['GL_FILL', 'GL_LINE', 'GL_POINT'],
 'MinmaxTargetEXT': ['GL_MINMAX', 'GL_MINMAX_EXT'],
 'NormalPointerType': ['GL_BYTE',
                       'GL_DOUBLE',
                       'GL_FLOAT',
                       'GL_INT',
                       'GL_SHORT'],
 'ObjectIdentifier': ['GL_BUFFER',
                      'GL_SHADER',
                      'GL_PROGRAM',
                      'GL_VERTEX_ARRAY',
                      'GL_QUERY',
                      'GL_PROGRAM_PIPELINE',
                      'GL_TRANSFORM_FEEDBACK',
                      'GL_SAMPLER',
                      'GL_TEXTURE',
                      'GL_RENDERBUFFER',
                      'GL_FRAMEBUFFER'],
 'ObjectTypeAPPLE': [],
 'OcclusionQueryEventMaskAMD': [],
 'OcclusionQueryParameterNameNV': [],
 'PNTrianglesPNameATI': [],
 'ParameterRangeEXT': ['GL_NORMALIZED_RANGE_EXT', 'GL_FULL_RANGE_EXT'],
 'PatchParameterName': ['GL_PATCH_VERTICES',
                        'GL_PATCH_DEFAULT_OUTER_LEVEL',
                        'GL_PATCH_DEFAULT_INNER_LEVEL'],
 'PathColor': ['GL_PRIMARY_COLOR'],
 'PathColorFormat': ['GL_NONE',
                     'GL_LUMINANCE',
                     'GL_ALPHA',
                     'GL_INTENSITY',
                     'GL_LUMINANCE_ALPHA',
                     'GL_RGB',
                     'GL_RGBA'],
 'PathCoordType': [],
 'PathCoverMode': [],
 'PathElementType': [],
 'PathFillMode': ['GL_INVERT'],
 'PathFontStyle': ['GL_NONE'],
 'PathFontTarget': [],
 'PathGenMode': ['GL_NONE', 'GL_EYE_LINEAR', 'GL_OBJECT_LINEAR', 'GL_CONSTANT'],
 'PathHandleMissingGlyphs': [],
 'PathListMode': [],
 'PathMetricMask': [],
 'PathParameter': [],
 'PathStringFormat': [],
 'PathTransformType': ['GL_NONE'],
 'PipelineParameterName': ['GL_ACTIVE_PROGRAM',
                           'GL_VERTEX_SHADER',
                           'GL_TESS_CONTROL_SHADER',
                           'GL_TESS_EVALUATION_SHADER',
                           'GL_GEOMETRY_SHADER',
                           'GL_FRAGMENT_SHADER',
                           'GL_INFO_LOG_LENGTH'],
 'PixelCopyType': ['GL_COLOR',
                   'GL_COLOR_EXT',
                   'GL_DEPTH',
                   'GL_DEPTH_EXT',
                   'GL_STENCIL',
                   'GL_STENCIL_EXT'],
 'PixelDataRangeTargetNV': [],
 'PixelFormat': ['GL_ABGR_EXT',
                 'GL_ALPHA',
                 'GL_BGR',
                 'GL_BGR_INTEGER',
                 'GL_BGRA',
                 'GL_BGRA_INTEGER',
                 'GL_BLUE',
                 'GL_BLUE_INTEGER',
                 'GL_CMYKA_EXT',
                 'GL_CMYK_EXT',
                 'GL_COLOR_INDEX',
                 'GL_DEPTH_COMPONENT',
                 'GL_DEPTH_STENCIL',
                 'GL_GREEN',
                 'GL_GREEN_INTEGER',
                 'GL_LUMINANCE',
                 'GL_LUMINANCE_ALPHA',
                 'GL_RED',
                 'GL_RED_EXT',
                 'GL_RED_INTEGER',
                 'GL_RG',
                 'GL_RG_INTEGER',
                 'GL_RGB',
                 'GL_RGB_INTEGER',
                 'GL_RGBA',
                 'GL_RGBA_INTEGER',
                 'GL_STENCIL_INDEX',
                 'GL_UNSIGNED_INT',
                 'GL_UNSIGNED_SHORT'],
 'PixelMap': ['GL_PIXEL_MAP_A_TO_A',
              'GL_PIXEL_MAP_B_TO_B',
              'GL_PIXEL_MAP_G_TO_G',
              'GL_PIXEL_MAP_I_TO_A',
              'GL_PIXEL_MAP_I_TO_B',
              'GL_PIXEL_MAP_I_TO_G',
              'GL_PIXEL_MAP_I_TO_I',
              'GL_PIXEL_MAP_I_TO_R',
              'GL_PIXEL_MAP_R_TO_R',
              'GL_PIXEL_MAP_S_TO_S'],
 'PixelStoreParameter': ['GL_PACK_ALIGNMENT',
                         'GL_PACK_IMAGE_HEIGHT',
                         'GL_PACK_IMAGE_HEIGHT_EXT',
                         'GL_PACK_LSB_FIRST',
                         'GL_PACK_RESAMPLE_OML',
                         'GL_PACK_ROW_LENGTH',
                         'GL_PACK_SKIP_IMAGES',
                         'GL_PACK_SKIP_IMAGES_EXT',
                         'GL_PACK_SKIP_PIXELS',
                         'GL_PACK_SKIP_ROWS',
                         'GL_PACK_SWAP_BYTES',
                         'GL_UNPACK_ALIGNMENT',
                         'GL_UNPACK_IMAGE_HEIGHT',
                         'GL_UNPACK_IMAGE_HEIGHT_EXT',
                         'GL_UNPACK_LSB_FIRST',
                         'GL_UNPACK_RESAMPLE_OML',
                         'GL_UNPACK_ROW_LENGTH',
                         'GL_UNPACK_ROW_LENGTH_EXT',
                         'GL_UNPACK_SKIP_IMAGES',
                         'GL_UNPACK_SKIP_IMAGES_EXT',
                         'GL_UNPACK_SKIP_PIXELS',
                         'GL_UNPACK_SKIP_PIXELS_EXT',
                         'GL_UNPACK_SKIP_ROWS',
                         'GL_UNPACK_SKIP_ROWS_EXT',
                         'GL_UNPACK_SWAP_BYTES'],
 'PixelStoreResampleMode': [],
 'PixelStoreSubsampleRate': [],
 'PixelTexGenMode': ['GL_LUMINANCE',
                     'GL_LUMINANCE_ALPHA',
                     'GL_NONE',
                     'GL_RGB',
                     'GL_RGBA'],
 'PixelTexGenModeSGIX': [],
 'PixelTexGenParameterNameSGIS': [],
 'PixelTransferParameter': ['GL_ALPHA_BIAS',
                            'GL_ALPHA_SCALE',
                            'GL_BLUE_BIAS',
                            'GL_BLUE_SCALE',
                            'GL_DEPTH_BIAS',
                            'GL_DEPTH_SCALE',
                            'GL_GREEN_BIAS',
                            'GL_GREEN_SCALE',
                            'GL_INDEX_OFFSET',
                            'GL_INDEX_SHIFT',
                            'GL_MAP_COLOR',
                            'GL_MAP_STENCIL',
                            'GL_POST_COLOR_MATRIX_ALPHA_BIAS',
                            'GL_POST_COLOR_MATRIX_ALPHA_SCALE',
                            'GL_POST_COLOR_MATRIX_BLUE_BIAS',
                            'GL_POST_COLOR_MATRIX_BLUE_SCALE',
                            'GL_POST_COLOR_MATRIX_GREEN_BIAS',
                            'GL_POST_COLOR_MATRIX_GREEN_SCALE',
                            'GL_POST_COLOR_MATRIX_RED_BIAS',
                            'GL_POST_COLOR_MATRIX_RED_SCALE',
                            'GL_POST_CONVOLUTION_ALPHA_BIAS',
                            'GL_POST_CONVOLUTION_ALPHA_BIAS_EXT',
                            'GL_POST_CONVOLUTION_ALPHA_SCALE',
                            'GL_POST_CONVOLUTION_ALPHA_SCALE_EXT',
                            'GL_POST_CONVOLUTION_BLUE_BIAS',
                            'GL_POST_CONVOLUTION_BLUE_BIAS_EXT',
                            'GL_POST_CONVOLUTION_BLUE_SCALE',
                            'GL_POST_CONVOLUTION_BLUE_SCALE_EXT',
                            'GL_POST_CONVOLUTION_GREEN_BIAS',
                            'GL_POST_CONVOLUTION_GREEN_BIAS_EXT',
                            'GL_POST_CONVOLUTION_GREEN_SCALE',
                            'GL_POST_CONVOLUTION_GREEN_SCALE_EXT',
                            'GL_POST_CONVOLUTION_RED_BIAS',
                            'GL_POST_CONVOLUTION_RED_BIAS_EXT',
                            'GL_POST_CONVOLUTION_RED_SCALE',
                            'GL_POST_CONVOLUTION_RED_SCALE_EXT',
                            'GL_RED_BIAS',
                            'GL_RED_SCALE'],
 'PixelTransformPNameEXT': ['GL_PIXEL_MAG_FILTER_EXT',
                            'GL_PIXEL_MIN_FILTER_EXT',
                            'GL_PIXEL_CUBIC_WEIGHT_EXT'],
 'PixelTransformTargetEXT': ['GL_PIXEL_TRANSFORM_2D_EXT'],
 'PixelType': ['GL_BITMAP',
               'GL_BYTE',
               'GL_FLOAT',
               'GL_INT',
               'GL_SHORT',
               'GL_UNSIGNED_BYTE',
               'GL_UNSIGNED_BYTE_3_3_2',
               'GL_UNSIGNED_BYTE_3_3_2_EXT',
               'GL_UNSIGNED_INT',
               'GL_UNSIGNED_INT_10_10_10_2',
               'GL_UNSIGNED_INT_10_10_10_2_EXT',
               'GL_UNSIGNED_INT_8_8_8_8',
               'GL_UNSIGNED_INT_8_8_8_8_EXT',
               'GL_UNSIGNED_SHORT',
               'GL_UNSIGNED_SHORT_4_4_4_4',
               'GL_UNSIGNED_SHORT_4_4_4_4_EXT',
               'GL_UNSIGNED_SHORT_5_5_5_1',
               'GL_UNSIGNED_SHORT_5_5_5_1_EXT'],
 'PointParameterNameARB': ['GL_POINT_SIZE_MIN_EXT',
                           'GL_POINT_SIZE_MAX_EXT',
                           'GL_POINT_FADE_THRESHOLD_SIZE_EXT',
                           'GL_POINT_FADE_THRESHOLD_SIZE'],
 'PointParameterNameSGIS': ['GL_DISTANCE_ATTENUATION_EXT',
                            'GL_POINT_DISTANCE_ATTENUATION',
                            'GL_POINT_DISTANCE_ATTENUATION_ARB',
                            'GL_POINT_FADE_THRESHOLD_SIZE',
                            'GL_POINT_FADE_THRESHOLD_SIZE_ARB',
                            'GL_POINT_FADE_THRESHOLD_SIZE_EXT',
                            'GL_POINT_SIZE_MAX',
                            'GL_POINT_SIZE_MAX_ARB',
                            'GL_POINT_SIZE_MAX_EXT',
                            'GL_POINT_SIZE_MIN',
                            'GL_POINT_SIZE_MIN_ARB',
                            'GL_POINT_SIZE_MIN_EXT'],
 'PolygonMode': ['GL_FILL', 'GL_LINE', 'GL_POINT'],
 'PrecisionType': ['GL_LOW_FLOAT',
                   'GL_MEDIUM_FLOAT',
                   'GL_HIGH_FLOAT',
                   'GL_LOW_INT',
                   'GL_MEDIUM_INT',
                   'GL_HIGH_INT'],
 'PreserveModeATI': [],
 'PrimitiveType': ['GL_LINES',
                   'GL_LINES_ADJACENCY',
                   'GL_LINES_ADJACENCY_ARB',
                   'GL_LINES_ADJACENCY_EXT',
                   'GL_LINE_LOOP',
                   'GL_LINE_STRIP',
                   'GL_LINE_STRIP_ADJACENCY',
                   'GL_LINE_STRIP_ADJACENCY_ARB',
                   'GL_LINE_STRIP_ADJACENCY_EXT',
                   'GL_PATCHES',
                   'GL_PATCHES_EXT',
                   'GL_POINTS',
                   'GL_POLYGON',
                   'GL_QUADS',
                   'GL_QUADS_EXT',
                   'GL_QUAD_STRIP',
                   'GL_TRIANGLES',
                   'GL_TRIANGLES_ADJACENCY',
                   'GL_TRIANGLES_ADJACENCY_ARB',
                   'GL_TRIANGLES_ADJACENCY_EXT',
                   'GL_TRIANGLE_FAN',
                   'GL_TRIANGLE_STRIP',
                   'GL_TRIANGLE_STRIP_ADJACENCY',
                   'GL_TRIANGLE_STRIP_ADJACENCY_ARB',
                   'GL_TRIANGLE_STRIP_ADJACENCY_EXT'],
 'ProgramFormat': ['GL_PROGRAM_FORMAT_ASCII'],
 'ProgramFormatARB': ['GL_PROGRAM_FORMAT_ASCII_ARB'],
 'ProgramInterface': ['GL_UNIFORM',
                      'GL_UNIFORM_BLOCK',
                      'GL_PROGRAM_INPUT',
                      'GL_PROGRAM_OUTPUT',
                      'GL_VERTEX_SUBROUTINE',
                      'GL_TESS_CONTROL_SUBROUTINE',
                      'GL_TESS_EVALUATION_SUBROUTINE',
                      'GL_GEOMETRY_SUBROUTINE',
                      'GL_FRAGMENT_SUBROUTINE',
                      'GL_COMPUTE_SUBROUTINE',
                      'GL_VERTEX_SUBROUTINE_UNIFORM',
                      'GL_TESS_CONTROL_SUBROUTINE_UNIFORM',
                      'GL_TESS_EVALUATION_SUBROUTINE_UNIFORM',
                      'GL_GEOMETRY_SUBROUTINE_UNIFORM',
                      'GL_FRAGMENT_SUBROUTINE_UNIFORM',
                      'GL_COMPUTE_SUBROUTINE_UNIFORM',
                      'GL_TRANSFORM_FEEDBACK_VARYING',
                      'GL_TRANSFORM_FEEDBACK_BUFFER',
                      'GL_BUFFER_VARIABLE',
                      'GL_SHADER_STORAGE_BLOCK'],
 'ProgramInterfacePName': ['GL_ACTIVE_RESOURCES',
                           'GL_MAX_NAME_LENGTH',
                           'GL_MAX_NUM_ACTIVE_VARIABLES',
                           'GL_MAX_NUM_COMPATIBLE_SUBROUTINES'],
 'ProgramParameterPName': ['GL_PROGRAM_BINARY_RETRIEVABLE_HINT',
                           'GL_PROGRAM_SEPARABLE'],
 'ProgramPropertyARB': ['GL_DELETE_STATUS',
                        'GL_LINK_STATUS',
                        'GL_VALIDATE_STATUS',
                        'GL_INFO_LOG_LENGTH',
                        'GL_ATTACHED_SHADERS',
                        'GL_ACTIVE_ATOMIC_COUNTER_BUFFERS',
                        'GL_ACTIVE_ATTRIBUTES',
                        'GL_ACTIVE_ATTRIBUTE_MAX_LENGTH',
                        'GL_ACTIVE_UNIFORMS',
                        'GL_ACTIVE_UNIFORM_BLOCKS',
                        'GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH',
                        'GL_ACTIVE_UNIFORM_MAX_LENGTH',
                        'GL_COMPUTE_WORK_GROUP_SIZE',
                        'GL_PROGRAM_BINARY_LENGTH',
                        'GL_TRANSFORM_FEEDBACK_BUFFER_MODE',
                        'GL_TRANSFORM_FEEDBACK_VARYINGS',
                        'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH',
                        'GL_GEOMETRY_VERTICES_OUT',
                        'GL_GEOMETRY_INPUT_TYPE',
                        'GL_GEOMETRY_OUTPUT_TYPE'],
 'ProgramResourceProperty': ['GL_ACTIVE_VARIABLES',
                             'GL_BUFFER_BINDING',
                             'GL_NUM_ACTIVE_VARIABLES',
                             'GL_ARRAY_SIZE',
                             'GL_ARRAY_STRIDE',
                             'GL_BLOCK_INDEX',
                             'GL_IS_ROW_MAJOR',
                             'GL_MATRIX_STRIDE',
                             'GL_ATOMIC_COUNTER_BUFFER_INDEX',
                             'GL_BUFFER_DATA_SIZE',
                             'GL_NUM_COMPATIBLE_SUBROUTINES',
                             'GL_COMPATIBLE_SUBROUTINES',
                             'GL_IS_PER_PATCH',
                             'GL_LOCATION',
                             'GL_UNIFORM',
                             'GL_LOCATION_COMPONENT',
                             'GL_LOCATION_INDEX',
                             'GL_NAME_LENGTH',
                             'GL_OFFSET',
                             'GL_REFERENCED_BY_VERTEX_SHADER',
                             'GL_REFERENCED_BY_TESS_CONTROL_SHADER',
                             'GL_REFERENCED_BY_TESS_EVALUATION_SHADER',
                             'GL_REFERENCED_BY_GEOMETRY_SHADER',
                             'GL_REFERENCED_BY_FRAGMENT_SHADER',
                             'GL_REFERENCED_BY_COMPUTE_SHADER',
                             'GL_TRANSFORM_FEEDBACK_BUFFER_INDEX',
                             'GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE',
                             'GL_TOP_LEVEL_ARRAY_SIZE',
                             'GL_TOP_LEVEL_ARRAY_STRIDE',
                             'GL_TYPE'],
 'ProgramStagePName': ['GL_ACTIVE_SUBROUTINE_UNIFORMS',
                       'GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS',
                       'GL_ACTIVE_SUBROUTINES',
                       'GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH',
                       'GL_ACTIVE_SUBROUTINE_MAX_LENGTH'],
 'ProgramStringProperty': ['GL_PROGRAM_STRING'],
 'ProgramStringPropertyARB': ['GL_PROGRAM_STRING_ARB'],
 'ProgramTarget': ['GL_TEXT_FRAGMENT_SHADER'],
 'ProgramTargetARB': [],
 'QueryCounterTarget': ['GL_TIMESTAMP'],
 'QueryObjectParameterName': ['GL_QUERY_RESULT_AVAILABLE',
                              'GL_QUERY_RESULT',
                              'GL_QUERY_RESULT_NO_WAIT',
                              'GL_QUERY_TARGET'],
 'QueryParameterName': ['GL_CURRENT_QUERY', 'GL_QUERY_COUNTER_BITS'],
 'QueryTarget': ['GL_SAMPLES_PASSED',
                 'GL_ANY_SAMPLES_PASSED',
                 'GL_ANY_SAMPLES_PASSED_CONSERVATIVE',
                 'GL_PRIMITIVES_GENERATED',
                 'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN',
                 'GL_TIME_ELAPSED',
                 'GL_TRANSFORM_FEEDBACK_OVERFLOW',
                 'GL_VERTICES_SUBMITTED',
                 'GL_PRIMITIVES_SUBMITTED',
                 'GL_VERTEX_SHADER_INVOCATIONS'],
 'ReadBufferMode': ['GL_NONE',
                    'GL_AUX0',
                    'GL_AUX1',
                    'GL_AUX2',
                    'GL_AUX3',
                    'GL_BACK',
                    'GL_BACK_LEFT',
                    'GL_BACK_RIGHT',
                    'GL_FRONT',
                    'GL_FRONT_LEFT',
                    'GL_FRONT_RIGHT',
                    'GL_LEFT',
                    'GL_RIGHT',
                    'GL_COLOR_ATTACHMENT0',
                    'GL_COLOR_ATTACHMENT1',
                    'GL_COLOR_ATTACHMENT2',
                    'GL_COLOR_ATTACHMENT3',
                    'GL_COLOR_ATTACHMENT4',
                    'GL_COLOR_ATTACHMENT5',
                    'GL_COLOR_ATTACHMENT6',
                    'GL_COLOR_ATTACHMENT7',
                    'GL_COLOR_ATTACHMENT8',
                    'GL_COLOR_ATTACHMENT9',
                    'GL_COLOR_ATTACHMENT10',
                    'GL_COLOR_ATTACHMENT11',
                    'GL_COLOR_ATTACHMENT12',
                    'GL_COLOR_ATTACHMENT13',
                    'GL_COLOR_ATTACHMENT14',
                    'GL_COLOR_ATTACHMENT15'],
 'RenderbufferParameterName': ['GL_RENDERBUFFER_WIDTH',
                               'GL_RENDERBUFFER_WIDTH_EXT',
                               'GL_RENDERBUFFER_HEIGHT',
                               'GL_RENDERBUFFER_HEIGHT_EXT',
                               'GL_RENDERBUFFER_INTERNAL_FORMAT',
                               'GL_RENDERBUFFER_INTERNAL_FORMAT_EXT',
                               'GL_RENDERBUFFER_SAMPLES',
                               'GL_RENDERBUFFER_SAMPLES_ANGLE',
                               'GL_RENDERBUFFER_SAMPLES_EXT',
                               'GL_RENDERBUFFER_SAMPLES_IMG',
                               'GL_RENDERBUFFER_RED_SIZE',
                               'GL_RENDERBUFFER_RED_SIZE_EXT',
                               'GL_RENDERBUFFER_GREEN_SIZE',
                               'GL_RENDERBUFFER_GREEN_SIZE_EXT',
                               'GL_RENDERBUFFER_BLUE_SIZE',
                               'GL_RENDERBUFFER_BLUE_SIZE_EXT',
                               'GL_RENDERBUFFER_ALPHA_SIZE',
                               'GL_RENDERBUFFER_ALPHA_SIZE_EXT',
                               'GL_RENDERBUFFER_DEPTH_SIZE',
                               'GL_RENDERBUFFER_DEPTH_SIZE_EXT',
                               'GL_RENDERBUFFER_STENCIL_SIZE',
                               'GL_RENDERBUFFER_STENCIL_SIZE_EXT'],
 'RenderbufferTarget': ['GL_RENDERBUFFER'],
 'RenderingMode': ['GL_FEEDBACK', 'GL_RENDER', 'GL_SELECT'],
 'ReplacementCodeTypeSUN': [],
 'SamplePatternEXT': ['GL_1PASS_EXT',
                      'GL_2PASS_0_EXT',
                      'GL_2PASS_1_EXT',
                      'GL_4PASS_0_EXT',
                      'GL_4PASS_1_EXT',
                      'GL_4PASS_2_EXT',
                      'GL_4PASS_3_EXT'],
 'SamplePatternSGIS': ['GL_1PASS_EXT',
                       'GL_2PASS_0_EXT',
                       'GL_2PASS_1_EXT',
                       'GL_4PASS_0_EXT',
                       'GL_4PASS_1_EXT',
                       'GL_4PASS_2_EXT',
                       'GL_4PASS_3_EXT'],
 'SamplerParameterF': ['GL_TEXTURE_BORDER_COLOR',
                       'GL_TEXTURE_MIN_LOD',
                       'GL_TEXTURE_MAX_LOD',
                       'GL_TEXTURE_MAX_ANISOTROPY'],
 'SamplerParameterI': ['GL_TEXTURE_WRAP_S',
                       'GL_TEXTURE_WRAP_T',
                       'GL_TEXTURE_WRAP_R',
                       'GL_TEXTURE_MIN_FILTER',
                       'GL_TEXTURE_MAG_FILTER',
                       'GL_TEXTURE_COMPARE_MODE',
                       'GL_TEXTURE_COMPARE_FUNC'],
 'ScalarType': ['GL_UNSIGNED_BYTE', 'GL_UNSIGNED_SHORT', 'GL_UNSIGNED_INT'],
 'SecondaryColorPointerTypeIBM': [],
 'SemaphoreParameterName': ['GL_D3D12_FENCE_VALUE_EXT'],
 'SeparableTargetEXT': ['GL_SEPARABLE_2D', 'GL_SEPARABLE_2D_EXT'],
 'ShaderParameterName': ['GL_SHADER_TYPE',
                         'GL_DELETE_STATUS',
                         'GL_COMPILE_STATUS',
                         'GL_INFO_LOG_LENGTH',
                         'GL_SHADER_SOURCE_LENGTH'],
 'ShaderType': ['GL_COMPUTE_SHADER',
                'GL_VERTEX_SHADER',
                'GL_TESS_CONTROL_SHADER',
                'GL_TESS_EVALUATION_SHADER',
                'GL_GEOMETRY_SHADER',
                'GL_FRAGMENT_SHADER',
                'GL_FRAGMENT_SHADER_ARB',
                'GL_VERTEX_SHADER_ARB'],
 'ShadingModel': ['GL_FLAT', 'GL_SMOOTH'],
 'SpriteParameterNameSGIX': [],
 'StencilFaceDirection': ['GL_FRONT', 'GL_BACK', 'GL_FRONT_AND_BACK'],
 'StencilFunction': ['GL_ALWAYS',
                     'GL_EQUAL',
                     'GL_GEQUAL',
                     'GL_GREATER',
                     'GL_LEQUAL',
                     'GL_LESS',
                     'GL_NEVER',
                     'GL_NOTEQUAL'],
 'StencilOp': ['GL_DECR',
               'GL_DECR_WRAP',
               'GL_INCR',
               'GL_INCR_WRAP',
               'GL_INVERT',
               'GL_KEEP',
               'GL_REPLACE',
               'GL_ZERO'],
 'StringName': ['GL_EXTENSIONS',
                'GL_RENDERER',
                'GL_VENDOR',
                'GL_VERSION',
                'GL_SHADING_LANGUAGE_VERSION'],
 'SubgroupSupportedFeatures': [],
 'SubroutineParameterName': ['GL_NUM_COMPATIBLE_SUBROUTINES',
                             'GL_COMPATIBLE_SUBROUTINES',
                             'GL_UNIFORM_SIZE',
                             'GL_UNIFORM_NAME_LENGTH'],
 'SwizzleOpATI': [],
 'SyncCondition': ['GL_SYNC_GPU_COMMANDS_COMPLETE'],
 'SyncObjectMask': ['GL_SYNC_FLUSH_COMMANDS_BIT'],
 'SyncParameterName': ['GL_OBJECT_TYPE',
                       'GL_SYNC_STATUS',
                       'GL_SYNC_CONDITION',
                       'GL_SYNC_FLAGS'],
 'SyncStatus': ['GL_ALREADY_SIGNALED',
                'GL_TIMEOUT_EXPIRED',
                'GL_CONDITION_SATISFIED',
                'GL_WAIT_FAILED'],
 'TangentPointerTypeEXT': ['GL_BYTE_EXT',
                           'GL_SHORT_EXT',
                           'GL_FLOAT_EXT',
                           'GL_DOUBLE_EXT'],
 'TexBumpParameterATI': [],
 'TexCoordPointerType': ['GL_DOUBLE', 'GL_FLOAT', 'GL_INT', 'GL_SHORT'],
 'TextureCompareMode': ['GL_NONE',
                        'GL_COMPARE_REF_TO_TEXTURE',
                        'GL_COMPARE_R_TO_TEXTURE'],
 'TextureCoordName': ['GL_S', 'GL_T', 'GL_R', 'GL_Q'],
 'TextureEnvMode': ['GL_ADD',
                    'GL_BLEND',
                    'GL_DECAL',
                    'GL_MODULATE',
                    'GL_REPLACE_EXT'],
 'TextureEnvParameter': ['GL_TEXTURE_ENV_COLOR', 'GL_TEXTURE_ENV_MODE'],
 'TextureEnvTarget': [],
 'TextureFilterFuncSGIS': [],
 'TextureFilterSGIS': [],
 'TextureGenMode': ['GL_EYE_LINEAR', 'GL_OBJECT_LINEAR', 'GL_SPHERE_MAP'],
 'TextureGenParameter': ['GL_EYE_PLANE',
                         'GL_OBJECT_PLANE',
                         'GL_TEXTURE_GEN_MODE'],
 'TextureLayout': ['GL_LAYOUT_GENERAL_EXT',
                   'GL_LAYOUT_COLOR_ATTACHMENT_EXT',
                   'GL_LAYOUT_DEPTH_STENCIL_ATTACHMENT_EXT',
                   'GL_LAYOUT_DEPTH_STENCIL_READ_ONLY_EXT',
                   'GL_LAYOUT_SHADER_READ_ONLY_EXT',
                   'GL_LAYOUT_TRANSFER_SRC_EXT',
                   'GL_LAYOUT_TRANSFER_DST_EXT',
                   'GL_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_EXT',
                   'GL_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_EXT'],
 'TextureMagFilter': ['GL_LINEAR', 'GL_NEAREST'],
 'TextureMinFilter': ['GL_LINEAR',
                      'GL_LINEAR_MIPMAP_LINEAR',
                      'GL_LINEAR_MIPMAP_NEAREST',
                      'GL_NEAREST',
                      'GL_NEAREST_MIPMAP_LINEAR',
                      'GL_NEAREST_MIPMAP_NEAREST'],
 'TextureNormalModeEXT': ['GL_PERTURB_EXT'],
 'TextureParameterName': ['GL_GENERATE_MIPMAP',
                          'GL_TEXTURE_BORDER_COLOR',
                          'GL_TEXTURE_MAG_FILTER',
                          'GL_TEXTURE_MIN_FILTER',
                          'GL_TEXTURE_PRIORITY',
                          'GL_TEXTURE_PRIORITY_EXT',
                          'GL_TEXTURE_WRAP_R',
                          'GL_TEXTURE_WRAP_R_EXT',
                          'GL_TEXTURE_WRAP_S',
                          'GL_TEXTURE_WRAP_T',
                          'GL_TEXTURE_BASE_LEVEL',
                          'GL_TEXTURE_COMPARE_MODE',
                          'GL_TEXTURE_COMPARE_FUNC',
                          'GL_TEXTURE_LOD_BIAS',
                          'GL_TEXTURE_MIN_LOD',
                          'GL_TEXTURE_MAX_LOD',
                          'GL_TEXTURE_MAX_LEVEL',
                          'GL_TEXTURE_SWIZZLE_R',
                          'GL_TEXTURE_SWIZZLE_G',
                          'GL_TEXTURE_SWIZZLE_B',
                          'GL_TEXTURE_SWIZZLE_A',
                          'GL_TEXTURE_SWIZZLE_RGBA',
                          'GL_TEXTURE_TILING_EXT',
                          'GL_DEPTH_STENCIL_TEXTURE_MODE',
                          'GL_TEXTURE_ALPHA_SIZE',
                          'GL_TEXTURE_BLUE_SIZE',
                          'GL_TEXTURE_BORDER',
                          'GL_TEXTURE_COMPONENTS',
                          'GL_TEXTURE_DEPTH_EXT',
                          'GL_TEXTURE_GREEN_SIZE',
                          'GL_TEXTURE_HEIGHT',
                          'GL_TEXTURE_INTENSITY_SIZE',
                          'GL_TEXTURE_INTERNAL_FORMAT',
                          'GL_TEXTURE_LUMINANCE_SIZE',
                          'GL_TEXTURE_RED_SIZE',
                          'GL_TEXTURE_RESIDENT',
                          'GL_TEXTURE_WIDTH'],
 'TextureStorageMaskAMD': [],
 'TextureSwizzle': ['GL_RED',
                    'GL_GREEN',
                    'GL_BLUE',
                    'GL_ALPHA',
                    'GL_ZERO',
                    'GL_ONE'],
 'TextureTarget': ['GL_PROXY_TEXTURE_1D',
                   'GL_PROXY_TEXTURE_1D_ARRAY',
                   'GL_PROXY_TEXTURE_1D_ARRAY_EXT',
                   'GL_PROXY_TEXTURE_1D_EXT',
                   'GL_PROXY_TEXTURE_2D',
                   'GL_PROXY_TEXTURE_2D_ARRAY',
                   'GL_PROXY_TEXTURE_2D_ARRAY_EXT',
                   'GL_PROXY_TEXTURE_2D_EXT',
                   'GL_PROXY_TEXTURE_2D_MULTISAMPLE',
                   'GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY',
                   'GL_PROXY_TEXTURE_3D',
                   'GL_PROXY_TEXTURE_3D_EXT',
                   'GL_PROXY_TEXTURE_CUBE_MAP',
                   'GL_PROXY_TEXTURE_CUBE_MAP_ARB',
                   'GL_PROXY_TEXTURE_CUBE_MAP_EXT',
                   'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY',
                   'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB',
                   'GL_PROXY_TEXTURE_RECTANGLE',
                   'GL_PROXY_TEXTURE_RECTANGLE_ARB',
                   'GL_TEXTURE_1D',
                   'GL_TEXTURE_2D',
                   'GL_TEXTURE_3D',
                   'GL_TEXTURE_3D_EXT',
                   'GL_TEXTURE_RECTANGLE',
                   'GL_TEXTURE_CUBE_MAP',
                   'GL_TEXTURE_CUBE_MAP_POSITIVE_X',
                   'GL_TEXTURE_CUBE_MAP_NEGATIVE_X',
                   'GL_TEXTURE_CUBE_MAP_POSITIVE_Y',
                   'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y',
                   'GL_TEXTURE_CUBE_MAP_POSITIVE_Z',
                   'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z',
                   'GL_TEXTURE_CUBE_MAP_ARRAY',
                   'GL_TEXTURE_CUBE_MAP_ARRAY_ARB',
                   'GL_TEXTURE_CUBE_MAP_ARRAY_EXT',
                   'GL_TEXTURE_1D_ARRAY',
                   'GL_TEXTURE_2D_ARRAY',
                   'GL_TEXTURE_2D_MULTISAMPLE',
                   'GL_TEXTURE_2D_MULTISAMPLE_ARRAY'],
 'TextureUnit': ['GL_TEXTURE0',
                 'GL_TEXTURE1',
                 'GL_TEXTURE2',
                 'GL_TEXTURE3',
                 'GL_TEXTURE4',
                 'GL_TEXTURE5',
                 'GL_TEXTURE6',
                 'GL_TEXTURE7',
                 'GL_TEXTURE8',
                 'GL_TEXTURE9',
                 'GL_TEXTURE10',
                 'GL_TEXTURE11',
                 'GL_TEXTURE12',
                 'GL_TEXTURE13',
                 'GL_TEXTURE14',
                 'GL_TEXTURE15',
                 'GL_TEXTURE16',
                 'GL_TEXTURE17',
                 'GL_TEXTURE18',
                 'GL_TEXTURE19',
                 'GL_TEXTURE20',
                 'GL_TEXTURE21',
                 'GL_TEXTURE22',
                 'GL_TEXTURE23',
                 'GL_TEXTURE24',
                 'GL_TEXTURE25',
                 'GL_TEXTURE26',
                 'GL_TEXTURE27',
                 'GL_TEXTURE28',
                 'GL_TEXTURE29',
                 'GL_TEXTURE30',
                 'GL_TEXTURE31'],
 'TextureWrapMode': ['GL_CLAMP',
                     'GL_CLAMP_TO_BORDER',
                     'GL_CLAMP_TO_BORDER_ARB',
                     'GL_CLAMP_TO_EDGE',
                     'GL_REPEAT',
                     'GL_LINEAR_MIPMAP_LINEAR',
                     'GL_MIRRORED_REPEAT'],
 'TransformFeedbackBufferMode': ['GL_INTERLEAVED_ATTRIBS',
                                 'GL_SEPARATE_ATTRIBS'],
 'TransformFeedbackPName': ['GL_TRANSFORM_FEEDBACK_BUFFER_BINDING',
                            'GL_TRANSFORM_FEEDBACK_BUFFER_START',
                            'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE',
                            'GL_TRANSFORM_FEEDBACK_PAUSED',
                            'GL_TRANSFORM_FEEDBACK_ACTIVE'],
 'UniformBlockPName': ['GL_UNIFORM_BLOCK_BINDING',
                       'GL_UNIFORM_BLOCK_DATA_SIZE',
                       'GL_UNIFORM_BLOCK_NAME_LENGTH',
                       'GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS',
                       'GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES',
                       'GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER',
                       'GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER',
                       'GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER',
                       'GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER',
                       'GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER',
                       'GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER'],
 'UniformPName': ['GL_UNIFORM_TYPE',
                  'GL_UNIFORM_SIZE',
                  'GL_UNIFORM_NAME_LENGTH',
                  'GL_UNIFORM_BLOCK_INDEX',
                  'GL_UNIFORM_OFFSET',
                  'GL_UNIFORM_ARRAY_STRIDE',
                  'GL_UNIFORM_MATRIX_STRIDE',
                  'GL_UNIFORM_IS_ROW_MAJOR',
                  'GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX'],
 'UniformType': ['GL_INT',
                 'GL_UNSIGNED_INT',
                 'GL_FLOAT',
                 'GL_DOUBLE',
                 'GL_FLOAT_VEC2',
                 'GL_FLOAT_VEC3',
                 'GL_FLOAT_VEC4',
                 'GL_INT_VEC2',
                 'GL_INT_VEC3',
                 'GL_INT_VEC4',
                 'GL_BOOL',
                 'GL_BOOL_VEC2',
                 'GL_BOOL_VEC3',
                 'GL_BOOL_VEC4',
                 'GL_FLOAT_MAT2',
                 'GL_FLOAT_MAT3',
                 'GL_FLOAT_MAT4',
                 'GL_SAMPLER_1D',
                 'GL_SAMPLER_2D',
                 'GL_SAMPLER_3D',
                 'GL_SAMPLER_CUBE',
                 'GL_SAMPLER_1D_SHADOW',
                 'GL_SAMPLER_2D_SHADOW',
                 'GL_SAMPLER_2D_RECT',
                 'GL_SAMPLER_2D_RECT_SHADOW',
                 'GL_FLOAT_MAT2X3',
                 'GL_FLOAT_MAT2X4',
                 'GL_FLOAT_MAT3X2',
                 'GL_FLOAT_MAT3X4',
                 'GL_FLOAT_MAT4X2',
                 'GL_FLOAT_MAT4X3',
                 'GL_SAMPLER_1D_ARRAY',
                 'GL_SAMPLER_2D_ARRAY',
                 'GL_SAMPLER_BUFFER',
                 'GL_SAMPLER_1D_ARRAY_SHADOW',
                 'GL_SAMPLER_2D_ARRAY_SHADOW',
                 'GL_SAMPLER_CUBE_SHADOW',
                 'GL_UNSIGNED_INT_VEC2',
                 'GL_UNSIGNED_INT_VEC3',
                 'GL_UNSIGNED_INT_VEC4',
                 'GL_INT_SAMPLER_1D',
                 'GL_INT_SAMPLER_2D',
                 'GL_INT_SAMPLER_3D',
                 'GL_INT_SAMPLER_CUBE',
                 'GL_INT_SAMPLER_2D_RECT',
                 'GL_INT_SAMPLER_1D_ARRAY',
                 'GL_INT_SAMPLER_2D_ARRAY',
                 'GL_INT_SAMPLER_BUFFER',
                 'GL_UNSIGNED_INT_SAMPLER_1D',
                 'GL_UNSIGNED_INT_SAMPLER_2D',
                 'GL_UNSIGNED_INT_SAMPLER_3D',
                 'GL_UNSIGNED_INT_SAMPLER_CUBE',
                 'GL_UNSIGNED_INT_SAMPLER_2D_RECT',
                 'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY',
                 'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY',
                 'GL_UNSIGNED_INT_SAMPLER_BUFFER',
                 'GL_DOUBLE_MAT2',
                 'GL_DOUBLE_MAT3',
                 'GL_DOUBLE_MAT4',
                 'GL_DOUBLE_MAT2x3',
                 'GL_DOUBLE_MAT2x4',
                 'GL_DOUBLE_MAT3x2',
                 'GL_DOUBLE_MAT3x4',
                 'GL_DOUBLE_MAT4x2',
                 'GL_DOUBLE_MAT4x3',
                 'GL_DOUBLE_VEC2',
                 'GL_DOUBLE_VEC3',
                 'GL_DOUBLE_VEC4',
                 'GL_SAMPLER_CUBE_MAP_ARRAY',
                 'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW',
                 'GL_INT_SAMPLER_CUBE_MAP_ARRAY',
                 'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY',
                 'GL_SAMPLER_2D_MULTISAMPLE',
                 'GL_INT_SAMPLER_2D_MULTISAMPLE',
                 'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE',
                 'GL_SAMPLER_2D_MULTISAMPLE_ARRAY',
                 'GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY',
                 'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY'],
 'UseProgramStageMask': ['GL_VERTEX_SHADER_BIT',
                         'GL_VERTEX_SHADER_BIT_EXT',
                         'GL_FRAGMENT_SHADER_BIT',
                         'GL_FRAGMENT_SHADER_BIT_EXT',
                         'GL_GEOMETRY_SHADER_BIT',
                         'GL_GEOMETRY_SHADER_BIT_EXT',
                         'GL_TESS_CONTROL_SHADER_BIT',
                         'GL_TESS_CONTROL_SHADER_BIT_EXT',
                         'GL_TESS_EVALUATION_SHADER_BIT',
                         'GL_TESS_EVALUATION_SHADER_BIT_EXT',
                         'GL_COMPUTE_SHADER_BIT',
                         'GL_ALL_SHADER_BITS',
                         'GL_ALL_SHADER_BITS_EXT'],
 'VariantCapEXT': ['GL_VARIANT_ARRAY_EXT'],
 'VertexArrayPName': ['GL_VERTEX_ATTRIB_ARRAY_ENABLED',
                      'GL_VERTEX_ATTRIB_ARRAY_SIZE',
                      'GL_VERTEX_ATTRIB_ARRAY_STRIDE',
                      'GL_VERTEX_ATTRIB_ARRAY_TYPE',
                      'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED',
                      'GL_VERTEX_ATTRIB_ARRAY_INTEGER',
                      'GL_VERTEX_ATTRIB_ARRAY_LONG',
                      'GL_VERTEX_ATTRIB_ARRAY_DIVISOR',
                      'GL_VERTEX_ATTRIB_RELATIVE_OFFSET'],
 'VertexArrayPNameAPPLE': [],
 'VertexAttribEnum': ['GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING',
                      'GL_VERTEX_ATTRIB_ARRAY_ENABLED',
                      'GL_VERTEX_ATTRIB_ARRAY_SIZE',
                      'GL_VERTEX_ATTRIB_ARRAY_STRIDE',
                      'GL_VERTEX_ATTRIB_ARRAY_TYPE',
                      'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED',
                      'GL_VERTEX_ATTRIB_ARRAY_INTEGER',
                      'GL_VERTEX_ATTRIB_ARRAY_DIVISOR',
                      'GL_CURRENT_VERTEX_ATTRIB'],
 'VertexAttribEnumNV': [],
 'VertexAttribIType': ['GL_BYTE',
                       'GL_UNSIGNED_BYTE',
                       'GL_SHORT',
                       'GL_UNSIGNED_SHORT',
                       'GL_INT',
                       'GL_UNSIGNED_INT'],
 'VertexAttribLType': ['GL_DOUBLE'],
 'VertexAttribPointerPropertyARB': ['GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB',
                                    'GL_VERTEX_ATTRIB_ARRAY_POINTER'],
 'VertexAttribPointerType': ['GL_BYTE',
                             'GL_UNSIGNED_BYTE',
                             'GL_SHORT',
                             'GL_UNSIGNED_SHORT',
                             'GL_INT',
                             'GL_UNSIGNED_INT',
                             'GL_FLOAT',
                             'GL_DOUBLE',
                             'GL_HALF_FLOAT',
                             'GL_FIXED',
                             'GL_INT_2_10_10_10_REV',
                             'GL_UNSIGNED_INT_2_10_10_10_REV',
                             'GL_UNSIGNED_INT_10F_11F_11F_REV'],
 'VertexAttribPropertyARB': ['GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING',
                             'GL_VERTEX_ATTRIB_ARRAY_ENABLED',
                             'GL_VERTEX_ATTRIB_ARRAY_SIZE',
                             'GL_VERTEX_ATTRIB_ARRAY_STRIDE',
                             'GL_VERTEX_ATTRIB_ARRAY_TYPE',
                             'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED',
                             'GL_VERTEX_ATTRIB_ARRAY_INTEGER',
                             'GL_VERTEX_ATTRIB_ARRAY_LONG',
                             'GL_VERTEX_ATTRIB_ARRAY_DIVISOR',
                             'GL_VERTEX_ATTRIB_BINDING',
                             'GL_VERTEX_ATTRIB_RELATIVE_OFFSET',
                             'GL_CURRENT_VERTEX_ATTRIB',
                             'GL_VERTEX_ATTRIB_ARRAY_INTEGER_EXT'],
 'VertexAttribType': ['GL_BYTE',
                      'GL_SHORT',
                      'GL_INT',
                      'GL_FIXED',
                      'GL_FLOAT',
                      'GL_HALF_FLOAT',
                      'GL_DOUBLE',
                      'GL_UNSIGNED_BYTE',
                      'GL_UNSIGNED_SHORT',
                      'GL_UNSIGNED_INT',
                      'GL_INT_2_10_10_10_REV',
                      'GL_UNSIGNED_INT_2_10_10_10_REV',
                      'GL_UNSIGNED_INT_10F_11F_11F_REV'],
 'VertexBufferObjectParameter': ['GL_BUFFER_ACCESS',
                                 'GL_BUFFER_ACCESS_FLAGS',
                                 'GL_BUFFER_IMMUTABLE_STORAGE',
                                 'GL_BUFFER_MAPPED',
                                 'GL_BUFFER_MAP_LENGTH',
                                 'GL_BUFFER_MAP_OFFSET',
                                 'GL_BUFFER_SIZE',
                                 'GL_BUFFER_STORAGE_FLAGS',
                                 'GL_BUFFER_USAGE'],
 'VertexBufferObjectUsage': ['GL_STREAM_DRAW',
                             'GL_STREAM_READ',
                             'GL_STREAM_COPY',
                             'GL_STATIC_DRAW',
                             'GL_STATIC_READ',
                             'GL_STATIC_COPY',
                             'GL_DYNAMIC_DRAW',
                             'GL_DYNAMIC_READ',
                             'GL_DYNAMIC_COPY'],
 'VertexPointerType': ['GL_DOUBLE', 'GL_FLOAT', 'GL_INT', 'GL_SHORT'],
 'VertexProvokingMode': ['GL_FIRST_VERTEX_CONVENTION',
                         'GL_LAST_VERTEX_CONVENTION'],
 'VertexShaderCoordOutEXT': ['GL_X_EXT',
                             'GL_Y_EXT',
                             'GL_Z_EXT',
                             'GL_W_EXT',
                             'GL_NEGATIVE_X_EXT',
                             'GL_NEGATIVE_Y_EXT',
                             'GL_NEGATIVE_Z_EXT',
                             'GL_NEGATIVE_W_EXT',
                             'GL_ZERO_EXT',
                             'GL_ONE_EXT',
                             'GL_NEGATIVE_ONE_EXT'],
 'VertexShaderOpEXT': ['GL_OP_INDEX_EXT',
                       'GL_OP_NEGATE_EXT',
                       'GL_OP_DOT3_EXT',
                       'GL_OP_DOT4_EXT',
                       'GL_OP_MUL_EXT',
                       'GL_OP_ADD_EXT',
                       'GL_OP_MADD_EXT',
                       'GL_OP_FRAC_EXT',
                       'GL_OP_MAX_EXT',
                       'GL_OP_MIN_EXT',
                       'GL_OP_SET_GE_EXT',
                       'GL_OP_SET_LT_EXT',
                       'GL_OP_CLAMP_EXT',
                       'GL_OP_FLOOR_EXT',
                       'GL_OP_ROUND_EXT',
                       'GL_OP_EXP_BASE_2_EXT',
                       'GL_OP_LOG_BASE_2_EXT',
                       'GL_OP_POWER_EXT',
                       'GL_OP_RECIP_EXT',
                       'GL_OP_RECIP_SQRT_EXT',
                       'GL_OP_SUB_EXT',
                       'GL_OP_CROSS_PRODUCT_EXT',
                       'GL_OP_MULTIPLY_MATRIX_EXT',
                       'GL_OP_MOV_EXT'],
 'VertexShaderParameterEXT': ['GL_CURRENT_VERTEX_EXT', 'GL_MVP_MATRIX_EXT'],
 'VertexShaderStorageTypeEXT': ['GL_VARIANT_EXT',
                                'GL_INVARIANT_EXT',
                                'GL_LOCAL_CONSTANT_EXT',
                                'GL_LOCAL_EXT'],
 'VertexShaderTextureUnitParameter': ['GL_CURRENT_TEXTURE_COORDS',
                                      'GL_TEXTURE_MATRIX'],
 'VertexShaderWriteMaskEXT': ['GL_TRUE_EXT', 'GL_FALSE_EXT'],
 'VertexStreamATI': [],
 'VertexWeightPointerTypeEXT': ['GL_FLOAT_EXT'],
 'WeightPointerTypeARB': ['GL_BYTE_ARB',
                          'GL_UNSIGNED_BYTE_ARB',
                          'GL_SHORT_ARB',
                          'GL_UNSIGNED_SHORT_ARB',
                          'GL_INT_ARB',
                          'GL_UNSIGNED_INT_ARB',
                          'GL_FLOAT_ARB',
                          'GL_DOUBLE_ARB']}
gligroups= {'GL_1PASS_EXT': ['SamplePatternEXT', 'SamplePatternSGIS'],
 'GL_2D': ['FeedbackType'],
 'GL_2PASS_0_EXT': ['SamplePatternEXT', 'SamplePatternSGIS'],
 'GL_2PASS_1_EXT': ['SamplePatternEXT', 'SamplePatternSGIS'],
 'GL_2_BYTES': ['ListNameType'],
 'GL_3D': ['FeedbackType'],
 'GL_3D_COLOR': ['FeedbackType'],
 'GL_3D_COLOR_TEXTURE': ['FeedbackType'],
 'GL_3_BYTES': ['ListNameType'],
 'GL_4D_COLOR_TEXTURE': ['FeedbackType'],
 'GL_4PASS_0_EXT': ['SamplePatternEXT', 'SamplePatternSGIS'],
 'GL_4PASS_1_EXT': ['SamplePatternEXT', 'SamplePatternSGIS'],
 'GL_4PASS_2_EXT': ['SamplePatternEXT', 'SamplePatternSGIS'],
 'GL_4PASS_3_EXT': ['SamplePatternEXT', 'SamplePatternSGIS'],
 'GL_4_BYTES': ['ListNameType'],
 'GL_ABGR_EXT': ['PixelFormat'],
 'GL_ACCUM': ['AccumOp'],
 'GL_ACCUM_ALPHA_BITS': ['GetPName'],
 'GL_ACCUM_BLUE_BITS': ['GetPName'],
 'GL_ACCUM_BUFFER_BIT': ['AttribMask', 'ClearBufferMask'],
 'GL_ACCUM_CLEAR_VALUE': ['GetPName'],
 'GL_ACCUM_GREEN_BITS': ['GetPName'],
 'GL_ACCUM_RED_BITS': ['GetPName'],
 'GL_ACTIVE_ATOMIC_COUNTER_BUFFERS': ['ProgramPropertyARB'],
 'GL_ACTIVE_ATTRIBUTES': ['ProgramPropertyARB'],
 'GL_ACTIVE_ATTRIBUTE_MAX_LENGTH': ['ProgramPropertyARB'],
 'GL_ACTIVE_PROGRAM': ['PipelineParameterName'],
 'GL_ACTIVE_RESOURCES': ['ProgramInterfacePName'],
 'GL_ACTIVE_SUBROUTINES': ['ProgramStagePName'],
 'GL_ACTIVE_SUBROUTINE_MAX_LENGTH': ['ProgramStagePName'],
 'GL_ACTIVE_SUBROUTINE_UNIFORMS': ['ProgramStagePName'],
 'GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS': ['ProgramStagePName'],
 'GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH': ['ProgramStagePName'],
 'GL_ACTIVE_TEXTURE': ['GetPName'],
 'GL_ACTIVE_UNIFORMS': ['ProgramPropertyARB'],
 'GL_ACTIVE_UNIFORM_BLOCKS': ['ProgramPropertyARB'],
 'GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH': ['ProgramPropertyARB'],
 'GL_ACTIVE_UNIFORM_MAX_LENGTH': ['ProgramPropertyARB'],
 'GL_ACTIVE_VARIABLES': ['ProgramResourceProperty'],
 'GL_ADD': ['AccumOp', 'LightEnvModeSGIX', 'TextureEnvMode'],
 'GL_ALIASED_LINE_WIDTH_RANGE': ['GetPName'],
 'GL_ALIASED_POINT_SIZE_RANGE': ['GetPName'],
 'GL_ALL_ATTRIB_BITS': ['AttribMask'],
 'GL_ALL_BARRIER_BITS': ['MemoryBarrierMask'],
 'GL_ALL_BARRIER_BITS_EXT': ['MemoryBarrierMask'],
 'GL_ALL_SHADER_BITS': ['UseProgramStageMask'],
 'GL_ALL_SHADER_BITS_EXT': ['UseProgramStageMask'],
 'GL_ALPHA': ['PathColorFormat', 'PixelFormat', 'TextureSwizzle'],
 'GL_ALPHA12': ['InternalFormat'],
 'GL_ALPHA16': ['InternalFormat'],
 'GL_ALPHA4': ['InternalFormat'],
 'GL_ALPHA8': ['InternalFormat'],
 'GL_ALPHA_BIAS': ['GetPName', 'PixelTransferParameter'],
 'GL_ALPHA_BITS': ['GetPName'],
 'GL_ALPHA_SCALE': ['GetPName', 'PixelTransferParameter'],
 'GL_ALPHA_TEST': ['EnableCap', 'GetPName'],
 'GL_ALPHA_TEST_FUNC': ['GetPName'],
 'GL_ALPHA_TEST_REF': ['GetPName'],
 'GL_ALREADY_SIGNALED': ['SyncStatus'],
 'GL_ALWAYS': ['AlphaFunction', 'DepthFunction', 'StencilFunction'],
 'GL_ALWAYS_EXT': ['IndexFunctionEXT'],
 'GL_AMBIENT': ['ColorMaterialParameter',
                'LightParameter',
                'MaterialParameter'],
 'GL_AMBIENT_AND_DIFFUSE': ['ColorMaterialParameter', 'MaterialParameter'],
 'GL_AND': ['LogicOp'],
 'GL_AND_INVERTED': ['LogicOp'],
 'GL_AND_REVERSE': ['LogicOp'],
 'GL_ANY_SAMPLES_PASSED': ['QueryTarget'],
 'GL_ANY_SAMPLES_PASSED_CONSERVATIVE': ['QueryTarget'],
 'GL_ARRAY_BUFFER': ['BufferTargetARB',
                     'BufferStorageTarget',
                     'CopyBufferSubDataTarget'],
 'GL_ARRAY_BUFFER_BINDING': ['GetPName'],
 'GL_ARRAY_SIZE': ['ProgramResourceProperty'],
 'GL_ARRAY_STRIDE': ['ProgramResourceProperty'],
 'GL_ATOMIC_COUNTER_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_ATOMIC_COUNTER_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_ATOMIC_COUNTER_BUFFER': ['BufferTargetARB',
                              'BufferStorageTarget',
                              'CopyBufferSubDataTarget'],
 'GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_BINDING': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_INDEX': ['ProgramResourceProperty'],
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER': ['AtomicCounterBufferPName'],
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER': ['AtomicCounterBufferPName'],
 'GL_ATTACHED_SHADERS': ['ProgramPropertyARB'],
 'GL_ATTENUATION_EXT': ['LightTexturePNameEXT'],
 'GL_ATTRIB_STACK_DEPTH': ['GetPName'],
 'GL_AUTO_GENERATE_MIPMAP': ['InternalFormatPName'],
 'GL_AUTO_NORMAL': ['EnableCap', 'GetPName'],
 'GL_AUX0': ['DrawBufferMode', 'ReadBufferMode'],
 'GL_AUX1': ['DrawBufferMode', 'ReadBufferMode'],
 'GL_AUX2': ['DrawBufferMode', 'ReadBufferMode'],
 'GL_AUX3': ['DrawBufferMode', 'ReadBufferMode'],
 'GL_AUX_BUFFERS': ['GetPName'],
 'GL_BACK': ['ColorMaterialFace',
             'CullFaceMode',
             'DrawBufferMode',
             'MaterialFace',
             'ReadBufferMode',
             'StencilFaceDirection',
             'ColorBuffer'],
 'GL_BACK_LEFT': ['DrawBufferMode', 'ReadBufferMode', 'ColorBuffer'],
 'GL_BACK_RIGHT': ['DrawBufferMode', 'ReadBufferMode', 'ColorBuffer'],
 'GL_BGR': ['PixelFormat'],
 'GL_BGRA': ['PixelFormat'],
 'GL_BGRA_INTEGER': ['PixelFormat'],
 'GL_BGR_INTEGER': ['PixelFormat'],
 'GL_BITMAP': ['PixelType'],
 'GL_BITMAP_TOKEN': ['FeedBackToken'],
 'GL_BLEND': ['EnableCap', 'GetPName', 'TextureEnvMode'],
 'GL_BLEND_COLOR': ['GetPName'],
 'GL_BLEND_COLOR_EXT': ['GetPName'],
 'GL_BLEND_DST': ['GetPName'],
 'GL_BLEND_DST_ALPHA': ['GetPName'],
 'GL_BLEND_DST_RGB': ['GetPName'],
 'GL_BLEND_EQUATION_ALPHA': ['GetPName'],
 'GL_BLEND_EQUATION_EXT': ['GetPName'],
 'GL_BLEND_EQUATION_RGB': ['GetPName'],
 'GL_BLEND_SRC': ['GetPName'],
 'GL_BLEND_SRC_ALPHA': ['GetPName'],
 'GL_BLEND_SRC_RGB': ['GetPName'],
 'GL_BLOCK_INDEX': ['ProgramResourceProperty'],
 'GL_BLUE': ['PixelFormat', 'TextureSwizzle'],
 'GL_BLUE_BIAS': ['GetPName', 'PixelTransferParameter'],
 'GL_BLUE_BITS': ['GetPName'],
 'GL_BLUE_INTEGER': ['PixelFormat'],
 'GL_BLUE_SCALE': ['GetPName', 'PixelTransferParameter'],
 'GL_BOOL': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_BOOL_ARB': ['AttributeType'],
 'GL_BOOL_VEC2': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_BOOL_VEC2_ARB': ['AttributeType'],
 'GL_BOOL_VEC3': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_BOOL_VEC3_ARB': ['AttributeType'],
 'GL_BOOL_VEC4': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_BOOL_VEC4_ARB': ['AttributeType'],
 'GL_BUFFER': ['ObjectIdentifier'],
 'GL_BUFFER_ACCESS': ['BufferPNameARB', 'VertexBufferObjectParameter'],
 'GL_BUFFER_ACCESS_ARB': ['BufferPNameARB'],
 'GL_BUFFER_ACCESS_FLAGS': ['BufferPNameARB', 'VertexBufferObjectParameter'],
 'GL_BUFFER_BINDING': ['ProgramResourceProperty'],
 'GL_BUFFER_DATA_SIZE': ['ProgramResourceProperty'],
 'GL_BUFFER_IMMUTABLE_STORAGE': ['BufferPNameARB',
                                 'VertexBufferObjectParameter'],
 'GL_BUFFER_MAPPED': ['BufferPNameARB', 'VertexBufferObjectParameter'],
 'GL_BUFFER_MAPPED_ARB': ['BufferPNameARB'],
 'GL_BUFFER_MAP_LENGTH': ['BufferPNameARB', 'VertexBufferObjectParameter'],
 'GL_BUFFER_MAP_OFFSET': ['BufferPNameARB', 'VertexBufferObjectParameter'],
 'GL_BUFFER_MAP_POINTER': ['BufferPointerNameARB'],
 'GL_BUFFER_MAP_POINTER_ARB': ['BufferPointerNameARB'],
 'GL_BUFFER_SIZE': ['BufferPNameARB', 'VertexBufferObjectParameter'],
 'GL_BUFFER_SIZE_ARB': ['BufferPNameARB'],
 'GL_BUFFER_STORAGE_FLAGS': ['BufferPNameARB', 'VertexBufferObjectParameter'],
 'GL_BUFFER_UPDATE_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_BUFFER_UPDATE_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_BUFFER_USAGE': ['BufferPNameARB', 'VertexBufferObjectParameter'],
 'GL_BUFFER_USAGE_ARB': ['BufferPNameARB'],
 'GL_BUFFER_VARIABLE': ['ProgramInterface'],
 'GL_BYTE': ['ColorPointerType',
             'ListNameType',
             'NormalPointerType',
             'PixelType',
             'VertexAttribType',
             'VertexAttribPointerType',
             'VertexAttribIType'],
 'GL_BYTE_ARB': ['WeightPointerTypeARB'],
 'GL_BYTE_EXT': ['TangentPointerTypeEXT', 'BinormalPointerTypeEXT'],
 'GL_C3F_V3F': ['InterleavedArrayFormat'],
 'GL_C4F_N3F_V3F': ['InterleavedArrayFormat'],
 'GL_C4UB_V2F': ['InterleavedArrayFormat'],
 'GL_C4UB_V3F': ['InterleavedArrayFormat'],
 'GL_CCW': ['FrontFaceDirection'],
 'GL_CLAMP': ['TextureWrapMode'],
 'GL_CLAMP_FRAGMENT_COLOR_ARB': ['ClampColorTargetARB'],
 'GL_CLAMP_READ_COLOR': ['ClampColorTargetARB'],
 'GL_CLAMP_READ_COLOR_ARB': ['ClampColorTargetARB'],
 'GL_CLAMP_TO_BORDER': ['TextureWrapMode'],
 'GL_CLAMP_TO_BORDER_ARB': ['TextureWrapMode'],
 'GL_CLAMP_TO_EDGE': ['TextureWrapMode'],
 'GL_CLAMP_VERTEX_COLOR_ARB': ['ClampColorTargetARB'],
 'GL_CLEAR': ['LogicOp'],
 'GL_CLEAR_BUFFER': ['InternalFormatPName'],
 'GL_CLEAR_TEXTURE': ['InternalFormatPName'],
 'GL_CLIENT_ALL_ATTRIB_BITS': ['ClientAttribMask'],
 'GL_CLIENT_ATTRIB_STACK_DEPTH': ['GetPName'],
 'GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_CLIENT_PIXEL_STORE_BIT': ['ClientAttribMask'],
 'GL_CLIENT_STORAGE_BIT': ['BufferStorageMask'],
 'GL_CLIENT_STORAGE_BIT_EXT': ['BufferStorageMask'],
 'GL_CLIENT_VERTEX_ARRAY_BIT': ['ClientAttribMask'],
 'GL_CLIP_DISTANCE0': ['ClipPlaneName', 'EnableCap'],
 'GL_CLIP_DISTANCE1': ['ClipPlaneName', 'EnableCap'],
 'GL_CLIP_DISTANCE2': ['ClipPlaneName', 'EnableCap'],
 'GL_CLIP_DISTANCE3': ['ClipPlaneName', 'EnableCap'],
 'GL_CLIP_DISTANCE4': ['ClipPlaneName', 'EnableCap'],
 'GL_CLIP_DISTANCE5': ['ClipPlaneName', 'EnableCap'],
 'GL_CLIP_DISTANCE6': ['ClipPlaneName', 'EnableCap'],
 'GL_CLIP_DISTANCE7': ['ClipPlaneName', 'EnableCap'],
 'GL_CLIP_PLANE0': ['ClipPlaneName', 'EnableCap', 'GetPName'],
 'GL_CLIP_PLANE1': ['ClipPlaneName', 'EnableCap', 'GetPName'],
 'GL_CLIP_PLANE2': ['ClipPlaneName', 'EnableCap', 'GetPName'],
 'GL_CLIP_PLANE3': ['ClipPlaneName', 'EnableCap', 'GetPName'],
 'GL_CLIP_PLANE4': ['ClipPlaneName', 'EnableCap', 'GetPName'],
 'GL_CLIP_PLANE5': ['ClipPlaneName', 'EnableCap', 'GetPName'],
 'GL_CLIP_VOLUME_CLIPPING_HINT_EXT': ['HintTarget'],
 'GL_CMYKA_EXT': ['PixelFormat'],
 'GL_CMYK_EXT': ['PixelFormat'],
 'GL_COEFF': ['GetMapQuery', 'MapQuery'],
 'GL_COLOR': ['PixelCopyType', 'InvalidateFramebufferAttachment', 'Buffer'],
 'GL_COLOR_ARRAY': ['EnableCap', 'GetPName'],
 'GL_COLOR_ARRAY_COUNT_EXT': ['GetPName'],
 'GL_COLOR_ARRAY_POINTER': ['GetPointervPName'],
 'GL_COLOR_ARRAY_POINTER_EXT': ['GetPointervPName'],
 'GL_COLOR_ARRAY_SIZE': ['GetPName'],
 'GL_COLOR_ARRAY_STRIDE': ['GetPName'],
 'GL_COLOR_ARRAY_TYPE': ['GetPName'],
 'GL_COLOR_ATTACHMENT0': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT0_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT1': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT10': ['DrawBufferMode',
                           'ReadBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT10_EXT': ['FramebufferAttachment',
                               'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT11': ['DrawBufferMode',
                           'ReadBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT11_EXT': ['FramebufferAttachment',
                               'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT12': ['DrawBufferMode',
                           'ReadBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT12_EXT': ['FramebufferAttachment',
                               'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT13': ['DrawBufferMode',
                           'ReadBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT13_EXT': ['FramebufferAttachment',
                               'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT14': ['DrawBufferMode',
                           'ReadBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT14_EXT': ['FramebufferAttachment',
                               'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT15': ['DrawBufferMode',
                           'ReadBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT15_EXT': ['FramebufferAttachment',
                               'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT16': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT17': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT18': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT19': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT1_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT2': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT20': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT21': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT22': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT23': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT24': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT25': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT26': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT27': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT28': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT29': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT2_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT3': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT30': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT31': ['DrawBufferMode',
                           'FramebufferAttachment',
                           'InvalidateFramebufferAttachment',
                           'ColorBuffer'],
 'GL_COLOR_ATTACHMENT3_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT4': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT4_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT5': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT5_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT6': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT6_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT7': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT7_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT8': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT8_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_ATTACHMENT9': ['DrawBufferMode',
                          'ReadBufferMode',
                          'FramebufferAttachment',
                          'InvalidateFramebufferAttachment',
                          'ColorBuffer'],
 'GL_COLOR_ATTACHMENT9_EXT': ['FramebufferAttachment',
                              'InvalidateFramebufferAttachment'],
 'GL_COLOR_BUFFER_BIT': ['AttribMask', 'ClearBufferMask'],
 'GL_COLOR_CLEAR_VALUE': ['GetPName'],
 'GL_COLOR_COMPONENTS': ['InternalFormatPName'],
 'GL_COLOR_ENCODING': ['InternalFormatPName'],
 'GL_COLOR_EXT': ['PixelCopyType'],
 'GL_COLOR_INDEX': ['PixelFormat'],
 'GL_COLOR_INDEXES': ['MaterialParameter'],
 'GL_COLOR_LOGIC_OP': ['EnableCap', 'GetPName'],
 'GL_COLOR_MATERIAL': ['EnableCap', 'GetPName'],
 'GL_COLOR_MATERIAL_FACE': ['GetPName'],
 'GL_COLOR_MATERIAL_PARAMETER': ['GetPName'],
 'GL_COLOR_RENDERABLE': ['InternalFormatPName'],
 'GL_COLOR_TABLE': ['ColorTableTargetSGI', 'ColorTableTarget'],
 'GL_COLOR_TABLE_ALPHA_SIZE': ['GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_BIAS': ['ColorTableParameterPNameSGI',
                         'GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_BLUE_SIZE': ['GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_FORMAT': ['GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_GREEN_SIZE': ['GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_INTENSITY_SIZE': ['GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_LUMINANCE_SIZE': ['GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_RED_SIZE': ['GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_SCALE': ['ColorTableParameterPNameSGI',
                          'GetColorTableParameterPNameSGI'],
 'GL_COLOR_TABLE_WIDTH': ['GetColorTableParameterPNameSGI'],
 'GL_COLOR_WRITEMASK': ['GetPName'],
 'GL_COMMAND_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_COMMAND_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_COMPARE_REF_TO_TEXTURE': ['TextureCompareMode'],
 'GL_COMPARE_R_TO_TEXTURE': ['TextureCompareMode'],
 'GL_COMPATIBLE_SUBROUTINES': ['SubroutineParameterName',
                               'ProgramResourceProperty'],
 'GL_COMPILE': ['ListMode'],
 'GL_COMPILE_AND_EXECUTE': ['ListMode'],
 'GL_COMPILE_STATUS': ['ShaderParameterName'],
 'GL_COMPRESSED_R11_EAC': ['InternalFormat'],
 'GL_COMPRESSED_RED': ['InternalFormat'],
 'GL_COMPRESSED_RED_RGTC1': ['InternalFormat'],
 'GL_COMPRESSED_RED_RGTC1_EXT': ['InternalFormat'],
 'GL_COMPRESSED_RG': ['InternalFormat'],
 'GL_COMPRESSED_RG11_EAC': ['InternalFormat'],
 'GL_COMPRESSED_RGB': ['InternalFormat'],
 'GL_COMPRESSED_RGB8_ETC2': ['InternalFormat'],
 'GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2': ['InternalFormat'],
 'GL_COMPRESSED_RGBA': ['InternalFormat'],
 'GL_COMPRESSED_RGBA8_ETC2_EAC': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_10x10': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_10x5': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_10x6': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_10x8': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_12x10': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_12x12': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_4x4': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_5x4': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_5x5': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_6x5': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_6x6': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_8x5': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_8x6': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_ASTC_8x8': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_BPTC_UNORM': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_S3TC_DXT1_EXT': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_S3TC_DXT3_EXT': ['InternalFormat'],
 'GL_COMPRESSED_RGBA_S3TC_DXT5_EXT': ['InternalFormat'],
 'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT': ['InternalFormat'],
 'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT': ['InternalFormat'],
 'GL_COMPRESSED_RGB_S3TC_DXT1_EXT': ['InternalFormat'],
 'GL_COMPRESSED_RG_RGTC2': ['InternalFormat'],
 'GL_COMPRESSED_SIGNED_R11_EAC': ['InternalFormat'],
 'GL_COMPRESSED_SIGNED_RED_RGTC1': ['InternalFormat'],
 'GL_COMPRESSED_SIGNED_RED_RGTC1_EXT': ['InternalFormat'],
 'GL_COMPRESSED_SIGNED_RG11_EAC': ['InternalFormat'],
 'GL_COMPRESSED_SIGNED_RG_RGTC2': ['InternalFormat'],
 'GL_COMPRESSED_SRGB': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_ETC2': ['InternalFormat'],
 'GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2': ['InternalFormat'],
 'GL_COMPRESSED_SRGB_ALPHA': ['InternalFormat'],
 'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM': ['InternalFormat'],
 'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT': ['InternalFormat'],
 'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT': ['InternalFormat'],
 'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT': ['InternalFormat'],
 'GL_COMPRESSED_SRGB_S3TC_DXT1_EXT': ['InternalFormat'],
 'GL_COMPRESSED_TEXTURE_FORMATS': ['GetPName'],
 'GL_COMPUTE_SHADER': ['ShaderType'],
 'GL_COMPUTE_SHADER_BIT': ['UseProgramStageMask'],
 'GL_COMPUTE_SUBROUTINE': ['ProgramInterface'],
 'GL_COMPUTE_SUBROUTINE_UNIFORM': ['ProgramInterface'],
 'GL_COMPUTE_TEXTURE': ['InternalFormatPName'],
 'GL_COMPUTE_WORK_GROUP_SIZE': ['ProgramPropertyARB'],
 'GL_CONDITION_SATISFIED': ['SyncStatus'],
 'GL_CONSTANT': ['PathGenMode'],
 'GL_CONSTANT_ALPHA': ['BlendingFactor'],
 'GL_CONSTANT_ATTENUATION': ['LightParameter'],
 'GL_CONSTANT_COLOR': ['BlendingFactor'],
 'GL_CONTEXT_COMPATIBILITY_PROFILE_BIT': ['ContextProfileMask'],
 'GL_CONTEXT_CORE_PROFILE_BIT': ['ContextProfileMask'],
 'GL_CONTEXT_FLAGS': ['GetPName'],
 'GL_CONTEXT_FLAG_DEBUG_BIT': ['ContextFlagMask'],
 'GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT': ['ContextFlagMask'],
 'GL_CONTEXT_FLAG_NO_ERROR_BIT': ['ContextFlagMask'],
 'GL_CONTEXT_FLAG_PROTECTED_CONTENT_BIT_EXT': ['ContextFlagMask'],
 'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT': ['ContextFlagMask'],
 'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB': ['ContextFlagMask'],
 'GL_CONVOLUTION_1D': ['ConvolutionTargetEXT', 'ConvolutionTarget'],
 'GL_CONVOLUTION_1D_EXT': ['ConvolutionTargetEXT', 'EnableCap', 'GetPName'],
 'GL_CONVOLUTION_2D': ['ConvolutionTargetEXT', 'ConvolutionTarget'],
 'GL_CONVOLUTION_2D_EXT': ['ConvolutionTargetEXT', 'EnableCap', 'GetPName'],
 'GL_CONVOLUTION_BORDER_COLOR': ['GetConvolutionParameter'],
 'GL_CONVOLUTION_BORDER_MODE': ['ConvolutionParameterEXT',
                                'GetConvolutionParameter'],
 'GL_CONVOLUTION_BORDER_MODE_EXT': ['ConvolutionParameterEXT',
                                    'GetConvolutionParameter'],
 'GL_CONVOLUTION_FILTER_BIAS': ['ConvolutionParameterEXT',
                                'GetConvolutionParameter'],
 'GL_CONVOLUTION_FILTER_BIAS_EXT': ['ConvolutionParameterEXT',
                                    'GetConvolutionParameter'],
 'GL_CONVOLUTION_FILTER_SCALE': ['ConvolutionParameterEXT',
                                 'GetConvolutionParameter'],
 'GL_CONVOLUTION_FILTER_SCALE_EXT': ['ConvolutionParameterEXT',
                                     'GetConvolutionParameter'],
 'GL_CONVOLUTION_FORMAT': ['GetConvolutionParameter'],
 'GL_CONVOLUTION_FORMAT_EXT': ['GetConvolutionParameter'],
 'GL_CONVOLUTION_HEIGHT': ['GetConvolutionParameter'],
 'GL_CONVOLUTION_HEIGHT_EXT': ['GetConvolutionParameter'],
 'GL_CONVOLUTION_WIDTH': ['GetConvolutionParameter'],
 'GL_CONVOLUTION_WIDTH_EXT': ['GetConvolutionParameter'],
 'GL_COPY': ['LogicOp'],
 'GL_COPY_INVERTED': ['LogicOp'],
 'GL_COPY_PIXEL_TOKEN': ['FeedBackToken'],
 'GL_COPY_READ_BUFFER': ['BufferTargetARB',
                         'BufferStorageTarget',
                         'CopyBufferSubDataTarget'],
 'GL_COPY_WRITE_BUFFER': ['BufferTargetARB',
                          'BufferStorageTarget',
                          'CopyBufferSubDataTarget'],
 'GL_CULL_FACE': ['EnableCap', 'GetPName'],
 'GL_CULL_FACE_MODE': ['GetPName'],
 'GL_CULL_VERTEX_EYE_POSITION_EXT': ['CullParameterEXT'],
 'GL_CULL_VERTEX_OBJECT_POSITION_EXT': ['CullParameterEXT'],
 'GL_CURRENT_BIT': ['AttribMask'],
 'GL_CURRENT_COLOR': ['GetPName'],
 'GL_CURRENT_INDEX': ['GetPName'],
 'GL_CURRENT_NORMAL': ['GetPName'],
 'GL_CURRENT_PROGRAM': ['GetPName'],
 'GL_CURRENT_QUERY': ['QueryParameterName'],
 'GL_CURRENT_RASTER_COLOR': ['GetPName'],
 'GL_CURRENT_RASTER_DISTANCE': ['GetPName'],
 'GL_CURRENT_RASTER_INDEX': ['GetPName'],
 'GL_CURRENT_RASTER_POSITION': ['GetPName'],
 'GL_CURRENT_RASTER_POSITION_VALID': ['GetPName'],
 'GL_CURRENT_RASTER_TEXTURE_COORDS': ['GetPName'],
 'GL_CURRENT_TEXTURE_COORDS': ['VertexShaderTextureUnitParameter', 'GetPName'],
 'GL_CURRENT_VERTEX_ATTRIB': ['VertexAttribPropertyARB', 'VertexAttribEnum'],
 'GL_CURRENT_VERTEX_EXT': ['VertexShaderParameterEXT'],
 'GL_CW': ['FrontFaceDirection'],
 'GL_D3D12_FENCE_VALUE_EXT': ['SemaphoreParameterName'],
 'GL_DEBUG_CALLBACK_FUNCTION': ['GetPointervPName'],
 'GL_DEBUG_CALLBACK_USER_PARAM': ['GetPointervPName'],
 'GL_DEBUG_GROUP_STACK_DEPTH': ['GetPName'],
 'GL_DEBUG_OUTPUT': ['EnableCap'],
 'GL_DEBUG_OUTPUT_SYNCHRONOUS': ['EnableCap'],
 'GL_DEBUG_SEVERITY_HIGH': ['DebugSeverity'],
 'GL_DEBUG_SEVERITY_LOW': ['DebugSeverity'],
 'GL_DEBUG_SEVERITY_MEDIUM': ['DebugSeverity'],
 'GL_DEBUG_SEVERITY_NOTIFICATION': ['DebugSeverity'],
 'GL_DEBUG_SOURCE_API': ['DebugSource'],
 'GL_DEBUG_SOURCE_APPLICATION': ['DebugSource'],
 'GL_DEBUG_SOURCE_OTHER': ['DebugSource'],
 'GL_DEBUG_SOURCE_SHADER_COMPILER': ['DebugSource'],
 'GL_DEBUG_SOURCE_THIRD_PARTY': ['DebugSource'],
 'GL_DEBUG_SOURCE_WINDOW_SYSTEM': ['DebugSource'],
 'GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR': ['DebugType'],
 'GL_DEBUG_TYPE_ERROR': ['DebugType'],
 'GL_DEBUG_TYPE_MARKER': ['DebugType'],
 'GL_DEBUG_TYPE_OTHER': ['DebugType'],
 'GL_DEBUG_TYPE_PERFORMANCE': ['DebugType'],
 'GL_DEBUG_TYPE_POP_GROUP': ['DebugType'],
 'GL_DEBUG_TYPE_PORTABILITY': ['DebugType'],
 'GL_DEBUG_TYPE_PUSH_GROUP': ['DebugType'],
 'GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR': ['DebugType'],
 'GL_DECAL': ['TextureEnvMode'],
 'GL_DECR': ['StencilOp'],
 'GL_DECR_WRAP': ['StencilOp'],
 'GL_DEDICATED_MEMORY_OBJECT_EXT': ['MemoryObjectParameterName'],
 'GL_DELETE_STATUS': ['ShaderParameterName', 'ProgramPropertyARB'],
 'GL_DEPTH': ['PixelCopyType', 'InvalidateFramebufferAttachment', 'Buffer'],
 'GL_DEPTH24_STENCIL8': ['InternalFormat'],
 'GL_DEPTH24_STENCIL8_EXT': ['InternalFormat'],
 'GL_DEPTH32F_STENCIL8': ['InternalFormat'],
 'GL_DEPTH_ATTACHMENT': ['FramebufferAttachment',
                         'InvalidateFramebufferAttachment'],
 'GL_DEPTH_ATTACHMENT_EXT': ['FramebufferAttachment',
                             'InvalidateFramebufferAttachment'],
 'GL_DEPTH_BIAS': ['GetPName', 'PixelTransferParameter'],
 'GL_DEPTH_BITS': ['GetPName'],
 'GL_DEPTH_BUFFER_BIT': ['AttribMask', 'ClearBufferMask'],
 'GL_DEPTH_CLAMP': ['EnableCap'],
 'GL_DEPTH_CLEAR_VALUE': ['GetPName'],
 'GL_DEPTH_COMPONENT': ['PixelFormat', 'InternalFormat'],
 'GL_DEPTH_COMPONENT16': ['InternalFormat'],
 'GL_DEPTH_COMPONENT16_ARB': ['InternalFormat'],
 'GL_DEPTH_COMPONENT24_ARB': ['InternalFormat'],
 'GL_DEPTH_COMPONENT32F': ['InternalFormat'],
 'GL_DEPTH_COMPONENT32_ARB': ['InternalFormat'],
 'GL_DEPTH_EXT': ['PixelCopyType'],
 'GL_DEPTH_FUNC': ['GetPName'],
 'GL_DEPTH_RANGE': ['GetPName'],
 'GL_DEPTH_RENDERABLE': ['InternalFormatPName'],
 'GL_DEPTH_SCALE': ['GetPName', 'PixelTransferParameter'],
 'GL_DEPTH_STENCIL': ['PixelFormat', 'InternalFormat'],
 'GL_DEPTH_STENCIL_ATTACHMENT': ['FramebufferAttachment',
                                 'InvalidateFramebufferAttachment'],
 'GL_DEPTH_STENCIL_EXT': ['InternalFormat'],
 'GL_DEPTH_STENCIL_TEXTURE_MODE': ['TextureParameterName'],
 'GL_DEPTH_TEST': ['EnableCap', 'GetPName'],
 'GL_DEPTH_WRITEMASK': ['GetPName'],
 'GL_DEVICE_LUID_EXT': ['GetPName'],
 'GL_DEVICE_NODE_MASK_EXT': ['GetPName'],
 'GL_DEVICE_UUID_EXT': ['GetPName'],
 'GL_DIFFUSE': ['ColorMaterialParameter',
                'LightParameter',
                'MaterialParameter'],
 'GL_DISPATCH_INDIRECT_BUFFER': ['BufferTargetARB',
                                 'BufferStorageTarget',
                                 'CopyBufferSubDataTarget'],
 'GL_DISPATCH_INDIRECT_BUFFER_BINDING': ['GetPName'],
 'GL_DISTANCE_ATTENUATION_EXT': ['PointParameterNameSGIS'],
 'GL_DITHER': ['EnableCap', 'GetPName'],
 'GL_DOMAIN': ['GetMapQuery', 'MapQuery'],
 'GL_DONT_CARE': ['HintMode', 'DebugSource', 'DebugType', 'DebugSeverity'],
 'GL_DOUBLE': ['ColorPointerType',
               'FogCoordinatePointerType',
               'FogPointerTypeEXT',
               'FogPointerTypeIBM',
               'IndexPointerType',
               'NormalPointerType',
               'TexCoordPointerType',
               'VertexPointerType',
               'VertexAttribType',
               'UniformType',
               'VertexAttribPointerType',
               'GlslTypeToken',
               'VertexAttribLType'],
 'GL_DOUBLEBUFFER': ['GetPName', 'GetFramebufferParameter'],
 'GL_DOUBLE_ARB': ['WeightPointerTypeARB'],
 'GL_DOUBLE_EXT': ['TangentPointerTypeEXT', 'BinormalPointerTypeEXT'],
 'GL_DOUBLE_MAT2': ['UniformType', 'GlslTypeToken'],
 'GL_DOUBLE_MAT2x3': ['UniformType'],
 'GL_DOUBLE_MAT2x4': ['UniformType'],
 'GL_DOUBLE_MAT3': ['UniformType', 'GlslTypeToken'],
 'GL_DOUBLE_MAT3x2': ['UniformType'],
 'GL_DOUBLE_MAT3x4': ['UniformType'],
 'GL_DOUBLE_MAT4': ['UniformType', 'GlslTypeToken'],
 'GL_DOUBLE_MAT4x2': ['UniformType'],
 'GL_DOUBLE_MAT4x3': ['UniformType'],
 'GL_DOUBLE_VEC2': ['UniformType', 'GlslTypeToken'],
 'GL_DOUBLE_VEC3': ['UniformType', 'GlslTypeToken'],
 'GL_DOUBLE_VEC4': ['UniformType', 'GlslTypeToken'],
 'GL_DRAW_BUFFER': ['GetPName'],
 'GL_DRAW_BUFFER_EXT': ['GetPName'],
 'GL_DRAW_FRAMEBUFFER': ['FramebufferTarget', 'CheckFramebufferStatusTarget'],
 'GL_DRAW_FRAMEBUFFER_BINDING': ['GetPName'],
 'GL_DRAW_INDIRECT_BUFFER': ['BufferTargetARB',
                             'BufferStorageTarget',
                             'CopyBufferSubDataTarget'],
 'GL_DRAW_PIXEL_TOKEN': ['FeedBackToken'],
 'GL_DRIVER_UUID_EXT': ['GetPName'],
 'GL_DST_ALPHA': ['BlendingFactor'],
 'GL_DST_COLOR': ['BlendingFactor'],
 'GL_DYNAMIC_COPY': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_DYNAMIC_DRAW': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_DYNAMIC_READ': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_DYNAMIC_STORAGE_BIT': ['BufferStorageMask'],
 'GL_DYNAMIC_STORAGE_BIT_EXT': ['BufferStorageMask'],
 'GL_EDGE_FLAG': ['GetPName'],
 'GL_EDGE_FLAG_ARRAY': ['EnableCap', 'GetPName'],
 'GL_EDGE_FLAG_ARRAY_COUNT_EXT': ['GetPName'],
 'GL_EDGE_FLAG_ARRAY_POINTER': ['GetPointervPName'],
 'GL_EDGE_FLAG_ARRAY_POINTER_EXT': ['GetPointervPName'],
 'GL_EDGE_FLAG_ARRAY_STRIDE': ['GetPName'],
 'GL_ELEMENT_ARRAY_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_ELEMENT_ARRAY_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_ELEMENT_ARRAY_BUFFER': ['BufferTargetARB',
                             'BufferStorageTarget',
                             'CopyBufferSubDataTarget'],
 'GL_ELEMENT_ARRAY_BUFFER_BINDING': ['GetPName'],
 'GL_EMISSION': ['ColorMaterialParameter', 'MaterialParameter'],
 'GL_ENABLE_BIT': ['AttribMask'],
 'GL_EQUAL': ['AlphaFunction', 'DepthFunction', 'StencilFunction'],
 'GL_EQUAL_EXT': ['IndexFunctionEXT'],
 'GL_EQUIV': ['LogicOp'],
 'GL_EVAL_BIT': ['AttribMask'],
 'GL_EXP': ['FogMode'],
 'GL_EXP2': ['FogMode'],
 'GL_EXTENSIONS': ['StringName'],
 'GL_EYE_LINEAR': ['TextureGenMode', 'PathGenMode'],
 'GL_EYE_PLANE': ['TextureGenParameter'],
 'GL_FALSE': ['ClampColorModeARB', 'ClampColorModeARB', 'Boolean'],
 'GL_FALSE_EXT': ['VertexShaderWriteMaskEXT'],
 'GL_FASTEST': ['HintMode'],
 'GL_FEEDBACK': ['RenderingMode'],
 'GL_FEEDBACK_BUFFER_POINTER': ['GetPointervPName'],
 'GL_FEEDBACK_BUFFER_SIZE': ['GetPName'],
 'GL_FEEDBACK_BUFFER_TYPE': ['GetPName'],
 'GL_FILL': ['MeshMode2', 'PolygonMode'],
 'GL_FILTER': ['InternalFormatPName'],
 'GL_FIRST_VERTEX_CONVENTION': ['VertexProvokingMode'],
 'GL_FIXED': ['VertexAttribType', 'VertexAttribPointerType'],
 'GL_FIXED_ONLY': ['ClampColorModeARB'],
 'GL_FIXED_ONLY_ARB': ['ClampColorModeARB'],
 'GL_FLAT': ['ShadingModel'],
 'GL_FLOAT': ['ColorPointerType',
              'FogCoordinatePointerType',
              'FogPointerTypeEXT',
              'FogPointerTypeIBM',
              'IndexPointerType',
              'ListNameType',
              'NormalPointerType',
              'PixelType',
              'TexCoordPointerType',
              'VertexPointerType',
              'VertexAttribType',
              'UniformType',
              'VertexAttribPointerType',
              'GlslTypeToken'],
 'GL_FLOAT_ARB': ['WeightPointerTypeARB'],
 'GL_FLOAT_EXT': ['VertexWeightPointerTypeEXT',
                  'TangentPointerTypeEXT',
                  'BinormalPointerTypeEXT'],
 'GL_FLOAT_MAT2': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_FLOAT_MAT2X3': ['UniformType'],
 'GL_FLOAT_MAT2X4': ['UniformType'],
 'GL_FLOAT_MAT2_ARB': ['AttributeType'],
 'GL_FLOAT_MAT2x3': ['AttributeType', 'GlslTypeToken'],
 'GL_FLOAT_MAT2x4': ['AttributeType', 'GlslTypeToken'],
 'GL_FLOAT_MAT3': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_FLOAT_MAT3X2': ['UniformType'],
 'GL_FLOAT_MAT3X4': ['UniformType'],
 'GL_FLOAT_MAT3_ARB': ['AttributeType'],
 'GL_FLOAT_MAT3x2': ['AttributeType', 'GlslTypeToken'],
 'GL_FLOAT_MAT3x4': ['AttributeType', 'GlslTypeToken'],
 'GL_FLOAT_MAT4': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_FLOAT_MAT4X2': ['UniformType'],
 'GL_FLOAT_MAT4X3': ['UniformType'],
 'GL_FLOAT_MAT4_ARB': ['AttributeType'],
 'GL_FLOAT_MAT4x2': ['AttributeType', 'GlslTypeToken'],
 'GL_FLOAT_MAT4x3': ['AttributeType', 'GlslTypeToken'],
 'GL_FLOAT_VEC2': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_FLOAT_VEC2_ARB': ['AttributeType'],
 'GL_FLOAT_VEC3': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_FLOAT_VEC3_ARB': ['AttributeType'],
 'GL_FLOAT_VEC4': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_FLOAT_VEC4_ARB': ['AttributeType'],
 'GL_FOG': ['EnableCap', 'GetPName'],
 'GL_FOG_BIT': ['AttribMask'],
 'GL_FOG_COLOR': ['FogParameter', 'GetPName'],
 'GL_FOG_COORD_SRC': ['FogPName'],
 'GL_FOG_DENSITY': ['FogParameter', 'GetPName', 'FogPName'],
 'GL_FOG_END': ['FogParameter', 'GetPName', 'FogPName'],
 'GL_FOG_HINT': ['GetPName', 'HintTarget'],
 'GL_FOG_INDEX': ['FogParameter', 'GetPName', 'FogPName'],
 'GL_FOG_MODE': ['FogParameter', 'GetPName', 'FogPName'],
 'GL_FOG_START': ['FogParameter', 'GetPName', 'FogPName'],
 'GL_FRAGMENT_COLOR_EXT': ['LightTextureModeEXT'],
 'GL_FRAGMENT_DEPTH_EXT': ['LightTextureModeEXT'],
 'GL_FRAGMENT_MATERIAL_EXT': ['LightTextureModeEXT'],
 'GL_FRAGMENT_NORMAL_EXT': ['LightTextureModeEXT'],
 'GL_FRAGMENT_SHADER': ['ShaderType', 'PipelineParameterName'],
 'GL_FRAGMENT_SHADER_ARB': ['ShaderType'],
 'GL_FRAGMENT_SHADER_BIT': ['UseProgramStageMask'],
 'GL_FRAGMENT_SHADER_BIT_EXT': ['UseProgramStageMask'],
 'GL_FRAGMENT_SHADER_DERIVATIVE_HINT': ['GetPName', 'HintTarget'],
 'GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB': ['HintTarget'],
 'GL_FRAGMENT_SUBROUTINE': ['ProgramInterface'],
 'GL_FRAGMENT_SUBROUTINE_UNIFORM': ['ProgramInterface'],
 'GL_FRAGMENT_TEXTURE': ['InternalFormatPName'],
 'GL_FRAMEBUFFER': ['FramebufferTarget',
                    'CheckFramebufferStatusTarget',
                    'ObjectIdentifier'],
 'GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_LAYERED': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SCALE_IMG': ['FramebufferAttachmentParameterName'],
 'GL_FRAMEBUFFER_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_FRAMEBUFFER_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_FRAMEBUFFER_BLEND': ['InternalFormatPName'],
 'GL_FRAMEBUFFER_COMPLETE': ['FramebufferStatus'],
 'GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS': ['FramebufferParameterName',
                                                   'GetFramebufferParameter'],
 'GL_FRAMEBUFFER_DEFAULT_HEIGHT': ['FramebufferParameterName',
                                   'GetFramebufferParameter'],
 'GL_FRAMEBUFFER_DEFAULT_LAYERS': ['FramebufferParameterName',
                                   'GetFramebufferParameter'],
 'GL_FRAMEBUFFER_DEFAULT_SAMPLES': ['FramebufferParameterName',
                                    'GetFramebufferParameter'],
 'GL_FRAMEBUFFER_DEFAULT_WIDTH': ['FramebufferParameterName',
                                  'GetFramebufferParameter'],
 'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT': ['FramebufferStatus'],
 'GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER': ['FramebufferStatus'],
 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS': ['FramebufferStatus'],
 'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT': ['FramebufferStatus'],
 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE': ['FramebufferStatus',
                                           'FramebufferStatus'],
 'GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER': ['FramebufferStatus'],
 'GL_FRAMEBUFFER_RENDERABLE': ['InternalFormatPName'],
 'GL_FRAMEBUFFER_RENDERABLE_LAYERED': ['InternalFormatPName'],
 'GL_FRAMEBUFFER_SRGB': ['EnableCap'],
 'GL_FRAMEBUFFER_UNDEFINED': ['FramebufferStatus'],
 'GL_FRAMEBUFFER_UNSUPPORTED': ['FramebufferStatus'],
 'GL_FRONT': ['ColorMaterialFace',
              'CullFaceMode',
              'DrawBufferMode',
              'MaterialFace',
              'ReadBufferMode',
              'StencilFaceDirection',
              'ColorBuffer'],
 'GL_FRONT_AND_BACK': ['ColorMaterialFace',
                       'CullFaceMode',
                       'DrawBufferMode',
                       'MaterialFace',
                       'StencilFaceDirection',
                       'ColorBuffer'],
 'GL_FRONT_FACE': ['GetPName'],
 'GL_FRONT_LEFT': ['DrawBufferMode', 'ReadBufferMode', 'ColorBuffer'],
 'GL_FRONT_RIGHT': ['DrawBufferMode', 'ReadBufferMode', 'ColorBuffer'],
 'GL_FULL_RANGE_EXT': ['ParameterRangeEXT'],
 'GL_FUNC_ADD': ['BlendEquationModeEXT'],
 'GL_FUNC_ADD_EXT': ['BlendEquationModeEXT'],
 'GL_FUNC_REVERSE_SUBTRACT': ['BlendEquationModeEXT'],
 'GL_FUNC_REVERSE_SUBTRACT_EXT': ['BlendEquationModeEXT'],
 'GL_FUNC_SUBTRACT': ['BlendEquationModeEXT'],
 'GL_FUNC_SUBTRACT_EXT': ['BlendEquationModeEXT'],
 'GL_GENERATE_MIPMAP': ['TextureParameterName', 'InternalFormatPName'],
 'GL_GENERATE_MIPMAP_HINT': ['HintTarget'],
 'GL_GEOMETRY_INPUT_TYPE': ['ProgramPropertyARB'],
 'GL_GEOMETRY_OUTPUT_TYPE': ['ProgramPropertyARB'],
 'GL_GEOMETRY_SHADER': ['ShaderType', 'PipelineParameterName'],
 'GL_GEOMETRY_SHADER_BIT': ['UseProgramStageMask'],
 'GL_GEOMETRY_SHADER_BIT_EXT': ['UseProgramStageMask'],
 'GL_GEOMETRY_SUBROUTINE': ['ProgramInterface'],
 'GL_GEOMETRY_SUBROUTINE_UNIFORM': ['ProgramInterface'],
 'GL_GEOMETRY_TEXTURE': ['InternalFormatPName'],
 'GL_GEOMETRY_VERTICES_OUT': ['ProgramPropertyARB'],
 'GL_GEQUAL': ['AlphaFunction', 'DepthFunction', 'StencilFunction'],
 'GL_GEQUAL_EXT': ['IndexFunctionEXT'],
 'GL_GET_TEXTURE_IMAGE_FORMAT': ['InternalFormatPName'],
 'GL_GET_TEXTURE_IMAGE_TYPE': ['InternalFormatPName'],
 'GL_GREATER': ['AlphaFunction', 'DepthFunction', 'StencilFunction'],
 'GL_GREATER_EXT': ['IndexFunctionEXT'],
 'GL_GREEN': ['PixelFormat', 'TextureSwizzle'],
 'GL_GREEN_BIAS': ['GetPName', 'PixelTransferParameter'],
 'GL_GREEN_BITS': ['GetPName'],
 'GL_GREEN_INTEGER': ['PixelFormat'],
 'GL_GREEN_SCALE': ['GetPName', 'PixelTransferParameter'],
 'GL_GUILTY_CONTEXT_RESET': ['GraphicsResetStatus'],
 'GL_HALF_FLOAT': ['VertexAttribType', 'VertexAttribPointerType'],
 'GL_HANDLE_TYPE_D3D11_IMAGE_EXT': ['ExternalHandleType'],
 'GL_HANDLE_TYPE_D3D11_IMAGE_KMT_EXT': ['ExternalHandleType'],
 'GL_HANDLE_TYPE_D3D12_FENCE_EXT': ['ExternalHandleType'],
 'GL_HANDLE_TYPE_D3D12_RESOURCE_EXT': ['ExternalHandleType'],
 'GL_HANDLE_TYPE_D3D12_TILEPOOL_EXT': ['ExternalHandleType'],
 'GL_HANDLE_TYPE_OPAQUE_FD_EXT': ['ExternalHandleType'],
 'GL_HANDLE_TYPE_OPAQUE_WIN32_EXT': ['ExternalHandleType'],
 'GL_HANDLE_TYPE_OPAQUE_WIN32_KMT_EXT': ['ExternalHandleType'],
 'GL_HIGH_FLOAT': ['PrecisionType'],
 'GL_HIGH_INT': ['PrecisionType'],
 'GL_HINT_BIT': ['AttribMask'],
 'GL_HISTOGRAM': ['HistogramTargetEXT'],
 'GL_HISTOGRAM_ALPHA_SIZE': ['GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_ALPHA_SIZE_EXT': ['GetHistogramParameterPNameEXT',
                                 'GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_BLUE_SIZE': ['GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_BLUE_SIZE_EXT': ['GetHistogramParameterPNameEXT',
                                'GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_EXT': ['EnableCap', 'GetPName', 'HistogramTargetEXT'],
 'GL_HISTOGRAM_FORMAT': ['GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_FORMAT_EXT': ['GetHistogramParameterPNameEXT',
                             'GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_GREEN_SIZE': ['GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_GREEN_SIZE_EXT': ['GetHistogramParameterPNameEXT',
                                 'GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_LUMINANCE_SIZE': ['GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_LUMINANCE_SIZE_EXT': ['GetHistogramParameterPNameEXT',
                                     'GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_RED_SIZE': ['GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_RED_SIZE_EXT': ['GetHistogramParameterPNameEXT',
                               'GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_SINK': ['GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_SINK_EXT': ['GetHistogramParameterPNameEXT',
                           'GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_WIDTH': ['GetHistogramParameterPNameEXT'],
 'GL_HISTOGRAM_WIDTH_EXT': ['GetHistogramParameterPNameEXT',
                            'GetHistogramParameterPNameEXT'],
 'GL_IMAGE_1D': ['GlslTypeToken'],
 'GL_IMAGE_1D_ARRAY': ['GlslTypeToken'],
 'GL_IMAGE_2D': ['GlslTypeToken'],
 'GL_IMAGE_2D_ARRAY': ['GlslTypeToken'],
 'GL_IMAGE_2D_MULTISAMPLE': ['GlslTypeToken'],
 'GL_IMAGE_2D_MULTISAMPLE_ARRAY': ['GlslTypeToken'],
 'GL_IMAGE_2D_RECT': ['GlslTypeToken'],
 'GL_IMAGE_3D': ['GlslTypeToken'],
 'GL_IMAGE_BUFFER': ['GlslTypeToken'],
 'GL_IMAGE_COMPATIBILITY_CLASS': ['InternalFormatPName'],
 'GL_IMAGE_CUBE': ['GlslTypeToken'],
 'GL_IMAGE_CUBE_MAP_ARRAY': ['GlslTypeToken'],
 'GL_IMAGE_CUBIC_WEIGHT_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_FORMAT_COMPATIBILITY_TYPE': ['InternalFormatPName'],
 'GL_IMAGE_MAG_FILTER_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_MIN_FILTER_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_PIXEL_FORMAT': ['InternalFormatPName'],
 'GL_IMAGE_PIXEL_TYPE': ['InternalFormatPName'],
 'GL_IMAGE_ROTATE_ANGLE_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_ROTATE_ORIGIN_X_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_ROTATE_ORIGIN_Y_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_SCALE_X_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_SCALE_Y_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_TEXEL_SIZE': ['InternalFormatPName'],
 'GL_IMAGE_TRANSFORM_2D_HP': ['ImageTransformTargetHP'],
 'GL_IMAGE_TRANSLATE_X_HP': ['ImageTransformPNameHP'],
 'GL_IMAGE_TRANSLATE_Y_HP': ['ImageTransformPNameHP'],
 'GL_IMPLEMENTATION_COLOR_READ_FORMAT': ['GetPName', 'GetFramebufferParameter'],
 'GL_IMPLEMENTATION_COLOR_READ_TYPE': ['GetPName', 'GetFramebufferParameter'],
 'GL_INCR': ['StencilOp'],
 'GL_INCR_WRAP': ['StencilOp'],
 'GL_INDEX_ARRAY': ['EnableCap', 'GetPName'],
 'GL_INDEX_ARRAY_COUNT_EXT': ['GetPName'],
 'GL_INDEX_ARRAY_POINTER': ['GetPointervPName'],
 'GL_INDEX_ARRAY_POINTER_EXT': ['GetPointervPName'],
 'GL_INDEX_ARRAY_STRIDE': ['GetPName'],
 'GL_INDEX_ARRAY_TYPE': ['GetPName'],
 'GL_INDEX_BITS': ['GetPName'],
 'GL_INDEX_CLEAR_VALUE': ['GetPName'],
 'GL_INDEX_LOGIC_OP': ['EnableCap', 'GetPName'],
 'GL_INDEX_MODE': ['GetPName'],
 'GL_INDEX_OFFSET': ['IndexMaterialParameterEXT',
                     'GetPName',
                     'PixelTransferParameter'],
 'GL_INDEX_SHIFT': ['GetPName', 'PixelTransferParameter'],
 'GL_INDEX_WRITEMASK': ['GetPName'],
 'GL_INFO_LOG_LENGTH': ['ShaderParameterName',
                        'PipelineParameterName',
                        'ProgramPropertyARB'],
 'GL_INNOCENT_CONTEXT_RESET': ['GraphicsResetStatus'],
 'GL_INT': ['ColorPointerType',
            'IndexPointerType',
            'ListNameType',
            'NormalPointerType',
            'PixelType',
            'TexCoordPointerType',
            'VertexPointerType',
            'VertexAttribType',
            'UniformType',
            'VertexAttribPointerType',
            'GlslTypeToken',
            'VertexAttribIType'],
 'GL_INTENSITY': ['PathColorFormat', 'InternalFormat'],
 'GL_INTENSITY12': ['InternalFormat'],
 'GL_INTENSITY16': ['InternalFormat'],
 'GL_INTENSITY4': ['InternalFormat'],
 'GL_INTENSITY8': ['InternalFormat'],
 'GL_INTERLEAVED_ATTRIBS': ['TransformFeedbackBufferMode'],
 'GL_INTERNALFORMAT_ALPHA_SIZE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_ALPHA_TYPE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_BLUE_SIZE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_BLUE_TYPE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_DEPTH_SIZE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_DEPTH_TYPE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_GREEN_SIZE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_GREEN_TYPE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_PREFERRED': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_RED_SIZE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_RED_TYPE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_SHARED_SIZE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_STENCIL_SIZE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_STENCIL_TYPE': ['InternalFormatPName'],
 'GL_INTERNALFORMAT_SUPPORTED': ['InternalFormatPName'],
 'GL_INT_2_10_10_10_REV': ['VertexAttribType', 'VertexAttribPointerType'],
 'GL_INT_ARB': ['WeightPointerTypeARB'],
 'GL_INT_IMAGE_1D': ['GlslTypeToken'],
 'GL_INT_IMAGE_1D_ARRAY': ['GlslTypeToken'],
 'GL_INT_IMAGE_2D': ['GlslTypeToken'],
 'GL_INT_IMAGE_2D_ARRAY': ['GlslTypeToken'],
 'GL_INT_IMAGE_2D_MULTISAMPLE': ['GlslTypeToken'],
 'GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY': ['GlslTypeToken'],
 'GL_INT_IMAGE_2D_RECT': ['GlslTypeToken'],
 'GL_INT_IMAGE_3D': ['GlslTypeToken'],
 'GL_INT_IMAGE_BUFFER': ['GlslTypeToken'],
 'GL_INT_IMAGE_CUBE': ['GlslTypeToken'],
 'GL_INT_IMAGE_CUBE_MAP_ARRAY': ['GlslTypeToken'],
 'GL_INT_SAMPLER_1D': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_1D_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_2D': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_2D_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_2D_MULTISAMPLE': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_2D_RECT': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_3D': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_BUFFER': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_CUBE': ['UniformType', 'GlslTypeToken'],
 'GL_INT_SAMPLER_CUBE_MAP_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_INT_VEC2': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_INT_VEC2_ARB': ['AttributeType'],
 'GL_INT_VEC3': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_INT_VEC3_ARB': ['AttributeType'],
 'GL_INT_VEC4': ['AttributeType', 'UniformType', 'GlslTypeToken'],
 'GL_INT_VEC4_ARB': ['AttributeType'],
 'GL_INVALID_ENUM': ['ErrorCode'],
 'GL_INVALID_FRAMEBUFFER_OPERATION': ['ErrorCode'],
 'GL_INVALID_FRAMEBUFFER_OPERATION_EXT': ['ErrorCode'],
 'GL_INVALID_OPERATION': ['ErrorCode'],
 'GL_INVALID_VALUE': ['ErrorCode'],
 'GL_INVARIANT_EXT': ['VertexShaderStorageTypeEXT'],
 'GL_INVERT': ['LogicOp', 'StencilOp', 'PathFillMode'],
 'GL_IS_PER_PATCH': ['ProgramResourceProperty'],
 'GL_IS_ROW_MAJOR': ['ProgramResourceProperty'],
 'GL_KEEP': ['StencilOp'],
 'GL_LAST_VERTEX_CONVENTION': ['VertexProvokingMode'],
 'GL_LAYER_PROVOKING_VERTEX': ['GetPName'],
 'GL_LAYOUT_COLOR_ATTACHMENT_EXT': ['TextureLayout'],
 'GL_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_EXT': ['TextureLayout'],
 'GL_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_EXT': ['TextureLayout'],
 'GL_LAYOUT_DEPTH_STENCIL_ATTACHMENT_EXT': ['TextureLayout'],
 'GL_LAYOUT_DEPTH_STENCIL_READ_ONLY_EXT': ['TextureLayout'],
 'GL_LAYOUT_GENERAL_EXT': ['TextureLayout'],
 'GL_LAYOUT_SHADER_READ_ONLY_EXT': ['TextureLayout'],
 'GL_LAYOUT_TRANSFER_DST_EXT': ['TextureLayout'],
 'GL_LAYOUT_TRANSFER_SRC_EXT': ['TextureLayout'],
 'GL_LEFT': ['DrawBufferMode', 'ReadBufferMode', 'ColorBuffer'],
 'GL_LEQUAL': ['AlphaFunction', 'DepthFunction', 'StencilFunction'],
 'GL_LEQUAL_EXT': ['IndexFunctionEXT'],
 'GL_LESS': ['AlphaFunction', 'DepthFunction', 'StencilFunction'],
 'GL_LESS_EXT': ['IndexFunctionEXT'],
 'GL_LGPU_SEPARATE_STORAGE_BIT_NVX': ['BufferStorageMask'],
 'GL_LIGHT0': ['EnableCap', 'GetPName', 'LightName'],
 'GL_LIGHT1': ['EnableCap', 'GetPName', 'LightName'],
 'GL_LIGHT2': ['EnableCap', 'GetPName', 'LightName'],
 'GL_LIGHT3': ['EnableCap', 'GetPName', 'LightName'],
 'GL_LIGHT4': ['EnableCap', 'GetPName', 'LightName'],
 'GL_LIGHT5': ['EnableCap', 'GetPName', 'LightName'],
 'GL_LIGHT6': ['EnableCap', 'GetPName', 'LightName'],
 'GL_LIGHT7': ['EnableCap', 'GetPName', 'LightName'],
 'GL_LIGHTING': ['EnableCap', 'GetPName'],
 'GL_LIGHTING_BIT': ['AttribMask'],
 'GL_LIGHT_MODEL_AMBIENT': ['GetPName', 'LightModelParameter'],
 'GL_LIGHT_MODEL_COLOR_CONTROL': ['GetPName', 'LightModelParameter'],
 'GL_LIGHT_MODEL_COLOR_CONTROL_EXT': ['LightModelParameter'],
 'GL_LIGHT_MODEL_LOCAL_VIEWER': ['GetPName', 'LightModelParameter'],
 'GL_LIGHT_MODEL_TWO_SIDE': ['GetPName', 'LightModelParameter'],
 'GL_LINE': ['MeshMode1', 'MeshMode2', 'PolygonMode'],
 'GL_LINEAR': ['FogMode',
               'TextureMagFilter',
               'TextureMinFilter',
               'BlitFramebufferFilter'],
 'GL_LINEAR_ATTENUATION': ['LightParameter'],
 'GL_LINEAR_MIPMAP_LINEAR': ['TextureMinFilter', 'TextureWrapMode'],
 'GL_LINEAR_MIPMAP_NEAREST': ['TextureMinFilter'],
 'GL_LINES': ['PrimitiveType'],
 'GL_LINES_ADJACENCY': ['PrimitiveType'],
 'GL_LINES_ADJACENCY_ARB': ['PrimitiveType'],
 'GL_LINES_ADJACENCY_EXT': ['PrimitiveType'],
 'GL_LINE_BIT': ['AttribMask'],
 'GL_LINE_LOOP': ['PrimitiveType'],
 'GL_LINE_RESET_TOKEN': ['FeedBackToken'],
 'GL_LINE_SMOOTH': ['EnableCap', 'GetPName'],
 'GL_LINE_SMOOTH_HINT': ['GetPName', 'HintTarget'],
 'GL_LINE_STIPPLE': ['EnableCap', 'GetPName'],
 'GL_LINE_STIPPLE_PATTERN': ['GetPName'],
 'GL_LINE_STIPPLE_REPEAT': ['GetPName'],
 'GL_LINE_STRIP': ['PrimitiveType'],
 'GL_LINE_STRIP_ADJACENCY': ['PrimitiveType'],
 'GL_LINE_STRIP_ADJACENCY_ARB': ['PrimitiveType'],
 'GL_LINE_STRIP_ADJACENCY_EXT': ['PrimitiveType'],
 'GL_LINE_TOKEN': ['FeedBackToken'],
 'GL_LINE_WIDTH': ['GetPName'],
 'GL_LINE_WIDTH_GRANULARITY': ['GetPName'],
 'GL_LINE_WIDTH_RANGE': ['GetPName'],
 'GL_LINK_STATUS': ['ProgramPropertyARB'],
 'GL_LIST_BASE': ['GetPName'],
 'GL_LIST_BIT': ['AttribMask'],
 'GL_LIST_INDEX': ['GetPName'],
 'GL_LIST_MODE': ['GetPName'],
 'GL_LOAD': ['AccumOp'],
 'GL_LOCAL_CONSTANT_EXT': ['VertexShaderStorageTypeEXT'],
 'GL_LOCAL_EXT': ['VertexShaderStorageTypeEXT'],
 'GL_LOCATION': ['ProgramResourceProperty'],
 'GL_LOCATION_COMPONENT': ['ProgramResourceProperty'],
 'GL_LOCATION_INDEX': ['ProgramResourceProperty'],
 'GL_LOGIC_OP': ['GetPName'],
 'GL_LOGIC_OP_MODE': ['GetPName'],
 'GL_LOWER_LEFT': ['ClipControlOrigin'],
 'GL_LOW_FLOAT': ['PrecisionType'],
 'GL_LOW_INT': ['PrecisionType'],
 'GL_LUMINANCE': ['PathColorFormat', 'PixelFormat', 'PixelTexGenMode'],
 'GL_LUMINANCE12': ['InternalFormat'],
 'GL_LUMINANCE12_ALPHA12': ['InternalFormat'],
 'GL_LUMINANCE12_ALPHA4': ['InternalFormat'],
 'GL_LUMINANCE16': ['InternalFormat'],
 'GL_LUMINANCE16_ALPHA16': ['InternalFormat'],
 'GL_LUMINANCE4': ['InternalFormat'],
 'GL_LUMINANCE4_ALPHA4': ['InternalFormat'],
 'GL_LUMINANCE6_ALPHA2': ['InternalFormat'],
 'GL_LUMINANCE8': ['InternalFormat'],
 'GL_LUMINANCE8_ALPHA8': ['InternalFormat'],
 'GL_LUMINANCE_ALPHA': ['PathColorFormat', 'PixelFormat', 'PixelTexGenMode'],
 'GL_MAJOR_VERSION': ['GetPName'],
 'GL_MAP1_COLOR_4': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP1_GRID_DOMAIN': ['GetPName'],
 'GL_MAP1_GRID_SEGMENTS': ['GetPName'],
 'GL_MAP1_INDEX': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP1_NORMAL': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP1_TEXTURE_COORD_1': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP1_TEXTURE_COORD_2': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP1_TEXTURE_COORD_3': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP1_TEXTURE_COORD_4': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP1_VERTEX_3': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP1_VERTEX_4': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_COLOR_4': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_GRID_DOMAIN': ['GetPName'],
 'GL_MAP2_GRID_SEGMENTS': ['GetPName'],
 'GL_MAP2_INDEX': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_NORMAL': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_TEXTURE_COORD_1': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_TEXTURE_COORD_2': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_TEXTURE_COORD_3': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_TEXTURE_COORD_4': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_VERTEX_3': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP2_VERTEX_4': ['EnableCap', 'GetPName', 'MapTarget'],
 'GL_MAP_COHERENT_BIT': ['BufferStorageMask', 'MapBufferAccessMask'],
 'GL_MAP_COHERENT_BIT_EXT': ['BufferStorageMask', 'MapBufferAccessMask'],
 'GL_MAP_COLOR': ['GetPName', 'PixelTransferParameter'],
 'GL_MAP_FLUSH_EXPLICIT_BIT': ['MapBufferAccessMask'],
 'GL_MAP_FLUSH_EXPLICIT_BIT_EXT': ['MapBufferAccessMask'],
 'GL_MAP_INVALIDATE_BUFFER_BIT': ['MapBufferAccessMask'],
 'GL_MAP_INVALIDATE_BUFFER_BIT_EXT': ['MapBufferAccessMask'],
 'GL_MAP_INVALIDATE_RANGE_BIT': ['MapBufferAccessMask'],
 'GL_MAP_INVALIDATE_RANGE_BIT_EXT': ['MapBufferAccessMask'],
 'GL_MAP_PERSISTENT_BIT': ['BufferStorageMask', 'MapBufferAccessMask'],
 'GL_MAP_PERSISTENT_BIT_EXT': ['BufferStorageMask', 'MapBufferAccessMask'],
 'GL_MAP_READ_BIT': ['BufferStorageMask', 'MapBufferAccessMask'],
 'GL_MAP_READ_BIT_EXT': ['BufferStorageMask', 'MapBufferAccessMask'],
 'GL_MAP_STENCIL': ['GetPName', 'PixelTransferParameter'],
 'GL_MAP_UNSYNCHRONIZED_BIT': ['MapBufferAccessMask'],
 'GL_MAP_UNSYNCHRONIZED_BIT_EXT': ['MapBufferAccessMask'],
 'GL_MAP_WRITE_BIT': ['BufferStorageMask', 'MapBufferAccessMask'],
 'GL_MAP_WRITE_BIT_EXT': ['BufferStorageMask', 'MapBufferAccessMask'],
 'GL_MATRIX_EXT': ['DataTypeEXT'],
 'GL_MATRIX_MODE': ['GetPName'],
 'GL_MATRIX_STRIDE': ['ProgramResourceProperty'],
 'GL_MAX': ['BlendEquationModeEXT'],
 'GL_MAX_3D_TEXTURE_SIZE': ['GetPName'],
 'GL_MAX_3D_TEXTURE_SIZE_EXT': ['GetPName'],
 'GL_MAX_ARRAY_TEXTURE_LAYERS': ['GetPName'],
 'GL_MAX_ATTRIB_STACK_DEPTH': ['GetPName'],
 'GL_MAX_CLIENT_ATTRIB_STACK_DEPTH': ['GetPName'],
 'GL_MAX_CLIP_DISTANCES': ['GetPName'],
 'GL_MAX_CLIP_PLANES': ['GetPName'],
 'GL_MAX_COLOR_TEXTURE_SAMPLES': ['GetPName'],
 'GL_MAX_COMBINED_ATOMIC_COUNTERS': ['GetPName'],
 'GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS': ['GetPName'],
 'GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS': ['GetPName'],
 'GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS': ['GetPName'],
 'GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS': ['GetPName'],
 'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS': ['GetPName'],
 'GL_MAX_COMBINED_UNIFORM_BLOCKS': ['GetPName'],
 'GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS': ['GetPName'],
 'GL_MAX_COMPUTE_ATOMIC_COUNTERS': ['GetPName'],
 'GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS': ['GetPName'],
 'GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS': ['GetPName'],
 'GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS': ['GetPName'],
 'GL_MAX_COMPUTE_UNIFORM_BLOCKS': ['GetPName'],
 'GL_MAX_COMPUTE_UNIFORM_COMPONENTS': ['GetPName'],
 'GL_MAX_COMPUTE_WORK_GROUP_COUNT': ['GetPName'],
 'GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS': ['GetPName'],
 'GL_MAX_COMPUTE_WORK_GROUP_SIZE': ['GetPName'],
 'GL_MAX_CONVOLUTION_HEIGHT': ['GetConvolutionParameter'],
 'GL_MAX_CONVOLUTION_HEIGHT_EXT': ['GetConvolutionParameter'],
 'GL_MAX_CONVOLUTION_WIDTH': ['GetConvolutionParameter'],
 'GL_MAX_CONVOLUTION_WIDTH_EXT': ['GetConvolutionParameter'],
 'GL_MAX_CUBE_MAP_TEXTURE_SIZE': ['GetPName'],
 'GL_MAX_DEBUG_GROUP_STACK_DEPTH': ['GetPName'],
 'GL_MAX_DEPTH': ['InternalFormatPName'],
 'GL_MAX_DEPTH_TEXTURE_SAMPLES': ['GetPName'],
 'GL_MAX_DRAW_BUFFERS': ['GetPName'],
 'GL_MAX_DUAL_SOURCE_DRAW_BUFFERS': ['GetPName'],
 'GL_MAX_ELEMENTS_INDICES': ['GetPName'],
 'GL_MAX_ELEMENTS_VERTICES': ['GetPName'],
 'GL_MAX_ELEMENT_INDEX': ['GetPName'],
 'GL_MAX_EVAL_ORDER': ['GetPName'],
 'GL_MAX_EXT': ['BlendEquationModeEXT'],
 'GL_MAX_FRAGMENT_ATOMIC_COUNTERS': ['GetPName'],
 'GL_MAX_FRAGMENT_INPUT_COMPONENTS': ['GetPName'],
 'GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS': ['GetPName'],
 'GL_MAX_FRAGMENT_UNIFORM_BLOCKS': ['GetPName'],
 'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS': ['GetPName'],
 'GL_MAX_FRAGMENT_UNIFORM_VECTORS': ['GetPName'],
 'GL_MAX_FRAMEBUFFER_HEIGHT': ['GetPName'],
 'GL_MAX_FRAMEBUFFER_LAYERS': ['GetPName'],
 'GL_MAX_FRAMEBUFFER_SAMPLES': ['GetPName'],
 'GL_MAX_FRAMEBUFFER_WIDTH': ['GetPName'],
 'GL_MAX_GEOMETRY_ATOMIC_COUNTERS': ['GetPName'],
 'GL_MAX_GEOMETRY_INPUT_COMPONENTS': ['GetPName'],
 'GL_MAX_GEOMETRY_OUTPUT_COMPONENTS': ['GetPName'],
 'GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS': ['GetPName'],
 'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS': ['GetPName'],
 'GL_MAX_GEOMETRY_UNIFORM_BLOCKS': ['GetPName'],
 'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS': ['GetPName'],
 'GL_MAX_HEIGHT': ['InternalFormatPName'],
 'GL_MAX_INTEGER_SAMPLES': ['GetPName'],
 'GL_MAX_LABEL_LENGTH': ['GetPName'],
 'GL_MAX_LAYERS': ['InternalFormatPName'],
 'GL_MAX_LIGHTS': ['GetPName'],
 'GL_MAX_LIST_NESTING': ['GetPName'],
 'GL_MAX_MODELVIEW_STACK_DEPTH': ['GetPName'],
 'GL_MAX_NAME_LENGTH': ['ProgramInterfacePName'],
 'GL_MAX_NAME_STACK_DEPTH': ['GetPName'],
 'GL_MAX_NUM_ACTIVE_VARIABLES': ['ProgramInterfacePName'],
 'GL_MAX_NUM_COMPATIBLE_SUBROUTINES': ['ProgramInterfacePName'],
 'GL_MAX_PIXEL_MAP_TABLE': ['GetPName'],
 'GL_MAX_PROGRAM_TEXEL_OFFSET': ['GetPName'],
 'GL_MAX_PROJECTION_STACK_DEPTH': ['GetPName'],
 'GL_MAX_RECTANGLE_TEXTURE_SIZE': ['GetPName'],
 'GL_MAX_RENDERBUFFER_SIZE': ['GetPName'],
 'GL_MAX_SAMPLE_MASK_WORDS': ['GetPName'],
 'GL_MAX_SERVER_WAIT_TIMEOUT': ['GetPName'],
 'GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS': ['GetPName'],
 'GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS': ['GetPName'],
 'GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS': ['GetPName'],
 'GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS': ['GetPName'],
 'GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS': ['GetPName'],
 'GL_MAX_TEXTURE_BUFFER_SIZE': ['GetPName'],
 'GL_MAX_TEXTURE_IMAGE_UNITS': ['GetPName'],
 'GL_MAX_TEXTURE_LOD_BIAS': ['GetPName'],
 'GL_MAX_TEXTURE_SIZE': ['GetPName'],
 'GL_MAX_TEXTURE_STACK_DEPTH': ['GetPName'],
 'GL_MAX_UNIFORM_BLOCK_SIZE': ['GetPName'],
 'GL_MAX_UNIFORM_BUFFER_BINDINGS': ['GetPName'],
 'GL_MAX_UNIFORM_LOCATIONS': ['GetPName'],
 'GL_MAX_VARYING_COMPONENTS': ['GetPName'],
 'GL_MAX_VARYING_FLOATS': ['GetPName'],
 'GL_MAX_VARYING_VECTORS': ['GetPName'],
 'GL_MAX_VERTEX_ATOMIC_COUNTERS': ['GetPName'],
 'GL_MAX_VERTEX_ATTRIBS': ['GetPName'],
 'GL_MAX_VERTEX_ATTRIB_BINDINGS': ['GetPName'],
 'GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET': ['GetPName'],
 'GL_MAX_VERTEX_OUTPUT_COMPONENTS': ['GetPName'],
 'GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS': ['GetPName'],
 'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS': ['GetPName'],
 'GL_MAX_VERTEX_UNIFORM_BLOCKS': ['GetPName'],
 'GL_MAX_VERTEX_UNIFORM_COMPONENTS': ['GetPName'],
 'GL_MAX_VERTEX_UNIFORM_VECTORS': ['GetPName'],
 'GL_MAX_VIEWPORTS': ['GetPName'],
 'GL_MAX_VIEWPORT_DIMS': ['GetPName'],
 'GL_MAX_WIDTH': ['InternalFormatPName'],
 'GL_MEDIUM_FLOAT': ['PrecisionType'],
 'GL_MEDIUM_INT': ['PrecisionType'],
 'GL_MIN': ['BlendEquationModeEXT'],
 'GL_MINMAX': ['MinmaxTargetEXT'],
 'GL_MINMAX_EXT': ['EnableCap', 'GetPName', 'MinmaxTargetEXT'],
 'GL_MINMAX_FORMAT': ['GetMinmaxParameterPNameEXT',
                      'GetMinmaxParameterPNameEXT'],
 'GL_MINMAX_FORMAT_EXT': ['GetMinmaxParameterPNameEXT'],
 'GL_MINMAX_SINK': ['GetMinmaxParameterPNameEXT', 'GetMinmaxParameterPNameEXT'],
 'GL_MINMAX_SINK_EXT': ['GetMinmaxParameterPNameEXT'],
 'GL_MINOR_VERSION': ['GetPName'],
 'GL_MIN_EXT': ['BlendEquationModeEXT'],
 'GL_MIN_MAP_BUFFER_ALIGNMENT': ['GetPName'],
 'GL_MIN_PROGRAM_TEXEL_OFFSET': ['GetPName'],
 'GL_MIPMAP': ['InternalFormatPName'],
 'GL_MIRRORED_REPEAT': ['TextureWrapMode'],
 'GL_MODELVIEW': ['MatrixMode'],
 'GL_MODELVIEW0_EXT': ['MatrixMode'],
 'GL_MODELVIEW0_MATRIX_EXT': ['GetPName'],
 'GL_MODELVIEW0_STACK_DEPTH_EXT': ['GetPName'],
 'GL_MODELVIEW_MATRIX': ['GetPName'],
 'GL_MODELVIEW_STACK_DEPTH': ['GetPName'],
 'GL_MODULATE': ['LightEnvModeSGIX', 'TextureEnvMode'],
 'GL_MULT': ['AccumOp'],
 'GL_MULTISAMPLE': ['EnableCap'],
 'GL_MULTISAMPLE_BIT': ['AttribMask'],
 'GL_MULTISAMPLE_BIT_3DFX': ['AttribMask'],
 'GL_MULTISAMPLE_BIT_ARB': ['AttribMask'],
 'GL_MULTISAMPLE_BIT_EXT': ['AttribMask'],
 'GL_MVP_MATRIX_EXT': ['VertexShaderParameterEXT'],
 'GL_N3F_V3F': ['InterleavedArrayFormat'],
 'GL_NAME_LENGTH': ['ProgramResourceProperty'],
 'GL_NAME_STACK_DEPTH': ['GetPName'],
 'GL_NAND': ['LogicOp'],
 'GL_NEAREST': ['TextureMagFilter',
                'TextureMinFilter',
                'BlitFramebufferFilter'],
 'GL_NEAREST_MIPMAP_LINEAR': ['TextureMinFilter'],
 'GL_NEAREST_MIPMAP_NEAREST': ['TextureMinFilter'],
 'GL_NEGATIVE_ONE_EXT': ['VertexShaderCoordOutEXT'],
 'GL_NEGATIVE_ONE_TO_ONE': ['ClipControlDepth'],
 'GL_NEGATIVE_W_EXT': ['VertexShaderCoordOutEXT'],
 'GL_NEGATIVE_X_EXT': ['VertexShaderCoordOutEXT'],
 'GL_NEGATIVE_Y_EXT': ['VertexShaderCoordOutEXT'],
 'GL_NEGATIVE_Z_EXT': ['VertexShaderCoordOutEXT'],
 'GL_NEVER': ['AlphaFunction', 'DepthFunction', 'StencilFunction'],
 'GL_NEVER_EXT': ['IndexFunctionEXT'],
 'GL_NICEST': ['HintMode'],
 'GL_NONE': ['PathColorFormat',
             'CombinerBiasNV',
             'CombinerScaleNV',
             'DrawBufferMode',
             'PixelTexGenMode',
             'ReadBufferMode',
             'ColorBuffer',
             'PathGenMode',
             'PathTransformType',
             'PathFontStyle',
             'TextureCompareMode'],
 'GL_NOOP': ['LogicOp'],
 'GL_NOR': ['LogicOp'],
 'GL_NORMALIZE': ['EnableCap', 'GetPName'],
 'GL_NORMALIZED_RANGE_EXT': ['ParameterRangeEXT'],
 'GL_NORMAL_ARRAY': ['EnableCap', 'GetPName'],
 'GL_NORMAL_ARRAY_COUNT_EXT': ['GetPName'],
 'GL_NORMAL_ARRAY_POINTER': ['GetPointervPName'],
 'GL_NORMAL_ARRAY_POINTER_EXT': ['GetPointervPName'],
 'GL_NORMAL_ARRAY_STRIDE': ['GetPName'],
 'GL_NORMAL_ARRAY_TYPE': ['GetPName'],
 'GL_NOTEQUAL': ['AlphaFunction', 'DepthFunction', 'StencilFunction'],
 'GL_NOTEQUAL_EXT': ['IndexFunctionEXT'],
 'GL_NO_ERROR': ['ErrorCode', 'GraphicsResetStatus'],
 'GL_NUM_ACTIVE_VARIABLES': ['ProgramResourceProperty'],
 'GL_NUM_COMPATIBLE_SUBROUTINES': ['SubroutineParameterName',
                                   'ProgramResourceProperty'],
 'GL_NUM_COMPRESSED_TEXTURE_FORMATS': ['GetPName'],
 'GL_NUM_DEVICE_UUIDS_EXT': ['GetPName'],
 'GL_NUM_EXTENSIONS': ['GetPName'],
 'GL_NUM_PROGRAM_BINARY_FORMATS': ['GetPName'],
 'GL_NUM_SAMPLE_COUNTS': ['InternalFormatPName'],
 'GL_NUM_SHADER_BINARY_FORMATS': ['GetPName'],
 'GL_OBJECT_LINEAR': ['TextureGenMode', 'PathGenMode'],
 'GL_OBJECT_PLANE': ['TextureGenParameter'],
 'GL_OBJECT_TYPE': ['SyncParameterName'],
 'GL_OFFSET': ['ProgramResourceProperty'],
 'GL_ONE': ['BlendingFactor', 'TextureSwizzle'],
 'GL_ONE_EXT': ['VertexShaderCoordOutEXT'],
 'GL_ONE_MINUS_CONSTANT_ALPHA': ['BlendingFactor'],
 'GL_ONE_MINUS_CONSTANT_COLOR': ['BlendingFactor'],
 'GL_ONE_MINUS_DST_ALPHA': ['BlendingFactor'],
 'GL_ONE_MINUS_DST_COLOR': ['BlendingFactor'],
 'GL_ONE_MINUS_SRC1_ALPHA': ['BlendingFactor'],
 'GL_ONE_MINUS_SRC1_COLOR': ['BlendingFactor'],
 'GL_ONE_MINUS_SRC_ALPHA': ['BlendingFactor'],
 'GL_ONE_MINUS_SRC_COLOR': ['BlendingFactor'],
 'GL_OP_ADD_EXT': ['VertexShaderOpEXT'],
 'GL_OP_CLAMP_EXT': ['VertexShaderOpEXT'],
 'GL_OP_CROSS_PRODUCT_EXT': ['VertexShaderOpEXT'],
 'GL_OP_DOT3_EXT': ['VertexShaderOpEXT'],
 'GL_OP_DOT4_EXT': ['VertexShaderOpEXT'],
 'GL_OP_EXP_BASE_2_EXT': ['VertexShaderOpEXT'],
 'GL_OP_FLOOR_EXT': ['VertexShaderOpEXT'],
 'GL_OP_FRAC_EXT': ['VertexShaderOpEXT'],
 'GL_OP_INDEX_EXT': ['VertexShaderOpEXT'],
 'GL_OP_LOG_BASE_2_EXT': ['VertexShaderOpEXT'],
 'GL_OP_MADD_EXT': ['VertexShaderOpEXT'],
 'GL_OP_MAX_EXT': ['VertexShaderOpEXT'],
 'GL_OP_MIN_EXT': ['VertexShaderOpEXT'],
 'GL_OP_MOV_EXT': ['VertexShaderOpEXT'],
 'GL_OP_MULTIPLY_MATRIX_EXT': ['VertexShaderOpEXT'],
 'GL_OP_MUL_EXT': ['VertexShaderOpEXT'],
 'GL_OP_NEGATE_EXT': ['VertexShaderOpEXT'],
 'GL_OP_POWER_EXT': ['VertexShaderOpEXT'],
 'GL_OP_RECIP_EXT': ['VertexShaderOpEXT'],
 'GL_OP_RECIP_SQRT_EXT': ['VertexShaderOpEXT'],
 'GL_OP_ROUND_EXT': ['VertexShaderOpEXT'],
 'GL_OP_SET_GE_EXT': ['VertexShaderOpEXT'],
 'GL_OP_SET_LT_EXT': ['VertexShaderOpEXT'],
 'GL_OP_SUB_EXT': ['VertexShaderOpEXT'],
 'GL_OR': ['LogicOp'],
 'GL_ORDER': ['GetMapQuery', 'MapQuery'],
 'GL_OR_INVERTED': ['LogicOp'],
 'GL_OR_REVERSE': ['LogicOp'],
 'GL_OUT_OF_MEMORY': ['ErrorCode'],
 'GL_PACK_ALIGNMENT': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_CMYK_HINT_EXT': ['GetPName', 'HintTarget'],
 'GL_PACK_IMAGE_HEIGHT': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_IMAGE_HEIGHT_EXT': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_LSB_FIRST': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_RESAMPLE_OML': ['PixelStoreParameter'],
 'GL_PACK_ROW_LENGTH': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_SKIP_IMAGES': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_SKIP_IMAGES_EXT': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_SKIP_PIXELS': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_SKIP_ROWS': ['GetPName', 'PixelStoreParameter'],
 'GL_PACK_SWAP_BYTES': ['GetPName', 'PixelStoreParameter'],
 'GL_PARAMETER_BUFFER': ['BufferTargetARB'],
 'GL_PASS_THROUGH_TOKEN': ['FeedBackToken'],
 'GL_PATCHES': ['PrimitiveType'],
 'GL_PATCHES_EXT': ['PrimitiveType'],
 'GL_PATCH_DEFAULT_INNER_LEVEL': ['PatchParameterName'],
 'GL_PATCH_DEFAULT_OUTER_LEVEL': ['PatchParameterName'],
 'GL_PATCH_VERTICES': ['PatchParameterName'],
 'GL_PERSPECTIVE_CORRECTION_HINT': ['GetPName', 'HintTarget'],
 'GL_PERTURB_EXT': ['TextureNormalModeEXT'],
 'GL_PHONG_HINT_WIN': ['HintTarget'],
 'GL_PIXEL_BUFFER_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_PIXEL_BUFFER_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_PIXEL_CUBIC_WEIGHT_EXT': ['PixelTransformPNameEXT'],
 'GL_PIXEL_MAG_FILTER_EXT': ['PixelTransformPNameEXT'],
 'GL_PIXEL_MAP_A_TO_A': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_A_TO_A_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_B_TO_B': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_B_TO_B_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_G_TO_G': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_G_TO_G_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_I_TO_A': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_I_TO_A_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_I_TO_B': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_I_TO_B_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_I_TO_G': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_I_TO_G_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_I_TO_I': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_I_TO_I_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_I_TO_R': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_I_TO_R_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_R_TO_R': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_R_TO_R_SIZE': ['GetPName'],
 'GL_PIXEL_MAP_S_TO_S': ['GetPixelMap', 'PixelMap'],
 'GL_PIXEL_MAP_S_TO_S_SIZE': ['GetPName'],
 'GL_PIXEL_MIN_FILTER_EXT': ['PixelTransformPNameEXT'],
 'GL_PIXEL_MODE_BIT': ['AttribMask'],
 'GL_PIXEL_PACK_BUFFER': ['BufferTargetARB',
                          'BufferStorageTarget',
                          'CopyBufferSubDataTarget'],
 'GL_PIXEL_PACK_BUFFER_BINDING': ['GetPName'],
 'GL_PIXEL_TRANSFORM_2D_EXT': ['PixelTransformTargetEXT'],
 'GL_PIXEL_UNPACK_BUFFER': ['BufferTargetARB',
                            'BufferStorageTarget',
                            'CopyBufferSubDataTarget'],
 'GL_PIXEL_UNPACK_BUFFER_BINDING': ['GetPName'],
 'GL_POINT': ['MeshMode1', 'MeshMode2', 'PolygonMode'],
 'GL_POINTS': ['PrimitiveType'],
 'GL_POINT_BIT': ['AttribMask'],
 'GL_POINT_DISTANCE_ATTENUATION': ['PointParameterNameSGIS'],
 'GL_POINT_DISTANCE_ATTENUATION_ARB': ['PointParameterNameSGIS'],
 'GL_POINT_FADE_THRESHOLD_SIZE': ['PointParameterNameARB',
                                  'GetPName',
                                  'PointParameterNameSGIS'],
 'GL_POINT_FADE_THRESHOLD_SIZE_ARB': ['PointParameterNameSGIS'],
 'GL_POINT_FADE_THRESHOLD_SIZE_EXT': ['PointParameterNameARB',
                                      'PointParameterNameSGIS'],
 'GL_POINT_SIZE': ['GetPName'],
 'GL_POINT_SIZE_GRANULARITY': ['GetPName'],
 'GL_POINT_SIZE_MAX': ['PointParameterNameSGIS'],
 'GL_POINT_SIZE_MAX_ARB': ['PointParameterNameSGIS'],
 'GL_POINT_SIZE_MAX_EXT': ['PointParameterNameARB', 'PointParameterNameSGIS'],
 'GL_POINT_SIZE_MIN': ['PointParameterNameSGIS'],
 'GL_POINT_SIZE_MIN_ARB': ['PointParameterNameSGIS'],
 'GL_POINT_SIZE_MIN_EXT': ['PointParameterNameARB', 'PointParameterNameSGIS'],
 'GL_POINT_SIZE_RANGE': ['GetPName'],
 'GL_POINT_SMOOTH': ['EnableCap', 'GetPName'],
 'GL_POINT_SMOOTH_HINT': ['GetPName', 'HintTarget'],
 'GL_POINT_TOKEN': ['FeedBackToken'],
 'GL_POLYGON': ['PrimitiveType'],
 'GL_POLYGON_BIT': ['AttribMask'],
 'GL_POLYGON_MODE': ['GetPName'],
 'GL_POLYGON_OFFSET_BIAS_EXT': ['GetPName'],
 'GL_POLYGON_OFFSET_FACTOR': ['GetPName'],
 'GL_POLYGON_OFFSET_FILL': ['EnableCap', 'GetPName'],
 'GL_POLYGON_OFFSET_LINE': ['EnableCap', 'GetPName'],
 'GL_POLYGON_OFFSET_POINT': ['EnableCap', 'GetPName'],
 'GL_POLYGON_OFFSET_UNITS': ['GetPName'],
 'GL_POLYGON_SMOOTH': ['EnableCap', 'GetPName'],
 'GL_POLYGON_SMOOTH_HINT': ['GetPName', 'HintTarget'],
 'GL_POLYGON_STIPPLE': ['EnableCap', 'GetPName'],
 'GL_POLYGON_STIPPLE_BIT': ['AttribMask'],
 'GL_POLYGON_TOKEN': ['FeedBackToken'],
 'GL_POSITION': ['LightParameter'],
 'GL_POST_COLOR_MATRIX_ALPHA_BIAS': ['PixelTransferParameter'],
 'GL_POST_COLOR_MATRIX_ALPHA_SCALE': ['PixelTransferParameter'],
 'GL_POST_COLOR_MATRIX_BLUE_BIAS': ['PixelTransferParameter'],
 'GL_POST_COLOR_MATRIX_BLUE_SCALE': ['PixelTransferParameter'],
 'GL_POST_COLOR_MATRIX_COLOR_TABLE': ['ColorTableTargetSGI',
                                      'ColorTableTarget'],
 'GL_POST_COLOR_MATRIX_GREEN_BIAS': ['PixelTransferParameter'],
 'GL_POST_COLOR_MATRIX_GREEN_SCALE': ['PixelTransferParameter'],
 'GL_POST_COLOR_MATRIX_RED_BIAS': ['PixelTransferParameter'],
 'GL_POST_COLOR_MATRIX_RED_SCALE': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_ALPHA_BIAS': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_ALPHA_BIAS_EXT': ['GetPName', 'PixelTransferParameter'],
 'GL_POST_CONVOLUTION_ALPHA_SCALE': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_ALPHA_SCALE_EXT': ['GetPName', 'PixelTransferParameter'],
 'GL_POST_CONVOLUTION_BLUE_BIAS': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_BLUE_BIAS_EXT': ['GetPName', 'PixelTransferParameter'],
 'GL_POST_CONVOLUTION_BLUE_SCALE': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_BLUE_SCALE_EXT': ['GetPName', 'PixelTransferParameter'],
 'GL_POST_CONVOLUTION_COLOR_TABLE': ['ColorTableTargetSGI', 'ColorTableTarget'],
 'GL_POST_CONVOLUTION_GREEN_BIAS': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_GREEN_BIAS_EXT': ['GetPName', 'PixelTransferParameter'],
 'GL_POST_CONVOLUTION_GREEN_SCALE': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_GREEN_SCALE_EXT': ['GetPName', 'PixelTransferParameter'],
 'GL_POST_CONVOLUTION_RED_BIAS': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_RED_BIAS_EXT': ['GetPName', 'PixelTransferParameter'],
 'GL_POST_CONVOLUTION_RED_SCALE': ['PixelTransferParameter'],
 'GL_POST_CONVOLUTION_RED_SCALE_EXT': ['GetPName', 'PixelTransferParameter'],
 'GL_PRIMARY_COLOR': ['PathColor'],
 'GL_PRIMITIVES_GENERATED': ['QueryTarget'],
 'GL_PRIMITIVES_SUBMITTED': ['QueryTarget'],
 'GL_PRIMITIVE_RESTART': ['EnableCap'],
 'GL_PRIMITIVE_RESTART_FIXED_INDEX': ['EnableCap'],
 'GL_PRIMITIVE_RESTART_INDEX': ['GetPName'],
 'GL_PROGRAM': ['ObjectIdentifier'],
 'GL_PROGRAMMABLE_SAMPLE_LOCATION_ARB': ['GetMultisamplePNameNV'],
 'GL_PROGRAM_BINARY_FORMATS': ['GetPName'],
 'GL_PROGRAM_BINARY_LENGTH': ['ProgramPropertyARB'],
 'GL_PROGRAM_BINARY_RETRIEVABLE_HINT': ['HintTarget', 'ProgramParameterPName'],
 'GL_PROGRAM_FORMAT_ASCII': ['ProgramFormat'],
 'GL_PROGRAM_FORMAT_ASCII_ARB': ['ProgramFormatARB'],
 'GL_PROGRAM_INPUT': ['ProgramInterface'],
 'GL_PROGRAM_OUTPUT': ['ProgramInterface'],
 'GL_PROGRAM_PIPELINE': ['ObjectIdentifier'],
 'GL_PROGRAM_PIPELINE_BINDING': ['GetPName'],
 'GL_PROGRAM_POINT_SIZE': ['EnableCap', 'GetPName'],
 'GL_PROGRAM_SEPARABLE': ['ProgramParameterPName'],
 'GL_PROGRAM_STRING': ['ProgramStringProperty'],
 'GL_PROGRAM_STRING_ARB': ['ProgramStringPropertyARB'],
 'GL_PROJECTION': ['MatrixMode'],
 'GL_PROJECTION_MATRIX': ['GetPName'],
 'GL_PROJECTION_STACK_DEPTH': ['GetPName'],
 'GL_PROTECTED_MEMORY_OBJECT_EXT': ['MemoryObjectParameterName'],
 'GL_PROVOKING_VERTEX': ['GetPName'],
 'GL_PROXY_COLOR_TABLE': ['ColorTableTargetSGI'],
 'GL_PROXY_HISTOGRAM': ['HistogramTargetEXT'],
 'GL_PROXY_HISTOGRAM_EXT': ['HistogramTargetEXT'],
 'GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE': ['ColorTableTargetSGI'],
 'GL_PROXY_POST_CONVOLUTION_COLOR_TABLE': ['ColorTableTargetSGI'],
 'GL_PROXY_TEXTURE_1D': ['TextureTarget'],
 'GL_PROXY_TEXTURE_1D_ARRAY': ['TextureTarget'],
 'GL_PROXY_TEXTURE_1D_ARRAY_EXT': ['TextureTarget'],
 'GL_PROXY_TEXTURE_1D_EXT': ['TextureTarget'],
 'GL_PROXY_TEXTURE_2D': ['TextureTarget'],
 'GL_PROXY_TEXTURE_2D_ARRAY': ['TextureTarget'],
 'GL_PROXY_TEXTURE_2D_ARRAY_EXT': ['TextureTarget'],
 'GL_PROXY_TEXTURE_2D_EXT': ['TextureTarget'],
 'GL_PROXY_TEXTURE_2D_MULTISAMPLE': ['TextureTarget'],
 'GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY': ['TextureTarget'],
 'GL_PROXY_TEXTURE_3D': ['TextureTarget'],
 'GL_PROXY_TEXTURE_3D_EXT': ['TextureTarget'],
 'GL_PROXY_TEXTURE_CUBE_MAP': ['TextureTarget'],
 'GL_PROXY_TEXTURE_CUBE_MAP_ARB': ['TextureTarget'],
 'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY': ['TextureTarget'],
 'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB': ['TextureTarget'],
 'GL_PROXY_TEXTURE_CUBE_MAP_EXT': ['TextureTarget'],
 'GL_PROXY_TEXTURE_RECTANGLE': ['TextureTarget'],
 'GL_PROXY_TEXTURE_RECTANGLE_ARB': ['TextureTarget'],
 'GL_Q': ['TextureCoordName'],
 'GL_QUADRATIC_ATTENUATION': ['LightParameter'],
 'GL_QUADS': ['PrimitiveType'],
 'GL_QUADS_EXT': ['PrimitiveType'],
 'GL_QUAD_STRIP': ['PrimitiveType'],
 'GL_QUERY': ['ObjectIdentifier'],
 'GL_QUERY_BUFFER': ['BufferTargetARB',
                     'BufferStorageTarget',
                     'CopyBufferSubDataTarget'],
 'GL_QUERY_BUFFER_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_QUERY_BY_REGION_NO_WAIT': ['ConditionalRenderMode'],
 'GL_QUERY_BY_REGION_NO_WAIT_INVERTED': ['ConditionalRenderMode'],
 'GL_QUERY_BY_REGION_WAIT': ['ConditionalRenderMode'],
 'GL_QUERY_BY_REGION_WAIT_INVERTED': ['ConditionalRenderMode'],
 'GL_QUERY_COUNTER_BITS': ['QueryParameterName'],
 'GL_QUERY_NO_WAIT': ['ConditionalRenderMode'],
 'GL_QUERY_NO_WAIT_INVERTED': ['ConditionalRenderMode'],
 'GL_QUERY_RESULT': ['QueryObjectParameterName'],
 'GL_QUERY_RESULT_AVAILABLE': ['QueryObjectParameterName'],
 'GL_QUERY_RESULT_NO_WAIT': ['QueryObjectParameterName'],
 'GL_QUERY_TARGET': ['QueryObjectParameterName'],
 'GL_QUERY_WAIT': ['ConditionalRenderMode'],
 'GL_QUERY_WAIT_INVERTED': ['ConditionalRenderMode'],
 'GL_R': ['TextureCoordName'],
 'GL_R11F_G11F_B10F': ['InternalFormat'],
 'GL_R11F_G11F_B10F_EXT': ['InternalFormat'],
 'GL_R16': ['InternalFormat'],
 'GL_R16F': ['InternalFormat'],
 'GL_R16F_EXT': ['InternalFormat'],
 'GL_R16I': ['InternalFormat'],
 'GL_R16UI': ['InternalFormat'],
 'GL_R16_EXT': ['InternalFormat'],
 'GL_R16_SNORM': ['InternalFormat'],
 'GL_R16_SNORM_EXT': ['InternalFormat'],
 'GL_R32F': ['InternalFormat'],
 'GL_R32F_EXT': ['InternalFormat'],
 'GL_R32I': ['InternalFormat'],
 'GL_R32UI': ['InternalFormat'],
 'GL_R3_G3_B2': ['InternalFormat'],
 'GL_R8': ['InternalFormat'],
 'GL_R8I': ['InternalFormat'],
 'GL_R8UI': ['InternalFormat'],
 'GL_R8_EXT': ['InternalFormat'],
 'GL_R8_SNORM': ['InternalFormat'],
 'GL_RASTERIZER_DISCARD': ['EnableCap'],
 'GL_READ_BUFFER': ['GetPName'],
 'GL_READ_BUFFER_EXT': ['GetPName'],
 'GL_READ_FRAMEBUFFER': ['FramebufferTarget', 'CheckFramebufferStatusTarget'],
 'GL_READ_FRAMEBUFFER_BINDING': ['GetPName'],
 'GL_READ_ONLY': ['BufferAccessARB'],
 'GL_READ_PIXELS': ['InternalFormatPName'],
 'GL_READ_PIXELS_FORMAT': ['InternalFormatPName'],
 'GL_READ_PIXELS_TYPE': ['InternalFormatPName'],
 'GL_READ_WRITE': ['BufferAccessARB'],
 'GL_RED': ['PixelFormat', 'InternalFormat', 'TextureSwizzle'],
 'GL_REDUCE': ['ConvolutionBorderModeEXT'],
 'GL_REDUCE_EXT': ['ConvolutionBorderModeEXT'],
 'GL_RED_BIAS': ['GetPName', 'PixelTransferParameter'],
 'GL_RED_BITS': ['GetPName'],
 'GL_RED_EXT': ['PixelFormat', 'InternalFormat'],
 'GL_RED_INTEGER': ['PixelFormat'],
 'GL_RED_SCALE': ['GetPName', 'PixelTransferParameter'],
 'GL_REFERENCED_BY_COMPUTE_SHADER': ['ProgramResourceProperty'],
 'GL_REFERENCED_BY_FRAGMENT_SHADER': ['ProgramResourceProperty'],
 'GL_REFERENCED_BY_GEOMETRY_SHADER': ['ProgramResourceProperty'],
 'GL_REFERENCED_BY_TESS_CONTROL_SHADER': ['ProgramResourceProperty'],
 'GL_REFERENCED_BY_TESS_EVALUATION_SHADER': ['ProgramResourceProperty'],
 'GL_REFERENCED_BY_VERTEX_SHADER': ['ProgramResourceProperty'],
 'GL_RENDER': ['RenderingMode'],
 'GL_RENDERBUFFER': ['RenderbufferTarget',
                     'CopyImageSubDataTarget',
                     'ObjectIdentifier'],
 'GL_RENDERBUFFER_ALPHA_SIZE': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_ALPHA_SIZE_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_BINDING': ['GetPName'],
 'GL_RENDERBUFFER_BLUE_SIZE': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_BLUE_SIZE_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_DEPTH_SIZE': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_DEPTH_SIZE_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_GREEN_SIZE': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_GREEN_SIZE_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_HEIGHT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_HEIGHT_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_INTERNAL_FORMAT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_INTERNAL_FORMAT_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_RED_SIZE': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_RED_SIZE_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_SAMPLES': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_SAMPLES_ANGLE': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_SAMPLES_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_SAMPLES_IMG': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_STENCIL_SIZE': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_STENCIL_SIZE_EXT': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_WIDTH': ['RenderbufferParameterName'],
 'GL_RENDERBUFFER_WIDTH_EXT': ['RenderbufferParameterName'],
 'GL_RENDERER': ['StringName'],
 'GL_RENDER_MODE': ['GetPName'],
 'GL_REPEAT': ['TextureWrapMode'],
 'GL_REPLACE': ['LightEnvModeSGIX', 'StencilOp'],
 'GL_REPLACE_EXT': ['TextureEnvMode'],
 'GL_RESCALE_NORMAL_EXT': ['EnableCap', 'GetPName'],
 'GL_RETURN': ['AccumOp'],
 'GL_RG': ['PixelFormat', 'InternalFormat'],
 'GL_RG16': ['InternalFormat'],
 'GL_RG16F': ['InternalFormat'],
 'GL_RG16F_EXT': ['InternalFormat'],
 'GL_RG16I': ['InternalFormat'],
 'GL_RG16UI': ['InternalFormat'],
 'GL_RG16_EXT': ['InternalFormat'],
 'GL_RG16_SNORM': ['InternalFormat'],
 'GL_RG16_SNORM_EXT': ['InternalFormat'],
 'GL_RG32F': ['InternalFormat'],
 'GL_RG32F_EXT': ['InternalFormat'],
 'GL_RG32I': ['InternalFormat'],
 'GL_RG32UI': ['InternalFormat'],
 'GL_RG8': ['InternalFormat'],
 'GL_RG8I': ['InternalFormat'],
 'GL_RG8UI': ['InternalFormat'],
 'GL_RG8_EXT': ['InternalFormat'],
 'GL_RG8_SNORM': ['InternalFormat'],
 'GL_RGB': ['PathColorFormat',
            'PixelFormat',
            'InternalFormat',
            'PixelTexGenMode'],
 'GL_RGB10': ['InternalFormat'],
 'GL_RGB10_A2': ['InternalFormat'],
 'GL_RGB10_A2UI': ['InternalFormat'],
 'GL_RGB10_A2_EXT': ['InternalFormat'],
 'GL_RGB10_EXT': ['InternalFormat'],
 'GL_RGB12': ['InternalFormat'],
 'GL_RGB12_EXT': ['InternalFormat'],
 'GL_RGB16': ['InternalFormat'],
 'GL_RGB16F': ['InternalFormat'],
 'GL_RGB16F_ARB': ['InternalFormat'],
 'GL_RGB16F_EXT': ['InternalFormat'],
 'GL_RGB16I': ['InternalFormat'],
 'GL_RGB16UI': ['InternalFormat'],
 'GL_RGB16_EXT': ['InternalFormat'],
 'GL_RGB16_SNORM': ['InternalFormat'],
 'GL_RGB16_SNORM_EXT': ['InternalFormat'],
 'GL_RGB2_EXT': ['InternalFormat'],
 'GL_RGB32F': ['InternalFormat'],
 'GL_RGB32I': ['InternalFormat'],
 'GL_RGB32UI': ['InternalFormat'],
 'GL_RGB4': ['InternalFormat'],
 'GL_RGB4_EXT': ['InternalFormat'],
 'GL_RGB5': ['InternalFormat'],
 'GL_RGB5_A1': ['InternalFormat'],
 'GL_RGB5_A1_EXT': ['InternalFormat'],
 'GL_RGB5_EXT': ['InternalFormat'],
 'GL_RGB8': ['InternalFormat'],
 'GL_RGB8I': ['InternalFormat'],
 'GL_RGB8UI': ['InternalFormat'],
 'GL_RGB8_EXT': ['InternalFormat'],
 'GL_RGB8_SNORM': ['InternalFormat'],
 'GL_RGB9_E5': ['InternalFormat'],
 'GL_RGB9_E5_EXT': ['InternalFormat'],
 'GL_RGBA': ['PathColorFormat',
             'PixelFormat',
             'InternalFormat',
             'PixelTexGenMode'],
 'GL_RGBA12': ['InternalFormat'],
 'GL_RGBA12_EXT': ['InternalFormat'],
 'GL_RGBA16': ['InternalFormat'],
 'GL_RGBA16F': ['InternalFormat'],
 'GL_RGBA16F_ARB': ['InternalFormat'],
 'GL_RGBA16F_EXT': ['InternalFormat'],
 'GL_RGBA16I': ['InternalFormat'],
 'GL_RGBA16UI': ['InternalFormat'],
 'GL_RGBA16_EXT': ['InternalFormat'],
 'GL_RGBA32F': ['InternalFormat'],
 'GL_RGBA32F_ARB': ['InternalFormat'],
 'GL_RGBA32F_EXT': ['InternalFormat'],
 'GL_RGBA32I': ['InternalFormat'],
 'GL_RGBA32UI': ['InternalFormat'],
 'GL_RGBA4': ['InternalFormat'],
 'GL_RGBA4_EXT': ['InternalFormat'],
 'GL_RGBA8': ['InternalFormat'],
 'GL_RGBA8I': ['InternalFormat'],
 'GL_RGBA8UI': ['InternalFormat'],
 'GL_RGBA8_EXT': ['InternalFormat'],
 'GL_RGBA8_SNORM': ['InternalFormat'],
 'GL_RGBA_INTEGER': ['PixelFormat'],
 'GL_RGBA_MODE': ['GetPName'],
 'GL_RGB_INTEGER': ['PixelFormat'],
 'GL_RG_INTEGER': ['PixelFormat'],
 'GL_RIGHT': ['DrawBufferMode', 'ReadBufferMode', 'ColorBuffer'],
 'GL_S': ['TextureCoordName'],
 'GL_SAMPLER': ['ObjectIdentifier'],
 'GL_SAMPLER_1D': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_1D_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_1D_ARRAY_SHADOW': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_1D_SHADOW': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_2D': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_2D_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_2D_ARRAY_SHADOW': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_2D_MULTISAMPLE': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_2D_MULTISAMPLE_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_2D_RECT': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_2D_RECT_SHADOW': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_2D_SHADOW': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_3D': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_BINDING': ['GetPName'],
 'GL_SAMPLER_BUFFER': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_CUBE': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_CUBE_MAP_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLER_CUBE_SHADOW': ['UniformType', 'GlslTypeToken'],
 'GL_SAMPLES': ['GetPName', 'InternalFormatPName', 'GetFramebufferParameter'],
 'GL_SAMPLES_PASSED': ['QueryTarget'],
 'GL_SAMPLE_ALPHA_TO_COVERAGE': ['EnableCap'],
 'GL_SAMPLE_ALPHA_TO_ONE': ['EnableCap'],
 'GL_SAMPLE_BUFFERS': ['GetPName', 'GetFramebufferParameter'],
 'GL_SAMPLE_COVERAGE': ['EnableCap'],
 'GL_SAMPLE_COVERAGE_INVERT': ['GetPName'],
 'GL_SAMPLE_COVERAGE_VALUE': ['GetPName'],
 'GL_SAMPLE_LOCATION_ARB': ['GetMultisamplePNameNV'],
 'GL_SAMPLE_MASK': ['EnableCap'],
 'GL_SAMPLE_POSITION': ['GetMultisamplePNameNV'],
 'GL_SAMPLE_SHADING': ['EnableCap'],
 'GL_SCALAR_EXT': ['DataTypeEXT'],
 'GL_SCISSOR_BIT': ['AttribMask'],
 'GL_SCISSOR_BOX': ['GetPName'],
 'GL_SCISSOR_TEST': ['EnableCap', 'GetPName'],
 'GL_SELECT': ['RenderingMode'],
 'GL_SELECTION_BUFFER_POINTER': ['GetPointervPName'],
 'GL_SELECTION_BUFFER_SIZE': ['GetPName'],
 'GL_SEPARABLE_2D': ['SeparableTargetEXT'],
 'GL_SEPARABLE_2D_EXT': ['EnableCap', 'GetPName', 'SeparableTargetEXT'],
 'GL_SEPARATE_ATTRIBS': ['TransformFeedbackBufferMode'],
 'GL_SEPARATE_SPECULAR_COLOR': ['LightModelColorControl'],
 'GL_SEPARATE_SPECULAR_COLOR_EXT': ['LightModelColorControl'],
 'GL_SET': ['LogicOp'],
 'GL_SHADER': ['ObjectIdentifier'],
 'GL_SHADER_COMPILER': ['GetPName'],
 'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_SHADER_IMAGE_ATOMIC': ['InternalFormatPName'],
 'GL_SHADER_IMAGE_LOAD': ['InternalFormatPName'],
 'GL_SHADER_IMAGE_STORE': ['InternalFormatPName'],
 'GL_SHADER_SOURCE_LENGTH': ['ShaderParameterName'],
 'GL_SHADER_STORAGE_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_SHADER_STORAGE_BLOCK': ['ProgramInterface'],
 'GL_SHADER_STORAGE_BUFFER': ['BufferTargetARB',
                              'BufferStorageTarget',
                              'CopyBufferSubDataTarget'],
 'GL_SHADER_STORAGE_BUFFER_BINDING': ['GetPName'],
 'GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT': ['GetPName'],
 'GL_SHADER_STORAGE_BUFFER_SIZE': ['GetPName'],
 'GL_SHADER_STORAGE_BUFFER_START': ['GetPName'],
 'GL_SHADER_TYPE': ['ShaderParameterName'],
 'GL_SHADE_MODEL': ['GetPName'],
 'GL_SHADING_LANGUAGE_VERSION': ['StringName'],
 'GL_SHADOW_ATTENUATION_EXT': ['LightTexturePNameEXT'],
 'GL_SHARED_TEXTURE_PALETTE_EXT': ['EnableCap', 'GetPName'],
 'GL_SHININESS': ['MaterialParameter'],
 'GL_SHORT': ['ColorPointerType',
              'IndexPointerType',
              'ListNameType',
              'NormalPointerType',
              'PixelType',
              'TexCoordPointerType',
              'VertexPointerType',
              'VertexAttribType',
              'VertexAttribPointerType',
              'VertexAttribIType'],
 'GL_SHORT_ARB': ['WeightPointerTypeARB'],
 'GL_SHORT_EXT': ['TangentPointerTypeEXT', 'BinormalPointerTypeEXT'],
 'GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST': ['InternalFormatPName'],
 'GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE': ['InternalFormatPName'],
 'GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST': ['InternalFormatPName'],
 'GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE': ['InternalFormatPName'],
 'GL_SINGLE_COLOR': ['LightModelColorControl'],
 'GL_SINGLE_COLOR_EXT': ['LightModelColorControl'],
 'GL_SMOOTH': ['ShadingModel'],
 'GL_SMOOTH_LINE_WIDTH_GRANULARITY': ['GetPName'],
 'GL_SMOOTH_LINE_WIDTH_RANGE': ['GetPName'],
 'GL_SMOOTH_POINT_SIZE_GRANULARITY': ['GetPName'],
 'GL_SMOOTH_POINT_SIZE_RANGE': ['GetPName'],
 'GL_SPARSE_STORAGE_BIT_ARB': ['BufferStorageMask'],
 'GL_SPECULAR': ['ColorMaterialParameter',
                 'LightParameter',
                 'MaterialParameter'],
 'GL_SPHERE_MAP': ['TextureGenMode'],
 'GL_SPOT_CUTOFF': ['LightParameter'],
 'GL_SPOT_DIRECTION': ['LightParameter'],
 'GL_SPOT_EXPONENT': ['LightParameter'],
 'GL_SRC1_ALPHA': ['BlendingFactor'],
 'GL_SRC1_COLOR': ['BlendingFactor'],
 'GL_SRC_ALPHA': ['BlendingFactor'],
 'GL_SRC_ALPHA_SATURATE': ['BlendingFactor'],
 'GL_SRC_COLOR': ['BlendingFactor'],
 'GL_SRGB': ['InternalFormat'],
 'GL_SRGB8': ['InternalFormat'],
 'GL_SRGB8_ALPHA8': ['InternalFormat'],
 'GL_SRGB8_ALPHA8_EXT': ['InternalFormat'],
 'GL_SRGB8_EXT': ['InternalFormat'],
 'GL_SRGB_ALPHA': ['InternalFormat'],
 'GL_SRGB_ALPHA_EXT': ['InternalFormat'],
 'GL_SRGB_EXT': ['InternalFormat'],
 'GL_SRGB_READ': ['InternalFormatPName'],
 'GL_SRGB_WRITE': ['InternalFormatPName'],
 'GL_STACK_OVERFLOW': ['ErrorCode'],
 'GL_STACK_UNDERFLOW': ['ErrorCode'],
 'GL_STATIC_COPY': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_STATIC_DRAW': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_STATIC_READ': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_STENCIL': ['PixelCopyType',
                'InvalidateFramebufferAttachment',
                'InvalidateFramebufferAttachment',
                'Buffer'],
 'GL_STENCIL_ATTACHMENT': ['FramebufferAttachment'],
 'GL_STENCIL_ATTACHMENT_EXT': ['FramebufferAttachment',
                               'InvalidateFramebufferAttachment'],
 'GL_STENCIL_BACK_FAIL': ['GetPName'],
 'GL_STENCIL_BACK_FUNC': ['GetPName'],
 'GL_STENCIL_BACK_PASS_DEPTH_FAIL': ['GetPName'],
 'GL_STENCIL_BACK_PASS_DEPTH_PASS': ['GetPName'],
 'GL_STENCIL_BACK_REF': ['GetPName'],
 'GL_STENCIL_BACK_VALUE_MASK': ['GetPName'],
 'GL_STENCIL_BACK_WRITEMASK': ['GetPName'],
 'GL_STENCIL_BITS': ['GetPName'],
 'GL_STENCIL_BUFFER_BIT': ['AttribMask', 'ClearBufferMask'],
 'GL_STENCIL_CLEAR_VALUE': ['GetPName'],
 'GL_STENCIL_EXT': ['PixelCopyType'],
 'GL_STENCIL_FAIL': ['GetPName'],
 'GL_STENCIL_FUNC': ['GetPName'],
 'GL_STENCIL_INDEX': ['PixelFormat', 'InternalFormat'],
 'GL_STENCIL_INDEX1': ['InternalFormat'],
 'GL_STENCIL_INDEX16': ['InternalFormat'],
 'GL_STENCIL_INDEX16_EXT': ['InternalFormat'],
 'GL_STENCIL_INDEX1_EXT': ['InternalFormat'],
 'GL_STENCIL_INDEX4': ['InternalFormat'],
 'GL_STENCIL_INDEX4_EXT': ['InternalFormat'],
 'GL_STENCIL_INDEX8': ['InternalFormat'],
 'GL_STENCIL_INDEX8_EXT': ['InternalFormat'],
 'GL_STENCIL_PASS_DEPTH_FAIL': ['GetPName'],
 'GL_STENCIL_PASS_DEPTH_PASS': ['GetPName'],
 'GL_STENCIL_REF': ['GetPName'],
 'GL_STENCIL_RENDERABLE': ['InternalFormatPName'],
 'GL_STENCIL_TEST': ['EnableCap', 'GetPName'],
 'GL_STENCIL_VALUE_MASK': ['GetPName'],
 'GL_STENCIL_WRITEMASK': ['GetPName'],
 'GL_STEREO': ['GetPName', 'GetFramebufferParameter'],
 'GL_STREAM_COPY': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_STREAM_DRAW': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_STREAM_READ': ['BufferUsageARB', 'VertexBufferObjectUsage'],
 'GL_SUBPIXEL_BITS': ['GetPName'],
 'GL_SYNC_CONDITION': ['SyncParameterName'],
 'GL_SYNC_FLAGS': ['SyncParameterName'],
 'GL_SYNC_FLUSH_COMMANDS_BIT': ['SyncObjectMask'],
 'GL_SYNC_GPU_COMMANDS_COMPLETE': ['SyncCondition'],
 'GL_SYNC_STATUS': ['SyncParameterName'],
 'GL_T': ['TextureCoordName'],
 'GL_T2F_C3F_V3F': ['InterleavedArrayFormat'],
 'GL_T2F_C4F_N3F_V3F': ['InterleavedArrayFormat'],
 'GL_T2F_C4UB_V3F': ['InterleavedArrayFormat'],
 'GL_T2F_N3F_V3F': ['InterleavedArrayFormat'],
 'GL_T2F_V3F': ['InterleavedArrayFormat'],
 'GL_T4F_C4F_N3F_V4F': ['InterleavedArrayFormat'],
 'GL_T4F_V4F': ['InterleavedArrayFormat'],
 'GL_TABLE_TOO_LARGE': ['ErrorCode'],
 'GL_TABLE_TOO_LARGE_EXT': ['ErrorCode'],
 'GL_TESS_CONTROL_SHADER': ['ShaderType', 'PipelineParameterName'],
 'GL_TESS_CONTROL_SHADER_BIT': ['UseProgramStageMask'],
 'GL_TESS_CONTROL_SHADER_BIT_EXT': ['UseProgramStageMask'],
 'GL_TESS_CONTROL_SUBROUTINE': ['ProgramInterface'],
 'GL_TESS_CONTROL_SUBROUTINE_UNIFORM': ['ProgramInterface'],
 'GL_TESS_CONTROL_TEXTURE': ['InternalFormatPName'],
 'GL_TESS_EVALUATION_SHADER': ['ShaderType', 'PipelineParameterName'],
 'GL_TESS_EVALUATION_SHADER_BIT': ['UseProgramStageMask'],
 'GL_TESS_EVALUATION_SHADER_BIT_EXT': ['UseProgramStageMask'],
 'GL_TESS_EVALUATION_SUBROUTINE': ['ProgramInterface'],
 'GL_TESS_EVALUATION_SUBROUTINE_UNIFORM': ['ProgramInterface'],
 'GL_TESS_EVALUATION_TEXTURE': ['InternalFormatPName'],
 'GL_TEXTURE': ['MatrixMode', 'ObjectIdentifier'],
 'GL_TEXTURE0': ['TextureUnit'],
 'GL_TEXTURE0_ARB': ['CombinerRegisterNV'],
 'GL_TEXTURE1': ['TextureUnit'],
 'GL_TEXTURE10': ['TextureUnit'],
 'GL_TEXTURE11': ['TextureUnit'],
 'GL_TEXTURE12': ['TextureUnit'],
 'GL_TEXTURE13': ['TextureUnit'],
 'GL_TEXTURE14': ['TextureUnit'],
 'GL_TEXTURE15': ['TextureUnit'],
 'GL_TEXTURE16': ['TextureUnit'],
 'GL_TEXTURE17': ['TextureUnit'],
 'GL_TEXTURE18': ['TextureUnit'],
 'GL_TEXTURE19': ['TextureUnit'],
 'GL_TEXTURE1_ARB': ['CombinerRegisterNV'],
 'GL_TEXTURE2': ['TextureUnit'],
 'GL_TEXTURE20': ['TextureUnit'],
 'GL_TEXTURE21': ['TextureUnit'],
 'GL_TEXTURE22': ['TextureUnit'],
 'GL_TEXTURE23': ['TextureUnit'],
 'GL_TEXTURE24': ['TextureUnit'],
 'GL_TEXTURE25': ['TextureUnit'],
 'GL_TEXTURE26': ['TextureUnit'],
 'GL_TEXTURE27': ['TextureUnit'],
 'GL_TEXTURE28': ['TextureUnit'],
 'GL_TEXTURE29': ['TextureUnit'],
 'GL_TEXTURE3': ['TextureUnit'],
 'GL_TEXTURE30': ['TextureUnit'],
 'GL_TEXTURE31': ['TextureUnit'],
 'GL_TEXTURE4': ['TextureUnit'],
 'GL_TEXTURE5': ['TextureUnit'],
 'GL_TEXTURE6': ['TextureUnit'],
 'GL_TEXTURE7': ['TextureUnit'],
 'GL_TEXTURE8': ['TextureUnit'],
 'GL_TEXTURE9': ['TextureUnit'],
 'GL_TEXTURE_1D': ['EnableCap',
                   'GetPName',
                   'TextureTarget',
                   'CopyImageSubDataTarget'],
 'GL_TEXTURE_1D_ARRAY': ['TextureTarget', 'CopyImageSubDataTarget'],
 'GL_TEXTURE_2D': ['EnableCap',
                   'GetPName',
                   'TextureTarget',
                   'CopyImageSubDataTarget'],
 'GL_TEXTURE_2D_ARRAY': ['TextureTarget', 'CopyImageSubDataTarget'],
 'GL_TEXTURE_2D_MULTISAMPLE': ['TextureTarget', 'CopyImageSubDataTarget'],
 'GL_TEXTURE_2D_MULTISAMPLE_ARRAY': ['TextureTarget', 'CopyImageSubDataTarget'],
 'GL_TEXTURE_3D': ['TextureTarget', 'CopyImageSubDataTarget'],
 'GL_TEXTURE_3D_BINDING_EXT': ['GetPName'],
 'GL_TEXTURE_3D_EXT': ['EnableCap', 'GetPName', 'TextureTarget'],
 'GL_TEXTURE_ALPHA_SIZE': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_BASE_LEVEL': ['TextureParameterName'],
 'GL_TEXTURE_BINDING_1D': ['GetPName'],
 'GL_TEXTURE_BINDING_1D_ARRAY': ['GetPName'],
 'GL_TEXTURE_BINDING_2D': ['GetPName'],
 'GL_TEXTURE_BINDING_2D_ARRAY': ['GetPName'],
 'GL_TEXTURE_BINDING_2D_MULTISAMPLE': ['GetPName'],
 'GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY': ['GetPName'],
 'GL_TEXTURE_BINDING_3D': ['GetPName'],
 'GL_TEXTURE_BINDING_BUFFER': ['GetPName'],
 'GL_TEXTURE_BINDING_CUBE_MAP': ['GetPName'],
 'GL_TEXTURE_BINDING_RECTANGLE': ['GetPName'],
 'GL_TEXTURE_BIT': ['AttribMask'],
 'GL_TEXTURE_BLUE_SIZE': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_BORDER': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_BORDER_COLOR': ['GetTextureParameter',
                             'TextureParameterName',
                             'SamplerParameterF'],
 'GL_TEXTURE_BUFFER': ['BufferTargetARB',
                       'BufferStorageTarget',
                       'CopyBufferSubDataTarget'],
 'GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT': ['GetPName'],
 'GL_TEXTURE_COMPARE_FUNC': ['TextureParameterName', 'SamplerParameterI'],
 'GL_TEXTURE_COMPARE_MODE': ['TextureParameterName', 'SamplerParameterI'],
 'GL_TEXTURE_COMPONENTS': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_COMPRESSED': ['InternalFormatPName'],
 'GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT': ['InternalFormatPName'],
 'GL_TEXTURE_COMPRESSED_BLOCK_SIZE': ['InternalFormatPName'],
 'GL_TEXTURE_COMPRESSED_BLOCK_WIDTH': ['InternalFormatPName'],
 'GL_TEXTURE_COMPRESSION_HINT': ['GetPName', 'HintTarget'],
 'GL_TEXTURE_COMPRESSION_HINT_ARB': ['HintTarget'],
 'GL_TEXTURE_COORD_ARRAY': ['EnableCap', 'GetPName'],
 'GL_TEXTURE_COORD_ARRAY_COUNT_EXT': ['GetPName'],
 'GL_TEXTURE_COORD_ARRAY_POINTER': ['GetPointervPName'],
 'GL_TEXTURE_COORD_ARRAY_POINTER_EXT': ['GetPointervPName'],
 'GL_TEXTURE_COORD_ARRAY_SIZE': ['GetPName'],
 'GL_TEXTURE_COORD_ARRAY_STRIDE': ['GetPName'],
 'GL_TEXTURE_COORD_ARRAY_TYPE': ['GetPName'],
 'GL_TEXTURE_CUBE_MAP': ['TextureTarget', 'CopyImageSubDataTarget'],
 'GL_TEXTURE_CUBE_MAP_ARRAY': ['TextureTarget', 'CopyImageSubDataTarget'],
 'GL_TEXTURE_CUBE_MAP_ARRAY_ARB': ['TextureTarget'],
 'GL_TEXTURE_CUBE_MAP_ARRAY_EXT': ['TextureTarget'],
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X': ['TextureTarget'],
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y': ['TextureTarget'],
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z': ['TextureTarget'],
 'GL_TEXTURE_CUBE_MAP_POSITIVE_X': ['TextureTarget'],
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y': ['TextureTarget'],
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z': ['TextureTarget'],
 'GL_TEXTURE_CUBE_MAP_SEAMLESS': ['EnableCap'],
 'GL_TEXTURE_DEPTH_EXT': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_ENV_COLOR': ['TextureEnvParameter'],
 'GL_TEXTURE_ENV_MODE': ['TextureEnvParameter'],
 'GL_TEXTURE_FETCH_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_TEXTURE_FETCH_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_TEXTURE_GATHER': ['InternalFormatPName'],
 'GL_TEXTURE_GATHER_SHADOW': ['InternalFormatPName'],
 'GL_TEXTURE_GEN_MODE': ['TextureGenParameter'],
 'GL_TEXTURE_GEN_Q': ['EnableCap', 'GetPName'],
 'GL_TEXTURE_GEN_R': ['EnableCap', 'GetPName'],
 'GL_TEXTURE_GEN_S': ['EnableCap', 'GetPName'],
 'GL_TEXTURE_GEN_T': ['EnableCap', 'GetPName'],
 'GL_TEXTURE_GREEN_SIZE': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_HEIGHT': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_IMAGE_FORMAT': ['InternalFormatPName'],
 'GL_TEXTURE_IMAGE_TYPE': ['InternalFormatPName'],
 'GL_TEXTURE_INTENSITY_SIZE': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_INTERNAL_FORMAT': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_LOD_BIAS': ['TextureParameterName'],
 'GL_TEXTURE_LUMINANCE_SIZE': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_MAG_FILTER': ['GetTextureParameter',
                           'TextureParameterName',
                           'SamplerParameterI'],
 'GL_TEXTURE_MATRIX': ['VertexShaderTextureUnitParameter', 'GetPName'],
 'GL_TEXTURE_MAX_ANISOTROPY': ['SamplerParameterF'],
 'GL_TEXTURE_MAX_LEVEL': ['TextureParameterName'],
 'GL_TEXTURE_MAX_LOD': ['TextureParameterName', 'SamplerParameterF'],
 'GL_TEXTURE_MIN_FILTER': ['GetTextureParameter',
                           'TextureParameterName',
                           'SamplerParameterI'],
 'GL_TEXTURE_MIN_LOD': ['TextureParameterName', 'SamplerParameterF'],
 'GL_TEXTURE_PRIORITY': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_PRIORITY_EXT': ['TextureParameterName'],
 'GL_TEXTURE_RECTANGLE': ['TextureTarget', 'CopyImageSubDataTarget'],
 'GL_TEXTURE_RED_SIZE': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_RESIDENT': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_SHADOW': ['InternalFormatPName'],
 'GL_TEXTURE_STACK_DEPTH': ['GetPName'],
 'GL_TEXTURE_SWIZZLE_A': ['TextureParameterName'],
 'GL_TEXTURE_SWIZZLE_B': ['TextureParameterName'],
 'GL_TEXTURE_SWIZZLE_G': ['TextureParameterName'],
 'GL_TEXTURE_SWIZZLE_R': ['TextureParameterName'],
 'GL_TEXTURE_SWIZZLE_RGBA': ['TextureParameterName'],
 'GL_TEXTURE_TILING_EXT': ['TextureParameterName'],
 'GL_TEXTURE_TOO_LARGE_EXT': ['ErrorCode'],
 'GL_TEXTURE_UPDATE_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_TEXTURE_UPDATE_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_TEXTURE_VIEW': ['InternalFormatPName'],
 'GL_TEXTURE_WIDTH': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_WRAP_R': ['TextureParameterName', 'SamplerParameterI'],
 'GL_TEXTURE_WRAP_R_EXT': ['GetTextureParameter', 'TextureParameterName'],
 'GL_TEXTURE_WRAP_S': ['GetTextureParameter',
                       'TextureParameterName',
                       'SamplerParameterI'],
 'GL_TEXTURE_WRAP_T': ['GetTextureParameter',
                       'TextureParameterName',
                       'SamplerParameterI'],
 'GL_TEXT_FRAGMENT_SHADER': ['ProgramTarget'],
 'GL_TIMEOUT_EXPIRED': ['SyncStatus'],
 'GL_TIMESTAMP': ['GetPName', 'QueryCounterTarget'],
 'GL_TIME_ELAPSED': ['QueryTarget'],
 'GL_TOP_LEVEL_ARRAY_SIZE': ['ProgramResourceProperty'],
 'GL_TOP_LEVEL_ARRAY_STRIDE': ['ProgramResourceProperty'],
 'GL_TRANSFORM_BIT': ['AttribMask'],
 'GL_TRANSFORM_FEEDBACK': ['BindTransformFeedbackTarget', 'ObjectIdentifier'],
 'GL_TRANSFORM_FEEDBACK_ACTIVE': ['TransformFeedbackPName'],
 'GL_TRANSFORM_FEEDBACK_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_TRANSFORM_FEEDBACK_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_TRANSFORM_FEEDBACK_BUFFER': ['BufferTargetARB',
                                  'BufferStorageTarget',
                                  'CopyBufferSubDataTarget',
                                  'ProgramInterface'],
 'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING': ['GetPName', 'TransformFeedbackPName'],
 'GL_TRANSFORM_FEEDBACK_BUFFER_INDEX': ['ProgramResourceProperty'],
 'GL_TRANSFORM_FEEDBACK_BUFFER_MODE': ['ProgramPropertyARB'],
 'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE': ['GetPName', 'TransformFeedbackPName'],
 'GL_TRANSFORM_FEEDBACK_BUFFER_START': ['GetPName', 'TransformFeedbackPName'],
 'GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE': ['ProgramResourceProperty'],
 'GL_TRANSFORM_FEEDBACK_OVERFLOW': ['QueryTarget'],
 'GL_TRANSFORM_FEEDBACK_PAUSED': ['TransformFeedbackPName'],
 'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN': ['QueryTarget'],
 'GL_TRANSFORM_FEEDBACK_VARYING': ['ProgramInterface'],
 'GL_TRANSFORM_FEEDBACK_VARYINGS': ['ProgramPropertyARB'],
 'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH': ['ProgramPropertyARB'],
 'GL_TRIANGLES': ['PrimitiveType'],
 'GL_TRIANGLES_ADJACENCY': ['PrimitiveType'],
 'GL_TRIANGLES_ADJACENCY_ARB': ['PrimitiveType'],
 'GL_TRIANGLES_ADJACENCY_EXT': ['PrimitiveType'],
 'GL_TRIANGLE_FAN': ['PrimitiveType'],
 'GL_TRIANGLE_STRIP': ['PrimitiveType'],
 'GL_TRIANGLE_STRIP_ADJACENCY': ['PrimitiveType'],
 'GL_TRIANGLE_STRIP_ADJACENCY_ARB': ['PrimitiveType'],
 'GL_TRIANGLE_STRIP_ADJACENCY_EXT': ['PrimitiveType'],
 'GL_TRUE': ['ClampColorModeARB', 'ClampColorModeARB', 'Boolean'],
 'GL_TRUE_EXT': ['VertexShaderWriteMaskEXT'],
 'GL_TYPE': ['ProgramResourceProperty'],
 'GL_UNIFORM': ['ProgramInterface', 'ProgramResourceProperty'],
 'GL_UNIFORM_ARRAY_STRIDE': ['UniformPName'],
 'GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX': ['UniformPName'],
 'GL_UNIFORM_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_UNIFORM_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_UNIFORM_BLOCK': ['ProgramInterface'],
 'GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_BINDING': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_DATA_SIZE': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_INDEX': ['UniformPName'],
 'GL_UNIFORM_BLOCK_NAME_LENGTH': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER': ['UniformBlockPName'],
 'GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER': ['UniformBlockPName'],
 'GL_UNIFORM_BUFFER': ['BufferTargetARB',
                       'BufferStorageTarget',
                       'CopyBufferSubDataTarget'],
 'GL_UNIFORM_BUFFER_BINDING': ['GetPName'],
 'GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT': ['GetPName'],
 'GL_UNIFORM_BUFFER_SIZE': ['GetPName'],
 'GL_UNIFORM_BUFFER_START': ['GetPName'],
 'GL_UNIFORM_IS_ROW_MAJOR': ['UniformPName'],
 'GL_UNIFORM_MATRIX_STRIDE': ['UniformPName'],
 'GL_UNIFORM_NAME_LENGTH': ['UniformPName', 'SubroutineParameterName'],
 'GL_UNIFORM_OFFSET': ['UniformPName'],
 'GL_UNIFORM_SIZE': ['UniformPName', 'SubroutineParameterName'],
 'GL_UNIFORM_TYPE': ['UniformPName'],
 'GL_UNKNOWN_CONTEXT_RESET': ['GraphicsResetStatus'],
 'GL_UNPACK_ALIGNMENT': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_CMYK_HINT_EXT': ['GetPName', 'HintTarget'],
 'GL_UNPACK_IMAGE_HEIGHT': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_IMAGE_HEIGHT_EXT': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_LSB_FIRST': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_RESAMPLE_OML': ['PixelStoreParameter'],
 'GL_UNPACK_ROW_LENGTH': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_ROW_LENGTH_EXT': ['PixelStoreParameter'],
 'GL_UNPACK_SKIP_IMAGES': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_SKIP_IMAGES_EXT': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_SKIP_PIXELS': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_SKIP_PIXELS_EXT': ['PixelStoreParameter'],
 'GL_UNPACK_SKIP_ROWS': ['GetPName', 'PixelStoreParameter'],
 'GL_UNPACK_SKIP_ROWS_EXT': ['PixelStoreParameter'],
 'GL_UNPACK_SWAP_BYTES': ['GetPName', 'PixelStoreParameter'],
 'GL_UNSIGNED_BYTE': ['ScalarType',
                      'ColorPointerType',
                      'DrawElementsType',
                      'ListNameType',
                      'PixelType',
                      'VertexAttribType',
                      'VertexAttribPointerType',
                      'VertexAttribIType'],
 'GL_UNSIGNED_BYTE_3_3_2': ['PixelType'],
 'GL_UNSIGNED_BYTE_3_3_2_EXT': ['PixelType'],
 'GL_UNSIGNED_BYTE_ARB': ['MatrixIndexPointerTypeARB', 'WeightPointerTypeARB'],
 'GL_UNSIGNED_INT': ['ScalarType',
                     'ColorPointerType',
                     'DrawElementsType',
                     'ListNameType',
                     'PixelFormat',
                     'PixelType',
                     'VertexAttribType',
                     'UniformType',
                     'VertexAttribPointerType',
                     'GlslTypeToken',
                     'VertexAttribIType'],
 'GL_UNSIGNED_INT_10F_11F_11F_REV': ['VertexAttribType',
                                     'VertexAttribPointerType'],
 'GL_UNSIGNED_INT_10_10_10_2': ['PixelType'],
 'GL_UNSIGNED_INT_10_10_10_2_EXT': ['PixelType'],
 'GL_UNSIGNED_INT_2_10_10_10_REV': ['VertexAttribType',
                                    'VertexAttribPointerType'],
 'GL_UNSIGNED_INT_8_8_8_8': ['PixelType'],
 'GL_UNSIGNED_INT_8_8_8_8_EXT': ['PixelType'],
 'GL_UNSIGNED_INT_ARB': ['MatrixIndexPointerTypeARB', 'WeightPointerTypeARB'],
 'GL_UNSIGNED_INT_ATOMIC_COUNTER': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_1D': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_1D_ARRAY': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_2D': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_2D_ARRAY': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_2D_RECT': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_3D': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_BUFFER': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_CUBE': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY': ['GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_1D': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_2D': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY': ['UniformType',
                                                  'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_2D_RECT': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_3D': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_BUFFER': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_CUBE': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_VEC2': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_VEC3': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_INT_VEC4': ['UniformType', 'GlslTypeToken'],
 'GL_UNSIGNED_SHORT': ['ScalarType',
                       'ColorPointerType',
                       'DrawElementsType',
                       'ListNameType',
                       'PixelFormat',
                       'PixelType',
                       'VertexAttribType',
                       'VertexAttribPointerType',
                       'VertexAttribIType'],
 'GL_UNSIGNED_SHORT_4_4_4_4': ['PixelType'],
 'GL_UNSIGNED_SHORT_4_4_4_4_EXT': ['PixelType'],
 'GL_UNSIGNED_SHORT_5_5_5_1': ['PixelType'],
 'GL_UNSIGNED_SHORT_5_5_5_1_EXT': ['PixelType'],
 'GL_UNSIGNED_SHORT_ARB': ['MatrixIndexPointerTypeARB', 'WeightPointerTypeARB'],
 'GL_UPPER_LEFT': ['ClipControlOrigin'],
 'GL_V2F': ['InterleavedArrayFormat'],
 'GL_V3F': ['InterleavedArrayFormat'],
 'GL_VALIDATE_STATUS': ['ProgramPropertyARB'],
 'GL_VARIANT_ARRAY_EXT': ['VariantCapEXT'],
 'GL_VARIANT_ARRAY_STRIDE_EXT': ['GetVariantValueEXT'],
 'GL_VARIANT_ARRAY_TYPE_EXT': ['GetVariantValueEXT'],
 'GL_VARIANT_DATATYPE_EXT': ['GetVariantValueEXT'],
 'GL_VARIANT_EXT': ['VertexShaderStorageTypeEXT'],
 'GL_VARIANT_VALUE_EXT': ['GetVariantValueEXT'],
 'GL_VECTOR_EXT': ['DataTypeEXT'],
 'GL_VENDOR': ['StringName'],
 'GL_VERSION': ['StringName'],
 'GL_VERTEX_ARRAY': ['EnableCap', 'GetPName', 'ObjectIdentifier'],
 'GL_VERTEX_ARRAY_BINDING': ['GetPName'],
 'GL_VERTEX_ARRAY_COUNT_EXT': ['GetPName'],
 'GL_VERTEX_ARRAY_POINTER': ['GetPointervPName'],
 'GL_VERTEX_ARRAY_POINTER_EXT': ['GetPointervPName'],
 'GL_VERTEX_ARRAY_SIZE': ['GetPName'],
 'GL_VERTEX_ARRAY_STRIDE': ['GetPName'],
 'GL_VERTEX_ARRAY_TYPE': ['GetPName'],
 'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT': ['MemoryBarrierMask'],
 'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT_EXT': ['MemoryBarrierMask'],
 'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING': ['VertexAttribPropertyARB',
                                           'VertexAttribEnum'],
 'GL_VERTEX_ATTRIB_ARRAY_DIVISOR': ['VertexAttribPropertyARB',
                                    'VertexArrayPName',
                                    'VertexAttribEnum'],
 'GL_VERTEX_ATTRIB_ARRAY_ENABLED': ['VertexAttribPropertyARB',
                                    'VertexArrayPName',
                                    'VertexAttribEnum'],
 'GL_VERTEX_ATTRIB_ARRAY_INTEGER': ['VertexAttribPropertyARB',
                                    'VertexArrayPName',
                                    'VertexAttribEnum'],
 'GL_VERTEX_ATTRIB_ARRAY_INTEGER_EXT': ['VertexAttribPropertyARB'],
 'GL_VERTEX_ATTRIB_ARRAY_LONG': ['VertexAttribPropertyARB', 'VertexArrayPName'],
 'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED': ['VertexAttribPropertyARB',
                                       'VertexArrayPName',
                                       'VertexAttribEnum'],
 'GL_VERTEX_ATTRIB_ARRAY_POINTER': ['VertexAttribPointerPropertyARB'],
 'GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB': ['VertexAttribPointerPropertyARB'],
 'GL_VERTEX_ATTRIB_ARRAY_SIZE': ['VertexAttribPropertyARB',
                                 'VertexArrayPName',
                                 'VertexAttribEnum'],
 'GL_VERTEX_ATTRIB_ARRAY_STRIDE': ['VertexAttribPropertyARB',
                                   'VertexArrayPName',
                                   'VertexAttribEnum'],
 'GL_VERTEX_ATTRIB_ARRAY_TYPE': ['VertexAttribPropertyARB',
                                 'VertexArrayPName',
                                 'VertexAttribEnum'],
 'GL_VERTEX_ATTRIB_BINDING': ['VertexAttribPropertyARB'],
 'GL_VERTEX_ATTRIB_RELATIVE_OFFSET': ['VertexAttribPropertyARB',
                                      'VertexArrayPName'],
 'GL_VERTEX_BINDING_DIVISOR': ['GetPName'],
 'GL_VERTEX_BINDING_OFFSET': ['GetPName'],
 'GL_VERTEX_BINDING_STRIDE': ['GetPName'],
 'GL_VERTEX_SHADER': ['ShaderType', 'PipelineParameterName'],
 'GL_VERTEX_SHADER_ARB': ['ShaderType'],
 'GL_VERTEX_SHADER_BIT': ['UseProgramStageMask'],
 'GL_VERTEX_SHADER_BIT_EXT': ['UseProgramStageMask'],
 'GL_VERTEX_SHADER_INVOCATIONS': ['QueryTarget'],
 'GL_VERTEX_SUBROUTINE': ['ProgramInterface'],
 'GL_VERTEX_SUBROUTINE_UNIFORM': ['ProgramInterface'],
 'GL_VERTEX_TEXTURE': ['InternalFormatPName'],
 'GL_VERTICES_SUBMITTED': ['QueryTarget'],
 'GL_VIEWPORT': ['GetPName'],
 'GL_VIEWPORT_BIT': ['AttribMask'],
 'GL_VIEWPORT_BOUNDS_RANGE': ['GetPName'],
 'GL_VIEWPORT_INDEX_PROVOKING_VERTEX': ['GetPName'],
 'GL_VIEWPORT_SUBPIXEL_BITS': ['GetPName'],
 'GL_VIEW_COMPATIBILITY_CLASS': ['InternalFormatPName'],
 'GL_WAIT_FAILED': ['SyncStatus'],
 'GL_WRITE_ONLY': ['BufferAccessARB'],
 'GL_W_EXT': ['VertexShaderCoordOutEXT'],
 'GL_XOR': ['LogicOp'],
 'GL_X_EXT': ['VertexShaderCoordOutEXT'],
 'GL_Y_EXT': ['VertexShaderCoordOutEXT'],
 'GL_ZERO': ['StencilOp', 'BlendingFactor', 'TextureSwizzle'],
 'GL_ZERO_EXT': ['VertexShaderCoordOutEXT'],
 'GL_ZERO_TO_ONE': ['ClipControlDepth'],
 'GL_ZOOM_X': ['GetPName'],
 'GL_ZOOM_Y': ['GetPName'],
 'GL_Z_EXT': ['VertexShaderCoordOutEXT']}
glvalues= {'GL_1PASS_EXT': 32929,
 'GL_2D': 1536,
 'GL_2PASS_0_EXT': 32930,
 'GL_2PASS_1_EXT': 32931,
 'GL_2_BYTES': 5127,
 'GL_3D': 1537,
 'GL_3D_COLOR': 1538,
 'GL_3D_COLOR_TEXTURE': 1539,
 'GL_3_BYTES': 5128,
 'GL_422_AVERAGE_EXT': 32974,
 'GL_422_EXT': 32972,
 'GL_422_REV_AVERAGE_EXT': 32975,
 'GL_422_REV_EXT': 32973,
 'GL_4D_COLOR_TEXTURE': 1540,
 'GL_4PASS_0_EXT': 32932,
 'GL_4PASS_1_EXT': 32933,
 'GL_4PASS_2_EXT': 32934,
 'GL_4PASS_3_EXT': 32935,
 'GL_4_BYTES': 5129,
 'GL_ABGR_EXT': 32768,
 'GL_ACCUM': 256,
 'GL_ACCUM_ALPHA_BITS': 3419,
 'GL_ACCUM_BLUE_BITS': 3418,
 'GL_ACCUM_BUFFER_BIT': 512,
 'GL_ACCUM_CLEAR_VALUE': 2944,
 'GL_ACCUM_GREEN_BITS': 3417,
 'GL_ACCUM_RED_BITS': 3416,
 'GL_ACTIVE_ATOMIC_COUNTER_BUFFERS': 37593,
 'GL_ACTIVE_ATTRIBUTES': 35721,
 'GL_ACTIVE_ATTRIBUTE_MAX_LENGTH': 35722,
 'GL_ACTIVE_PROGRAM': 33369,
 'GL_ACTIVE_PROGRAM_EXT': 35725,
 'GL_ACTIVE_RESOURCES': 37621,
 'GL_ACTIVE_STENCIL_FACE_EXT': 35089,
 'GL_ACTIVE_SUBROUTINES': 36325,
 'GL_ACTIVE_SUBROUTINE_MAX_LENGTH': 36424,
 'GL_ACTIVE_SUBROUTINE_UNIFORMS': 36326,
 'GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS': 36423,
 'GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH': 36425,
 'GL_ACTIVE_TEXTURE': 34016,
 'GL_ACTIVE_TEXTURE_ARB': 34016,
 'GL_ACTIVE_UNIFORMS': 35718,
 'GL_ACTIVE_UNIFORM_BLOCKS': 35382,
 'GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH': 35381,
 'GL_ACTIVE_UNIFORM_MAX_LENGTH': 35719,
 'GL_ACTIVE_VARIABLES': 37637,
 'GL_ACTIVE_VERTEX_UNITS_ARB': 34469,
 'GL_ADD': 260,
 'GL_ADD_BLEND_IMG': 35849,
 'GL_ADD_SIGNED': 34164,
 'GL_ADD_SIGNED_ARB': 34164,
 'GL_ADD_SIGNED_EXT': 34164,
 'GL_ALIASED_LINE_WIDTH_RANGE': 33902,
 'GL_ALIASED_POINT_SIZE_RANGE': 33901,
 'GL_ALL_ATTRIB_BITS': 4294967295,
 'GL_ALL_BARRIER_BITS': 4294967295,
 'GL_ALL_BARRIER_BITS_EXT': 4294967295,
 'GL_ALL_SHADER_BITS': 4294967295,
 'GL_ALL_SHADER_BITS_EXT': 4294967295,
 'GL_ALPHA': 6406,
 'GL_ALPHA12': 32829,
 'GL_ALPHA12_EXT': 32829,
 'GL_ALPHA16': 32830,
 'GL_ALPHA16F_ARB': 34844,
 'GL_ALPHA16F_EXT': 34844,
 'GL_ALPHA16I_EXT': 36234,
 'GL_ALPHA16UI_EXT': 36216,
 'GL_ALPHA16_EXT': 32830,
 'GL_ALPHA16_SNORM': 36888,
 'GL_ALPHA32F_ARB': 34838,
 'GL_ALPHA32F_EXT': 34838,
 'GL_ALPHA32I_EXT': 36228,
 'GL_ALPHA32UI_EXT': 36210,
 'GL_ALPHA4': 32827,
 'GL_ALPHA4_EXT': 32827,
 'GL_ALPHA8': 32828,
 'GL_ALPHA8I_EXT': 36240,
 'GL_ALPHA8UI_EXT': 36222,
 'GL_ALPHA8_EXT': 32828,
 'GL_ALPHA8_SNORM': 36884,
 'GL_ALPHA_BIAS': 3357,
 'GL_ALPHA_BITS': 3413,
 'GL_ALPHA_INTEGER': 36247,
 'GL_ALPHA_INTEGER_EXT': 36247,
 'GL_ALPHA_MAX_CLAMP_INGR': 34151,
 'GL_ALPHA_MIN_CLAMP_INGR': 34147,
 'GL_ALPHA_SCALE': 3356,
 'GL_ALPHA_SNORM': 36880,
 'GL_ALPHA_TEST': 3008,
 'GL_ALPHA_TEST_FUNC': 3009,
 'GL_ALPHA_TEST_REF': 3010,
 'GL_ALREADY_SIGNALED': 37146,
 'GL_ALWAYS': 519,
 'GL_AMBIENT': 4608,
 'GL_AMBIENT_AND_DIFFUSE': 5634,
 'GL_AND': 5377,
 'GL_AND_INVERTED': 5380,
 'GL_AND_REVERSE': 5378,
 'GL_ANY_SAMPLES_PASSED': 35887,
 'GL_ANY_SAMPLES_PASSED_CONSERVATIVE': 36202,
 'GL_ANY_SAMPLES_PASSED_CONSERVATIVE_EXT': 36202,
 'GL_ANY_SAMPLES_PASSED_EXT': 35887,
 'GL_ARRAY_BUFFER': 34962,
 'GL_ARRAY_BUFFER_ARB': 34962,
 'GL_ARRAY_BUFFER_BINDING': 34964,
 'GL_ARRAY_BUFFER_BINDING_ARB': 34964,
 'GL_ARRAY_ELEMENT_LOCK_COUNT_EXT': 33193,
 'GL_ARRAY_ELEMENT_LOCK_FIRST_EXT': 33192,
 'GL_ARRAY_SIZE': 37627,
 'GL_ARRAY_STRIDE': 37630,
 'GL_ATOMIC_COUNTER_BARRIER_BIT': 4096,
 'GL_ATOMIC_COUNTER_BARRIER_BIT_EXT': 4096,
 'GL_ATOMIC_COUNTER_BUFFER': 37568,
 'GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS': 37573,
 'GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES': 37574,
 'GL_ATOMIC_COUNTER_BUFFER_BINDING': 37569,
 'GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE': 37572,
 'GL_ATOMIC_COUNTER_BUFFER_INDEX': 37633,
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER': 37101,
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER': 37579,
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER': 37578,
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER': 37576,
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER': 37577,
 'GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER': 37575,
 'GL_ATOMIC_COUNTER_BUFFER_SIZE': 37571,
 'GL_ATOMIC_COUNTER_BUFFER_START': 37570,
 'GL_ATTACHED_SHADERS': 35717,
 'GL_ATTENUATION_EXT': 33613,
 'GL_ATTRIB_STACK_DEPTH': 2992,
 'GL_AUTO_GENERATE_MIPMAP': 33429,
 'GL_AUTO_NORMAL': 3456,
 'GL_AUX0': 1033,
 'GL_AUX1': 1034,
 'GL_AUX2': 1035,
 'GL_AUX3': 1036,
 'GL_AUX_BUFFERS': 3072,
 'GL_AVERAGE_EXT': 33589,
 'GL_AVERAGE_HP': 33120,
 'GL_BACK': 1029,
 'GL_BACK_LEFT': 1026,
 'GL_BACK_RIGHT': 1027,
 'GL_BGR': 32992,
 'GL_BGRA': 32993,
 'GL_BGRA8_EXT': 37793,
 'GL_BGRA_EXT': 32993,
 'GL_BGRA_IMG': 32993,
 'GL_BGRA_INTEGER': 36251,
 'GL_BGRA_INTEGER_EXT': 36251,
 'GL_BGR_EXT': 32992,
 'GL_BGR_INTEGER': 36250,
 'GL_BGR_INTEGER_EXT': 36250,
 'GL_BINORMAL_ARRAY_EXT': 33850,
 'GL_BINORMAL_ARRAY_POINTER_EXT': 33859,
 'GL_BINORMAL_ARRAY_STRIDE_EXT': 33857,
 'GL_BINORMAL_ARRAY_TYPE_EXT': 33856,
 'GL_BITMAP': 6656,
 'GL_BITMAP_TOKEN': 1796,
 'GL_BLEND': 3042,
 'GL_BLEND_COLOR': 32773,
 'GL_BLEND_COLOR_EXT': 32773,
 'GL_BLEND_DST': 3040,
 'GL_BLEND_DST_ALPHA': 32970,
 'GL_BLEND_DST_ALPHA_EXT': 32970,
 'GL_BLEND_DST_RGB': 32968,
 'GL_BLEND_DST_RGB_EXT': 32968,
 'GL_BLEND_EQUATION': 32777,
 'GL_BLEND_EQUATION_ALPHA': 34877,
 'GL_BLEND_EQUATION_ALPHA_EXT': 34877,
 'GL_BLEND_EQUATION_EXT': 32777,
 'GL_BLEND_EQUATION_RGB': 32777,
 'GL_BLEND_EQUATION_RGB_EXT': 32777,
 'GL_BLEND_SRC': 3041,
 'GL_BLEND_SRC_ALPHA': 32971,
 'GL_BLEND_SRC_ALPHA_EXT': 32971,
 'GL_BLEND_SRC_RGB': 32969,
 'GL_BLEND_SRC_RGB_EXT': 32969,
 'GL_BLOCK_INDEX': 37629,
 'GL_BLUE': 6405,
 'GL_BLUE_BIAS': 3355,
 'GL_BLUE_BITS': 3412,
 'GL_BLUE_INTEGER': 36246,
 'GL_BLUE_INTEGER_EXT': 36246,
 'GL_BLUE_MAX_CLAMP_INGR': 34150,
 'GL_BLUE_MIN_CLAMP_INGR': 34146,
 'GL_BLUE_SCALE': 3354,
 'GL_BOOL': 35670,
 'GL_BOOL_ARB': 35670,
 'GL_BOOL_VEC2': 35671,
 'GL_BOOL_VEC2_ARB': 35671,
 'GL_BOOL_VEC3': 35672,
 'GL_BOOL_VEC3_ARB': 35672,
 'GL_BOOL_VEC4': 35673,
 'GL_BOOL_VEC4_ARB': 35673,
 'GL_BROWSER_DEFAULT_WEBGL': 37444,
 'GL_BUFFER': 33504,
 'GL_BUFFER_ACCESS': 35003,
 'GL_BUFFER_ACCESS_ARB': 35003,
 'GL_BUFFER_ACCESS_FLAGS': 37151,
 'GL_BUFFER_BINDING': 37634,
 'GL_BUFFER_DATA_SIZE': 37635,
 'GL_BUFFER_IMMUTABLE_STORAGE': 33311,
 'GL_BUFFER_IMMUTABLE_STORAGE_EXT': 33311,
 'GL_BUFFER_MAPPED': 35004,
 'GL_BUFFER_MAPPED_ARB': 35004,
 'GL_BUFFER_MAP_LENGTH': 37152,
 'GL_BUFFER_MAP_OFFSET': 37153,
 'GL_BUFFER_MAP_POINTER': 35005,
 'GL_BUFFER_MAP_POINTER_ARB': 35005,
 'GL_BUFFER_OBJECT_EXT': 37201,
 'GL_BUFFER_SIZE': 34660,
 'GL_BUFFER_SIZE_ARB': 34660,
 'GL_BUFFER_STORAGE_FLAGS': 33312,
 'GL_BUFFER_STORAGE_FLAGS_EXT': 33312,
 'GL_BUFFER_UPDATE_BARRIER_BIT': 512,
 'GL_BUFFER_UPDATE_BARRIER_BIT_EXT': 512,
 'GL_BUFFER_USAGE': 34661,
 'GL_BUFFER_USAGE_ARB': 34661,
 'GL_BUFFER_VARIABLE': 37605,
 'GL_BYTE': 5120,
 'GL_C3F_V3F': 10788,
 'GL_C4F_N3F_V3F': 10790,
 'GL_C4UB_V2F': 10786,
 'GL_C4UB_V3F': 10787,
 'GL_CAVEAT_SUPPORT': 33464,
 'GL_CCW': 2305,
 'GL_CLAMP': 10496,
 'GL_CLAMP_FRAGMENT_COLOR': 35099,
 'GL_CLAMP_FRAGMENT_COLOR_ARB': 35099,
 'GL_CLAMP_READ_COLOR': 35100,
 'GL_CLAMP_READ_COLOR_ARB': 35100,
 'GL_CLAMP_TO_BORDER': 33069,
 'GL_CLAMP_TO_BORDER_ARB': 33069,
 'GL_CLAMP_TO_BORDER_EXT': 33069,
 'GL_CLAMP_TO_EDGE': 33071,
 'GL_CLAMP_VERTEX_COLOR': 35098,
 'GL_CLAMP_VERTEX_COLOR_ARB': 35098,
 'GL_CLEAR': 5376,
 'GL_CLEAR_BUFFER': 33460,
 'GL_CLEAR_TEXTURE': 37733,
 'GL_CLIENT_ACTIVE_TEXTURE': 34017,
 'GL_CLIENT_ACTIVE_TEXTURE_ARB': 34017,
 'GL_CLIENT_ALL_ATTRIB_BITS': 4294967295,
 'GL_CLIENT_ATTRIB_STACK_DEPTH': 2993,
 'GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT': 16384,
 'GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT_EXT': 16384,
 'GL_CLIENT_PIXEL_STORE_BIT': 1,
 'GL_CLIENT_STORAGE_BIT': 512,
 'GL_CLIENT_STORAGE_BIT_EXT': 512,
 'GL_CLIENT_VERTEX_ARRAY_BIT': 2,
 'GL_CLIPPING_INPUT_PRIMITIVES': 33526,
 'GL_CLIPPING_INPUT_PRIMITIVES_ARB': 33526,
 'GL_CLIPPING_OUTPUT_PRIMITIVES': 33527,
 'GL_CLIPPING_OUTPUT_PRIMITIVES_ARB': 33527,
 'GL_CLIP_DEPTH_MODE': 37725,
 'GL_CLIP_DEPTH_MODE_EXT': 37725,
 'GL_CLIP_DISTANCE0': 12288,
 'GL_CLIP_DISTANCE0_EXT': 12288,
 'GL_CLIP_DISTANCE1': 12289,
 'GL_CLIP_DISTANCE1_EXT': 12289,
 'GL_CLIP_DISTANCE2': 12290,
 'GL_CLIP_DISTANCE2_EXT': 12290,
 'GL_CLIP_DISTANCE3': 12291,
 'GL_CLIP_DISTANCE3_EXT': 12291,
 'GL_CLIP_DISTANCE4': 12292,
 'GL_CLIP_DISTANCE4_EXT': 12292,
 'GL_CLIP_DISTANCE5': 12293,
 'GL_CLIP_DISTANCE5_EXT': 12293,
 'GL_CLIP_DISTANCE6': 12294,
 'GL_CLIP_DISTANCE6_EXT': 12294,
 'GL_CLIP_DISTANCE7': 12295,
 'GL_CLIP_DISTANCE7_EXT': 12295,
 'GL_CLIP_ORIGIN': 37724,
 'GL_CLIP_ORIGIN_EXT': 37724,
 'GL_CLIP_PLANE0': 12288,
 'GL_CLIP_PLANE0_IMG': 12288,
 'GL_CLIP_PLANE1': 12289,
 'GL_CLIP_PLANE1_IMG': 12289,
 'GL_CLIP_PLANE2': 12290,
 'GL_CLIP_PLANE2_IMG': 12290,
 'GL_CLIP_PLANE3': 12291,
 'GL_CLIP_PLANE3_IMG': 12291,
 'GL_CLIP_PLANE4': 12292,
 'GL_CLIP_PLANE4_IMG': 12292,
 'GL_CLIP_PLANE5': 12293,
 'GL_CLIP_PLANE5_IMG': 12293,
 'GL_CLIP_VOLUME_CLIPPING_HINT_EXT': 33008,
 'GL_CMYKA_EXT': 32781,
 'GL_CMYK_EXT': 32780,
 'GL_COEFF': 2560,
 'GL_COLOR': 6144,
 'GL_COLORBURN': 37530,
 'GL_COLORDODGE': 37529,
 'GL_COLOR_ARRAY': 32886,
 'GL_COLOR_ARRAY_BUFFER_BINDING': 34968,
 'GL_COLOR_ARRAY_BUFFER_BINDING_ARB': 34968,
 'GL_COLOR_ARRAY_COUNT_EXT': 32900,
 'GL_COLOR_ARRAY_EXT': 32886,
 'GL_COLOR_ARRAY_POINTER': 32912,
 'GL_COLOR_ARRAY_POINTER_EXT': 32912,
 'GL_COLOR_ARRAY_SIZE': 32897,
 'GL_COLOR_ARRAY_SIZE_EXT': 32897,
 'GL_COLOR_ARRAY_STRIDE': 32899,
 'GL_COLOR_ARRAY_STRIDE_EXT': 32899,
 'GL_COLOR_ARRAY_TYPE': 32898,
 'GL_COLOR_ARRAY_TYPE_EXT': 32898,
 'GL_COLOR_ATTACHMENT0': 36064,
 'GL_COLOR_ATTACHMENT0_EXT': 36064,
 'GL_COLOR_ATTACHMENT1': 36065,
 'GL_COLOR_ATTACHMENT10': 36074,
 'GL_COLOR_ATTACHMENT10_EXT': 36074,
 'GL_COLOR_ATTACHMENT11': 36075,
 'GL_COLOR_ATTACHMENT11_EXT': 36075,
 'GL_COLOR_ATTACHMENT12': 36076,
 'GL_COLOR_ATTACHMENT12_EXT': 36076,
 'GL_COLOR_ATTACHMENT13': 36077,
 'GL_COLOR_ATTACHMENT13_EXT': 36077,
 'GL_COLOR_ATTACHMENT14': 36078,
 'GL_COLOR_ATTACHMENT14_EXT': 36078,
 'GL_COLOR_ATTACHMENT15': 36079,
 'GL_COLOR_ATTACHMENT15_EXT': 36079,
 'GL_COLOR_ATTACHMENT16': 36080,
 'GL_COLOR_ATTACHMENT17': 36081,
 'GL_COLOR_ATTACHMENT18': 36082,
 'GL_COLOR_ATTACHMENT19': 36083,
 'GL_COLOR_ATTACHMENT1_EXT': 36065,
 'GL_COLOR_ATTACHMENT2': 36066,
 'GL_COLOR_ATTACHMENT20': 36084,
 'GL_COLOR_ATTACHMENT21': 36085,
 'GL_COLOR_ATTACHMENT22': 36086,
 'GL_COLOR_ATTACHMENT23': 36087,
 'GL_COLOR_ATTACHMENT24': 36088,
 'GL_COLOR_ATTACHMENT25': 36089,
 'GL_COLOR_ATTACHMENT26': 36090,
 'GL_COLOR_ATTACHMENT27': 36091,
 'GL_COLOR_ATTACHMENT28': 36092,
 'GL_COLOR_ATTACHMENT29': 36093,
 'GL_COLOR_ATTACHMENT2_EXT': 36066,
 'GL_COLOR_ATTACHMENT3': 36067,
 'GL_COLOR_ATTACHMENT30': 36094,
 'GL_COLOR_ATTACHMENT31': 36095,
 'GL_COLOR_ATTACHMENT3_EXT': 36067,
 'GL_COLOR_ATTACHMENT4': 36068,
 'GL_COLOR_ATTACHMENT4_EXT': 36068,
 'GL_COLOR_ATTACHMENT5': 36069,
 'GL_COLOR_ATTACHMENT5_EXT': 36069,
 'GL_COLOR_ATTACHMENT6': 36070,
 'GL_COLOR_ATTACHMENT6_EXT': 36070,
 'GL_COLOR_ATTACHMENT7': 36071,
 'GL_COLOR_ATTACHMENT7_EXT': 36071,
 'GL_COLOR_ATTACHMENT8': 36072,
 'GL_COLOR_ATTACHMENT8_EXT': 36072,
 'GL_COLOR_ATTACHMENT9': 36073,
 'GL_COLOR_ATTACHMENT9_EXT': 36073,
 'GL_COLOR_ATTACHMENT_EXT': 37104,
 'GL_COLOR_BUFFER_BIT': 16384,
 'GL_COLOR_CLEAR_VALUE': 3106,
 'GL_COLOR_COMPONENTS': 33411,
 'GL_COLOR_ENCODING': 33430,
 'GL_COLOR_EXT': 6144,
 'GL_COLOR_INDEX': 6400,
 'GL_COLOR_INDEX12_EXT': 32998,
 'GL_COLOR_INDEX16_EXT': 32999,
 'GL_COLOR_INDEX1_EXT': 32994,
 'GL_COLOR_INDEX2_EXT': 32995,
 'GL_COLOR_INDEX4_EXT': 32996,
 'GL_COLOR_INDEX8_EXT': 32997,
 'GL_COLOR_INDEXES': 5635,
 'GL_COLOR_LOGIC_OP': 3058,
 'GL_COLOR_MATERIAL': 2903,
 'GL_COLOR_MATERIAL_FACE': 2901,
 'GL_COLOR_MATERIAL_PARAMETER': 2902,
 'GL_COLOR_MATRIX': 32945,
 'GL_COLOR_MATRIX_STACK_DEPTH': 32946,
 'GL_COLOR_RENDERABLE': 33414,
 'GL_COLOR_SUM': 33880,
 'GL_COLOR_SUM_ARB': 33880,
 'GL_COLOR_SUM_EXT': 33880,
 'GL_COLOR_TABLE': 32976,
 'GL_COLOR_TABLE_ALPHA_SIZE': 32989,
 'GL_COLOR_TABLE_BIAS': 32983,
 'GL_COLOR_TABLE_BLUE_SIZE': 32988,
 'GL_COLOR_TABLE_FORMAT': 32984,
 'GL_COLOR_TABLE_GREEN_SIZE': 32987,
 'GL_COLOR_TABLE_INTENSITY_SIZE': 32991,
 'GL_COLOR_TABLE_LUMINANCE_SIZE': 32990,
 'GL_COLOR_TABLE_RED_SIZE': 32986,
 'GL_COLOR_TABLE_SCALE': 32982,
 'GL_COLOR_TABLE_WIDTH': 32985,
 'GL_COLOR_WRITEMASK': 3107,
 'GL_COMBINE': 34160,
 'GL_COMBINE_ALPHA': 34162,
 'GL_COMBINE_ALPHA_ARB': 34162,
 'GL_COMBINE_ALPHA_EXT': 34162,
 'GL_COMBINE_ARB': 34160,
 'GL_COMBINE_EXT': 34160,
 'GL_COMBINE_RGB': 34161,
 'GL_COMBINE_RGB_ARB': 34161,
 'GL_COMBINE_RGB_EXT': 34161,
 'GL_COMMAND_BARRIER_BIT': 64,
 'GL_COMMAND_BARRIER_BIT_EXT': 64,
 'GL_COMPARE_REF_DEPTH_TO_TEXTURE_EXT': 34894,
 'GL_COMPARE_REF_TO_TEXTURE': 34894,
 'GL_COMPARE_REF_TO_TEXTURE_EXT': 34894,
 'GL_COMPARE_R_TO_TEXTURE': 34894,
 'GL_COMPARE_R_TO_TEXTURE_ARB': 34894,
 'GL_COMPATIBLE_SUBROUTINES': 36427,
 'GL_COMPILE': 4864,
 'GL_COMPILE_AND_EXECUTE': 4865,
 'GL_COMPILE_STATUS': 35713,
 'GL_COMPLETION_STATUS_ARB': 37297,
 'GL_COMPRESSED_ALPHA': 34025,
 'GL_COMPRESSED_ALPHA_ARB': 34025,
 'GL_COMPRESSED_INTENSITY': 34028,
 'GL_COMPRESSED_INTENSITY_ARB': 34028,
 'GL_COMPRESSED_LUMINANCE': 34026,
 'GL_COMPRESSED_LUMINANCE_ALPHA': 34027,
 'GL_COMPRESSED_LUMINANCE_ALPHA_ARB': 34027,
 'GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT': 35954,
 'GL_COMPRESSED_LUMINANCE_ARB': 34026,
 'GL_COMPRESSED_LUMINANCE_LATC1_EXT': 35952,
 'GL_COMPRESSED_R11_EAC': 37488,
 'GL_COMPRESSED_RED': 33317,
 'GL_COMPRESSED_RED_GREEN_RGTC2_EXT': 36285,
 'GL_COMPRESSED_RED_RGTC1': 36283,
 'GL_COMPRESSED_RED_RGTC1_EXT': 36283,
 'GL_COMPRESSED_RG': 33318,
 'GL_COMPRESSED_RG11_EAC': 37490,
 'GL_COMPRESSED_RGB': 34029,
 'GL_COMPRESSED_RGB8_ETC2': 37492,
 'GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2': 37494,
 'GL_COMPRESSED_RGBA': 34030,
 'GL_COMPRESSED_RGBA8_ETC2_EAC': 37496,
 'GL_COMPRESSED_RGBA_ARB': 34030,
 'GL_COMPRESSED_RGBA_ASTC_10x10': 37819,
 'GL_COMPRESSED_RGBA_ASTC_10x5': 37816,
 'GL_COMPRESSED_RGBA_ASTC_10x6': 37817,
 'GL_COMPRESSED_RGBA_ASTC_10x8': 37818,
 'GL_COMPRESSED_RGBA_ASTC_12x10': 37820,
 'GL_COMPRESSED_RGBA_ASTC_12x12': 37821,
 'GL_COMPRESSED_RGBA_ASTC_4x4': 37808,
 'GL_COMPRESSED_RGBA_ASTC_5x4': 37809,
 'GL_COMPRESSED_RGBA_ASTC_5x5': 37810,
 'GL_COMPRESSED_RGBA_ASTC_6x5': 37811,
 'GL_COMPRESSED_RGBA_ASTC_6x6': 37812,
 'GL_COMPRESSED_RGBA_ASTC_8x5': 37813,
 'GL_COMPRESSED_RGBA_ASTC_8x6': 37814,
 'GL_COMPRESSED_RGBA_ASTC_8x8': 37815,
 'GL_COMPRESSED_RGBA_BPTC_UNORM': 36492,
 'GL_COMPRESSED_RGBA_BPTC_UNORM_ARB': 36492,
 'GL_COMPRESSED_RGBA_BPTC_UNORM_EXT': 36492,
 'GL_COMPRESSED_RGBA_FXT1_3DFX': 34481,
 'GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG': 35843,
 'GL_COMPRESSED_RGBA_PVRTC_2BPPV2_IMG': 37175,
 'GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG': 35842,
 'GL_COMPRESSED_RGBA_PVRTC_4BPPV2_IMG': 37176,
 'GL_COMPRESSED_RGBA_S3TC_DXT1_EXT': 33777,
 'GL_COMPRESSED_RGBA_S3TC_DXT3_ANGLE': 33778,
 'GL_COMPRESSED_RGBA_S3TC_DXT3_EXT': 33778,
 'GL_COMPRESSED_RGBA_S3TC_DXT5_ANGLE': 33779,
 'GL_COMPRESSED_RGBA_S3TC_DXT5_EXT': 33779,
 'GL_COMPRESSED_RGB_ARB': 34029,
 'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT': 36494,
 'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB': 36494,
 'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT': 36494,
 'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT': 36495,
 'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB': 36495,
 'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT': 36495,
 'GL_COMPRESSED_RGB_FXT1_3DFX': 34480,
 'GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG': 35841,
 'GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG': 35840,
 'GL_COMPRESSED_RGB_S3TC_DXT1_EXT': 33776,
 'GL_COMPRESSED_RG_RGTC2': 36285,
 'GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT': 35955,
 'GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT': 35953,
 'GL_COMPRESSED_SIGNED_R11_EAC': 37489,
 'GL_COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT': 36286,
 'GL_COMPRESSED_SIGNED_RED_RGTC1': 36284,
 'GL_COMPRESSED_SIGNED_RED_RGTC1_EXT': 36284,
 'GL_COMPRESSED_SIGNED_RG11_EAC': 37491,
 'GL_COMPRESSED_SIGNED_RG_RGTC2': 36286,
 'GL_COMPRESSED_SLUMINANCE': 35914,
 'GL_COMPRESSED_SLUMINANCE_ALPHA': 35915,
 'GL_COMPRESSED_SLUMINANCE_ALPHA_EXT': 35915,
 'GL_COMPRESSED_SLUMINANCE_EXT': 35914,
 'GL_COMPRESSED_SRGB': 35912,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10': 37851,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5': 37848,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6': 37849,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8': 37850,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10': 37852,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12': 37853,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4': 37840,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4': 37841,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5': 37842,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5': 37843,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6': 37844,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5': 37845,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6': 37846,
 'GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8': 37847,
 'GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC': 37497,
 'GL_COMPRESSED_SRGB8_ETC2': 37493,
 'GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2': 37495,
 'GL_COMPRESSED_SRGB_ALPHA': 35913,
 'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM': 36493,
 'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB': 36493,
 'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT': 36493,
 'GL_COMPRESSED_SRGB_ALPHA_EXT': 35913,
 'GL_COMPRESSED_SRGB_ALPHA_PVRTC_2BPPV1_EXT': 35414,
 'GL_COMPRESSED_SRGB_ALPHA_PVRTC_2BPPV2_IMG': 37872,
 'GL_COMPRESSED_SRGB_ALPHA_PVRTC_4BPPV1_EXT': 35415,
 'GL_COMPRESSED_SRGB_ALPHA_PVRTC_4BPPV2_IMG': 37873,
 'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT': 35917,
 'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT': 35918,
 'GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT': 35919,
 'GL_COMPRESSED_SRGB_EXT': 35912,
 'GL_COMPRESSED_SRGB_PVRTC_2BPPV1_EXT': 35412,
 'GL_COMPRESSED_SRGB_PVRTC_4BPPV1_EXT': 35413,
 'GL_COMPRESSED_SRGB_S3TC_DXT1_EXT': 35916,
 'GL_COMPRESSED_TEXTURE_FORMATS': 34467,
 'GL_COMPRESSED_TEXTURE_FORMATS_ARB': 34467,
 'GL_COMPUTE_SHADER': 37305,
 'GL_COMPUTE_SHADER_BIT': 32,
 'GL_COMPUTE_SHADER_INVOCATIONS': 33525,
 'GL_COMPUTE_SHADER_INVOCATIONS_ARB': 33525,
 'GL_COMPUTE_SUBROUTINE': 37613,
 'GL_COMPUTE_SUBROUTINE_UNIFORM': 37619,
 'GL_COMPUTE_TEXTURE': 33440,
 'GL_COMPUTE_WORK_GROUP_SIZE': 33383,
 'GL_CONDITION_SATISFIED': 37148,
 'GL_CONSTANT': 34166,
 'GL_CONSTANT_ALPHA': 32771,
 'GL_CONSTANT_ALPHA_EXT': 32771,
 'GL_CONSTANT_ARB': 34166,
 'GL_CONSTANT_ATTENUATION': 4615,
 'GL_CONSTANT_BORDER': 33105,
 'GL_CONSTANT_BORDER_HP': 33105,
 'GL_CONSTANT_COLOR': 32769,
 'GL_CONSTANT_COLOR_EXT': 32769,
 'GL_CONSTANT_EXT': 34166,
 'GL_CONTEXT_COMPATIBILITY_PROFILE_BIT': 2,
 'GL_CONTEXT_CORE_PROFILE_BIT': 1,
 'GL_CONTEXT_FLAGS': 33310,
 'GL_CONTEXT_FLAG_DEBUG_BIT': 2,
 'GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT': 1,
 'GL_CONTEXT_FLAG_NO_ERROR_BIT': 8,
 'GL_CONTEXT_FLAG_PROTECTED_CONTENT_BIT_EXT': 16,
 'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT': 4,
 'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB': 4,
 'GL_CONTEXT_LOST': 1287,
 'GL_CONTEXT_LOST_WEBGL': 37442,
 'GL_CONTEXT_PROFILE_MASK': 37158,
 'GL_CONTEXT_RELEASE_BEHAVIOR': 33531,
 'GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH': 33532,
 'GL_CONTEXT_ROBUST_ACCESS': 37107,
 'GL_CONTEXT_ROBUST_ACCESS_EXT': 37107,
 'GL_CONVOLUTION_1D': 32784,
 'GL_CONVOLUTION_1D_EXT': 32784,
 'GL_CONVOLUTION_2D': 32785,
 'GL_CONVOLUTION_2D_EXT': 32785,
 'GL_CONVOLUTION_BORDER_COLOR': 33108,
 'GL_CONVOLUTION_BORDER_COLOR_HP': 33108,
 'GL_CONVOLUTION_BORDER_MODE': 32787,
 'GL_CONVOLUTION_BORDER_MODE_EXT': 32787,
 'GL_CONVOLUTION_FILTER_BIAS': 32789,
 'GL_CONVOLUTION_FILTER_BIAS_EXT': 32789,
 'GL_CONVOLUTION_FILTER_SCALE': 32788,
 'GL_CONVOLUTION_FILTER_SCALE_EXT': 32788,
 'GL_CONVOLUTION_FORMAT': 32791,
 'GL_CONVOLUTION_FORMAT_EXT': 32791,
 'GL_CONVOLUTION_HEIGHT': 32793,
 'GL_CONVOLUTION_HEIGHT_EXT': 32793,
 'GL_CONVOLUTION_WIDTH': 32792,
 'GL_CONVOLUTION_WIDTH_EXT': 32792,
 'GL_COORD_REPLACE': 34914,
 'GL_COORD_REPLACE_ARB': 34914,
 'GL_COPY': 5379,
 'GL_COPY_INVERTED': 5388,
 'GL_COPY_PIXEL_TOKEN': 1798,
 'GL_COPY_READ_BUFFER': 36662,
 'GL_COPY_READ_BUFFER_BINDING': 36662,
 'GL_COPY_WRITE_BUFFER': 36663,
 'GL_COPY_WRITE_BUFFER_BINDING': 36663,
 'GL_CUBIC_EXT': 33588,
 'GL_CUBIC_HP': 33119,
 'GL_CUBIC_IMG': 37177,
 'GL_CUBIC_MIPMAP_LINEAR_IMG': 37179,
 'GL_CUBIC_MIPMAP_NEAREST_IMG': 37178,
 'GL_CULL_FACE': 2884,
 'GL_CULL_FACE_MODE': 2885,
 'GL_CULL_VERTEX_EXT': 33194,
 'GL_CULL_VERTEX_EYE_POSITION_EXT': 33195,
 'GL_CULL_VERTEX_OBJECT_POSITION_EXT': 33196,
 'GL_CURRENT_BINORMAL_EXT': 33852,
 'GL_CURRENT_BIT': 1,
 'GL_CURRENT_COLOR': 2816,
 'GL_CURRENT_FOG_COORD': 33875,
 'GL_CURRENT_FOG_COORDINATE': 33875,
 'GL_CURRENT_FOG_COORDINATE_EXT': 33875,
 'GL_CURRENT_INDEX': 2817,
 'GL_CURRENT_MATRIX_ARB': 34369,
 'GL_CURRENT_MATRIX_INDEX_ARB': 34885,
 'GL_CURRENT_MATRIX_STACK_DEPTH_ARB': 34368,
 'GL_CURRENT_NORMAL': 2818,
 'GL_CURRENT_PALETTE_MATRIX_ARB': 34883,
 'GL_CURRENT_PROGRAM': 35725,
 'GL_CURRENT_QUERY': 34917,
 'GL_CURRENT_QUERY_ARB': 34917,
 'GL_CURRENT_QUERY_EXT': 34917,
 'GL_CURRENT_RASTER_COLOR': 2820,
 'GL_CURRENT_RASTER_DISTANCE': 2825,
 'GL_CURRENT_RASTER_INDEX': 2821,
 'GL_CURRENT_RASTER_POSITION': 2823,
 'GL_CURRENT_RASTER_POSITION_VALID': 2824,
 'GL_CURRENT_RASTER_SECONDARY_COLOR': 33887,
 'GL_CURRENT_RASTER_TEXTURE_COORDS': 2822,
 'GL_CURRENT_SECONDARY_COLOR': 33881,
 'GL_CURRENT_SECONDARY_COLOR_EXT': 33881,
 'GL_CURRENT_TANGENT_EXT': 33851,
 'GL_CURRENT_TEXTURE_COORDS': 2819,
 'GL_CURRENT_VERTEX_ATTRIB': 34342,
 'GL_CURRENT_VERTEX_ATTRIB_ARB': 34342,
 'GL_CURRENT_VERTEX_EXT': 34786,
 'GL_CURRENT_VERTEX_WEIGHT_EXT': 34059,
 'GL_CURRENT_WEIGHT_ARB': 34472,
 'GL_CW': 2304,
 'GL_D3D12_FENCE_VALUE_EXT': 38293,
 'GL_DARKEN': 37527,
 'GL_DEBUG_CALLBACK_FUNCTION': 33348,
 'GL_DEBUG_CALLBACK_FUNCTION_ARB': 33348,
 'GL_DEBUG_CALLBACK_USER_PARAM': 33349,
 'GL_DEBUG_CALLBACK_USER_PARAM_ARB': 33349,
 'GL_DEBUG_GROUP_STACK_DEPTH': 33389,
 'GL_DEBUG_LOGGED_MESSAGES': 37189,
 'GL_DEBUG_LOGGED_MESSAGES_ARB': 37189,
 'GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH': 33347,
 'GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB': 33347,
 'GL_DEBUG_OUTPUT': 37600,
 'GL_DEBUG_OUTPUT_SYNCHRONOUS': 33346,
 'GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB': 33346,
 'GL_DEBUG_SEVERITY_HIGH': 37190,
 'GL_DEBUG_SEVERITY_HIGH_ARB': 37190,
 'GL_DEBUG_SEVERITY_LOW': 37192,
 'GL_DEBUG_SEVERITY_LOW_ARB': 37192,
 'GL_DEBUG_SEVERITY_MEDIUM': 37191,
 'GL_DEBUG_SEVERITY_MEDIUM_ARB': 37191,
 'GL_DEBUG_SEVERITY_NOTIFICATION': 33387,
 'GL_DEBUG_SOURCE_API': 33350,
 'GL_DEBUG_SOURCE_API_ARB': 33350,
 'GL_DEBUG_SOURCE_APPLICATION': 33354,
 'GL_DEBUG_SOURCE_APPLICATION_ARB': 33354,
 'GL_DEBUG_SOURCE_OTHER': 33355,
 'GL_DEBUG_SOURCE_OTHER_ARB': 33355,
 'GL_DEBUG_SOURCE_SHADER_COMPILER': 33352,
 'GL_DEBUG_SOURCE_SHADER_COMPILER_ARB': 33352,
 'GL_DEBUG_SOURCE_THIRD_PARTY': 33353,
 'GL_DEBUG_SOURCE_THIRD_PARTY_ARB': 33353,
 'GL_DEBUG_SOURCE_WINDOW_SYSTEM': 33351,
 'GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB': 33351,
 'GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR': 33357,
 'GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB': 33357,
 'GL_DEBUG_TYPE_ERROR': 33356,
 'GL_DEBUG_TYPE_ERROR_ARB': 33356,
 'GL_DEBUG_TYPE_MARKER': 33384,
 'GL_DEBUG_TYPE_OTHER': 33361,
 'GL_DEBUG_TYPE_OTHER_ARB': 33361,
 'GL_DEBUG_TYPE_PERFORMANCE': 33360,
 'GL_DEBUG_TYPE_PERFORMANCE_ARB': 33360,
 'GL_DEBUG_TYPE_POP_GROUP': 33386,
 'GL_DEBUG_TYPE_PORTABILITY': 33359,
 'GL_DEBUG_TYPE_PORTABILITY_ARB': 33359,
 'GL_DEBUG_TYPE_PUSH_GROUP': 33385,
 'GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR': 33358,
 'GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB': 33358,
 'GL_DECAL': 8449,
 'GL_DECODE_EXT': 35401,
 'GL_DECR': 7683,
 'GL_DECR_WRAP': 34056,
 'GL_DECR_WRAP_EXT': 34056,
 'GL_DEDICATED_MEMORY_OBJECT_EXT': 38273,
 'GL_DELETE_STATUS': 35712,
 'GL_DEPTH': 6145,
 'GL_DEPTH24_STENCIL8': 35056,
 'GL_DEPTH24_STENCIL8_EXT': 35056,
 'GL_DEPTH32F_STENCIL8': 36013,
 'GL_DEPTH_ATTACHMENT': 36096,
 'GL_DEPTH_ATTACHMENT_EXT': 36096,
 'GL_DEPTH_BIAS': 3359,
 'GL_DEPTH_BITS': 3414,
 'GL_DEPTH_BOUNDS_EXT': 34961,
 'GL_DEPTH_BOUNDS_TEST_EXT': 34960,
 'GL_DEPTH_BUFFER_BIT': 256,
 'GL_DEPTH_CLAMP': 34383,
 'GL_DEPTH_CLAMP_EXT': 34383,
 'GL_DEPTH_CLEAR_VALUE': 2931,
 'GL_DEPTH_COMPONENT': 6402,
 'GL_DEPTH_COMPONENT16': 33189,
 'GL_DEPTH_COMPONENT16_ARB': 33189,
 'GL_DEPTH_COMPONENT24': 33190,
 'GL_DEPTH_COMPONENT24_ARB': 33190,
 'GL_DEPTH_COMPONENT32': 33191,
 'GL_DEPTH_COMPONENT32F': 36012,
 'GL_DEPTH_COMPONENT32_ARB': 33191,
 'GL_DEPTH_COMPONENTS': 33412,
 'GL_DEPTH_EXT': 6145,
 'GL_DEPTH_FUNC': 2932,
 'GL_DEPTH_RANGE': 2928,
 'GL_DEPTH_RENDERABLE': 33415,
 'GL_DEPTH_SCALE': 3358,
 'GL_DEPTH_STENCIL': 34041,
 'GL_DEPTH_STENCIL_ATTACHMENT': 33306,
 'GL_DEPTH_STENCIL_EXT': 34041,
 'GL_DEPTH_STENCIL_TEXTURE_MODE': 37098,
 'GL_DEPTH_TEST': 2929,
 'GL_DEPTH_TEXTURE_MODE': 34891,
 'GL_DEPTH_TEXTURE_MODE_ARB': 34891,
 'GL_DEPTH_WRITEMASK': 2930,
 'GL_DEVICE_LUID_EXT': 38297,
 'GL_DEVICE_NODE_MASK_EXT': 38298,
 'GL_DEVICE_UUID_EXT': 38295,
 'GL_DIFFERENCE': 37534,
 'GL_DIFFUSE': 4609,
 'GL_DISPATCH_INDIRECT_BUFFER': 37102,
 'GL_DISPATCH_INDIRECT_BUFFER_BINDING': 37103,
 'GL_DISPLAY_LIST': 33511,
 'GL_DISTANCE_ATTENUATION_EXT': 33065,
 'GL_DITHER': 3024,
 'GL_DMP_PROGRAM_BINARY_DMP': 37459,
 'GL_DOMAIN': 2562,
 'GL_DONT_CARE': 4352,
 'GL_DOT3_RGB': 34478,
 'GL_DOT3_RGBA': 34479,
 'GL_DOT3_RGBA_ARB': 34479,
 'GL_DOT3_RGBA_EXT': 34625,
 'GL_DOT3_RGBA_IMG': 34479,
 'GL_DOT3_RGB_ARB': 34478,
 'GL_DOT3_RGB_EXT': 34624,
 'GL_DOUBLE': 5130,
 'GL_DOUBLEBUFFER': 3122,
 'GL_DOUBLE_EXT': 5130,
 'GL_DOUBLE_MAT2': 36678,
 'GL_DOUBLE_MAT2_EXT': 36678,
 'GL_DOUBLE_MAT2x3': 36681,
 'GL_DOUBLE_MAT2x3_EXT': 36681,
 'GL_DOUBLE_MAT2x4': 36682,
 'GL_DOUBLE_MAT2x4_EXT': 36682,
 'GL_DOUBLE_MAT3': 36679,
 'GL_DOUBLE_MAT3_EXT': 36679,
 'GL_DOUBLE_MAT3x2': 36683,
 'GL_DOUBLE_MAT3x2_EXT': 36683,
 'GL_DOUBLE_MAT3x4': 36684,
 'GL_DOUBLE_MAT3x4_EXT': 36684,
 'GL_DOUBLE_MAT4': 36680,
 'GL_DOUBLE_MAT4_EXT': 36680,
 'GL_DOUBLE_MAT4x2': 36685,
 'GL_DOUBLE_MAT4x2_EXT': 36685,
 'GL_DOUBLE_MAT4x3': 36686,
 'GL_DOUBLE_MAT4x3_EXT': 36686,
 'GL_DOUBLE_VEC2': 36860,
 'GL_DOUBLE_VEC2_EXT': 36860,
 'GL_DOUBLE_VEC3': 36861,
 'GL_DOUBLE_VEC3_EXT': 36861,
 'GL_DOUBLE_VEC4': 36862,
 'GL_DOUBLE_VEC4_EXT': 36862,
 'GL_DOWNSAMPLE_SCALES_IMG': 37182,
 'GL_DRAW_BUFFER': 3073,
 'GL_DRAW_BUFFER0': 34853,
 'GL_DRAW_BUFFER0_ARB': 34853,
 'GL_DRAW_BUFFER0_EXT': 34853,
 'GL_DRAW_BUFFER1': 34854,
 'GL_DRAW_BUFFER10': 34863,
 'GL_DRAW_BUFFER10_ARB': 34863,
 'GL_DRAW_BUFFER10_EXT': 34863,
 'GL_DRAW_BUFFER11': 34864,
 'GL_DRAW_BUFFER11_ARB': 34864,
 'GL_DRAW_BUFFER11_EXT': 34864,
 'GL_DRAW_BUFFER12': 34865,
 'GL_DRAW_BUFFER12_ARB': 34865,
 'GL_DRAW_BUFFER12_EXT': 34865,
 'GL_DRAW_BUFFER13': 34866,
 'GL_DRAW_BUFFER13_ARB': 34866,
 'GL_DRAW_BUFFER13_EXT': 34866,
 'GL_DRAW_BUFFER14': 34867,
 'GL_DRAW_BUFFER14_ARB': 34867,
 'GL_DRAW_BUFFER14_EXT': 34867,
 'GL_DRAW_BUFFER15': 34868,
 'GL_DRAW_BUFFER15_ARB': 34868,
 'GL_DRAW_BUFFER15_EXT': 34868,
 'GL_DRAW_BUFFER1_ARB': 34854,
 'GL_DRAW_BUFFER1_EXT': 34854,
 'GL_DRAW_BUFFER2': 34855,
 'GL_DRAW_BUFFER2_ARB': 34855,
 'GL_DRAW_BUFFER2_EXT': 34855,
 'GL_DRAW_BUFFER3': 34856,
 'GL_DRAW_BUFFER3_ARB': 34856,
 'GL_DRAW_BUFFER3_EXT': 34856,
 'GL_DRAW_BUFFER4': 34857,
 'GL_DRAW_BUFFER4_ARB': 34857,
 'GL_DRAW_BUFFER4_EXT': 34857,
 'GL_DRAW_BUFFER5': 34858,
 'GL_DRAW_BUFFER5_ARB': 34858,
 'GL_DRAW_BUFFER5_EXT': 34858,
 'GL_DRAW_BUFFER6': 34859,
 'GL_DRAW_BUFFER6_ARB': 34859,
 'GL_DRAW_BUFFER6_EXT': 34859,
 'GL_DRAW_BUFFER7': 34860,
 'GL_DRAW_BUFFER7_ARB': 34860,
 'GL_DRAW_BUFFER7_EXT': 34860,
 'GL_DRAW_BUFFER8': 34861,
 'GL_DRAW_BUFFER8_ARB': 34861,
 'GL_DRAW_BUFFER8_EXT': 34861,
 'GL_DRAW_BUFFER9': 34862,
 'GL_DRAW_BUFFER9_ARB': 34862,
 'GL_DRAW_BUFFER9_EXT': 34862,
 'GL_DRAW_BUFFER_EXT': 3073,
 'GL_DRAW_FRAMEBUFFER': 36009,
 'GL_DRAW_FRAMEBUFFER_ANGLE': 36009,
 'GL_DRAW_FRAMEBUFFER_BINDING': 36006,
 'GL_DRAW_FRAMEBUFFER_BINDING_ANGLE': 36006,
 'GL_DRAW_FRAMEBUFFER_BINDING_EXT': 36006,
 'GL_DRAW_FRAMEBUFFER_EXT': 36009,
 'GL_DRAW_INDIRECT_BUFFER': 36671,
 'GL_DRAW_INDIRECT_BUFFER_BINDING': 36675,
 'GL_DRAW_PIXEL_TOKEN': 1797,
 'GL_DRIVER_UUID_EXT': 38296,
 'GL_DST_ALPHA': 772,
 'GL_DST_COLOR': 774,
 'GL_DYNAMIC_COPY': 35050,
 'GL_DYNAMIC_COPY_ARB': 35050,
 'GL_DYNAMIC_DRAW': 35048,
 'GL_DYNAMIC_DRAW_ARB': 35048,
 'GL_DYNAMIC_READ': 35049,
 'GL_DYNAMIC_READ_ARB': 35049,
 'GL_DYNAMIC_STORAGE_BIT': 256,
 'GL_DYNAMIC_STORAGE_BIT_EXT': 256,
 'GL_EDGE_FLAG': 2883,
 'GL_EDGE_FLAG_ARRAY': 32889,
 'GL_EDGE_FLAG_ARRAY_BUFFER_BINDING': 34971,
 'GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB': 34971,
 'GL_EDGE_FLAG_ARRAY_COUNT_EXT': 32909,
 'GL_EDGE_FLAG_ARRAY_EXT': 32889,
 'GL_EDGE_FLAG_ARRAY_POINTER': 32915,
 'GL_EDGE_FLAG_ARRAY_POINTER_EXT': 32915,
 'GL_EDGE_FLAG_ARRAY_STRIDE': 32908,
 'GL_EDGE_FLAG_ARRAY_STRIDE_EXT': 32908,
 'GL_EFFECTIVE_RASTER_SAMPLES_EXT': 37676,
 'GL_ELEMENT_ARRAY_BARRIER_BIT': 2,
 'GL_ELEMENT_ARRAY_BARRIER_BIT_EXT': 2,
 'GL_ELEMENT_ARRAY_BUFFER': 34963,
 'GL_ELEMENT_ARRAY_BUFFER_ARB': 34963,
 'GL_ELEMENT_ARRAY_BUFFER_BINDING': 34965,
 'GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB': 34965,
 'GL_EMISSION': 5632,
 'GL_ENABLE_BIT': 8192,
 'GL_EQUAL': 514,
 'GL_EQUIV': 5385,
 'GL_EVAL_BIT': 65536,
 'GL_EXCLUSION': 37536,
 'GL_EXCLUSIVE_EXT': 36625,
 'GL_EXP': 2048,
 'GL_EXP2': 2049,
 'GL_EXTENSIONS': 7939,
 'GL_EXTERNAL_STORAGE_BIT_NVX': 8192,
 'GL_EYE_LINEAR': 9216,
 'GL_EYE_PLANE': 9474,
 'GL_FACTOR_ALPHA_MODULATE_IMG': 35847,
 'GL_FALSE': 0,
 'GL_FASTEST': 4353,
 'GL_FEEDBACK': 7169,
 'GL_FEEDBACK_BUFFER_POINTER': 3568,
 'GL_FEEDBACK_BUFFER_SIZE': 3569,
 'GL_FEEDBACK_BUFFER_TYPE': 3570,
 'GL_FETCH_PER_SAMPLE_ARM': 36709,
 'GL_FILL': 6914,
 'GL_FILTER': 33434,
 'GL_FIRST_VERTEX_CONVENTION': 36429,
 'GL_FIRST_VERTEX_CONVENTION_EXT': 36429,
 'GL_FIXED': 5132,
 'GL_FIXED_ONLY': 35101,
 'GL_FIXED_ONLY_ARB': 35101,
 'GL_FLAT': 7424,
 'GL_FLOAT': 5126,
 'GL_FLOAT_32_UNSIGNED_INT_24_8_REV': 36269,
 'GL_FLOAT_MAT2': 35674,
 'GL_FLOAT_MAT2_ARB': 35674,
 'GL_FLOAT_MAT2x3': 35685,
 'GL_FLOAT_MAT2x4': 35686,
 'GL_FLOAT_MAT3': 35675,
 'GL_FLOAT_MAT3_ARB': 35675,
 'GL_FLOAT_MAT3x2': 35687,
 'GL_FLOAT_MAT3x4': 35688,
 'GL_FLOAT_MAT4': 35676,
 'GL_FLOAT_MAT4_ARB': 35676,
 'GL_FLOAT_MAT4x2': 35689,
 'GL_FLOAT_MAT4x3': 35690,
 'GL_FLOAT_VEC2': 35664,
 'GL_FLOAT_VEC2_ARB': 35664,
 'GL_FLOAT_VEC3': 35665,
 'GL_FLOAT_VEC3_ARB': 35665,
 'GL_FLOAT_VEC4': 35666,
 'GL_FLOAT_VEC4_ARB': 35666,
 'GL_FOG': 2912,
 'GL_FOG_BIT': 128,
 'GL_FOG_COLOR': 2918,
 'GL_FOG_COORD': 33873,
 'GL_FOG_COORDINATE': 33873,
 'GL_FOG_COORDINATE_ARRAY': 33879,
 'GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING': 34973,
 'GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB': 34973,
 'GL_FOG_COORDINATE_ARRAY_EXT': 33879,
 'GL_FOG_COORDINATE_ARRAY_POINTER': 33878,
 'GL_FOG_COORDINATE_ARRAY_POINTER_EXT': 33878,
 'GL_FOG_COORDINATE_ARRAY_STRIDE': 33877,
 'GL_FOG_COORDINATE_ARRAY_STRIDE_EXT': 33877,
 'GL_FOG_COORDINATE_ARRAY_TYPE': 33876,
 'GL_FOG_COORDINATE_ARRAY_TYPE_EXT': 33876,
 'GL_FOG_COORDINATE_EXT': 33873,
 'GL_FOG_COORDINATE_SOURCE': 33872,
 'GL_FOG_COORDINATE_SOURCE_EXT': 33872,
 'GL_FOG_COORD_ARRAY': 33879,
 'GL_FOG_COORD_ARRAY_BUFFER_BINDING': 34973,
 'GL_FOG_COORD_ARRAY_POINTER': 33878,
 'GL_FOG_COORD_ARRAY_STRIDE': 33877,
 'GL_FOG_COORD_ARRAY_TYPE': 33876,
 'GL_FOG_COORD_SRC': 33872,
 'GL_FOG_DENSITY': 2914,
 'GL_FOG_END': 2916,
 'GL_FOG_HINT': 3156,
 'GL_FOG_INDEX': 2913,
 'GL_FOG_MODE': 2917,
 'GL_FOG_SPECULAR_TEXTURE_WIN': 33004,
 'GL_FOG_START': 2915,
 'GL_FORMAT_SUBSAMPLE_244_244_OML': 35203,
 'GL_FORMAT_SUBSAMPLE_24_24_OML': 35202,
 'GL_FRACTIONAL_EVEN': 36476,
 'GL_FRACTIONAL_EVEN_EXT': 36476,
 'GL_FRACTIONAL_ODD': 36475,
 'GL_FRACTIONAL_ODD_EXT': 36475,
 'GL_FRAGMENT_ALPHA_MODULATE_IMG': 35848,
 'GL_FRAGMENT_COLOR_EXT': 33612,
 'GL_FRAGMENT_DEPTH': 33874,
 'GL_FRAGMENT_DEPTH_EXT': 33874,
 'GL_FRAGMENT_INTERPOLATION_OFFSET_BITS': 36445,
 'GL_FRAGMENT_MATERIAL_EXT': 33609,
 'GL_FRAGMENT_NORMAL_EXT': 33610,
 'GL_FRAGMENT_PROGRAM_ARB': 34820,
 'GL_FRAGMENT_SHADER': 35632,
 'GL_FRAGMENT_SHADER_ARB': 35632,
 'GL_FRAGMENT_SHADER_BIT': 2,
 'GL_FRAGMENT_SHADER_BIT_EXT': 2,
 'GL_FRAGMENT_SHADER_DERIVATIVE_HINT': 35723,
 'GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB': 35723,
 'GL_FRAGMENT_SHADER_DISCARDS_SAMPLES_EXT': 35410,
 'GL_FRAGMENT_SHADER_FRAMEBUFFER_FETCH_MRT_ARM': 36710,
 'GL_FRAGMENT_SHADER_INVOCATIONS': 33524,
 'GL_FRAGMENT_SHADER_INVOCATIONS_ARB': 33524,
 'GL_FRAGMENT_SUBROUTINE': 37612,
 'GL_FRAGMENT_SUBROUTINE_UNIFORM': 37618,
 'GL_FRAGMENT_TEXTURE': 33439,
 'GL_FRAMEBUFFER': 36160,
 'GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE': 33301,
 'GL_FRAMEBUFFER_ATTACHMENT_ANGLE': 37795,
 'GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE': 33300,
 'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING': 33296,
 'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT': 33296,
 'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE': 33297,
 'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT': 33297,
 'GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE': 33302,
 'GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE': 33299,
 'GL_FRAMEBUFFER_ATTACHMENT_LAYERED': 36263,
 'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB': 36263,
 'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT': 36263,
 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME': 36049,
 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT': 36049,
 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE': 36048,
 'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT': 36048,
 'GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE': 33298,
 'GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE': 33303,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT': 36052,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR': 38450,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE': 36051,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT': 36051,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER': 36052,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT': 36052,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL': 36050,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT': 36050,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR': 38448,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT': 36204,
 'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SCALE_IMG': 37183,
 'GL_FRAMEBUFFER_BARRIER_BIT': 1024,
 'GL_FRAMEBUFFER_BARRIER_BIT_EXT': 1024,
 'GL_FRAMEBUFFER_BINDING': 36006,
 'GL_FRAMEBUFFER_BINDING_ANGLE': 36006,
 'GL_FRAMEBUFFER_BINDING_EXT': 36006,
 'GL_FRAMEBUFFER_BLEND': 33419,
 'GL_FRAMEBUFFER_COMPLETE': 36053,
 'GL_FRAMEBUFFER_COMPLETE_EXT': 36053,
 'GL_FRAMEBUFFER_DEFAULT': 33304,
 'GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS': 37652,
 'GL_FRAMEBUFFER_DEFAULT_HEIGHT': 37649,
 'GL_FRAMEBUFFER_DEFAULT_LAYERS': 37650,
 'GL_FRAMEBUFFER_DEFAULT_LAYERS_EXT': 37650,
 'GL_FRAMEBUFFER_DEFAULT_SAMPLES': 37651,
 'GL_FRAMEBUFFER_DEFAULT_WIDTH': 37648,
 'GL_FRAMEBUFFER_EXT': 36160,
 'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT': 36054,
 'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT': 36054,
 'GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS': 36057,
 'GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT': 36057,
 'GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER': 36059,
 'GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT': 36059,
 'GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT': 36058,
 'GL_FRAMEBUFFER_INCOMPLETE_INSUFFICIENT_SHADER_COMBINED_LOCAL_STORAGE_EXT': 38482,
 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB': 36265,
 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT': 36265,
 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS': 36264,
 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB': 36264,
 'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT': 36264,
 'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT': 36055,
 'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT': 36055,
 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE': 36182,
 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_AND_DOWNSAMPLE_IMG': 37180,
 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_ANGLE': 36182,
 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT': 36182,
 'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG': 37172,
 'GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER': 36060,
 'GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT': 36060,
 'GL_FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR': 38451,
 'GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_ARB': 37698,
 'GL_FRAMEBUFFER_RENDERABLE': 33417,
 'GL_FRAMEBUFFER_RENDERABLE_LAYERED': 33418,
 'GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_ARB': 37699,
 'GL_FRAMEBUFFER_SRGB': 36281,
 'GL_FRAMEBUFFER_SRGB_CAPABLE_EXT': 36282,
 'GL_FRAMEBUFFER_SRGB_EXT': 36281,
 'GL_FRAMEBUFFER_UNDEFINED': 33305,
 'GL_FRAMEBUFFER_UNSUPPORTED': 36061,
 'GL_FRAMEBUFFER_UNSUPPORTED_EXT': 36061,
 'GL_FRONT': 1028,
 'GL_FRONT_AND_BACK': 1032,
 'GL_FRONT_FACE': 2886,
 'GL_FRONT_LEFT': 1024,
 'GL_FRONT_RIGHT': 1025,
 'GL_FULL_RANGE_EXT': 34785,
 'GL_FULL_SUPPORT': 33463,
 'GL_FUNC_ADD': 32774,
 'GL_FUNC_ADD_EXT': 32774,
 'GL_FUNC_REVERSE_SUBTRACT': 32779,
 'GL_FUNC_REVERSE_SUBTRACT_EXT': 32779,
 'GL_FUNC_SUBTRACT': 32778,
 'GL_FUNC_SUBTRACT_EXT': 32778,
 'GL_GCCSO_SHADER_BINARY_FJ': 37472,
 'GL_GENERATE_MIPMAP': 33169,
 'GL_GENERATE_MIPMAP_HINT': 33170,
 'GL_GEOMETRY_INPUT_TYPE': 35095,
 'GL_GEOMETRY_INPUT_TYPE_ARB': 36315,
 'GL_GEOMETRY_INPUT_TYPE_EXT': 36315,
 'GL_GEOMETRY_LINKED_INPUT_TYPE_EXT': 35095,
 'GL_GEOMETRY_LINKED_OUTPUT_TYPE_EXT': 35096,
 'GL_GEOMETRY_LINKED_VERTICES_OUT_EXT': 35094,
 'GL_GEOMETRY_OUTPUT_TYPE': 35096,
 'GL_GEOMETRY_OUTPUT_TYPE_ARB': 36316,
 'GL_GEOMETRY_OUTPUT_TYPE_EXT': 36316,
 'GL_GEOMETRY_SHADER': 36313,
 'GL_GEOMETRY_SHADER_ARB': 36313,
 'GL_GEOMETRY_SHADER_BIT': 4,
 'GL_GEOMETRY_SHADER_BIT_EXT': 4,
 'GL_GEOMETRY_SHADER_EXT': 36313,
 'GL_GEOMETRY_SHADER_INVOCATIONS': 34943,
 'GL_GEOMETRY_SHADER_INVOCATIONS_EXT': 34943,
 'GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED': 33523,
 'GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED_ARB': 33523,
 'GL_GEOMETRY_SUBROUTINE': 37611,
 'GL_GEOMETRY_SUBROUTINE_UNIFORM': 37617,
 'GL_GEOMETRY_TEXTURE': 33438,
 'GL_GEOMETRY_VERTICES_OUT': 35094,
 'GL_GEOMETRY_VERTICES_OUT_ARB': 36314,
 'GL_GEOMETRY_VERTICES_OUT_EXT': 36314,
 'GL_GEQUAL': 518,
 'GL_GET_TEXTURE_IMAGE_FORMAT': 33425,
 'GL_GET_TEXTURE_IMAGE_TYPE': 33426,
 'GL_GPU_DISJOINT_EXT': 36795,
 'GL_GPU_MEMORY_INFO_CURRENT_AVAILABLE_VIDMEM_NVX': 36937,
 'GL_GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX': 36935,
 'GL_GPU_MEMORY_INFO_EVICTED_MEMORY_NVX': 36939,
 'GL_GPU_MEMORY_INFO_EVICTION_COUNT_NVX': 36938,
 'GL_GPU_MEMORY_INFO_TOTAL_AVAILABLE_MEMORY_NVX': 36936,
 'GL_GREATER': 516,
 'GL_GREEN': 6404,
 'GL_GREEN_BIAS': 3353,
 'GL_GREEN_BITS': 3411,
 'GL_GREEN_INTEGER': 36245,
 'GL_GREEN_INTEGER_EXT': 36245,
 'GL_GREEN_MAX_CLAMP_INGR': 34149,
 'GL_GREEN_MIN_CLAMP_INGR': 34145,
 'GL_GREEN_SCALE': 3352,
 'GL_GS_PROGRAM_BINARY_MTK': 38465,
 'GL_GS_SHADER_BINARY_MTK': 38464,
 'GL_GUILTY_CONTEXT_RESET': 33363,
 'GL_GUILTY_CONTEXT_RESET_ARB': 33363,
 'GL_GUILTY_CONTEXT_RESET_EXT': 33363,
 'GL_HALF_FLOAT': 5131,
 'GL_HALF_FLOAT_ARB': 5131,
 'GL_HANDLE_TYPE_D3D11_IMAGE_EXT': 38283,
 'GL_HANDLE_TYPE_D3D11_IMAGE_KMT_EXT': 38284,
 'GL_HANDLE_TYPE_D3D12_FENCE_EXT': 38292,
 'GL_HANDLE_TYPE_D3D12_RESOURCE_EXT': 38282,
 'GL_HANDLE_TYPE_D3D12_TILEPOOL_EXT': 38281,
 'GL_HANDLE_TYPE_OPAQUE_FD_EXT': 38278,
 'GL_HANDLE_TYPE_OPAQUE_WIN32_EXT': 38279,
 'GL_HANDLE_TYPE_OPAQUE_WIN32_KMT_EXT': 38280,
 'GL_HARDLIGHT': 37531,
 'GL_HIGH_FLOAT': 36338,
 'GL_HIGH_INT': 36341,
 'GL_HINT_BIT': 32768,
 'GL_HISTOGRAM': 32804,
 'GL_HISTOGRAM_ALPHA_SIZE': 32811,
 'GL_HISTOGRAM_ALPHA_SIZE_EXT': 32811,
 'GL_HISTOGRAM_BLUE_SIZE': 32810,
 'GL_HISTOGRAM_BLUE_SIZE_EXT': 32810,
 'GL_HISTOGRAM_EXT': 32804,
 'GL_HISTOGRAM_FORMAT': 32807,
 'GL_HISTOGRAM_FORMAT_EXT': 32807,
 'GL_HISTOGRAM_GREEN_SIZE': 32809,
 'GL_HISTOGRAM_GREEN_SIZE_EXT': 32809,
 'GL_HISTOGRAM_LUMINANCE_SIZE': 32812,
 'GL_HISTOGRAM_LUMINANCE_SIZE_EXT': 32812,
 'GL_HISTOGRAM_RED_SIZE': 32808,
 'GL_HISTOGRAM_RED_SIZE_EXT': 32808,
 'GL_HISTOGRAM_SINK': 32813,
 'GL_HISTOGRAM_SINK_EXT': 32813,
 'GL_HISTOGRAM_WIDTH': 32806,
 'GL_HISTOGRAM_WIDTH_EXT': 32806,
 'GL_HSL_COLOR': 37551,
 'GL_HSL_HUE': 37549,
 'GL_HSL_LUMINOSITY': 37552,
 'GL_HSL_SATURATION': 37550,
 'GL_IGNORE_BORDER_HP': 33104,
 'GL_IMAGE_1D': 36940,
 'GL_IMAGE_1D_ARRAY': 36946,
 'GL_IMAGE_1D_ARRAY_EXT': 36946,
 'GL_IMAGE_1D_EXT': 36940,
 'GL_IMAGE_2D': 36941,
 'GL_IMAGE_2D_ARRAY': 36947,
 'GL_IMAGE_2D_ARRAY_EXT': 36947,
 'GL_IMAGE_2D_EXT': 36941,
 'GL_IMAGE_2D_MULTISAMPLE': 36949,
 'GL_IMAGE_2D_MULTISAMPLE_ARRAY': 36950,
 'GL_IMAGE_2D_MULTISAMPLE_ARRAY_EXT': 36950,
 'GL_IMAGE_2D_MULTISAMPLE_EXT': 36949,
 'GL_IMAGE_2D_RECT': 36943,
 'GL_IMAGE_2D_RECT_EXT': 36943,
 'GL_IMAGE_3D': 36942,
 'GL_IMAGE_3D_EXT': 36942,
 'GL_IMAGE_BINDING_ACCESS': 36670,
 'GL_IMAGE_BINDING_ACCESS_EXT': 36670,
 'GL_IMAGE_BINDING_FORMAT': 36974,
 'GL_IMAGE_BINDING_FORMAT_EXT': 36974,
 'GL_IMAGE_BINDING_LAYER': 36669,
 'GL_IMAGE_BINDING_LAYERED': 36668,
 'GL_IMAGE_BINDING_LAYERED_EXT': 36668,
 'GL_IMAGE_BINDING_LAYER_EXT': 36669,
 'GL_IMAGE_BINDING_LEVEL': 36667,
 'GL_IMAGE_BINDING_LEVEL_EXT': 36667,
 'GL_IMAGE_BINDING_NAME': 36666,
 'GL_IMAGE_BINDING_NAME_EXT': 36666,
 'GL_IMAGE_BUFFER': 36945,
 'GL_IMAGE_BUFFER_EXT': 36945,
 'GL_IMAGE_CLASS_10_10_10_2': 33475,
 'GL_IMAGE_CLASS_11_11_10': 33474,
 'GL_IMAGE_CLASS_1_X_16': 33470,
 'GL_IMAGE_CLASS_1_X_32': 33467,
 'GL_IMAGE_CLASS_1_X_8': 33473,
 'GL_IMAGE_CLASS_2_X_16': 33469,
 'GL_IMAGE_CLASS_2_X_32': 33466,
 'GL_IMAGE_CLASS_2_X_8': 33472,
 'GL_IMAGE_CLASS_4_X_16': 33468,
 'GL_IMAGE_CLASS_4_X_32': 33465,
 'GL_IMAGE_CLASS_4_X_8': 33471,
 'GL_IMAGE_COMPATIBILITY_CLASS': 33448,
 'GL_IMAGE_CUBE': 36944,
 'GL_IMAGE_CUBE_EXT': 36944,
 'GL_IMAGE_CUBE_MAP_ARRAY': 36948,
 'GL_IMAGE_CUBE_MAP_ARRAY_EXT': 36948,
 'GL_IMAGE_CUBIC_WEIGHT_HP': 33118,
 'GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS': 37065,
 'GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE': 37064,
 'GL_IMAGE_FORMAT_COMPATIBILITY_TYPE': 37063,
 'GL_IMAGE_MAG_FILTER_HP': 33116,
 'GL_IMAGE_MIN_FILTER_HP': 33117,
 'GL_IMAGE_PIXEL_FORMAT': 33449,
 'GL_IMAGE_PIXEL_TYPE': 33450,
 'GL_IMAGE_ROTATE_ANGLE_HP': 33113,
 'GL_IMAGE_ROTATE_ORIGIN_X_HP': 33114,
 'GL_IMAGE_ROTATE_ORIGIN_Y_HP': 33115,
 'GL_IMAGE_SCALE_X_HP': 33109,
 'GL_IMAGE_SCALE_Y_HP': 33110,
 'GL_IMAGE_TEXEL_SIZE': 33447,
 'GL_IMAGE_TRANSFORM_2D_HP': 33121,
 'GL_IMAGE_TRANSLATE_X_HP': 33111,
 'GL_IMAGE_TRANSLATE_Y_HP': 33112,
 'GL_IMPLEMENTATION_COLOR_READ_FORMAT': 35739,
 'GL_IMPLEMENTATION_COLOR_READ_TYPE': 35738,
 'GL_INCLUSIVE_EXT': 36624,
 'GL_INCR': 7682,
 'GL_INCR_WRAP': 34055,
 'GL_INCR_WRAP_EXT': 34055,
 'GL_INDEX': 33314,
 'GL_INDEX_ARRAY': 32887,
 'GL_INDEX_ARRAY_BUFFER_BINDING': 34969,
 'GL_INDEX_ARRAY_BUFFER_BINDING_ARB': 34969,
 'GL_INDEX_ARRAY_COUNT_EXT': 32903,
 'GL_INDEX_ARRAY_EXT': 32887,
 'GL_INDEX_ARRAY_POINTER': 32913,
 'GL_INDEX_ARRAY_POINTER_EXT': 32913,
 'GL_INDEX_ARRAY_STRIDE': 32902,
 'GL_INDEX_ARRAY_STRIDE_EXT': 32902,
 'GL_INDEX_ARRAY_TYPE': 32901,
 'GL_INDEX_ARRAY_TYPE_EXT': 32901,
 'GL_INDEX_BITS': 3409,
 'GL_INDEX_CLEAR_VALUE': 3104,
 'GL_INDEX_LOGIC_OP': 3057,
 'GL_INDEX_MATERIAL_EXT': 33208,
 'GL_INDEX_MATERIAL_FACE_EXT': 33210,
 'GL_INDEX_MATERIAL_PARAMETER_EXT': 33209,
 'GL_INDEX_MODE': 3120,
 'GL_INDEX_OFFSET': 3347,
 'GL_INDEX_SHIFT': 3346,
 'GL_INDEX_TEST_EXT': 33205,
 'GL_INDEX_TEST_FUNC_EXT': 33206,
 'GL_INDEX_TEST_REF_EXT': 33207,
 'GL_INDEX_WRITEMASK': 3105,
 'GL_INFO_LOG_LENGTH': 35716,
 'GL_INNOCENT_CONTEXT_RESET': 33364,
 'GL_INNOCENT_CONTEXT_RESET_ARB': 33364,
 'GL_INNOCENT_CONTEXT_RESET_EXT': 33364,
 'GL_INT': 5124,
 'GL_INT64_ARB': 5134,
 'GL_INT64_VEC2_ARB': 36841,
 'GL_INT64_VEC3_ARB': 36842,
 'GL_INT64_VEC4_ARB': 36843,
 'GL_INTENSITY': 32841,
 'GL_INTENSITY12': 32844,
 'GL_INTENSITY12_EXT': 32844,
 'GL_INTENSITY16': 32845,
 'GL_INTENSITY16F_ARB': 34845,
 'GL_INTENSITY16I_EXT': 36235,
 'GL_INTENSITY16UI_EXT': 36217,
 'GL_INTENSITY16_EXT': 32845,
 'GL_INTENSITY16_SNORM': 36891,
 'GL_INTENSITY32F_ARB': 34839,
 'GL_INTENSITY32I_EXT': 36229,
 'GL_INTENSITY32UI_EXT': 36211,
 'GL_INTENSITY4': 32842,
 'GL_INTENSITY4_EXT': 32842,
 'GL_INTENSITY8': 32843,
 'GL_INTENSITY8I_EXT': 36241,
 'GL_INTENSITY8UI_EXT': 36223,
 'GL_INTENSITY8_EXT': 32843,
 'GL_INTENSITY8_SNORM': 36887,
 'GL_INTENSITY_EXT': 32841,
 'GL_INTENSITY_SNORM': 36883,
 'GL_INTERLACE_OML': 35200,
 'GL_INTERLACE_READ_INGR': 34152,
 'GL_INTERLACE_READ_OML': 35201,
 'GL_INTERLEAVED_ATTRIBS': 35980,
 'GL_INTERLEAVED_ATTRIBS_EXT': 35980,
 'GL_INTERNALFORMAT_ALPHA_SIZE': 33396,
 'GL_INTERNALFORMAT_ALPHA_TYPE': 33403,
 'GL_INTERNALFORMAT_BLUE_SIZE': 33395,
 'GL_INTERNALFORMAT_BLUE_TYPE': 33402,
 'GL_INTERNALFORMAT_DEPTH_SIZE': 33397,
 'GL_INTERNALFORMAT_DEPTH_TYPE': 33404,
 'GL_INTERNALFORMAT_GREEN_SIZE': 33394,
 'GL_INTERNALFORMAT_GREEN_TYPE': 33401,
 'GL_INTERNALFORMAT_PREFERRED': 33392,
 'GL_INTERNALFORMAT_RED_SIZE': 33393,
 'GL_INTERNALFORMAT_RED_TYPE': 33400,
 'GL_INTERNALFORMAT_SHARED_SIZE': 33399,
 'GL_INTERNALFORMAT_STENCIL_SIZE': 33398,
 'GL_INTERNALFORMAT_STENCIL_TYPE': 33405,
 'GL_INTERNALFORMAT_SUPPORTED': 33391,
 'GL_INTERPOLATE': 34165,
 'GL_INTERPOLATE_ARB': 34165,
 'GL_INTERPOLATE_EXT': 34165,
 'GL_INT_2_10_10_10_REV': 36255,
 'GL_INT_IMAGE_1D': 36951,
 'GL_INT_IMAGE_1D_ARRAY': 36957,
 'GL_INT_IMAGE_1D_ARRAY_EXT': 36957,
 'GL_INT_IMAGE_1D_EXT': 36951,
 'GL_INT_IMAGE_2D': 36952,
 'GL_INT_IMAGE_2D_ARRAY': 36958,
 'GL_INT_IMAGE_2D_ARRAY_EXT': 36958,
 'GL_INT_IMAGE_2D_EXT': 36952,
 'GL_INT_IMAGE_2D_MULTISAMPLE': 36960,
 'GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY': 36961,
 'GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT': 36961,
 'GL_INT_IMAGE_2D_MULTISAMPLE_EXT': 36960,
 'GL_INT_IMAGE_2D_RECT': 36954,
 'GL_INT_IMAGE_2D_RECT_EXT': 36954,
 'GL_INT_IMAGE_3D': 36953,
 'GL_INT_IMAGE_3D_EXT': 36953,
 'GL_INT_IMAGE_BUFFER': 36956,
 'GL_INT_IMAGE_BUFFER_EXT': 36956,
 'GL_INT_IMAGE_CUBE': 36955,
 'GL_INT_IMAGE_CUBE_EXT': 36955,
 'GL_INT_IMAGE_CUBE_MAP_ARRAY': 36959,
 'GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT': 36959,
 'GL_INT_SAMPLER_1D': 36297,
 'GL_INT_SAMPLER_1D_ARRAY': 36302,
 'GL_INT_SAMPLER_1D_ARRAY_EXT': 36302,
 'GL_INT_SAMPLER_1D_EXT': 36297,
 'GL_INT_SAMPLER_2D': 36298,
 'GL_INT_SAMPLER_2D_ARRAY': 36303,
 'GL_INT_SAMPLER_2D_ARRAY_EXT': 36303,
 'GL_INT_SAMPLER_2D_EXT': 36298,
 'GL_INT_SAMPLER_2D_MULTISAMPLE': 37129,
 'GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY': 37132,
 'GL_INT_SAMPLER_2D_RECT': 36301,
 'GL_INT_SAMPLER_2D_RECT_EXT': 36301,
 'GL_INT_SAMPLER_3D': 36299,
 'GL_INT_SAMPLER_3D_EXT': 36299,
 'GL_INT_SAMPLER_BUFFER': 36304,
 'GL_INT_SAMPLER_BUFFER_EXT': 36304,
 'GL_INT_SAMPLER_CUBE': 36300,
 'GL_INT_SAMPLER_CUBE_EXT': 36300,
 'GL_INT_SAMPLER_CUBE_MAP_ARRAY': 36878,
 'GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB': 36878,
 'GL_INT_SAMPLER_CUBE_MAP_ARRAY_EXT': 36878,
 'GL_INT_VEC2': 35667,
 'GL_INT_VEC2_ARB': 35667,
 'GL_INT_VEC3': 35668,
 'GL_INT_VEC3_ARB': 35668,
 'GL_INT_VEC4': 35669,
 'GL_INT_VEC4_ARB': 35669,
 'GL_INVALID_ENUM': 1280,
 'GL_INVALID_FRAMEBUFFER_OPERATION': 1286,
 'GL_INVALID_FRAMEBUFFER_OPERATION_EXT': 1286,
 'GL_INVALID_INDEX': 4294967295,
 'GL_INVALID_OPERATION': 1282,
 'GL_INVALID_VALUE': 1281,
 'GL_INVARIANT_DATATYPE_EXT': 34795,
 'GL_INVARIANT_EXT': 34754,
 'GL_INVARIANT_VALUE_EXT': 34794,
 'GL_INVERT': 5386,
 'GL_INVERTED_SCREEN_W_REND': 33937,
 'GL_ISOLINES': 36474,
 'GL_ISOLINES_EXT': 36474,
 'GL_IS_PER_PATCH': 37607,
 'GL_IS_PER_PATCH_EXT': 37607,
 'GL_IS_ROW_MAJOR': 37632,
 'GL_IUI_N3F_V2F_EXT': 33199,
 'GL_IUI_N3F_V3F_EXT': 33200,
 'GL_IUI_V2F_EXT': 33197,
 'GL_IUI_V3F_EXT': 33198,
 'GL_KEEP': 7680,
 'GL_LAST_VERTEX_CONVENTION': 36430,
 'GL_LAST_VERTEX_CONVENTION_EXT': 36430,
 'GL_LAYER_PROVOKING_VERTEX': 33374,
 'GL_LAYER_PROVOKING_VERTEX_EXT': 33374,
 'GL_LAYOUT_COLOR_ATTACHMENT_EXT': 38286,
 'GL_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_EXT': 38193,
 'GL_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_EXT': 38192,
 'GL_LAYOUT_DEPTH_STENCIL_ATTACHMENT_EXT': 38287,
 'GL_LAYOUT_DEPTH_STENCIL_READ_ONLY_EXT': 38288,
 'GL_LAYOUT_GENERAL_EXT': 38285,
 'GL_LAYOUT_SHADER_READ_ONLY_EXT': 38289,
 'GL_LAYOUT_TRANSFER_DST_EXT': 38291,
 'GL_LAYOUT_TRANSFER_SRC_EXT': 38290,
 'GL_LEFT': 1030,
 'GL_LEQUAL': 515,
 'GL_LESS': 513,
 'GL_LGPU_SEPARATE_STORAGE_BIT_NVX': 2048,
 'GL_LIGHT0': 16384,
 'GL_LIGHT1': 16385,
 'GL_LIGHT2': 16386,
 'GL_LIGHT3': 16387,
 'GL_LIGHT4': 16388,
 'GL_LIGHT5': 16389,
 'GL_LIGHT6': 16390,
 'GL_LIGHT7': 16391,
 'GL_LIGHTEN': 37528,
 'GL_LIGHTING': 2896,
 'GL_LIGHTING_BIT': 64,
 'GL_LIGHT_MODEL_AMBIENT': 2899,
 'GL_LIGHT_MODEL_COLOR_CONTROL': 33272,
 'GL_LIGHT_MODEL_COLOR_CONTROL_EXT': 33272,
 'GL_LIGHT_MODEL_LOCAL_VIEWER': 2897,
 'GL_LIGHT_MODEL_TWO_SIDE': 2898,
 'GL_LINE': 6913,
 'GL_LINEAR': 9729,
 'GL_LINEAR_ATTENUATION': 4616,
 'GL_LINEAR_MIPMAP_LINEAR': 9987,
 'GL_LINEAR_MIPMAP_NEAREST': 9985,
 'GL_LINEAR_TILING_EXT': 38277,
 'GL_LINES': 1,
 'GL_LINES_ADJACENCY': 10,
 'GL_LINES_ADJACENCY_ARB': 10,
 'GL_LINES_ADJACENCY_EXT': 10,
 'GL_LINE_BIT': 4,
 'GL_LINE_LOOP': 2,
 'GL_LINE_RESET_TOKEN': 1799,
 'GL_LINE_SMOOTH': 2848,
 'GL_LINE_SMOOTH_HINT': 3154,
 'GL_LINE_STIPPLE': 2852,
 'GL_LINE_STIPPLE_PATTERN': 2853,
 'GL_LINE_STIPPLE_REPEAT': 2854,
 'GL_LINE_STRIP': 3,
 'GL_LINE_STRIP_ADJACENCY': 11,
 'GL_LINE_STRIP_ADJACENCY_ARB': 11,
 'GL_LINE_STRIP_ADJACENCY_EXT': 11,
 'GL_LINE_TOKEN': 1794,
 'GL_LINE_WIDTH': 2849,
 'GL_LINE_WIDTH_GRANULARITY': 2851,
 'GL_LINE_WIDTH_RANGE': 2850,
 'GL_LINK_STATUS': 35714,
 'GL_LIST_BASE': 2866,
 'GL_LIST_BIT': 131072,
 'GL_LIST_INDEX': 2867,
 'GL_LIST_MODE': 2864,
 'GL_LOAD': 257,
 'GL_LOCAL_CONSTANT_DATATYPE_EXT': 34797,
 'GL_LOCAL_CONSTANT_EXT': 34755,
 'GL_LOCAL_CONSTANT_VALUE_EXT': 34796,
 'GL_LOCAL_EXT': 34756,
 'GL_LOCATION': 37646,
 'GL_LOCATION_COMPONENT': 37706,
 'GL_LOCATION_INDEX': 37647,
 'GL_LOCATION_INDEX_EXT': 37647,
 'GL_LOGIC_OP': 3057,
 'GL_LOGIC_OP_MODE': 3056,
 'GL_LOSE_CONTEXT_ON_RESET': 33362,
 'GL_LOSE_CONTEXT_ON_RESET_ARB': 33362,
 'GL_LOSE_CONTEXT_ON_RESET_EXT': 33362,
 'GL_LOWER_LEFT': 36001,
 'GL_LOWER_LEFT_EXT': 36001,
 'GL_LOW_FLOAT': 36336,
 'GL_LOW_INT': 36339,
 'GL_LUID_SIZE_EXT': 8,
 'GL_LUMINANCE': 6409,
 'GL_LUMINANCE12': 32833,
 'GL_LUMINANCE12_ALPHA12': 32839,
 'GL_LUMINANCE12_ALPHA12_EXT': 32839,
 'GL_LUMINANCE12_ALPHA4': 32838,
 'GL_LUMINANCE12_ALPHA4_EXT': 32838,
 'GL_LUMINANCE12_EXT': 32833,
 'GL_LUMINANCE16': 32834,
 'GL_LUMINANCE16F_ARB': 34846,
 'GL_LUMINANCE16F_EXT': 34846,
 'GL_LUMINANCE16I_EXT': 36236,
 'GL_LUMINANCE16UI_EXT': 36218,
 'GL_LUMINANCE16_ALPHA16': 32840,
 'GL_LUMINANCE16_ALPHA16_EXT': 32840,
 'GL_LUMINANCE16_ALPHA16_SNORM': 36890,
 'GL_LUMINANCE16_EXT': 32834,
 'GL_LUMINANCE16_SNORM': 36889,
 'GL_LUMINANCE32F_ARB': 34840,
 'GL_LUMINANCE32F_EXT': 34840,
 'GL_LUMINANCE32I_EXT': 36230,
 'GL_LUMINANCE32UI_EXT': 36212,
 'GL_LUMINANCE4': 32831,
 'GL_LUMINANCE4_ALPHA4': 32835,
 'GL_LUMINANCE4_ALPHA4_EXT': 32835,
 'GL_LUMINANCE4_EXT': 32831,
 'GL_LUMINANCE6_ALPHA2': 32836,
 'GL_LUMINANCE6_ALPHA2_EXT': 32836,
 'GL_LUMINANCE8': 32832,
 'GL_LUMINANCE8I_EXT': 36242,
 'GL_LUMINANCE8UI_EXT': 36224,
 'GL_LUMINANCE8_ALPHA8': 32837,
 'GL_LUMINANCE8_ALPHA8_EXT': 32837,
 'GL_LUMINANCE8_ALPHA8_SNORM': 36886,
 'GL_LUMINANCE8_EXT': 32832,
 'GL_LUMINANCE8_SNORM': 36885,
 'GL_LUMINANCE_ALPHA': 6410,
 'GL_LUMINANCE_ALPHA16F_ARB': 34847,
 'GL_LUMINANCE_ALPHA16F_EXT': 34847,
 'GL_LUMINANCE_ALPHA16I_EXT': 36237,
 'GL_LUMINANCE_ALPHA16UI_EXT': 36219,
 'GL_LUMINANCE_ALPHA32F_ARB': 34841,
 'GL_LUMINANCE_ALPHA32F_EXT': 34841,
 'GL_LUMINANCE_ALPHA32I_EXT': 36231,
 'GL_LUMINANCE_ALPHA32UI_EXT': 36213,
 'GL_LUMINANCE_ALPHA8I_EXT': 36243,
 'GL_LUMINANCE_ALPHA8UI_EXT': 36225,
 'GL_LUMINANCE_ALPHA_INTEGER_EXT': 36253,
 'GL_LUMINANCE_ALPHA_SNORM': 36882,
 'GL_LUMINANCE_INTEGER_EXT': 36252,
 'GL_LUMINANCE_SNORM': 36881,
 'GL_MAJOR_VERSION': 33307,
 'GL_MALI_PROGRAM_BINARY_ARM': 36705,
 'GL_MALI_SHADER_BINARY_ARM': 36704,
 'GL_MANUAL_GENERATE_MIPMAP': 33428,
 'GL_MAP1_BINORMAL_EXT': 33862,
 'GL_MAP1_COLOR_4': 3472,
 'GL_MAP1_GRID_DOMAIN': 3536,
 'GL_MAP1_GRID_SEGMENTS': 3537,
 'GL_MAP1_INDEX': 3473,
 'GL_MAP1_NORMAL': 3474,
 'GL_MAP1_TANGENT_EXT': 33860,
 'GL_MAP1_TEXTURE_COORD_1': 3475,
 'GL_MAP1_TEXTURE_COORD_2': 3476,
 'GL_MAP1_TEXTURE_COORD_3': 3477,
 'GL_MAP1_TEXTURE_COORD_4': 3478,
 'GL_MAP1_VERTEX_3': 3479,
 'GL_MAP1_VERTEX_4': 3480,
 'GL_MAP2_BINORMAL_EXT': 33863,
 'GL_MAP2_COLOR_4': 3504,
 'GL_MAP2_GRID_DOMAIN': 3538,
 'GL_MAP2_GRID_SEGMENTS': 3539,
 'GL_MAP2_INDEX': 3505,
 'GL_MAP2_NORMAL': 3506,
 'GL_MAP2_TANGENT_EXT': 33861,
 'GL_MAP2_TEXTURE_COORD_1': 3507,
 'GL_MAP2_TEXTURE_COORD_2': 3508,
 'GL_MAP2_TEXTURE_COORD_3': 3509,
 'GL_MAP2_TEXTURE_COORD_4': 3510,
 'GL_MAP2_VERTEX_3': 3511,
 'GL_MAP2_VERTEX_4': 3512,
 'GL_MAP_COHERENT_BIT': 128,
 'GL_MAP_COHERENT_BIT_EXT': 128,
 'GL_MAP_COLOR': 3344,
 'GL_MAP_FLUSH_EXPLICIT_BIT': 16,
 'GL_MAP_FLUSH_EXPLICIT_BIT_EXT': 16,
 'GL_MAP_INVALIDATE_BUFFER_BIT': 8,
 'GL_MAP_INVALIDATE_BUFFER_BIT_EXT': 8,
 'GL_MAP_INVALIDATE_RANGE_BIT': 4,
 'GL_MAP_INVALIDATE_RANGE_BIT_EXT': 4,
 'GL_MAP_PERSISTENT_BIT': 64,
 'GL_MAP_PERSISTENT_BIT_EXT': 64,
 'GL_MAP_READ_BIT': 1,
 'GL_MAP_READ_BIT_EXT': 1,
 'GL_MAP_STENCIL': 3345,
 'GL_MAP_UNSYNCHRONIZED_BIT': 32,
 'GL_MAP_UNSYNCHRONIZED_BIT_EXT': 32,
 'GL_MAP_WRITE_BIT': 2,
 'GL_MAP_WRITE_BIT_EXT': 2,
 'GL_MATRIX0_ARB': 35008,
 'GL_MATRIX10_ARB': 35018,
 'GL_MATRIX11_ARB': 35019,
 'GL_MATRIX12_ARB': 35020,
 'GL_MATRIX13_ARB': 35021,
 'GL_MATRIX14_ARB': 35022,
 'GL_MATRIX15_ARB': 35023,
 'GL_MATRIX16_ARB': 35024,
 'GL_MATRIX17_ARB': 35025,
 'GL_MATRIX18_ARB': 35026,
 'GL_MATRIX19_ARB': 35027,
 'GL_MATRIX1_ARB': 35009,
 'GL_MATRIX20_ARB': 35028,
 'GL_MATRIX21_ARB': 35029,
 'GL_MATRIX22_ARB': 35030,
 'GL_MATRIX23_ARB': 35031,
 'GL_MATRIX24_ARB': 35032,
 'GL_MATRIX25_ARB': 35033,
 'GL_MATRIX26_ARB': 35034,
 'GL_MATRIX27_ARB': 35035,
 'GL_MATRIX28_ARB': 35036,
 'GL_MATRIX29_ARB': 35037,
 'GL_MATRIX2_ARB': 35010,
 'GL_MATRIX30_ARB': 35038,
 'GL_MATRIX31_ARB': 35039,
 'GL_MATRIX3_ARB': 35011,
 'GL_MATRIX4_ARB': 35012,
 'GL_MATRIX5_ARB': 35013,
 'GL_MATRIX6_ARB': 35014,
 'GL_MATRIX7_ARB': 35015,
 'GL_MATRIX8_ARB': 35016,
 'GL_MATRIX9_ARB': 35017,
 'GL_MATRIX_EXT': 34752,
 'GL_MATRIX_INDEX_ARRAY_ARB': 34884,
 'GL_MATRIX_INDEX_ARRAY_POINTER_ARB': 34889,
 'GL_MATRIX_INDEX_ARRAY_SIZE_ARB': 34886,
 'GL_MATRIX_INDEX_ARRAY_STRIDE_ARB': 34888,
 'GL_MATRIX_INDEX_ARRAY_TYPE_ARB': 34887,
 'GL_MATRIX_MODE': 2976,
 'GL_MATRIX_PALETTE_ARB': 34880,
 'GL_MATRIX_STRIDE': 37631,
 'GL_MAX': 32776,
 'GL_MAX_3D_TEXTURE_SIZE': 32883,
 'GL_MAX_3D_TEXTURE_SIZE_EXT': 32883,
 'GL_MAX_ARRAY_TEXTURE_LAYERS': 35071,
 'GL_MAX_ARRAY_TEXTURE_LAYERS_EXT': 35071,
 'GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS': 37596,
 'GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE': 37592,
 'GL_MAX_ATTRIB_STACK_DEPTH': 3381,
 'GL_MAX_BINDABLE_UNIFORM_SIZE_EXT': 36333,
 'GL_MAX_CLIENT_ATTRIB_STACK_DEPTH': 3387,
 'GL_MAX_CLIP_DISTANCES': 3378,
 'GL_MAX_CLIP_DISTANCES_EXT': 3378,
 'GL_MAX_CLIP_PLANES': 3378,
 'GL_MAX_CLIP_PLANES_IMG': 3378,
 'GL_MAX_COLOR_ATTACHMENTS': 36063,
 'GL_MAX_COLOR_ATTACHMENTS_EXT': 36063,
 'GL_MAX_COLOR_MATRIX_STACK_DEPTH': 32947,
 'GL_MAX_COLOR_TEXTURE_SAMPLES': 37134,
 'GL_MAX_COMBINED_ATOMIC_COUNTERS': 37591,
 'GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS': 37585,
 'GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES': 33530,
 'GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES_EXT': 33530,
 'GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS': 33382,
 'GL_MAX_COMBINED_DIMENSIONS': 33410,
 'GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS': 35379,
 'GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS': 35378,
 'GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS_EXT': 35378,
 'GL_MAX_COMBINED_IMAGE_UNIFORMS': 37071,
 'GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS': 36665,
 'GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS_EXT': 36665,
 'GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES': 36665,
 'GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS': 37084,
 'GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS': 36382,
 'GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS_EXT': 36382,
 'GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS': 36383,
 'GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT': 36383,
 'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS': 35661,
 'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB': 35661,
 'GL_MAX_COMBINED_UNIFORM_BLOCKS': 35374,
 'GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS': 35377,
 'GL_MAX_COMPUTE_ATOMIC_COUNTERS': 33381,
 'GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS': 33380,
 'GL_MAX_COMPUTE_FIXED_GROUP_INVOCATIONS_ARB': 37099,
 'GL_MAX_COMPUTE_FIXED_GROUP_SIZE_ARB': 37311,
 'GL_MAX_COMPUTE_IMAGE_UNIFORMS': 37309,
 'GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS': 37083,
 'GL_MAX_COMPUTE_SHARED_MEMORY_SIZE': 33378,
 'GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS': 37308,
 'GL_MAX_COMPUTE_UNIFORM_BLOCKS': 37307,
 'GL_MAX_COMPUTE_UNIFORM_COMPONENTS': 33379,
 'GL_MAX_COMPUTE_VARIABLE_GROUP_INVOCATIONS_ARB': 37700,
 'GL_MAX_COMPUTE_VARIABLE_GROUP_SIZE_ARB': 37701,
 'GL_MAX_COMPUTE_WORK_GROUP_COUNT': 37310,
 'GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS': 37099,
 'GL_MAX_COMPUTE_WORK_GROUP_SIZE': 37311,
 'GL_MAX_CONVOLUTION_HEIGHT': 32795,
 'GL_MAX_CONVOLUTION_HEIGHT_EXT': 32795,
 'GL_MAX_CONVOLUTION_WIDTH': 32794,
 'GL_MAX_CONVOLUTION_WIDTH_EXT': 32794,
 'GL_MAX_CUBE_MAP_TEXTURE_SIZE': 34076,
 'GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB': 34076,
 'GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT': 34076,
 'GL_MAX_CULL_DISTANCES': 33529,
 'GL_MAX_CULL_DISTANCES_EXT': 33529,
 'GL_MAX_DEBUG_GROUP_STACK_DEPTH': 33388,
 'GL_MAX_DEBUG_LOGGED_MESSAGES': 37188,
 'GL_MAX_DEBUG_LOGGED_MESSAGES_ARB': 37188,
 'GL_MAX_DEBUG_MESSAGE_LENGTH': 37187,
 'GL_MAX_DEBUG_MESSAGE_LENGTH_ARB': 37187,
 'GL_MAX_DEPTH': 33408,
 'GL_MAX_DEPTH_TEXTURE_SAMPLES': 37135,
 'GL_MAX_DRAW_BUFFERS': 34852,
 'GL_MAX_DRAW_BUFFERS_ARB': 34852,
 'GL_MAX_DRAW_BUFFERS_EXT': 34852,
 'GL_MAX_DUAL_SOURCE_DRAW_BUFFERS': 35068,
 'GL_MAX_DUAL_SOURCE_DRAW_BUFFERS_EXT': 35068,
 'GL_MAX_ELEMENTS_INDICES': 33001,
 'GL_MAX_ELEMENTS_INDICES_EXT': 33001,
 'GL_MAX_ELEMENTS_VERTICES': 33000,
 'GL_MAX_ELEMENTS_VERTICES_EXT': 33000,
 'GL_MAX_ELEMENT_INDEX': 36203,
 'GL_MAX_EVAL_ORDER': 3376,
 'GL_MAX_EXT': 32776,
 'GL_MAX_FRAGMENT_ATOMIC_COUNTERS': 37590,
 'GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS': 37584,
 'GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT': 36323,
 'GL_MAX_FRAGMENT_IMAGE_UNIFORMS': 37070,
 'GL_MAX_FRAGMENT_INPUT_COMPONENTS': 37157,
 'GL_MAX_FRAGMENT_INTERPOLATION_OFFSET': 36444,
 'GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS': 37082,
 'GL_MAX_FRAGMENT_UNIFORM_BLOCKS': 35373,
 'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS': 35657,
 'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB': 35657,
 'GL_MAX_FRAGMENT_UNIFORM_VECTORS': 36349,
 'GL_MAX_FRAMEBUFFER_HEIGHT': 37654,
 'GL_MAX_FRAMEBUFFER_LAYERS': 37655,
 'GL_MAX_FRAMEBUFFER_LAYERS_EXT': 37655,
 'GL_MAX_FRAMEBUFFER_SAMPLES': 37656,
 'GL_MAX_FRAMEBUFFER_WIDTH': 37653,
 'GL_MAX_GEOMETRY_ATOMIC_COUNTERS': 37589,
 'GL_MAX_GEOMETRY_ATOMIC_COUNTERS_EXT': 37589,
 'GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS': 37583,
 'GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS_EXT': 37583,
 'GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT': 36324,
 'GL_MAX_GEOMETRY_IMAGE_UNIFORMS': 37069,
 'GL_MAX_GEOMETRY_IMAGE_UNIFORMS_EXT': 37069,
 'GL_MAX_GEOMETRY_INPUT_COMPONENTS': 37155,
 'GL_MAX_GEOMETRY_INPUT_COMPONENTS_EXT': 37155,
 'GL_MAX_GEOMETRY_OUTPUT_COMPONENTS': 37156,
 'GL_MAX_GEOMETRY_OUTPUT_COMPONENTS_EXT': 37156,
 'GL_MAX_GEOMETRY_OUTPUT_VERTICES': 36320,
 'GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB': 36320,
 'GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT': 36320,
 'GL_MAX_GEOMETRY_SHADER_INVOCATIONS': 36442,
 'GL_MAX_GEOMETRY_SHADER_INVOCATIONS_EXT': 36442,
 'GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS': 37079,
 'GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS_EXT': 37079,
 'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS': 35881,
 'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB': 35881,
 'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT': 35881,
 'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS': 36321,
 'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB': 36321,
 'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT': 36321,
 'GL_MAX_GEOMETRY_UNIFORM_BLOCKS': 35372,
 'GL_MAX_GEOMETRY_UNIFORM_BLOCKS_EXT': 35372,
 'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS': 36319,
 'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB': 36319,
 'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT': 36319,
 'GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB': 36317,
 'GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT': 36317,
 'GL_MAX_HEIGHT': 33407,
 'GL_MAX_IMAGE_SAMPLES': 36973,
 'GL_MAX_IMAGE_SAMPLES_EXT': 36973,
 'GL_MAX_IMAGE_UNITS': 36664,
 'GL_MAX_IMAGE_UNITS_EXT': 36664,
 'GL_MAX_INTEGER_SAMPLES': 37136,
 'GL_MAX_LABEL_LENGTH': 33512,
 'GL_MAX_LAYERS': 33409,
 'GL_MAX_LGPU_GPUS_NVX': 37562,
 'GL_MAX_LIGHTS': 3377,
 'GL_MAX_LIST_NESTING': 2865,
 'GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB': 34881,
 'GL_MAX_MODELVIEW_STACK_DEPTH': 3382,
 'GL_MAX_MULTIVIEW_BUFFERS_EXT': 37106,
 'GL_MAX_NAME_LENGTH': 37622,
 'GL_MAX_NAME_STACK_DEPTH': 3383,
 'GL_MAX_NUM_ACTIVE_VARIABLES': 37623,
 'GL_MAX_NUM_COMPATIBLE_SUBROUTINES': 37624,
 'GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT': 34762,
 'GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT': 34765,
 'GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT': 34766,
 'GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT': 34764,
 'GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT': 34763,
 'GL_MAX_PALETTE_MATRICES_ARB': 34882,
 'GL_MAX_PATCH_VERTICES': 36477,
 'GL_MAX_PATCH_VERTICES_EXT': 36477,
 'GL_MAX_PIXEL_MAP_TABLE': 3380,
 'GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT': 33591,
 'GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB': 34993,
 'GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB': 34827,
 'GL_MAX_PROGRAM_ATTRIBS_ARB': 34989,
 'GL_MAX_PROGRAM_ENV_PARAMETERS_ARB': 34997,
 'GL_MAX_PROGRAM_INSTRUCTIONS_ARB': 34977,
 'GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB': 34996,
 'GL_MAX_PROGRAM_MATRICES_ARB': 34351,
 'GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB': 34350,
 'GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB': 34995,
 'GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB': 34830,
 'GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB': 34991,
 'GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB': 34979,
 'GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB': 34987,
 'GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB': 34983,
 'GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB': 34832,
 'GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB': 34831,
 'GL_MAX_PROGRAM_PARAMETERS_ARB': 34985,
 'GL_MAX_PROGRAM_TEMPORARIES_ARB': 34981,
 'GL_MAX_PROGRAM_TEXEL_OFFSET': 35077,
 'GL_MAX_PROGRAM_TEXEL_OFFSET_EXT': 35077,
 'GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB': 36767,
 'GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET': 36447,
 'GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB': 36447,
 'GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB': 34829,
 'GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB': 34828,
 'GL_MAX_PROJECTION_STACK_DEPTH': 3384,
 'GL_MAX_RASTER_SAMPLES_EXT': 37673,
 'GL_MAX_RECTANGLE_TEXTURE_SIZE': 34040,
 'GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB': 34040,
 'GL_MAX_RENDERBUFFER_SIZE': 34024,
 'GL_MAX_RENDERBUFFER_SIZE_EXT': 34024,
 'GL_MAX_SAMPLES': 36183,
 'GL_MAX_SAMPLES_ANGLE': 36183,
 'GL_MAX_SAMPLES_EXT': 36183,
 'GL_MAX_SAMPLES_IMG': 37173,
 'GL_MAX_SAMPLE_MASK_WORDS': 36441,
 'GL_MAX_SERVER_WAIT_TIMEOUT': 37137,
 'GL_MAX_SHADER_COMBINED_LOCAL_STORAGE_FAST_SIZE_EXT': 38480,
 'GL_MAX_SHADER_COMBINED_LOCAL_STORAGE_SIZE_EXT': 38481,
 'GL_MAX_SHADER_COMPILER_THREADS_ARB': 37296,
 'GL_MAX_SHADER_PIXEL_LOCAL_STORAGE_FAST_SIZE_EXT': 36707,
 'GL_MAX_SHADER_PIXEL_LOCAL_STORAGE_SIZE_EXT': 36711,
 'GL_MAX_SHADER_STORAGE_BLOCK_SIZE': 37086,
 'GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS': 37085,
 'GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB': 37273,
 'GL_MAX_SPARSE_3D_TEXTURE_SIZE_EXT': 37273,
 'GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS': 37274,
 'GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB': 37274,
 'GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_EXT': 37274,
 'GL_MAX_SPARSE_TEXTURE_SIZE_ARB': 37272,
 'GL_MAX_SPARSE_TEXTURE_SIZE_EXT': 37272,
 'GL_MAX_SUBROUTINES': 36327,
 'GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS': 36328,
 'GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS': 37587,
 'GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS_EXT': 37587,
 'GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS': 37581,
 'GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS_EXT': 37581,
 'GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS': 37067,
 'GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS_EXT': 37067,
 'GL_MAX_TESS_CONTROL_INPUT_COMPONENTS': 34924,
 'GL_MAX_TESS_CONTROL_INPUT_COMPONENTS_EXT': 34924,
 'GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS': 36483,
 'GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS_EXT': 36483,
 'GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS': 37080,
 'GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS_EXT': 37080,
 'GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS': 36481,
 'GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS_EXT': 36481,
 'GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS': 36485,
 'GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS_EXT': 36485,
 'GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS': 36489,
 'GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS_EXT': 36489,
 'GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS': 36479,
 'GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS_EXT': 36479,
 'GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS': 37588,
 'GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS_EXT': 37588,
 'GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS': 37582,
 'GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS_EXT': 37582,
 'GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS': 37068,
 'GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS_EXT': 37068,
 'GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS': 34925,
 'GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS_EXT': 34925,
 'GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS': 36486,
 'GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS_EXT': 36486,
 'GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS': 37081,
 'GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS_EXT': 37081,
 'GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS': 36482,
 'GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS_EXT': 36482,
 'GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS': 36490,
 'GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS_EXT': 36490,
 'GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS': 36480,
 'GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT': 36480,
 'GL_MAX_TESS_GEN_LEVEL': 36478,
 'GL_MAX_TESS_GEN_LEVEL_EXT': 36478,
 'GL_MAX_TESS_PATCH_COMPONENTS': 36484,
 'GL_MAX_TESS_PATCH_COMPONENTS_EXT': 36484,
 'GL_MAX_TEXTURE_BUFFER_SIZE': 35883,
 'GL_MAX_TEXTURE_BUFFER_SIZE_ARB': 35883,
 'GL_MAX_TEXTURE_BUFFER_SIZE_EXT': 35883,
 'GL_MAX_TEXTURE_COORDS': 34929,
 'GL_MAX_TEXTURE_COORDS_ARB': 34929,
 'GL_MAX_TEXTURE_IMAGE_UNITS': 34930,
 'GL_MAX_TEXTURE_IMAGE_UNITS_ARB': 34930,
 'GL_MAX_TEXTURE_LOD_BIAS': 34045,
 'GL_MAX_TEXTURE_LOD_BIAS_EXT': 34045,
 'GL_MAX_TEXTURE_MAX_ANISOTROPY': 34047,
 'GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT': 34047,
 'GL_MAX_TEXTURE_SIZE': 3379,
 'GL_MAX_TEXTURE_STACK_DEPTH': 3385,
 'GL_MAX_TEXTURE_UNITS': 34018,
 'GL_MAX_TEXTURE_UNITS_ARB': 34018,
 'GL_MAX_TRANSFORM_FEEDBACK_BUFFERS': 36464,
 'GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS': 35978,
 'GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT': 35978,
 'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS': 35979,
 'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT': 35979,
 'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS': 35968,
 'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT': 35968,
 'GL_MAX_UNIFORM_BLOCK_SIZE': 35376,
 'GL_MAX_UNIFORM_BUFFER_BINDINGS': 35375,
 'GL_MAX_UNIFORM_LOCATIONS': 33390,
 'GL_MAX_VARYING_COMPONENTS': 35659,
 'GL_MAX_VARYING_COMPONENTS_EXT': 35659,
 'GL_MAX_VARYING_FLOATS': 35659,
 'GL_MAX_VARYING_FLOATS_ARB': 35659,
 'GL_MAX_VARYING_VECTORS': 36348,
 'GL_MAX_VERTEX_ATOMIC_COUNTERS': 37586,
 'GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS': 37580,
 'GL_MAX_VERTEX_ATTRIBS': 34921,
 'GL_MAX_VERTEX_ATTRIBS_ARB': 34921,
 'GL_MAX_VERTEX_ATTRIB_BINDINGS': 33498,
 'GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET': 33497,
 'GL_MAX_VERTEX_ATTRIB_STRIDE': 33509,
 'GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT': 36322,
 'GL_MAX_VERTEX_IMAGE_UNIFORMS': 37066,
 'GL_MAX_VERTEX_OUTPUT_COMPONENTS': 37154,
 'GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT': 34757,
 'GL_MAX_VERTEX_SHADER_INVARIANTS_EXT': 34759,
 'GL_MAX_VERTEX_SHADER_LOCALS_EXT': 34761,
 'GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT': 34760,
 'GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS': 37078,
 'GL_MAX_VERTEX_SHADER_VARIANTS_EXT': 34758,
 'GL_MAX_VERTEX_STREAMS': 36465,
 'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS': 35660,
 'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB': 35660,
 'GL_MAX_VERTEX_UNIFORM_BLOCKS': 35371,
 'GL_MAX_VERTEX_UNIFORM_COMPONENTS': 35658,
 'GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB': 35658,
 'GL_MAX_VERTEX_UNIFORM_VECTORS': 36347,
 'GL_MAX_VERTEX_UNITS_ARB': 34468,
 'GL_MAX_VERTEX_VARYING_COMPONENTS_ARB': 36318,
 'GL_MAX_VERTEX_VARYING_COMPONENTS_EXT': 36318,
 'GL_MAX_VIEWPORTS': 33371,
 'GL_MAX_VIEWPORT_DIMS': 3386,
 'GL_MAX_VIEWS_OVR': 38449,
 'GL_MAX_WIDTH': 33406,
 'GL_MAX_WINDOW_RECTANGLES_EXT': 36628,
 'GL_MEDIUM_FLOAT': 36337,
 'GL_MEDIUM_INT': 36340,
 'GL_MIN': 32775,
 'GL_MINMAX': 32814,
 'GL_MINMAX_EXT': 32814,
 'GL_MINMAX_FORMAT': 32815,
 'GL_MINMAX_FORMAT_EXT': 32815,
 'GL_MINMAX_SINK': 32816,
 'GL_MINMAX_SINK_EXT': 32816,
 'GL_MINOR_VERSION': 33308,
 'GL_MIN_EXT': 32775,
 'GL_MIN_FRAGMENT_INTERPOLATION_OFFSET': 36443,
 'GL_MIN_MAP_BUFFER_ALIGNMENT': 37052,
 'GL_MIN_PROGRAM_TEXEL_OFFSET': 35076,
 'GL_MIN_PROGRAM_TEXEL_OFFSET_EXT': 35076,
 'GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET': 36446,
 'GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB': 36446,
 'GL_MIN_SAMPLE_SHADING_VALUE': 35895,
 'GL_MIN_SAMPLE_SHADING_VALUE_ARB': 35895,
 'GL_MIPMAP': 33427,
 'GL_MIRRORED_REPEAT': 33648,
 'GL_MIRRORED_REPEAT_ARB': 33648,
 'GL_MIRROR_CLAMP_EXT': 34626,
 'GL_MIRROR_CLAMP_TO_BORDER_EXT': 35090,
 'GL_MIRROR_CLAMP_TO_EDGE': 34627,
 'GL_MIRROR_CLAMP_TO_EDGE_EXT': 34627,
 'GL_MODELVIEW': 5888,
 'GL_MODELVIEW0_ARB': 5888,
 'GL_MODELVIEW0_EXT': 5888,
 'GL_MODELVIEW0_MATRIX_EXT': 2982,
 'GL_MODELVIEW0_STACK_DEPTH_EXT': 2979,
 'GL_MODELVIEW10_ARB': 34602,
 'GL_MODELVIEW11_ARB': 34603,
 'GL_MODELVIEW12_ARB': 34604,
 'GL_MODELVIEW13_ARB': 34605,
 'GL_MODELVIEW14_ARB': 34606,
 'GL_MODELVIEW15_ARB': 34607,
 'GL_MODELVIEW16_ARB': 34608,
 'GL_MODELVIEW17_ARB': 34609,
 'GL_MODELVIEW18_ARB': 34610,
 'GL_MODELVIEW19_ARB': 34611,
 'GL_MODELVIEW1_ARB': 34058,
 'GL_MODELVIEW1_EXT': 34058,
 'GL_MODELVIEW1_MATRIX_EXT': 34054,
 'GL_MODELVIEW1_STACK_DEPTH_EXT': 34050,
 'GL_MODELVIEW20_ARB': 34612,
 'GL_MODELVIEW21_ARB': 34613,
 'GL_MODELVIEW22_ARB': 34614,
 'GL_MODELVIEW23_ARB': 34615,
 'GL_MODELVIEW24_ARB': 34616,
 'GL_MODELVIEW25_ARB': 34617,
 'GL_MODELVIEW26_ARB': 34618,
 'GL_MODELVIEW27_ARB': 34619,
 'GL_MODELVIEW28_ARB': 34620,
 'GL_MODELVIEW29_ARB': 34621,
 'GL_MODELVIEW2_ARB': 34594,
 'GL_MODELVIEW30_ARB': 34622,
 'GL_MODELVIEW31_ARB': 34623,
 'GL_MODELVIEW3_ARB': 34595,
 'GL_MODELVIEW4_ARB': 34596,
 'GL_MODELVIEW5_ARB': 34597,
 'GL_MODELVIEW6_ARB': 34598,
 'GL_MODELVIEW7_ARB': 34599,
 'GL_MODELVIEW8_ARB': 34600,
 'GL_MODELVIEW9_ARB': 34601,
 'GL_MODELVIEW_MATRIX': 2982,
 'GL_MODELVIEW_STACK_DEPTH': 2979,
 'GL_MODULATE': 8448,
 'GL_MODULATE_COLOR_IMG': 35844,
 'GL_MULT': 259,
 'GL_MULTIPLY': 37524,
 'GL_MULTISAMPLE': 32925,
 'GL_MULTISAMPLE_3DFX': 34482,
 'GL_MULTISAMPLE_ARB': 32925,
 'GL_MULTISAMPLE_BIT': 536870912,
 'GL_MULTISAMPLE_BIT_3DFX': 536870912,
 'GL_MULTISAMPLE_BIT_ARB': 536870912,
 'GL_MULTISAMPLE_BIT_EXT': 536870912,
 'GL_MULTISAMPLE_EXT': 32925,
 'GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY': 37762,
 'GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY_ARB': 37762,
 'GL_MULTISAMPLE_LINE_WIDTH_RANGE': 37761,
 'GL_MULTISAMPLE_LINE_WIDTH_RANGE_ARB': 37761,
 'GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT': 37675,
 'GL_MULTIVIEW_EXT': 37105,
 'GL_MVP_MATRIX_EXT': 34787,
 'GL_N3F_V3F': 10789,
 'GL_NAMED_STRING_LENGTH_ARB': 36329,
 'GL_NAMED_STRING_TYPE_ARB': 36330,
 'GL_NAME_LENGTH': 37625,
 'GL_NAME_STACK_DEPTH': 3440,
 'GL_NAND': 5390,
 'GL_NEAREST': 9728,
 'GL_NEAREST_MIPMAP_LINEAR': 9986,
 'GL_NEAREST_MIPMAP_NEAREST': 9984,
 'GL_NEGATIVE_ONE_EXT': 34783,
 'GL_NEGATIVE_ONE_TO_ONE': 37726,
 'GL_NEGATIVE_ONE_TO_ONE_EXT': 37726,
 'GL_NEGATIVE_W_EXT': 34780,
 'GL_NEGATIVE_X_EXT': 34777,
 'GL_NEGATIVE_Y_EXT': 34778,
 'GL_NEGATIVE_Z_EXT': 34779,
 'GL_NEVER': 512,
 'GL_NICEST': 4354,
 'GL_NONE': 0,
 'GL_NOOP': 5381,
 'GL_NOR': 5384,
 'GL_NORMALIZE': 2977,
 'GL_NORMALIZED_RANGE_EXT': 34784,
 'GL_NORMAL_ARRAY': 32885,
 'GL_NORMAL_ARRAY_BUFFER_BINDING': 34967,
 'GL_NORMAL_ARRAY_BUFFER_BINDING_ARB': 34967,
 'GL_NORMAL_ARRAY_COUNT_EXT': 32896,
 'GL_NORMAL_ARRAY_EXT': 32885,
 'GL_NORMAL_ARRAY_POINTER': 32911,
 'GL_NORMAL_ARRAY_POINTER_EXT': 32911,
 'GL_NORMAL_ARRAY_STRIDE': 32895,
 'GL_NORMAL_ARRAY_STRIDE_EXT': 32895,
 'GL_NORMAL_ARRAY_TYPE': 32894,
 'GL_NORMAL_ARRAY_TYPE_EXT': 32894,
 'GL_NORMAL_MAP': 34065,
 'GL_NORMAL_MAP_ARB': 34065,
 'GL_NORMAL_MAP_EXT': 34065,
 'GL_NOTEQUAL': 517,
 'GL_NO_ERROR': 0,
 'GL_NO_RESET_NOTIFICATION': 33377,
 'GL_NO_RESET_NOTIFICATION_ARB': 33377,
 'GL_NO_RESET_NOTIFICATION_EXT': 33377,
 'GL_NUM_ACTIVE_VARIABLES': 37636,
 'GL_NUM_COMPATIBLE_SUBROUTINES': 36426,
 'GL_NUM_COMPRESSED_TEXTURE_FORMATS': 34466,
 'GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB': 34466,
 'GL_NUM_DEVICE_UUIDS_EXT': 38294,
 'GL_NUM_DOWNSAMPLE_SCALES_IMG': 37181,
 'GL_NUM_EXTENSIONS': 33309,
 'GL_NUM_PROGRAM_BINARY_FORMATS': 34814,
 'GL_NUM_SAMPLE_COUNTS': 37760,
 'GL_NUM_SHADER_BINARY_FORMATS': 36345,
 'GL_NUM_SHADING_LANGUAGE_VERSIONS': 33513,
 'GL_NUM_SPARSE_LEVELS_ARB': 37290,
 'GL_NUM_SPARSE_LEVELS_EXT': 37290,
 'GL_NUM_SPIR_V_EXTENSIONS': 38228,
 'GL_NUM_TILING_TYPES_EXT': 38274,
 'GL_NUM_VIRTUAL_PAGE_SIZES_ARB': 37288,
 'GL_NUM_VIRTUAL_PAGE_SIZES_EXT': 37288,
 'GL_NUM_WINDOW_RECTANGLES_EXT': 36629,
 'GL_OBJECT_ACTIVE_ATTRIBUTES_ARB': 35721,
 'GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB': 35722,
 'GL_OBJECT_ACTIVE_UNIFORMS_ARB': 35718,
 'GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB': 35719,
 'GL_OBJECT_ATTACHED_OBJECTS_ARB': 35717,
 'GL_OBJECT_COMPILE_STATUS_ARB': 35713,
 'GL_OBJECT_DELETE_STATUS_ARB': 35712,
 'GL_OBJECT_INFO_LOG_LENGTH_ARB': 35716,
 'GL_OBJECT_LINEAR': 9217,
 'GL_OBJECT_LINK_STATUS_ARB': 35714,
 'GL_OBJECT_PLANE': 9473,
 'GL_OBJECT_SHADER_SOURCE_LENGTH_ARB': 35720,
 'GL_OBJECT_SUBTYPE_ARB': 35663,
 'GL_OBJECT_TYPE': 37138,
 'GL_OBJECT_TYPE_ARB': 35662,
 'GL_OBJECT_VALIDATE_STATUS_ARB': 35715,
 'GL_OCCLUSION_TEST_HP': 33125,
 'GL_OCCLUSION_TEST_RESULT_HP': 33126,
 'GL_OFFSET': 37628,
 'GL_ONE': 1,
 'GL_ONE_EXT': 34782,
 'GL_ONE_MINUS_CONSTANT_ALPHA': 32772,
 'GL_ONE_MINUS_CONSTANT_ALPHA_EXT': 32772,
 'GL_ONE_MINUS_CONSTANT_COLOR': 32770,
 'GL_ONE_MINUS_CONSTANT_COLOR_EXT': 32770,
 'GL_ONE_MINUS_DST_ALPHA': 773,
 'GL_ONE_MINUS_DST_COLOR': 775,
 'GL_ONE_MINUS_SRC1_ALPHA': 35067,
 'GL_ONE_MINUS_SRC1_ALPHA_EXT': 35067,
 'GL_ONE_MINUS_SRC1_COLOR': 35066,
 'GL_ONE_MINUS_SRC1_COLOR_EXT': 35066,
 'GL_ONE_MINUS_SRC_ALPHA': 771,
 'GL_ONE_MINUS_SRC_COLOR': 769,
 'GL_OPERAND0_ALPHA': 34200,
 'GL_OPERAND0_ALPHA_ARB': 34200,
 'GL_OPERAND0_ALPHA_EXT': 34200,
 'GL_OPERAND0_RGB': 34192,
 'GL_OPERAND0_RGB_ARB': 34192,
 'GL_OPERAND0_RGB_EXT': 34192,
 'GL_OPERAND1_ALPHA': 34201,
 'GL_OPERAND1_ALPHA_ARB': 34201,
 'GL_OPERAND1_ALPHA_EXT': 34201,
 'GL_OPERAND1_RGB': 34193,
 'GL_OPERAND1_RGB_ARB': 34193,
 'GL_OPERAND1_RGB_EXT': 34193,
 'GL_OPERAND2_ALPHA': 34202,
 'GL_OPERAND2_ALPHA_ARB': 34202,
 'GL_OPERAND2_ALPHA_EXT': 34202,
 'GL_OPERAND2_RGB': 34194,
 'GL_OPERAND2_RGB_ARB': 34194,
 'GL_OPERAND2_RGB_EXT': 34194,
 'GL_OPTIMAL_TILING_EXT': 38276,
 'GL_OP_ADD_EXT': 34695,
 'GL_OP_CLAMP_EXT': 34702,
 'GL_OP_CROSS_PRODUCT_EXT': 34711,
 'GL_OP_DOT3_EXT': 34692,
 'GL_OP_DOT4_EXT': 34693,
 'GL_OP_EXP_BASE_2_EXT': 34705,
 'GL_OP_FLOOR_EXT': 34703,
 'GL_OP_FRAC_EXT': 34697,
 'GL_OP_INDEX_EXT': 34690,
 'GL_OP_LOG_BASE_2_EXT': 34706,
 'GL_OP_MADD_EXT': 34696,
 'GL_OP_MAX_EXT': 34698,
 'GL_OP_MIN_EXT': 34699,
 'GL_OP_MOV_EXT': 34713,
 'GL_OP_MULTIPLY_MATRIX_EXT': 34712,
 'GL_OP_MUL_EXT': 34694,
 'GL_OP_NEGATE_EXT': 34691,
 'GL_OP_POWER_EXT': 34707,
 'GL_OP_RECIP_EXT': 34708,
 'GL_OP_RECIP_SQRT_EXT': 34709,
 'GL_OP_ROUND_EXT': 34704,
 'GL_OP_SET_GE_EXT': 34700,
 'GL_OP_SET_LT_EXT': 34701,
 'GL_OP_SUB_EXT': 34710,
 'GL_OR': 5383,
 'GL_ORDER': 2561,
 'GL_OR_INVERTED': 5389,
 'GL_OR_REVERSE': 5387,
 'GL_OUTPUT_COLOR0_EXT': 34715,
 'GL_OUTPUT_COLOR1_EXT': 34716,
 'GL_OUTPUT_FOG_EXT': 34749,
 'GL_OUTPUT_TEXTURE_COORD0_EXT': 34717,
 'GL_OUTPUT_TEXTURE_COORD10_EXT': 34727,
 'GL_OUTPUT_TEXTURE_COORD11_EXT': 34728,
 'GL_OUTPUT_TEXTURE_COORD12_EXT': 34729,
 'GL_OUTPUT_TEXTURE_COORD13_EXT': 34730,
 'GL_OUTPUT_TEXTURE_COORD14_EXT': 34731,
 'GL_OUTPUT_TEXTURE_COORD15_EXT': 34732,
 'GL_OUTPUT_TEXTURE_COORD16_EXT': 34733,
 'GL_OUTPUT_TEXTURE_COORD17_EXT': 34734,
 'GL_OUTPUT_TEXTURE_COORD18_EXT': 34735,
 'GL_OUTPUT_TEXTURE_COORD19_EXT': 34736,
 'GL_OUTPUT_TEXTURE_COORD1_EXT': 34718,
 'GL_OUTPUT_TEXTURE_COORD20_EXT': 34737,
 'GL_OUTPUT_TEXTURE_COORD21_EXT': 34738,
 'GL_OUTPUT_TEXTURE_COORD22_EXT': 34739,
 'GL_OUTPUT_TEXTURE_COORD23_EXT': 34740,
 'GL_OUTPUT_TEXTURE_COORD24_EXT': 34741,
 'GL_OUTPUT_TEXTURE_COORD25_EXT': 34742,
 'GL_OUTPUT_TEXTURE_COORD26_EXT': 34743,
 'GL_OUTPUT_TEXTURE_COORD27_EXT': 34744,
 'GL_OUTPUT_TEXTURE_COORD28_EXT': 34745,
 'GL_OUTPUT_TEXTURE_COORD29_EXT': 34746,
 'GL_OUTPUT_TEXTURE_COORD2_EXT': 34719,
 'GL_OUTPUT_TEXTURE_COORD30_EXT': 34747,
 'GL_OUTPUT_TEXTURE_COORD31_EXT': 34748,
 'GL_OUTPUT_TEXTURE_COORD3_EXT': 34720,
 'GL_OUTPUT_TEXTURE_COORD4_EXT': 34721,
 'GL_OUTPUT_TEXTURE_COORD5_EXT': 34722,
 'GL_OUTPUT_TEXTURE_COORD6_EXT': 34723,
 'GL_OUTPUT_TEXTURE_COORD7_EXT': 34724,
 'GL_OUTPUT_TEXTURE_COORD8_EXT': 34725,
 'GL_OUTPUT_TEXTURE_COORD9_EXT': 34726,
 'GL_OUTPUT_VERTEX_EXT': 34714,
 'GL_OUT_OF_MEMORY': 1285,
 'GL_OVERLAY': 37526,
 'GL_PACK_ALIGNMENT': 3333,
 'GL_PACK_CMYK_HINT_EXT': 32782,
 'GL_PACK_COMPRESSED_BLOCK_DEPTH': 37165,
 'GL_PACK_COMPRESSED_BLOCK_HEIGHT': 37164,
 'GL_PACK_COMPRESSED_BLOCK_SIZE': 37166,
 'GL_PACK_COMPRESSED_BLOCK_WIDTH': 37163,
 'GL_PACK_IMAGE_HEIGHT': 32876,
 'GL_PACK_IMAGE_HEIGHT_EXT': 32876,
 'GL_PACK_LSB_FIRST': 3329,
 'GL_PACK_RESAMPLE_OML': 35204,
 'GL_PACK_REVERSE_ROW_ORDER_ANGLE': 37796,
 'GL_PACK_ROW_LENGTH': 3330,
 'GL_PACK_SKIP_IMAGES': 32875,
 'GL_PACK_SKIP_IMAGES_EXT': 32875,
 'GL_PACK_SKIP_PIXELS': 3332,
 'GL_PACK_SKIP_ROWS': 3331,
 'GL_PACK_SWAP_BYTES': 3328,
 'GL_PARAMETER_BUFFER': 33006,
 'GL_PARAMETER_BUFFER_ARB': 33006,
 'GL_PARAMETER_BUFFER_BINDING': 33007,
 'GL_PARAMETER_BUFFER_BINDING_ARB': 33007,
 'GL_PASS_THROUGH_TOKEN': 1792,
 'GL_PATCHES': 14,
 'GL_PATCHES_EXT': 14,
 'GL_PATCH_DEFAULT_INNER_LEVEL': 36467,
 'GL_PATCH_DEFAULT_INNER_LEVEL_EXT': 36467,
 'GL_PATCH_DEFAULT_OUTER_LEVEL': 36468,
 'GL_PATCH_DEFAULT_OUTER_LEVEL_EXT': 36468,
 'GL_PATCH_VERTICES': 36466,
 'GL_PATCH_VERTICES_EXT': 36466,
 'GL_PERSPECTIVE_CORRECTION_HINT': 3152,
 'GL_PERTURB_EXT': 34222,
 'GL_PHONG_HINT_WIN': 33003,
 'GL_PHONG_WIN': 33002,
 'GL_PIXEL_BUFFER_BARRIER_BIT': 128,
 'GL_PIXEL_BUFFER_BARRIER_BIT_EXT': 128,
 'GL_PIXEL_CUBIC_WEIGHT_EXT': 33587,
 'GL_PIXEL_MAG_FILTER_EXT': 33585,
 'GL_PIXEL_MAP_A_TO_A': 3193,
 'GL_PIXEL_MAP_A_TO_A_SIZE': 3257,
 'GL_PIXEL_MAP_B_TO_B': 3192,
 'GL_PIXEL_MAP_B_TO_B_SIZE': 3256,
 'GL_PIXEL_MAP_G_TO_G': 3191,
 'GL_PIXEL_MAP_G_TO_G_SIZE': 3255,
 'GL_PIXEL_MAP_I_TO_A': 3189,
 'GL_PIXEL_MAP_I_TO_A_SIZE': 3253,
 'GL_PIXEL_MAP_I_TO_B': 3188,
 'GL_PIXEL_MAP_I_TO_B_SIZE': 3252,
 'GL_PIXEL_MAP_I_TO_G': 3187,
 'GL_PIXEL_MAP_I_TO_G_SIZE': 3251,
 'GL_PIXEL_MAP_I_TO_I': 3184,
 'GL_PIXEL_MAP_I_TO_I_SIZE': 3248,
 'GL_PIXEL_MAP_I_TO_R': 3186,
 'GL_PIXEL_MAP_I_TO_R_SIZE': 3250,
 'GL_PIXEL_MAP_R_TO_R': 3190,
 'GL_PIXEL_MAP_R_TO_R_SIZE': 3254,
 'GL_PIXEL_MAP_S_TO_S': 3185,
 'GL_PIXEL_MAP_S_TO_S_SIZE': 3249,
 'GL_PIXEL_MIN_FILTER_EXT': 33586,
 'GL_PIXEL_MODE_BIT': 32,
 'GL_PIXEL_PACK_BUFFER': 35051,
 'GL_PIXEL_PACK_BUFFER_ARB': 35051,
 'GL_PIXEL_PACK_BUFFER_BINDING': 35053,
 'GL_PIXEL_PACK_BUFFER_BINDING_ARB': 35053,
 'GL_PIXEL_PACK_BUFFER_BINDING_EXT': 35053,
 'GL_PIXEL_PACK_BUFFER_EXT': 35051,
 'GL_PIXEL_TRANSFORM_2D_EXT': 33584,
 'GL_PIXEL_TRANSFORM_2D_MATRIX_EXT': 33592,
 'GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT': 33590,
 'GL_PIXEL_UNPACK_BUFFER': 35052,
 'GL_PIXEL_UNPACK_BUFFER_ARB': 35052,
 'GL_PIXEL_UNPACK_BUFFER_BINDING': 35055,
 'GL_PIXEL_UNPACK_BUFFER_BINDING_ARB': 35055,
 'GL_PIXEL_UNPACK_BUFFER_BINDING_EXT': 35055,
 'GL_PIXEL_UNPACK_BUFFER_EXT': 35052,
 'GL_POINT': 6912,
 'GL_POINTS': 0,
 'GL_POINT_BIT': 2,
 'GL_POINT_DISTANCE_ATTENUATION': 33065,
 'GL_POINT_DISTANCE_ATTENUATION_ARB': 33065,
 'GL_POINT_FADE_THRESHOLD_SIZE': 33064,
 'GL_POINT_FADE_THRESHOLD_SIZE_ARB': 33064,
 'GL_POINT_FADE_THRESHOLD_SIZE_EXT': 33064,
 'GL_POINT_SIZE': 2833,
 'GL_POINT_SIZE_GRANULARITY': 2835,
 'GL_POINT_SIZE_MAX': 33063,
 'GL_POINT_SIZE_MAX_ARB': 33063,
 'GL_POINT_SIZE_MAX_EXT': 33063,
 'GL_POINT_SIZE_MIN': 33062,
 'GL_POINT_SIZE_MIN_ARB': 33062,
 'GL_POINT_SIZE_MIN_EXT': 33062,
 'GL_POINT_SIZE_RANGE': 2834,
 'GL_POINT_SMOOTH': 2832,
 'GL_POINT_SMOOTH_HINT': 3153,
 'GL_POINT_SPRITE': 34913,
 'GL_POINT_SPRITE_ARB': 34913,
 'GL_POINT_SPRITE_COORD_ORIGIN': 36000,
 'GL_POINT_TOKEN': 1793,
 'GL_POLYGON': 9,
 'GL_POLYGON_BIT': 8,
 'GL_POLYGON_MODE': 2880,
 'GL_POLYGON_OFFSET_BIAS_EXT': 32825,
 'GL_POLYGON_OFFSET_CLAMP': 36379,
 'GL_POLYGON_OFFSET_CLAMP_EXT': 36379,
 'GL_POLYGON_OFFSET_EXT': 32823,
 'GL_POLYGON_OFFSET_FACTOR': 32824,
 'GL_POLYGON_OFFSET_FACTOR_EXT': 32824,
 'GL_POLYGON_OFFSET_FILL': 32823,
 'GL_POLYGON_OFFSET_LINE': 10754,
 'GL_POLYGON_OFFSET_POINT': 10753,
 'GL_POLYGON_OFFSET_UNITS': 10752,
 'GL_POLYGON_SMOOTH': 2881,
 'GL_POLYGON_SMOOTH_HINT': 3155,
 'GL_POLYGON_STIPPLE': 2882,
 'GL_POLYGON_STIPPLE_BIT': 16,
 'GL_POLYGON_TOKEN': 1795,
 'GL_POSITION': 4611,
 'GL_POST_COLOR_MATRIX_ALPHA_BIAS': 32955,
 'GL_POST_COLOR_MATRIX_ALPHA_SCALE': 32951,
 'GL_POST_COLOR_MATRIX_BLUE_BIAS': 32954,
 'GL_POST_COLOR_MATRIX_BLUE_SCALE': 32950,
 'GL_POST_COLOR_MATRIX_COLOR_TABLE': 32978,
 'GL_POST_COLOR_MATRIX_GREEN_BIAS': 32953,
 'GL_POST_COLOR_MATRIX_GREEN_SCALE': 32949,
 'GL_POST_COLOR_MATRIX_RED_BIAS': 32952,
 'GL_POST_COLOR_MATRIX_RED_SCALE': 32948,
 'GL_POST_CONVOLUTION_ALPHA_BIAS': 32803,
 'GL_POST_CONVOLUTION_ALPHA_BIAS_EXT': 32803,
 'GL_POST_CONVOLUTION_ALPHA_SCALE': 32799,
 'GL_POST_CONVOLUTION_ALPHA_SCALE_EXT': 32799,
 'GL_POST_CONVOLUTION_BLUE_BIAS': 32802,
 'GL_POST_CONVOLUTION_BLUE_BIAS_EXT': 32802,
 'GL_POST_CONVOLUTION_BLUE_SCALE': 32798,
 'GL_POST_CONVOLUTION_BLUE_SCALE_EXT': 32798,
 'GL_POST_CONVOLUTION_COLOR_TABLE': 32977,
 'GL_POST_CONVOLUTION_GREEN_BIAS': 32801,
 'GL_POST_CONVOLUTION_GREEN_BIAS_EXT': 32801,
 'GL_POST_CONVOLUTION_GREEN_SCALE': 32797,
 'GL_POST_CONVOLUTION_GREEN_SCALE_EXT': 32797,
 'GL_POST_CONVOLUTION_RED_BIAS': 32800,
 'GL_POST_CONVOLUTION_RED_BIAS_EXT': 32800,
 'GL_POST_CONVOLUTION_RED_SCALE': 32796,
 'GL_POST_CONVOLUTION_RED_SCALE_EXT': 32796,
 'GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP': 33122,
 'GL_PREVIOUS': 34168,
 'GL_PREVIOUS_ARB': 34168,
 'GL_PREVIOUS_EXT': 34168,
 'GL_PRIMARY_COLOR': 34167,
 'GL_PRIMARY_COLOR_ARB': 34167,
 'GL_PRIMARY_COLOR_EXT': 34167,
 'GL_PRIMITIVES_GENERATED': 35975,
 'GL_PRIMITIVES_GENERATED_EXT': 35975,
 'GL_PRIMITIVES_SUBMITTED': 33519,
 'GL_PRIMITIVES_SUBMITTED_ARB': 33519,
 'GL_PRIMITIVE_BOUNDING_BOX': 37566,
 'GL_PRIMITIVE_BOUNDING_BOX_ARB': 37566,
 'GL_PRIMITIVE_BOUNDING_BOX_EXT': 37566,
 'GL_PRIMITIVE_RESTART': 36765,
 'GL_PRIMITIVE_RESTART_FIXED_INDEX': 36201,
 'GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED': 33313,
 'GL_PRIMITIVE_RESTART_INDEX': 36766,
 'GL_PROGRAM': 33506,
 'GL_PROGRAMMABLE_SAMPLE_LOCATION_ARB': 37697,
 'GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_ARB': 37696,
 'GL_PROGRAM_ADDRESS_REGISTERS_ARB': 34992,
 'GL_PROGRAM_ALU_INSTRUCTIONS_ARB': 34821,
 'GL_PROGRAM_ATTRIBS_ARB': 34988,
 'GL_PROGRAM_BINARY_ANGLE': 37798,
 'GL_PROGRAM_BINARY_FORMATS': 34815,
 'GL_PROGRAM_BINARY_LENGTH': 34625,
 'GL_PROGRAM_BINARY_RETRIEVABLE_HINT': 33367,
 'GL_PROGRAM_BINDING_ARB': 34423,
 'GL_PROGRAM_ERROR_POSITION_ARB': 34379,
 'GL_PROGRAM_ERROR_STRING_ARB': 34932,
 'GL_PROGRAM_FORMAT_ARB': 34934,
 'GL_PROGRAM_FORMAT_ASCII_ARB': 34933,
 'GL_PROGRAM_INPUT': 37603,
 'GL_PROGRAM_INSTRUCTIONS_ARB': 34976,
 'GL_PROGRAM_LENGTH_ARB': 34343,
 'GL_PROGRAM_MATRIX_EXT': 36397,
 'GL_PROGRAM_MATRIX_STACK_DEPTH_EXT': 36399,
 'GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB': 34994,
 'GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB': 34824,
 'GL_PROGRAM_NATIVE_ATTRIBS_ARB': 34990,
 'GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB': 34978,
 'GL_PROGRAM_NATIVE_PARAMETERS_ARB': 34986,
 'GL_PROGRAM_NATIVE_TEMPORARIES_ARB': 34982,
 'GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB': 34826,
 'GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB': 34825,
 'GL_PROGRAM_OBJECT_ARB': 35648,
 'GL_PROGRAM_OBJECT_EXT': 35648,
 'GL_PROGRAM_OUTPUT': 37604,
 'GL_PROGRAM_PARAMETERS_ARB': 34984,
 'GL_PROGRAM_PIPELINE': 33508,
 'GL_PROGRAM_PIPELINE_BINDING': 33370,
 'GL_PROGRAM_PIPELINE_BINDING_EXT': 33370,
 'GL_PROGRAM_PIPELINE_OBJECT_EXT': 35407,
 'GL_PROGRAM_POINT_SIZE': 34370,
 'GL_PROGRAM_POINT_SIZE_ARB': 34370,
 'GL_PROGRAM_POINT_SIZE_EXT': 34370,
 'GL_PROGRAM_SEPARABLE': 33368,
 'GL_PROGRAM_SEPARABLE_EXT': 33368,
 'GL_PROGRAM_STRING_ARB': 34344,
 'GL_PROGRAM_TEMPORARIES_ARB': 34980,
 'GL_PROGRAM_TEX_INDIRECTIONS_ARB': 34823,
 'GL_PROGRAM_TEX_INSTRUCTIONS_ARB': 34822,
 'GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB': 34998,
 'GL_PROJECTION': 5889,
 'GL_PROJECTION_MATRIX': 2983,
 'GL_PROJECTION_STACK_DEPTH': 2980,
 'GL_PROTECTED_MEMORY_OBJECT_EXT': 38299,
 'GL_PROVOKING_VERTEX': 36431,
 'GL_PROVOKING_VERTEX_EXT': 36431,
 'GL_PROXY_COLOR_TABLE': 32979,
 'GL_PROXY_HISTOGRAM': 32805,
 'GL_PROXY_HISTOGRAM_EXT': 32805,
 'GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE': 32981,
 'GL_PROXY_POST_CONVOLUTION_COLOR_TABLE': 32980,
 'GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP': 33123,
 'GL_PROXY_TEXTURE_1D': 32867,
 'GL_PROXY_TEXTURE_1D_ARRAY': 35865,
 'GL_PROXY_TEXTURE_1D_ARRAY_EXT': 35865,
 'GL_PROXY_TEXTURE_1D_EXT': 32867,
 'GL_PROXY_TEXTURE_1D_STACK_MESAX': 34651,
 'GL_PROXY_TEXTURE_2D': 32868,
 'GL_PROXY_TEXTURE_2D_ARRAY': 35867,
 'GL_PROXY_TEXTURE_2D_ARRAY_EXT': 35867,
 'GL_PROXY_TEXTURE_2D_EXT': 32868,
 'GL_PROXY_TEXTURE_2D_MULTISAMPLE': 37121,
 'GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY': 37123,
 'GL_PROXY_TEXTURE_2D_STACK_MESAX': 34652,
 'GL_PROXY_TEXTURE_3D': 32880,
 'GL_PROXY_TEXTURE_3D_EXT': 32880,
 'GL_PROXY_TEXTURE_CUBE_MAP': 34075,
 'GL_PROXY_TEXTURE_CUBE_MAP_ARB': 34075,
 'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY': 36875,
 'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB': 36875,
 'GL_PROXY_TEXTURE_CUBE_MAP_EXT': 34075,
 'GL_PROXY_TEXTURE_RECTANGLE': 34039,
 'GL_PROXY_TEXTURE_RECTANGLE_ARB': 34039,
 'GL_Q': 8195,
 'GL_QUADRATIC_ATTENUATION': 4617,
 'GL_QUADS': 7,
 'GL_QUADS_EXT': 7,
 'GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION': 36428,
 'GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION_EXT': 36428,
 'GL_QUAD_STRIP': 8,
 'GL_QUERY': 33507,
 'GL_QUERY_BUFFER': 37266,
 'GL_QUERY_BUFFER_BARRIER_BIT': 32768,
 'GL_QUERY_BUFFER_BINDING': 37267,
 'GL_QUERY_BY_REGION_NO_WAIT': 36374,
 'GL_QUERY_BY_REGION_NO_WAIT_INVERTED': 36378,
 'GL_QUERY_BY_REGION_WAIT': 36373,
 'GL_QUERY_BY_REGION_WAIT_INVERTED': 36377,
 'GL_QUERY_COUNTER_BITS': 34916,
 'GL_QUERY_COUNTER_BITS_ARB': 34916,
 'GL_QUERY_COUNTER_BITS_EXT': 34916,
 'GL_QUERY_NO_WAIT': 36372,
 'GL_QUERY_NO_WAIT_INVERTED': 36376,
 'GL_QUERY_OBJECT_EXT': 37203,
 'GL_QUERY_RESULT': 34918,
 'GL_QUERY_RESULT_ARB': 34918,
 'GL_QUERY_RESULT_AVAILABLE': 34919,
 'GL_QUERY_RESULT_AVAILABLE_ARB': 34919,
 'GL_QUERY_RESULT_AVAILABLE_EXT': 34919,
 'GL_QUERY_RESULT_EXT': 34918,
 'GL_QUERY_RESULT_NO_WAIT': 37268,
 'GL_QUERY_TARGET': 33514,
 'GL_QUERY_WAIT': 36371,
 'GL_QUERY_WAIT_INVERTED': 36375,
 'GL_R': 8194,
 'GL_R11F_G11F_B10F': 35898,
 'GL_R11F_G11F_B10F_EXT': 35898,
 'GL_R16': 33322,
 'GL_R16F': 33325,
 'GL_R16F_EXT': 33325,
 'GL_R16I': 33331,
 'GL_R16UI': 33332,
 'GL_R16_EXT': 33322,
 'GL_R16_SNORM': 36760,
 'GL_R16_SNORM_EXT': 36760,
 'GL_R32F': 33326,
 'GL_R32F_EXT': 33326,
 'GL_R32I': 33333,
 'GL_R32UI': 33334,
 'GL_R3_G3_B2': 10768,
 'GL_R8': 33321,
 'GL_R8I': 33329,
 'GL_R8UI': 33330,
 'GL_R8_EXT': 33321,
 'GL_R8_SNORM': 36756,
 'GL_RASTERIZER_DISCARD': 35977,
 'GL_RASTERIZER_DISCARD_EXT': 35977,
 'GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT': 37674,
 'GL_RASTER_MULTISAMPLE_EXT': 37671,
 'GL_RASTER_SAMPLES_EXT': 37672,
 'GL_READ_BUFFER': 3074,
 'GL_READ_BUFFER_EXT': 3074,
 'GL_READ_FRAMEBUFFER': 36008,
 'GL_READ_FRAMEBUFFER_ANGLE': 36008,
 'GL_READ_FRAMEBUFFER_BINDING': 36010,
 'GL_READ_FRAMEBUFFER_BINDING_ANGLE': 36010,
 'GL_READ_FRAMEBUFFER_BINDING_EXT': 36010,
 'GL_READ_FRAMEBUFFER_EXT': 36008,
 'GL_READ_ONLY': 35000,
 'GL_READ_ONLY_ARB': 35000,
 'GL_READ_PIXELS': 33420,
 'GL_READ_PIXELS_FORMAT': 33421,
 'GL_READ_PIXELS_TYPE': 33422,
 'GL_READ_WRITE': 35002,
 'GL_READ_WRITE_ARB': 35002,
 'GL_RECIP_ADD_SIGNED_ALPHA_IMG': 35845,
 'GL_RED': 6403,
 'GL_REDUCE': 32790,
 'GL_REDUCE_EXT': 32790,
 'GL_RED_BIAS': 3349,
 'GL_RED_BITS': 3410,
 'GL_RED_EXT': 6403,
 'GL_RED_INTEGER': 36244,
 'GL_RED_INTEGER_EXT': 36244,
 'GL_RED_MAX_CLAMP_INGR': 34148,
 'GL_RED_MIN_CLAMP_INGR': 34144,
 'GL_RED_SCALE': 3348,
 'GL_RED_SNORM': 36752,
 'GL_REFERENCED_BY_COMPUTE_SHADER': 37643,
 'GL_REFERENCED_BY_FRAGMENT_SHADER': 37642,
 'GL_REFERENCED_BY_GEOMETRY_SHADER': 37641,
 'GL_REFERENCED_BY_GEOMETRY_SHADER_EXT': 37641,
 'GL_REFERENCED_BY_TESS_CONTROL_SHADER': 37639,
 'GL_REFERENCED_BY_TESS_CONTROL_SHADER_EXT': 37639,
 'GL_REFERENCED_BY_TESS_EVALUATION_SHADER': 37640,
 'GL_REFERENCED_BY_TESS_EVALUATION_SHADER_EXT': 37640,
 'GL_REFERENCED_BY_VERTEX_SHADER': 37638,
 'GL_REFLECTION_MAP': 34066,
 'GL_REFLECTION_MAP_ARB': 34066,
 'GL_REFLECTION_MAP_EXT': 34066,
 'GL_RENDER': 7168,
 'GL_RENDERBUFFER': 36161,
 'GL_RENDERBUFFER_ALPHA_SIZE': 36179,
 'GL_RENDERBUFFER_ALPHA_SIZE_EXT': 36179,
 'GL_RENDERBUFFER_BINDING': 36007,
 'GL_RENDERBUFFER_BINDING_ANGLE': 36007,
 'GL_RENDERBUFFER_BINDING_EXT': 36007,
 'GL_RENDERBUFFER_BLUE_SIZE': 36178,
 'GL_RENDERBUFFER_BLUE_SIZE_EXT': 36178,
 'GL_RENDERBUFFER_DEPTH_SIZE': 36180,
 'GL_RENDERBUFFER_DEPTH_SIZE_EXT': 36180,
 'GL_RENDERBUFFER_EXT': 36161,
 'GL_RENDERBUFFER_GREEN_SIZE': 36177,
 'GL_RENDERBUFFER_GREEN_SIZE_EXT': 36177,
 'GL_RENDERBUFFER_HEIGHT': 36163,
 'GL_RENDERBUFFER_HEIGHT_EXT': 36163,
 'GL_RENDERBUFFER_INTERNAL_FORMAT': 36164,
 'GL_RENDERBUFFER_INTERNAL_FORMAT_EXT': 36164,
 'GL_RENDERBUFFER_RED_SIZE': 36176,
 'GL_RENDERBUFFER_RED_SIZE_EXT': 36176,
 'GL_RENDERBUFFER_SAMPLES': 36011,
 'GL_RENDERBUFFER_SAMPLES_ANGLE': 36011,
 'GL_RENDERBUFFER_SAMPLES_EXT': 36011,
 'GL_RENDERBUFFER_SAMPLES_IMG': 37171,
 'GL_RENDERBUFFER_STENCIL_SIZE': 36181,
 'GL_RENDERBUFFER_STENCIL_SIZE_EXT': 36181,
 'GL_RENDERBUFFER_WIDTH': 36162,
 'GL_RENDERBUFFER_WIDTH_EXT': 36162,
 'GL_RENDERER': 7937,
 'GL_RENDER_MODE': 3136,
 'GL_REPEAT': 10497,
 'GL_REPLACE': 7681,
 'GL_REPLACE_EXT': 32866,
 'GL_REPLICATE_BORDER': 33107,
 'GL_REPLICATE_BORDER_HP': 33107,
 'GL_RESAMPLE_AVERAGE_OML': 35208,
 'GL_RESAMPLE_DECIMATE_OML': 35209,
 'GL_RESAMPLE_REPLICATE_OML': 35206,
 'GL_RESAMPLE_ZERO_FILL_OML': 35207,
 'GL_RESCALE_NORMAL': 32826,
 'GL_RESCALE_NORMAL_EXT': 32826,
 'GL_RESET_NOTIFICATION_STRATEGY': 33366,
 'GL_RESET_NOTIFICATION_STRATEGY_ARB': 33366,
 'GL_RESET_NOTIFICATION_STRATEGY_EXT': 33366,
 'GL_RETURN': 258,
 'GL_RG': 33319,
 'GL_RG16': 33324,
 'GL_RG16F': 33327,
 'GL_RG16F_EXT': 33327,
 'GL_RG16I': 33337,
 'GL_RG16UI': 33338,
 'GL_RG16_EXT': 33324,
 'GL_RG16_SNORM': 36761,
 'GL_RG16_SNORM_EXT': 36761,
 'GL_RG32F': 33328,
 'GL_RG32F_EXT': 33328,
 'GL_RG32I': 33339,
 'GL_RG32UI': 33340,
 'GL_RG8': 33323,
 'GL_RG8I': 33335,
 'GL_RG8UI': 33336,
 'GL_RG8_EXT': 33323,
 'GL_RG8_SNORM': 36757,
 'GL_RGB': 6407,
 'GL_RGB10': 32850,
 'GL_RGB10_A2': 32857,
 'GL_RGB10_A2UI': 36975,
 'GL_RGB10_A2_EXT': 32857,
 'GL_RGB10_EXT': 32850,
 'GL_RGB12': 32851,
 'GL_RGB12_EXT': 32851,
 'GL_RGB16': 32852,
 'GL_RGB16F': 34843,
 'GL_RGB16F_ARB': 34843,
 'GL_RGB16F_EXT': 34843,
 'GL_RGB16I': 36233,
 'GL_RGB16I_EXT': 36233,
 'GL_RGB16UI': 36215,
 'GL_RGB16UI_EXT': 36215,
 'GL_RGB16_EXT': 32852,
 'GL_RGB16_SNORM': 36762,
 'GL_RGB16_SNORM_EXT': 36762,
 'GL_RGB2_EXT': 32846,
 'GL_RGB32F': 34837,
 'GL_RGB32F_ARB': 34837,
 'GL_RGB32F_EXT': 34837,
 'GL_RGB32I': 36227,
 'GL_RGB32I_EXT': 36227,
 'GL_RGB32UI': 36209,
 'GL_RGB32UI_EXT': 36209,
 'GL_RGB4': 32847,
 'GL_RGB4_EXT': 32847,
 'GL_RGB4_S3TC': 33697,
 'GL_RGB5': 32848,
 'GL_RGB565': 36194,
 'GL_RGB5_A1': 32855,
 'GL_RGB5_A1_EXT': 32855,
 'GL_RGB5_EXT': 32848,
 'GL_RGB8': 32849,
 'GL_RGB8I': 36239,
 'GL_RGB8I_EXT': 36239,
 'GL_RGB8UI': 36221,
 'GL_RGB8UI_EXT': 36221,
 'GL_RGB8_EXT': 32849,
 'GL_RGB8_SNORM': 36758,
 'GL_RGB9_E5': 35901,
 'GL_RGB9_E5_EXT': 35901,
 'GL_RGBA': 6408,
 'GL_RGBA12': 32858,
 'GL_RGBA12_EXT': 32858,
 'GL_RGBA16': 32859,
 'GL_RGBA16F': 34842,
 'GL_RGBA16F_ARB': 34842,
 'GL_RGBA16F_EXT': 34842,
 'GL_RGBA16I': 36232,
 'GL_RGBA16I_EXT': 36232,
 'GL_RGBA16UI': 36214,
 'GL_RGBA16UI_EXT': 36214,
 'GL_RGBA16_EXT': 32859,
 'GL_RGBA16_SNORM': 36763,
 'GL_RGBA16_SNORM_EXT': 36763,
 'GL_RGBA2': 32853,
 'GL_RGBA2_EXT': 32853,
 'GL_RGBA32F': 34836,
 'GL_RGBA32F_ARB': 34836,
 'GL_RGBA32F_EXT': 34836,
 'GL_RGBA32I': 36226,
 'GL_RGBA32I_EXT': 36226,
 'GL_RGBA32UI': 36208,
 'GL_RGBA32UI_EXT': 36208,
 'GL_RGBA4': 32854,
 'GL_RGBA4_DXT5_S3TC': 33701,
 'GL_RGBA4_EXT': 32854,
 'GL_RGBA4_S3TC': 33699,
 'GL_RGBA8': 32856,
 'GL_RGBA8I': 36238,
 'GL_RGBA8I_EXT': 36238,
 'GL_RGBA8UI': 36220,
 'GL_RGBA8UI_EXT': 36220,
 'GL_RGBA8_EXT': 32856,
 'GL_RGBA8_SNORM': 36759,
 'GL_RGBA_DXT5_S3TC': 33700,
 'GL_RGBA_FLOAT_MODE_ARB': 34848,
 'GL_RGBA_INTEGER': 36249,
 'GL_RGBA_INTEGER_EXT': 36249,
 'GL_RGBA_INTEGER_MODE_EXT': 36254,
 'GL_RGBA_MODE': 3121,
 'GL_RGBA_S3TC': 33698,
 'GL_RGBA_SIGNED_COMPONENTS_EXT': 35900,
 'GL_RGBA_SNORM': 36755,
 'GL_RGB_INTEGER': 36248,
 'GL_RGB_INTEGER_EXT': 36248,
 'GL_RGB_S3TC': 33696,
 'GL_RGB_SCALE': 34163,
 'GL_RGB_SCALE_ARB': 34163,
 'GL_RGB_SCALE_EXT': 34163,
 'GL_RGB_SNORM': 36754,
 'GL_RG_EXT': 33319,
 'GL_RG_INTEGER': 33320,
 'GL_RG_SNORM': 36753,
 'GL_RIGHT': 1031,
 'GL_S': 8192,
 'GL_SAMPLER': 33510,
 'GL_SAMPLER_1D': 35677,
 'GL_SAMPLER_1D_ARB': 35677,
 'GL_SAMPLER_1D_ARRAY': 36288,
 'GL_SAMPLER_1D_ARRAY_EXT': 36288,
 'GL_SAMPLER_1D_ARRAY_SHADOW': 36291,
 'GL_SAMPLER_1D_ARRAY_SHADOW_EXT': 36291,
 'GL_SAMPLER_1D_SHADOW': 35681,
 'GL_SAMPLER_1D_SHADOW_ARB': 35681,
 'GL_SAMPLER_2D': 35678,
 'GL_SAMPLER_2D_ARB': 35678,
 'GL_SAMPLER_2D_ARRAY': 36289,
 'GL_SAMPLER_2D_ARRAY_EXT': 36289,
 'GL_SAMPLER_2D_ARRAY_SHADOW': 36292,
 'GL_SAMPLER_2D_ARRAY_SHADOW_EXT': 36292,
 'GL_SAMPLER_2D_MULTISAMPLE': 37128,
 'GL_SAMPLER_2D_MULTISAMPLE_ARRAY': 37131,
 'GL_SAMPLER_2D_RECT': 35683,
 'GL_SAMPLER_2D_RECT_ARB': 35683,
 'GL_SAMPLER_2D_RECT_SHADOW': 35684,
 'GL_SAMPLER_2D_RECT_SHADOW_ARB': 35684,
 'GL_SAMPLER_2D_SHADOW': 35682,
 'GL_SAMPLER_2D_SHADOW_ARB': 35682,
 'GL_SAMPLER_2D_SHADOW_EXT': 35682,
 'GL_SAMPLER_3D': 35679,
 'GL_SAMPLER_3D_ARB': 35679,
 'GL_SAMPLER_BINDING': 35097,
 'GL_SAMPLER_BUFFER': 36290,
 'GL_SAMPLER_BUFFER_EXT': 36290,
 'GL_SAMPLER_CUBE': 35680,
 'GL_SAMPLER_CUBE_ARB': 35680,
 'GL_SAMPLER_CUBE_MAP_ARRAY': 36876,
 'GL_SAMPLER_CUBE_MAP_ARRAY_ARB': 36876,
 'GL_SAMPLER_CUBE_MAP_ARRAY_EXT': 36876,
 'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW': 36877,
 'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB': 36877,
 'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_EXT': 36877,
 'GL_SAMPLER_CUBE_SHADOW': 36293,
 'GL_SAMPLER_CUBE_SHADOW_EXT': 36293,
 'GL_SAMPLER_EXTERNAL_2D_Y2Y_EXT': 35815,
 'GL_SAMPLES': 32937,
 'GL_SAMPLES_3DFX': 34484,
 'GL_SAMPLES_ARB': 32937,
 'GL_SAMPLES_EXT': 32937,
 'GL_SAMPLES_PASSED': 35092,
 'GL_SAMPLES_PASSED_ARB': 35092,
 'GL_SAMPLE_ALPHA_TO_COVERAGE': 32926,
 'GL_SAMPLE_ALPHA_TO_COVERAGE_ARB': 32926,
 'GL_SAMPLE_ALPHA_TO_MASK_EXT': 32926,
 'GL_SAMPLE_ALPHA_TO_ONE': 32927,
 'GL_SAMPLE_ALPHA_TO_ONE_ARB': 32927,
 'GL_SAMPLE_ALPHA_TO_ONE_EXT': 32927,
 'GL_SAMPLE_BUFFERS': 32936,
 'GL_SAMPLE_BUFFERS_3DFX': 34483,
 'GL_SAMPLE_BUFFERS_ARB': 32936,
 'GL_SAMPLE_BUFFERS_EXT': 32936,
 'GL_SAMPLE_COVERAGE': 32928,
 'GL_SAMPLE_COVERAGE_ARB': 32928,
 'GL_SAMPLE_COVERAGE_INVERT': 32939,
 'GL_SAMPLE_COVERAGE_INVERT_ARB': 32939,
 'GL_SAMPLE_COVERAGE_VALUE': 32938,
 'GL_SAMPLE_COVERAGE_VALUE_ARB': 32938,
 'GL_SAMPLE_LOCATION_ARB': 36432,
 'GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_ARB': 37695,
 'GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_ARB': 37694,
 'GL_SAMPLE_LOCATION_SUBPIXEL_BITS_ARB': 37693,
 'GL_SAMPLE_MASK': 36433,
 'GL_SAMPLE_MASK_EXT': 32928,
 'GL_SAMPLE_MASK_INVERT_EXT': 32939,
 'GL_SAMPLE_MASK_VALUE': 36434,
 'GL_SAMPLE_MASK_VALUE_EXT': 32938,
 'GL_SAMPLE_PATTERN_EXT': 32940,
 'GL_SAMPLE_POSITION': 36432,
 'GL_SAMPLE_SHADING': 35894,
 'GL_SAMPLE_SHADING_ARB': 35894,
 'GL_SCALAR_EXT': 34750,
 'GL_SCALED_RESOLVE_FASTEST_EXT': 37050,
 'GL_SCALED_RESOLVE_NICEST_EXT': 37051,
 'GL_SCISSOR_BIT': 524288,
 'GL_SCISSOR_BOX': 3088,
 'GL_SCISSOR_TEST': 3089,
 'GL_SCREEN': 37525,
 'GL_SCREEN_COORDINATES_REND': 33936,
 'GL_SECONDARY_COLOR_ARRAY': 33886,
 'GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING': 34972,
 'GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB': 34972,
 'GL_SECONDARY_COLOR_ARRAY_EXT': 33886,
 'GL_SECONDARY_COLOR_ARRAY_POINTER': 33885,
 'GL_SECONDARY_COLOR_ARRAY_POINTER_EXT': 33885,
 'GL_SECONDARY_COLOR_ARRAY_SIZE': 33882,
 'GL_SECONDARY_COLOR_ARRAY_SIZE_EXT': 33882,
 'GL_SECONDARY_COLOR_ARRAY_STRIDE': 33884,
 'GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT': 33884,
 'GL_SECONDARY_COLOR_ARRAY_TYPE': 33883,
 'GL_SECONDARY_COLOR_ARRAY_TYPE_EXT': 33883,
 'GL_SELECT': 7170,
 'GL_SELECTION_BUFFER_POINTER': 3571,
 'GL_SELECTION_BUFFER_SIZE': 3572,
 'GL_SEPARABLE_2D': 32786,
 'GL_SEPARABLE_2D_EXT': 32786,
 'GL_SEPARATE_ATTRIBS': 35981,
 'GL_SEPARATE_ATTRIBS_EXT': 35981,
 'GL_SEPARATE_SPECULAR_COLOR': 33274,
 'GL_SEPARATE_SPECULAR_COLOR_EXT': 33274,
 'GL_SET': 5391,
 'GL_SGX_BINARY_IMG': 35850,
 'GL_SGX_PROGRAM_BINARY_IMG': 37168,
 'GL_SHADER': 33505,
 'GL_SHADER_BINARY_DMP': 37456,
 'GL_SHADER_BINARY_FORMATS': 36344,
 'GL_SHADER_BINARY_FORMAT_SPIR_V': 38225,
 'GL_SHADER_BINARY_FORMAT_SPIR_V_ARB': 38225,
 'GL_SHADER_BINARY_VIV': 36804,
 'GL_SHADER_COMPILER': 36346,
 'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT': 32,
 'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT_EXT': 32,
 'GL_SHADER_IMAGE_ATOMIC': 33446,
 'GL_SHADER_IMAGE_LOAD': 33444,
 'GL_SHADER_IMAGE_STORE': 33445,
 'GL_SHADER_INCLUDE_ARB': 36270,
 'GL_SHADER_OBJECT_ARB': 35656,
 'GL_SHADER_OBJECT_EXT': 35656,
 'GL_SHADER_PIXEL_LOCAL_STORAGE_EXT': 36708,
 'GL_SHADER_SOURCE_LENGTH': 35720,
 'GL_SHADER_STORAGE_BARRIER_BIT': 8192,
 'GL_SHADER_STORAGE_BLOCK': 37606,
 'GL_SHADER_STORAGE_BUFFER': 37074,
 'GL_SHADER_STORAGE_BUFFER_BINDING': 37075,
 'GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT': 37087,
 'GL_SHADER_STORAGE_BUFFER_SIZE': 37077,
 'GL_SHADER_STORAGE_BUFFER_START': 37076,
 'GL_SHADER_TYPE': 35663,
 'GL_SHADE_MODEL': 2900,
 'GL_SHADING_LANGUAGE_VERSION': 35724,
 'GL_SHADING_LANGUAGE_VERSION_ARB': 35724,
 'GL_SHADOW_ATTENUATION_EXT': 33614,
 'GL_SHARED_TEXTURE_PALETTE_EXT': 33275,
 'GL_SHININESS': 5633,
 'GL_SHORT': 5122,
 'GL_SIGNALED': 37145,
 'GL_SIGNED_NORMALIZED': 36764,
 'GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST': 33452,
 'GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE': 33454,
 'GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST': 33453,
 'GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE': 33455,
 'GL_SINGLE_COLOR': 33273,
 'GL_SINGLE_COLOR_EXT': 33273,
 'GL_SKIP_DECODE_EXT': 35402,
 'GL_SLUMINANCE': 35910,
 'GL_SLUMINANCE8': 35911,
 'GL_SLUMINANCE8_ALPHA8': 35909,
 'GL_SLUMINANCE8_ALPHA8_EXT': 35909,
 'GL_SLUMINANCE8_EXT': 35911,
 'GL_SLUMINANCE_ALPHA': 35908,
 'GL_SLUMINANCE_ALPHA_EXT': 35908,
 'GL_SLUMINANCE_EXT': 35910,
 'GL_SMAPHS30_PROGRAM_BINARY_DMP': 37457,
 'GL_SMAPHS_PROGRAM_BINARY_DMP': 37458,
 'GL_SMOOTH': 7425,
 'GL_SMOOTH_LINE_WIDTH_GRANULARITY': 2851,
 'GL_SMOOTH_LINE_WIDTH_RANGE': 2850,
 'GL_SMOOTH_POINT_SIZE_GRANULARITY': 2835,
 'GL_SMOOTH_POINT_SIZE_RANGE': 2834,
 'GL_SOFTLIGHT': 37532,
 'GL_SOURCE0_ALPHA': 34184,
 'GL_SOURCE0_ALPHA_ARB': 34184,
 'GL_SOURCE0_ALPHA_EXT': 34184,
 'GL_SOURCE0_RGB': 34176,
 'GL_SOURCE0_RGB_ARB': 34176,
 'GL_SOURCE0_RGB_EXT': 34176,
 'GL_SOURCE1_ALPHA': 34185,
 'GL_SOURCE1_ALPHA_ARB': 34185,
 'GL_SOURCE1_ALPHA_EXT': 34185,
 'GL_SOURCE1_RGB': 34177,
 'GL_SOURCE1_RGB_ARB': 34177,
 'GL_SOURCE1_RGB_EXT': 34177,
 'GL_SOURCE2_ALPHA': 34186,
 'GL_SOURCE2_ALPHA_ARB': 34186,
 'GL_SOURCE2_ALPHA_EXT': 34186,
 'GL_SOURCE2_RGB': 34178,
 'GL_SOURCE2_RGB_ARB': 34178,
 'GL_SOURCE2_RGB_EXT': 34178,
 'GL_SPARSE_BUFFER_PAGE_SIZE_ARB': 33528,
 'GL_SPARSE_STORAGE_BIT_ARB': 1024,
 'GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB': 37289,
 'GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_EXT': 37289,
 'GL_SPECULAR': 4610,
 'GL_SPHERE_MAP': 9218,
 'GL_SPIR_V_BINARY': 38226,
 'GL_SPIR_V_BINARY_ARB': 38226,
 'GL_SPIR_V_EXTENSIONS': 38227,
 'GL_SPOT_CUTOFF': 4614,
 'GL_SPOT_DIRECTION': 4612,
 'GL_SPOT_EXPONENT': 4613,
 'GL_SR8_EXT': 36797,
 'GL_SRC0_ALPHA': 34184,
 'GL_SRC0_RGB': 34176,
 'GL_SRC1_ALPHA': 34185,
 'GL_SRC1_ALPHA_EXT': 34185,
 'GL_SRC1_COLOR': 35065,
 'GL_SRC1_COLOR_EXT': 35065,
 'GL_SRC1_RGB': 34177,
 'GL_SRC2_ALPHA': 34186,
 'GL_SRC2_RGB': 34178,
 'GL_SRC_ALPHA': 770,
 'GL_SRC_ALPHA_SATURATE': 776,
 'GL_SRC_ALPHA_SATURATE_EXT': 776,
 'GL_SRC_COLOR': 768,
 'GL_SRG8_EXT': 36798,
 'GL_SRGB': 35904,
 'GL_SRGB8': 35905,
 'GL_SRGB8_ALPHA8': 35907,
 'GL_SRGB8_ALPHA8_EXT': 35907,
 'GL_SRGB8_EXT': 35905,
 'GL_SRGB_ALPHA': 35906,
 'GL_SRGB_ALPHA_EXT': 35906,
 'GL_SRGB_DECODE_ARB': 33433,
 'GL_SRGB_EXT': 35904,
 'GL_SRGB_READ': 33431,
 'GL_SRGB_WRITE': 33432,
 'GL_STACK_OVERFLOW': 1283,
 'GL_STACK_UNDERFLOW': 1284,
 'GL_STATE_RESTORE': 35804,
 'GL_STATIC_COPY': 35046,
 'GL_STATIC_COPY_ARB': 35046,
 'GL_STATIC_DRAW': 35044,
 'GL_STATIC_DRAW_ARB': 35044,
 'GL_STATIC_READ': 35045,
 'GL_STATIC_READ_ARB': 35045,
 'GL_STENCIL': 6146,
 'GL_STENCIL_ATTACHMENT': 36128,
 'GL_STENCIL_ATTACHMENT_EXT': 36128,
 'GL_STENCIL_BACK_FAIL': 34817,
 'GL_STENCIL_BACK_FUNC': 34816,
 'GL_STENCIL_BACK_PASS_DEPTH_FAIL': 34818,
 'GL_STENCIL_BACK_PASS_DEPTH_PASS': 34819,
 'GL_STENCIL_BACK_REF': 36003,
 'GL_STENCIL_BACK_VALUE_MASK': 36004,
 'GL_STENCIL_BACK_WRITEMASK': 36005,
 'GL_STENCIL_BITS': 3415,
 'GL_STENCIL_BUFFER_BIT': 1024,
 'GL_STENCIL_CLEAR_TAG_VALUE_EXT': 35059,
 'GL_STENCIL_CLEAR_VALUE': 2961,
 'GL_STENCIL_COMPONENTS': 33413,
 'GL_STENCIL_EXT': 6146,
 'GL_STENCIL_FAIL': 2964,
 'GL_STENCIL_FUNC': 2962,
 'GL_STENCIL_INDEX': 6401,
 'GL_STENCIL_INDEX1': 36166,
 'GL_STENCIL_INDEX16': 36169,
 'GL_STENCIL_INDEX16_EXT': 36169,
 'GL_STENCIL_INDEX1_EXT': 36166,
 'GL_STENCIL_INDEX4': 36167,
 'GL_STENCIL_INDEX4_EXT': 36167,
 'GL_STENCIL_INDEX8': 36168,
 'GL_STENCIL_INDEX8_EXT': 36168,
 'GL_STENCIL_PASS_DEPTH_FAIL': 2965,
 'GL_STENCIL_PASS_DEPTH_PASS': 2966,
 'GL_STENCIL_REF': 2967,
 'GL_STENCIL_RENDERABLE': 33416,
 'GL_STENCIL_TAG_BITS_EXT': 35058,
 'GL_STENCIL_TEST': 2960,
 'GL_STENCIL_TEST_TWO_SIDE_EXT': 35088,
 'GL_STENCIL_VALUE_MASK': 2963,
 'GL_STENCIL_WRITEMASK': 2968,
 'GL_STEREO': 3123,
 'GL_STREAM_COPY': 35042,
 'GL_STREAM_COPY_ARB': 35042,
 'GL_STREAM_DRAW': 35040,
 'GL_STREAM_DRAW_ARB': 35040,
 'GL_STREAM_READ': 35041,
 'GL_STREAM_READ_ARB': 35041,
 'GL_SUBPIXEL_BITS': 3408,
 'GL_SUBTRACT': 34023,
 'GL_SUBTRACT_ARB': 34023,
 'GL_SYNC_CL_EVENT_ARB': 33344,
 'GL_SYNC_CL_EVENT_COMPLETE_ARB': 33345,
 'GL_SYNC_CONDITION': 37139,
 'GL_SYNC_FENCE': 37142,
 'GL_SYNC_FLAGS': 37141,
 'GL_SYNC_FLUSH_COMMANDS_BIT': 1,
 'GL_SYNC_GPU_COMMANDS_COMPLETE': 37143,
 'GL_SYNC_STATUS': 37140,
 'GL_SYNC_X11_FENCE_EXT': 37089,
 'GL_T': 8193,
 'GL_T2F_C3F_V3F': 10794,
 'GL_T2F_C4F_N3F_V3F': 10796,
 'GL_T2F_C4UB_V3F': 10793,
 'GL_T2F_IUI_N3F_V2F_EXT': 33203,
 'GL_T2F_IUI_N3F_V3F_EXT': 33204,
 'GL_T2F_IUI_V2F_EXT': 33201,
 'GL_T2F_IUI_V3F_EXT': 33202,
 'GL_T2F_N3F_V3F': 10795,
 'GL_T2F_V3F': 10791,
 'GL_T4F_C4F_N3F_V4F': 10797,
 'GL_T4F_V4F': 10792,
 'GL_TABLE_TOO_LARGE': 32817,
 'GL_TABLE_TOO_LARGE_EXT': 32817,
 'GL_TANGENT_ARRAY_EXT': 33849,
 'GL_TANGENT_ARRAY_POINTER_EXT': 33858,
 'GL_TANGENT_ARRAY_STRIDE_EXT': 33855,
 'GL_TANGENT_ARRAY_TYPE_EXT': 33854,
 'GL_TESS_CONTROL_OUTPUT_VERTICES': 36469,
 'GL_TESS_CONTROL_OUTPUT_VERTICES_EXT': 36469,
 'GL_TESS_CONTROL_SHADER': 36488,
 'GL_TESS_CONTROL_SHADER_BIT': 8,
 'GL_TESS_CONTROL_SHADER_BIT_EXT': 8,
 'GL_TESS_CONTROL_SHADER_EXT': 36488,
 'GL_TESS_CONTROL_SHADER_PATCHES': 33521,
 'GL_TESS_CONTROL_SHADER_PATCHES_ARB': 33521,
 'GL_TESS_CONTROL_SUBROUTINE': 37609,
 'GL_TESS_CONTROL_SUBROUTINE_UNIFORM': 37615,
 'GL_TESS_CONTROL_TEXTURE': 33436,
 'GL_TESS_EVALUATION_SHADER': 36487,
 'GL_TESS_EVALUATION_SHADER_BIT': 16,
 'GL_TESS_EVALUATION_SHADER_BIT_EXT': 16,
 'GL_TESS_EVALUATION_SHADER_EXT': 36487,
 'GL_TESS_EVALUATION_SHADER_INVOCATIONS': 33522,
 'GL_TESS_EVALUATION_SHADER_INVOCATIONS_ARB': 33522,
 'GL_TESS_EVALUATION_SUBROUTINE': 37610,
 'GL_TESS_EVALUATION_SUBROUTINE_UNIFORM': 37616,
 'GL_TESS_EVALUATION_TEXTURE': 33437,
 'GL_TESS_GEN_MODE': 36470,
 'GL_TESS_GEN_MODE_EXT': 36470,
 'GL_TESS_GEN_POINT_MODE': 36473,
 'GL_TESS_GEN_POINT_MODE_EXT': 36473,
 'GL_TESS_GEN_SPACING': 36471,
 'GL_TESS_GEN_SPACING_EXT': 36471,
 'GL_TESS_GEN_VERTEX_ORDER': 36472,
 'GL_TESS_GEN_VERTEX_ORDER_EXT': 36472,
 'GL_TEXTURE': 5890,
 'GL_TEXTURE0': 33984,
 'GL_TEXTURE0_ARB': 33984,
 'GL_TEXTURE1': 33985,
 'GL_TEXTURE10': 33994,
 'GL_TEXTURE10_ARB': 33994,
 'GL_TEXTURE11': 33995,
 'GL_TEXTURE11_ARB': 33995,
 'GL_TEXTURE12': 33996,
 'GL_TEXTURE12_ARB': 33996,
 'GL_TEXTURE13': 33997,
 'GL_TEXTURE13_ARB': 33997,
 'GL_TEXTURE14': 33998,
 'GL_TEXTURE14_ARB': 33998,
 'GL_TEXTURE15': 33999,
 'GL_TEXTURE15_ARB': 33999,
 'GL_TEXTURE16': 34000,
 'GL_TEXTURE16_ARB': 34000,
 'GL_TEXTURE17': 34001,
 'GL_TEXTURE17_ARB': 34001,
 'GL_TEXTURE18': 34002,
 'GL_TEXTURE18_ARB': 34002,
 'GL_TEXTURE19': 34003,
 'GL_TEXTURE19_ARB': 34003,
 'GL_TEXTURE1_ARB': 33985,
 'GL_TEXTURE2': 33986,
 'GL_TEXTURE20': 34004,
 'GL_TEXTURE20_ARB': 34004,
 'GL_TEXTURE21': 34005,
 'GL_TEXTURE21_ARB': 34005,
 'GL_TEXTURE22': 34006,
 'GL_TEXTURE22_ARB': 34006,
 'GL_TEXTURE23': 34007,
 'GL_TEXTURE23_ARB': 34007,
 'GL_TEXTURE24': 34008,
 'GL_TEXTURE24_ARB': 34008,
 'GL_TEXTURE25': 34009,
 'GL_TEXTURE25_ARB': 34009,
 'GL_TEXTURE26': 34010,
 'GL_TEXTURE26_ARB': 34010,
 'GL_TEXTURE27': 34011,
 'GL_TEXTURE27_ARB': 34011,
 'GL_TEXTURE28': 34012,
 'GL_TEXTURE28_ARB': 34012,
 'GL_TEXTURE29': 34013,
 'GL_TEXTURE29_ARB': 34013,
 'GL_TEXTURE2_ARB': 33986,
 'GL_TEXTURE3': 33987,
 'GL_TEXTURE30': 34014,
 'GL_TEXTURE30_ARB': 34014,
 'GL_TEXTURE31': 34015,
 'GL_TEXTURE31_ARB': 34015,
 'GL_TEXTURE3_ARB': 33987,
 'GL_TEXTURE4': 33988,
 'GL_TEXTURE4_ARB': 33988,
 'GL_TEXTURE5': 33989,
 'GL_TEXTURE5_ARB': 33989,
 'GL_TEXTURE6': 33990,
 'GL_TEXTURE6_ARB': 33990,
 'GL_TEXTURE7': 33991,
 'GL_TEXTURE7_ARB': 33991,
 'GL_TEXTURE8': 33992,
 'GL_TEXTURE8_ARB': 33992,
 'GL_TEXTURE9': 33993,
 'GL_TEXTURE9_ARB': 33993,
 'GL_TEXTURE_1D': 3552,
 'GL_TEXTURE_1D_ARRAY': 35864,
 'GL_TEXTURE_1D_ARRAY_EXT': 35864,
 'GL_TEXTURE_1D_BINDING_EXT': 32872,
 'GL_TEXTURE_1D_STACK_BINDING_MESAX': 34653,
 'GL_TEXTURE_1D_STACK_MESAX': 34649,
 'GL_TEXTURE_2D': 3553,
 'GL_TEXTURE_2D_ARRAY': 35866,
 'GL_TEXTURE_2D_ARRAY_EXT': 35866,
 'GL_TEXTURE_2D_BINDING_EXT': 32873,
 'GL_TEXTURE_2D_MULTISAMPLE': 37120,
 'GL_TEXTURE_2D_MULTISAMPLE_ARRAY': 37122,
 'GL_TEXTURE_2D_STACK_BINDING_MESAX': 34654,
 'GL_TEXTURE_2D_STACK_MESAX': 34650,
 'GL_TEXTURE_3D': 32879,
 'GL_TEXTURE_3D_BINDING_EXT': 32874,
 'GL_TEXTURE_3D_EXT': 32879,
 'GL_TEXTURE_ALPHA_MODULATE_IMG': 35846,
 'GL_TEXTURE_ALPHA_SIZE': 32863,
 'GL_TEXTURE_ALPHA_SIZE_EXT': 32863,
 'GL_TEXTURE_ALPHA_TYPE': 35859,
 'GL_TEXTURE_ALPHA_TYPE_ARB': 35859,
 'GL_TEXTURE_APPLICATION_MODE_EXT': 33615,
 'GL_TEXTURE_ASTC_DECODE_PRECISION_EXT': 36713,
 'GL_TEXTURE_BASE_LEVEL': 33084,
 'GL_TEXTURE_BINDING_1D': 32872,
 'GL_TEXTURE_BINDING_1D_ARRAY': 35868,
 'GL_TEXTURE_BINDING_1D_ARRAY_EXT': 35868,
 'GL_TEXTURE_BINDING_2D': 32873,
 'GL_TEXTURE_BINDING_2D_ARRAY': 35869,
 'GL_TEXTURE_BINDING_2D_ARRAY_EXT': 35869,
 'GL_TEXTURE_BINDING_2D_MULTISAMPLE': 37124,
 'GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY': 37125,
 'GL_TEXTURE_BINDING_3D': 32874,
 'GL_TEXTURE_BINDING_BUFFER': 35884,
 'GL_TEXTURE_BINDING_BUFFER_ARB': 35884,
 'GL_TEXTURE_BINDING_BUFFER_EXT': 35884,
 'GL_TEXTURE_BINDING_CUBE_MAP': 34068,
 'GL_TEXTURE_BINDING_CUBE_MAP_ARB': 34068,
 'GL_TEXTURE_BINDING_CUBE_MAP_ARRAY': 36874,
 'GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB': 36874,
 'GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_EXT': 36874,
 'GL_TEXTURE_BINDING_CUBE_MAP_EXT': 34068,
 'GL_TEXTURE_BINDING_RECTANGLE': 34038,
 'GL_TEXTURE_BINDING_RECTANGLE_ARB': 34038,
 'GL_TEXTURE_BIT': 262144,
 'GL_TEXTURE_BLUE_SIZE': 32862,
 'GL_TEXTURE_BLUE_SIZE_EXT': 32862,
 'GL_TEXTURE_BLUE_TYPE': 35858,
 'GL_TEXTURE_BLUE_TYPE_ARB': 35858,
 'GL_TEXTURE_BORDER': 4101,
 'GL_TEXTURE_BORDER_COLOR': 4100,
 'GL_TEXTURE_BORDER_COLOR_EXT': 4100,
 'GL_TEXTURE_BUFFER': 35882,
 'GL_TEXTURE_BUFFER_ARB': 35882,
 'GL_TEXTURE_BUFFER_BINDING': 35882,
 'GL_TEXTURE_BUFFER_BINDING_EXT': 35882,
 'GL_TEXTURE_BUFFER_DATA_STORE_BINDING': 35885,
 'GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB': 35885,
 'GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT': 35885,
 'GL_TEXTURE_BUFFER_EXT': 35882,
 'GL_TEXTURE_BUFFER_FORMAT_ARB': 35886,
 'GL_TEXTURE_BUFFER_FORMAT_EXT': 35886,
 'GL_TEXTURE_BUFFER_OFFSET': 37277,
 'GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT': 37279,
 'GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT_EXT': 37279,
 'GL_TEXTURE_BUFFER_OFFSET_EXT': 37277,
 'GL_TEXTURE_BUFFER_SIZE': 37278,
 'GL_TEXTURE_BUFFER_SIZE_EXT': 37278,
 'GL_TEXTURE_COMPARE_FAIL_VALUE_ARB': 32959,
 'GL_TEXTURE_COMPARE_FUNC': 34893,
 'GL_TEXTURE_COMPARE_FUNC_ARB': 34893,
 'GL_TEXTURE_COMPARE_FUNC_EXT': 34893,
 'GL_TEXTURE_COMPARE_MODE': 34892,
 'GL_TEXTURE_COMPARE_MODE_ARB': 34892,
 'GL_TEXTURE_COMPARE_MODE_EXT': 34892,
 'GL_TEXTURE_COMPONENTS': 4099,
 'GL_TEXTURE_COMPRESSED': 34465,
 'GL_TEXTURE_COMPRESSED_ARB': 34465,
 'GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT': 33458,
 'GL_TEXTURE_COMPRESSED_BLOCK_SIZE': 33459,
 'GL_TEXTURE_COMPRESSED_BLOCK_WIDTH': 33457,
 'GL_TEXTURE_COMPRESSED_IMAGE_SIZE': 34464,
 'GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB': 34464,
 'GL_TEXTURE_COMPRESSION_HINT': 34031,
 'GL_TEXTURE_COMPRESSION_HINT_ARB': 34031,
 'GL_TEXTURE_CONSTANT_DATA_SUNX': 33238,
 'GL_TEXTURE_COORD_ARRAY': 32888,
 'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING': 34970,
 'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB': 34970,
 'GL_TEXTURE_COORD_ARRAY_COUNT_EXT': 32907,
 'GL_TEXTURE_COORD_ARRAY_EXT': 32888,
 'GL_TEXTURE_COORD_ARRAY_POINTER': 32914,
 'GL_TEXTURE_COORD_ARRAY_POINTER_EXT': 32914,
 'GL_TEXTURE_COORD_ARRAY_SIZE': 32904,
 'GL_TEXTURE_COORD_ARRAY_SIZE_EXT': 32904,
 'GL_TEXTURE_COORD_ARRAY_STRIDE': 32906,
 'GL_TEXTURE_COORD_ARRAY_STRIDE_EXT': 32906,
 'GL_TEXTURE_COORD_ARRAY_TYPE': 32905,
 'GL_TEXTURE_COORD_ARRAY_TYPE_EXT': 32905,
 'GL_TEXTURE_CUBE_MAP': 34067,
 'GL_TEXTURE_CUBE_MAP_ARB': 34067,
 'GL_TEXTURE_CUBE_MAP_ARRAY': 36873,
 'GL_TEXTURE_CUBE_MAP_ARRAY_ARB': 36873,
 'GL_TEXTURE_CUBE_MAP_ARRAY_EXT': 36873,
 'GL_TEXTURE_CUBE_MAP_EXT': 34067,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X': 34070,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB': 34070,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT': 34070,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y': 34072,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB': 34072,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT': 34072,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z': 34074,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB': 34074,
 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT': 34074,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_X': 34069,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB': 34069,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT': 34069,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y': 34071,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB': 34071,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT': 34071,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z': 34073,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB': 34073,
 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT': 34073,
 'GL_TEXTURE_CUBE_MAP_SEAMLESS': 34895,
 'GL_TEXTURE_DEPTH': 32881,
 'GL_TEXTURE_DEPTH_EXT': 32881,
 'GL_TEXTURE_DEPTH_SIZE': 34890,
 'GL_TEXTURE_DEPTH_SIZE_ARB': 34890,
 'GL_TEXTURE_DEPTH_TYPE': 35862,
 'GL_TEXTURE_DEPTH_TYPE_ARB': 35862,
 'GL_TEXTURE_ENV_COLOR': 8705,
 'GL_TEXTURE_ENV_MODE': 8704,
 'GL_TEXTURE_FETCH_BARRIER_BIT': 8,
 'GL_TEXTURE_FETCH_BARRIER_BIT_EXT': 8,
 'GL_TEXTURE_FILTER_CONTROL': 34048,
 'GL_TEXTURE_FILTER_CONTROL_EXT': 34048,
 'GL_TEXTURE_FIXED_SAMPLE_LOCATIONS': 37127,
 'GL_TEXTURE_FORMAT_SRGB_OVERRIDE_EXT': 36799,
 'GL_TEXTURE_GATHER': 33442,
 'GL_TEXTURE_GATHER_SHADOW': 33443,
 'GL_TEXTURE_GEN_MODE': 9472,
 'GL_TEXTURE_GEN_Q': 3171,
 'GL_TEXTURE_GEN_R': 3170,
 'GL_TEXTURE_GEN_S': 3168,
 'GL_TEXTURE_GEN_T': 3169,
 'GL_TEXTURE_GREEN_SIZE': 32861,
 'GL_TEXTURE_GREEN_SIZE_EXT': 32861,
 'GL_TEXTURE_GREEN_TYPE': 35857,
 'GL_TEXTURE_GREEN_TYPE_ARB': 35857,
 'GL_TEXTURE_HEIGHT': 4097,
 'GL_TEXTURE_IMAGE_FORMAT': 33423,
 'GL_TEXTURE_IMAGE_TYPE': 33424,
 'GL_TEXTURE_IMMUTABLE_FORMAT': 37167,
 'GL_TEXTURE_IMMUTABLE_FORMAT_EXT': 37167,
 'GL_TEXTURE_IMMUTABLE_LEVELS': 33503,
 'GL_TEXTURE_INDEX_SIZE_EXT': 33005,
 'GL_TEXTURE_INTENSITY_SIZE': 32865,
 'GL_TEXTURE_INTENSITY_SIZE_EXT': 32865,
 'GL_TEXTURE_INTENSITY_TYPE': 35861,
 'GL_TEXTURE_INTENSITY_TYPE_ARB': 35861,
 'GL_TEXTURE_INTERNAL_FORMAT': 4099,
 'GL_TEXTURE_LIGHTING_MODE_HP': 33127,
 'GL_TEXTURE_LIGHT_EXT': 33616,
 'GL_TEXTURE_LOD_BIAS': 34049,
 'GL_TEXTURE_LOD_BIAS_EXT': 34049,
 'GL_TEXTURE_LUMINANCE_SIZE': 32864,
 'GL_TEXTURE_LUMINANCE_SIZE_EXT': 32864,
 'GL_TEXTURE_LUMINANCE_TYPE': 35860,
 'GL_TEXTURE_LUMINANCE_TYPE_ARB': 35860,
 'GL_TEXTURE_MAG_FILTER': 10240,
 'GL_TEXTURE_MATERIAL_FACE_EXT': 33617,
 'GL_TEXTURE_MATERIAL_PARAMETER_EXT': 33618,
 'GL_TEXTURE_MATRIX': 2984,
 'GL_TEXTURE_MAX_ANISOTROPY': 34046,
 'GL_TEXTURE_MAX_ANISOTROPY_EXT': 34046,
 'GL_TEXTURE_MAX_LEVEL': 33085,
 'GL_TEXTURE_MAX_LOD': 33083,
 'GL_TEXTURE_MIN_FILTER': 10241,
 'GL_TEXTURE_MIN_LOD': 33082,
 'GL_TEXTURE_NORMAL_EXT': 34223,
 'GL_TEXTURE_POST_SPECULAR_HP': 33128,
 'GL_TEXTURE_PRE_SPECULAR_HP': 33129,
 'GL_TEXTURE_PRIORITY': 32870,
 'GL_TEXTURE_PRIORITY_EXT': 32870,
 'GL_TEXTURE_PROTECTED_EXT': 35834,
 'GL_TEXTURE_RECTANGLE': 34037,
 'GL_TEXTURE_RECTANGLE_ARB': 34037,
 'GL_TEXTURE_REDUCTION_MODE_ARB': 37734,
 'GL_TEXTURE_REDUCTION_MODE_EXT': 37734,
 'GL_TEXTURE_RED_SIZE': 32860,
 'GL_TEXTURE_RED_SIZE_EXT': 32860,
 'GL_TEXTURE_RED_TYPE': 35856,
 'GL_TEXTURE_RED_TYPE_ARB': 35856,
 'GL_TEXTURE_RESIDENT': 32871,
 'GL_TEXTURE_RESIDENT_EXT': 32871,
 'GL_TEXTURE_SAMPLES': 37126,
 'GL_TEXTURE_SAMPLES_IMG': 37174,
 'GL_TEXTURE_SHADOW': 33441,
 'GL_TEXTURE_SHARED_SIZE': 35903,
 'GL_TEXTURE_SHARED_SIZE_EXT': 35903,
 'GL_TEXTURE_SPARSE_ARB': 37286,
 'GL_TEXTURE_SPARSE_EXT': 37286,
 'GL_TEXTURE_SRGB_DECODE_EXT': 35400,
 'GL_TEXTURE_STACK_DEPTH': 2981,
 'GL_TEXTURE_STENCIL_SIZE': 35057,
 'GL_TEXTURE_STENCIL_SIZE_EXT': 35057,
 'GL_TEXTURE_SWIZZLE_A': 36421,
 'GL_TEXTURE_SWIZZLE_A_EXT': 36421,
 'GL_TEXTURE_SWIZZLE_B': 36420,
 'GL_TEXTURE_SWIZZLE_B_EXT': 36420,
 'GL_TEXTURE_SWIZZLE_G': 36419,
 'GL_TEXTURE_SWIZZLE_G_EXT': 36419,
 'GL_TEXTURE_SWIZZLE_R': 36418,
 'GL_TEXTURE_SWIZZLE_RGBA': 36422,
 'GL_TEXTURE_SWIZZLE_RGBA_EXT': 36422,
 'GL_TEXTURE_SWIZZLE_R_EXT': 36418,
 'GL_TEXTURE_TARGET': 4102,
 'GL_TEXTURE_TILING_EXT': 38272,
 'GL_TEXTURE_TOO_LARGE_EXT': 32869,
 'GL_TEXTURE_UPDATE_BARRIER_BIT': 256,
 'GL_TEXTURE_UPDATE_BARRIER_BIT_EXT': 256,
 'GL_TEXTURE_USAGE_ANGLE': 37794,
 'GL_TEXTURE_VIEW': 33461,
 'GL_TEXTURE_VIEW_MIN_LAYER': 33501,
 'GL_TEXTURE_VIEW_MIN_LAYER_EXT': 33501,
 'GL_TEXTURE_VIEW_MIN_LEVEL': 33499,
 'GL_TEXTURE_VIEW_MIN_LEVEL_EXT': 33499,
 'GL_TEXTURE_VIEW_NUM_LAYERS': 33502,
 'GL_TEXTURE_VIEW_NUM_LAYERS_EXT': 33502,
 'GL_TEXTURE_VIEW_NUM_LEVELS': 33500,
 'GL_TEXTURE_VIEW_NUM_LEVELS_EXT': 33500,
 'GL_TEXTURE_WIDTH': 4096,
 'GL_TEXTURE_WRAP_R': 32882,
 'GL_TEXTURE_WRAP_R_EXT': 32882,
 'GL_TEXTURE_WRAP_S': 10242,
 'GL_TEXTURE_WRAP_T': 10243,
 'GL_TILING_TYPES_EXT': 38275,
 'GL_TIMEOUT_EXPIRED': 37147,
 'GL_TIMEOUT_IGNORED': 18446744073709551615,
 'GL_TIMESTAMP': 36392,
 'GL_TIMESTAMP_EXT': 36392,
 'GL_TIME_ELAPSED': 35007,
 'GL_TIME_ELAPSED_EXT': 35007,
 'GL_TOP_LEVEL_ARRAY_SIZE': 37644,
 'GL_TOP_LEVEL_ARRAY_STRIDE': 37645,
 'GL_TRANSFORM_BIT': 4096,
 'GL_TRANSFORM_FEEDBACK': 36386,
 'GL_TRANSFORM_FEEDBACK_ACTIVE': 36388,
 'GL_TRANSFORM_FEEDBACK_BARRIER_BIT': 2048,
 'GL_TRANSFORM_FEEDBACK_BARRIER_BIT_EXT': 2048,
 'GL_TRANSFORM_FEEDBACK_BINDING': 36389,
 'GL_TRANSFORM_FEEDBACK_BUFFER': 35982,
 'GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE': 36388,
 'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING': 35983,
 'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT': 35983,
 'GL_TRANSFORM_FEEDBACK_BUFFER_EXT': 35982,
 'GL_TRANSFORM_FEEDBACK_BUFFER_INDEX': 37707,
 'GL_TRANSFORM_FEEDBACK_BUFFER_MODE': 35967,
 'GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT': 35967,
 'GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED': 36387,
 'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE': 35973,
 'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT': 35973,
 'GL_TRANSFORM_FEEDBACK_BUFFER_START': 35972,
 'GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT': 35972,
 'GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE': 37708,
 'GL_TRANSFORM_FEEDBACK_OVERFLOW': 33516,
 'GL_TRANSFORM_FEEDBACK_OVERFLOW_ARB': 33516,
 'GL_TRANSFORM_FEEDBACK_PAUSED': 36387,
 'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN': 35976,
 'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT': 35976,
 'GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW': 33517,
 'GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW_ARB': 33517,
 'GL_TRANSFORM_FEEDBACK_VARYING': 37620,
 'GL_TRANSFORM_FEEDBACK_VARYINGS': 35971,
 'GL_TRANSFORM_FEEDBACK_VARYINGS_EXT': 35971,
 'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH': 35958,
 'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT': 35958,
 'GL_TRANSLATED_SHADER_SOURCE_LENGTH_ANGLE': 37792,
 'GL_TRANSPOSE_COLOR_MATRIX': 34022,
 'GL_TRANSPOSE_COLOR_MATRIX_ARB': 34022,
 'GL_TRANSPOSE_CURRENT_MATRIX_ARB': 34999,
 'GL_TRANSPOSE_MODELVIEW_MATRIX': 34019,
 'GL_TRANSPOSE_MODELVIEW_MATRIX_ARB': 34019,
 'GL_TRANSPOSE_PROGRAM_MATRIX_EXT': 36398,
 'GL_TRANSPOSE_PROJECTION_MATRIX': 34020,
 'GL_TRANSPOSE_PROJECTION_MATRIX_ARB': 34020,
 'GL_TRANSPOSE_TEXTURE_MATRIX': 34021,
 'GL_TRANSPOSE_TEXTURE_MATRIX_ARB': 34021,
 'GL_TRIANGLES': 4,
 'GL_TRIANGLES_ADJACENCY': 12,
 'GL_TRIANGLES_ADJACENCY_ARB': 12,
 'GL_TRIANGLES_ADJACENCY_EXT': 12,
 'GL_TRIANGLE_FAN': 6,
 'GL_TRIANGLE_STRIP': 5,
 'GL_TRIANGLE_STRIP_ADJACENCY': 13,
 'GL_TRIANGLE_STRIP_ADJACENCY_ARB': 13,
 'GL_TRIANGLE_STRIP_ADJACENCY_EXT': 13,
 'GL_TRUE': 1,
 'GL_TYPE': 37626,
 'GL_UNDEFINED_VERTEX': 33376,
 'GL_UNDEFINED_VERTEX_EXT': 33376,
 'GL_UNIFORM': 37601,
 'GL_UNIFORM_ARRAY_STRIDE': 35388,
 'GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX': 37594,
 'GL_UNIFORM_BARRIER_BIT': 4,
 'GL_UNIFORM_BARRIER_BIT_EXT': 4,
 'GL_UNIFORM_BLOCK': 37602,
 'GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS': 35394,
 'GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES': 35395,
 'GL_UNIFORM_BLOCK_BINDING': 35391,
 'GL_UNIFORM_BLOCK_DATA_SIZE': 35392,
 'GL_UNIFORM_BLOCK_INDEX': 35386,
 'GL_UNIFORM_BLOCK_NAME_LENGTH': 35393,
 'GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER': 37100,
 'GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER': 35398,
 'GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER': 35397,
 'GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER': 34032,
 'GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER': 34033,
 'GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER': 35396,
 'GL_UNIFORM_BUFFER': 35345,
 'GL_UNIFORM_BUFFER_BINDING': 35368,
 'GL_UNIFORM_BUFFER_BINDING_EXT': 36335,
 'GL_UNIFORM_BUFFER_EXT': 36334,
 'GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT': 35380,
 'GL_UNIFORM_BUFFER_SIZE': 35370,
 'GL_UNIFORM_BUFFER_START': 35369,
 'GL_UNIFORM_IS_ROW_MAJOR': 35390,
 'GL_UNIFORM_MATRIX_STRIDE': 35389,
 'GL_UNIFORM_NAME_LENGTH': 35385,
 'GL_UNIFORM_OFFSET': 35387,
 'GL_UNIFORM_SIZE': 35384,
 'GL_UNIFORM_TYPE': 35383,
 'GL_UNKNOWN_CONTEXT_RESET': 33365,
 'GL_UNKNOWN_CONTEXT_RESET_ARB': 33365,
 'GL_UNKNOWN_CONTEXT_RESET_EXT': 33365,
 'GL_UNPACK_ALIGNMENT': 3317,
 'GL_UNPACK_CMYK_HINT_EXT': 32783,
 'GL_UNPACK_COLORSPACE_CONVERSION_WEBGL': 37443,
 'GL_UNPACK_COMPRESSED_BLOCK_DEPTH': 37161,
 'GL_UNPACK_COMPRESSED_BLOCK_HEIGHT': 37160,
 'GL_UNPACK_COMPRESSED_BLOCK_SIZE': 37162,
 'GL_UNPACK_COMPRESSED_BLOCK_WIDTH': 37159,
 'GL_UNPACK_CONSTANT_DATA_SUNX': 33237,
 'GL_UNPACK_FLIP_Y_WEBGL': 37440,
 'GL_UNPACK_IMAGE_HEIGHT': 32878,
 'GL_UNPACK_IMAGE_HEIGHT_EXT': 32878,
 'GL_UNPACK_LSB_FIRST': 3313,
 'GL_UNPACK_PREMULTIPLY_ALPHA_WEBGL': 37441,
 'GL_UNPACK_RESAMPLE_OML': 35205,
 'GL_UNPACK_ROW_LENGTH': 3314,
 'GL_UNPACK_ROW_LENGTH_EXT': 3314,
 'GL_UNPACK_SKIP_IMAGES': 32877,
 'GL_UNPACK_SKIP_IMAGES_EXT': 32877,
 'GL_UNPACK_SKIP_PIXELS': 3316,
 'GL_UNPACK_SKIP_PIXELS_EXT': 3316,
 'GL_UNPACK_SKIP_ROWS': 3315,
 'GL_UNPACK_SKIP_ROWS_EXT': 3315,
 'GL_UNPACK_SWAP_BYTES': 3312,
 'GL_UNSIGNALED': 37144,
 'GL_UNSIGNED_BYTE': 5121,
 'GL_UNSIGNED_BYTE_2_3_3_REV': 33634,
 'GL_UNSIGNED_BYTE_2_3_3_REV_EXT': 33634,
 'GL_UNSIGNED_BYTE_3_3_2': 32818,
 'GL_UNSIGNED_BYTE_3_3_2_EXT': 32818,
 'GL_UNSIGNED_INT': 5125,
 'GL_UNSIGNED_INT64_ARB': 5135,
 'GL_UNSIGNED_INT64_VEC2_ARB': 36853,
 'GL_UNSIGNED_INT64_VEC3_ARB': 36854,
 'GL_UNSIGNED_INT64_VEC4_ARB': 36855,
 'GL_UNSIGNED_INT_10F_11F_11F_REV': 35899,
 'GL_UNSIGNED_INT_10F_11F_11F_REV_EXT': 35899,
 'GL_UNSIGNED_INT_10_10_10_2': 32822,
 'GL_UNSIGNED_INT_10_10_10_2_EXT': 32822,
 'GL_UNSIGNED_INT_24_8': 34042,
 'GL_UNSIGNED_INT_24_8_EXT': 34042,
 'GL_UNSIGNED_INT_2_10_10_10_REV': 33640,
 'GL_UNSIGNED_INT_2_10_10_10_REV_EXT': 33640,
 'GL_UNSIGNED_INT_5_9_9_9_REV': 35902,
 'GL_UNSIGNED_INT_5_9_9_9_REV_EXT': 35902,
 'GL_UNSIGNED_INT_8_8_8_8': 32821,
 'GL_UNSIGNED_INT_8_8_8_8_EXT': 32821,
 'GL_UNSIGNED_INT_8_8_8_8_REV': 33639,
 'GL_UNSIGNED_INT_8_8_8_8_REV_EXT': 33639,
 'GL_UNSIGNED_INT_ATOMIC_COUNTER': 37595,
 'GL_UNSIGNED_INT_IMAGE_1D': 36962,
 'GL_UNSIGNED_INT_IMAGE_1D_ARRAY': 36968,
 'GL_UNSIGNED_INT_IMAGE_1D_ARRAY_EXT': 36968,
 'GL_UNSIGNED_INT_IMAGE_1D_EXT': 36962,
 'GL_UNSIGNED_INT_IMAGE_2D': 36963,
 'GL_UNSIGNED_INT_IMAGE_2D_ARRAY': 36969,
 'GL_UNSIGNED_INT_IMAGE_2D_ARRAY_EXT': 36969,
 'GL_UNSIGNED_INT_IMAGE_2D_EXT': 36963,
 'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE': 36971,
 'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY': 36972,
 'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT': 36972,
 'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_EXT': 36971,
 'GL_UNSIGNED_INT_IMAGE_2D_RECT': 36965,
 'GL_UNSIGNED_INT_IMAGE_2D_RECT_EXT': 36965,
 'GL_UNSIGNED_INT_IMAGE_3D': 36964,
 'GL_UNSIGNED_INT_IMAGE_3D_EXT': 36964,
 'GL_UNSIGNED_INT_IMAGE_BUFFER': 36967,
 'GL_UNSIGNED_INT_IMAGE_BUFFER_EXT': 36967,
 'GL_UNSIGNED_INT_IMAGE_CUBE': 36966,
 'GL_UNSIGNED_INT_IMAGE_CUBE_EXT': 36966,
 'GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY': 36970,
 'GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT': 36970,
 'GL_UNSIGNED_INT_SAMPLER_1D': 36305,
 'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY': 36310,
 'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY_EXT': 36310,
 'GL_UNSIGNED_INT_SAMPLER_1D_EXT': 36305,
 'GL_UNSIGNED_INT_SAMPLER_2D': 36306,
 'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY': 36311,
 'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY_EXT': 36311,
 'GL_UNSIGNED_INT_SAMPLER_2D_EXT': 36306,
 'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE': 37130,
 'GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY': 37133,
 'GL_UNSIGNED_INT_SAMPLER_2D_RECT': 36309,
 'GL_UNSIGNED_INT_SAMPLER_2D_RECT_EXT': 36309,
 'GL_UNSIGNED_INT_SAMPLER_3D': 36307,
 'GL_UNSIGNED_INT_SAMPLER_3D_EXT': 36307,
 'GL_UNSIGNED_INT_SAMPLER_BUFFER': 36312,
 'GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT': 36312,
 'GL_UNSIGNED_INT_SAMPLER_CUBE': 36308,
 'GL_UNSIGNED_INT_SAMPLER_CUBE_EXT': 36308,
 'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY': 36879,
 'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB': 36879,
 'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_EXT': 36879,
 'GL_UNSIGNED_INT_VEC2': 36294,
 'GL_UNSIGNED_INT_VEC2_EXT': 36294,
 'GL_UNSIGNED_INT_VEC3': 36295,
 'GL_UNSIGNED_INT_VEC3_EXT': 36295,
 'GL_UNSIGNED_INT_VEC4': 36296,
 'GL_UNSIGNED_INT_VEC4_EXT': 36296,
 'GL_UNSIGNED_NORMALIZED': 35863,
 'GL_UNSIGNED_NORMALIZED_ARB': 35863,
 'GL_UNSIGNED_NORMALIZED_EXT': 35863,
 'GL_UNSIGNED_SHORT': 5123,
 'GL_UNSIGNED_SHORT_1_5_5_5_REV': 33638,
 'GL_UNSIGNED_SHORT_1_5_5_5_REV_EXT': 33638,
 'GL_UNSIGNED_SHORT_4_4_4_4': 32819,
 'GL_UNSIGNED_SHORT_4_4_4_4_EXT': 32819,
 'GL_UNSIGNED_SHORT_4_4_4_4_REV': 33637,
 'GL_UNSIGNED_SHORT_4_4_4_4_REV_EXT': 33637,
 'GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG': 33637,
 'GL_UNSIGNED_SHORT_5_5_5_1': 32820,
 'GL_UNSIGNED_SHORT_5_5_5_1_EXT': 32820,
 'GL_UNSIGNED_SHORT_5_6_5': 33635,
 'GL_UNSIGNED_SHORT_5_6_5_EXT': 33635,
 'GL_UNSIGNED_SHORT_5_6_5_REV': 33636,
 'GL_UNSIGNED_SHORT_5_6_5_REV_EXT': 33636,
 'GL_UPLOAD_GPU_MASK_NVX': 38218,
 'GL_UPPER_LEFT': 36002,
 'GL_UPPER_LEFT_EXT': 36002,
 'GL_UUID_SIZE_EXT': 16,
 'GL_V2F': 10784,
 'GL_V3F': 10785,
 'GL_VALIDATE_STATUS': 35715,
 'GL_VARIANT_ARRAY_EXT': 34792,
 'GL_VARIANT_ARRAY_POINTER_EXT': 34793,
 'GL_VARIANT_ARRAY_STRIDE_EXT': 34790,
 'GL_VARIANT_ARRAY_TYPE_EXT': 34791,
 'GL_VARIANT_DATATYPE_EXT': 34789,
 'GL_VARIANT_EXT': 34753,
 'GL_VARIANT_VALUE_EXT': 34788,
 'GL_VECTOR_EXT': 34751,
 'GL_VENDOR': 7936,
 'GL_VERSION': 7938,
 'GL_VERSION_ES_CL_1_0': 1,
 'GL_VERSION_ES_CL_1_1': 1,
 'GL_VERSION_ES_CM_1_1': 1,
 'GL_VERTEX_ARRAY': 32884,
 'GL_VERTEX_ARRAY_BINDING': 34229,
 'GL_VERTEX_ARRAY_BUFFER_BINDING': 34966,
 'GL_VERTEX_ARRAY_BUFFER_BINDING_ARB': 34966,
 'GL_VERTEX_ARRAY_COUNT_EXT': 32893,
 'GL_VERTEX_ARRAY_EXT': 32884,
 'GL_VERTEX_ARRAY_OBJECT_EXT': 37204,
 'GL_VERTEX_ARRAY_POINTER': 32910,
 'GL_VERTEX_ARRAY_POINTER_EXT': 32910,
 'GL_VERTEX_ARRAY_SIZE': 32890,
 'GL_VERTEX_ARRAY_SIZE_EXT': 32890,
 'GL_VERTEX_ARRAY_STRIDE': 32892,
 'GL_VERTEX_ARRAY_STRIDE_EXT': 32892,
 'GL_VERTEX_ARRAY_TYPE': 32891,
 'GL_VERTEX_ARRAY_TYPE_EXT': 32891,
 'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT': 1,
 'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT_EXT': 1,
 'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING': 34975,
 'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB': 34975,
 'GL_VERTEX_ATTRIB_ARRAY_DIVISOR': 35070,
 'GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE': 35070,
 'GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB': 35070,
 'GL_VERTEX_ATTRIB_ARRAY_DIVISOR_EXT': 35070,
 'GL_VERTEX_ATTRIB_ARRAY_ENABLED': 34338,
 'GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB': 34338,
 'GL_VERTEX_ATTRIB_ARRAY_INTEGER': 35069,
 'GL_VERTEX_ATTRIB_ARRAY_INTEGER_EXT': 35069,
 'GL_VERTEX_ATTRIB_ARRAY_LONG': 34638,
 'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED': 34922,
 'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB': 34922,
 'GL_VERTEX_ATTRIB_ARRAY_POINTER': 34373,
 'GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB': 34373,
 'GL_VERTEX_ATTRIB_ARRAY_SIZE': 34339,
 'GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB': 34339,
 'GL_VERTEX_ATTRIB_ARRAY_STRIDE': 34340,
 'GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB': 34340,
 'GL_VERTEX_ATTRIB_ARRAY_TYPE': 34341,
 'GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB': 34341,
 'GL_VERTEX_ATTRIB_BINDING': 33492,
 'GL_VERTEX_ATTRIB_RELATIVE_OFFSET': 33493,
 'GL_VERTEX_BINDING_BUFFER': 36687,
 'GL_VERTEX_BINDING_DIVISOR': 33494,
 'GL_VERTEX_BINDING_OFFSET': 33495,
 'GL_VERTEX_BINDING_STRIDE': 33496,
 'GL_VERTEX_BLEND_ARB': 34471,
 'GL_VERTEX_PROGRAM_ARB': 34336,
 'GL_VERTEX_PROGRAM_POINT_SIZE': 34370,
 'GL_VERTEX_PROGRAM_POINT_SIZE_ARB': 34370,
 'GL_VERTEX_PROGRAM_TWO_SIDE': 34371,
 'GL_VERTEX_PROGRAM_TWO_SIDE_ARB': 34371,
 'GL_VERTEX_SHADER': 35633,
 'GL_VERTEX_SHADER_ARB': 35633,
 'GL_VERTEX_SHADER_BINDING_EXT': 34689,
 'GL_VERTEX_SHADER_BIT': 1,
 'GL_VERTEX_SHADER_BIT_EXT': 1,
 'GL_VERTEX_SHADER_EXT': 34688,
 'GL_VERTEX_SHADER_INSTRUCTIONS_EXT': 34767,
 'GL_VERTEX_SHADER_INVARIANTS_EXT': 34769,
 'GL_VERTEX_SHADER_INVOCATIONS': 33520,
 'GL_VERTEX_SHADER_INVOCATIONS_ARB': 33520,
 'GL_VERTEX_SHADER_LOCALS_EXT': 34771,
 'GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT': 34770,
 'GL_VERTEX_SHADER_OPTIMIZED_EXT': 34772,
 'GL_VERTEX_SHADER_VARIANTS_EXT': 34768,
 'GL_VERTEX_SUBROUTINE': 37608,
 'GL_VERTEX_SUBROUTINE_UNIFORM': 37614,
 'GL_VERTEX_TEXTURE': 33435,
 'GL_VERTEX_WEIGHTING_EXT': 34057,
 'GL_VERTEX_WEIGHT_ARRAY_EXT': 34060,
 'GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT': 34064,
 'GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT': 34061,
 'GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT': 34063,
 'GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT': 34062,
 'GL_VERTICES_SUBMITTED': 33518,
 'GL_VERTICES_SUBMITTED_ARB': 33518,
 'GL_VIEWPORT': 2978,
 'GL_VIEWPORT_BIT': 2048,
 'GL_VIEWPORT_BOUNDS_RANGE': 33373,
 'GL_VIEWPORT_BOUNDS_RANGE_EXT': 33373,
 'GL_VIEWPORT_INDEX_PROVOKING_VERTEX': 33375,
 'GL_VIEWPORT_INDEX_PROVOKING_VERTEX_EXT': 33375,
 'GL_VIEWPORT_SUBPIXEL_BITS': 33372,
 'GL_VIEWPORT_SUBPIXEL_BITS_EXT': 33372,
 'GL_VIEW_CLASS_128_BITS': 33476,
 'GL_VIEW_CLASS_16_BITS': 33482,
 'GL_VIEW_CLASS_24_BITS': 33481,
 'GL_VIEW_CLASS_32_BITS': 33480,
 'GL_VIEW_CLASS_48_BITS': 33479,
 'GL_VIEW_CLASS_64_BITS': 33478,
 'GL_VIEW_CLASS_8_BITS': 33483,
 'GL_VIEW_CLASS_96_BITS': 33477,
 'GL_VIEW_CLASS_ASTC_10x10_RGBA': 37779,
 'GL_VIEW_CLASS_ASTC_10x5_RGBA': 37776,
 'GL_VIEW_CLASS_ASTC_10x6_RGBA': 37777,
 'GL_VIEW_CLASS_ASTC_10x8_RGBA': 37778,
 'GL_VIEW_CLASS_ASTC_12x10_RGBA': 37780,
 'GL_VIEW_CLASS_ASTC_12x12_RGBA': 37781,
 'GL_VIEW_CLASS_ASTC_4x4_RGBA': 37768,
 'GL_VIEW_CLASS_ASTC_5x4_RGBA': 37769,
 'GL_VIEW_CLASS_ASTC_5x5_RGBA': 37770,
 'GL_VIEW_CLASS_ASTC_6x5_RGBA': 37771,
 'GL_VIEW_CLASS_ASTC_6x6_RGBA': 37772,
 'GL_VIEW_CLASS_ASTC_8x5_RGBA': 37773,
 'GL_VIEW_CLASS_ASTC_8x6_RGBA': 37774,
 'GL_VIEW_CLASS_ASTC_8x8_RGBA': 37775,
 'GL_VIEW_CLASS_BPTC_FLOAT': 33491,
 'GL_VIEW_CLASS_BPTC_UNORM': 33490,
 'GL_VIEW_CLASS_EAC_R11': 37763,
 'GL_VIEW_CLASS_EAC_RG11': 37764,
 'GL_VIEW_CLASS_ETC2_EAC_RGBA': 37767,
 'GL_VIEW_CLASS_ETC2_RGB': 37765,
 'GL_VIEW_CLASS_ETC2_RGBA': 37766,
 'GL_VIEW_CLASS_RGTC1_RED': 33488,
 'GL_VIEW_CLASS_RGTC2_RG': 33489,
 'GL_VIEW_CLASS_S3TC_DXT1_RGB': 33484,
 'GL_VIEW_CLASS_S3TC_DXT1_RGBA': 33485,
 'GL_VIEW_CLASS_S3TC_DXT3_RGBA': 33486,
 'GL_VIEW_CLASS_S3TC_DXT5_RGBA': 33487,
 'GL_VIEW_COMPATIBILITY_CLASS': 33462,
 'GL_VIRTUAL_PAGE_SIZE_INDEX_ARB': 37287,
 'GL_VIRTUAL_PAGE_SIZE_INDEX_EXT': 37287,
 'GL_VIRTUAL_PAGE_SIZE_X_ARB': 37269,
 'GL_VIRTUAL_PAGE_SIZE_X_EXT': 37269,
 'GL_VIRTUAL_PAGE_SIZE_Y_ARB': 37270,
 'GL_VIRTUAL_PAGE_SIZE_Y_EXT': 37270,
 'GL_VIRTUAL_PAGE_SIZE_Z_ARB': 37271,
 'GL_VIRTUAL_PAGE_SIZE_Z_EXT': 37271,
 'GL_WAIT_FAILED': 37149,
 'GL_WEIGHTED_AVERAGE_ARB': 37735,
 'GL_WEIGHTED_AVERAGE_EXT': 37735,
 'GL_WEIGHT_ARRAY_ARB': 34477,
 'GL_WEIGHT_ARRAY_BUFFER_BINDING': 34974,
 'GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB': 34974,
 'GL_WEIGHT_ARRAY_POINTER_ARB': 34476,
 'GL_WEIGHT_ARRAY_SIZE_ARB': 34475,
 'GL_WEIGHT_ARRAY_STRIDE_ARB': 34474,
 'GL_WEIGHT_ARRAY_TYPE_ARB': 34473,
 'GL_WEIGHT_SUM_UNITY_ARB': 34470,
 'GL_WINDOW_RECTANGLE_EXT': 36626,
 'GL_WINDOW_RECTANGLE_MODE_EXT': 36627,
 'GL_WRITE_ONLY': 35001,
 'GL_WRITE_ONLY_ARB': 35001,
 'GL_W_EXT': 34776,
 'GL_XOR': 5382,
 'GL_X_EXT': 34773,
 'GL_Y_EXT': 34774,
 'GL_ZERO': 0,
 'GL_ZERO_EXT': 34781,
 'GL_ZERO_TO_ONE': 37727,
 'GL_ZERO_TO_ONE_EXT': 37727,
 'GL_ZOOM_X': 3350,
 'GL_ZOOM_Y': 3351,
 'GL_Z_EXT': 34775}
glivalues= {0: ['GL_FALSE', 'GL_NO_ERROR', 'GL_ZERO', 'GL_NONE', 'GL_POINTS'],
 1: ['GL_CURRENT_BIT',
     'GL_CLIENT_PIXEL_STORE_BIT',
     'GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT',
     'GL_CONTEXT_CORE_PROFILE_BIT',
     'GL_MAP_READ_BIT',
     'GL_MAP_READ_BIT_EXT',
     'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT',
     'GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT_EXT',
     'GL_SYNC_FLUSH_COMMANDS_BIT',
     'GL_VERTEX_SHADER_BIT',
     'GL_VERTEX_SHADER_BIT_EXT',
     'GL_TRUE',
     'GL_ONE',
     'GL_VERSION_ES_CL_1_0',
     'GL_VERSION_ES_CM_1_1',
     'GL_VERSION_ES_CL_1_1',
     'GL_LINES'],
 2: ['GL_POINT_BIT',
     'GL_CLIENT_VERTEX_ARRAY_BIT',
     'GL_CONTEXT_FLAG_DEBUG_BIT',
     'GL_CONTEXT_COMPATIBILITY_PROFILE_BIT',
     'GL_MAP_WRITE_BIT',
     'GL_MAP_WRITE_BIT_EXT',
     'GL_ELEMENT_ARRAY_BARRIER_BIT',
     'GL_ELEMENT_ARRAY_BARRIER_BIT_EXT',
     'GL_FRAGMENT_SHADER_BIT',
     'GL_FRAGMENT_SHADER_BIT_EXT',
     'GL_LINE_LOOP'],
 3: ['GL_LINE_STRIP'],
 4: ['GL_LINE_BIT',
     'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT',
     'GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB',
     'GL_MAP_INVALIDATE_RANGE_BIT',
     'GL_MAP_INVALIDATE_RANGE_BIT_EXT',
     'GL_UNIFORM_BARRIER_BIT',
     'GL_UNIFORM_BARRIER_BIT_EXT',
     'GL_GEOMETRY_SHADER_BIT',
     'GL_GEOMETRY_SHADER_BIT_EXT',
     'GL_TRIANGLES'],
 5: ['GL_TRIANGLE_STRIP'],
 6: ['GL_TRIANGLE_FAN'],
 7: ['GL_QUADS', 'GL_QUADS_EXT'],
 8: ['GL_POLYGON_BIT',
     'GL_CONTEXT_FLAG_NO_ERROR_BIT',
     'GL_MAP_INVALIDATE_BUFFER_BIT',
     'GL_MAP_INVALIDATE_BUFFER_BIT_EXT',
     'GL_TEXTURE_FETCH_BARRIER_BIT',
     'GL_TEXTURE_FETCH_BARRIER_BIT_EXT',
     'GL_TESS_CONTROL_SHADER_BIT',
     'GL_TESS_CONTROL_SHADER_BIT_EXT',
     'GL_LUID_SIZE_EXT',
     'GL_QUAD_STRIP'],
 9: ['GL_POLYGON'],
 10: ['GL_LINES_ADJACENCY', 'GL_LINES_ADJACENCY_ARB', 'GL_LINES_ADJACENCY_EXT'],
 11: ['GL_LINE_STRIP_ADJACENCY',
      'GL_LINE_STRIP_ADJACENCY_ARB',
      'GL_LINE_STRIP_ADJACENCY_EXT'],
 12: ['GL_TRIANGLES_ADJACENCY',
      'GL_TRIANGLES_ADJACENCY_ARB',
      'GL_TRIANGLES_ADJACENCY_EXT'],
 13: ['GL_TRIANGLE_STRIP_ADJACENCY',
      'GL_TRIANGLE_STRIP_ADJACENCY_ARB',
      'GL_TRIANGLE_STRIP_ADJACENCY_EXT'],
 14: ['GL_PATCHES', 'GL_PATCHES_EXT'],
 16: ['GL_POLYGON_STIPPLE_BIT',
      'GL_CONTEXT_FLAG_PROTECTED_CONTENT_BIT_EXT',
      'GL_MAP_FLUSH_EXPLICIT_BIT',
      'GL_MAP_FLUSH_EXPLICIT_BIT_EXT',
      'GL_TESS_EVALUATION_SHADER_BIT',
      'GL_TESS_EVALUATION_SHADER_BIT_EXT',
      'GL_UUID_SIZE_EXT'],
 32: ['GL_PIXEL_MODE_BIT',
      'GL_MAP_UNSYNCHRONIZED_BIT',
      'GL_MAP_UNSYNCHRONIZED_BIT_EXT',
      'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT',
      'GL_SHADER_IMAGE_ACCESS_BARRIER_BIT_EXT',
      'GL_COMPUTE_SHADER_BIT'],
 64: ['GL_LIGHTING_BIT',
      'GL_MAP_PERSISTENT_BIT',
      'GL_MAP_PERSISTENT_BIT_EXT',
      'GL_COMMAND_BARRIER_BIT',
      'GL_COMMAND_BARRIER_BIT_EXT'],
 128: ['GL_FOG_BIT',
       'GL_MAP_COHERENT_BIT',
       'GL_MAP_COHERENT_BIT_EXT',
       'GL_PIXEL_BUFFER_BARRIER_BIT',
       'GL_PIXEL_BUFFER_BARRIER_BIT_EXT'],
 256: ['GL_DEPTH_BUFFER_BIT',
       'GL_DYNAMIC_STORAGE_BIT',
       'GL_DYNAMIC_STORAGE_BIT_EXT',
       'GL_TEXTURE_UPDATE_BARRIER_BIT',
       'GL_TEXTURE_UPDATE_BARRIER_BIT_EXT',
       'GL_ACCUM'],
 257: ['GL_LOAD'],
 258: ['GL_RETURN'],
 259: ['GL_MULT'],
 260: ['GL_ADD'],
 512: ['GL_ACCUM_BUFFER_BIT',
       'GL_CLIENT_STORAGE_BIT',
       'GL_CLIENT_STORAGE_BIT_EXT',
       'GL_BUFFER_UPDATE_BARRIER_BIT',
       'GL_BUFFER_UPDATE_BARRIER_BIT_EXT',
       'GL_NEVER'],
 513: ['GL_LESS'],
 514: ['GL_EQUAL'],
 515: ['GL_LEQUAL'],
 516: ['GL_GREATER'],
 517: ['GL_NOTEQUAL'],
 518: ['GL_GEQUAL'],
 519: ['GL_ALWAYS'],
 768: ['GL_SRC_COLOR'],
 769: ['GL_ONE_MINUS_SRC_COLOR'],
 770: ['GL_SRC_ALPHA'],
 771: ['GL_ONE_MINUS_SRC_ALPHA'],
 772: ['GL_DST_ALPHA'],
 773: ['GL_ONE_MINUS_DST_ALPHA'],
 774: ['GL_DST_COLOR'],
 775: ['GL_ONE_MINUS_DST_COLOR'],
 776: ['GL_SRC_ALPHA_SATURATE', 'GL_SRC_ALPHA_SATURATE_EXT'],
 1024: ['GL_STENCIL_BUFFER_BIT',
        'GL_SPARSE_STORAGE_BIT_ARB',
        'GL_FRAMEBUFFER_BARRIER_BIT',
        'GL_FRAMEBUFFER_BARRIER_BIT_EXT',
        'GL_FRONT_LEFT'],
 1025: ['GL_FRONT_RIGHT'],
 1026: ['GL_BACK_LEFT'],
 1027: ['GL_BACK_RIGHT'],
 1028: ['GL_FRONT'],
 1029: ['GL_BACK'],
 1030: ['GL_LEFT'],
 1031: ['GL_RIGHT'],
 1032: ['GL_FRONT_AND_BACK'],
 1033: ['GL_AUX0'],
 1034: ['GL_AUX1'],
 1035: ['GL_AUX2'],
 1036: ['GL_AUX3'],
 1280: ['GL_INVALID_ENUM'],
 1281: ['GL_INVALID_VALUE'],
 1282: ['GL_INVALID_OPERATION'],
 1283: ['GL_STACK_OVERFLOW'],
 1284: ['GL_STACK_UNDERFLOW'],
 1285: ['GL_OUT_OF_MEMORY'],
 1286: ['GL_INVALID_FRAMEBUFFER_OPERATION',
        'GL_INVALID_FRAMEBUFFER_OPERATION_EXT'],
 1287: ['GL_CONTEXT_LOST'],
 1536: ['GL_2D'],
 1537: ['GL_3D'],
 1538: ['GL_3D_COLOR'],
 1539: ['GL_3D_COLOR_TEXTURE'],
 1540: ['GL_4D_COLOR_TEXTURE'],
 1792: ['GL_PASS_THROUGH_TOKEN'],
 1793: ['GL_POINT_TOKEN'],
 1794: ['GL_LINE_TOKEN'],
 1795: ['GL_POLYGON_TOKEN'],
 1796: ['GL_BITMAP_TOKEN'],
 1797: ['GL_DRAW_PIXEL_TOKEN'],
 1798: ['GL_COPY_PIXEL_TOKEN'],
 1799: ['GL_LINE_RESET_TOKEN'],
 2048: ['GL_VIEWPORT_BIT',
        'GL_LGPU_SEPARATE_STORAGE_BIT_NVX',
        'GL_TRANSFORM_FEEDBACK_BARRIER_BIT',
        'GL_TRANSFORM_FEEDBACK_BARRIER_BIT_EXT',
        'GL_EXP'],
 2049: ['GL_EXP2'],
 2304: ['GL_CW'],
 2305: ['GL_CCW'],
 2560: ['GL_COEFF'],
 2561: ['GL_ORDER'],
 2562: ['GL_DOMAIN'],
 2816: ['GL_CURRENT_COLOR'],
 2817: ['GL_CURRENT_INDEX'],
 2818: ['GL_CURRENT_NORMAL'],
 2819: ['GL_CURRENT_TEXTURE_COORDS'],
 2820: ['GL_CURRENT_RASTER_COLOR'],
 2821: ['GL_CURRENT_RASTER_INDEX'],
 2822: ['GL_CURRENT_RASTER_TEXTURE_COORDS'],
 2823: ['GL_CURRENT_RASTER_POSITION'],
 2824: ['GL_CURRENT_RASTER_POSITION_VALID'],
 2825: ['GL_CURRENT_RASTER_DISTANCE'],
 2832: ['GL_POINT_SMOOTH'],
 2833: ['GL_POINT_SIZE'],
 2834: ['GL_POINT_SIZE_RANGE', 'GL_SMOOTH_POINT_SIZE_RANGE'],
 2835: ['GL_POINT_SIZE_GRANULARITY', 'GL_SMOOTH_POINT_SIZE_GRANULARITY'],
 2848: ['GL_LINE_SMOOTH'],
 2849: ['GL_LINE_WIDTH'],
 2850: ['GL_LINE_WIDTH_RANGE', 'GL_SMOOTH_LINE_WIDTH_RANGE'],
 2851: ['GL_LINE_WIDTH_GRANULARITY', 'GL_SMOOTH_LINE_WIDTH_GRANULARITY'],
 2852: ['GL_LINE_STIPPLE'],
 2853: ['GL_LINE_STIPPLE_PATTERN'],
 2854: ['GL_LINE_STIPPLE_REPEAT'],
 2864: ['GL_LIST_MODE'],
 2865: ['GL_MAX_LIST_NESTING'],
 2866: ['GL_LIST_BASE'],
 2867: ['GL_LIST_INDEX'],
 2880: ['GL_POLYGON_MODE'],
 2881: ['GL_POLYGON_SMOOTH'],
 2882: ['GL_POLYGON_STIPPLE'],
 2883: ['GL_EDGE_FLAG'],
 2884: ['GL_CULL_FACE'],
 2885: ['GL_CULL_FACE_MODE'],
 2886: ['GL_FRONT_FACE'],
 2896: ['GL_LIGHTING'],
 2897: ['GL_LIGHT_MODEL_LOCAL_VIEWER'],
 2898: ['GL_LIGHT_MODEL_TWO_SIDE'],
 2899: ['GL_LIGHT_MODEL_AMBIENT'],
 2900: ['GL_SHADE_MODEL'],
 2901: ['GL_COLOR_MATERIAL_FACE'],
 2902: ['GL_COLOR_MATERIAL_PARAMETER'],
 2903: ['GL_COLOR_MATERIAL'],
 2912: ['GL_FOG'],
 2913: ['GL_FOG_INDEX'],
 2914: ['GL_FOG_DENSITY'],
 2915: ['GL_FOG_START'],
 2916: ['GL_FOG_END'],
 2917: ['GL_FOG_MODE'],
 2918: ['GL_FOG_COLOR'],
 2928: ['GL_DEPTH_RANGE'],
 2929: ['GL_DEPTH_TEST'],
 2930: ['GL_DEPTH_WRITEMASK'],
 2931: ['GL_DEPTH_CLEAR_VALUE'],
 2932: ['GL_DEPTH_FUNC'],
 2944: ['GL_ACCUM_CLEAR_VALUE'],
 2960: ['GL_STENCIL_TEST'],
 2961: ['GL_STENCIL_CLEAR_VALUE'],
 2962: ['GL_STENCIL_FUNC'],
 2963: ['GL_STENCIL_VALUE_MASK'],
 2964: ['GL_STENCIL_FAIL'],
 2965: ['GL_STENCIL_PASS_DEPTH_FAIL'],
 2966: ['GL_STENCIL_PASS_DEPTH_PASS'],
 2967: ['GL_STENCIL_REF'],
 2968: ['GL_STENCIL_WRITEMASK'],
 2976: ['GL_MATRIX_MODE'],
 2977: ['GL_NORMALIZE'],
 2978: ['GL_VIEWPORT'],
 2979: ['GL_MODELVIEW_STACK_DEPTH', 'GL_MODELVIEW0_STACK_DEPTH_EXT'],
 2980: ['GL_PROJECTION_STACK_DEPTH'],
 2981: ['GL_TEXTURE_STACK_DEPTH'],
 2982: ['GL_MODELVIEW_MATRIX', 'GL_MODELVIEW0_MATRIX_EXT'],
 2983: ['GL_PROJECTION_MATRIX'],
 2984: ['GL_TEXTURE_MATRIX'],
 2992: ['GL_ATTRIB_STACK_DEPTH'],
 2993: ['GL_CLIENT_ATTRIB_STACK_DEPTH'],
 3008: ['GL_ALPHA_TEST'],
 3009: ['GL_ALPHA_TEST_FUNC'],
 3010: ['GL_ALPHA_TEST_REF'],
 3024: ['GL_DITHER'],
 3040: ['GL_BLEND_DST'],
 3041: ['GL_BLEND_SRC'],
 3042: ['GL_BLEND'],
 3056: ['GL_LOGIC_OP_MODE'],
 3057: ['GL_INDEX_LOGIC_OP', 'GL_LOGIC_OP'],
 3058: ['GL_COLOR_LOGIC_OP'],
 3072: ['GL_AUX_BUFFERS'],
 3073: ['GL_DRAW_BUFFER', 'GL_DRAW_BUFFER_EXT'],
 3074: ['GL_READ_BUFFER', 'GL_READ_BUFFER_EXT'],
 3088: ['GL_SCISSOR_BOX'],
 3089: ['GL_SCISSOR_TEST'],
 3104: ['GL_INDEX_CLEAR_VALUE'],
 3105: ['GL_INDEX_WRITEMASK'],
 3106: ['GL_COLOR_CLEAR_VALUE'],
 3107: ['GL_COLOR_WRITEMASK'],
 3120: ['GL_INDEX_MODE'],
 3121: ['GL_RGBA_MODE'],
 3122: ['GL_DOUBLEBUFFER'],
 3123: ['GL_STEREO'],
 3136: ['GL_RENDER_MODE'],
 3152: ['GL_PERSPECTIVE_CORRECTION_HINT'],
 3153: ['GL_POINT_SMOOTH_HINT'],
 3154: ['GL_LINE_SMOOTH_HINT'],
 3155: ['GL_POLYGON_SMOOTH_HINT'],
 3156: ['GL_FOG_HINT'],
 3168: ['GL_TEXTURE_GEN_S'],
 3169: ['GL_TEXTURE_GEN_T'],
 3170: ['GL_TEXTURE_GEN_R'],
 3171: ['GL_TEXTURE_GEN_Q'],
 3184: ['GL_PIXEL_MAP_I_TO_I'],
 3185: ['GL_PIXEL_MAP_S_TO_S'],
 3186: ['GL_PIXEL_MAP_I_TO_R'],
 3187: ['GL_PIXEL_MAP_I_TO_G'],
 3188: ['GL_PIXEL_MAP_I_TO_B'],
 3189: ['GL_PIXEL_MAP_I_TO_A'],
 3190: ['GL_PIXEL_MAP_R_TO_R'],
 3191: ['GL_PIXEL_MAP_G_TO_G'],
 3192: ['GL_PIXEL_MAP_B_TO_B'],
 3193: ['GL_PIXEL_MAP_A_TO_A'],
 3248: ['GL_PIXEL_MAP_I_TO_I_SIZE'],
 3249: ['GL_PIXEL_MAP_S_TO_S_SIZE'],
 3250: ['GL_PIXEL_MAP_I_TO_R_SIZE'],
 3251: ['GL_PIXEL_MAP_I_TO_G_SIZE'],
 3252: ['GL_PIXEL_MAP_I_TO_B_SIZE'],
 3253: ['GL_PIXEL_MAP_I_TO_A_SIZE'],
 3254: ['GL_PIXEL_MAP_R_TO_R_SIZE'],
 3255: ['GL_PIXEL_MAP_G_TO_G_SIZE'],
 3256: ['GL_PIXEL_MAP_B_TO_B_SIZE'],
 3257: ['GL_PIXEL_MAP_A_TO_A_SIZE'],
 3312: ['GL_UNPACK_SWAP_BYTES'],
 3313: ['GL_UNPACK_LSB_FIRST'],
 3314: ['GL_UNPACK_ROW_LENGTH', 'GL_UNPACK_ROW_LENGTH_EXT'],
 3315: ['GL_UNPACK_SKIP_ROWS', 'GL_UNPACK_SKIP_ROWS_EXT'],
 3316: ['GL_UNPACK_SKIP_PIXELS', 'GL_UNPACK_SKIP_PIXELS_EXT'],
 3317: ['GL_UNPACK_ALIGNMENT'],
 3328: ['GL_PACK_SWAP_BYTES'],
 3329: ['GL_PACK_LSB_FIRST'],
 3330: ['GL_PACK_ROW_LENGTH'],
 3331: ['GL_PACK_SKIP_ROWS'],
 3332: ['GL_PACK_SKIP_PIXELS'],
 3333: ['GL_PACK_ALIGNMENT'],
 3344: ['GL_MAP_COLOR'],
 3345: ['GL_MAP_STENCIL'],
 3346: ['GL_INDEX_SHIFT'],
 3347: ['GL_INDEX_OFFSET'],
 3348: ['GL_RED_SCALE'],
 3349: ['GL_RED_BIAS'],
 3350: ['GL_ZOOM_X'],
 3351: ['GL_ZOOM_Y'],
 3352: ['GL_GREEN_SCALE'],
 3353: ['GL_GREEN_BIAS'],
 3354: ['GL_BLUE_SCALE'],
 3355: ['GL_BLUE_BIAS'],
 3356: ['GL_ALPHA_SCALE'],
 3357: ['GL_ALPHA_BIAS'],
 3358: ['GL_DEPTH_SCALE'],
 3359: ['GL_DEPTH_BIAS'],
 3376: ['GL_MAX_EVAL_ORDER'],
 3377: ['GL_MAX_LIGHTS'],
 3378: ['GL_MAX_CLIP_PLANES',
        'GL_MAX_CLIP_PLANES_IMG',
        'GL_MAX_CLIP_DISTANCES',
        'GL_MAX_CLIP_DISTANCES_EXT'],
 3379: ['GL_MAX_TEXTURE_SIZE'],
 3380: ['GL_MAX_PIXEL_MAP_TABLE'],
 3381: ['GL_MAX_ATTRIB_STACK_DEPTH'],
 3382: ['GL_MAX_MODELVIEW_STACK_DEPTH'],
 3383: ['GL_MAX_NAME_STACK_DEPTH'],
 3384: ['GL_MAX_PROJECTION_STACK_DEPTH'],
 3385: ['GL_MAX_TEXTURE_STACK_DEPTH'],
 3386: ['GL_MAX_VIEWPORT_DIMS'],
 3387: ['GL_MAX_CLIENT_ATTRIB_STACK_DEPTH'],
 3408: ['GL_SUBPIXEL_BITS'],
 3409: ['GL_INDEX_BITS'],
 3410: ['GL_RED_BITS'],
 3411: ['GL_GREEN_BITS'],
 3412: ['GL_BLUE_BITS'],
 3413: ['GL_ALPHA_BITS'],
 3414: ['GL_DEPTH_BITS'],
 3415: ['GL_STENCIL_BITS'],
 3416: ['GL_ACCUM_RED_BITS'],
 3417: ['GL_ACCUM_GREEN_BITS'],
 3418: ['GL_ACCUM_BLUE_BITS'],
 3419: ['GL_ACCUM_ALPHA_BITS'],
 3440: ['GL_NAME_STACK_DEPTH'],
 3456: ['GL_AUTO_NORMAL'],
 3472: ['GL_MAP1_COLOR_4'],
 3473: ['GL_MAP1_INDEX'],
 3474: ['GL_MAP1_NORMAL'],
 3475: ['GL_MAP1_TEXTURE_COORD_1'],
 3476: ['GL_MAP1_TEXTURE_COORD_2'],
 3477: ['GL_MAP1_TEXTURE_COORD_3'],
 3478: ['GL_MAP1_TEXTURE_COORD_4'],
 3479: ['GL_MAP1_VERTEX_3'],
 3480: ['GL_MAP1_VERTEX_4'],
 3504: ['GL_MAP2_COLOR_4'],
 3505: ['GL_MAP2_INDEX'],
 3506: ['GL_MAP2_NORMAL'],
 3507: ['GL_MAP2_TEXTURE_COORD_1'],
 3508: ['GL_MAP2_TEXTURE_COORD_2'],
 3509: ['GL_MAP2_TEXTURE_COORD_3'],
 3510: ['GL_MAP2_TEXTURE_COORD_4'],
 3511: ['GL_MAP2_VERTEX_3'],
 3512: ['GL_MAP2_VERTEX_4'],
 3536: ['GL_MAP1_GRID_DOMAIN'],
 3537: ['GL_MAP1_GRID_SEGMENTS'],
 3538: ['GL_MAP2_GRID_DOMAIN'],
 3539: ['GL_MAP2_GRID_SEGMENTS'],
 3552: ['GL_TEXTURE_1D'],
 3553: ['GL_TEXTURE_2D'],
 3568: ['GL_FEEDBACK_BUFFER_POINTER'],
 3569: ['GL_FEEDBACK_BUFFER_SIZE'],
 3570: ['GL_FEEDBACK_BUFFER_TYPE'],
 3571: ['GL_SELECTION_BUFFER_POINTER'],
 3572: ['GL_SELECTION_BUFFER_SIZE'],
 4096: ['GL_TRANSFORM_BIT',
        'GL_ATOMIC_COUNTER_BARRIER_BIT',
        'GL_ATOMIC_COUNTER_BARRIER_BIT_EXT',
        'GL_TEXTURE_WIDTH'],
 4097: ['GL_TEXTURE_HEIGHT'],
 4099: ['GL_TEXTURE_INTERNAL_FORMAT', 'GL_TEXTURE_COMPONENTS'],
 4100: ['GL_TEXTURE_BORDER_COLOR', 'GL_TEXTURE_BORDER_COLOR_EXT'],
 4101: ['GL_TEXTURE_BORDER'],
 4102: ['GL_TEXTURE_TARGET'],
 4352: ['GL_DONT_CARE'],
 4353: ['GL_FASTEST'],
 4354: ['GL_NICEST'],
 4608: ['GL_AMBIENT'],
 4609: ['GL_DIFFUSE'],
 4610: ['GL_SPECULAR'],
 4611: ['GL_POSITION'],
 4612: ['GL_SPOT_DIRECTION'],
 4613: ['GL_SPOT_EXPONENT'],
 4614: ['GL_SPOT_CUTOFF'],
 4615: ['GL_CONSTANT_ATTENUATION'],
 4616: ['GL_LINEAR_ATTENUATION'],
 4617: ['GL_QUADRATIC_ATTENUATION'],
 4864: ['GL_COMPILE'],
 4865: ['GL_COMPILE_AND_EXECUTE'],
 5120: ['GL_BYTE'],
 5121: ['GL_UNSIGNED_BYTE'],
 5122: ['GL_SHORT'],
 5123: ['GL_UNSIGNED_SHORT'],
 5124: ['GL_INT'],
 5125: ['GL_UNSIGNED_INT'],
 5126: ['GL_FLOAT'],
 5127: ['GL_2_BYTES'],
 5128: ['GL_3_BYTES'],
 5129: ['GL_4_BYTES'],
 5130: ['GL_DOUBLE', 'GL_DOUBLE_EXT'],
 5131: ['GL_HALF_FLOAT', 'GL_HALF_FLOAT_ARB'],
 5132: ['GL_FIXED'],
 5134: ['GL_INT64_ARB'],
 5135: ['GL_UNSIGNED_INT64_ARB'],
 5376: ['GL_CLEAR'],
 5377: ['GL_AND'],
 5378: ['GL_AND_REVERSE'],
 5379: ['GL_COPY'],
 5380: ['GL_AND_INVERTED'],
 5381: ['GL_NOOP'],
 5382: ['GL_XOR'],
 5383: ['GL_OR'],
 5384: ['GL_NOR'],
 5385: ['GL_EQUIV'],
 5386: ['GL_INVERT'],
 5387: ['GL_OR_REVERSE'],
 5388: ['GL_COPY_INVERTED'],
 5389: ['GL_OR_INVERTED'],
 5390: ['GL_NAND'],
 5391: ['GL_SET'],
 5632: ['GL_EMISSION'],
 5633: ['GL_SHININESS'],
 5634: ['GL_AMBIENT_AND_DIFFUSE'],
 5635: ['GL_COLOR_INDEXES'],
 5888: ['GL_MODELVIEW', 'GL_MODELVIEW0_ARB', 'GL_MODELVIEW0_EXT'],
 5889: ['GL_PROJECTION'],
 5890: ['GL_TEXTURE'],
 6144: ['GL_COLOR', 'GL_COLOR_EXT'],
 6145: ['GL_DEPTH', 'GL_DEPTH_EXT'],
 6146: ['GL_STENCIL', 'GL_STENCIL_EXT'],
 6400: ['GL_COLOR_INDEX'],
 6401: ['GL_STENCIL_INDEX'],
 6402: ['GL_DEPTH_COMPONENT'],
 6403: ['GL_RED', 'GL_RED_EXT'],
 6404: ['GL_GREEN'],
 6405: ['GL_BLUE'],
 6406: ['GL_ALPHA'],
 6407: ['GL_RGB'],
 6408: ['GL_RGBA'],
 6409: ['GL_LUMINANCE'],
 6410: ['GL_LUMINANCE_ALPHA'],
 6656: ['GL_BITMAP'],
 6912: ['GL_POINT'],
 6913: ['GL_LINE'],
 6914: ['GL_FILL'],
 7168: ['GL_RENDER'],
 7169: ['GL_FEEDBACK'],
 7170: ['GL_SELECT'],
 7424: ['GL_FLAT'],
 7425: ['GL_SMOOTH'],
 7680: ['GL_KEEP'],
 7681: ['GL_REPLACE'],
 7682: ['GL_INCR'],
 7683: ['GL_DECR'],
 7936: ['GL_VENDOR'],
 7937: ['GL_RENDERER'],
 7938: ['GL_VERSION'],
 7939: ['GL_EXTENSIONS'],
 8192: ['GL_ENABLE_BIT',
        'GL_EXTERNAL_STORAGE_BIT_NVX',
        'GL_SHADER_STORAGE_BARRIER_BIT',
        'GL_S'],
 8193: ['GL_T'],
 8194: ['GL_R'],
 8195: ['GL_Q'],
 8448: ['GL_MODULATE'],
 8449: ['GL_DECAL'],
 8704: ['GL_TEXTURE_ENV_MODE'],
 8705: ['GL_TEXTURE_ENV_COLOR'],
 9216: ['GL_EYE_LINEAR'],
 9217: ['GL_OBJECT_LINEAR'],
 9218: ['GL_SPHERE_MAP'],
 9472: ['GL_TEXTURE_GEN_MODE'],
 9473: ['GL_OBJECT_PLANE'],
 9474: ['GL_EYE_PLANE'],
 9728: ['GL_NEAREST'],
 9729: ['GL_LINEAR'],
 9984: ['GL_NEAREST_MIPMAP_NEAREST'],
 9985: ['GL_LINEAR_MIPMAP_NEAREST'],
 9986: ['GL_NEAREST_MIPMAP_LINEAR'],
 9987: ['GL_LINEAR_MIPMAP_LINEAR'],
 10240: ['GL_TEXTURE_MAG_FILTER'],
 10241: ['GL_TEXTURE_MIN_FILTER'],
 10242: ['GL_TEXTURE_WRAP_S'],
 10243: ['GL_TEXTURE_WRAP_T'],
 10496: ['GL_CLAMP'],
 10497: ['GL_REPEAT'],
 10752: ['GL_POLYGON_OFFSET_UNITS'],
 10753: ['GL_POLYGON_OFFSET_POINT'],
 10754: ['GL_POLYGON_OFFSET_LINE'],
 10768: ['GL_R3_G3_B2'],
 10784: ['GL_V2F'],
 10785: ['GL_V3F'],
 10786: ['GL_C4UB_V2F'],
 10787: ['GL_C4UB_V3F'],
 10788: ['GL_C3F_V3F'],
 10789: ['GL_N3F_V3F'],
 10790: ['GL_C4F_N3F_V3F'],
 10791: ['GL_T2F_V3F'],
 10792: ['GL_T4F_V4F'],
 10793: ['GL_T2F_C4UB_V3F'],
 10794: ['GL_T2F_C3F_V3F'],
 10795: ['GL_T2F_N3F_V3F'],
 10796: ['GL_T2F_C4F_N3F_V3F'],
 10797: ['GL_T4F_C4F_N3F_V4F'],
 12288: ['GL_CLIP_PLANE0',
         'GL_CLIP_PLANE0_IMG',
         'GL_CLIP_DISTANCE0',
         'GL_CLIP_DISTANCE0_EXT'],
 12289: ['GL_CLIP_PLANE1',
         'GL_CLIP_PLANE1_IMG',
         'GL_CLIP_DISTANCE1',
         'GL_CLIP_DISTANCE1_EXT'],
 12290: ['GL_CLIP_PLANE2',
         'GL_CLIP_PLANE2_IMG',
         'GL_CLIP_DISTANCE2',
         'GL_CLIP_DISTANCE2_EXT'],
 12291: ['GL_CLIP_PLANE3',
         'GL_CLIP_PLANE3_IMG',
         'GL_CLIP_DISTANCE3',
         'GL_CLIP_DISTANCE3_EXT'],
 12292: ['GL_CLIP_PLANE4',
         'GL_CLIP_PLANE4_IMG',
         'GL_CLIP_DISTANCE4',
         'GL_CLIP_DISTANCE4_EXT'],
 12293: ['GL_CLIP_PLANE5',
         'GL_CLIP_PLANE5_IMG',
         'GL_CLIP_DISTANCE5',
         'GL_CLIP_DISTANCE5_EXT'],
 12294: ['GL_CLIP_DISTANCE6', 'GL_CLIP_DISTANCE6_EXT'],
 12295: ['GL_CLIP_DISTANCE7', 'GL_CLIP_DISTANCE7_EXT'],
 16384: ['GL_COLOR_BUFFER_BIT',
         'GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT',
         'GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT_EXT',
         'GL_LIGHT0'],
 16385: ['GL_LIGHT1'],
 16386: ['GL_LIGHT2'],
 16387: ['GL_LIGHT3'],
 16388: ['GL_LIGHT4'],
 16389: ['GL_LIGHT5'],
 16390: ['GL_LIGHT6'],
 16391: ['GL_LIGHT7'],
 32768: ['GL_HINT_BIT', 'GL_QUERY_BUFFER_BARRIER_BIT', 'GL_ABGR_EXT'],
 32769: ['GL_CONSTANT_COLOR', 'GL_CONSTANT_COLOR_EXT'],
 32770: ['GL_ONE_MINUS_CONSTANT_COLOR', 'GL_ONE_MINUS_CONSTANT_COLOR_EXT'],
 32771: ['GL_CONSTANT_ALPHA', 'GL_CONSTANT_ALPHA_EXT'],
 32772: ['GL_ONE_MINUS_CONSTANT_ALPHA', 'GL_ONE_MINUS_CONSTANT_ALPHA_EXT'],
 32773: ['GL_BLEND_COLOR', 'GL_BLEND_COLOR_EXT'],
 32774: ['GL_FUNC_ADD', 'GL_FUNC_ADD_EXT'],
 32775: ['GL_MIN', 'GL_MIN_EXT'],
 32776: ['GL_MAX', 'GL_MAX_EXT'],
 32777: ['GL_BLEND_EQUATION',
         'GL_BLEND_EQUATION_EXT',
         'GL_BLEND_EQUATION_RGB',
         'GL_BLEND_EQUATION_RGB_EXT'],
 32778: ['GL_FUNC_SUBTRACT', 'GL_FUNC_SUBTRACT_EXT'],
 32779: ['GL_FUNC_REVERSE_SUBTRACT', 'GL_FUNC_REVERSE_SUBTRACT_EXT'],
 32780: ['GL_CMYK_EXT'],
 32781: ['GL_CMYKA_EXT'],
 32782: ['GL_PACK_CMYK_HINT_EXT'],
 32783: ['GL_UNPACK_CMYK_HINT_EXT'],
 32784: ['GL_CONVOLUTION_1D', 'GL_CONVOLUTION_1D_EXT'],
 32785: ['GL_CONVOLUTION_2D', 'GL_CONVOLUTION_2D_EXT'],
 32786: ['GL_SEPARABLE_2D', 'GL_SEPARABLE_2D_EXT'],
 32787: ['GL_CONVOLUTION_BORDER_MODE', 'GL_CONVOLUTION_BORDER_MODE_EXT'],
 32788: ['GL_CONVOLUTION_FILTER_SCALE', 'GL_CONVOLUTION_FILTER_SCALE_EXT'],
 32789: ['GL_CONVOLUTION_FILTER_BIAS', 'GL_CONVOLUTION_FILTER_BIAS_EXT'],
 32790: ['GL_REDUCE', 'GL_REDUCE_EXT'],
 32791: ['GL_CONVOLUTION_FORMAT', 'GL_CONVOLUTION_FORMAT_EXT'],
 32792: ['GL_CONVOLUTION_WIDTH', 'GL_CONVOLUTION_WIDTH_EXT'],
 32793: ['GL_CONVOLUTION_HEIGHT', 'GL_CONVOLUTION_HEIGHT_EXT'],
 32794: ['GL_MAX_CONVOLUTION_WIDTH', 'GL_MAX_CONVOLUTION_WIDTH_EXT'],
 32795: ['GL_MAX_CONVOLUTION_HEIGHT', 'GL_MAX_CONVOLUTION_HEIGHT_EXT'],
 32796: ['GL_POST_CONVOLUTION_RED_SCALE', 'GL_POST_CONVOLUTION_RED_SCALE_EXT'],
 32797: ['GL_POST_CONVOLUTION_GREEN_SCALE',
         'GL_POST_CONVOLUTION_GREEN_SCALE_EXT'],
 32798: ['GL_POST_CONVOLUTION_BLUE_SCALE',
         'GL_POST_CONVOLUTION_BLUE_SCALE_EXT'],
 32799: ['GL_POST_CONVOLUTION_ALPHA_SCALE',
         'GL_POST_CONVOLUTION_ALPHA_SCALE_EXT'],
 32800: ['GL_POST_CONVOLUTION_RED_BIAS', 'GL_POST_CONVOLUTION_RED_BIAS_EXT'],
 32801: ['GL_POST_CONVOLUTION_GREEN_BIAS',
         'GL_POST_CONVOLUTION_GREEN_BIAS_EXT'],
 32802: ['GL_POST_CONVOLUTION_BLUE_BIAS', 'GL_POST_CONVOLUTION_BLUE_BIAS_EXT'],
 32803: ['GL_POST_CONVOLUTION_ALPHA_BIAS',
         'GL_POST_CONVOLUTION_ALPHA_BIAS_EXT'],
 32804: ['GL_HISTOGRAM', 'GL_HISTOGRAM_EXT'],
 32805: ['GL_PROXY_HISTOGRAM', 'GL_PROXY_HISTOGRAM_EXT'],
 32806: ['GL_HISTOGRAM_WIDTH', 'GL_HISTOGRAM_WIDTH_EXT'],
 32807: ['GL_HISTOGRAM_FORMAT', 'GL_HISTOGRAM_FORMAT_EXT'],
 32808: ['GL_HISTOGRAM_RED_SIZE', 'GL_HISTOGRAM_RED_SIZE_EXT'],
 32809: ['GL_HISTOGRAM_GREEN_SIZE', 'GL_HISTOGRAM_GREEN_SIZE_EXT'],
 32810: ['GL_HISTOGRAM_BLUE_SIZE', 'GL_HISTOGRAM_BLUE_SIZE_EXT'],
 32811: ['GL_HISTOGRAM_ALPHA_SIZE', 'GL_HISTOGRAM_ALPHA_SIZE_EXT'],
 32812: ['GL_HISTOGRAM_LUMINANCE_SIZE', 'GL_HISTOGRAM_LUMINANCE_SIZE_EXT'],
 32813: ['GL_HISTOGRAM_SINK', 'GL_HISTOGRAM_SINK_EXT'],
 32814: ['GL_MINMAX', 'GL_MINMAX_EXT'],
 32815: ['GL_MINMAX_FORMAT', 'GL_MINMAX_FORMAT_EXT'],
 32816: ['GL_MINMAX_SINK', 'GL_MINMAX_SINK_EXT'],
 32817: ['GL_TABLE_TOO_LARGE_EXT', 'GL_TABLE_TOO_LARGE'],
 32818: ['GL_UNSIGNED_BYTE_3_3_2', 'GL_UNSIGNED_BYTE_3_3_2_EXT'],
 32819: ['GL_UNSIGNED_SHORT_4_4_4_4', 'GL_UNSIGNED_SHORT_4_4_4_4_EXT'],
 32820: ['GL_UNSIGNED_SHORT_5_5_5_1', 'GL_UNSIGNED_SHORT_5_5_5_1_EXT'],
 32821: ['GL_UNSIGNED_INT_8_8_8_8', 'GL_UNSIGNED_INT_8_8_8_8_EXT'],
 32822: ['GL_UNSIGNED_INT_10_10_10_2', 'GL_UNSIGNED_INT_10_10_10_2_EXT'],
 32823: ['GL_POLYGON_OFFSET_EXT', 'GL_POLYGON_OFFSET_FILL'],
 32824: ['GL_POLYGON_OFFSET_FACTOR', 'GL_POLYGON_OFFSET_FACTOR_EXT'],
 32825: ['GL_POLYGON_OFFSET_BIAS_EXT'],
 32826: ['GL_RESCALE_NORMAL', 'GL_RESCALE_NORMAL_EXT'],
 32827: ['GL_ALPHA4', 'GL_ALPHA4_EXT'],
 32828: ['GL_ALPHA8', 'GL_ALPHA8_EXT'],
 32829: ['GL_ALPHA12', 'GL_ALPHA12_EXT'],
 32830: ['GL_ALPHA16', 'GL_ALPHA16_EXT'],
 32831: ['GL_LUMINANCE4', 'GL_LUMINANCE4_EXT'],
 32832: ['GL_LUMINANCE8', 'GL_LUMINANCE8_EXT'],
 32833: ['GL_LUMINANCE12', 'GL_LUMINANCE12_EXT'],
 32834: ['GL_LUMINANCE16', 'GL_LUMINANCE16_EXT'],
 32835: ['GL_LUMINANCE4_ALPHA4', 'GL_LUMINANCE4_ALPHA4_EXT'],
 32836: ['GL_LUMINANCE6_ALPHA2', 'GL_LUMINANCE6_ALPHA2_EXT'],
 32837: ['GL_LUMINANCE8_ALPHA8', 'GL_LUMINANCE8_ALPHA8_EXT'],
 32838: ['GL_LUMINANCE12_ALPHA4', 'GL_LUMINANCE12_ALPHA4_EXT'],
 32839: ['GL_LUMINANCE12_ALPHA12', 'GL_LUMINANCE12_ALPHA12_EXT'],
 32840: ['GL_LUMINANCE16_ALPHA16', 'GL_LUMINANCE16_ALPHA16_EXT'],
 32841: ['GL_INTENSITY', 'GL_INTENSITY_EXT'],
 32842: ['GL_INTENSITY4', 'GL_INTENSITY4_EXT'],
 32843: ['GL_INTENSITY8', 'GL_INTENSITY8_EXT'],
 32844: ['GL_INTENSITY12', 'GL_INTENSITY12_EXT'],
 32845: ['GL_INTENSITY16', 'GL_INTENSITY16_EXT'],
 32846: ['GL_RGB2_EXT'],
 32847: ['GL_RGB4', 'GL_RGB4_EXT'],
 32848: ['GL_RGB5', 'GL_RGB5_EXT'],
 32849: ['GL_RGB8', 'GL_RGB8_EXT'],
 32850: ['GL_RGB10', 'GL_RGB10_EXT'],
 32851: ['GL_RGB12', 'GL_RGB12_EXT'],
 32852: ['GL_RGB16', 'GL_RGB16_EXT'],
 32853: ['GL_RGBA2', 'GL_RGBA2_EXT'],
 32854: ['GL_RGBA4', 'GL_RGBA4_EXT'],
 32855: ['GL_RGB5_A1', 'GL_RGB5_A1_EXT'],
 32856: ['GL_RGBA8', 'GL_RGBA8_EXT'],
 32857: ['GL_RGB10_A2', 'GL_RGB10_A2_EXT'],
 32858: ['GL_RGBA12', 'GL_RGBA12_EXT'],
 32859: ['GL_RGBA16', 'GL_RGBA16_EXT'],
 32860: ['GL_TEXTURE_RED_SIZE', 'GL_TEXTURE_RED_SIZE_EXT'],
 32861: ['GL_TEXTURE_GREEN_SIZE', 'GL_TEXTURE_GREEN_SIZE_EXT'],
 32862: ['GL_TEXTURE_BLUE_SIZE', 'GL_TEXTURE_BLUE_SIZE_EXT'],
 32863: ['GL_TEXTURE_ALPHA_SIZE', 'GL_TEXTURE_ALPHA_SIZE_EXT'],
 32864: ['GL_TEXTURE_LUMINANCE_SIZE', 'GL_TEXTURE_LUMINANCE_SIZE_EXT'],
 32865: ['GL_TEXTURE_INTENSITY_SIZE', 'GL_TEXTURE_INTENSITY_SIZE_EXT'],
 32866: ['GL_REPLACE_EXT'],
 32867: ['GL_PROXY_TEXTURE_1D', 'GL_PROXY_TEXTURE_1D_EXT'],
 32868: ['GL_PROXY_TEXTURE_2D', 'GL_PROXY_TEXTURE_2D_EXT'],
 32869: ['GL_TEXTURE_TOO_LARGE_EXT'],
 32870: ['GL_TEXTURE_PRIORITY', 'GL_TEXTURE_PRIORITY_EXT'],
 32871: ['GL_TEXTURE_RESIDENT', 'GL_TEXTURE_RESIDENT_EXT'],
 32872: ['GL_TEXTURE_1D_BINDING_EXT', 'GL_TEXTURE_BINDING_1D'],
 32873: ['GL_TEXTURE_2D_BINDING_EXT', 'GL_TEXTURE_BINDING_2D'],
 32874: ['GL_TEXTURE_3D_BINDING_EXT', 'GL_TEXTURE_BINDING_3D'],
 32875: ['GL_PACK_SKIP_IMAGES', 'GL_PACK_SKIP_IMAGES_EXT'],
 32876: ['GL_PACK_IMAGE_HEIGHT', 'GL_PACK_IMAGE_HEIGHT_EXT'],
 32877: ['GL_UNPACK_SKIP_IMAGES', 'GL_UNPACK_SKIP_IMAGES_EXT'],
 32878: ['GL_UNPACK_IMAGE_HEIGHT', 'GL_UNPACK_IMAGE_HEIGHT_EXT'],
 32879: ['GL_TEXTURE_3D', 'GL_TEXTURE_3D_EXT'],
 32880: ['GL_PROXY_TEXTURE_3D', 'GL_PROXY_TEXTURE_3D_EXT'],
 32881: ['GL_TEXTURE_DEPTH', 'GL_TEXTURE_DEPTH_EXT'],
 32882: ['GL_TEXTURE_WRAP_R', 'GL_TEXTURE_WRAP_R_EXT'],
 32883: ['GL_MAX_3D_TEXTURE_SIZE', 'GL_MAX_3D_TEXTURE_SIZE_EXT'],
 32884: ['GL_VERTEX_ARRAY', 'GL_VERTEX_ARRAY_EXT'],
 32885: ['GL_NORMAL_ARRAY', 'GL_NORMAL_ARRAY_EXT'],
 32886: ['GL_COLOR_ARRAY', 'GL_COLOR_ARRAY_EXT'],
 32887: ['GL_INDEX_ARRAY', 'GL_INDEX_ARRAY_EXT'],
 32888: ['GL_TEXTURE_COORD_ARRAY', 'GL_TEXTURE_COORD_ARRAY_EXT'],
 32889: ['GL_EDGE_FLAG_ARRAY', 'GL_EDGE_FLAG_ARRAY_EXT'],
 32890: ['GL_VERTEX_ARRAY_SIZE', 'GL_VERTEX_ARRAY_SIZE_EXT'],
 32891: ['GL_VERTEX_ARRAY_TYPE', 'GL_VERTEX_ARRAY_TYPE_EXT'],
 32892: ['GL_VERTEX_ARRAY_STRIDE', 'GL_VERTEX_ARRAY_STRIDE_EXT'],
 32893: ['GL_VERTEX_ARRAY_COUNT_EXT'],
 32894: ['GL_NORMAL_ARRAY_TYPE', 'GL_NORMAL_ARRAY_TYPE_EXT'],
 32895: ['GL_NORMAL_ARRAY_STRIDE', 'GL_NORMAL_ARRAY_STRIDE_EXT'],
 32896: ['GL_NORMAL_ARRAY_COUNT_EXT'],
 32897: ['GL_COLOR_ARRAY_SIZE', 'GL_COLOR_ARRAY_SIZE_EXT'],
 32898: ['GL_COLOR_ARRAY_TYPE', 'GL_COLOR_ARRAY_TYPE_EXT'],
 32899: ['GL_COLOR_ARRAY_STRIDE', 'GL_COLOR_ARRAY_STRIDE_EXT'],
 32900: ['GL_COLOR_ARRAY_COUNT_EXT'],
 32901: ['GL_INDEX_ARRAY_TYPE', 'GL_INDEX_ARRAY_TYPE_EXT'],
 32902: ['GL_INDEX_ARRAY_STRIDE', 'GL_INDEX_ARRAY_STRIDE_EXT'],
 32903: ['GL_INDEX_ARRAY_COUNT_EXT'],
 32904: ['GL_TEXTURE_COORD_ARRAY_SIZE', 'GL_TEXTURE_COORD_ARRAY_SIZE_EXT'],
 32905: ['GL_TEXTURE_COORD_ARRAY_TYPE', 'GL_TEXTURE_COORD_ARRAY_TYPE_EXT'],
 32906: ['GL_TEXTURE_COORD_ARRAY_STRIDE', 'GL_TEXTURE_COORD_ARRAY_STRIDE_EXT'],
 32907: ['GL_TEXTURE_COORD_ARRAY_COUNT_EXT'],
 32908: ['GL_EDGE_FLAG_ARRAY_STRIDE', 'GL_EDGE_FLAG_ARRAY_STRIDE_EXT'],
 32909: ['GL_EDGE_FLAG_ARRAY_COUNT_EXT'],
 32910: ['GL_VERTEX_ARRAY_POINTER', 'GL_VERTEX_ARRAY_POINTER_EXT'],
 32911: ['GL_NORMAL_ARRAY_POINTER', 'GL_NORMAL_ARRAY_POINTER_EXT'],
 32912: ['GL_COLOR_ARRAY_POINTER', 'GL_COLOR_ARRAY_POINTER_EXT'],
 32913: ['GL_INDEX_ARRAY_POINTER', 'GL_INDEX_ARRAY_POINTER_EXT'],
 32914: ['GL_TEXTURE_COORD_ARRAY_POINTER',
         'GL_TEXTURE_COORD_ARRAY_POINTER_EXT'],
 32915: ['GL_EDGE_FLAG_ARRAY_POINTER', 'GL_EDGE_FLAG_ARRAY_POINTER_EXT'],
 32925: ['GL_MULTISAMPLE', 'GL_MULTISAMPLE_ARB', 'GL_MULTISAMPLE_EXT'],
 32926: ['GL_SAMPLE_ALPHA_TO_COVERAGE',
         'GL_SAMPLE_ALPHA_TO_COVERAGE_ARB',
         'GL_SAMPLE_ALPHA_TO_MASK_EXT'],
 32927: ['GL_SAMPLE_ALPHA_TO_ONE',
         'GL_SAMPLE_ALPHA_TO_ONE_ARB',
         'GL_SAMPLE_ALPHA_TO_ONE_EXT'],
 32928: ['GL_SAMPLE_COVERAGE', 'GL_SAMPLE_COVERAGE_ARB', 'GL_SAMPLE_MASK_EXT'],
 32929: ['GL_1PASS_EXT'],
 32930: ['GL_2PASS_0_EXT'],
 32931: ['GL_2PASS_1_EXT'],
 32932: ['GL_4PASS_0_EXT'],
 32933: ['GL_4PASS_1_EXT'],
 32934: ['GL_4PASS_2_EXT'],
 32935: ['GL_4PASS_3_EXT'],
 32936: ['GL_SAMPLE_BUFFERS', 'GL_SAMPLE_BUFFERS_ARB', 'GL_SAMPLE_BUFFERS_EXT'],
 32937: ['GL_SAMPLES', 'GL_SAMPLES_ARB', 'GL_SAMPLES_EXT'],
 32938: ['GL_SAMPLE_COVERAGE_VALUE',
         'GL_SAMPLE_COVERAGE_VALUE_ARB',
         'GL_SAMPLE_MASK_VALUE_EXT'],
 32939: ['GL_SAMPLE_COVERAGE_INVERT',
         'GL_SAMPLE_COVERAGE_INVERT_ARB',
         'GL_SAMPLE_MASK_INVERT_EXT'],
 32940: ['GL_SAMPLE_PATTERN_EXT'],
 32945: ['GL_COLOR_MATRIX'],
 32946: ['GL_COLOR_MATRIX_STACK_DEPTH'],
 32947: ['GL_MAX_COLOR_MATRIX_STACK_DEPTH'],
 32948: ['GL_POST_COLOR_MATRIX_RED_SCALE'],
 32949: ['GL_POST_COLOR_MATRIX_GREEN_SCALE'],
 32950: ['GL_POST_COLOR_MATRIX_BLUE_SCALE'],
 32951: ['GL_POST_COLOR_MATRIX_ALPHA_SCALE'],
 32952: ['GL_POST_COLOR_MATRIX_RED_BIAS'],
 32953: ['GL_POST_COLOR_MATRIX_GREEN_BIAS'],
 32954: ['GL_POST_COLOR_MATRIX_BLUE_BIAS'],
 32955: ['GL_POST_COLOR_MATRIX_ALPHA_BIAS'],
 32959: ['GL_TEXTURE_COMPARE_FAIL_VALUE_ARB'],
 32968: ['GL_BLEND_DST_RGB', 'GL_BLEND_DST_RGB_EXT'],
 32969: ['GL_BLEND_SRC_RGB', 'GL_BLEND_SRC_RGB_EXT'],
 32970: ['GL_BLEND_DST_ALPHA', 'GL_BLEND_DST_ALPHA_EXT'],
 32971: ['GL_BLEND_SRC_ALPHA', 'GL_BLEND_SRC_ALPHA_EXT'],
 32972: ['GL_422_EXT'],
 32973: ['GL_422_REV_EXT'],
 32974: ['GL_422_AVERAGE_EXT'],
 32975: ['GL_422_REV_AVERAGE_EXT'],
 32976: ['GL_COLOR_TABLE'],
 32977: ['GL_POST_CONVOLUTION_COLOR_TABLE'],
 32978: ['GL_POST_COLOR_MATRIX_COLOR_TABLE'],
 32979: ['GL_PROXY_COLOR_TABLE'],
 32980: ['GL_PROXY_POST_CONVOLUTION_COLOR_TABLE'],
 32981: ['GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE'],
 32982: ['GL_COLOR_TABLE_SCALE'],
 32983: ['GL_COLOR_TABLE_BIAS'],
 32984: ['GL_COLOR_TABLE_FORMAT'],
 32985: ['GL_COLOR_TABLE_WIDTH'],
 32986: ['GL_COLOR_TABLE_RED_SIZE'],
 32987: ['GL_COLOR_TABLE_GREEN_SIZE'],
 32988: ['GL_COLOR_TABLE_BLUE_SIZE'],
 32989: ['GL_COLOR_TABLE_ALPHA_SIZE'],
 32990: ['GL_COLOR_TABLE_LUMINANCE_SIZE'],
 32991: ['GL_COLOR_TABLE_INTENSITY_SIZE'],
 32992: ['GL_BGR', 'GL_BGR_EXT'],
 32993: ['GL_BGRA', 'GL_BGRA_EXT', 'GL_BGRA_IMG'],
 32994: ['GL_COLOR_INDEX1_EXT'],
 32995: ['GL_COLOR_INDEX2_EXT'],
 32996: ['GL_COLOR_INDEX4_EXT'],
 32997: ['GL_COLOR_INDEX8_EXT'],
 32998: ['GL_COLOR_INDEX12_EXT'],
 32999: ['GL_COLOR_INDEX16_EXT'],
 33000: ['GL_MAX_ELEMENTS_VERTICES', 'GL_MAX_ELEMENTS_VERTICES_EXT'],
 33001: ['GL_MAX_ELEMENTS_INDICES', 'GL_MAX_ELEMENTS_INDICES_EXT'],
 33002: ['GL_PHONG_WIN'],
 33003: ['GL_PHONG_HINT_WIN'],
 33004: ['GL_FOG_SPECULAR_TEXTURE_WIN'],
 33005: ['GL_TEXTURE_INDEX_SIZE_EXT'],
 33006: ['GL_PARAMETER_BUFFER', 'GL_PARAMETER_BUFFER_ARB'],
 33007: ['GL_PARAMETER_BUFFER_BINDING', 'GL_PARAMETER_BUFFER_BINDING_ARB'],
 33008: ['GL_CLIP_VOLUME_CLIPPING_HINT_EXT'],
 33062: ['GL_POINT_SIZE_MIN', 'GL_POINT_SIZE_MIN_ARB', 'GL_POINT_SIZE_MIN_EXT'],
 33063: ['GL_POINT_SIZE_MAX', 'GL_POINT_SIZE_MAX_ARB', 'GL_POINT_SIZE_MAX_EXT'],
 33064: ['GL_POINT_FADE_THRESHOLD_SIZE',
         'GL_POINT_FADE_THRESHOLD_SIZE_ARB',
         'GL_POINT_FADE_THRESHOLD_SIZE_EXT'],
 33065: ['GL_DISTANCE_ATTENUATION_EXT',
         'GL_POINT_DISTANCE_ATTENUATION',
         'GL_POINT_DISTANCE_ATTENUATION_ARB'],
 33069: ['GL_CLAMP_TO_BORDER',
         'GL_CLAMP_TO_BORDER_ARB',
         'GL_CLAMP_TO_BORDER_EXT'],
 33071: ['GL_CLAMP_TO_EDGE'],
 33082: ['GL_TEXTURE_MIN_LOD'],
 33083: ['GL_TEXTURE_MAX_LOD'],
 33084: ['GL_TEXTURE_BASE_LEVEL'],
 33085: ['GL_TEXTURE_MAX_LEVEL'],
 33104: ['GL_IGNORE_BORDER_HP'],
 33105: ['GL_CONSTANT_BORDER', 'GL_CONSTANT_BORDER_HP'],
 33107: ['GL_REPLICATE_BORDER', 'GL_REPLICATE_BORDER_HP'],
 33108: ['GL_CONVOLUTION_BORDER_COLOR', 'GL_CONVOLUTION_BORDER_COLOR_HP'],
 33109: ['GL_IMAGE_SCALE_X_HP'],
 33110: ['GL_IMAGE_SCALE_Y_HP'],
 33111: ['GL_IMAGE_TRANSLATE_X_HP'],
 33112: ['GL_IMAGE_TRANSLATE_Y_HP'],
 33113: ['GL_IMAGE_ROTATE_ANGLE_HP'],
 33114: ['GL_IMAGE_ROTATE_ORIGIN_X_HP'],
 33115: ['GL_IMAGE_ROTATE_ORIGIN_Y_HP'],
 33116: ['GL_IMAGE_MAG_FILTER_HP'],
 33117: ['GL_IMAGE_MIN_FILTER_HP'],
 33118: ['GL_IMAGE_CUBIC_WEIGHT_HP'],
 33119: ['GL_CUBIC_HP'],
 33120: ['GL_AVERAGE_HP'],
 33121: ['GL_IMAGE_TRANSFORM_2D_HP'],
 33122: ['GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP'],
 33123: ['GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP'],
 33125: ['GL_OCCLUSION_TEST_HP'],
 33126: ['GL_OCCLUSION_TEST_RESULT_HP'],
 33127: ['GL_TEXTURE_LIGHTING_MODE_HP'],
 33128: ['GL_TEXTURE_POST_SPECULAR_HP'],
 33129: ['GL_TEXTURE_PRE_SPECULAR_HP'],
 33169: ['GL_GENERATE_MIPMAP'],
 33170: ['GL_GENERATE_MIPMAP_HINT'],
 33189: ['GL_DEPTH_COMPONENT16', 'GL_DEPTH_COMPONENT16_ARB'],
 33190: ['GL_DEPTH_COMPONENT24', 'GL_DEPTH_COMPONENT24_ARB'],
 33191: ['GL_DEPTH_COMPONENT32', 'GL_DEPTH_COMPONENT32_ARB'],
 33192: ['GL_ARRAY_ELEMENT_LOCK_FIRST_EXT'],
 33193: ['GL_ARRAY_ELEMENT_LOCK_COUNT_EXT'],
 33194: ['GL_CULL_VERTEX_EXT'],
 33195: ['GL_CULL_VERTEX_EYE_POSITION_EXT'],
 33196: ['GL_CULL_VERTEX_OBJECT_POSITION_EXT'],
 33197: ['GL_IUI_V2F_EXT'],
 33198: ['GL_IUI_V3F_EXT'],
 33199: ['GL_IUI_N3F_V2F_EXT'],
 33200: ['GL_IUI_N3F_V3F_EXT'],
 33201: ['GL_T2F_IUI_V2F_EXT'],
 33202: ['GL_T2F_IUI_V3F_EXT'],
 33203: ['GL_T2F_IUI_N3F_V2F_EXT'],
 33204: ['GL_T2F_IUI_N3F_V3F_EXT'],
 33205: ['GL_INDEX_TEST_EXT'],
 33206: ['GL_INDEX_TEST_FUNC_EXT'],
 33207: ['GL_INDEX_TEST_REF_EXT'],
 33208: ['GL_INDEX_MATERIAL_EXT'],
 33209: ['GL_INDEX_MATERIAL_PARAMETER_EXT'],
 33210: ['GL_INDEX_MATERIAL_FACE_EXT'],
 33237: ['GL_UNPACK_CONSTANT_DATA_SUNX'],
 33238: ['GL_TEXTURE_CONSTANT_DATA_SUNX'],
 33272: ['GL_LIGHT_MODEL_COLOR_CONTROL', 'GL_LIGHT_MODEL_COLOR_CONTROL_EXT'],
 33273: ['GL_SINGLE_COLOR', 'GL_SINGLE_COLOR_EXT'],
 33274: ['GL_SEPARATE_SPECULAR_COLOR', 'GL_SEPARATE_SPECULAR_COLOR_EXT'],
 33275: ['GL_SHARED_TEXTURE_PALETTE_EXT'],
 33296: ['GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING',
         'GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT'],
 33297: ['GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE',
         'GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT'],
 33298: ['GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE'],
 33299: ['GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE'],
 33300: ['GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE'],
 33301: ['GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE'],
 33302: ['GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE'],
 33303: ['GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE'],
 33304: ['GL_FRAMEBUFFER_DEFAULT'],
 33305: ['GL_FRAMEBUFFER_UNDEFINED'],
 33306: ['GL_DEPTH_STENCIL_ATTACHMENT'],
 33307: ['GL_MAJOR_VERSION'],
 33308: ['GL_MINOR_VERSION'],
 33309: ['GL_NUM_EXTENSIONS'],
 33310: ['GL_CONTEXT_FLAGS'],
 33311: ['GL_BUFFER_IMMUTABLE_STORAGE', 'GL_BUFFER_IMMUTABLE_STORAGE_EXT'],
 33312: ['GL_BUFFER_STORAGE_FLAGS', 'GL_BUFFER_STORAGE_FLAGS_EXT'],
 33313: ['GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED'],
 33314: ['GL_INDEX'],
 33317: ['GL_COMPRESSED_RED'],
 33318: ['GL_COMPRESSED_RG'],
 33319: ['GL_RG', 'GL_RG_EXT'],
 33320: ['GL_RG_INTEGER'],
 33321: ['GL_R8', 'GL_R8_EXT'],
 33322: ['GL_R16', 'GL_R16_EXT'],
 33323: ['GL_RG8', 'GL_RG8_EXT'],
 33324: ['GL_RG16', 'GL_RG16_EXT'],
 33325: ['GL_R16F', 'GL_R16F_EXT'],
 33326: ['GL_R32F', 'GL_R32F_EXT'],
 33327: ['GL_RG16F', 'GL_RG16F_EXT'],
 33328: ['GL_RG32F', 'GL_RG32F_EXT'],
 33329: ['GL_R8I'],
 33330: ['GL_R8UI'],
 33331: ['GL_R16I'],
 33332: ['GL_R16UI'],
 33333: ['GL_R32I'],
 33334: ['GL_R32UI'],
 33335: ['GL_RG8I'],
 33336: ['GL_RG8UI'],
 33337: ['GL_RG16I'],
 33338: ['GL_RG16UI'],
 33339: ['GL_RG32I'],
 33340: ['GL_RG32UI'],
 33344: ['GL_SYNC_CL_EVENT_ARB'],
 33345: ['GL_SYNC_CL_EVENT_COMPLETE_ARB'],
 33346: ['GL_DEBUG_OUTPUT_SYNCHRONOUS', 'GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB'],
 33347: ['GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH',
         'GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB'],
 33348: ['GL_DEBUG_CALLBACK_FUNCTION', 'GL_DEBUG_CALLBACK_FUNCTION_ARB'],
 33349: ['GL_DEBUG_CALLBACK_USER_PARAM', 'GL_DEBUG_CALLBACK_USER_PARAM_ARB'],
 33350: ['GL_DEBUG_SOURCE_API', 'GL_DEBUG_SOURCE_API_ARB'],
 33351: ['GL_DEBUG_SOURCE_WINDOW_SYSTEM', 'GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB'],
 33352: ['GL_DEBUG_SOURCE_SHADER_COMPILER',
         'GL_DEBUG_SOURCE_SHADER_COMPILER_ARB'],
 33353: ['GL_DEBUG_SOURCE_THIRD_PARTY', 'GL_DEBUG_SOURCE_THIRD_PARTY_ARB'],
 33354: ['GL_DEBUG_SOURCE_APPLICATION', 'GL_DEBUG_SOURCE_APPLICATION_ARB'],
 33355: ['GL_DEBUG_SOURCE_OTHER', 'GL_DEBUG_SOURCE_OTHER_ARB'],
 33356: ['GL_DEBUG_TYPE_ERROR', 'GL_DEBUG_TYPE_ERROR_ARB'],
 33357: ['GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR',
         'GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB'],
 33358: ['GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR',
         'GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB'],
 33359: ['GL_DEBUG_TYPE_PORTABILITY', 'GL_DEBUG_TYPE_PORTABILITY_ARB'],
 33360: ['GL_DEBUG_TYPE_PERFORMANCE', 'GL_DEBUG_TYPE_PERFORMANCE_ARB'],
 33361: ['GL_DEBUG_TYPE_OTHER', 'GL_DEBUG_TYPE_OTHER_ARB'],
 33362: ['GL_LOSE_CONTEXT_ON_RESET',
         'GL_LOSE_CONTEXT_ON_RESET_ARB',
         'GL_LOSE_CONTEXT_ON_RESET_EXT'],
 33363: ['GL_GUILTY_CONTEXT_RESET',
         'GL_GUILTY_CONTEXT_RESET_ARB',
         'GL_GUILTY_CONTEXT_RESET_EXT'],
 33364: ['GL_INNOCENT_CONTEXT_RESET',
         'GL_INNOCENT_CONTEXT_RESET_ARB',
         'GL_INNOCENT_CONTEXT_RESET_EXT'],
 33365: ['GL_UNKNOWN_CONTEXT_RESET',
         'GL_UNKNOWN_CONTEXT_RESET_ARB',
         'GL_UNKNOWN_CONTEXT_RESET_EXT'],
 33366: ['GL_RESET_NOTIFICATION_STRATEGY',
         'GL_RESET_NOTIFICATION_STRATEGY_ARB',
         'GL_RESET_NOTIFICATION_STRATEGY_EXT'],
 33367: ['GL_PROGRAM_BINARY_RETRIEVABLE_HINT'],
 33368: ['GL_PROGRAM_SEPARABLE', 'GL_PROGRAM_SEPARABLE_EXT'],
 33369: ['GL_ACTIVE_PROGRAM', 'GL_ACTIVE_PROGRAM_EXT'],
 33370: ['GL_PROGRAM_PIPELINE_BINDING', 'GL_PROGRAM_PIPELINE_BINDING_EXT'],
 33371: ['GL_MAX_VIEWPORTS'],
 33372: ['GL_VIEWPORT_SUBPIXEL_BITS', 'GL_VIEWPORT_SUBPIXEL_BITS_EXT'],
 33373: ['GL_VIEWPORT_BOUNDS_RANGE', 'GL_VIEWPORT_BOUNDS_RANGE_EXT'],
 33374: ['GL_LAYER_PROVOKING_VERTEX', 'GL_LAYER_PROVOKING_VERTEX_EXT'],
 33375: ['GL_VIEWPORT_INDEX_PROVOKING_VERTEX',
         'GL_VIEWPORT_INDEX_PROVOKING_VERTEX_EXT'],
 33376: ['GL_UNDEFINED_VERTEX', 'GL_UNDEFINED_VERTEX_EXT'],
 33377: ['GL_NO_RESET_NOTIFICATION',
         'GL_NO_RESET_NOTIFICATION_ARB',
         'GL_NO_RESET_NOTIFICATION_EXT'],
 33378: ['GL_MAX_COMPUTE_SHARED_MEMORY_SIZE'],
 33379: ['GL_MAX_COMPUTE_UNIFORM_COMPONENTS'],
 33380: ['GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS'],
 33381: ['GL_MAX_COMPUTE_ATOMIC_COUNTERS'],
 33382: ['GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS'],
 33383: ['GL_COMPUTE_WORK_GROUP_SIZE'],
 33384: ['GL_DEBUG_TYPE_MARKER'],
 33385: ['GL_DEBUG_TYPE_PUSH_GROUP'],
 33386: ['GL_DEBUG_TYPE_POP_GROUP'],
 33387: ['GL_DEBUG_SEVERITY_NOTIFICATION'],
 33388: ['GL_MAX_DEBUG_GROUP_STACK_DEPTH'],
 33389: ['GL_DEBUG_GROUP_STACK_DEPTH'],
 33390: ['GL_MAX_UNIFORM_LOCATIONS'],
 33391: ['GL_INTERNALFORMAT_SUPPORTED'],
 33392: ['GL_INTERNALFORMAT_PREFERRED'],
 33393: ['GL_INTERNALFORMAT_RED_SIZE'],
 33394: ['GL_INTERNALFORMAT_GREEN_SIZE'],
 33395: ['GL_INTERNALFORMAT_BLUE_SIZE'],
 33396: ['GL_INTERNALFORMAT_ALPHA_SIZE'],
 33397: ['GL_INTERNALFORMAT_DEPTH_SIZE'],
 33398: ['GL_INTERNALFORMAT_STENCIL_SIZE'],
 33399: ['GL_INTERNALFORMAT_SHARED_SIZE'],
 33400: ['GL_INTERNALFORMAT_RED_TYPE'],
 33401: ['GL_INTERNALFORMAT_GREEN_TYPE'],
 33402: ['GL_INTERNALFORMAT_BLUE_TYPE'],
 33403: ['GL_INTERNALFORMAT_ALPHA_TYPE'],
 33404: ['GL_INTERNALFORMAT_DEPTH_TYPE'],
 33405: ['GL_INTERNALFORMAT_STENCIL_TYPE'],
 33406: ['GL_MAX_WIDTH'],
 33407: ['GL_MAX_HEIGHT'],
 33408: ['GL_MAX_DEPTH'],
 33409: ['GL_MAX_LAYERS'],
 33410: ['GL_MAX_COMBINED_DIMENSIONS'],
 33411: ['GL_COLOR_COMPONENTS'],
 33412: ['GL_DEPTH_COMPONENTS'],
 33413: ['GL_STENCIL_COMPONENTS'],
 33414: ['GL_COLOR_RENDERABLE'],
 33415: ['GL_DEPTH_RENDERABLE'],
 33416: ['GL_STENCIL_RENDERABLE'],
 33417: ['GL_FRAMEBUFFER_RENDERABLE'],
 33418: ['GL_FRAMEBUFFER_RENDERABLE_LAYERED'],
 33419: ['GL_FRAMEBUFFER_BLEND'],
 33420: ['GL_READ_PIXELS'],
 33421: ['GL_READ_PIXELS_FORMAT'],
 33422: ['GL_READ_PIXELS_TYPE'],
 33423: ['GL_TEXTURE_IMAGE_FORMAT'],
 33424: ['GL_TEXTURE_IMAGE_TYPE'],
 33425: ['GL_GET_TEXTURE_IMAGE_FORMAT'],
 33426: ['GL_GET_TEXTURE_IMAGE_TYPE'],
 33427: ['GL_MIPMAP'],
 33428: ['GL_MANUAL_GENERATE_MIPMAP'],
 33429: ['GL_AUTO_GENERATE_MIPMAP'],
 33430: ['GL_COLOR_ENCODING'],
 33431: ['GL_SRGB_READ'],
 33432: ['GL_SRGB_WRITE'],
 33433: ['GL_SRGB_DECODE_ARB'],
 33434: ['GL_FILTER'],
 33435: ['GL_VERTEX_TEXTURE'],
 33436: ['GL_TESS_CONTROL_TEXTURE'],
 33437: ['GL_TESS_EVALUATION_TEXTURE'],
 33438: ['GL_GEOMETRY_TEXTURE'],
 33439: ['GL_FRAGMENT_TEXTURE'],
 33440: ['GL_COMPUTE_TEXTURE'],
 33441: ['GL_TEXTURE_SHADOW'],
 33442: ['GL_TEXTURE_GATHER'],
 33443: ['GL_TEXTURE_GATHER_SHADOW'],
 33444: ['GL_SHADER_IMAGE_LOAD'],
 33445: ['GL_SHADER_IMAGE_STORE'],
 33446: ['GL_SHADER_IMAGE_ATOMIC'],
 33447: ['GL_IMAGE_TEXEL_SIZE'],
 33448: ['GL_IMAGE_COMPATIBILITY_CLASS'],
 33449: ['GL_IMAGE_PIXEL_FORMAT'],
 33450: ['GL_IMAGE_PIXEL_TYPE'],
 33452: ['GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST'],
 33453: ['GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST'],
 33454: ['GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE'],
 33455: ['GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE'],
 33457: ['GL_TEXTURE_COMPRESSED_BLOCK_WIDTH'],
 33458: ['GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT'],
 33459: ['GL_TEXTURE_COMPRESSED_BLOCK_SIZE'],
 33460: ['GL_CLEAR_BUFFER'],
 33461: ['GL_TEXTURE_VIEW'],
 33462: ['GL_VIEW_COMPATIBILITY_CLASS'],
 33463: ['GL_FULL_SUPPORT'],
 33464: ['GL_CAVEAT_SUPPORT'],
 33465: ['GL_IMAGE_CLASS_4_X_32'],
 33466: ['GL_IMAGE_CLASS_2_X_32'],
 33467: ['GL_IMAGE_CLASS_1_X_32'],
 33468: ['GL_IMAGE_CLASS_4_X_16'],
 33469: ['GL_IMAGE_CLASS_2_X_16'],
 33470: ['GL_IMAGE_CLASS_1_X_16'],
 33471: ['GL_IMAGE_CLASS_4_X_8'],
 33472: ['GL_IMAGE_CLASS_2_X_8'],
 33473: ['GL_IMAGE_CLASS_1_X_8'],
 33474: ['GL_IMAGE_CLASS_11_11_10'],
 33475: ['GL_IMAGE_CLASS_10_10_10_2'],
 33476: ['GL_VIEW_CLASS_128_BITS'],
 33477: ['GL_VIEW_CLASS_96_BITS'],
 33478: ['GL_VIEW_CLASS_64_BITS'],
 33479: ['GL_VIEW_CLASS_48_BITS'],
 33480: ['GL_VIEW_CLASS_32_BITS'],
 33481: ['GL_VIEW_CLASS_24_BITS'],
 33482: ['GL_VIEW_CLASS_16_BITS'],
 33483: ['GL_VIEW_CLASS_8_BITS'],
 33484: ['GL_VIEW_CLASS_S3TC_DXT1_RGB'],
 33485: ['GL_VIEW_CLASS_S3TC_DXT1_RGBA'],
 33486: ['GL_VIEW_CLASS_S3TC_DXT3_RGBA'],
 33487: ['GL_VIEW_CLASS_S3TC_DXT5_RGBA'],
 33488: ['GL_VIEW_CLASS_RGTC1_RED'],
 33489: ['GL_VIEW_CLASS_RGTC2_RG'],
 33490: ['GL_VIEW_CLASS_BPTC_UNORM'],
 33491: ['GL_VIEW_CLASS_BPTC_FLOAT'],
 33492: ['GL_VERTEX_ATTRIB_BINDING'],
 33493: ['GL_VERTEX_ATTRIB_RELATIVE_OFFSET'],
 33494: ['GL_VERTEX_BINDING_DIVISOR'],
 33495: ['GL_VERTEX_BINDING_OFFSET'],
 33496: ['GL_VERTEX_BINDING_STRIDE'],
 33497: ['GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET'],
 33498: ['GL_MAX_VERTEX_ATTRIB_BINDINGS'],
 33499: ['GL_TEXTURE_VIEW_MIN_LEVEL', 'GL_TEXTURE_VIEW_MIN_LEVEL_EXT'],
 33500: ['GL_TEXTURE_VIEW_NUM_LEVELS', 'GL_TEXTURE_VIEW_NUM_LEVELS_EXT'],
 33501: ['GL_TEXTURE_VIEW_MIN_LAYER', 'GL_TEXTURE_VIEW_MIN_LAYER_EXT'],
 33502: ['GL_TEXTURE_VIEW_NUM_LAYERS', 'GL_TEXTURE_VIEW_NUM_LAYERS_EXT'],
 33503: ['GL_TEXTURE_IMMUTABLE_LEVELS'],
 33504: ['GL_BUFFER'],
 33505: ['GL_SHADER'],
 33506: ['GL_PROGRAM'],
 33507: ['GL_QUERY'],
 33508: ['GL_PROGRAM_PIPELINE'],
 33509: ['GL_MAX_VERTEX_ATTRIB_STRIDE'],
 33510: ['GL_SAMPLER'],
 33511: ['GL_DISPLAY_LIST'],
 33512: ['GL_MAX_LABEL_LENGTH'],
 33513: ['GL_NUM_SHADING_LANGUAGE_VERSIONS'],
 33514: ['GL_QUERY_TARGET'],
 33516: ['GL_TRANSFORM_FEEDBACK_OVERFLOW',
         'GL_TRANSFORM_FEEDBACK_OVERFLOW_ARB'],
 33517: ['GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW',
         'GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW_ARB'],
 33518: ['GL_VERTICES_SUBMITTED', 'GL_VERTICES_SUBMITTED_ARB'],
 33519: ['GL_PRIMITIVES_SUBMITTED', 'GL_PRIMITIVES_SUBMITTED_ARB'],
 33520: ['GL_VERTEX_SHADER_INVOCATIONS', 'GL_VERTEX_SHADER_INVOCATIONS_ARB'],
 33521: ['GL_TESS_CONTROL_SHADER_PATCHES',
         'GL_TESS_CONTROL_SHADER_PATCHES_ARB'],
 33522: ['GL_TESS_EVALUATION_SHADER_INVOCATIONS',
         'GL_TESS_EVALUATION_SHADER_INVOCATIONS_ARB'],
 33523: ['GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED',
         'GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED_ARB'],
 33524: ['GL_FRAGMENT_SHADER_INVOCATIONS',
         'GL_FRAGMENT_SHADER_INVOCATIONS_ARB'],
 33525: ['GL_COMPUTE_SHADER_INVOCATIONS', 'GL_COMPUTE_SHADER_INVOCATIONS_ARB'],
 33526: ['GL_CLIPPING_INPUT_PRIMITIVES', 'GL_CLIPPING_INPUT_PRIMITIVES_ARB'],
 33527: ['GL_CLIPPING_OUTPUT_PRIMITIVES', 'GL_CLIPPING_OUTPUT_PRIMITIVES_ARB'],
 33528: ['GL_SPARSE_BUFFER_PAGE_SIZE_ARB'],
 33529: ['GL_MAX_CULL_DISTANCES', 'GL_MAX_CULL_DISTANCES_EXT'],
 33530: ['GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES',
         'GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES_EXT'],
 33531: ['GL_CONTEXT_RELEASE_BEHAVIOR'],
 33532: ['GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH'],
 33584: ['GL_PIXEL_TRANSFORM_2D_EXT'],
 33585: ['GL_PIXEL_MAG_FILTER_EXT'],
 33586: ['GL_PIXEL_MIN_FILTER_EXT'],
 33587: ['GL_PIXEL_CUBIC_WEIGHT_EXT'],
 33588: ['GL_CUBIC_EXT'],
 33589: ['GL_AVERAGE_EXT'],
 33590: ['GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT'],
 33591: ['GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT'],
 33592: ['GL_PIXEL_TRANSFORM_2D_MATRIX_EXT'],
 33609: ['GL_FRAGMENT_MATERIAL_EXT'],
 33610: ['GL_FRAGMENT_NORMAL_EXT'],
 33612: ['GL_FRAGMENT_COLOR_EXT'],
 33613: ['GL_ATTENUATION_EXT'],
 33614: ['GL_SHADOW_ATTENUATION_EXT'],
 33615: ['GL_TEXTURE_APPLICATION_MODE_EXT'],
 33616: ['GL_TEXTURE_LIGHT_EXT'],
 33617: ['GL_TEXTURE_MATERIAL_FACE_EXT'],
 33618: ['GL_TEXTURE_MATERIAL_PARAMETER_EXT'],
 33634: ['GL_UNSIGNED_BYTE_2_3_3_REV', 'GL_UNSIGNED_BYTE_2_3_3_REV_EXT'],
 33635: ['GL_UNSIGNED_SHORT_5_6_5', 'GL_UNSIGNED_SHORT_5_6_5_EXT'],
 33636: ['GL_UNSIGNED_SHORT_5_6_5_REV', 'GL_UNSIGNED_SHORT_5_6_5_REV_EXT'],
 33637: ['GL_UNSIGNED_SHORT_4_4_4_4_REV',
         'GL_UNSIGNED_SHORT_4_4_4_4_REV_EXT',
         'GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG'],
 33638: ['GL_UNSIGNED_SHORT_1_5_5_5_REV', 'GL_UNSIGNED_SHORT_1_5_5_5_REV_EXT'],
 33639: ['GL_UNSIGNED_INT_8_8_8_8_REV', 'GL_UNSIGNED_INT_8_8_8_8_REV_EXT'],
 33640: ['GL_UNSIGNED_INT_2_10_10_10_REV',
         'GL_UNSIGNED_INT_2_10_10_10_REV_EXT'],
 33648: ['GL_MIRRORED_REPEAT', 'GL_MIRRORED_REPEAT_ARB'],
 33696: ['GL_RGB_S3TC'],
 33697: ['GL_RGB4_S3TC'],
 33698: ['GL_RGBA_S3TC'],
 33699: ['GL_RGBA4_S3TC'],
 33700: ['GL_RGBA_DXT5_S3TC'],
 33701: ['GL_RGBA4_DXT5_S3TC'],
 33776: ['GL_COMPRESSED_RGB_S3TC_DXT1_EXT'],
 33777: ['GL_COMPRESSED_RGBA_S3TC_DXT1_EXT'],
 33778: ['GL_COMPRESSED_RGBA_S3TC_DXT3_ANGLE',
         'GL_COMPRESSED_RGBA_S3TC_DXT3_EXT'],
 33779: ['GL_COMPRESSED_RGBA_S3TC_DXT5_ANGLE',
         'GL_COMPRESSED_RGBA_S3TC_DXT5_EXT'],
 33849: ['GL_TANGENT_ARRAY_EXT'],
 33850: ['GL_BINORMAL_ARRAY_EXT'],
 33851: ['GL_CURRENT_TANGENT_EXT'],
 33852: ['GL_CURRENT_BINORMAL_EXT'],
 33854: ['GL_TANGENT_ARRAY_TYPE_EXT'],
 33855: ['GL_TANGENT_ARRAY_STRIDE_EXT'],
 33856: ['GL_BINORMAL_ARRAY_TYPE_EXT'],
 33857: ['GL_BINORMAL_ARRAY_STRIDE_EXT'],
 33858: ['GL_TANGENT_ARRAY_POINTER_EXT'],
 33859: ['GL_BINORMAL_ARRAY_POINTER_EXT'],
 33860: ['GL_MAP1_TANGENT_EXT'],
 33861: ['GL_MAP2_TANGENT_EXT'],
 33862: ['GL_MAP1_BINORMAL_EXT'],
 33863: ['GL_MAP2_BINORMAL_EXT'],
 33872: ['GL_FOG_COORDINATE_SOURCE',
         'GL_FOG_COORDINATE_SOURCE_EXT',
         'GL_FOG_COORD_SRC'],
 33873: ['GL_FOG_COORDINATE', 'GL_FOG_COORD', 'GL_FOG_COORDINATE_EXT'],
 33874: ['GL_FRAGMENT_DEPTH', 'GL_FRAGMENT_DEPTH_EXT'],
 33875: ['GL_CURRENT_FOG_COORDINATE',
         'GL_CURRENT_FOG_COORD',
         'GL_CURRENT_FOG_COORDINATE_EXT'],
 33876: ['GL_FOG_COORDINATE_ARRAY_TYPE',
         'GL_FOG_COORDINATE_ARRAY_TYPE_EXT',
         'GL_FOG_COORD_ARRAY_TYPE'],
 33877: ['GL_FOG_COORDINATE_ARRAY_STRIDE',
         'GL_FOG_COORDINATE_ARRAY_STRIDE_EXT',
         'GL_FOG_COORD_ARRAY_STRIDE'],
 33878: ['GL_FOG_COORDINATE_ARRAY_POINTER',
         'GL_FOG_COORDINATE_ARRAY_POINTER_EXT',
         'GL_FOG_COORD_ARRAY_POINTER'],
 33879: ['GL_FOG_COORDINATE_ARRAY',
         'GL_FOG_COORDINATE_ARRAY_EXT',
         'GL_FOG_COORD_ARRAY'],
 33880: ['GL_COLOR_SUM', 'GL_COLOR_SUM_ARB', 'GL_COLOR_SUM_EXT'],
 33881: ['GL_CURRENT_SECONDARY_COLOR', 'GL_CURRENT_SECONDARY_COLOR_EXT'],
 33882: ['GL_SECONDARY_COLOR_ARRAY_SIZE', 'GL_SECONDARY_COLOR_ARRAY_SIZE_EXT'],
 33883: ['GL_SECONDARY_COLOR_ARRAY_TYPE', 'GL_SECONDARY_COLOR_ARRAY_TYPE_EXT'],
 33884: ['GL_SECONDARY_COLOR_ARRAY_STRIDE',
         'GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT'],
 33885: ['GL_SECONDARY_COLOR_ARRAY_POINTER',
         'GL_SECONDARY_COLOR_ARRAY_POINTER_EXT'],
 33886: ['GL_SECONDARY_COLOR_ARRAY', 'GL_SECONDARY_COLOR_ARRAY_EXT'],
 33887: ['GL_CURRENT_RASTER_SECONDARY_COLOR'],
 33901: ['GL_ALIASED_POINT_SIZE_RANGE'],
 33902: ['GL_ALIASED_LINE_WIDTH_RANGE'],
 33936: ['GL_SCREEN_COORDINATES_REND'],
 33937: ['GL_INVERTED_SCREEN_W_REND'],
 33984: ['GL_TEXTURE0', 'GL_TEXTURE0_ARB'],
 33985: ['GL_TEXTURE1', 'GL_TEXTURE1_ARB'],
 33986: ['GL_TEXTURE2', 'GL_TEXTURE2_ARB'],
 33987: ['GL_TEXTURE3', 'GL_TEXTURE3_ARB'],
 33988: ['GL_TEXTURE4', 'GL_TEXTURE4_ARB'],
 33989: ['GL_TEXTURE5', 'GL_TEXTURE5_ARB'],
 33990: ['GL_TEXTURE6', 'GL_TEXTURE6_ARB'],
 33991: ['GL_TEXTURE7', 'GL_TEXTURE7_ARB'],
 33992: ['GL_TEXTURE8', 'GL_TEXTURE8_ARB'],
 33993: ['GL_TEXTURE9', 'GL_TEXTURE9_ARB'],
 33994: ['GL_TEXTURE10', 'GL_TEXTURE10_ARB'],
 33995: ['GL_TEXTURE11', 'GL_TEXTURE11_ARB'],
 33996: ['GL_TEXTURE12', 'GL_TEXTURE12_ARB'],
 33997: ['GL_TEXTURE13', 'GL_TEXTURE13_ARB'],
 33998: ['GL_TEXTURE14', 'GL_TEXTURE14_ARB'],
 33999: ['GL_TEXTURE15', 'GL_TEXTURE15_ARB'],
 34000: ['GL_TEXTURE16', 'GL_TEXTURE16_ARB'],
 34001: ['GL_TEXTURE17', 'GL_TEXTURE17_ARB'],
 34002: ['GL_TEXTURE18', 'GL_TEXTURE18_ARB'],
 34003: ['GL_TEXTURE19', 'GL_TEXTURE19_ARB'],
 34004: ['GL_TEXTURE20', 'GL_TEXTURE20_ARB'],
 34005: ['GL_TEXTURE21', 'GL_TEXTURE21_ARB'],
 34006: ['GL_TEXTURE22', 'GL_TEXTURE22_ARB'],
 34007: ['GL_TEXTURE23', 'GL_TEXTURE23_ARB'],
 34008: ['GL_TEXTURE24', 'GL_TEXTURE24_ARB'],
 34009: ['GL_TEXTURE25', 'GL_TEXTURE25_ARB'],
 34010: ['GL_TEXTURE26', 'GL_TEXTURE26_ARB'],
 34011: ['GL_TEXTURE27', 'GL_TEXTURE27_ARB'],
 34012: ['GL_TEXTURE28', 'GL_TEXTURE28_ARB'],
 34013: ['GL_TEXTURE29', 'GL_TEXTURE29_ARB'],
 34014: ['GL_TEXTURE30', 'GL_TEXTURE30_ARB'],
 34015: ['GL_TEXTURE31', 'GL_TEXTURE31_ARB'],
 34016: ['GL_ACTIVE_TEXTURE', 'GL_ACTIVE_TEXTURE_ARB'],
 34017: ['GL_CLIENT_ACTIVE_TEXTURE', 'GL_CLIENT_ACTIVE_TEXTURE_ARB'],
 34018: ['GL_MAX_TEXTURE_UNITS', 'GL_MAX_TEXTURE_UNITS_ARB'],
 34019: ['GL_TRANSPOSE_MODELVIEW_MATRIX', 'GL_TRANSPOSE_MODELVIEW_MATRIX_ARB'],
 34020: ['GL_TRANSPOSE_PROJECTION_MATRIX',
         'GL_TRANSPOSE_PROJECTION_MATRIX_ARB'],
 34021: ['GL_TRANSPOSE_TEXTURE_MATRIX', 'GL_TRANSPOSE_TEXTURE_MATRIX_ARB'],
 34022: ['GL_TRANSPOSE_COLOR_MATRIX', 'GL_TRANSPOSE_COLOR_MATRIX_ARB'],
 34023: ['GL_SUBTRACT', 'GL_SUBTRACT_ARB'],
 34024: ['GL_MAX_RENDERBUFFER_SIZE', 'GL_MAX_RENDERBUFFER_SIZE_EXT'],
 34025: ['GL_COMPRESSED_ALPHA', 'GL_COMPRESSED_ALPHA_ARB'],
 34026: ['GL_COMPRESSED_LUMINANCE', 'GL_COMPRESSED_LUMINANCE_ARB'],
 34027: ['GL_COMPRESSED_LUMINANCE_ALPHA', 'GL_COMPRESSED_LUMINANCE_ALPHA_ARB'],
 34028: ['GL_COMPRESSED_INTENSITY', 'GL_COMPRESSED_INTENSITY_ARB'],
 34029: ['GL_COMPRESSED_RGB', 'GL_COMPRESSED_RGB_ARB'],
 34030: ['GL_COMPRESSED_RGBA', 'GL_COMPRESSED_RGBA_ARB'],
 34031: ['GL_TEXTURE_COMPRESSION_HINT', 'GL_TEXTURE_COMPRESSION_HINT_ARB'],
 34032: ['GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER'],
 34033: ['GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER'],
 34037: ['GL_TEXTURE_RECTANGLE', 'GL_TEXTURE_RECTANGLE_ARB'],
 34038: ['GL_TEXTURE_BINDING_RECTANGLE', 'GL_TEXTURE_BINDING_RECTANGLE_ARB'],
 34039: ['GL_PROXY_TEXTURE_RECTANGLE', 'GL_PROXY_TEXTURE_RECTANGLE_ARB'],
 34040: ['GL_MAX_RECTANGLE_TEXTURE_SIZE', 'GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB'],
 34041: ['GL_DEPTH_STENCIL', 'GL_DEPTH_STENCIL_EXT'],
 34042: ['GL_UNSIGNED_INT_24_8', 'GL_UNSIGNED_INT_24_8_EXT'],
 34045: ['GL_MAX_TEXTURE_LOD_BIAS', 'GL_MAX_TEXTURE_LOD_BIAS_EXT'],
 34046: ['GL_TEXTURE_MAX_ANISOTROPY', 'GL_TEXTURE_MAX_ANISOTROPY_EXT'],
 34047: ['GL_MAX_TEXTURE_MAX_ANISOTROPY', 'GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT'],
 34048: ['GL_TEXTURE_FILTER_CONTROL', 'GL_TEXTURE_FILTER_CONTROL_EXT'],
 34049: ['GL_TEXTURE_LOD_BIAS', 'GL_TEXTURE_LOD_BIAS_EXT'],
 34050: ['GL_MODELVIEW1_STACK_DEPTH_EXT'],
 34054: ['GL_MODELVIEW1_MATRIX_EXT'],
 34055: ['GL_INCR_WRAP', 'GL_INCR_WRAP_EXT'],
 34056: ['GL_DECR_WRAP', 'GL_DECR_WRAP_EXT'],
 34057: ['GL_VERTEX_WEIGHTING_EXT'],
 34058: ['GL_MODELVIEW1_ARB', 'GL_MODELVIEW1_EXT'],
 34059: ['GL_CURRENT_VERTEX_WEIGHT_EXT'],
 34060: ['GL_VERTEX_WEIGHT_ARRAY_EXT'],
 34061: ['GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT'],
 34062: ['GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT'],
 34063: ['GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT'],
 34064: ['GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT'],
 34065: ['GL_NORMAL_MAP', 'GL_NORMAL_MAP_ARB', 'GL_NORMAL_MAP_EXT'],
 34066: ['GL_REFLECTION_MAP', 'GL_REFLECTION_MAP_ARB', 'GL_REFLECTION_MAP_EXT'],
 34067: ['GL_TEXTURE_CUBE_MAP',
         'GL_TEXTURE_CUBE_MAP_ARB',
         'GL_TEXTURE_CUBE_MAP_EXT'],
 34068: ['GL_TEXTURE_BINDING_CUBE_MAP',
         'GL_TEXTURE_BINDING_CUBE_MAP_ARB',
         'GL_TEXTURE_BINDING_CUBE_MAP_EXT'],
 34069: ['GL_TEXTURE_CUBE_MAP_POSITIVE_X',
         'GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB',
         'GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT'],
 34070: ['GL_TEXTURE_CUBE_MAP_NEGATIVE_X',
         'GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB',
         'GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT'],
 34071: ['GL_TEXTURE_CUBE_MAP_POSITIVE_Y',
         'GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB',
         'GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT'],
 34072: ['GL_TEXTURE_CUBE_MAP_NEGATIVE_Y',
         'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB',
         'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT'],
 34073: ['GL_TEXTURE_CUBE_MAP_POSITIVE_Z',
         'GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB',
         'GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT'],
 34074: ['GL_TEXTURE_CUBE_MAP_NEGATIVE_Z',
         'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB',
         'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT'],
 34075: ['GL_PROXY_TEXTURE_CUBE_MAP',
         'GL_PROXY_TEXTURE_CUBE_MAP_ARB',
         'GL_PROXY_TEXTURE_CUBE_MAP_EXT'],
 34076: ['GL_MAX_CUBE_MAP_TEXTURE_SIZE',
         'GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB',
         'GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT'],
 34144: ['GL_RED_MIN_CLAMP_INGR'],
 34145: ['GL_GREEN_MIN_CLAMP_INGR'],
 34146: ['GL_BLUE_MIN_CLAMP_INGR'],
 34147: ['GL_ALPHA_MIN_CLAMP_INGR'],
 34148: ['GL_RED_MAX_CLAMP_INGR'],
 34149: ['GL_GREEN_MAX_CLAMP_INGR'],
 34150: ['GL_BLUE_MAX_CLAMP_INGR'],
 34151: ['GL_ALPHA_MAX_CLAMP_INGR'],
 34152: ['GL_INTERLACE_READ_INGR'],
 34160: ['GL_COMBINE', 'GL_COMBINE_ARB', 'GL_COMBINE_EXT'],
 34161: ['GL_COMBINE_RGB', 'GL_COMBINE_RGB_ARB', 'GL_COMBINE_RGB_EXT'],
 34162: ['GL_COMBINE_ALPHA', 'GL_COMBINE_ALPHA_ARB', 'GL_COMBINE_ALPHA_EXT'],
 34163: ['GL_RGB_SCALE', 'GL_RGB_SCALE_ARB', 'GL_RGB_SCALE_EXT'],
 34164: ['GL_ADD_SIGNED', 'GL_ADD_SIGNED_ARB', 'GL_ADD_SIGNED_EXT'],
 34165: ['GL_INTERPOLATE', 'GL_INTERPOLATE_ARB', 'GL_INTERPOLATE_EXT'],
 34166: ['GL_CONSTANT', 'GL_CONSTANT_ARB', 'GL_CONSTANT_EXT'],
 34167: ['GL_PRIMARY_COLOR', 'GL_PRIMARY_COLOR_ARB', 'GL_PRIMARY_COLOR_EXT'],
 34168: ['GL_PREVIOUS', 'GL_PREVIOUS_ARB', 'GL_PREVIOUS_EXT'],
 34176: ['GL_SOURCE0_RGB',
         'GL_SOURCE0_RGB_ARB',
         'GL_SOURCE0_RGB_EXT',
         'GL_SRC0_RGB'],
 34177: ['GL_SOURCE1_RGB',
         'GL_SOURCE1_RGB_ARB',
         'GL_SOURCE1_RGB_EXT',
         'GL_SRC1_RGB'],
 34178: ['GL_SOURCE2_RGB',
         'GL_SOURCE2_RGB_ARB',
         'GL_SOURCE2_RGB_EXT',
         'GL_SRC2_RGB'],
 34184: ['GL_SOURCE0_ALPHA',
         'GL_SOURCE0_ALPHA_ARB',
         'GL_SOURCE0_ALPHA_EXT',
         'GL_SRC0_ALPHA'],
 34185: ['GL_SOURCE1_ALPHA',
         'GL_SOURCE1_ALPHA_ARB',
         'GL_SOURCE1_ALPHA_EXT',
         'GL_SRC1_ALPHA',
         'GL_SRC1_ALPHA_EXT'],
 34186: ['GL_SOURCE2_ALPHA',
         'GL_SOURCE2_ALPHA_ARB',
         'GL_SOURCE2_ALPHA_EXT',
         'GL_SRC2_ALPHA'],
 34192: ['GL_OPERAND0_RGB', 'GL_OPERAND0_RGB_ARB', 'GL_OPERAND0_RGB_EXT'],
 34193: ['GL_OPERAND1_RGB', 'GL_OPERAND1_RGB_ARB', 'GL_OPERAND1_RGB_EXT'],
 34194: ['GL_OPERAND2_RGB', 'GL_OPERAND2_RGB_ARB', 'GL_OPERAND2_RGB_EXT'],
 34200: ['GL_OPERAND0_ALPHA', 'GL_OPERAND0_ALPHA_ARB', 'GL_OPERAND0_ALPHA_EXT'],
 34201: ['GL_OPERAND1_ALPHA', 'GL_OPERAND1_ALPHA_ARB', 'GL_OPERAND1_ALPHA_EXT'],
 34202: ['GL_OPERAND2_ALPHA', 'GL_OPERAND2_ALPHA_ARB', 'GL_OPERAND2_ALPHA_EXT'],
 34222: ['GL_PERTURB_EXT'],
 34223: ['GL_TEXTURE_NORMAL_EXT'],
 34229: ['GL_VERTEX_ARRAY_BINDING'],
 34336: ['GL_VERTEX_PROGRAM_ARB'],
 34338: ['GL_VERTEX_ATTRIB_ARRAY_ENABLED',
         'GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB'],
 34339: ['GL_VERTEX_ATTRIB_ARRAY_SIZE', 'GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB'],
 34340: ['GL_VERTEX_ATTRIB_ARRAY_STRIDE', 'GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB'],
 34341: ['GL_VERTEX_ATTRIB_ARRAY_TYPE', 'GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB'],
 34342: ['GL_CURRENT_VERTEX_ATTRIB', 'GL_CURRENT_VERTEX_ATTRIB_ARB'],
 34343: ['GL_PROGRAM_LENGTH_ARB'],
 34344: ['GL_PROGRAM_STRING_ARB'],
 34350: ['GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB'],
 34351: ['GL_MAX_PROGRAM_MATRICES_ARB'],
 34368: ['GL_CURRENT_MATRIX_STACK_DEPTH_ARB'],
 34369: ['GL_CURRENT_MATRIX_ARB'],
 34370: ['GL_VERTEX_PROGRAM_POINT_SIZE',
         'GL_VERTEX_PROGRAM_POINT_SIZE_ARB',
         'GL_PROGRAM_POINT_SIZE',
         'GL_PROGRAM_POINT_SIZE_ARB',
         'GL_PROGRAM_POINT_SIZE_EXT'],
 34371: ['GL_VERTEX_PROGRAM_TWO_SIDE', 'GL_VERTEX_PROGRAM_TWO_SIDE_ARB'],
 34373: ['GL_VERTEX_ATTRIB_ARRAY_POINTER',
         'GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB'],
 34379: ['GL_PROGRAM_ERROR_POSITION_ARB'],
 34383: ['GL_DEPTH_CLAMP', 'GL_DEPTH_CLAMP_EXT'],
 34423: ['GL_PROGRAM_BINDING_ARB'],
 34464: ['GL_TEXTURE_COMPRESSED_IMAGE_SIZE',
         'GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB'],
 34465: ['GL_TEXTURE_COMPRESSED', 'GL_TEXTURE_COMPRESSED_ARB'],
 34466: ['GL_NUM_COMPRESSED_TEXTURE_FORMATS',
         'GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB'],
 34467: ['GL_COMPRESSED_TEXTURE_FORMATS', 'GL_COMPRESSED_TEXTURE_FORMATS_ARB'],
 34468: ['GL_MAX_VERTEX_UNITS_ARB'],
 34469: ['GL_ACTIVE_VERTEX_UNITS_ARB'],
 34470: ['GL_WEIGHT_SUM_UNITY_ARB'],
 34471: ['GL_VERTEX_BLEND_ARB'],
 34472: ['GL_CURRENT_WEIGHT_ARB'],
 34473: ['GL_WEIGHT_ARRAY_TYPE_ARB'],
 34474: ['GL_WEIGHT_ARRAY_STRIDE_ARB'],
 34475: ['GL_WEIGHT_ARRAY_SIZE_ARB'],
 34476: ['GL_WEIGHT_ARRAY_POINTER_ARB'],
 34477: ['GL_WEIGHT_ARRAY_ARB'],
 34478: ['GL_DOT3_RGB', 'GL_DOT3_RGB_ARB'],
 34479: ['GL_DOT3_RGBA', 'GL_DOT3_RGBA_ARB', 'GL_DOT3_RGBA_IMG'],
 34480: ['GL_COMPRESSED_RGB_FXT1_3DFX'],
 34481: ['GL_COMPRESSED_RGBA_FXT1_3DFX'],
 34482: ['GL_MULTISAMPLE_3DFX'],
 34483: ['GL_SAMPLE_BUFFERS_3DFX'],
 34484: ['GL_SAMPLES_3DFX'],
 34594: ['GL_MODELVIEW2_ARB'],
 34595: ['GL_MODELVIEW3_ARB'],
 34596: ['GL_MODELVIEW4_ARB'],
 34597: ['GL_MODELVIEW5_ARB'],
 34598: ['GL_MODELVIEW6_ARB'],
 34599: ['GL_MODELVIEW7_ARB'],
 34600: ['GL_MODELVIEW8_ARB'],
 34601: ['GL_MODELVIEW9_ARB'],
 34602: ['GL_MODELVIEW10_ARB'],
 34603: ['GL_MODELVIEW11_ARB'],
 34604: ['GL_MODELVIEW12_ARB'],
 34605: ['GL_MODELVIEW13_ARB'],
 34606: ['GL_MODELVIEW14_ARB'],
 34607: ['GL_MODELVIEW15_ARB'],
 34608: ['GL_MODELVIEW16_ARB'],
 34609: ['GL_MODELVIEW17_ARB'],
 34610: ['GL_MODELVIEW18_ARB'],
 34611: ['GL_MODELVIEW19_ARB'],
 34612: ['GL_MODELVIEW20_ARB'],
 34613: ['GL_MODELVIEW21_ARB'],
 34614: ['GL_MODELVIEW22_ARB'],
 34615: ['GL_MODELVIEW23_ARB'],
 34616: ['GL_MODELVIEW24_ARB'],
 34617: ['GL_MODELVIEW25_ARB'],
 34618: ['GL_MODELVIEW26_ARB'],
 34619: ['GL_MODELVIEW27_ARB'],
 34620: ['GL_MODELVIEW28_ARB'],
 34621: ['GL_MODELVIEW29_ARB'],
 34622: ['GL_MODELVIEW30_ARB'],
 34623: ['GL_MODELVIEW31_ARB'],
 34624: ['GL_DOT3_RGB_EXT'],
 34625: ['GL_DOT3_RGBA_EXT', 'GL_PROGRAM_BINARY_LENGTH'],
 34626: ['GL_MIRROR_CLAMP_EXT'],
 34627: ['GL_MIRROR_CLAMP_TO_EDGE', 'GL_MIRROR_CLAMP_TO_EDGE_EXT'],
 34638: ['GL_VERTEX_ATTRIB_ARRAY_LONG'],
 34649: ['GL_TEXTURE_1D_STACK_MESAX'],
 34650: ['GL_TEXTURE_2D_STACK_MESAX'],
 34651: ['GL_PROXY_TEXTURE_1D_STACK_MESAX'],
 34652: ['GL_PROXY_TEXTURE_2D_STACK_MESAX'],
 34653: ['GL_TEXTURE_1D_STACK_BINDING_MESAX'],
 34654: ['GL_TEXTURE_2D_STACK_BINDING_MESAX'],
 34660: ['GL_BUFFER_SIZE', 'GL_BUFFER_SIZE_ARB'],
 34661: ['GL_BUFFER_USAGE', 'GL_BUFFER_USAGE_ARB'],
 34688: ['GL_VERTEX_SHADER_EXT'],
 34689: ['GL_VERTEX_SHADER_BINDING_EXT'],
 34690: ['GL_OP_INDEX_EXT'],
 34691: ['GL_OP_NEGATE_EXT'],
 34692: ['GL_OP_DOT3_EXT'],
 34693: ['GL_OP_DOT4_EXT'],
 34694: ['GL_OP_MUL_EXT'],
 34695: ['GL_OP_ADD_EXT'],
 34696: ['GL_OP_MADD_EXT'],
 34697: ['GL_OP_FRAC_EXT'],
 34698: ['GL_OP_MAX_EXT'],
 34699: ['GL_OP_MIN_EXT'],
 34700: ['GL_OP_SET_GE_EXT'],
 34701: ['GL_OP_SET_LT_EXT'],
 34702: ['GL_OP_CLAMP_EXT'],
 34703: ['GL_OP_FLOOR_EXT'],
 34704: ['GL_OP_ROUND_EXT'],
 34705: ['GL_OP_EXP_BASE_2_EXT'],
 34706: ['GL_OP_LOG_BASE_2_EXT'],
 34707: ['GL_OP_POWER_EXT'],
 34708: ['GL_OP_RECIP_EXT'],
 34709: ['GL_OP_RECIP_SQRT_EXT'],
 34710: ['GL_OP_SUB_EXT'],
 34711: ['GL_OP_CROSS_PRODUCT_EXT'],
 34712: ['GL_OP_MULTIPLY_MATRIX_EXT'],
 34713: ['GL_OP_MOV_EXT'],
 34714: ['GL_OUTPUT_VERTEX_EXT'],
 34715: ['GL_OUTPUT_COLOR0_EXT'],
 34716: ['GL_OUTPUT_COLOR1_EXT'],
 34717: ['GL_OUTPUT_TEXTURE_COORD0_EXT'],
 34718: ['GL_OUTPUT_TEXTURE_COORD1_EXT'],
 34719: ['GL_OUTPUT_TEXTURE_COORD2_EXT'],
 34720: ['GL_OUTPUT_TEXTURE_COORD3_EXT'],
 34721: ['GL_OUTPUT_TEXTURE_COORD4_EXT'],
 34722: ['GL_OUTPUT_TEXTURE_COORD5_EXT'],
 34723: ['GL_OUTPUT_TEXTURE_COORD6_EXT'],
 34724: ['GL_OUTPUT_TEXTURE_COORD7_EXT'],
 34725: ['GL_OUTPUT_TEXTURE_COORD8_EXT'],
 34726: ['GL_OUTPUT_TEXTURE_COORD9_EXT'],
 34727: ['GL_OUTPUT_TEXTURE_COORD10_EXT'],
 34728: ['GL_OUTPUT_TEXTURE_COORD11_EXT'],
 34729: ['GL_OUTPUT_TEXTURE_COORD12_EXT'],
 34730: ['GL_OUTPUT_TEXTURE_COORD13_EXT'],
 34731: ['GL_OUTPUT_TEXTURE_COORD14_EXT'],
 34732: ['GL_OUTPUT_TEXTURE_COORD15_EXT'],
 34733: ['GL_OUTPUT_TEXTURE_COORD16_EXT'],
 34734: ['GL_OUTPUT_TEXTURE_COORD17_EXT'],
 34735: ['GL_OUTPUT_TEXTURE_COORD18_EXT'],
 34736: ['GL_OUTPUT_TEXTURE_COORD19_EXT'],
 34737: ['GL_OUTPUT_TEXTURE_COORD20_EXT'],
 34738: ['GL_OUTPUT_TEXTURE_COORD21_EXT'],
 34739: ['GL_OUTPUT_TEXTURE_COORD22_EXT'],
 34740: ['GL_OUTPUT_TEXTURE_COORD23_EXT'],
 34741: ['GL_OUTPUT_TEXTURE_COORD24_EXT'],
 34742: ['GL_OUTPUT_TEXTURE_COORD25_EXT'],
 34743: ['GL_OUTPUT_TEXTURE_COORD26_EXT'],
 34744: ['GL_OUTPUT_TEXTURE_COORD27_EXT'],
 34745: ['GL_OUTPUT_TEXTURE_COORD28_EXT'],
 34746: ['GL_OUTPUT_TEXTURE_COORD29_EXT'],
 34747: ['GL_OUTPUT_TEXTURE_COORD30_EXT'],
 34748: ['GL_OUTPUT_TEXTURE_COORD31_EXT'],
 34749: ['GL_OUTPUT_FOG_EXT'],
 34750: ['GL_SCALAR_EXT'],
 34751: ['GL_VECTOR_EXT'],
 34752: ['GL_MATRIX_EXT'],
 34753: ['GL_VARIANT_EXT'],
 34754: ['GL_INVARIANT_EXT'],
 34755: ['GL_LOCAL_CONSTANT_EXT'],
 34756: ['GL_LOCAL_EXT'],
 34757: ['GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT'],
 34758: ['GL_MAX_VERTEX_SHADER_VARIANTS_EXT'],
 34759: ['GL_MAX_VERTEX_SHADER_INVARIANTS_EXT'],
 34760: ['GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT'],
 34761: ['GL_MAX_VERTEX_SHADER_LOCALS_EXT'],
 34762: ['GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT'],
 34763: ['GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT'],
 34764: ['GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT'],
 34765: ['GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT'],
 34766: ['GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT'],
 34767: ['GL_VERTEX_SHADER_INSTRUCTIONS_EXT'],
 34768: ['GL_VERTEX_SHADER_VARIANTS_EXT'],
 34769: ['GL_VERTEX_SHADER_INVARIANTS_EXT'],
 34770: ['GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT'],
 34771: ['GL_VERTEX_SHADER_LOCALS_EXT'],
 34772: ['GL_VERTEX_SHADER_OPTIMIZED_EXT'],
 34773: ['GL_X_EXT'],
 34774: ['GL_Y_EXT'],
 34775: ['GL_Z_EXT'],
 34776: ['GL_W_EXT'],
 34777: ['GL_NEGATIVE_X_EXT'],
 34778: ['GL_NEGATIVE_Y_EXT'],
 34779: ['GL_NEGATIVE_Z_EXT'],
 34780: ['GL_NEGATIVE_W_EXT'],
 34781: ['GL_ZERO_EXT'],
 34782: ['GL_ONE_EXT'],
 34783: ['GL_NEGATIVE_ONE_EXT'],
 34784: ['GL_NORMALIZED_RANGE_EXT'],
 34785: ['GL_FULL_RANGE_EXT'],
 34786: ['GL_CURRENT_VERTEX_EXT'],
 34787: ['GL_MVP_MATRIX_EXT'],
 34788: ['GL_VARIANT_VALUE_EXT'],
 34789: ['GL_VARIANT_DATATYPE_EXT'],
 34790: ['GL_VARIANT_ARRAY_STRIDE_EXT'],
 34791: ['GL_VARIANT_ARRAY_TYPE_EXT'],
 34792: ['GL_VARIANT_ARRAY_EXT'],
 34793: ['GL_VARIANT_ARRAY_POINTER_EXT'],
 34794: ['GL_INVARIANT_VALUE_EXT'],
 34795: ['GL_INVARIANT_DATATYPE_EXT'],
 34796: ['GL_LOCAL_CONSTANT_VALUE_EXT'],
 34797: ['GL_LOCAL_CONSTANT_DATATYPE_EXT'],
 34814: ['GL_NUM_PROGRAM_BINARY_FORMATS'],
 34815: ['GL_PROGRAM_BINARY_FORMATS'],
 34816: ['GL_STENCIL_BACK_FUNC'],
 34817: ['GL_STENCIL_BACK_FAIL'],
 34818: ['GL_STENCIL_BACK_PASS_DEPTH_FAIL'],
 34819: ['GL_STENCIL_BACK_PASS_DEPTH_PASS'],
 34820: ['GL_FRAGMENT_PROGRAM_ARB'],
 34821: ['GL_PROGRAM_ALU_INSTRUCTIONS_ARB'],
 34822: ['GL_PROGRAM_TEX_INSTRUCTIONS_ARB'],
 34823: ['GL_PROGRAM_TEX_INDIRECTIONS_ARB'],
 34824: ['GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB'],
 34825: ['GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB'],
 34826: ['GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB'],
 34827: ['GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB'],
 34828: ['GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB'],
 34829: ['GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB'],
 34830: ['GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB'],
 34831: ['GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB'],
 34832: ['GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB'],
 34836: ['GL_RGBA32F', 'GL_RGBA32F_ARB', 'GL_RGBA32F_EXT'],
 34837: ['GL_RGB32F', 'GL_RGB32F_ARB', 'GL_RGB32F_EXT'],
 34838: ['GL_ALPHA32F_ARB', 'GL_ALPHA32F_EXT'],
 34839: ['GL_INTENSITY32F_ARB'],
 34840: ['GL_LUMINANCE32F_ARB', 'GL_LUMINANCE32F_EXT'],
 34841: ['GL_LUMINANCE_ALPHA32F_ARB', 'GL_LUMINANCE_ALPHA32F_EXT'],
 34842: ['GL_RGBA16F', 'GL_RGBA16F_ARB', 'GL_RGBA16F_EXT'],
 34843: ['GL_RGB16F', 'GL_RGB16F_ARB', 'GL_RGB16F_EXT'],
 34844: ['GL_ALPHA16F_ARB', 'GL_ALPHA16F_EXT'],
 34845: ['GL_INTENSITY16F_ARB'],
 34846: ['GL_LUMINANCE16F_ARB', 'GL_LUMINANCE16F_EXT'],
 34847: ['GL_LUMINANCE_ALPHA16F_ARB', 'GL_LUMINANCE_ALPHA16F_EXT'],
 34848: ['GL_RGBA_FLOAT_MODE_ARB'],
 34852: ['GL_MAX_DRAW_BUFFERS',
         'GL_MAX_DRAW_BUFFERS_ARB',
         'GL_MAX_DRAW_BUFFERS_EXT'],
 34853: ['GL_DRAW_BUFFER0', 'GL_DRAW_BUFFER0_ARB', 'GL_DRAW_BUFFER0_EXT'],
 34854: ['GL_DRAW_BUFFER1', 'GL_DRAW_BUFFER1_ARB', 'GL_DRAW_BUFFER1_EXT'],
 34855: ['GL_DRAW_BUFFER2', 'GL_DRAW_BUFFER2_ARB', 'GL_DRAW_BUFFER2_EXT'],
 34856: ['GL_DRAW_BUFFER3', 'GL_DRAW_BUFFER3_ARB', 'GL_DRAW_BUFFER3_EXT'],
 34857: ['GL_DRAW_BUFFER4', 'GL_DRAW_BUFFER4_ARB', 'GL_DRAW_BUFFER4_EXT'],
 34858: ['GL_DRAW_BUFFER5', 'GL_DRAW_BUFFER5_ARB', 'GL_DRAW_BUFFER5_EXT'],
 34859: ['GL_DRAW_BUFFER6', 'GL_DRAW_BUFFER6_ARB', 'GL_DRAW_BUFFER6_EXT'],
 34860: ['GL_DRAW_BUFFER7', 'GL_DRAW_BUFFER7_ARB', 'GL_DRAW_BUFFER7_EXT'],
 34861: ['GL_DRAW_BUFFER8', 'GL_DRAW_BUFFER8_ARB', 'GL_DRAW_BUFFER8_EXT'],
 34862: ['GL_DRAW_BUFFER9', 'GL_DRAW_BUFFER9_ARB', 'GL_DRAW_BUFFER9_EXT'],
 34863: ['GL_DRAW_BUFFER10', 'GL_DRAW_BUFFER10_ARB', 'GL_DRAW_BUFFER10_EXT'],
 34864: ['GL_DRAW_BUFFER11', 'GL_DRAW_BUFFER11_ARB', 'GL_DRAW_BUFFER11_EXT'],
 34865: ['GL_DRAW_BUFFER12', 'GL_DRAW_BUFFER12_ARB', 'GL_DRAW_BUFFER12_EXT'],
 34866: ['GL_DRAW_BUFFER13', 'GL_DRAW_BUFFER13_ARB', 'GL_DRAW_BUFFER13_EXT'],
 34867: ['GL_DRAW_BUFFER14', 'GL_DRAW_BUFFER14_ARB', 'GL_DRAW_BUFFER14_EXT'],
 34868: ['GL_DRAW_BUFFER15', 'GL_DRAW_BUFFER15_ARB', 'GL_DRAW_BUFFER15_EXT'],
 34877: ['GL_BLEND_EQUATION_ALPHA', 'GL_BLEND_EQUATION_ALPHA_EXT'],
 34880: ['GL_MATRIX_PALETTE_ARB'],
 34881: ['GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB'],
 34882: ['GL_MAX_PALETTE_MATRICES_ARB'],
 34883: ['GL_CURRENT_PALETTE_MATRIX_ARB'],
 34884: ['GL_MATRIX_INDEX_ARRAY_ARB'],
 34885: ['GL_CURRENT_MATRIX_INDEX_ARB'],
 34886: ['GL_MATRIX_INDEX_ARRAY_SIZE_ARB'],
 34887: ['GL_MATRIX_INDEX_ARRAY_TYPE_ARB'],
 34888: ['GL_MATRIX_INDEX_ARRAY_STRIDE_ARB'],
 34889: ['GL_MATRIX_INDEX_ARRAY_POINTER_ARB'],
 34890: ['GL_TEXTURE_DEPTH_SIZE', 'GL_TEXTURE_DEPTH_SIZE_ARB'],
 34891: ['GL_DEPTH_TEXTURE_MODE', 'GL_DEPTH_TEXTURE_MODE_ARB'],
 34892: ['GL_TEXTURE_COMPARE_MODE',
         'GL_TEXTURE_COMPARE_MODE_ARB',
         'GL_TEXTURE_COMPARE_MODE_EXT'],
 34893: ['GL_TEXTURE_COMPARE_FUNC',
         'GL_TEXTURE_COMPARE_FUNC_ARB',
         'GL_TEXTURE_COMPARE_FUNC_EXT'],
 34894: ['GL_COMPARE_R_TO_TEXTURE',
         'GL_COMPARE_R_TO_TEXTURE_ARB',
         'GL_COMPARE_REF_DEPTH_TO_TEXTURE_EXT',
         'GL_COMPARE_REF_TO_TEXTURE',
         'GL_COMPARE_REF_TO_TEXTURE_EXT'],
 34895: ['GL_TEXTURE_CUBE_MAP_SEAMLESS'],
 34913: ['GL_POINT_SPRITE', 'GL_POINT_SPRITE_ARB'],
 34914: ['GL_COORD_REPLACE', 'GL_COORD_REPLACE_ARB'],
 34916: ['GL_QUERY_COUNTER_BITS',
         'GL_QUERY_COUNTER_BITS_ARB',
         'GL_QUERY_COUNTER_BITS_EXT'],
 34917: ['GL_CURRENT_QUERY', 'GL_CURRENT_QUERY_ARB', 'GL_CURRENT_QUERY_EXT'],
 34918: ['GL_QUERY_RESULT', 'GL_QUERY_RESULT_ARB', 'GL_QUERY_RESULT_EXT'],
 34919: ['GL_QUERY_RESULT_AVAILABLE',
         'GL_QUERY_RESULT_AVAILABLE_ARB',
         'GL_QUERY_RESULT_AVAILABLE_EXT'],
 34921: ['GL_MAX_VERTEX_ATTRIBS', 'GL_MAX_VERTEX_ATTRIBS_ARB'],
 34922: ['GL_VERTEX_ATTRIB_ARRAY_NORMALIZED',
         'GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB'],
 34924: ['GL_MAX_TESS_CONTROL_INPUT_COMPONENTS',
         'GL_MAX_TESS_CONTROL_INPUT_COMPONENTS_EXT'],
 34925: ['GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS',
         'GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS_EXT'],
 34929: ['GL_MAX_TEXTURE_COORDS', 'GL_MAX_TEXTURE_COORDS_ARB'],
 34930: ['GL_MAX_TEXTURE_IMAGE_UNITS', 'GL_MAX_TEXTURE_IMAGE_UNITS_ARB'],
 34932: ['GL_PROGRAM_ERROR_STRING_ARB'],
 34933: ['GL_PROGRAM_FORMAT_ASCII_ARB'],
 34934: ['GL_PROGRAM_FORMAT_ARB'],
 34943: ['GL_GEOMETRY_SHADER_INVOCATIONS',
         'GL_GEOMETRY_SHADER_INVOCATIONS_EXT'],
 34960: ['GL_DEPTH_BOUNDS_TEST_EXT'],
 34961: ['GL_DEPTH_BOUNDS_EXT'],
 34962: ['GL_ARRAY_BUFFER', 'GL_ARRAY_BUFFER_ARB'],
 34963: ['GL_ELEMENT_ARRAY_BUFFER', 'GL_ELEMENT_ARRAY_BUFFER_ARB'],
 34964: ['GL_ARRAY_BUFFER_BINDING', 'GL_ARRAY_BUFFER_BINDING_ARB'],
 34965: ['GL_ELEMENT_ARRAY_BUFFER_BINDING',
         'GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB'],
 34966: ['GL_VERTEX_ARRAY_BUFFER_BINDING',
         'GL_VERTEX_ARRAY_BUFFER_BINDING_ARB'],
 34967: ['GL_NORMAL_ARRAY_BUFFER_BINDING',
         'GL_NORMAL_ARRAY_BUFFER_BINDING_ARB'],
 34968: ['GL_COLOR_ARRAY_BUFFER_BINDING', 'GL_COLOR_ARRAY_BUFFER_BINDING_ARB'],
 34969: ['GL_INDEX_ARRAY_BUFFER_BINDING', 'GL_INDEX_ARRAY_BUFFER_BINDING_ARB'],
 34970: ['GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING',
         'GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB'],
 34971: ['GL_EDGE_FLAG_ARRAY_BUFFER_BINDING',
         'GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB'],
 34972: ['GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING',
         'GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB'],
 34973: ['GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB',
         'GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING',
         'GL_FOG_COORD_ARRAY_BUFFER_BINDING'],
 34974: ['GL_WEIGHT_ARRAY_BUFFER_BINDING',
         'GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB'],
 34975: ['GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING',
         'GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB'],
 34976: ['GL_PROGRAM_INSTRUCTIONS_ARB'],
 34977: ['GL_MAX_PROGRAM_INSTRUCTIONS_ARB'],
 34978: ['GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB'],
 34979: ['GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB'],
 34980: ['GL_PROGRAM_TEMPORARIES_ARB'],
 34981: ['GL_MAX_PROGRAM_TEMPORARIES_ARB'],
 34982: ['GL_PROGRAM_NATIVE_TEMPORARIES_ARB'],
 34983: ['GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB'],
 34984: ['GL_PROGRAM_PARAMETERS_ARB'],
 34985: ['GL_MAX_PROGRAM_PARAMETERS_ARB'],
 34986: ['GL_PROGRAM_NATIVE_PARAMETERS_ARB'],
 34987: ['GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB'],
 34988: ['GL_PROGRAM_ATTRIBS_ARB'],
 34989: ['GL_MAX_PROGRAM_ATTRIBS_ARB'],
 34990: ['GL_PROGRAM_NATIVE_ATTRIBS_ARB'],
 34991: ['GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB'],
 34992: ['GL_PROGRAM_ADDRESS_REGISTERS_ARB'],
 34993: ['GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB'],
 34994: ['GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB'],
 34995: ['GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB'],
 34996: ['GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB'],
 34997: ['GL_MAX_PROGRAM_ENV_PARAMETERS_ARB'],
 34998: ['GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB'],
 34999: ['GL_TRANSPOSE_CURRENT_MATRIX_ARB'],
 35000: ['GL_READ_ONLY', 'GL_READ_ONLY_ARB'],
 35001: ['GL_WRITE_ONLY', 'GL_WRITE_ONLY_ARB'],
 35002: ['GL_READ_WRITE', 'GL_READ_WRITE_ARB'],
 35003: ['GL_BUFFER_ACCESS', 'GL_BUFFER_ACCESS_ARB'],
 35004: ['GL_BUFFER_MAPPED', 'GL_BUFFER_MAPPED_ARB'],
 35005: ['GL_BUFFER_MAP_POINTER', 'GL_BUFFER_MAP_POINTER_ARB'],
 35007: ['GL_TIME_ELAPSED', 'GL_TIME_ELAPSED_EXT'],
 35008: ['GL_MATRIX0_ARB'],
 35009: ['GL_MATRIX1_ARB'],
 35010: ['GL_MATRIX2_ARB'],
 35011: ['GL_MATRIX3_ARB'],
 35012: ['GL_MATRIX4_ARB'],
 35013: ['GL_MATRIX5_ARB'],
 35014: ['GL_MATRIX6_ARB'],
 35015: ['GL_MATRIX7_ARB'],
 35016: ['GL_MATRIX8_ARB'],
 35017: ['GL_MATRIX9_ARB'],
 35018: ['GL_MATRIX10_ARB'],
 35019: ['GL_MATRIX11_ARB'],
 35020: ['GL_MATRIX12_ARB'],
 35021: ['GL_MATRIX13_ARB'],
 35022: ['GL_MATRIX14_ARB'],
 35023: ['GL_MATRIX15_ARB'],
 35024: ['GL_MATRIX16_ARB'],
 35025: ['GL_MATRIX17_ARB'],
 35026: ['GL_MATRIX18_ARB'],
 35027: ['GL_MATRIX19_ARB'],
 35028: ['GL_MATRIX20_ARB'],
 35029: ['GL_MATRIX21_ARB'],
 35030: ['GL_MATRIX22_ARB'],
 35031: ['GL_MATRIX23_ARB'],
 35032: ['GL_MATRIX24_ARB'],
 35033: ['GL_MATRIX25_ARB'],
 35034: ['GL_MATRIX26_ARB'],
 35035: ['GL_MATRIX27_ARB'],
 35036: ['GL_MATRIX28_ARB'],
 35037: ['GL_MATRIX29_ARB'],
 35038: ['GL_MATRIX30_ARB'],
 35039: ['GL_MATRIX31_ARB'],
 35040: ['GL_STREAM_DRAW', 'GL_STREAM_DRAW_ARB'],
 35041: ['GL_STREAM_READ', 'GL_STREAM_READ_ARB'],
 35042: ['GL_STREAM_COPY', 'GL_STREAM_COPY_ARB'],
 35044: ['GL_STATIC_DRAW', 'GL_STATIC_DRAW_ARB'],
 35045: ['GL_STATIC_READ', 'GL_STATIC_READ_ARB'],
 35046: ['GL_STATIC_COPY', 'GL_STATIC_COPY_ARB'],
 35048: ['GL_DYNAMIC_DRAW', 'GL_DYNAMIC_DRAW_ARB'],
 35049: ['GL_DYNAMIC_READ', 'GL_DYNAMIC_READ_ARB'],
 35050: ['GL_DYNAMIC_COPY', 'GL_DYNAMIC_COPY_ARB'],
 35051: ['GL_PIXEL_PACK_BUFFER',
         'GL_PIXEL_PACK_BUFFER_ARB',
         'GL_PIXEL_PACK_BUFFER_EXT'],
 35052: ['GL_PIXEL_UNPACK_BUFFER',
         'GL_PIXEL_UNPACK_BUFFER_ARB',
         'GL_PIXEL_UNPACK_BUFFER_EXT'],
 35053: ['GL_PIXEL_PACK_BUFFER_BINDING',
         'GL_PIXEL_PACK_BUFFER_BINDING_ARB',
         'GL_PIXEL_PACK_BUFFER_BINDING_EXT'],
 35055: ['GL_PIXEL_UNPACK_BUFFER_BINDING',
         'GL_PIXEL_UNPACK_BUFFER_BINDING_ARB',
         'GL_PIXEL_UNPACK_BUFFER_BINDING_EXT'],
 35056: ['GL_DEPTH24_STENCIL8', 'GL_DEPTH24_STENCIL8_EXT'],
 35057: ['GL_TEXTURE_STENCIL_SIZE', 'GL_TEXTURE_STENCIL_SIZE_EXT'],
 35058: ['GL_STENCIL_TAG_BITS_EXT'],
 35059: ['GL_STENCIL_CLEAR_TAG_VALUE_EXT'],
 35065: ['GL_SRC1_COLOR', 'GL_SRC1_COLOR_EXT'],
 35066: ['GL_ONE_MINUS_SRC1_COLOR', 'GL_ONE_MINUS_SRC1_COLOR_EXT'],
 35067: ['GL_ONE_MINUS_SRC1_ALPHA', 'GL_ONE_MINUS_SRC1_ALPHA_EXT'],
 35068: ['GL_MAX_DUAL_SOURCE_DRAW_BUFFERS',
         'GL_MAX_DUAL_SOURCE_DRAW_BUFFERS_EXT'],
 35069: ['GL_VERTEX_ATTRIB_ARRAY_INTEGER',
         'GL_VERTEX_ATTRIB_ARRAY_INTEGER_EXT'],
 35070: ['GL_VERTEX_ATTRIB_ARRAY_DIVISOR',
         'GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE',
         'GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB',
         'GL_VERTEX_ATTRIB_ARRAY_DIVISOR_EXT'],
 35071: ['GL_MAX_ARRAY_TEXTURE_LAYERS', 'GL_MAX_ARRAY_TEXTURE_LAYERS_EXT'],
 35076: ['GL_MIN_PROGRAM_TEXEL_OFFSET', 'GL_MIN_PROGRAM_TEXEL_OFFSET_EXT'],
 35077: ['GL_MAX_PROGRAM_TEXEL_OFFSET', 'GL_MAX_PROGRAM_TEXEL_OFFSET_EXT'],
 35088: ['GL_STENCIL_TEST_TWO_SIDE_EXT'],
 35089: ['GL_ACTIVE_STENCIL_FACE_EXT'],
 35090: ['GL_MIRROR_CLAMP_TO_BORDER_EXT'],
 35092: ['GL_SAMPLES_PASSED', 'GL_SAMPLES_PASSED_ARB'],
 35094: ['GL_GEOMETRY_VERTICES_OUT', 'GL_GEOMETRY_LINKED_VERTICES_OUT_EXT'],
 35095: ['GL_GEOMETRY_INPUT_TYPE', 'GL_GEOMETRY_LINKED_INPUT_TYPE_EXT'],
 35096: ['GL_GEOMETRY_OUTPUT_TYPE', 'GL_GEOMETRY_LINKED_OUTPUT_TYPE_EXT'],
 35097: ['GL_SAMPLER_BINDING'],
 35098: ['GL_CLAMP_VERTEX_COLOR', 'GL_CLAMP_VERTEX_COLOR_ARB'],
 35099: ['GL_CLAMP_FRAGMENT_COLOR', 'GL_CLAMP_FRAGMENT_COLOR_ARB'],
 35100: ['GL_CLAMP_READ_COLOR', 'GL_CLAMP_READ_COLOR_ARB'],
 35101: ['GL_FIXED_ONLY', 'GL_FIXED_ONLY_ARB'],
 35200: ['GL_INTERLACE_OML'],
 35201: ['GL_INTERLACE_READ_OML'],
 35202: ['GL_FORMAT_SUBSAMPLE_24_24_OML'],
 35203: ['GL_FORMAT_SUBSAMPLE_244_244_OML'],
 35204: ['GL_PACK_RESAMPLE_OML'],
 35205: ['GL_UNPACK_RESAMPLE_OML'],
 35206: ['GL_RESAMPLE_REPLICATE_OML'],
 35207: ['GL_RESAMPLE_ZERO_FILL_OML'],
 35208: ['GL_RESAMPLE_AVERAGE_OML'],
 35209: ['GL_RESAMPLE_DECIMATE_OML'],
 35345: ['GL_UNIFORM_BUFFER'],
 35368: ['GL_UNIFORM_BUFFER_BINDING'],
 35369: ['GL_UNIFORM_BUFFER_START'],
 35370: ['GL_UNIFORM_BUFFER_SIZE'],
 35371: ['GL_MAX_VERTEX_UNIFORM_BLOCKS'],
 35372: ['GL_MAX_GEOMETRY_UNIFORM_BLOCKS',
         'GL_MAX_GEOMETRY_UNIFORM_BLOCKS_EXT'],
 35373: ['GL_MAX_FRAGMENT_UNIFORM_BLOCKS'],
 35374: ['GL_MAX_COMBINED_UNIFORM_BLOCKS'],
 35375: ['GL_MAX_UNIFORM_BUFFER_BINDINGS'],
 35376: ['GL_MAX_UNIFORM_BLOCK_SIZE'],
 35377: ['GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS'],
 35378: ['GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS',
         'GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS_EXT'],
 35379: ['GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS'],
 35380: ['GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT'],
 35381: ['GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH'],
 35382: ['GL_ACTIVE_UNIFORM_BLOCKS'],
 35383: ['GL_UNIFORM_TYPE'],
 35384: ['GL_UNIFORM_SIZE'],
 35385: ['GL_UNIFORM_NAME_LENGTH'],
 35386: ['GL_UNIFORM_BLOCK_INDEX'],
 35387: ['GL_UNIFORM_OFFSET'],
 35388: ['GL_UNIFORM_ARRAY_STRIDE'],
 35389: ['GL_UNIFORM_MATRIX_STRIDE'],
 35390: ['GL_UNIFORM_IS_ROW_MAJOR'],
 35391: ['GL_UNIFORM_BLOCK_BINDING'],
 35392: ['GL_UNIFORM_BLOCK_DATA_SIZE'],
 35393: ['GL_UNIFORM_BLOCK_NAME_LENGTH'],
 35394: ['GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS'],
 35395: ['GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES'],
 35396: ['GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER'],
 35397: ['GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER'],
 35398: ['GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER'],
 35400: ['GL_TEXTURE_SRGB_DECODE_EXT'],
 35401: ['GL_DECODE_EXT'],
 35402: ['GL_SKIP_DECODE_EXT'],
 35407: ['GL_PROGRAM_PIPELINE_OBJECT_EXT'],
 35410: ['GL_FRAGMENT_SHADER_DISCARDS_SAMPLES_EXT'],
 35412: ['GL_COMPRESSED_SRGB_PVRTC_2BPPV1_EXT'],
 35413: ['GL_COMPRESSED_SRGB_PVRTC_4BPPV1_EXT'],
 35414: ['GL_COMPRESSED_SRGB_ALPHA_PVRTC_2BPPV1_EXT'],
 35415: ['GL_COMPRESSED_SRGB_ALPHA_PVRTC_4BPPV1_EXT'],
 35632: ['GL_FRAGMENT_SHADER', 'GL_FRAGMENT_SHADER_ARB'],
 35633: ['GL_VERTEX_SHADER', 'GL_VERTEX_SHADER_ARB'],
 35648: ['GL_PROGRAM_OBJECT_ARB', 'GL_PROGRAM_OBJECT_EXT'],
 35656: ['GL_SHADER_OBJECT_ARB', 'GL_SHADER_OBJECT_EXT'],
 35657: ['GL_MAX_FRAGMENT_UNIFORM_COMPONENTS',
         'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB'],
 35658: ['GL_MAX_VERTEX_UNIFORM_COMPONENTS',
         'GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB'],
 35659: ['GL_MAX_VARYING_FLOATS',
         'GL_MAX_VARYING_COMPONENTS',
         'GL_MAX_VARYING_COMPONENTS_EXT',
         'GL_MAX_VARYING_FLOATS_ARB'],
 35660: ['GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS',
         'GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB'],
 35661: ['GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS',
         'GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB'],
 35662: ['GL_OBJECT_TYPE_ARB'],
 35663: ['GL_SHADER_TYPE', 'GL_OBJECT_SUBTYPE_ARB'],
 35664: ['GL_FLOAT_VEC2', 'GL_FLOAT_VEC2_ARB'],
 35665: ['GL_FLOAT_VEC3', 'GL_FLOAT_VEC3_ARB'],
 35666: ['GL_FLOAT_VEC4', 'GL_FLOAT_VEC4_ARB'],
 35667: ['GL_INT_VEC2', 'GL_INT_VEC2_ARB'],
 35668: ['GL_INT_VEC3', 'GL_INT_VEC3_ARB'],
 35669: ['GL_INT_VEC4', 'GL_INT_VEC4_ARB'],
 35670: ['GL_BOOL', 'GL_BOOL_ARB'],
 35671: ['GL_BOOL_VEC2', 'GL_BOOL_VEC2_ARB'],
 35672: ['GL_BOOL_VEC3', 'GL_BOOL_VEC3_ARB'],
 35673: ['GL_BOOL_VEC4', 'GL_BOOL_VEC4_ARB'],
 35674: ['GL_FLOAT_MAT2', 'GL_FLOAT_MAT2_ARB'],
 35675: ['GL_FLOAT_MAT3', 'GL_FLOAT_MAT3_ARB'],
 35676: ['GL_FLOAT_MAT4', 'GL_FLOAT_MAT4_ARB'],
 35677: ['GL_SAMPLER_1D', 'GL_SAMPLER_1D_ARB'],
 35678: ['GL_SAMPLER_2D', 'GL_SAMPLER_2D_ARB'],
 35679: ['GL_SAMPLER_3D', 'GL_SAMPLER_3D_ARB'],
 35680: ['GL_SAMPLER_CUBE', 'GL_SAMPLER_CUBE_ARB'],
 35681: ['GL_SAMPLER_1D_SHADOW', 'GL_SAMPLER_1D_SHADOW_ARB'],
 35682: ['GL_SAMPLER_2D_SHADOW',
         'GL_SAMPLER_2D_SHADOW_ARB',
         'GL_SAMPLER_2D_SHADOW_EXT'],
 35683: ['GL_SAMPLER_2D_RECT', 'GL_SAMPLER_2D_RECT_ARB'],
 35684: ['GL_SAMPLER_2D_RECT_SHADOW', 'GL_SAMPLER_2D_RECT_SHADOW_ARB'],
 35685: ['GL_FLOAT_MAT2x3'],
 35686: ['GL_FLOAT_MAT2x4'],
 35687: ['GL_FLOAT_MAT3x2'],
 35688: ['GL_FLOAT_MAT3x4'],
 35689: ['GL_FLOAT_MAT4x2'],
 35690: ['GL_FLOAT_MAT4x3'],
 35712: ['GL_DELETE_STATUS', 'GL_OBJECT_DELETE_STATUS_ARB'],
 35713: ['GL_COMPILE_STATUS', 'GL_OBJECT_COMPILE_STATUS_ARB'],
 35714: ['GL_LINK_STATUS', 'GL_OBJECT_LINK_STATUS_ARB'],
 35715: ['GL_VALIDATE_STATUS', 'GL_OBJECT_VALIDATE_STATUS_ARB'],
 35716: ['GL_INFO_LOG_LENGTH', 'GL_OBJECT_INFO_LOG_LENGTH_ARB'],
 35717: ['GL_ATTACHED_SHADERS', 'GL_OBJECT_ATTACHED_OBJECTS_ARB'],
 35718: ['GL_ACTIVE_UNIFORMS', 'GL_OBJECT_ACTIVE_UNIFORMS_ARB'],
 35719: ['GL_ACTIVE_UNIFORM_MAX_LENGTH',
         'GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB'],
 35720: ['GL_SHADER_SOURCE_LENGTH', 'GL_OBJECT_SHADER_SOURCE_LENGTH_ARB'],
 35721: ['GL_ACTIVE_ATTRIBUTES', 'GL_OBJECT_ACTIVE_ATTRIBUTES_ARB'],
 35722: ['GL_ACTIVE_ATTRIBUTE_MAX_LENGTH',
         'GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB'],
 35723: ['GL_FRAGMENT_SHADER_DERIVATIVE_HINT',
         'GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB'],
 35724: ['GL_SHADING_LANGUAGE_VERSION', 'GL_SHADING_LANGUAGE_VERSION_ARB'],
 35725: ['GL_CURRENT_PROGRAM', 'GL_ACTIVE_PROGRAM_EXT'],
 35738: ['GL_IMPLEMENTATION_COLOR_READ_TYPE'],
 35739: ['GL_IMPLEMENTATION_COLOR_READ_FORMAT'],
 35804: ['GL_STATE_RESTORE'],
 35815: ['GL_SAMPLER_EXTERNAL_2D_Y2Y_EXT'],
 35834: ['GL_TEXTURE_PROTECTED_EXT'],
 35840: ['GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG'],
 35841: ['GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG'],
 35842: ['GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG'],
 35843: ['GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG'],
 35844: ['GL_MODULATE_COLOR_IMG'],
 35845: ['GL_RECIP_ADD_SIGNED_ALPHA_IMG'],
 35846: ['GL_TEXTURE_ALPHA_MODULATE_IMG'],
 35847: ['GL_FACTOR_ALPHA_MODULATE_IMG'],
 35848: ['GL_FRAGMENT_ALPHA_MODULATE_IMG'],
 35849: ['GL_ADD_BLEND_IMG'],
 35850: ['GL_SGX_BINARY_IMG'],
 35856: ['GL_TEXTURE_RED_TYPE', 'GL_TEXTURE_RED_TYPE_ARB'],
 35857: ['GL_TEXTURE_GREEN_TYPE', 'GL_TEXTURE_GREEN_TYPE_ARB'],
 35858: ['GL_TEXTURE_BLUE_TYPE', 'GL_TEXTURE_BLUE_TYPE_ARB'],
 35859: ['GL_TEXTURE_ALPHA_TYPE', 'GL_TEXTURE_ALPHA_TYPE_ARB'],
 35860: ['GL_TEXTURE_LUMINANCE_TYPE', 'GL_TEXTURE_LUMINANCE_TYPE_ARB'],
 35861: ['GL_TEXTURE_INTENSITY_TYPE', 'GL_TEXTURE_INTENSITY_TYPE_ARB'],
 35862: ['GL_TEXTURE_DEPTH_TYPE', 'GL_TEXTURE_DEPTH_TYPE_ARB'],
 35863: ['GL_UNSIGNED_NORMALIZED',
         'GL_UNSIGNED_NORMALIZED_ARB',
         'GL_UNSIGNED_NORMALIZED_EXT'],
 35864: ['GL_TEXTURE_1D_ARRAY', 'GL_TEXTURE_1D_ARRAY_EXT'],
 35865: ['GL_PROXY_TEXTURE_1D_ARRAY', 'GL_PROXY_TEXTURE_1D_ARRAY_EXT'],
 35866: ['GL_TEXTURE_2D_ARRAY', 'GL_TEXTURE_2D_ARRAY_EXT'],
 35867: ['GL_PROXY_TEXTURE_2D_ARRAY', 'GL_PROXY_TEXTURE_2D_ARRAY_EXT'],
 35868: ['GL_TEXTURE_BINDING_1D_ARRAY', 'GL_TEXTURE_BINDING_1D_ARRAY_EXT'],
 35869: ['GL_TEXTURE_BINDING_2D_ARRAY', 'GL_TEXTURE_BINDING_2D_ARRAY_EXT'],
 35881: ['GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS',
         'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB',
         'GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT'],
 35882: ['GL_TEXTURE_BUFFER',
         'GL_TEXTURE_BUFFER_ARB',
         'GL_TEXTURE_BUFFER_EXT',
         'GL_TEXTURE_BUFFER_BINDING',
         'GL_TEXTURE_BUFFER_BINDING_EXT'],
 35883: ['GL_MAX_TEXTURE_BUFFER_SIZE',
         'GL_MAX_TEXTURE_BUFFER_SIZE_ARB',
         'GL_MAX_TEXTURE_BUFFER_SIZE_EXT'],
 35884: ['GL_TEXTURE_BINDING_BUFFER',
         'GL_TEXTURE_BINDING_BUFFER_ARB',
         'GL_TEXTURE_BINDING_BUFFER_EXT'],
 35885: ['GL_TEXTURE_BUFFER_DATA_STORE_BINDING',
         'GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB',
         'GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT'],
 35886: ['GL_TEXTURE_BUFFER_FORMAT_ARB', 'GL_TEXTURE_BUFFER_FORMAT_EXT'],
 35887: ['GL_ANY_SAMPLES_PASSED', 'GL_ANY_SAMPLES_PASSED_EXT'],
 35894: ['GL_SAMPLE_SHADING', 'GL_SAMPLE_SHADING_ARB'],
 35895: ['GL_MIN_SAMPLE_SHADING_VALUE', 'GL_MIN_SAMPLE_SHADING_VALUE_ARB'],
 35898: ['GL_R11F_G11F_B10F', 'GL_R11F_G11F_B10F_EXT'],
 35899: ['GL_UNSIGNED_INT_10F_11F_11F_REV',
         'GL_UNSIGNED_INT_10F_11F_11F_REV_EXT'],
 35900: ['GL_RGBA_SIGNED_COMPONENTS_EXT'],
 35901: ['GL_RGB9_E5', 'GL_RGB9_E5_EXT'],
 35902: ['GL_UNSIGNED_INT_5_9_9_9_REV', 'GL_UNSIGNED_INT_5_9_9_9_REV_EXT'],
 35903: ['GL_TEXTURE_SHARED_SIZE', 'GL_TEXTURE_SHARED_SIZE_EXT'],
 35904: ['GL_SRGB', 'GL_SRGB_EXT'],
 35905: ['GL_SRGB8', 'GL_SRGB8_EXT'],
 35906: ['GL_SRGB_ALPHA', 'GL_SRGB_ALPHA_EXT'],
 35907: ['GL_SRGB8_ALPHA8', 'GL_SRGB8_ALPHA8_EXT'],
 35908: ['GL_SLUMINANCE_ALPHA', 'GL_SLUMINANCE_ALPHA_EXT'],
 35909: ['GL_SLUMINANCE8_ALPHA8', 'GL_SLUMINANCE8_ALPHA8_EXT'],
 35910: ['GL_SLUMINANCE', 'GL_SLUMINANCE_EXT'],
 35911: ['GL_SLUMINANCE8', 'GL_SLUMINANCE8_EXT'],
 35912: ['GL_COMPRESSED_SRGB', 'GL_COMPRESSED_SRGB_EXT'],
 35913: ['GL_COMPRESSED_SRGB_ALPHA', 'GL_COMPRESSED_SRGB_ALPHA_EXT'],
 35914: ['GL_COMPRESSED_SLUMINANCE', 'GL_COMPRESSED_SLUMINANCE_EXT'],
 35915: ['GL_COMPRESSED_SLUMINANCE_ALPHA',
         'GL_COMPRESSED_SLUMINANCE_ALPHA_EXT'],
 35916: ['GL_COMPRESSED_SRGB_S3TC_DXT1_EXT'],
 35917: ['GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT'],
 35918: ['GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT'],
 35919: ['GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT'],
 35952: ['GL_COMPRESSED_LUMINANCE_LATC1_EXT'],
 35953: ['GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT'],
 35954: ['GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT'],
 35955: ['GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT'],
 35958: ['GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH',
         'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT'],
 35967: ['GL_TRANSFORM_FEEDBACK_BUFFER_MODE',
         'GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT'],
 35968: ['GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS',
         'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT'],
 35971: ['GL_TRANSFORM_FEEDBACK_VARYINGS',
         'GL_TRANSFORM_FEEDBACK_VARYINGS_EXT'],
 35972: ['GL_TRANSFORM_FEEDBACK_BUFFER_START',
         'GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT'],
 35973: ['GL_TRANSFORM_FEEDBACK_BUFFER_SIZE',
         'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT'],
 35975: ['GL_PRIMITIVES_GENERATED', 'GL_PRIMITIVES_GENERATED_EXT'],
 35976: ['GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN',
         'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT'],
 35977: ['GL_RASTERIZER_DISCARD', 'GL_RASTERIZER_DISCARD_EXT'],
 35978: ['GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS',
         'GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT'],
 35979: ['GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS',
         'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT'],
 35980: ['GL_INTERLEAVED_ATTRIBS', 'GL_INTERLEAVED_ATTRIBS_EXT'],
 35981: ['GL_SEPARATE_ATTRIBS', 'GL_SEPARATE_ATTRIBS_EXT'],
 35982: ['GL_TRANSFORM_FEEDBACK_BUFFER', 'GL_TRANSFORM_FEEDBACK_BUFFER_EXT'],
 35983: ['GL_TRANSFORM_FEEDBACK_BUFFER_BINDING',
         'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT'],
 36000: ['GL_POINT_SPRITE_COORD_ORIGIN'],
 36001: ['GL_LOWER_LEFT', 'GL_LOWER_LEFT_EXT'],
 36002: ['GL_UPPER_LEFT', 'GL_UPPER_LEFT_EXT'],
 36003: ['GL_STENCIL_BACK_REF'],
 36004: ['GL_STENCIL_BACK_VALUE_MASK'],
 36005: ['GL_STENCIL_BACK_WRITEMASK'],
 36006: ['GL_DRAW_FRAMEBUFFER_BINDING',
         'GL_DRAW_FRAMEBUFFER_BINDING_ANGLE',
         'GL_DRAW_FRAMEBUFFER_BINDING_EXT',
         'GL_FRAMEBUFFER_BINDING',
         'GL_FRAMEBUFFER_BINDING_ANGLE',
         'GL_FRAMEBUFFER_BINDING_EXT'],
 36007: ['GL_RENDERBUFFER_BINDING',
         'GL_RENDERBUFFER_BINDING_ANGLE',
         'GL_RENDERBUFFER_BINDING_EXT'],
 36008: ['GL_READ_FRAMEBUFFER',
         'GL_READ_FRAMEBUFFER_ANGLE',
         'GL_READ_FRAMEBUFFER_EXT'],
 36009: ['GL_DRAW_FRAMEBUFFER',
         'GL_DRAW_FRAMEBUFFER_ANGLE',
         'GL_DRAW_FRAMEBUFFER_EXT'],
 36010: ['GL_READ_FRAMEBUFFER_BINDING',
         'GL_READ_FRAMEBUFFER_BINDING_ANGLE',
         'GL_READ_FRAMEBUFFER_BINDING_EXT'],
 36011: ['GL_RENDERBUFFER_SAMPLES',
         'GL_RENDERBUFFER_SAMPLES_ANGLE',
         'GL_RENDERBUFFER_SAMPLES_EXT'],
 36012: ['GL_DEPTH_COMPONENT32F'],
 36013: ['GL_DEPTH32F_STENCIL8'],
 36048: ['GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE',
         'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT'],
 36049: ['GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME',
         'GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT'],
 36050: ['GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL',
         'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT'],
 36051: ['GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE',
         'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT'],
 36052: ['GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT',
         'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER',
         'GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT'],
 36053: ['GL_FRAMEBUFFER_COMPLETE', 'GL_FRAMEBUFFER_COMPLETE_EXT'],
 36054: ['GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT',
         'GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT'],
 36055: ['GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT',
         'GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT'],
 36057: ['GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS',
         'GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT'],
 36058: ['GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT'],
 36059: ['GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER',
         'GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT'],
 36060: ['GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER',
         'GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT'],
 36061: ['GL_FRAMEBUFFER_UNSUPPORTED', 'GL_FRAMEBUFFER_UNSUPPORTED_EXT'],
 36063: ['GL_MAX_COLOR_ATTACHMENTS', 'GL_MAX_COLOR_ATTACHMENTS_EXT'],
 36064: ['GL_COLOR_ATTACHMENT0', 'GL_COLOR_ATTACHMENT0_EXT'],
 36065: ['GL_COLOR_ATTACHMENT1', 'GL_COLOR_ATTACHMENT1_EXT'],
 36066: ['GL_COLOR_ATTACHMENT2', 'GL_COLOR_ATTACHMENT2_EXT'],
 36067: ['GL_COLOR_ATTACHMENT3', 'GL_COLOR_ATTACHMENT3_EXT'],
 36068: ['GL_COLOR_ATTACHMENT4', 'GL_COLOR_ATTACHMENT4_EXT'],
 36069: ['GL_COLOR_ATTACHMENT5', 'GL_COLOR_ATTACHMENT5_EXT'],
 36070: ['GL_COLOR_ATTACHMENT6', 'GL_COLOR_ATTACHMENT6_EXT'],
 36071: ['GL_COLOR_ATTACHMENT7', 'GL_COLOR_ATTACHMENT7_EXT'],
 36072: ['GL_COLOR_ATTACHMENT8', 'GL_COLOR_ATTACHMENT8_EXT'],
 36073: ['GL_COLOR_ATTACHMENT9', 'GL_COLOR_ATTACHMENT9_EXT'],
 36074: ['GL_COLOR_ATTACHMENT10', 'GL_COLOR_ATTACHMENT10_EXT'],
 36075: ['GL_COLOR_ATTACHMENT11', 'GL_COLOR_ATTACHMENT11_EXT'],
 36076: ['GL_COLOR_ATTACHMENT12', 'GL_COLOR_ATTACHMENT12_EXT'],
 36077: ['GL_COLOR_ATTACHMENT13', 'GL_COLOR_ATTACHMENT13_EXT'],
 36078: ['GL_COLOR_ATTACHMENT14', 'GL_COLOR_ATTACHMENT14_EXT'],
 36079: ['GL_COLOR_ATTACHMENT15', 'GL_COLOR_ATTACHMENT15_EXT'],
 36080: ['GL_COLOR_ATTACHMENT16'],
 36081: ['GL_COLOR_ATTACHMENT17'],
 36082: ['GL_COLOR_ATTACHMENT18'],
 36083: ['GL_COLOR_ATTACHMENT19'],
 36084: ['GL_COLOR_ATTACHMENT20'],
 36085: ['GL_COLOR_ATTACHMENT21'],
 36086: ['GL_COLOR_ATTACHMENT22'],
 36087: ['GL_COLOR_ATTACHMENT23'],
 36088: ['GL_COLOR_ATTACHMENT24'],
 36089: ['GL_COLOR_ATTACHMENT25'],
 36090: ['GL_COLOR_ATTACHMENT26'],
 36091: ['GL_COLOR_ATTACHMENT27'],
 36092: ['GL_COLOR_ATTACHMENT28'],
 36093: ['GL_COLOR_ATTACHMENT29'],
 36094: ['GL_COLOR_ATTACHMENT30'],
 36095: ['GL_COLOR_ATTACHMENT31'],
 36096: ['GL_DEPTH_ATTACHMENT', 'GL_DEPTH_ATTACHMENT_EXT'],
 36128: ['GL_STENCIL_ATTACHMENT', 'GL_STENCIL_ATTACHMENT_EXT'],
 36160: ['GL_FRAMEBUFFER', 'GL_FRAMEBUFFER_EXT'],
 36161: ['GL_RENDERBUFFER', 'GL_RENDERBUFFER_EXT'],
 36162: ['GL_RENDERBUFFER_WIDTH', 'GL_RENDERBUFFER_WIDTH_EXT'],
 36163: ['GL_RENDERBUFFER_HEIGHT', 'GL_RENDERBUFFER_HEIGHT_EXT'],
 36164: ['GL_RENDERBUFFER_INTERNAL_FORMAT',
         'GL_RENDERBUFFER_INTERNAL_FORMAT_EXT'],
 36166: ['GL_STENCIL_INDEX1', 'GL_STENCIL_INDEX1_EXT'],
 36167: ['GL_STENCIL_INDEX4', 'GL_STENCIL_INDEX4_EXT'],
 36168: ['GL_STENCIL_INDEX8', 'GL_STENCIL_INDEX8_EXT'],
 36169: ['GL_STENCIL_INDEX16', 'GL_STENCIL_INDEX16_EXT'],
 36176: ['GL_RENDERBUFFER_RED_SIZE', 'GL_RENDERBUFFER_RED_SIZE_EXT'],
 36177: ['GL_RENDERBUFFER_GREEN_SIZE', 'GL_RENDERBUFFER_GREEN_SIZE_EXT'],
 36178: ['GL_RENDERBUFFER_BLUE_SIZE', 'GL_RENDERBUFFER_BLUE_SIZE_EXT'],
 36179: ['GL_RENDERBUFFER_ALPHA_SIZE', 'GL_RENDERBUFFER_ALPHA_SIZE_EXT'],
 36180: ['GL_RENDERBUFFER_DEPTH_SIZE', 'GL_RENDERBUFFER_DEPTH_SIZE_EXT'],
 36181: ['GL_RENDERBUFFER_STENCIL_SIZE', 'GL_RENDERBUFFER_STENCIL_SIZE_EXT'],
 36182: ['GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE',
         'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_ANGLE',
         'GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT'],
 36183: ['GL_MAX_SAMPLES', 'GL_MAX_SAMPLES_ANGLE', 'GL_MAX_SAMPLES_EXT'],
 36194: ['GL_RGB565'],
 36201: ['GL_PRIMITIVE_RESTART_FIXED_INDEX'],
 36202: ['GL_ANY_SAMPLES_PASSED_CONSERVATIVE',
         'GL_ANY_SAMPLES_PASSED_CONSERVATIVE_EXT'],
 36203: ['GL_MAX_ELEMENT_INDEX'],
 36204: ['GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT'],
 36208: ['GL_RGBA32UI', 'GL_RGBA32UI_EXT'],
 36209: ['GL_RGB32UI', 'GL_RGB32UI_EXT'],
 36210: ['GL_ALPHA32UI_EXT'],
 36211: ['GL_INTENSITY32UI_EXT'],
 36212: ['GL_LUMINANCE32UI_EXT'],
 36213: ['GL_LUMINANCE_ALPHA32UI_EXT'],
 36214: ['GL_RGBA16UI', 'GL_RGBA16UI_EXT'],
 36215: ['GL_RGB16UI', 'GL_RGB16UI_EXT'],
 36216: ['GL_ALPHA16UI_EXT'],
 36217: ['GL_INTENSITY16UI_EXT'],
 36218: ['GL_LUMINANCE16UI_EXT'],
 36219: ['GL_LUMINANCE_ALPHA16UI_EXT'],
 36220: ['GL_RGBA8UI', 'GL_RGBA8UI_EXT'],
 36221: ['GL_RGB8UI', 'GL_RGB8UI_EXT'],
 36222: ['GL_ALPHA8UI_EXT'],
 36223: ['GL_INTENSITY8UI_EXT'],
 36224: ['GL_LUMINANCE8UI_EXT'],
 36225: ['GL_LUMINANCE_ALPHA8UI_EXT'],
 36226: ['GL_RGBA32I', 'GL_RGBA32I_EXT'],
 36227: ['GL_RGB32I', 'GL_RGB32I_EXT'],
 36228: ['GL_ALPHA32I_EXT'],
 36229: ['GL_INTENSITY32I_EXT'],
 36230: ['GL_LUMINANCE32I_EXT'],
 36231: ['GL_LUMINANCE_ALPHA32I_EXT'],
 36232: ['GL_RGBA16I', 'GL_RGBA16I_EXT'],
 36233: ['GL_RGB16I', 'GL_RGB16I_EXT'],
 36234: ['GL_ALPHA16I_EXT'],
 36235: ['GL_INTENSITY16I_EXT'],
 36236: ['GL_LUMINANCE16I_EXT'],
 36237: ['GL_LUMINANCE_ALPHA16I_EXT'],
 36238: ['GL_RGBA8I', 'GL_RGBA8I_EXT'],
 36239: ['GL_RGB8I', 'GL_RGB8I_EXT'],
 36240: ['GL_ALPHA8I_EXT'],
 36241: ['GL_INTENSITY8I_EXT'],
 36242: ['GL_LUMINANCE8I_EXT'],
 36243: ['GL_LUMINANCE_ALPHA8I_EXT'],
 36244: ['GL_RED_INTEGER', 'GL_RED_INTEGER_EXT'],
 36245: ['GL_GREEN_INTEGER', 'GL_GREEN_INTEGER_EXT'],
 36246: ['GL_BLUE_INTEGER', 'GL_BLUE_INTEGER_EXT'],
 36247: ['GL_ALPHA_INTEGER', 'GL_ALPHA_INTEGER_EXT'],
 36248: ['GL_RGB_INTEGER', 'GL_RGB_INTEGER_EXT'],
 36249: ['GL_RGBA_INTEGER', 'GL_RGBA_INTEGER_EXT'],
 36250: ['GL_BGR_INTEGER', 'GL_BGR_INTEGER_EXT'],
 36251: ['GL_BGRA_INTEGER', 'GL_BGRA_INTEGER_EXT'],
 36252: ['GL_LUMINANCE_INTEGER_EXT'],
 36253: ['GL_LUMINANCE_ALPHA_INTEGER_EXT'],
 36254: ['GL_RGBA_INTEGER_MODE_EXT'],
 36255: ['GL_INT_2_10_10_10_REV'],
 36263: ['GL_FRAMEBUFFER_ATTACHMENT_LAYERED',
         'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB',
         'GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT'],
 36264: ['GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS',
         'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB',
         'GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT'],
 36265: ['GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB',
         'GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT'],
 36269: ['GL_FLOAT_32_UNSIGNED_INT_24_8_REV'],
 36270: ['GL_SHADER_INCLUDE_ARB'],
 36281: ['GL_FRAMEBUFFER_SRGB', 'GL_FRAMEBUFFER_SRGB_EXT'],
 36282: ['GL_FRAMEBUFFER_SRGB_CAPABLE_EXT'],
 36283: ['GL_COMPRESSED_RED_RGTC1', 'GL_COMPRESSED_RED_RGTC1_EXT'],
 36284: ['GL_COMPRESSED_SIGNED_RED_RGTC1',
         'GL_COMPRESSED_SIGNED_RED_RGTC1_EXT'],
 36285: ['GL_COMPRESSED_RED_GREEN_RGTC2_EXT', 'GL_COMPRESSED_RG_RGTC2'],
 36286: ['GL_COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT',
         'GL_COMPRESSED_SIGNED_RG_RGTC2'],
 36288: ['GL_SAMPLER_1D_ARRAY', 'GL_SAMPLER_1D_ARRAY_EXT'],
 36289: ['GL_SAMPLER_2D_ARRAY', 'GL_SAMPLER_2D_ARRAY_EXT'],
 36290: ['GL_SAMPLER_BUFFER', 'GL_SAMPLER_BUFFER_EXT'],
 36291: ['GL_SAMPLER_1D_ARRAY_SHADOW', 'GL_SAMPLER_1D_ARRAY_SHADOW_EXT'],
 36292: ['GL_SAMPLER_2D_ARRAY_SHADOW', 'GL_SAMPLER_2D_ARRAY_SHADOW_EXT'],
 36293: ['GL_SAMPLER_CUBE_SHADOW', 'GL_SAMPLER_CUBE_SHADOW_EXT'],
 36294: ['GL_UNSIGNED_INT_VEC2', 'GL_UNSIGNED_INT_VEC2_EXT'],
 36295: ['GL_UNSIGNED_INT_VEC3', 'GL_UNSIGNED_INT_VEC3_EXT'],
 36296: ['GL_UNSIGNED_INT_VEC4', 'GL_UNSIGNED_INT_VEC4_EXT'],
 36297: ['GL_INT_SAMPLER_1D', 'GL_INT_SAMPLER_1D_EXT'],
 36298: ['GL_INT_SAMPLER_2D', 'GL_INT_SAMPLER_2D_EXT'],
 36299: ['GL_INT_SAMPLER_3D', 'GL_INT_SAMPLER_3D_EXT'],
 36300: ['GL_INT_SAMPLER_CUBE', 'GL_INT_SAMPLER_CUBE_EXT'],
 36301: ['GL_INT_SAMPLER_2D_RECT', 'GL_INT_SAMPLER_2D_RECT_EXT'],
 36302: ['GL_INT_SAMPLER_1D_ARRAY', 'GL_INT_SAMPLER_1D_ARRAY_EXT'],
 36303: ['GL_INT_SAMPLER_2D_ARRAY', 'GL_INT_SAMPLER_2D_ARRAY_EXT'],
 36304: ['GL_INT_SAMPLER_BUFFER', 'GL_INT_SAMPLER_BUFFER_EXT'],
 36305: ['GL_UNSIGNED_INT_SAMPLER_1D', 'GL_UNSIGNED_INT_SAMPLER_1D_EXT'],
 36306: ['GL_UNSIGNED_INT_SAMPLER_2D', 'GL_UNSIGNED_INT_SAMPLER_2D_EXT'],
 36307: ['GL_UNSIGNED_INT_SAMPLER_3D', 'GL_UNSIGNED_INT_SAMPLER_3D_EXT'],
 36308: ['GL_UNSIGNED_INT_SAMPLER_CUBE', 'GL_UNSIGNED_INT_SAMPLER_CUBE_EXT'],
 36309: ['GL_UNSIGNED_INT_SAMPLER_2D_RECT',
         'GL_UNSIGNED_INT_SAMPLER_2D_RECT_EXT'],
 36310: ['GL_UNSIGNED_INT_SAMPLER_1D_ARRAY',
         'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY_EXT'],
 36311: ['GL_UNSIGNED_INT_SAMPLER_2D_ARRAY',
         'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY_EXT'],
 36312: ['GL_UNSIGNED_INT_SAMPLER_BUFFER',
         'GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT'],
 36313: ['GL_GEOMETRY_SHADER',
         'GL_GEOMETRY_SHADER_ARB',
         'GL_GEOMETRY_SHADER_EXT'],
 36314: ['GL_GEOMETRY_VERTICES_OUT_ARB', 'GL_GEOMETRY_VERTICES_OUT_EXT'],
 36315: ['GL_GEOMETRY_INPUT_TYPE_ARB', 'GL_GEOMETRY_INPUT_TYPE_EXT'],
 36316: ['GL_GEOMETRY_OUTPUT_TYPE_ARB', 'GL_GEOMETRY_OUTPUT_TYPE_EXT'],
 36317: ['GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB',
         'GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT'],
 36318: ['GL_MAX_VERTEX_VARYING_COMPONENTS_ARB',
         'GL_MAX_VERTEX_VARYING_COMPONENTS_EXT'],
 36319: ['GL_MAX_GEOMETRY_UNIFORM_COMPONENTS',
         'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB',
         'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT'],
 36320: ['GL_MAX_GEOMETRY_OUTPUT_VERTICES',
         'GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB',
         'GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT'],
 36321: ['GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS',
         'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB',
         'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT'],
 36322: ['GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT'],
 36323: ['GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT'],
 36324: ['GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT'],
 36325: ['GL_ACTIVE_SUBROUTINES'],
 36326: ['GL_ACTIVE_SUBROUTINE_UNIFORMS'],
 36327: ['GL_MAX_SUBROUTINES'],
 36328: ['GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS'],
 36329: ['GL_NAMED_STRING_LENGTH_ARB'],
 36330: ['GL_NAMED_STRING_TYPE_ARB'],
 36333: ['GL_MAX_BINDABLE_UNIFORM_SIZE_EXT'],
 36334: ['GL_UNIFORM_BUFFER_EXT'],
 36335: ['GL_UNIFORM_BUFFER_BINDING_EXT'],
 36336: ['GL_LOW_FLOAT'],
 36337: ['GL_MEDIUM_FLOAT'],
 36338: ['GL_HIGH_FLOAT'],
 36339: ['GL_LOW_INT'],
 36340: ['GL_MEDIUM_INT'],
 36341: ['GL_HIGH_INT'],
 36344: ['GL_SHADER_BINARY_FORMATS'],
 36345: ['GL_NUM_SHADER_BINARY_FORMATS'],
 36346: ['GL_SHADER_COMPILER'],
 36347: ['GL_MAX_VERTEX_UNIFORM_VECTORS'],
 36348: ['GL_MAX_VARYING_VECTORS'],
 36349: ['GL_MAX_FRAGMENT_UNIFORM_VECTORS'],
 36371: ['GL_QUERY_WAIT'],
 36372: ['GL_QUERY_NO_WAIT'],
 36373: ['GL_QUERY_BY_REGION_WAIT'],
 36374: ['GL_QUERY_BY_REGION_NO_WAIT'],
 36375: ['GL_QUERY_WAIT_INVERTED'],
 36376: ['GL_QUERY_NO_WAIT_INVERTED'],
 36377: ['GL_QUERY_BY_REGION_WAIT_INVERTED'],
 36378: ['GL_QUERY_BY_REGION_NO_WAIT_INVERTED'],
 36379: ['GL_POLYGON_OFFSET_CLAMP', 'GL_POLYGON_OFFSET_CLAMP_EXT'],
 36382: ['GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS',
         'GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS_EXT'],
 36383: ['GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS',
         'GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT'],
 36386: ['GL_TRANSFORM_FEEDBACK'],
 36387: ['GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED', 'GL_TRANSFORM_FEEDBACK_PAUSED'],
 36388: ['GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE', 'GL_TRANSFORM_FEEDBACK_ACTIVE'],
 36389: ['GL_TRANSFORM_FEEDBACK_BINDING'],
 36392: ['GL_TIMESTAMP', 'GL_TIMESTAMP_EXT'],
 36397: ['GL_PROGRAM_MATRIX_EXT'],
 36398: ['GL_TRANSPOSE_PROGRAM_MATRIX_EXT'],
 36399: ['GL_PROGRAM_MATRIX_STACK_DEPTH_EXT'],
 36418: ['GL_TEXTURE_SWIZZLE_R', 'GL_TEXTURE_SWIZZLE_R_EXT'],
 36419: ['GL_TEXTURE_SWIZZLE_G', 'GL_TEXTURE_SWIZZLE_G_EXT'],
 36420: ['GL_TEXTURE_SWIZZLE_B', 'GL_TEXTURE_SWIZZLE_B_EXT'],
 36421: ['GL_TEXTURE_SWIZZLE_A', 'GL_TEXTURE_SWIZZLE_A_EXT'],
 36422: ['GL_TEXTURE_SWIZZLE_RGBA', 'GL_TEXTURE_SWIZZLE_RGBA_EXT'],
 36423: ['GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS'],
 36424: ['GL_ACTIVE_SUBROUTINE_MAX_LENGTH'],
 36425: ['GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH'],
 36426: ['GL_NUM_COMPATIBLE_SUBROUTINES'],
 36427: ['GL_COMPATIBLE_SUBROUTINES'],
 36428: ['GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION',
         'GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION_EXT'],
 36429: ['GL_FIRST_VERTEX_CONVENTION', 'GL_FIRST_VERTEX_CONVENTION_EXT'],
 36430: ['GL_LAST_VERTEX_CONVENTION', 'GL_LAST_VERTEX_CONVENTION_EXT'],
 36431: ['GL_PROVOKING_VERTEX', 'GL_PROVOKING_VERTEX_EXT'],
 36432: ['GL_SAMPLE_POSITION', 'GL_SAMPLE_LOCATION_ARB'],
 36433: ['GL_SAMPLE_MASK'],
 36434: ['GL_SAMPLE_MASK_VALUE'],
 36441: ['GL_MAX_SAMPLE_MASK_WORDS'],
 36442: ['GL_MAX_GEOMETRY_SHADER_INVOCATIONS',
         'GL_MAX_GEOMETRY_SHADER_INVOCATIONS_EXT'],
 36443: ['GL_MIN_FRAGMENT_INTERPOLATION_OFFSET'],
 36444: ['GL_MAX_FRAGMENT_INTERPOLATION_OFFSET'],
 36445: ['GL_FRAGMENT_INTERPOLATION_OFFSET_BITS'],
 36446: ['GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET',
         'GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB'],
 36447: ['GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET',
         'GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB'],
 36464: ['GL_MAX_TRANSFORM_FEEDBACK_BUFFERS'],
 36465: ['GL_MAX_VERTEX_STREAMS'],
 36466: ['GL_PATCH_VERTICES', 'GL_PATCH_VERTICES_EXT'],
 36467: ['GL_PATCH_DEFAULT_INNER_LEVEL', 'GL_PATCH_DEFAULT_INNER_LEVEL_EXT'],
 36468: ['GL_PATCH_DEFAULT_OUTER_LEVEL', 'GL_PATCH_DEFAULT_OUTER_LEVEL_EXT'],
 36469: ['GL_TESS_CONTROL_OUTPUT_VERTICES',
         'GL_TESS_CONTROL_OUTPUT_VERTICES_EXT'],
 36470: ['GL_TESS_GEN_MODE', 'GL_TESS_GEN_MODE_EXT'],
 36471: ['GL_TESS_GEN_SPACING', 'GL_TESS_GEN_SPACING_EXT'],
 36472: ['GL_TESS_GEN_VERTEX_ORDER', 'GL_TESS_GEN_VERTEX_ORDER_EXT'],
 36473: ['GL_TESS_GEN_POINT_MODE', 'GL_TESS_GEN_POINT_MODE_EXT'],
 36474: ['GL_ISOLINES', 'GL_ISOLINES_EXT'],
 36475: ['GL_FRACTIONAL_ODD', 'GL_FRACTIONAL_ODD_EXT'],
 36476: ['GL_FRACTIONAL_EVEN', 'GL_FRACTIONAL_EVEN_EXT'],
 36477: ['GL_MAX_PATCH_VERTICES', 'GL_MAX_PATCH_VERTICES_EXT'],
 36478: ['GL_MAX_TESS_GEN_LEVEL', 'GL_MAX_TESS_GEN_LEVEL_EXT'],
 36479: ['GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS',
         'GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS_EXT'],
 36480: ['GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS',
         'GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT'],
 36481: ['GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS',
         'GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS_EXT'],
 36482: ['GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS',
         'GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS_EXT'],
 36483: ['GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS',
         'GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS_EXT'],
 36484: ['GL_MAX_TESS_PATCH_COMPONENTS', 'GL_MAX_TESS_PATCH_COMPONENTS_EXT'],
 36485: ['GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS',
         'GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS_EXT'],
 36486: ['GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS',
         'GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS_EXT'],
 36487: ['GL_TESS_EVALUATION_SHADER', 'GL_TESS_EVALUATION_SHADER_EXT'],
 36488: ['GL_TESS_CONTROL_SHADER', 'GL_TESS_CONTROL_SHADER_EXT'],
 36489: ['GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS',
         'GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS_EXT'],
 36490: ['GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS',
         'GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS_EXT'],
 36492: ['GL_COMPRESSED_RGBA_BPTC_UNORM',
         'GL_COMPRESSED_RGBA_BPTC_UNORM_ARB',
         'GL_COMPRESSED_RGBA_BPTC_UNORM_EXT'],
 36493: ['GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM',
         'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB',
         'GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT'],
 36494: ['GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT',
         'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB',
         'GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT'],
 36495: ['GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT',
         'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB',
         'GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT'],
 36624: ['GL_INCLUSIVE_EXT'],
 36625: ['GL_EXCLUSIVE_EXT'],
 36626: ['GL_WINDOW_RECTANGLE_EXT'],
 36627: ['GL_WINDOW_RECTANGLE_MODE_EXT'],
 36628: ['GL_MAX_WINDOW_RECTANGLES_EXT'],
 36629: ['GL_NUM_WINDOW_RECTANGLES_EXT'],
 36662: ['GL_COPY_READ_BUFFER', 'GL_COPY_READ_BUFFER_BINDING'],
 36663: ['GL_COPY_WRITE_BUFFER', 'GL_COPY_WRITE_BUFFER_BINDING'],
 36664: ['GL_MAX_IMAGE_UNITS', 'GL_MAX_IMAGE_UNITS_EXT'],
 36665: ['GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS',
         'GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS_EXT',
         'GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES'],
 36666: ['GL_IMAGE_BINDING_NAME', 'GL_IMAGE_BINDING_NAME_EXT'],
 36667: ['GL_IMAGE_BINDING_LEVEL', 'GL_IMAGE_BINDING_LEVEL_EXT'],
 36668: ['GL_IMAGE_BINDING_LAYERED', 'GL_IMAGE_BINDING_LAYERED_EXT'],
 36669: ['GL_IMAGE_BINDING_LAYER', 'GL_IMAGE_BINDING_LAYER_EXT'],
 36670: ['GL_IMAGE_BINDING_ACCESS', 'GL_IMAGE_BINDING_ACCESS_EXT'],
 36671: ['GL_DRAW_INDIRECT_BUFFER'],
 36675: ['GL_DRAW_INDIRECT_BUFFER_BINDING'],
 36678: ['GL_DOUBLE_MAT2', 'GL_DOUBLE_MAT2_EXT'],
 36679: ['GL_DOUBLE_MAT3', 'GL_DOUBLE_MAT3_EXT'],
 36680: ['GL_DOUBLE_MAT4', 'GL_DOUBLE_MAT4_EXT'],
 36681: ['GL_DOUBLE_MAT2x3', 'GL_DOUBLE_MAT2x3_EXT'],
 36682: ['GL_DOUBLE_MAT2x4', 'GL_DOUBLE_MAT2x4_EXT'],
 36683: ['GL_DOUBLE_MAT3x2', 'GL_DOUBLE_MAT3x2_EXT'],
 36684: ['GL_DOUBLE_MAT3x4', 'GL_DOUBLE_MAT3x4_EXT'],
 36685: ['GL_DOUBLE_MAT4x2', 'GL_DOUBLE_MAT4x2_EXT'],
 36686: ['GL_DOUBLE_MAT4x3', 'GL_DOUBLE_MAT4x3_EXT'],
 36687: ['GL_VERTEX_BINDING_BUFFER'],
 36704: ['GL_MALI_SHADER_BINARY_ARM'],
 36705: ['GL_MALI_PROGRAM_BINARY_ARM'],
 36707: ['GL_MAX_SHADER_PIXEL_LOCAL_STORAGE_FAST_SIZE_EXT'],
 36708: ['GL_SHADER_PIXEL_LOCAL_STORAGE_EXT'],
 36709: ['GL_FETCH_PER_SAMPLE_ARM'],
 36710: ['GL_FRAGMENT_SHADER_FRAMEBUFFER_FETCH_MRT_ARM'],
 36711: ['GL_MAX_SHADER_PIXEL_LOCAL_STORAGE_SIZE_EXT'],
 36713: ['GL_TEXTURE_ASTC_DECODE_PRECISION_EXT'],
 36752: ['GL_RED_SNORM'],
 36753: ['GL_RG_SNORM'],
 36754: ['GL_RGB_SNORM'],
 36755: ['GL_RGBA_SNORM'],
 36756: ['GL_R8_SNORM'],
 36757: ['GL_RG8_SNORM'],
 36758: ['GL_RGB8_SNORM'],
 36759: ['GL_RGBA8_SNORM'],
 36760: ['GL_R16_SNORM', 'GL_R16_SNORM_EXT'],
 36761: ['GL_RG16_SNORM', 'GL_RG16_SNORM_EXT'],
 36762: ['GL_RGB16_SNORM', 'GL_RGB16_SNORM_EXT'],
 36763: ['GL_RGBA16_SNORM', 'GL_RGBA16_SNORM_EXT'],
 36764: ['GL_SIGNED_NORMALIZED'],
 36765: ['GL_PRIMITIVE_RESTART'],
 36766: ['GL_PRIMITIVE_RESTART_INDEX'],
 36767: ['GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB'],
 36795: ['GL_GPU_DISJOINT_EXT'],
 36797: ['GL_SR8_EXT'],
 36798: ['GL_SRG8_EXT'],
 36799: ['GL_TEXTURE_FORMAT_SRGB_OVERRIDE_EXT'],
 36804: ['GL_SHADER_BINARY_VIV'],
 36841: ['GL_INT64_VEC2_ARB'],
 36842: ['GL_INT64_VEC3_ARB'],
 36843: ['GL_INT64_VEC4_ARB'],
 36853: ['GL_UNSIGNED_INT64_VEC2_ARB'],
 36854: ['GL_UNSIGNED_INT64_VEC3_ARB'],
 36855: ['GL_UNSIGNED_INT64_VEC4_ARB'],
 36860: ['GL_DOUBLE_VEC2', 'GL_DOUBLE_VEC2_EXT'],
 36861: ['GL_DOUBLE_VEC3', 'GL_DOUBLE_VEC3_EXT'],
 36862: ['GL_DOUBLE_VEC4', 'GL_DOUBLE_VEC4_EXT'],
 36873: ['GL_TEXTURE_CUBE_MAP_ARRAY',
         'GL_TEXTURE_CUBE_MAP_ARRAY_ARB',
         'GL_TEXTURE_CUBE_MAP_ARRAY_EXT'],
 36874: ['GL_TEXTURE_BINDING_CUBE_MAP_ARRAY',
         'GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB',
         'GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_EXT'],
 36875: ['GL_PROXY_TEXTURE_CUBE_MAP_ARRAY',
         'GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB'],
 36876: ['GL_SAMPLER_CUBE_MAP_ARRAY',
         'GL_SAMPLER_CUBE_MAP_ARRAY_ARB',
         'GL_SAMPLER_CUBE_MAP_ARRAY_EXT'],
 36877: ['GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW',
         'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB',
         'GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_EXT'],
 36878: ['GL_INT_SAMPLER_CUBE_MAP_ARRAY',
         'GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB',
         'GL_INT_SAMPLER_CUBE_MAP_ARRAY_EXT'],
 36879: ['GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY',
         'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB',
         'GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_EXT'],
 36880: ['GL_ALPHA_SNORM'],
 36881: ['GL_LUMINANCE_SNORM'],
 36882: ['GL_LUMINANCE_ALPHA_SNORM'],
 36883: ['GL_INTENSITY_SNORM'],
 36884: ['GL_ALPHA8_SNORM'],
 36885: ['GL_LUMINANCE8_SNORM'],
 36886: ['GL_LUMINANCE8_ALPHA8_SNORM'],
 36887: ['GL_INTENSITY8_SNORM'],
 36888: ['GL_ALPHA16_SNORM'],
 36889: ['GL_LUMINANCE16_SNORM'],
 36890: ['GL_LUMINANCE16_ALPHA16_SNORM'],
 36891: ['GL_INTENSITY16_SNORM'],
 36935: ['GL_GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX'],
 36936: ['GL_GPU_MEMORY_INFO_TOTAL_AVAILABLE_MEMORY_NVX'],
 36937: ['GL_GPU_MEMORY_INFO_CURRENT_AVAILABLE_VIDMEM_NVX'],
 36938: ['GL_GPU_MEMORY_INFO_EVICTION_COUNT_NVX'],
 36939: ['GL_GPU_MEMORY_INFO_EVICTED_MEMORY_NVX'],
 36940: ['GL_IMAGE_1D', 'GL_IMAGE_1D_EXT'],
 36941: ['GL_IMAGE_2D', 'GL_IMAGE_2D_EXT'],
 36942: ['GL_IMAGE_3D', 'GL_IMAGE_3D_EXT'],
 36943: ['GL_IMAGE_2D_RECT', 'GL_IMAGE_2D_RECT_EXT'],
 36944: ['GL_IMAGE_CUBE', 'GL_IMAGE_CUBE_EXT'],
 36945: ['GL_IMAGE_BUFFER', 'GL_IMAGE_BUFFER_EXT'],
 36946: ['GL_IMAGE_1D_ARRAY', 'GL_IMAGE_1D_ARRAY_EXT'],
 36947: ['GL_IMAGE_2D_ARRAY', 'GL_IMAGE_2D_ARRAY_EXT'],
 36948: ['GL_IMAGE_CUBE_MAP_ARRAY', 'GL_IMAGE_CUBE_MAP_ARRAY_EXT'],
 36949: ['GL_IMAGE_2D_MULTISAMPLE', 'GL_IMAGE_2D_MULTISAMPLE_EXT'],
 36950: ['GL_IMAGE_2D_MULTISAMPLE_ARRAY', 'GL_IMAGE_2D_MULTISAMPLE_ARRAY_EXT'],
 36951: ['GL_INT_IMAGE_1D', 'GL_INT_IMAGE_1D_EXT'],
 36952: ['GL_INT_IMAGE_2D', 'GL_INT_IMAGE_2D_EXT'],
 36953: ['GL_INT_IMAGE_3D', 'GL_INT_IMAGE_3D_EXT'],
 36954: ['GL_INT_IMAGE_2D_RECT', 'GL_INT_IMAGE_2D_RECT_EXT'],
 36955: ['GL_INT_IMAGE_CUBE', 'GL_INT_IMAGE_CUBE_EXT'],
 36956: ['GL_INT_IMAGE_BUFFER', 'GL_INT_IMAGE_BUFFER_EXT'],
 36957: ['GL_INT_IMAGE_1D_ARRAY', 'GL_INT_IMAGE_1D_ARRAY_EXT'],
 36958: ['GL_INT_IMAGE_2D_ARRAY', 'GL_INT_IMAGE_2D_ARRAY_EXT'],
 36959: ['GL_INT_IMAGE_CUBE_MAP_ARRAY', 'GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT'],
 36960: ['GL_INT_IMAGE_2D_MULTISAMPLE', 'GL_INT_IMAGE_2D_MULTISAMPLE_EXT'],
 36961: ['GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY',
         'GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT'],
 36962: ['GL_UNSIGNED_INT_IMAGE_1D', 'GL_UNSIGNED_INT_IMAGE_1D_EXT'],
 36963: ['GL_UNSIGNED_INT_IMAGE_2D', 'GL_UNSIGNED_INT_IMAGE_2D_EXT'],
 36964: ['GL_UNSIGNED_INT_IMAGE_3D', 'GL_UNSIGNED_INT_IMAGE_3D_EXT'],
 36965: ['GL_UNSIGNED_INT_IMAGE_2D_RECT', 'GL_UNSIGNED_INT_IMAGE_2D_RECT_EXT'],
 36966: ['GL_UNSIGNED_INT_IMAGE_CUBE', 'GL_UNSIGNED_INT_IMAGE_CUBE_EXT'],
 36967: ['GL_UNSIGNED_INT_IMAGE_BUFFER', 'GL_UNSIGNED_INT_IMAGE_BUFFER_EXT'],
 36968: ['GL_UNSIGNED_INT_IMAGE_1D_ARRAY',
         'GL_UNSIGNED_INT_IMAGE_1D_ARRAY_EXT'],
 36969: ['GL_UNSIGNED_INT_IMAGE_2D_ARRAY',
         'GL_UNSIGNED_INT_IMAGE_2D_ARRAY_EXT'],
 36970: ['GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY',
         'GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT'],
 36971: ['GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE',
         'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_EXT'],
 36972: ['GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY',
         'GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT'],
 36973: ['GL_MAX_IMAGE_SAMPLES', 'GL_MAX_IMAGE_SAMPLES_EXT'],
 36974: ['GL_IMAGE_BINDING_FORMAT', 'GL_IMAGE_BINDING_FORMAT_EXT'],
 36975: ['GL_RGB10_A2UI'],
 37050: ['GL_SCALED_RESOLVE_FASTEST_EXT'],
 37051: ['GL_SCALED_RESOLVE_NICEST_EXT'],
 37052: ['GL_MIN_MAP_BUFFER_ALIGNMENT'],
 37063: ['GL_IMAGE_FORMAT_COMPATIBILITY_TYPE'],
 37064: ['GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE'],
 37065: ['GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS'],
 37066: ['GL_MAX_VERTEX_IMAGE_UNIFORMS'],
 37067: ['GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS',
         'GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS_EXT'],
 37068: ['GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS',
         'GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS_EXT'],
 37069: ['GL_MAX_GEOMETRY_IMAGE_UNIFORMS',
         'GL_MAX_GEOMETRY_IMAGE_UNIFORMS_EXT'],
 37070: ['GL_MAX_FRAGMENT_IMAGE_UNIFORMS'],
 37071: ['GL_MAX_COMBINED_IMAGE_UNIFORMS'],
 37074: ['GL_SHADER_STORAGE_BUFFER'],
 37075: ['GL_SHADER_STORAGE_BUFFER_BINDING'],
 37076: ['GL_SHADER_STORAGE_BUFFER_START'],
 37077: ['GL_SHADER_STORAGE_BUFFER_SIZE'],
 37078: ['GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS'],
 37079: ['GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS',
         'GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS_EXT'],
 37080: ['GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS',
         'GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS_EXT'],
 37081: ['GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS',
         'GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS_EXT'],
 37082: ['GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS'],
 37083: ['GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS'],
 37084: ['GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS'],
 37085: ['GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS'],
 37086: ['GL_MAX_SHADER_STORAGE_BLOCK_SIZE'],
 37087: ['GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT'],
 37089: ['GL_SYNC_X11_FENCE_EXT'],
 37098: ['GL_DEPTH_STENCIL_TEXTURE_MODE'],
 37099: ['GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS',
         'GL_MAX_COMPUTE_FIXED_GROUP_INVOCATIONS_ARB'],
 37100: ['GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER'],
 37101: ['GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER'],
 37102: ['GL_DISPATCH_INDIRECT_BUFFER'],
 37103: ['GL_DISPATCH_INDIRECT_BUFFER_BINDING'],
 37104: ['GL_COLOR_ATTACHMENT_EXT'],
 37105: ['GL_MULTIVIEW_EXT'],
 37106: ['GL_MAX_MULTIVIEW_BUFFERS_EXT'],
 37107: ['GL_CONTEXT_ROBUST_ACCESS', 'GL_CONTEXT_ROBUST_ACCESS_EXT'],
 37120: ['GL_TEXTURE_2D_MULTISAMPLE'],
 37121: ['GL_PROXY_TEXTURE_2D_MULTISAMPLE'],
 37122: ['GL_TEXTURE_2D_MULTISAMPLE_ARRAY'],
 37123: ['GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY'],
 37124: ['GL_TEXTURE_BINDING_2D_MULTISAMPLE'],
 37125: ['GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY'],
 37126: ['GL_TEXTURE_SAMPLES'],
 37127: ['GL_TEXTURE_FIXED_SAMPLE_LOCATIONS'],
 37128: ['GL_SAMPLER_2D_MULTISAMPLE'],
 37129: ['GL_INT_SAMPLER_2D_MULTISAMPLE'],
 37130: ['GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE'],
 37131: ['GL_SAMPLER_2D_MULTISAMPLE_ARRAY'],
 37132: ['GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY'],
 37133: ['GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY'],
 37134: ['GL_MAX_COLOR_TEXTURE_SAMPLES'],
 37135: ['GL_MAX_DEPTH_TEXTURE_SAMPLES'],
 37136: ['GL_MAX_INTEGER_SAMPLES'],
 37137: ['GL_MAX_SERVER_WAIT_TIMEOUT'],
 37138: ['GL_OBJECT_TYPE'],
 37139: ['GL_SYNC_CONDITION'],
 37140: ['GL_SYNC_STATUS'],
 37141: ['GL_SYNC_FLAGS'],
 37142: ['GL_SYNC_FENCE'],
 37143: ['GL_SYNC_GPU_COMMANDS_COMPLETE'],
 37144: ['GL_UNSIGNALED'],
 37145: ['GL_SIGNALED'],
 37146: ['GL_ALREADY_SIGNALED'],
 37147: ['GL_TIMEOUT_EXPIRED'],
 37148: ['GL_CONDITION_SATISFIED'],
 37149: ['GL_WAIT_FAILED'],
 37151: ['GL_BUFFER_ACCESS_FLAGS'],
 37152: ['GL_BUFFER_MAP_LENGTH'],
 37153: ['GL_BUFFER_MAP_OFFSET'],
 37154: ['GL_MAX_VERTEX_OUTPUT_COMPONENTS'],
 37155: ['GL_MAX_GEOMETRY_INPUT_COMPONENTS',
         'GL_MAX_GEOMETRY_INPUT_COMPONENTS_EXT'],
 37156: ['GL_MAX_GEOMETRY_OUTPUT_COMPONENTS',
         'GL_MAX_GEOMETRY_OUTPUT_COMPONENTS_EXT'],
 37157: ['GL_MAX_FRAGMENT_INPUT_COMPONENTS'],
 37158: ['GL_CONTEXT_PROFILE_MASK'],
 37159: ['GL_UNPACK_COMPRESSED_BLOCK_WIDTH'],
 37160: ['GL_UNPACK_COMPRESSED_BLOCK_HEIGHT'],
 37161: ['GL_UNPACK_COMPRESSED_BLOCK_DEPTH'],
 37162: ['GL_UNPACK_COMPRESSED_BLOCK_SIZE'],
 37163: ['GL_PACK_COMPRESSED_BLOCK_WIDTH'],
 37164: ['GL_PACK_COMPRESSED_BLOCK_HEIGHT'],
 37165: ['GL_PACK_COMPRESSED_BLOCK_DEPTH'],
 37166: ['GL_PACK_COMPRESSED_BLOCK_SIZE'],
 37167: ['GL_TEXTURE_IMMUTABLE_FORMAT', 'GL_TEXTURE_IMMUTABLE_FORMAT_EXT'],
 37168: ['GL_SGX_PROGRAM_BINARY_IMG'],
 37171: ['GL_RENDERBUFFER_SAMPLES_IMG'],
 37172: ['GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG'],
 37173: ['GL_MAX_SAMPLES_IMG'],
 37174: ['GL_TEXTURE_SAMPLES_IMG'],
 37175: ['GL_COMPRESSED_RGBA_PVRTC_2BPPV2_IMG'],
 37176: ['GL_COMPRESSED_RGBA_PVRTC_4BPPV2_IMG'],
 37177: ['GL_CUBIC_IMG'],
 37178: ['GL_CUBIC_MIPMAP_NEAREST_IMG'],
 37179: ['GL_CUBIC_MIPMAP_LINEAR_IMG'],
 37180: ['GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_AND_DOWNSAMPLE_IMG'],
 37181: ['GL_NUM_DOWNSAMPLE_SCALES_IMG'],
 37182: ['GL_DOWNSAMPLE_SCALES_IMG'],
 37183: ['GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SCALE_IMG'],
 37187: ['GL_MAX_DEBUG_MESSAGE_LENGTH', 'GL_MAX_DEBUG_MESSAGE_LENGTH_ARB'],
 37188: ['GL_MAX_DEBUG_LOGGED_MESSAGES', 'GL_MAX_DEBUG_LOGGED_MESSAGES_ARB'],
 37189: ['GL_DEBUG_LOGGED_MESSAGES', 'GL_DEBUG_LOGGED_MESSAGES_ARB'],
 37190: ['GL_DEBUG_SEVERITY_HIGH', 'GL_DEBUG_SEVERITY_HIGH_ARB'],
 37191: ['GL_DEBUG_SEVERITY_MEDIUM', 'GL_DEBUG_SEVERITY_MEDIUM_ARB'],
 37192: ['GL_DEBUG_SEVERITY_LOW', 'GL_DEBUG_SEVERITY_LOW_ARB'],
 37201: ['GL_BUFFER_OBJECT_EXT'],
 37203: ['GL_QUERY_OBJECT_EXT'],
 37204: ['GL_VERTEX_ARRAY_OBJECT_EXT'],
 37266: ['GL_QUERY_BUFFER'],
 37267: ['GL_QUERY_BUFFER_BINDING'],
 37268: ['GL_QUERY_RESULT_NO_WAIT'],
 37269: ['GL_VIRTUAL_PAGE_SIZE_X_ARB', 'GL_VIRTUAL_PAGE_SIZE_X_EXT'],
 37270: ['GL_VIRTUAL_PAGE_SIZE_Y_ARB', 'GL_VIRTUAL_PAGE_SIZE_Y_EXT'],
 37271: ['GL_VIRTUAL_PAGE_SIZE_Z_ARB', 'GL_VIRTUAL_PAGE_SIZE_Z_EXT'],
 37272: ['GL_MAX_SPARSE_TEXTURE_SIZE_ARB', 'GL_MAX_SPARSE_TEXTURE_SIZE_EXT'],
 37273: ['GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB',
         'GL_MAX_SPARSE_3D_TEXTURE_SIZE_EXT'],
 37274: ['GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS',
         'GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB',
         'GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_EXT'],
 37277: ['GL_TEXTURE_BUFFER_OFFSET', 'GL_TEXTURE_BUFFER_OFFSET_EXT'],
 37278: ['GL_TEXTURE_BUFFER_SIZE', 'GL_TEXTURE_BUFFER_SIZE_EXT'],
 37279: ['GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT',
         'GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT_EXT'],
 37286: ['GL_TEXTURE_SPARSE_ARB', 'GL_TEXTURE_SPARSE_EXT'],
 37287: ['GL_VIRTUAL_PAGE_SIZE_INDEX_ARB', 'GL_VIRTUAL_PAGE_SIZE_INDEX_EXT'],
 37288: ['GL_NUM_VIRTUAL_PAGE_SIZES_ARB', 'GL_NUM_VIRTUAL_PAGE_SIZES_EXT'],
 37289: ['GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB',
         'GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_EXT'],
 37290: ['GL_NUM_SPARSE_LEVELS_ARB', 'GL_NUM_SPARSE_LEVELS_EXT'],
 37296: ['GL_MAX_SHADER_COMPILER_THREADS_ARB'],
 37297: ['GL_COMPLETION_STATUS_ARB'],
 37305: ['GL_COMPUTE_SHADER'],
 37307: ['GL_MAX_COMPUTE_UNIFORM_BLOCKS'],
 37308: ['GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS'],
 37309: ['GL_MAX_COMPUTE_IMAGE_UNIFORMS'],
 37310: ['GL_MAX_COMPUTE_WORK_GROUP_COUNT'],
 37311: ['GL_MAX_COMPUTE_WORK_GROUP_SIZE',
         'GL_MAX_COMPUTE_FIXED_GROUP_SIZE_ARB'],
 37440: ['GL_UNPACK_FLIP_Y_WEBGL'],
 37441: ['GL_UNPACK_PREMULTIPLY_ALPHA_WEBGL'],
 37442: ['GL_CONTEXT_LOST_WEBGL'],
 37443: ['GL_UNPACK_COLORSPACE_CONVERSION_WEBGL'],
 37444: ['GL_BROWSER_DEFAULT_WEBGL'],
 37456: ['GL_SHADER_BINARY_DMP'],
 37457: ['GL_SMAPHS30_PROGRAM_BINARY_DMP'],
 37458: ['GL_SMAPHS_PROGRAM_BINARY_DMP'],
 37459: ['GL_DMP_PROGRAM_BINARY_DMP'],
 37472: ['GL_GCCSO_SHADER_BINARY_FJ'],
 37488: ['GL_COMPRESSED_R11_EAC'],
 37489: ['GL_COMPRESSED_SIGNED_R11_EAC'],
 37490: ['GL_COMPRESSED_RG11_EAC'],
 37491: ['GL_COMPRESSED_SIGNED_RG11_EAC'],
 37492: ['GL_COMPRESSED_RGB8_ETC2'],
 37493: ['GL_COMPRESSED_SRGB8_ETC2'],
 37494: ['GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2'],
 37495: ['GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2'],
 37496: ['GL_COMPRESSED_RGBA8_ETC2_EAC'],
 37497: ['GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC'],
 37524: ['GL_MULTIPLY'],
 37525: ['GL_SCREEN'],
 37526: ['GL_OVERLAY'],
 37527: ['GL_DARKEN'],
 37528: ['GL_LIGHTEN'],
 37529: ['GL_COLORDODGE'],
 37530: ['GL_COLORBURN'],
 37531: ['GL_HARDLIGHT'],
 37532: ['GL_SOFTLIGHT'],
 37534: ['GL_DIFFERENCE'],
 37536: ['GL_EXCLUSION'],
 37549: ['GL_HSL_HUE'],
 37550: ['GL_HSL_SATURATION'],
 37551: ['GL_HSL_COLOR'],
 37552: ['GL_HSL_LUMINOSITY'],
 37562: ['GL_MAX_LGPU_GPUS_NVX'],
 37566: ['GL_PRIMITIVE_BOUNDING_BOX_ARB',
         'GL_PRIMITIVE_BOUNDING_BOX',
         'GL_PRIMITIVE_BOUNDING_BOX_EXT'],
 37568: ['GL_ATOMIC_COUNTER_BUFFER'],
 37569: ['GL_ATOMIC_COUNTER_BUFFER_BINDING'],
 37570: ['GL_ATOMIC_COUNTER_BUFFER_START'],
 37571: ['GL_ATOMIC_COUNTER_BUFFER_SIZE'],
 37572: ['GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE'],
 37573: ['GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS'],
 37574: ['GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES'],
 37575: ['GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER'],
 37576: ['GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER'],
 37577: ['GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER'],
 37578: ['GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER'],
 37579: ['GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER'],
 37580: ['GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS'],
 37581: ['GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS',
         'GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS_EXT'],
 37582: ['GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS',
         'GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS_EXT'],
 37583: ['GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS',
         'GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS_EXT'],
 37584: ['GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS'],
 37585: ['GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS'],
 37586: ['GL_MAX_VERTEX_ATOMIC_COUNTERS'],
 37587: ['GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS',
         'GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS_EXT'],
 37588: ['GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS',
         'GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS_EXT'],
 37589: ['GL_MAX_GEOMETRY_ATOMIC_COUNTERS',
         'GL_MAX_GEOMETRY_ATOMIC_COUNTERS_EXT'],
 37590: ['GL_MAX_FRAGMENT_ATOMIC_COUNTERS'],
 37591: ['GL_MAX_COMBINED_ATOMIC_COUNTERS'],
 37592: ['GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE'],
 37593: ['GL_ACTIVE_ATOMIC_COUNTER_BUFFERS'],
 37594: ['GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX'],
 37595: ['GL_UNSIGNED_INT_ATOMIC_COUNTER'],
 37596: ['GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS'],
 37600: ['GL_DEBUG_OUTPUT'],
 37601: ['GL_UNIFORM'],
 37602: ['GL_UNIFORM_BLOCK'],
 37603: ['GL_PROGRAM_INPUT'],
 37604: ['GL_PROGRAM_OUTPUT'],
 37605: ['GL_BUFFER_VARIABLE'],
 37606: ['GL_SHADER_STORAGE_BLOCK'],
 37607: ['GL_IS_PER_PATCH', 'GL_IS_PER_PATCH_EXT'],
 37608: ['GL_VERTEX_SUBROUTINE'],
 37609: ['GL_TESS_CONTROL_SUBROUTINE'],
 37610: ['GL_TESS_EVALUATION_SUBROUTINE'],
 37611: ['GL_GEOMETRY_SUBROUTINE'],
 37612: ['GL_FRAGMENT_SUBROUTINE'],
 37613: ['GL_COMPUTE_SUBROUTINE'],
 37614: ['GL_VERTEX_SUBROUTINE_UNIFORM'],
 37615: ['GL_TESS_CONTROL_SUBROUTINE_UNIFORM'],
 37616: ['GL_TESS_EVALUATION_SUBROUTINE_UNIFORM'],
 37617: ['GL_GEOMETRY_SUBROUTINE_UNIFORM'],
 37618: ['GL_FRAGMENT_SUBROUTINE_UNIFORM'],
 37619: ['GL_COMPUTE_SUBROUTINE_UNIFORM'],
 37620: ['GL_TRANSFORM_FEEDBACK_VARYING'],
 37621: ['GL_ACTIVE_RESOURCES'],
 37622: ['GL_MAX_NAME_LENGTH'],
 37623: ['GL_MAX_NUM_ACTIVE_VARIABLES'],
 37624: ['GL_MAX_NUM_COMPATIBLE_SUBROUTINES'],
 37625: ['GL_NAME_LENGTH'],
 37626: ['GL_TYPE'],
 37627: ['GL_ARRAY_SIZE'],
 37628: ['GL_OFFSET'],
 37629: ['GL_BLOCK_INDEX'],
 37630: ['GL_ARRAY_STRIDE'],
 37631: ['GL_MATRIX_STRIDE'],
 37632: ['GL_IS_ROW_MAJOR'],
 37633: ['GL_ATOMIC_COUNTER_BUFFER_INDEX'],
 37634: ['GL_BUFFER_BINDING'],
 37635: ['GL_BUFFER_DATA_SIZE'],
 37636: ['GL_NUM_ACTIVE_VARIABLES'],
 37637: ['GL_ACTIVE_VARIABLES'],
 37638: ['GL_REFERENCED_BY_VERTEX_SHADER'],
 37639: ['GL_REFERENCED_BY_TESS_CONTROL_SHADER',
         'GL_REFERENCED_BY_TESS_CONTROL_SHADER_EXT'],
 37640: ['GL_REFERENCED_BY_TESS_EVALUATION_SHADER',
         'GL_REFERENCED_BY_TESS_EVALUATION_SHADER_EXT'],
 37641: ['GL_REFERENCED_BY_GEOMETRY_SHADER',
         'GL_REFERENCED_BY_GEOMETRY_SHADER_EXT'],
 37642: ['GL_REFERENCED_BY_FRAGMENT_SHADER'],
 37643: ['GL_REFERENCED_BY_COMPUTE_SHADER'],
 37644: ['GL_TOP_LEVEL_ARRAY_SIZE'],
 37645: ['GL_TOP_LEVEL_ARRAY_STRIDE'],
 37646: ['GL_LOCATION'],
 37647: ['GL_LOCATION_INDEX', 'GL_LOCATION_INDEX_EXT'],
 37648: ['GL_FRAMEBUFFER_DEFAULT_WIDTH'],
 37649: ['GL_FRAMEBUFFER_DEFAULT_HEIGHT'],
 37650: ['GL_FRAMEBUFFER_DEFAULT_LAYERS', 'GL_FRAMEBUFFER_DEFAULT_LAYERS_EXT'],
 37651: ['GL_FRAMEBUFFER_DEFAULT_SAMPLES'],
 37652: ['GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS'],
 37653: ['GL_MAX_FRAMEBUFFER_WIDTH'],
 37654: ['GL_MAX_FRAMEBUFFER_HEIGHT'],
 37655: ['GL_MAX_FRAMEBUFFER_LAYERS', 'GL_MAX_FRAMEBUFFER_LAYERS_EXT'],
 37656: ['GL_MAX_FRAMEBUFFER_SAMPLES'],
 37671: ['GL_RASTER_MULTISAMPLE_EXT'],
 37672: ['GL_RASTER_SAMPLES_EXT'],
 37673: ['GL_MAX_RASTER_SAMPLES_EXT'],
 37674: ['GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT'],
 37675: ['GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT'],
 37676: ['GL_EFFECTIVE_RASTER_SAMPLES_EXT'],
 37693: ['GL_SAMPLE_LOCATION_SUBPIXEL_BITS_ARB'],
 37694: ['GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_ARB'],
 37695: ['GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_ARB'],
 37696: ['GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_ARB'],
 37697: ['GL_PROGRAMMABLE_SAMPLE_LOCATION_ARB'],
 37698: ['GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_ARB'],
 37699: ['GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_ARB'],
 37700: ['GL_MAX_COMPUTE_VARIABLE_GROUP_INVOCATIONS_ARB'],
 37701: ['GL_MAX_COMPUTE_VARIABLE_GROUP_SIZE_ARB'],
 37706: ['GL_LOCATION_COMPONENT'],
 37707: ['GL_TRANSFORM_FEEDBACK_BUFFER_INDEX'],
 37708: ['GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE'],
 37724: ['GL_CLIP_ORIGIN', 'GL_CLIP_ORIGIN_EXT'],
 37725: ['GL_CLIP_DEPTH_MODE', 'GL_CLIP_DEPTH_MODE_EXT'],
 37726: ['GL_NEGATIVE_ONE_TO_ONE', 'GL_NEGATIVE_ONE_TO_ONE_EXT'],
 37727: ['GL_ZERO_TO_ONE', 'GL_ZERO_TO_ONE_EXT'],
 37733: ['GL_CLEAR_TEXTURE'],
 37734: ['GL_TEXTURE_REDUCTION_MODE_ARB', 'GL_TEXTURE_REDUCTION_MODE_EXT'],
 37735: ['GL_WEIGHTED_AVERAGE_ARB', 'GL_WEIGHTED_AVERAGE_EXT'],
 37760: ['GL_NUM_SAMPLE_COUNTS'],
 37761: ['GL_MULTISAMPLE_LINE_WIDTH_RANGE_ARB',
         'GL_MULTISAMPLE_LINE_WIDTH_RANGE'],
 37762: ['GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY_ARB',
         'GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY'],
 37763: ['GL_VIEW_CLASS_EAC_R11'],
 37764: ['GL_VIEW_CLASS_EAC_RG11'],
 37765: ['GL_VIEW_CLASS_ETC2_RGB'],
 37766: ['GL_VIEW_CLASS_ETC2_RGBA'],
 37767: ['GL_VIEW_CLASS_ETC2_EAC_RGBA'],
 37768: ['GL_VIEW_CLASS_ASTC_4x4_RGBA'],
 37769: ['GL_VIEW_CLASS_ASTC_5x4_RGBA'],
 37770: ['GL_VIEW_CLASS_ASTC_5x5_RGBA'],
 37771: ['GL_VIEW_CLASS_ASTC_6x5_RGBA'],
 37772: ['GL_VIEW_CLASS_ASTC_6x6_RGBA'],
 37773: ['GL_VIEW_CLASS_ASTC_8x5_RGBA'],
 37774: ['GL_VIEW_CLASS_ASTC_8x6_RGBA'],
 37775: ['GL_VIEW_CLASS_ASTC_8x8_RGBA'],
 37776: ['GL_VIEW_CLASS_ASTC_10x5_RGBA'],
 37777: ['GL_VIEW_CLASS_ASTC_10x6_RGBA'],
 37778: ['GL_VIEW_CLASS_ASTC_10x8_RGBA'],
 37779: ['GL_VIEW_CLASS_ASTC_10x10_RGBA'],
 37780: ['GL_VIEW_CLASS_ASTC_12x10_RGBA'],
 37781: ['GL_VIEW_CLASS_ASTC_12x12_RGBA'],
 37792: ['GL_TRANSLATED_SHADER_SOURCE_LENGTH_ANGLE'],
 37793: ['GL_BGRA8_EXT'],
 37794: ['GL_TEXTURE_USAGE_ANGLE'],
 37795: ['GL_FRAMEBUFFER_ATTACHMENT_ANGLE'],
 37796: ['GL_PACK_REVERSE_ROW_ORDER_ANGLE'],
 37798: ['GL_PROGRAM_BINARY_ANGLE'],
 37808: ['GL_COMPRESSED_RGBA_ASTC_4x4'],
 37809: ['GL_COMPRESSED_RGBA_ASTC_5x4'],
 37810: ['GL_COMPRESSED_RGBA_ASTC_5x5'],
 37811: ['GL_COMPRESSED_RGBA_ASTC_6x5'],
 37812: ['GL_COMPRESSED_RGBA_ASTC_6x6'],
 37813: ['GL_COMPRESSED_RGBA_ASTC_8x5'],
 37814: ['GL_COMPRESSED_RGBA_ASTC_8x6'],
 37815: ['GL_COMPRESSED_RGBA_ASTC_8x8'],
 37816: ['GL_COMPRESSED_RGBA_ASTC_10x5'],
 37817: ['GL_COMPRESSED_RGBA_ASTC_10x6'],
 37818: ['GL_COMPRESSED_RGBA_ASTC_10x8'],
 37819: ['GL_COMPRESSED_RGBA_ASTC_10x10'],
 37820: ['GL_COMPRESSED_RGBA_ASTC_12x10'],
 37821: ['GL_COMPRESSED_RGBA_ASTC_12x12'],
 37840: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4'],
 37841: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4'],
 37842: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5'],
 37843: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5'],
 37844: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6'],
 37845: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5'],
 37846: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6'],
 37847: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8'],
 37848: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5'],
 37849: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6'],
 37850: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8'],
 37851: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10'],
 37852: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10'],
 37853: ['GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12'],
 37872: ['GL_COMPRESSED_SRGB_ALPHA_PVRTC_2BPPV2_IMG'],
 37873: ['GL_COMPRESSED_SRGB_ALPHA_PVRTC_4BPPV2_IMG'],
 38192: ['GL_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_EXT'],
 38193: ['GL_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_EXT'],
 38218: ['GL_UPLOAD_GPU_MASK_NVX'],
 38225: ['GL_SHADER_BINARY_FORMAT_SPIR_V',
         'GL_SHADER_BINARY_FORMAT_SPIR_V_ARB'],
 38226: ['GL_SPIR_V_BINARY', 'GL_SPIR_V_BINARY_ARB'],
 38227: ['GL_SPIR_V_EXTENSIONS'],
 38228: ['GL_NUM_SPIR_V_EXTENSIONS'],
 38272: ['GL_TEXTURE_TILING_EXT'],
 38273: ['GL_DEDICATED_MEMORY_OBJECT_EXT'],
 38274: ['GL_NUM_TILING_TYPES_EXT'],
 38275: ['GL_TILING_TYPES_EXT'],
 38276: ['GL_OPTIMAL_TILING_EXT'],
 38277: ['GL_LINEAR_TILING_EXT'],
 38278: ['GL_HANDLE_TYPE_OPAQUE_FD_EXT'],
 38279: ['GL_HANDLE_TYPE_OPAQUE_WIN32_EXT'],
 38280: ['GL_HANDLE_TYPE_OPAQUE_WIN32_KMT_EXT'],
 38281: ['GL_HANDLE_TYPE_D3D12_TILEPOOL_EXT'],
 38282: ['GL_HANDLE_TYPE_D3D12_RESOURCE_EXT'],
 38283: ['GL_HANDLE_TYPE_D3D11_IMAGE_EXT'],
 38284: ['GL_HANDLE_TYPE_D3D11_IMAGE_KMT_EXT'],
 38285: ['GL_LAYOUT_GENERAL_EXT'],
 38286: ['GL_LAYOUT_COLOR_ATTACHMENT_EXT'],
 38287: ['GL_LAYOUT_DEPTH_STENCIL_ATTACHMENT_EXT'],
 38288: ['GL_LAYOUT_DEPTH_STENCIL_READ_ONLY_EXT'],
 38289: ['GL_LAYOUT_SHADER_READ_ONLY_EXT'],
 38290: ['GL_LAYOUT_TRANSFER_SRC_EXT'],
 38291: ['GL_LAYOUT_TRANSFER_DST_EXT'],
 38292: ['GL_HANDLE_TYPE_D3D12_FENCE_EXT'],
 38293: ['GL_D3D12_FENCE_VALUE_EXT'],
 38294: ['GL_NUM_DEVICE_UUIDS_EXT'],
 38295: ['GL_DEVICE_UUID_EXT'],
 38296: ['GL_DRIVER_UUID_EXT'],
 38297: ['GL_DEVICE_LUID_EXT'],
 38298: ['GL_DEVICE_NODE_MASK_EXT'],
 38299: ['GL_PROTECTED_MEMORY_OBJECT_EXT'],
 38448: ['GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR'],
 38449: ['GL_MAX_VIEWS_OVR'],
 38450: ['GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR'],
 38451: ['GL_FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR'],
 38464: ['GL_GS_SHADER_BINARY_MTK'],
 38465: ['GL_GS_PROGRAM_BINARY_MTK'],
 38480: ['GL_MAX_SHADER_COMBINED_LOCAL_STORAGE_FAST_SIZE_EXT'],
 38481: ['GL_MAX_SHADER_COMBINED_LOCAL_STORAGE_SIZE_EXT'],
 38482: ['GL_FRAMEBUFFER_INCOMPLETE_INSUFFICIENT_SHADER_COMBINED_LOCAL_STORAGE_EXT'],
 65536: ['GL_EVAL_BIT'],
 131072: ['GL_LIST_BIT'],
 262144: ['GL_TEXTURE_BIT'],
 524288: ['GL_SCISSOR_BIT'],
 536870912: ['GL_MULTISAMPLE_BIT',
             'GL_MULTISAMPLE_BIT_ARB',
             'GL_MULTISAMPLE_BIT_EXT',
             'GL_MULTISAMPLE_BIT_3DFX'],
 4294967295: ['GL_ALL_ATTRIB_BITS',
              'GL_CLIENT_ALL_ATTRIB_BITS',
              'GL_ALL_BARRIER_BITS',
              'GL_ALL_BARRIER_BITS_EXT',
              'GL_ALL_SHADER_BITS',
              'GL_ALL_SHADER_BITS_EXT',
              'GL_INVALID_INDEX'],
 18446744073709551615: ['GL_TIMEOUT_IGNORED']}
glfuncs= {'glAccum': {0: 'AccumOp'},
 'glActiveStencilFaceEXT': {0: 'StencilFaceDirection'},
 'glActiveTexture': {0: 'TextureUnit'},
 'glActiveTextureARB': {0: 'TextureUnit'},
 'glAlphaFunc': {0: 'AlphaFunction'},
 'glAlphaFuncx': {0: 'AlphaFunction'},
 'glApplyTextureEXT': {0: 'LightTextureModeEXT'},
 'glAreTexturesResident': {2: 'Boolean'},
 'glAreTexturesResidentEXT': {2: 'Boolean'},
 'glBegin': {0: 'PrimitiveType'},
 'glBeginConditionalRender': {1: 'ConditionalRenderMode'},
 'glBeginQuery': {0: 'QueryTarget'},
 'glBeginQueryEXT': {0: 'QueryTarget'},
 'glBeginQueryIndexed': {0: 'QueryTarget'},
 'glBeginTransformFeedback': {0: 'PrimitiveType'},
 'glBeginTransformFeedbackEXT': {0: 'PrimitiveType'},
 'glBindBuffer': {0: 'BufferTargetARB'},
 'glBindBufferARB': {0: 'BufferTargetARB'},
 'glBindBufferBase': {0: 'BufferTargetARB'},
 'glBindBufferBaseEXT': {0: 'BufferTargetARB'},
 'glBindBufferOffsetEXT': {0: 'BufferTargetARB'},
 'glBindBufferRange': {0: 'BufferTargetARB'},
 'glBindBufferRangeEXT': {0: 'BufferTargetARB'},
 'glBindBuffersBase': {0: 'BufferTargetARB'},
 'glBindBuffersRange': {0: 'BufferTargetARB'},
 'glBindFramebuffer': {0: 'FramebufferTarget'},
 'glBindFramebufferEXT': {0: 'FramebufferTarget'},
 'glBindImageTexture': {3: 'Boolean',
                        5: 'BufferAccessARB',
                        6: 'InternalFormat'},
 'glBindImageTextureEXT': {3: 'Boolean', 5: 'BufferAccessARB'},
 'glBindLightParameterEXT': {0: 'LightName', 1: 'LightParameter'},
 'glBindMaterialParameterEXT': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glBindMultiTextureEXT': {0: 'TextureUnit', 1: 'TextureTarget'},
 'glBindParameterEXT': {0: 'VertexShaderParameterEXT'},
 'glBindProgramARB': {0: 'ProgramTargetARB'},
 'glBindRenderbuffer': {0: 'RenderbufferTarget'},
 'glBindRenderbufferEXT': {0: 'RenderbufferTarget'},
 'glBindTexGenParameterEXT': {0: 'TextureUnit',
                              1: 'TextureCoordName',
                              2: 'TextureGenParameter'},
 'glBindTexture': {0: 'TextureTarget'},
 'glBindTextureEXT': {0: 'TextureTarget'},
 'glBindTextureUnitParameterEXT': {0: 'TextureUnit',
                                   1: 'VertexShaderTextureUnitParameter'},
 'glBindTransformFeedback': {0: 'BindTransformFeedbackTarget'},
 'glBinormalPointerEXT': {0: 'BinormalPointerTypeEXT'},
 'glBlendEquation': {0: 'BlendEquationModeEXT'},
 'glBlendEquationEXT': {0: 'BlendEquationModeEXT'},
 'glBlendEquationSeparate': {0: 'BlendEquationModeEXT',
                             1: 'BlendEquationModeEXT'},
 'glBlendEquationSeparateEXT': {0: 'BlendEquationModeEXT',
                                1: 'BlendEquationModeEXT'},
 'glBlendEquationSeparatei': {1: 'BlendEquationModeEXT',
                              2: 'BlendEquationModeEXT'},
 'glBlendEquationSeparateiARB': {1: 'BlendEquationModeEXT',
                                 2: 'BlendEquationModeEXT'},
 'glBlendEquationSeparateiEXT': {1: 'BlendEquationModeEXT',
                                 2: 'BlendEquationModeEXT'},
 'glBlendEquationi': {1: 'BlendEquationModeEXT'},
 'glBlendEquationiARB': {1: 'BlendEquationModeEXT'},
 'glBlendEquationiEXT': {1: 'BlendEquationModeEXT'},
 'glBlendFunc': {0: 'BlendingFactor', 1: 'BlendingFactor'},
 'glBlendFuncSeparate': {0: 'BlendingFactor',
                         1: 'BlendingFactor',
                         2: 'BlendingFactor',
                         3: 'BlendingFactor'},
 'glBlendFuncSeparateEXT': {0: 'BlendingFactor',
                            1: 'BlendingFactor',
                            2: 'BlendingFactor',
                            3: 'BlendingFactor'},
 'glBlendFuncSeparateINGR': {0: 'BlendingFactor',
                             1: 'BlendingFactor',
                             2: 'BlendingFactor',
                             3: 'BlendingFactor'},
 'glBlendFuncSeparatei': {1: 'BlendingFactor',
                          2: 'BlendingFactor',
                          3: 'BlendingFactor',
                          4: 'BlendingFactor'},
 'glBlendFuncSeparateiARB': {1: 'BlendingFactor',
                             2: 'BlendingFactor',
                             3: 'BlendingFactor',
                             4: 'BlendingFactor'},
 'glBlendFuncSeparateiEXT': {1: 'BlendingFactor',
                             2: 'BlendingFactor',
                             3: 'BlendingFactor',
                             4: 'BlendingFactor'},
 'glBlendFunci': {1: 'BlendingFactor', 2: 'BlendingFactor'},
 'glBlendFunciARB': {1: 'BlendingFactor', 2: 'BlendingFactor'},
 'glBlendFunciEXT': {1: 'BlendingFactor', 2: 'BlendingFactor'},
 'glBlitFramebuffer': {8: 'ClearBufferMask', 9: 'BlitFramebufferFilter'},
 'glBlitFramebufferANGLE': {8: 'ClearBufferMask', 9: 'BlitFramebufferFilter'},
 'glBlitFramebufferEXT': {8: 'ClearBufferMask', 9: 'BlitFramebufferFilter'},
 'glBlitNamedFramebuffer': {10: 'ClearBufferMask', 11: 'BlitFramebufferFilter'},
 'glBufferData': {0: 'BufferTargetARB', 3: 'BufferUsageARB'},
 'glBufferDataARB': {0: 'BufferTargetARB', 3: 'BufferUsageARB'},
 'glBufferStorage': {0: 'BufferStorageTarget', 3: 'BufferStorageMask'},
 'glBufferStorageEXT': {0: 'BufferStorageTarget', 3: 'BufferStorageMask'},
 'glBufferStorageExternalEXT': {4: 'BufferStorageMask'},
 'glBufferStorageMemEXT': {0: 'BufferTargetARB'},
 'glBufferSubData': {0: 'BufferTargetARB'},
 'glBufferSubDataARB': {0: 'BufferTargetARB'},
 'glCallLists': {1: 'ListNameType'},
 'glCheckFramebufferStatus': {0: 'FramebufferTarget'},
 'glCheckFramebufferStatusEXT': {0: 'FramebufferTarget'},
 'glCheckNamedFramebufferStatus': {1: 'FramebufferTarget'},
 'glCheckNamedFramebufferStatusEXT': {1: 'FramebufferTarget'},
 'glClampColor': {0: 'ClampColorTargetARB', 1: 'ClampColorModeARB'},
 'glClampColorARB': {0: 'ClampColorTargetARB', 1: 'ClampColorModeARB'},
 'glClear': {0: 'ClearBufferMask'},
 'glClearBufferData': {0: 'BufferStorageTarget',
                       1: 'InternalFormat',
                       2: 'PixelFormat',
                       3: 'PixelType'},
 'glClearBufferSubData': {0: 'BufferTargetARB',
                          1: 'InternalFormat',
                          4: 'PixelFormat',
                          5: 'PixelType'},
 'glClearBufferfi': {0: 'Buffer'},
 'glClearBufferfv': {0: 'Buffer'},
 'glClearBufferiv': {0: 'Buffer'},
 'glClearBufferuiv': {0: 'Buffer'},
 'glClearNamedBufferData': {1: 'InternalFormat',
                            2: 'PixelFormat',
                            3: 'PixelType'},
 'glClearNamedBufferDataEXT': {1: 'InternalFormat',
                               2: 'PixelFormat',
                               3: 'PixelType'},
 'glClearNamedBufferSubData': {1: 'InternalFormat',
                               4: 'PixelFormat',
                               5: 'PixelType'},
 'glClearNamedBufferSubDataEXT': {4: 'PixelFormat', 5: 'PixelType'},
 'glClearNamedFramebufferfi': {1: 'Buffer'},
 'glClearNamedFramebufferfv': {1: 'Buffer'},
 'glClearNamedFramebufferiv': {1: 'Buffer'},
 'glClearNamedFramebufferuiv': {1: 'Buffer'},
 'glClearTexImage': {2: 'PixelFormat', 3: 'PixelType'},
 'glClearTexImageEXT': {2: 'PixelFormat', 3: 'PixelType'},
 'glClearTexSubImage': {8: 'PixelFormat', 9: 'PixelType'},
 'glClearTexSubImageEXT': {8: 'PixelFormat', 9: 'PixelType'},
 'glClientActiveTexture': {0: 'TextureUnit'},
 'glClientActiveTextureARB': {0: 'TextureUnit'},
 'glClientAttribDefaultEXT': {0: 'ClientAttribMask'},
 'glClientWaitSync': {1: 'SyncObjectMask'},
 'glClipControl': {0: 'ClipControlOrigin', 1: 'ClipControlDepth'},
 'glClipPlane': {0: 'ClipPlaneName'},
 'glClipPlanef': {0: 'ClipPlaneName'},
 'glClipPlanefIMG': {0: 'ClipPlaneName'},
 'glClipPlanex': {0: 'ClipPlaneName'},
 'glClipPlanexIMG': {0: 'ClipPlaneName'},
 'glColorMask': {0: 'Boolean', 1: 'Boolean', 2: 'Boolean', 3: 'Boolean'},
 'glColorMaskIndexedEXT': {1: 'Boolean',
                           2: 'Boolean',
                           3: 'Boolean',
                           4: 'Boolean'},
 'glColorMaski': {1: 'Boolean', 2: 'Boolean', 3: 'Boolean', 4: 'Boolean'},
 'glColorMaskiEXT': {1: 'Boolean', 2: 'Boolean', 3: 'Boolean', 4: 'Boolean'},
 'glColorMaterial': {0: 'MaterialFace', 1: 'ColorMaterialParameter'},
 'glColorP3ui': {0: 'ColorPointerType'},
 'glColorP3uiv': {0: 'ColorPointerType'},
 'glColorP4ui': {0: 'ColorPointerType'},
 'glColorP4uiv': {0: 'ColorPointerType'},
 'glColorPointer': {1: 'ColorPointerType'},
 'glColorPointerEXT': {1: 'ColorPointerType'},
 'glColorSubTable': {0: 'ColorTableTarget', 3: 'PixelFormat', 4: 'PixelType'},
 'glColorSubTableEXT': {0: 'ColorTableTarget',
                        3: 'PixelFormat',
                        4: 'PixelType'},
 'glColorTable': {0: 'ColorTableTarget',
                  1: 'InternalFormat',
                  3: 'PixelFormat',
                  4: 'PixelType'},
 'glColorTableEXT': {0: 'ColorTableTarget',
                     1: 'InternalFormat',
                     3: 'PixelFormat',
                     4: 'PixelType'},
 'glColorTableParameterfv': {0: 'ColorTableTarget',
                             1: 'ColorTableParameterPNameSGI'},
 'glColorTableParameteriv': {0: 'ColorTableTarget',
                             1: 'ColorTableParameterPNameSGI'},
 'glCompressedMultiTexImage1DEXT': {0: 'TextureUnit',
                                    1: 'TextureTarget',
                                    3: 'InternalFormat'},
 'glCompressedMultiTexImage2DEXT': {0: 'TextureUnit',
                                    1: 'TextureTarget',
                                    3: 'InternalFormat'},
 'glCompressedMultiTexImage3DEXT': {0: 'TextureUnit',
                                    1: 'TextureTarget',
                                    3: 'InternalFormat'},
 'glCompressedMultiTexSubImage1DEXT': {0: 'TextureUnit',
                                       1: 'TextureTarget',
                                       5: 'PixelFormat'},
 'glCompressedMultiTexSubImage2DEXT': {0: 'TextureUnit',
                                       1: 'TextureTarget',
                                       7: 'PixelFormat'},
 'glCompressedMultiTexSubImage3DEXT': {0: 'TextureUnit',
                                       1: 'TextureTarget',
                                       9: 'PixelFormat'},
 'glCompressedTexImage1D': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCompressedTexImage1DARB': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCompressedTexImage2D': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCompressedTexImage2DARB': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCompressedTexImage3D': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCompressedTexImage3DARB': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCompressedTexSubImage1D': {0: 'TextureTarget', 4: 'PixelFormat'},
 'glCompressedTexSubImage1DARB': {0: 'TextureTarget', 4: 'PixelFormat'},
 'glCompressedTexSubImage2D': {0: 'TextureTarget', 6: 'PixelFormat'},
 'glCompressedTexSubImage2DARB': {0: 'TextureTarget', 6: 'PixelFormat'},
 'glCompressedTexSubImage3D': {0: 'TextureTarget', 8: 'PixelFormat'},
 'glCompressedTexSubImage3DARB': {0: 'TextureTarget', 8: 'PixelFormat'},
 'glCompressedTextureImage1DEXT': {1: 'TextureTarget', 3: 'InternalFormat'},
 'glCompressedTextureImage2DEXT': {1: 'TextureTarget', 3: 'InternalFormat'},
 'glCompressedTextureImage3DEXT': {1: 'TextureTarget', 3: 'InternalFormat'},
 'glCompressedTextureSubImage1D': {4: 'PixelFormat'},
 'glCompressedTextureSubImage1DEXT': {1: 'TextureTarget', 5: 'PixelFormat'},
 'glCompressedTextureSubImage2D': {6: 'PixelFormat'},
 'glCompressedTextureSubImage2DEXT': {1: 'TextureTarget', 7: 'PixelFormat'},
 'glCompressedTextureSubImage3D': {8: 'PixelFormat'},
 'glCompressedTextureSubImage3DEXT': {1: 'TextureTarget', 9: 'PixelFormat'},
 'glConvolutionFilter1D': {0: 'ConvolutionTarget',
                           1: 'InternalFormat',
                           3: 'PixelFormat',
                           4: 'PixelType'},
 'glConvolutionFilter1DEXT': {0: 'ConvolutionTargetEXT',
                              1: 'InternalFormat',
                              3: 'PixelFormat',
                              4: 'PixelType'},
 'glConvolutionFilter2D': {0: 'ConvolutionTarget',
                           1: 'InternalFormat',
                           4: 'PixelFormat',
                           5: 'PixelType'},
 'glConvolutionFilter2DEXT': {0: 'ConvolutionTargetEXT',
                              1: 'InternalFormat',
                              4: 'PixelFormat',
                              5: 'PixelType'},
 'glConvolutionParameterf': {0: 'ConvolutionTarget',
                             1: 'ConvolutionParameterEXT'},
 'glConvolutionParameterfEXT': {0: 'ConvolutionTargetEXT',
                                1: 'ConvolutionParameterEXT'},
 'glConvolutionParameterfv': {0: 'ConvolutionTarget',
                              1: 'ConvolutionParameterEXT'},
 'glConvolutionParameterfvEXT': {0: 'ConvolutionTargetEXT',
                                 1: 'ConvolutionParameterEXT'},
 'glConvolutionParameteri': {0: 'ConvolutionTarget',
                             1: 'ConvolutionParameterEXT'},
 'glConvolutionParameteriEXT': {0: 'ConvolutionTargetEXT',
                                1: 'ConvolutionParameterEXT'},
 'glConvolutionParameteriv': {0: 'ConvolutionTarget',
                              1: 'ConvolutionParameterEXT'},
 'glConvolutionParameterivEXT': {0: 'ConvolutionTargetEXT',
                                 1: 'ConvolutionParameterEXT'},
 'glCopyBufferSubData': {0: 'CopyBufferSubDataTarget',
                         1: 'CopyBufferSubDataTarget'},
 'glCopyColorSubTable': {0: 'ColorTableTarget'},
 'glCopyColorSubTableEXT': {0: 'ColorTableTarget'},
 'glCopyColorTable': {0: 'ColorTableTarget', 1: 'InternalFormat'},
 'glCopyConvolutionFilter1D': {0: 'ConvolutionTarget', 1: 'InternalFormat'},
 'glCopyConvolutionFilter1DEXT': {0: 'ConvolutionTargetEXT',
                                  1: 'InternalFormat'},
 'glCopyConvolutionFilter2D': {0: 'ConvolutionTarget', 1: 'InternalFormat'},
 'glCopyConvolutionFilter2DEXT': {0: 'ConvolutionTargetEXT',
                                  1: 'InternalFormat'},
 'glCopyImageSubData': {1: 'CopyImageSubDataTarget',
                        7: 'CopyImageSubDataTarget'},
 'glCopyImageSubDataEXT': {1: 'CopyBufferSubDataTarget',
                           7: 'CopyBufferSubDataTarget'},
 'glCopyMultiTexImage1DEXT': {0: 'TextureUnit',
                              1: 'TextureTarget',
                              3: 'InternalFormat'},
 'glCopyMultiTexImage2DEXT': {0: 'TextureUnit',
                              1: 'TextureTarget',
                              3: 'InternalFormat'},
 'glCopyMultiTexSubImage1DEXT': {0: 'TextureUnit', 1: 'TextureTarget'},
 'glCopyMultiTexSubImage2DEXT': {0: 'TextureUnit', 1: 'TextureTarget'},
 'glCopyMultiTexSubImage3DEXT': {0: 'TextureUnit', 1: 'TextureTarget'},
 'glCopyPixels': {4: 'PixelCopyType'},
 'glCopyTexImage1D': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCopyTexImage1DEXT': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCopyTexImage2D': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCopyTexImage2DEXT': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glCopyTexSubImage1D': {0: 'TextureTarget'},
 'glCopyTexSubImage1DEXT': {0: 'TextureTarget'},
 'glCopyTexSubImage2D': {0: 'TextureTarget'},
 'glCopyTexSubImage2DEXT': {0: 'TextureTarget'},
 'glCopyTexSubImage3D': {0: 'TextureTarget'},
 'glCopyTexSubImage3DEXT': {0: 'TextureTarget'},
 'glCopyTextureImage1DEXT': {1: 'TextureTarget', 3: 'InternalFormat'},
 'glCopyTextureImage2DEXT': {1: 'TextureTarget', 3: 'InternalFormat'},
 'glCopyTextureSubImage1DEXT': {1: 'TextureTarget'},
 'glCopyTextureSubImage2DEXT': {1: 'TextureTarget'},
 'glCopyTextureSubImage3DEXT': {1: 'TextureTarget'},
 'glCreateQueries': {0: 'QueryTarget'},
 'glCreateShader': {0: 'ShaderType'},
 'glCreateShaderObjectARB': {0: 'ShaderType'},
 'glCreateShaderProgramEXT': {0: 'ShaderType'},
 'glCreateShaderProgramv': {0: 'ShaderType'},
 'glCreateShaderProgramvEXT': {0: 'ShaderType'},
 'glCreateTextures': {0: 'TextureTarget'},
 'glCullFace': {0: 'CullFaceMode'},
 'glCullParameterdvEXT': {0: 'CullParameterEXT'},
 'glCullParameterfvEXT': {0: 'CullParameterEXT'},
 'glDebugMessageControl': {0: 'DebugSource',
                           1: 'DebugType',
                           2: 'DebugSeverity',
                           5: 'Boolean'},
 'glDebugMessageControlARB': {0: 'DebugSource',
                              1: 'DebugType',
                              2: 'DebugSeverity',
                              5: 'Boolean'},
 'glDebugMessageInsert': {0: 'DebugSource', 1: 'DebugType', 3: 'DebugSeverity'},
 'glDebugMessageInsertARB': {0: 'DebugSource',
                             1: 'DebugType',
                             3: 'DebugSeverity'},
 'glDepthFunc': {0: 'DepthFunction'},
 'glDepthMask': {0: 'Boolean'},
 'glDisable': {0: 'EnableCap'},
 'glDisableClientState': {0: 'EnableCap'},
 'glDisableClientStateIndexedEXT': {0: 'EnableCap'},
 'glDisableClientStateiEXT': {0: 'EnableCap'},
 'glDisableIndexedEXT': {0: 'EnableCap'},
 'glDisableVertexArrayEXT': {1: 'EnableCap'},
 'glDisablei': {0: 'EnableCap'},
 'glDisableiEXT': {0: 'EnableCap'},
 'glDiscardFramebufferEXT': {0: 'FramebufferTarget',
                             2: 'InvalidateFramebufferAttachment'},
 'glDrawArrays': {0: 'PrimitiveType'},
 'glDrawArraysEXT': {0: 'PrimitiveType'},
 'glDrawArraysIndirect': {0: 'PrimitiveType'},
 'glDrawArraysInstanced': {0: 'PrimitiveType'},
 'glDrawArraysInstancedANGLE': {0: 'PrimitiveType'},
 'glDrawArraysInstancedARB': {0: 'PrimitiveType'},
 'glDrawArraysInstancedBaseInstance': {0: 'PrimitiveType'},
 'glDrawArraysInstancedBaseInstanceEXT': {0: 'PrimitiveType'},
 'glDrawArraysInstancedEXT': {0: 'PrimitiveType'},
 'glDrawBuffer': {0: 'DrawBufferMode'},
 'glDrawBuffers': {1: 'DrawBufferMode'},
 'glDrawBuffersARB': {1: 'DrawBufferMode'},
 'glDrawElements': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glDrawElementsBaseVertex': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glDrawElementsBaseVertexEXT': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glDrawElementsIndirect': {0: 'PrimitiveType', 1: 'DrawElementsType'},
 'glDrawElementsInstanced': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glDrawElementsInstancedANGLE': {0: 'PrimitiveType', 2: 'PrimitiveType'},
 'glDrawElementsInstancedARB': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glDrawElementsInstancedBaseInstance': {0: 'PrimitiveType',
                                         2: 'PrimitiveType'},
 'glDrawElementsInstancedBaseInstanceEXT': {0: 'PrimitiveType',
                                            2: 'PrimitiveType'},
 'glDrawElementsInstancedBaseVertex': {0: 'PrimitiveType',
                                       2: 'DrawElementsType'},
 'glDrawElementsInstancedBaseVertexBaseInstance': {0: 'PrimitiveType',
                                                   2: 'DrawElementsType'},
 'glDrawElementsInstancedBaseVertexBaseInstanceEXT': {0: 'PrimitiveType',
                                                      2: 'DrawElementsType'},
 'glDrawElementsInstancedBaseVertexEXT': {0: 'PrimitiveType',
                                          2: 'DrawElementsType'},
 'glDrawElementsInstancedEXT': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glDrawPixels': {2: 'PixelFormat', 3: 'PixelType'},
 'glDrawRangeElements': {0: 'PrimitiveType', 4: 'DrawElementsType'},
 'glDrawRangeElementsBaseVertex': {0: 'PrimitiveType', 4: 'DrawElementsType'},
 'glDrawRangeElementsBaseVertexEXT': {0: 'PrimitiveType',
                                      4: 'DrawElementsType'},
 'glDrawRangeElementsEXT': {0: 'PrimitiveType', 4: 'DrawElementsType'},
 'glDrawTransformFeedback': {0: 'PrimitiveType'},
 'glDrawTransformFeedbackEXT': {0: 'PrimitiveType'},
 'glDrawTransformFeedbackInstanced': {0: 'PrimitiveType'},
 'glDrawTransformFeedbackInstancedEXT': {0: 'PrimitiveType'},
 'glDrawTransformFeedbackStream': {0: 'PrimitiveType'},
 'glDrawTransformFeedbackStreamInstanced': {0: 'PrimitiveType'},
 'glEdgeFlag': {0: 'Boolean'},
 'glEdgeFlagPointerEXT': {2: 'Boolean'},
 'glEdgeFlagv': {0: 'Boolean'},
 'glEnable': {0: 'EnableCap'},
 'glEnableClientState': {0: 'EnableCap'},
 'glEnableClientStateIndexedEXT': {0: 'EnableCap'},
 'glEnableClientStateiEXT': {0: 'EnableCap'},
 'glEnableIndexedEXT': {0: 'EnableCap'},
 'glEnableVertexArrayEXT': {1: 'EnableCap'},
 'glEnablei': {0: 'EnableCap'},
 'glEnableiEXT': {0: 'EnableCap'},
 'glEndQuery': {0: 'QueryTarget'},
 'glEndQueryARB': {0: 'QueryTarget'},
 'glEndQueryEXT': {0: 'QueryTarget'},
 'glEndQueryIndexed': {0: 'QueryTarget'},
 'glEvalMesh1': {0: 'MeshMode1'},
 'glEvalMesh2': {0: 'MeshMode2'},
 'glFeedbackBuffer': {1: 'FeedbackType'},
 'glFenceSync': {0: 'SyncCondition'},
 'glFlushMappedBufferRange': {0: 'BufferTargetARB'},
 'glFlushMappedBufferRangeEXT': {0: 'BufferTargetARB'},
 'glFogCoordPointer': {0: 'FogPointerTypeEXT'},
 'glFogCoordPointerEXT': {0: 'FogPointerTypeEXT'},
 'glFogf': {0: 'FogParameter'},
 'glFogfv': {0: 'FogParameter'},
 'glFogi': {0: 'FogParameter'},
 'glFogiv': {0: 'FogParameter'},
 'glFogx': {0: 'FogPName'},
 'glFogxv': {0: 'FogPName'},
 'glFramebufferDrawBufferEXT': {1: 'DrawBufferMode'},
 'glFramebufferDrawBuffersEXT': {2: 'DrawBufferMode'},
 'glFramebufferParameteri': {0: 'FramebufferTarget',
                             1: 'FramebufferParameterName'},
 'glFramebufferReadBufferEXT': {1: 'ReadBufferMode'},
 'glFramebufferRenderbuffer': {0: 'FramebufferTarget',
                               1: 'FramebufferAttachment',
                               2: 'RenderbufferTarget'},
 'glFramebufferRenderbufferEXT': {0: 'FramebufferTarget',
                                  1: 'FramebufferAttachment',
                                  2: 'RenderbufferTarget'},
 'glFramebufferSampleLocationsfvARB': {0: 'FramebufferTarget'},
 'glFramebufferTexture': {0: 'FramebufferTarget', 1: 'FramebufferAttachment'},
 'glFramebufferTexture1D': {0: 'FramebufferTarget',
                            1: 'FramebufferAttachment',
                            2: 'TextureTarget'},
 'glFramebufferTexture1DEXT': {0: 'FramebufferTarget',
                               1: 'FramebufferAttachment',
                               2: 'TextureTarget'},
 'glFramebufferTexture2D': {0: 'FramebufferTarget',
                            1: 'FramebufferAttachment',
                            2: 'TextureTarget'},
 'glFramebufferTexture2DDownsampleIMG': {0: 'FramebufferTarget',
                                         1: 'FramebufferAttachment',
                                         2: 'TextureTarget'},
 'glFramebufferTexture2DEXT': {0: 'FramebufferTarget',
                               1: 'FramebufferAttachment',
                               2: 'TextureTarget'},
 'glFramebufferTexture2DMultisampleEXT': {0: 'FramebufferTarget',
                                          1: 'FramebufferAttachment',
                                          2: 'TextureTarget'},
 'glFramebufferTexture2DMultisampleIMG': {0: 'FramebufferTarget',
                                          1: 'FramebufferAttachment',
                                          2: 'TextureTarget'},
 'glFramebufferTexture3D': {0: 'FramebufferTarget',
                            1: 'FramebufferAttachment',
                            2: 'TextureTarget'},
 'glFramebufferTexture3DEXT': {0: 'FramebufferTarget',
                               1: 'FramebufferAttachment',
                               2: 'TextureTarget'},
 'glFramebufferTextureARB': {0: 'FramebufferTarget',
                             1: 'FramebufferAttachment'},
 'glFramebufferTextureEXT': {0: 'FramebufferTarget',
                             1: 'FramebufferAttachment'},
 'glFramebufferTextureFaceARB': {0: 'FramebufferTarget',
                                 1: 'FramebufferAttachment',
                                 4: 'TextureTarget'},
 'glFramebufferTextureFaceEXT': {0: 'FramebufferTarget',
                                 1: 'FramebufferAttachment',
                                 4: 'TextureTarget'},
 'glFramebufferTextureLayer': {0: 'FramebufferTarget',
                               1: 'FramebufferAttachment'},
 'glFramebufferTextureLayerARB': {0: 'FramebufferTarget',
                                  1: 'FramebufferAttachment'},
 'glFramebufferTextureLayerDownsampleIMG': {0: 'FramebufferTarget',
                                            1: 'FramebufferAttachment'},
 'glFramebufferTextureLayerEXT': {0: 'FramebufferTarget',
                                  1: 'FramebufferAttachment'},
 'glFramebufferTextureMultisampleMultiviewOVR': {0: 'FramebufferTarget',
                                                 1: 'FramebufferAttachment'},
 'glFramebufferTextureMultiviewOVR': {0: 'FramebufferTarget',
                                      1: 'FramebufferAttachment'},
 'glFrontFace': {0: 'FrontFaceDirection'},
 'glGenSymbolsEXT': {0: 'DataTypeEXT',
                     1: 'VertexShaderStorageTypeEXT',
                     2: 'ParameterRangeEXT'},
 'glGenerateMipmap': {0: 'TextureTarget'},
 'glGenerateMipmapEXT': {0: 'TextureTarget'},
 'glGenerateMultiTexMipmapEXT': {0: 'TextureUnit', 1: 'TextureTarget'},
 'glGenerateTextureMipmapEXT': {1: 'TextureTarget'},
 'glGetActiveAtomicCounterBufferiv': {2: 'AtomicCounterBufferPName'},
 'glGetActiveAttrib': {5: 'AttributeType'},
 'glGetActiveAttribARB': {5: 'AttributeType'},
 'glGetActiveSubroutineName': {1: 'ShaderType'},
 'glGetActiveSubroutineUniformName': {1: 'ShaderType'},
 'glGetActiveSubroutineUniformiv': {1: 'ShaderType',
                                    3: 'SubroutineParameterName'},
 'glGetActiveUniform': {5: 'UniformType'},
 'glGetActiveUniformARB': {5: 'UniformType'},
 'glGetActiveUniformBlockiv': {2: 'UniformBlockPName'},
 'glGetActiveUniformsiv': {3: 'UniformPName'},
 'glGetBooleanIndexedvEXT': {0: 'BufferTargetARB', 2: 'Boolean'},
 'glGetBooleani_v': {0: 'BufferTargetARB', 2: 'Boolean'},
 'glGetBooleanv': {0: 'GetPName', 1: 'Boolean'},
 'glGetBufferParameteri64v': {0: 'BufferTargetARB', 1: 'BufferPNameARB'},
 'glGetBufferParameteriv': {0: 'BufferTargetARB', 1: 'BufferPNameARB'},
 'glGetBufferParameterivARB': {0: 'BufferTargetARB', 1: 'BufferPNameARB'},
 'glGetBufferPointerv': {0: 'BufferTargetARB', 1: 'BufferPointerNameARB'},
 'glGetBufferPointervARB': {0: 'BufferTargetARB', 1: 'BufferPointerNameARB'},
 'glGetBufferSubData': {0: 'BufferTargetARB'},
 'glGetBufferSubDataARB': {0: 'BufferTargetARB'},
 'glGetClipPlane': {0: 'ClipPlaneName'},
 'glGetClipPlanef': {0: 'ClipPlaneName'},
 'glGetClipPlanex': {0: 'ClipPlaneName'},
 'glGetColorTable': {0: 'ColorTableTarget', 1: 'PixelFormat', 2: 'PixelType'},
 'glGetColorTableEXT': {0: 'ColorTableTarget',
                        1: 'PixelFormat',
                        2: 'PixelType'},
 'glGetColorTableParameterfv': {0: 'ColorTableTarget',
                                1: 'GetColorTableParameterPNameSGI'},
 'glGetColorTableParameterfvEXT': {0: 'ColorTableTarget',
                                   1: 'GetColorTableParameterPNameSGI'},
 'glGetColorTableParameteriv': {0: 'ColorTableTarget',
                                1: 'GetColorTableParameterPNameSGI'},
 'glGetColorTableParameterivEXT': {0: 'ColorTableTarget',
                                   1: 'GetColorTableParameterPNameSGI'},
 'glGetCompressedMultiTexImageEXT': {0: 'TextureUnit', 1: 'TextureTarget'},
 'glGetCompressedTexImage': {0: 'TextureTarget'},
 'glGetCompressedTexImageARB': {0: 'TextureTarget'},
 'glGetCompressedTextureImageEXT': {1: 'TextureTarget'},
 'glGetConvolutionFilter': {0: 'ConvolutionTarget',
                            1: 'PixelFormat',
                            2: 'PixelType'},
 'glGetConvolutionFilterEXT': {0: 'ConvolutionTargetEXT',
                               1: 'PixelFormat',
                               2: 'PixelType'},
 'glGetConvolutionParameterfv': {0: 'ConvolutionTarget',
                                 1: 'ConvolutionParameterEXT'},
 'glGetConvolutionParameterfvEXT': {0: 'ConvolutionTargetEXT',
                                    1: 'ConvolutionParameterEXT'},
 'glGetConvolutionParameteriv': {0: 'ConvolutionTarget',
                                 1: 'ConvolutionParameterEXT'},
 'glGetConvolutionParameterivEXT': {0: 'ConvolutionTargetEXT',
                                    1: 'ConvolutionParameterEXT'},
 'glGetDebugMessageLog': {2: 'DebugSource', 3: 'DebugType', 5: 'DebugSeverity'},
 'glGetDebugMessageLogARB': {2: 'DebugSource',
                             3: 'DebugType',
                             5: 'DebugSeverity'},
 'glGetDoublev': {0: 'GetPName'},
 'glGetFixedv': {0: 'GetPName'},
 'glGetFloatv': {0: 'GetPName'},
 'glGetFramebufferAttachmentParameteriv': {0: 'FramebufferTarget',
                                           1: 'FramebufferAttachment',
                                           2: 'FramebufferAttachmentParameterName'},
 'glGetFramebufferAttachmentParameterivEXT': {0: 'FramebufferTarget',
                                              1: 'FramebufferAttachment',
                                              2: 'FramebufferAttachmentParameterName'},
 'glGetFramebufferParameteriv': {0: 'FramebufferTarget',
                                 1: 'FramebufferAttachmentParameterName'},
 'glGetFramebufferParameterivEXT': {1: 'GetFramebufferParameter'},
 'glGetFramebufferPixelLocalStorageSizeEXT': {0: 'FramebufferTarget'},
 'glGetHistogram': {0: 'HistogramTargetEXT',
                    1: 'Boolean',
                    2: 'PixelFormat',
                    3: 'PixelType'},
 'glGetHistogramEXT': {0: 'HistogramTargetEXT',
                       1: 'Boolean',
                       2: 'PixelFormat',
                       3: 'PixelType'},
 'glGetHistogramParameterfv': {0: 'HistogramTargetEXT',
                               1: 'GetHistogramParameterPNameEXT'},
 'glGetHistogramParameterfvEXT': {0: 'HistogramTargetEXT',
                                  1: 'GetHistogramParameterPNameEXT'},
 'glGetHistogramParameteriv': {0: 'HistogramTargetEXT',
                               1: 'GetHistogramParameterPNameEXT'},
 'glGetHistogramParameterivEXT': {0: 'HistogramTargetEXT',
                                  1: 'GetHistogramParameterPNameEXT'},
 'glGetImageHandleARB': {4: 'PixelFormat'},
 'glGetImageTransformParameterfvHP': {0: 'ImageTransformTargetHP',
                                      1: 'ImageTransformPNameHP'},
 'glGetImageTransformParameterivHP': {0: 'ImageTransformTargetHP',
                                      1: 'ImageTransformPNameHP'},
 'glGetInteger64v': {0: 'GetPName'},
 'glGetIntegerv': {0: 'GetPName'},
 'glGetInternalformati64v': {0: 'TextureTarget',
                             1: 'InternalFormat',
                             2: 'InternalFormatPName'},
 'glGetInternalformativ': {0: 'TextureTarget',
                           1: 'InternalFormat',
                           2: 'InternalFormatPName'},
 'glGetInvariantBooleanvEXT': {1: 'GetVariantValueEXT', 2: 'Boolean'},
 'glGetInvariantFloatvEXT': {1: 'GetVariantValueEXT'},
 'glGetInvariantIntegervEXT': {1: 'GetVariantValueEXT'},
 'glGetLightfv': {0: 'LightName', 1: 'LightParameter'},
 'glGetLightiv': {0: 'LightName', 1: 'LightParameter'},
 'glGetLightxv': {0: 'LightName', 1: 'LightParameter'},
 'glGetLocalConstantBooleanvEXT': {1: 'GetVariantValueEXT', 2: 'Boolean'},
 'glGetLocalConstantFloatvEXT': {1: 'GetVariantValueEXT'},
 'glGetLocalConstantIntegervEXT': {1: 'GetVariantValueEXT'},
 'glGetMapdv': {0: 'MapTarget', 1: 'GetMapQuery'},
 'glGetMapfv': {0: 'MapTarget', 1: 'GetMapQuery'},
 'glGetMapiv': {0: 'MapTarget', 1: 'GetMapQuery'},
 'glGetMaterialfv': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glGetMaterialiv': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glGetMaterialxv': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glGetMemoryObjectParameterivEXT': {1: 'MemoryObjectParameterName'},
 'glGetMinmax': {0: 'MinmaxTargetEXT',
                 1: 'Boolean',
                 2: 'PixelFormat',
                 3: 'PixelType'},
 'glGetMinmaxEXT': {0: 'MinmaxTargetEXT',
                    1: 'Boolean',
                    2: 'PixelFormat',
                    3: 'PixelType'},
 'glGetMinmaxParameterfv': {0: 'MinmaxTargetEXT',
                            1: 'GetMinmaxParameterPNameEXT'},
 'glGetMinmaxParameterfvEXT': {0: 'MinmaxTargetEXT',
                               1: 'GetMinmaxParameterPNameEXT'},
 'glGetMinmaxParameteriv': {0: 'MinmaxTargetEXT',
                            1: 'GetMinmaxParameterPNameEXT'},
 'glGetMinmaxParameterivEXT': {0: 'MinmaxTargetEXT',
                               1: 'GetMinmaxParameterPNameEXT'},
 'glGetMultiTexEnvfvEXT': {0: 'TextureUnit',
                           1: 'TextureEnvTarget',
                           2: 'TextureEnvParameter'},
 'glGetMultiTexEnvivEXT': {0: 'TextureUnit',
                           1: 'TextureEnvTarget',
                           2: 'TextureEnvParameter'},
 'glGetMultiTexGendvEXT': {0: 'TextureUnit',
                           1: 'TextureCoordName',
                           2: 'TextureGenParameter'},
 'glGetMultiTexGenfvEXT': {0: 'TextureUnit',
                           1: 'TextureCoordName',
                           2: 'TextureGenParameter'},
 'glGetMultiTexGenivEXT': {0: 'TextureUnit',
                           1: 'TextureCoordName',
                           2: 'TextureGenParameter'},
 'glGetMultiTexImageEXT': {0: 'TextureUnit',
                           1: 'TextureTarget',
                           3: 'PixelFormat',
                           4: 'PixelType'},
 'glGetMultiTexLevelParameterfvEXT': {0: 'TextureUnit',
                                      1: 'TextureTarget',
                                      3: 'GetTextureParameter'},
 'glGetMultiTexLevelParameterivEXT': {0: 'TextureUnit',
                                      1: 'TextureTarget',
                                      3: 'GetTextureParameter'},
 'glGetMultiTexParameterIivEXT': {0: 'TextureUnit',
                                  1: 'TextureTarget',
                                  2: 'GetTextureParameter'},
 'glGetMultiTexParameterIuivEXT': {0: 'TextureUnit',
                                   1: 'TextureTarget',
                                   2: 'GetTextureParameter'},
 'glGetMultiTexParameterfvEXT': {0: 'TextureUnit',
                                 1: 'TextureTarget',
                                 2: 'GetTextureParameter'},
 'glGetMultiTexParameterivEXT': {0: 'TextureUnit',
                                 1: 'TextureTarget',
                                 2: 'GetTextureParameter'},
 'glGetMultisamplefv': {0: 'GetMultisamplePNameNV'},
 'glGetNamedBufferParameteri64v': {1: 'VertexBufferObjectParameter'},
 'glGetNamedBufferParameteriv': {1: 'VertexBufferObjectParameter'},
 'glGetNamedBufferParameterivEXT': {1: 'VertexBufferObjectParameter'},
 'glGetNamedBufferPointerv': {1: 'VertexBufferObjectParameter'},
 'glGetNamedBufferPointervEXT': {1: 'VertexBufferObjectParameter'},
 'glGetNamedFramebufferAttachmentParameteriv': {1: 'FramebufferAttachment',
                                                2: 'FramebufferAttachmentParameterName'},
 'glGetNamedFramebufferAttachmentParameterivEXT': {1: 'FramebufferAttachment',
                                                   2: 'FramebufferAttachmentParameterName'},
 'glGetNamedFramebufferParameteriv': {1: 'GetFramebufferParameter'},
 'glGetNamedFramebufferParameterivEXT': {1: 'GetFramebufferParameter'},
 'glGetNamedProgramLocalParameterIivEXT': {1: 'ProgramTarget'},
 'glGetNamedProgramLocalParameterIuivEXT': {1: 'ProgramTarget'},
 'glGetNamedProgramLocalParameterdvEXT': {1: 'ProgramTarget'},
 'glGetNamedProgramLocalParameterfvEXT': {1: 'ProgramTarget'},
 'glGetNamedProgramStringEXT': {1: 'ProgramTarget', 2: 'ProgramStringProperty'},
 'glGetNamedProgramivEXT': {1: 'ProgramTarget', 2: 'ProgramPropertyARB'},
 'glGetNamedRenderbufferParameteriv': {1: 'RenderbufferParameterName'},
 'glGetNamedRenderbufferParameterivEXT': {1: 'RenderbufferParameterName'},
 'glGetObjectLabel': {0: 'ObjectIdentifier'},
 'glGetPixelMapfv': {0: 'PixelMap'},
 'glGetPixelMapuiv': {0: 'PixelMap'},
 'glGetPixelMapusv': {0: 'PixelMap'},
 'glGetPixelMapxv': {0: 'PixelMap'},
 'glGetPointerv': {0: 'GetPointervPName'},
 'glGetPointervEXT': {0: 'GetPointervPName'},
 'glGetProgramEnvParameterdvARB': {0: 'ProgramTargetARB'},
 'glGetProgramEnvParameterfvARB': {0: 'ProgramTargetARB'},
 'glGetProgramInterfaceiv': {1: 'ProgramInterface', 2: 'ProgramInterfacePName'},
 'glGetProgramLocalParameterdvARB': {0: 'ProgramTargetARB'},
 'glGetProgramLocalParameterfvARB': {0: 'ProgramTargetARB'},
 'glGetProgramPipelineiv': {1: 'PipelineParameterName'},
 'glGetProgramPipelineivEXT': {1: 'PipelineParameterName'},
 'glGetProgramResourceIndex': {1: 'ProgramInterface'},
 'glGetProgramResourceLocation': {1: 'ProgramInterface'},
 'glGetProgramResourceLocationIndex': {1: 'ProgramInterface'},
 'glGetProgramResourceLocationIndexEXT': {1: 'ProgramInterface'},
 'glGetProgramResourceName': {1: 'ProgramInterface'},
 'glGetProgramResourceiv': {1: 'ProgramInterface',
                            4: 'ProgramResourceProperty'},
 'glGetProgramStageiv': {1: 'ShaderType', 2: 'ProgramStagePName'},
 'glGetProgramStringARB': {0: 'ProgramTargetARB',
                           1: 'ProgramStringPropertyARB'},
 'glGetProgramiv': {1: 'ProgramPropertyARB'},
 'glGetProgramivARB': {0: 'ProgramTargetARB', 1: 'ProgramPropertyARB'},
 'glGetQueryBufferObjecti64v': {2: 'QueryObjectParameterName'},
 'glGetQueryBufferObjectiv': {2: 'QueryObjectParameterName'},
 'glGetQueryBufferObjectui64v': {2: 'QueryObjectParameterName'},
 'glGetQueryBufferObjectuiv': {2: 'QueryObjectParameterName'},
 'glGetQueryIndexediv': {0: 'QueryTarget', 2: 'QueryParameterName'},
 'glGetQueryObjecti64v': {1: 'QueryObjectParameterName'},
 'glGetQueryObjecti64vEXT': {1: 'QueryObjectParameterName'},
 'glGetQueryObjectiv': {1: 'QueryObjectParameterName'},
 'glGetQueryObjectivARB': {1: 'QueryObjectParameterName'},
 'glGetQueryObjectivEXT': {1: 'QueryObjectParameterName'},
 'glGetQueryObjectui64v': {1: 'QueryObjectParameterName'},
 'glGetQueryObjectui64vEXT': {1: 'QueryObjectParameterName'},
 'glGetQueryObjectuiv': {1: 'QueryObjectParameterName'},
 'glGetQueryObjectuivARB': {1: 'QueryObjectParameterName'},
 'glGetQueryObjectuivEXT': {1: 'QueryObjectParameterName'},
 'glGetQueryiv': {0: 'QueryTarget', 1: 'QueryParameterName'},
 'glGetQueryivARB': {0: 'QueryTarget', 1: 'QueryParameterName'},
 'glGetQueryivEXT': {0: 'QueryTarget', 1: 'QueryParameterName'},
 'glGetRenderbufferParameteriv': {0: 'RenderbufferTarget',
                                  1: 'RenderbufferParameterName'},
 'glGetRenderbufferParameterivEXT': {0: 'RenderbufferTarget',
                                     1: 'RenderbufferParameterName'},
 'glGetSamplerParameterIiv': {1: 'SamplerParameterI'},
 'glGetSamplerParameterIivEXT': {1: 'SamplerParameterI'},
 'glGetSamplerParameterIuiv': {1: 'SamplerParameterI'},
 'glGetSamplerParameterIuivEXT': {1: 'SamplerParameterI'},
 'glGetSamplerParameterfv': {1: 'SamplerParameterF'},
 'glGetSamplerParameteriv': {1: 'SamplerParameterI'},
 'glGetSemaphoreParameterui64vEXT': {1: 'SemaphoreParameterName'},
 'glGetSeparableFilter': {0: 'SeparableTargetEXT',
                          1: 'PixelFormat',
                          2: 'PixelType'},
 'glGetSeparableFilterEXT': {0: 'SeparableTargetEXT',
                             1: 'PixelFormat',
                             2: 'PixelType'},
 'glGetShaderPrecisionFormat': {0: 'ShaderType', 1: 'PrecisionType'},
 'glGetShaderiv': {1: 'ShaderParameterName'},
 'glGetString': {0: 'StringName'},
 'glGetStringi': {0: 'StringName'},
 'glGetSubroutineIndex': {1: 'ShaderType'},
 'glGetSubroutineUniformLocation': {1: 'ShaderType'},
 'glGetSynciv': {1: 'SyncParameterName'},
 'glGetTexEnvfv': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glGetTexEnviv': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glGetTexEnvxv': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glGetTexGendv': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glGetTexGenfv': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glGetTexGeniv': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glGetTexImage': {0: 'TextureTarget', 2: 'PixelFormat', 3: 'PixelType'},
 'glGetTexLevelParameterfv': {0: 'TextureTarget', 2: 'GetTextureParameter'},
 'glGetTexLevelParameteriv': {0: 'TextureTarget', 2: 'GetTextureParameter'},
 'glGetTexParameterIiv': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glGetTexParameterIivEXT': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glGetTexParameterIuiv': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glGetTexParameterIuivEXT': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glGetTexParameterfv': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glGetTexParameteriv': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glGetTexParameterxv': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glGetTextureImage': {2: 'PixelFormat', 3: 'PixelType'},
 'glGetTextureImageEXT': {1: 'TextureTarget', 3: 'PixelFormat', 4: 'PixelType'},
 'glGetTextureLevelParameterfv': {2: 'GetTextureParameter'},
 'glGetTextureLevelParameterfvEXT': {1: 'TextureTarget',
                                     3: 'GetTextureParameter'},
 'glGetTextureLevelParameteriv': {2: 'GetTextureParameter'},
 'glGetTextureLevelParameterivEXT': {1: 'TextureTarget',
                                     3: 'GetTextureParameter'},
 'glGetTextureParameterIiv': {1: 'GetTextureParameter'},
 'glGetTextureParameterIivEXT': {1: 'TextureTarget', 2: 'GetTextureParameter'},
 'glGetTextureParameterIuiv': {1: 'GetTextureParameter'},
 'glGetTextureParameterIuivEXT': {1: 'TextureTarget', 2: 'GetTextureParameter'},
 'glGetTextureParameterfv': {1: 'GetTextureParameter'},
 'glGetTextureParameterfvEXT': {1: 'TextureTarget', 2: 'GetTextureParameter'},
 'glGetTextureParameteriv': {1: 'GetTextureParameter'},
 'glGetTextureParameterivEXT': {1: 'TextureTarget', 2: 'GetTextureParameter'},
 'glGetTextureSubImage': {8: 'PixelFormat', 9: 'PixelType'},
 'glGetTransformFeedbackVarying': {5: 'GlslTypeToken'},
 'glGetTransformFeedbackVaryingEXT': {5: 'GlslTypeToken'},
 'glGetTransformFeedbacki64_v': {1: 'TransformFeedbackPName'},
 'glGetTransformFeedbacki_v': {1: 'TransformFeedbackPName'},
 'glGetTransformFeedbackiv': {1: 'TransformFeedbackPName'},
 'glGetUniformSubroutineuiv': {0: 'ShaderType'},
 'glGetUnsignedBytevEXT': {0: 'GetPName'},
 'glGetVariantBooleanvEXT': {1: 'GetVariantValueEXT', 2: 'Boolean'},
 'glGetVariantFloatvEXT': {1: 'GetVariantValueEXT'},
 'glGetVariantIntegervEXT': {1: 'GetVariantValueEXT'},
 'glGetVariantPointervEXT': {1: 'GetVariantValueEXT'},
 'glGetVertexArrayIndexed64iv': {2: 'VertexArrayPName'},
 'glGetVertexArrayIndexediv': {2: 'VertexArrayPName'},
 'glGetVertexArrayIntegeri_vEXT': {2: 'VertexArrayPName'},
 'glGetVertexArrayIntegervEXT': {1: 'VertexArrayPName'},
 'glGetVertexArrayPointeri_vEXT': {2: 'VertexArrayPName'},
 'glGetVertexArrayPointervEXT': {1: 'VertexArrayPName'},
 'glGetVertexArrayiv': {1: 'VertexArrayPName'},
 'glGetVertexAttribIiv': {1: 'VertexAttribEnum'},
 'glGetVertexAttribIivEXT': {1: 'VertexAttribEnum'},
 'glGetVertexAttribIuiv': {1: 'VertexAttribEnum'},
 'glGetVertexAttribIuivEXT': {1: 'VertexAttribEnum'},
 'glGetVertexAttribLdv': {1: 'VertexAttribEnum'},
 'glGetVertexAttribLdvEXT': {1: 'VertexAttribEnum'},
 'glGetVertexAttribLui64vARB': {1: 'VertexAttribEnum'},
 'glGetVertexAttribPointerv': {1: 'VertexAttribPointerPropertyARB'},
 'glGetVertexAttribPointervARB': {1: 'VertexAttribPointerPropertyARB'},
 'glGetVertexAttribdv': {1: 'VertexAttribPropertyARB'},
 'glGetVertexAttribdvARB': {1: 'VertexAttribPropertyARB'},
 'glGetVertexAttribfv': {1: 'VertexAttribPropertyARB'},
 'glGetVertexAttribfvARB': {1: 'VertexAttribPropertyARB'},
 'glGetVertexAttribiv': {1: 'VertexAttribPropertyARB'},
 'glGetVertexAttribivARB': {1: 'VertexAttribPropertyARB'},
 'glGetnColorTable': {0: 'ColorTableTarget', 1: 'PixelFormat', 2: 'PixelType'},
 'glGetnColorTableARB': {0: 'ColorTableTarget',
                         1: 'PixelFormat',
                         2: 'PixelType'},
 'glGetnCompressedTexImage': {0: 'TextureTarget'},
 'glGetnCompressedTexImageARB': {0: 'TextureTarget'},
 'glGetnConvolutionFilter': {0: 'ConvolutionTarget',
                             1: 'PixelFormat',
                             2: 'PixelType'},
 'glGetnConvolutionFilterARB': {0: 'ConvolutionTarget',
                                1: 'PixelFormat',
                                2: 'PixelType'},
 'glGetnHistogram': {0: 'HistogramTargetEXT', 2: 'PixelFormat', 3: 'PixelType'},
 'glGetnHistogramARB': {0: 'HistogramTargetEXT',
                        1: 'Boolean',
                        2: 'PixelFormat',
                        3: 'PixelType'},
 'glGetnMapdv': {0: 'MapTarget', 1: 'MapQuery'},
 'glGetnMapdvARB': {0: 'MapTarget', 1: 'MapQuery'},
 'glGetnMapfv': {0: 'MapTarget', 1: 'MapQuery'},
 'glGetnMapfvARB': {0: 'MapTarget', 1: 'MapQuery'},
 'glGetnMapiv': {0: 'MapTarget', 1: 'MapQuery'},
 'glGetnMapivARB': {0: 'MapTarget', 1: 'MapQuery'},
 'glGetnMinmax': {0: 'MinmaxTargetEXT', 2: 'PixelFormat', 3: 'PixelType'},
 'glGetnMinmaxARB': {0: 'MinmaxTargetEXT',
                     1: 'Boolean',
                     2: 'PixelFormat',
                     3: 'PixelType'},
 'glGetnPixelMapfv': {0: 'PixelMap'},
 'glGetnPixelMapfvARB': {0: 'PixelMap'},
 'glGetnPixelMapuiv': {0: 'PixelMap'},
 'glGetnPixelMapuivARB': {0: 'PixelMap'},
 'glGetnPixelMapusv': {0: 'PixelMap'},
 'glGetnPixelMapusvARB': {0: 'PixelMap'},
 'glGetnSeparableFilter': {0: 'SeparableTargetEXT',
                           1: 'PixelFormat',
                           2: 'PixelType'},
 'glGetnSeparableFilterARB': {0: 'SeparableTargetEXT',
                              1: 'PixelFormat',
                              2: 'PixelType'},
 'glGetnTexImage': {0: 'TextureTarget', 2: 'PixelFormat', 3: 'PixelType'},
 'glGetnTexImageARB': {0: 'TextureTarget', 2: 'PixelFormat', 3: 'PixelType'},
 'glHint': {0: 'HintTarget', 1: 'HintMode'},
 'glHistogram': {0: 'HistogramTargetEXT', 2: 'InternalFormat', 3: 'Boolean'},
 'glHistogramEXT': {0: 'HistogramTargetEXT', 2: 'InternalFormat', 3: 'Boolean'},
 'glImageTransformParameterfHP': {0: 'ImageTransformTargetHP',
                                  1: 'ImageTransformPNameHP'},
 'glImageTransformParameterfvHP': {0: 'ImageTransformTargetHP',
                                   1: 'ImageTransformPNameHP'},
 'glImageTransformParameteriHP': {0: 'ImageTransformTargetHP',
                                  1: 'ImageTransformPNameHP'},
 'glImageTransformParameterivHP': {0: 'ImageTransformTargetHP',
                                   1: 'ImageTransformPNameHP'},
 'glImportMemoryFdEXT': {2: 'ExternalHandleType'},
 'glImportMemoryWin32HandleEXT': {2: 'ExternalHandleType'},
 'glImportMemoryWin32NameEXT': {2: 'ExternalHandleType'},
 'glImportSemaphoreFdEXT': {1: 'ExternalHandleType'},
 'glImportSemaphoreWin32HandleEXT': {1: 'ExternalHandleType'},
 'glImportSemaphoreWin32NameEXT': {1: 'ExternalHandleType'},
 'glIndexFuncEXT': {0: 'IndexFunctionEXT'},
 'glIndexMaterialEXT': {0: 'MaterialFace', 1: 'IndexMaterialParameterEXT'},
 'glIndexPointer': {0: 'IndexPointerType'},
 'glIndexPointerEXT': {0: 'IndexPointerType'},
 'glInterleavedArrays': {0: 'InterleavedArrayFormat'},
 'glInvalidateFramebuffer': {0: 'FramebufferTarget',
                             2: 'InvalidateFramebufferAttachment'},
 'glInvalidateNamedFramebufferData': {2: 'FramebufferAttachment'},
 'glInvalidateNamedFramebufferSubData': {2: 'FramebufferAttachment'},
 'glInvalidateSubFramebuffer': {0: 'FramebufferTarget',
                                2: 'InvalidateFramebufferAttachment'},
 'glIsEnabled': {0: 'EnableCap'},
 'glIsEnabledIndexedEXT': {0: 'EnableCap'},
 'glIsEnabledi': {0: 'EnableCap'},
 'glIsEnablediEXT': {0: 'EnableCap'},
 'glIsVariantEnabledEXT': {1: 'VariantCapEXT'},
 'glLightModelf': {0: 'LightModelParameter'},
 'glLightModelfv': {0: 'LightModelParameter'},
 'glLightModeli': {0: 'LightModelParameter'},
 'glLightModeliv': {0: 'LightModelParameter'},
 'glLightModelx': {0: 'LightModelParameter'},
 'glLightModelxv': {0: 'LightModelParameter'},
 'glLightf': {0: 'LightName', 1: 'LightParameter'},
 'glLightfv': {0: 'LightName', 1: 'LightParameter'},
 'glLighti': {0: 'LightName', 1: 'LightParameter'},
 'glLightiv': {0: 'LightName', 1: 'LightParameter'},
 'glLightx': {0: 'LightName', 1: 'LightParameter'},
 'glLightxv': {0: 'LightName', 1: 'LightParameter'},
 'glLogicOp': {0: 'LogicOp'},
 'glMap1d': {0: 'MapTarget'},
 'glMap1f': {0: 'MapTarget'},
 'glMap2d': {0: 'MapTarget'},
 'glMap2f': {0: 'MapTarget'},
 'glMapBuffer': {0: 'BufferTargetARB', 1: 'BufferAccessARB'},
 'glMapBufferARB': {0: 'BufferTargetARB', 1: 'BufferAccessARB'},
 'glMapBufferRange': {0: 'BufferTargetARB', 3: 'MapBufferAccessMask'},
 'glMapBufferRangeEXT': {0: 'BufferTargetARB', 3: 'MapBufferAccessMask'},
 'glMapNamedBuffer': {1: 'BufferAccessARB'},
 'glMapNamedBufferEXT': {1: 'BufferAccessARB'},
 'glMapNamedBufferRange': {3: 'MapBufferAccessMask'},
 'glMapNamedBufferRangeEXT': {3: 'MapBufferAccessMask'},
 'glMaterialf': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glMaterialfv': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glMateriali': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glMaterialiv': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glMaterialx': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glMaterialxv': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glMatrixFrustumEXT': {0: 'MatrixMode'},
 'glMatrixIndexPointerARB': {1: 'MatrixIndexPointerTypeARB'},
 'glMatrixLoadIdentityEXT': {0: 'MatrixMode'},
 'glMatrixLoadTransposedEXT': {0: 'MatrixMode'},
 'glMatrixLoadTransposefEXT': {0: 'MatrixMode'},
 'glMatrixLoaddEXT': {0: 'MatrixMode'},
 'glMatrixLoadfEXT': {0: 'MatrixMode'},
 'glMatrixMode': {0: 'MatrixMode'},
 'glMatrixMultTransposedEXT': {0: 'MatrixMode'},
 'glMatrixMultTransposefEXT': {0: 'MatrixMode'},
 'glMatrixMultdEXT': {0: 'MatrixMode'},
 'glMatrixMultfEXT': {0: 'MatrixMode'},
 'glMatrixOrthoEXT': {0: 'MatrixMode'},
 'glMatrixPopEXT': {0: 'MatrixMode'},
 'glMatrixPushEXT': {0: 'MatrixMode'},
 'glMatrixRotatedEXT': {0: 'MatrixMode'},
 'glMatrixRotatefEXT': {0: 'MatrixMode'},
 'glMatrixScaledEXT': {0: 'MatrixMode'},
 'glMatrixScalefEXT': {0: 'MatrixMode'},
 'glMatrixTranslatedEXT': {0: 'MatrixMode'},
 'glMatrixTranslatefEXT': {0: 'MatrixMode'},
 'glMemoryBarrier': {0: 'MemoryBarrierMask'},
 'glMemoryBarrierByRegion': {0: 'MemoryBarrierMask'},
 'glMemoryBarrierEXT': {0: 'MemoryBarrierMask'},
 'glMemoryObjectParameterivEXT': {1: 'MemoryObjectParameterName'},
 'glMinmax': {0: 'MinmaxTargetEXT', 1: 'InternalFormat', 2: 'Boolean'},
 'glMinmaxEXT': {0: 'MinmaxTargetEXT', 1: 'InternalFormat', 2: 'Boolean'},
 'glMultiDrawArrays': {0: 'PrimitiveType'},
 'glMultiDrawArraysEXT': {0: 'PrimitiveType'},
 'glMultiDrawArraysIndirect': {0: 'PrimitiveType'},
 'glMultiDrawArraysIndirectCount': {0: 'PrimitiveType'},
 'glMultiDrawArraysIndirectCountARB': {0: 'PrimitiveType'},
 'glMultiDrawArraysIndirectEXT': {0: 'PrimitiveType'},
 'glMultiDrawElements': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glMultiDrawElementsBaseVertex': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glMultiDrawElementsBaseVertexEXT': {0: 'PrimitiveType',
                                      2: 'DrawElementsType'},
 'glMultiDrawElementsEXT': {0: 'PrimitiveType', 2: 'DrawElementsType'},
 'glMultiDrawElementsIndirect': {0: 'PrimitiveType', 1: 'DrawElementsType'},
 'glMultiDrawElementsIndirectCount': {0: 'PrimitiveType',
                                      1: 'DrawElementsType'},
 'glMultiDrawElementsIndirectCountARB': {0: 'PrimitiveType',
                                         1: 'DrawElementsType'},
 'glMultiDrawElementsIndirectEXT': {0: 'PrimitiveType', 1: 'DrawElementsType'},
 'glMultiTexBufferEXT': {0: 'TextureUnit', 1: 'TextureTarget'},
 'glMultiTexCoord1d': {0: 'TextureUnit'},
 'glMultiTexCoord1dARB': {0: 'TextureUnit'},
 'glMultiTexCoord1dv': {0: 'TextureUnit'},
 'glMultiTexCoord1dvARB': {0: 'TextureUnit'},
 'glMultiTexCoord1f': {0: 'TextureUnit'},
 'glMultiTexCoord1fARB': {0: 'TextureUnit'},
 'glMultiTexCoord1fv': {0: 'TextureUnit'},
 'glMultiTexCoord1fvARB': {0: 'TextureUnit'},
 'glMultiTexCoord1i': {0: 'TextureUnit'},
 'glMultiTexCoord1iARB': {0: 'TextureUnit'},
 'glMultiTexCoord1iv': {0: 'TextureUnit'},
 'glMultiTexCoord1ivARB': {0: 'TextureUnit'},
 'glMultiTexCoord1s': {0: 'TextureUnit'},
 'glMultiTexCoord1sARB': {0: 'TextureUnit'},
 'glMultiTexCoord1sv': {0: 'TextureUnit'},
 'glMultiTexCoord1svARB': {0: 'TextureUnit'},
 'glMultiTexCoord2d': {0: 'TextureUnit'},
 'glMultiTexCoord2dARB': {0: 'TextureUnit'},
 'glMultiTexCoord2dv': {0: 'TextureUnit'},
 'glMultiTexCoord2dvARB': {0: 'TextureUnit'},
 'glMultiTexCoord2f': {0: 'TextureUnit'},
 'glMultiTexCoord2fARB': {0: 'TextureUnit'},
 'glMultiTexCoord2fv': {0: 'TextureUnit'},
 'glMultiTexCoord2fvARB': {0: 'TextureUnit'},
 'glMultiTexCoord2i': {0: 'TextureUnit'},
 'glMultiTexCoord2iARB': {0: 'TextureUnit'},
 'glMultiTexCoord2iv': {0: 'TextureUnit'},
 'glMultiTexCoord2ivARB': {0: 'TextureUnit'},
 'glMultiTexCoord2s': {0: 'TextureUnit'},
 'glMultiTexCoord2sARB': {0: 'TextureUnit'},
 'glMultiTexCoord2sv': {0: 'TextureUnit'},
 'glMultiTexCoord2svARB': {0: 'TextureUnit'},
 'glMultiTexCoord3d': {0: 'TextureUnit'},
 'glMultiTexCoord3dARB': {0: 'TextureUnit'},
 'glMultiTexCoord3dv': {0: 'TextureUnit'},
 'glMultiTexCoord3dvARB': {0: 'TextureUnit'},
 'glMultiTexCoord3f': {0: 'TextureUnit'},
 'glMultiTexCoord3fARB': {0: 'TextureUnit'},
 'glMultiTexCoord3fv': {0: 'TextureUnit'},
 'glMultiTexCoord3fvARB': {0: 'TextureUnit'},
 'glMultiTexCoord3i': {0: 'TextureUnit'},
 'glMultiTexCoord3iARB': {0: 'TextureUnit'},
 'glMultiTexCoord3iv': {0: 'TextureUnit'},
 'glMultiTexCoord3ivARB': {0: 'TextureUnit'},
 'glMultiTexCoord3s': {0: 'TextureUnit'},
 'glMultiTexCoord3sARB': {0: 'TextureUnit'},
 'glMultiTexCoord3sv': {0: 'TextureUnit'},
 'glMultiTexCoord3svARB': {0: 'TextureUnit'},
 'glMultiTexCoord4d': {0: 'TextureUnit'},
 'glMultiTexCoord4dARB': {0: 'TextureUnit'},
 'glMultiTexCoord4dv': {0: 'TextureUnit'},
 'glMultiTexCoord4dvARB': {0: 'TextureUnit'},
 'glMultiTexCoord4f': {0: 'TextureUnit'},
 'glMultiTexCoord4fARB': {0: 'TextureUnit'},
 'glMultiTexCoord4fv': {0: 'TextureUnit'},
 'glMultiTexCoord4fvARB': {0: 'TextureUnit'},
 'glMultiTexCoord4i': {0: 'TextureUnit'},
 'glMultiTexCoord4iARB': {0: 'TextureUnit'},
 'glMultiTexCoord4iv': {0: 'TextureUnit'},
 'glMultiTexCoord4ivARB': {0: 'TextureUnit'},
 'glMultiTexCoord4s': {0: 'TextureUnit'},
 'glMultiTexCoord4sARB': {0: 'TextureUnit'},
 'glMultiTexCoord4sv': {0: 'TextureUnit'},
 'glMultiTexCoord4svARB': {0: 'TextureUnit'},
 'glMultiTexCoord4x': {0: 'TextureUnit'},
 'glMultiTexCoordP1ui': {0: 'TextureUnit', 1: 'TexCoordPointerType'},
 'glMultiTexCoordP1uiv': {0: 'TextureUnit', 1: 'TexCoordPointerType'},
 'glMultiTexCoordP2ui': {0: 'TextureUnit', 1: 'TexCoordPointerType'},
 'glMultiTexCoordP2uiv': {0: 'TextureUnit', 1: 'TexCoordPointerType'},
 'glMultiTexCoordP3ui': {0: 'TextureUnit', 1: 'TexCoordPointerType'},
 'glMultiTexCoordP3uiv': {0: 'TextureUnit', 1: 'TexCoordPointerType'},
 'glMultiTexCoordP4ui': {0: 'TextureUnit', 1: 'TexCoordPointerType'},
 'glMultiTexCoordP4uiv': {0: 'TextureUnit', 1: 'TexCoordPointerType'},
 'glMultiTexCoordPointerEXT': {0: 'TextureUnit', 2: 'TexCoordPointerType'},
 'glMultiTexEnvfEXT': {0: 'TextureUnit',
                       1: 'TextureEnvTarget',
                       2: 'TextureEnvParameter'},
 'glMultiTexEnvfvEXT': {0: 'TextureUnit',
                        1: 'TextureEnvTarget',
                        2: 'TextureEnvParameter'},
 'glMultiTexEnviEXT': {0: 'TextureUnit',
                       1: 'TextureEnvTarget',
                       2: 'TextureEnvParameter'},
 'glMultiTexEnvivEXT': {0: 'TextureUnit',
                        1: 'TextureEnvTarget',
                        2: 'TextureEnvParameter'},
 'glMultiTexGendEXT': {0: 'TextureUnit',
                       1: 'TextureCoordName',
                       2: 'TextureGenParameter'},
 'glMultiTexGendvEXT': {0: 'TextureUnit',
                        1: 'TextureCoordName',
                        2: 'TextureGenParameter'},
 'glMultiTexGenfEXT': {0: 'TextureUnit',
                       1: 'TextureCoordName',
                       2: 'TextureGenParameter'},
 'glMultiTexGenfvEXT': {0: 'TextureUnit',
                        1: 'TextureCoordName',
                        2: 'TextureGenParameter'},
 'glMultiTexGeniEXT': {0: 'TextureUnit',
                       1: 'TextureCoordName',
                       2: 'TextureGenParameter'},
 'glMultiTexGenivEXT': {0: 'TextureUnit',
                        1: 'TextureCoordName',
                        2: 'TextureGenParameter'},
 'glMultiTexImage1DEXT': {0: 'TextureUnit',
                          1: 'TextureTarget',
                          3: 'InternalFormat',
                          6: 'PixelFormat',
                          7: 'PixelType'},
 'glMultiTexImage2DEXT': {0: 'TextureUnit',
                          1: 'TextureTarget',
                          3: 'InternalFormat',
                          7: 'PixelFormat',
                          8: 'PixelType'},
 'glMultiTexImage3DEXT': {0: 'TextureUnit',
                          1: 'TextureTarget',
                          3: 'InternalFormat',
                          8: 'PixelFormat',
                          9: 'PixelType'},
 'glMultiTexParameterIivEXT': {0: 'TextureUnit',
                               1: 'TextureTarget',
                               2: 'TextureParameterName'},
 'glMultiTexParameterIuivEXT': {0: 'TextureUnit',
                                1: 'TextureTarget',
                                2: 'TextureParameterName'},
 'glMultiTexParameterfEXT': {0: 'TextureUnit',
                             1: 'TextureTarget',
                             2: 'TextureParameterName'},
 'glMultiTexParameterfvEXT': {0: 'TextureUnit',
                              1: 'TextureTarget',
                              2: 'TextureParameterName'},
 'glMultiTexParameteriEXT': {0: 'TextureUnit',
                             1: 'TextureTarget',
                             2: 'TextureParameterName'},
 'glMultiTexParameterivEXT': {0: 'TextureUnit',
                              1: 'TextureTarget',
                              2: 'TextureParameterName'},
 'glMultiTexRenderbufferEXT': {0: 'TextureUnit', 1: 'TextureTarget'},
 'glMultiTexSubImage1DEXT': {0: 'TextureUnit',
                             1: 'TextureTarget',
                             5: 'PixelFormat',
                             6: 'PixelType'},
 'glMultiTexSubImage2DEXT': {0: 'TextureUnit',
                             1: 'TextureTarget',
                             7: 'PixelFormat',
                             8: 'PixelType'},
 'glMultiTexSubImage3DEXT': {0: 'TextureUnit',
                             1: 'TextureTarget',
                             9: 'PixelFormat',
                             10: 'PixelType'},
 'glNamedBufferData': {3: 'VertexBufferObjectUsage'},
 'glNamedBufferDataEXT': {3: 'VertexBufferObjectUsage'},
 'glNamedBufferStorage': {3: 'BufferStorageMask'},
 'glNamedBufferStorageEXT': {3: 'BufferStorageMask'},
 'glNamedBufferStorageExternalEXT': {4: 'BufferStorageMask'},
 'glNamedFramebufferDrawBuffer': {1: 'ColorBuffer'},
 'glNamedFramebufferDrawBuffers': {2: 'ColorBuffer'},
 'glNamedFramebufferParameteri': {1: 'FramebufferParameterName'},
 'glNamedFramebufferParameteriEXT': {1: 'FramebufferParameterName'},
 'glNamedFramebufferReadBuffer': {1: 'ColorBuffer'},
 'glNamedFramebufferRenderbuffer': {1: 'FramebufferAttachment',
                                    2: 'RenderbufferTarget'},
 'glNamedFramebufferRenderbufferEXT': {1: 'FramebufferAttachment',
                                       2: 'RenderbufferTarget'},
 'glNamedFramebufferTexture': {1: 'FramebufferAttachment'},
 'glNamedFramebufferTexture1DEXT': {1: 'FramebufferAttachment',
                                    2: 'TextureTarget'},
 'glNamedFramebufferTexture2DEXT': {1: 'FramebufferAttachment',
                                    2: 'TextureTarget'},
 'glNamedFramebufferTexture3DEXT': {1: 'FramebufferAttachment',
                                    2: 'TextureTarget'},
 'glNamedFramebufferTextureEXT': {1: 'FramebufferAttachment'},
 'glNamedFramebufferTextureFaceEXT': {1: 'FramebufferAttachment',
                                      4: 'TextureTarget'},
 'glNamedFramebufferTextureLayer': {1: 'FramebufferAttachment'},
 'glNamedFramebufferTextureLayerEXT': {1: 'FramebufferAttachment'},
 'glNamedProgramLocalParameter4dEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParameter4dvEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParameter4fEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParameter4fvEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParameterI4iEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParameterI4ivEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParameterI4uiEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParameterI4uivEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParameters4fvEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParametersI4ivEXT': {1: 'ProgramTarget'},
 'glNamedProgramLocalParametersI4uivEXT': {1: 'ProgramTarget'},
 'glNamedProgramStringEXT': {1: 'ProgramTarget', 2: 'ProgramFormat'},
 'glNamedRenderbufferStorage': {1: 'InternalFormat'},
 'glNamedRenderbufferStorageEXT': {1: 'InternalFormat'},
 'glNamedRenderbufferStorageMultisample': {2: 'InternalFormat'},
 'glNamedRenderbufferStorageMultisampleCoverageEXT': {3: 'InternalFormat'},
 'glNamedRenderbufferStorageMultisampleEXT': {2: 'InternalFormat'},
 'glNewList': {1: 'ListMode'},
 'glNormalP3ui': {0: 'NormalPointerType'},
 'glNormalP3uiv': {0: 'NormalPointerType'},
 'glNormalPointer': {0: 'NormalPointerType'},
 'glNormalPointerEXT': {0: 'NormalPointerType'},
 'glObjectLabel': {0: 'ObjectIdentifier'},
 'glPatchParameterfv': {0: 'PatchParameterName'},
 'glPatchParameteri': {0: 'PatchParameterName'},
 'glPatchParameteriEXT': {0: 'PatchParameterName'},
 'glPixelMapfv': {0: 'PixelMap'},
 'glPixelMapuiv': {0: 'PixelMap'},
 'glPixelMapusv': {0: 'PixelMap'},
 'glPixelMapx': {0: 'PixelMap'},
 'glPixelStoref': {0: 'PixelStoreParameter'},
 'glPixelStorei': {0: 'PixelStoreParameter'},
 'glPixelStorex': {0: 'PixelStoreParameter'},
 'glPixelTransferf': {0: 'PixelTransferParameter'},
 'glPixelTransferi': {0: 'PixelTransferParameter'},
 'glPixelTransformParameterfEXT': {0: 'PixelTransformTargetEXT',
                                   1: 'PixelTransformPNameEXT'},
 'glPixelTransformParameterfvEXT': {0: 'PixelTransformTargetEXT',
                                    1: 'PixelTransformPNameEXT'},
 'glPixelTransformParameteriEXT': {0: 'PixelTransformTargetEXT',
                                   1: 'PixelTransformPNameEXT'},
 'glPixelTransformParameterivEXT': {0: 'PixelTransformTargetEXT',
                                    1: 'PixelTransformPNameEXT'},
 'glPointParameterf': {0: 'PointParameterNameARB'},
 'glPointParameterfARB': {0: 'PointParameterNameARB'},
 'glPointParameterfEXT': {0: 'PointParameterNameARB'},
 'glPointParameterfv': {0: 'PointParameterNameARB'},
 'glPointParameterfvARB': {0: 'PointParameterNameARB'},
 'glPointParameterfvEXT': {0: 'PointParameterNameARB'},
 'glPointParameteri': {0: 'PointParameterNameARB'},
 'glPointParameteriv': {0: 'PointParameterNameARB'},
 'glPointParameterx': {0: 'PointParameterNameARB'},
 'glPointParameterxv': {0: 'PointParameterNameARB'},
 'glPolygonMode': {0: 'MaterialFace', 1: 'PolygonMode'},
 'glProgramEnvParameter4dARB': {0: 'ProgramTargetARB'},
 'glProgramEnvParameter4dvARB': {0: 'ProgramTargetARB'},
 'glProgramEnvParameter4fARB': {0: 'ProgramTargetARB'},
 'glProgramEnvParameter4fvARB': {0: 'ProgramTargetARB'},
 'glProgramEnvParameters4fvEXT': {0: 'ProgramTargetARB'},
 'glProgramLocalParameter4dARB': {0: 'ProgramTargetARB'},
 'glProgramLocalParameter4dvARB': {0: 'ProgramTargetARB'},
 'glProgramLocalParameter4fARB': {0: 'ProgramTargetARB'},
 'glProgramLocalParameter4fvARB': {0: 'ProgramTargetARB'},
 'glProgramLocalParameters4fvEXT': {0: 'ProgramTargetARB'},
 'glProgramParameteri': {1: 'ProgramParameterPName'},
 'glProgramParameteriARB': {1: 'ProgramParameterPName'},
 'glProgramParameteriEXT': {1: 'ProgramParameterPName'},
 'glProgramStringARB': {0: 'ProgramTargetARB', 1: 'ProgramFormatARB'},
 'glProgramUniformMatrix2dv': {3: 'Boolean'},
 'glProgramUniformMatrix2dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix2fv': {3: 'Boolean'},
 'glProgramUniformMatrix2fvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix2x3dv': {3: 'Boolean'},
 'glProgramUniformMatrix2x3dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix2x3fv': {3: 'Boolean'},
 'glProgramUniformMatrix2x3fvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix2x4dv': {3: 'Boolean'},
 'glProgramUniformMatrix2x4dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix2x4fv': {3: 'Boolean'},
 'glProgramUniformMatrix2x4fvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix3dv': {3: 'Boolean'},
 'glProgramUniformMatrix3dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix3fv': {3: 'Boolean'},
 'glProgramUniformMatrix3fvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix3x2dv': {3: 'Boolean'},
 'glProgramUniformMatrix3x2dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix3x2fv': {3: 'Boolean'},
 'glProgramUniformMatrix3x2fvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix3x4dv': {3: 'Boolean'},
 'glProgramUniformMatrix3x4dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix3x4fv': {3: 'Boolean'},
 'glProgramUniformMatrix3x4fvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix4dv': {3: 'Boolean'},
 'glProgramUniformMatrix4dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix4fv': {3: 'Boolean'},
 'glProgramUniformMatrix4fvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix4x2dv': {3: 'Boolean'},
 'glProgramUniformMatrix4x2dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix4x2fv': {3: 'Boolean'},
 'glProgramUniformMatrix4x2fvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix4x3dv': {3: 'Boolean'},
 'glProgramUniformMatrix4x3dvEXT': {3: 'Boolean'},
 'glProgramUniformMatrix4x3fv': {3: 'Boolean'},
 'glProgramUniformMatrix4x3fvEXT': {3: 'Boolean'},
 'glProvokingVertex': {0: 'VertexProvokingMode'},
 'glProvokingVertexEXT': {0: 'VertexProvokingMode'},
 'glPushAttrib': {0: 'AttribMask'},
 'glPushClientAttrib': {0: 'ClientAttribMask'},
 'glPushClientAttribDefaultEXT': {0: 'ClientAttribMask'},
 'glPushDebugGroup': {0: 'DebugSource'},
 'glQueryCounter': {1: 'QueryCounterTarget'},
 'glQueryCounterEXT': {1: 'QueryCounterTarget'},
 'glReadBuffer': {0: 'ReadBufferMode'},
 'glReadBufferIndexedEXT': {0: 'ReadBufferMode'},
 'glReadPixels': {4: 'PixelFormat', 5: 'PixelType'},
 'glReadnPixels': {4: 'PixelFormat', 5: 'PixelType'},
 'glReadnPixelsARB': {4: 'PixelFormat', 5: 'PixelType'},
 'glReadnPixelsEXT': {4: 'PixelFormat', 5: 'PixelType'},
 'glRenderMode': {0: 'RenderingMode'},
 'glRenderbufferStorage': {0: 'RenderbufferTarget', 1: 'InternalFormat'},
 'glRenderbufferStorageEXT': {0: 'RenderbufferTarget', 1: 'InternalFormat'},
 'glRenderbufferStorageMultisample': {0: 'RenderbufferTarget',
                                      2: 'InternalFormat'},
 'glRenderbufferStorageMultisampleANGLE': {0: 'RenderbufferTarget',
                                           2: 'InternalFormat'},
 'glRenderbufferStorageMultisampleEXT': {0: 'RenderbufferTarget',
                                         2: 'InternalFormat'},
 'glRenderbufferStorageMultisampleIMG': {0: 'RenderbufferTarget',
                                         2: 'InternalFormat'},
 'glResetHistogram': {0: 'HistogramTargetEXT'},
 'glResetHistogramEXT': {0: 'HistogramTargetEXT'},
 'glResetMinmax': {0: 'MinmaxTargetEXT'},
 'glResetMinmaxEXT': {0: 'MinmaxTargetEXT'},
 'glSampleCoverage': {1: 'Boolean'},
 'glSampleCoverageARB': {1: 'Boolean'},
 'glSampleMaskEXT': {1: 'Boolean'},
 'glSamplePatternEXT': {0: 'SamplePatternEXT'},
 'glSamplerParameterIiv': {1: 'SamplerParameterI'},
 'glSamplerParameterIivEXT': {1: 'SamplerParameterI'},
 'glSamplerParameterIuiv': {1: 'SamplerParameterI'},
 'glSamplerParameterIuivEXT': {1: 'SamplerParameterI'},
 'glSamplerParameterf': {1: 'SamplerParameterF'},
 'glSamplerParameterfv': {1: 'SamplerParameterF'},
 'glSamplerParameteri': {1: 'SamplerParameterI'},
 'glSamplerParameteriv': {1: 'SamplerParameterI'},
 'glSecondaryColorP3ui': {0: 'ColorPointerType'},
 'glSecondaryColorP3uiv': {0: 'ColorPointerType'},
 'glSecondaryColorPointer': {1: 'ColorPointerType'},
 'glSecondaryColorPointerEXT': {1: 'ColorPointerType'},
 'glSemaphoreParameterui64vEXT': {1: 'SemaphoreParameterName'},
 'glSeparableFilter2D': {0: 'SeparableTargetEXT',
                         1: 'InternalFormat',
                         4: 'PixelFormat',
                         5: 'PixelType'},
 'glSeparableFilter2DEXT': {0: 'SeparableTargetEXT',
                            1: 'InternalFormat',
                            4: 'PixelFormat',
                            5: 'PixelType'},
 'glSetInvariantEXT': {1: 'ScalarType'},
 'glSetLocalConstantEXT': {1: 'ScalarType'},
 'glShadeModel': {0: 'ShadingModel'},
 'glShaderOp1EXT': {0: 'VertexShaderOpEXT'},
 'glShaderOp2EXT': {0: 'VertexShaderOpEXT'},
 'glShaderOp3EXT': {0: 'VertexShaderOpEXT'},
 'glSignalSemaphoreEXT': {5: 'TextureLayout'},
 'glStencilFunc': {0: 'StencilFunction'},
 'glStencilFuncSeparate': {0: 'StencilFaceDirection', 1: 'StencilFunction'},
 'glStencilMaskSeparate': {0: 'StencilFaceDirection'},
 'glStencilOp': {0: 'StencilOp', 1: 'StencilOp', 2: 'StencilOp'},
 'glStencilOpSeparate': {0: 'StencilFaceDirection',
                         1: 'StencilOp',
                         2: 'StencilOp',
                         3: 'StencilOp'},
 'glSwizzleEXT': {2: 'VertexShaderCoordOutEXT',
                  3: 'VertexShaderCoordOutEXT',
                  4: 'VertexShaderCoordOutEXT',
                  5: 'VertexShaderCoordOutEXT'},
 'glTangentPointerEXT': {0: 'TangentPointerTypeEXT'},
 'glTexBuffer': {0: 'TextureTarget', 1: 'InternalFormat'},
 'glTexBufferARB': {0: 'TextureTarget', 1: 'InternalFormat'},
 'glTexBufferEXT': {0: 'TextureTarget', 1: 'InternalFormat'},
 'glTexBufferRange': {0: 'TextureTarget', 1: 'InternalFormat'},
 'glTexBufferRangeEXT': {0: 'TextureTarget', 1: 'InternalFormat'},
 'glTexCoordP1ui': {0: 'TexCoordPointerType'},
 'glTexCoordP1uiv': {0: 'TexCoordPointerType'},
 'glTexCoordP2ui': {0: 'TexCoordPointerType'},
 'glTexCoordP2uiv': {0: 'TexCoordPointerType'},
 'glTexCoordP3ui': {0: 'TexCoordPointerType'},
 'glTexCoordP3uiv': {0: 'TexCoordPointerType'},
 'glTexCoordP4ui': {0: 'TexCoordPointerType'},
 'glTexCoordP4uiv': {0: 'TexCoordPointerType'},
 'glTexCoordPointer': {1: 'TexCoordPointerType'},
 'glTexCoordPointerEXT': {1: 'TexCoordPointerType'},
 'glTexEnvf': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glTexEnvfv': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glTexEnvi': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glTexEnviv': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glTexEnvx': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glTexEnvxv': {0: 'TextureEnvTarget', 1: 'TextureEnvParameter'},
 'glTexGend': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glTexGendv': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glTexGenf': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glTexGenfv': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glTexGeni': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glTexGeniv': {0: 'TextureCoordName', 1: 'TextureGenParameter'},
 'glTexImage1D': {0: 'TextureTarget',
                  2: 'InternalFormat',
                  5: 'PixelFormat',
                  6: 'PixelType'},
 'glTexImage2D': {0: 'TextureTarget',
                  2: 'InternalFormat',
                  6: 'PixelFormat',
                  7: 'PixelType'},
 'glTexImage2DMultisample': {0: 'TextureTarget',
                             2: 'InternalFormat',
                             5: 'Boolean'},
 'glTexImage3D': {0: 'TextureTarget',
                  2: 'InternalFormat',
                  7: 'PixelFormat',
                  8: 'PixelType'},
 'glTexImage3DEXT': {0: 'TextureTarget',
                     2: 'InternalFormat',
                     7: 'PixelFormat',
                     8: 'PixelType'},
 'glTexImage3DMultisample': {0: 'TextureTarget',
                             2: 'InternalFormat',
                             6: 'Boolean'},
 'glTexParameterIiv': {0: 'TextureTarget', 1: 'TextureParameterName'},
 'glTexParameterIivEXT': {0: 'TextureTarget', 1: 'TextureParameterName'},
 'glTexParameterIuiv': {0: 'TextureTarget', 1: 'TextureParameterName'},
 'glTexParameterIuivEXT': {0: 'TextureTarget', 1: 'TextureParameterName'},
 'glTexParameterf': {0: 'TextureTarget', 1: 'TextureParameterName'},
 'glTexParameterfv': {0: 'TextureTarget', 1: 'TextureParameterName'},
 'glTexParameteri': {0: 'TextureTarget', 1: 'TextureParameterName'},
 'glTexParameteriv': {0: 'TextureTarget', 1: 'TextureParameterName'},
 'glTexParameterx': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glTexParameterxv': {0: 'TextureTarget', 1: 'GetTextureParameter'},
 'glTexStorage1D': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glTexStorage1DEXT': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glTexStorage2D': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glTexStorage2DEXT': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glTexStorage2DMultisample': {0: 'TextureTarget',
                               2: 'InternalFormat',
                               5: 'Boolean'},
 'glTexStorage3D': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glTexStorage3DEXT': {0: 'TextureTarget', 2: 'InternalFormat'},
 'glTexStorage3DMultisample': {0: 'TextureTarget',
                               2: 'InternalFormat',
                               6: 'Boolean'},
 'glTexStorageMem1DEXT': {0: 'TextureTarget'},
 'glTexStorageMem2DEXT': {0: 'TextureTarget'},
 'glTexStorageMem2DMultisampleEXT': {0: 'TextureTarget'},
 'glTexStorageMem3DEXT': {0: 'TextureTarget'},
 'glTexStorageMem3DMultisampleEXT': {0: 'TextureTarget'},
 'glTexSubImage1D': {0: 'TextureTarget', 4: 'PixelFormat', 5: 'PixelType'},
 'glTexSubImage1DEXT': {0: 'TextureTarget', 4: 'PixelFormat', 5: 'PixelType'},
 'glTexSubImage2D': {0: 'TextureTarget', 6: 'PixelFormat', 7: 'PixelType'},
 'glTexSubImage2DEXT': {0: 'TextureTarget', 6: 'PixelFormat', 7: 'PixelType'},
 'glTexSubImage3D': {0: 'TextureTarget', 8: 'PixelFormat', 9: 'PixelType'},
 'glTexSubImage3DEXT': {0: 'TextureTarget', 8: 'PixelFormat', 9: 'PixelType'},
 'glTextureBuffer': {1: 'InternalFormat'},
 'glTextureBufferEXT': {1: 'TextureTarget', 2: 'InternalFormat'},
 'glTextureBufferRange': {1: 'InternalFormat'},
 'glTextureBufferRangeEXT': {1: 'TextureTarget', 2: 'InternalFormat'},
 'glTextureImage1DEXT': {1: 'TextureTarget',
                         3: 'InternalFormat',
                         6: 'PixelFormat',
                         7: 'PixelType'},
 'glTextureImage2DEXT': {1: 'TextureTarget',
                         3: 'InternalFormat',
                         7: 'PixelFormat',
                         8: 'PixelType'},
 'glTextureImage3DEXT': {1: 'TextureTarget',
                         3: 'InternalFormat',
                         8: 'PixelFormat',
                         9: 'PixelType'},
 'glTextureLightEXT': {0: 'LightTexturePNameEXT'},
 'glTextureMaterialEXT': {0: 'MaterialFace', 1: 'MaterialParameter'},
 'glTextureNormalEXT': {0: 'TextureNormalModeEXT'},
 'glTextureParameterIiv': {1: 'TextureParameterName'},
 'glTextureParameterIivEXT': {1: 'TextureTarget', 2: 'TextureParameterName'},
 'glTextureParameterIuiv': {1: 'TextureParameterName'},
 'glTextureParameterIuivEXT': {1: 'TextureTarget', 2: 'TextureParameterName'},
 'glTextureParameterf': {1: 'TextureParameterName'},
 'glTextureParameterfEXT': {1: 'TextureTarget', 2: 'TextureParameterName'},
 'glTextureParameterfv': {1: 'TextureParameterName'},
 'glTextureParameterfvEXT': {1: 'TextureTarget', 2: 'TextureParameterName'},
 'glTextureParameteri': {1: 'TextureParameterName'},
 'glTextureParameteriEXT': {1: 'TextureTarget', 2: 'TextureParameterName'},
 'glTextureParameteriv': {1: 'TextureParameterName'},
 'glTextureParameterivEXT': {1: 'TextureTarget', 2: 'TextureParameterName'},
 'glTextureRenderbufferEXT': {1: 'TextureTarget'},
 'glTextureStorage1D': {2: 'InternalFormat'},
 'glTextureStorage1DEXT': {3: 'InternalFormat'},
 'glTextureStorage2D': {2: 'InternalFormat'},
 'glTextureStorage2DEXT': {3: 'InternalFormat'},
 'glTextureStorage2DMultisample': {2: 'InternalFormat'},
 'glTextureStorage2DMultisampleEXT': {1: 'TextureTarget',
                                      3: 'InternalFormat',
                                      6: 'Boolean'},
 'glTextureStorage3D': {2: 'InternalFormat'},
 'glTextureStorage3DEXT': {3: 'InternalFormat'},
 'glTextureStorage3DMultisample': {2: 'InternalFormat'},
 'glTextureStorage3DMultisampleEXT': {3: 'InternalFormat', 7: 'Boolean'},
 'glTextureSubImage1D': {4: 'PixelFormat', 5: 'PixelType'},
 'glTextureSubImage1DEXT': {1: 'TextureTarget',
                            5: 'PixelFormat',
                            6: 'PixelType'},
 'glTextureSubImage2D': {6: 'PixelFormat', 7: 'PixelType'},
 'glTextureSubImage2DEXT': {1: 'TextureTarget',
                            7: 'PixelFormat',
                            8: 'PixelType'},
 'glTextureSubImage3D': {8: 'PixelFormat', 9: 'PixelType'},
 'glTextureSubImage3DEXT': {1: 'TextureTarget',
                            9: 'PixelFormat',
                            10: 'PixelType'},
 'glTextureView': {1: 'TextureTarget', 3: 'InternalFormat'},
 'glTextureViewEXT': {1: 'TextureTarget', 3: 'InternalFormat'},
 'glTransformFeedbackVaryings': {3: 'TransformFeedbackBufferMode'},
 'glUniformMatrix2dv': {2: 'Boolean'},
 'glUniformMatrix2fv': {2: 'Boolean'},
 'glUniformMatrix2fvARB': {2: 'Boolean'},
 'glUniformMatrix2x3dv': {2: 'Boolean'},
 'glUniformMatrix2x3fv': {2: 'Boolean'},
 'glUniformMatrix2x4dv': {2: 'Boolean'},
 'glUniformMatrix2x4fv': {2: 'Boolean'},
 'glUniformMatrix3dv': {2: 'Boolean'},
 'glUniformMatrix3fv': {2: 'Boolean'},
 'glUniformMatrix3fvARB': {2: 'Boolean'},
 'glUniformMatrix3x2dv': {2: 'Boolean'},
 'glUniformMatrix3x2fv': {2: 'Boolean'},
 'glUniformMatrix3x4dv': {2: 'Boolean'},
 'glUniformMatrix3x4fv': {2: 'Boolean'},
 'glUniformMatrix4dv': {2: 'Boolean'},
 'glUniformMatrix4fv': {2: 'Boolean'},
 'glUniformMatrix4fvARB': {2: 'Boolean'},
 'glUniformMatrix4x2dv': {2: 'Boolean'},
 'glUniformMatrix4x2fv': {2: 'Boolean'},
 'glUniformMatrix4x3dv': {2: 'Boolean'},
 'glUniformMatrix4x3fv': {2: 'Boolean'},
 'glUniformSubroutinesuiv': {0: 'ShaderType'},
 'glUnmapBuffer': {0: 'BufferTargetARB'},
 'glUnmapBufferARB': {0: 'BufferTargetARB'},
 'glUseProgramStages': {1: 'UseProgramStageMask'},
 'glUseProgramStagesEXT': {1: 'UseProgramStageMask'},
 'glVariantPointerEXT': {1: 'ScalarType'},
 'glVertexArrayAttribFormat': {3: 'VertexAttribType'},
 'glVertexArrayAttribIFormat': {3: 'VertexAttribIType'},
 'glVertexArrayAttribLFormat': {3: 'VertexAttribLType'},
 'glVertexArrayColorOffsetEXT': {3: 'ColorPointerType'},
 'glVertexArrayFogCoordOffsetEXT': {2: 'FogCoordinatePointerType'},
 'glVertexArrayIndexOffsetEXT': {2: 'IndexPointerType'},
 'glVertexArrayMultiTexCoordOffsetEXT': {4: 'TexCoordPointerType'},
 'glVertexArrayNormalOffsetEXT': {2: 'NormalPointerType'},
 'glVertexArraySecondaryColorOffsetEXT': {3: 'ColorPointerType'},
 'glVertexArrayTexCoordOffsetEXT': {3: 'TexCoordPointerType'},
 'glVertexArrayVertexAttribFormatEXT': {3: 'VertexAttribType', 4: 'Boolean'},
 'glVertexArrayVertexAttribIFormatEXT': {3: 'VertexAttribIType'},
 'glVertexArrayVertexAttribIOffsetEXT': {4: 'VertexAttribType'},
 'glVertexArrayVertexAttribLFormatEXT': {3: 'VertexAttribLType'},
 'glVertexArrayVertexAttribLOffsetEXT': {4: 'VertexAttribLType'},
 'glVertexArrayVertexAttribOffsetEXT': {4: 'VertexAttribPointerType'},
 'glVertexArrayVertexOffsetEXT': {3: 'VertexPointerType'},
 'glVertexAttribFormat': {2: 'VertexAttribType', 3: 'Boolean'},
 'glVertexAttribIFormat': {2: 'VertexAttribIType'},
 'glVertexAttribIPointer': {2: 'VertexAttribPointerType'},
 'glVertexAttribIPointerEXT': {2: 'VertexAttribPointerType'},
 'glVertexAttribLFormat': {2: 'VertexAttribLType'},
 'glVertexAttribLPointer': {2: 'VertexAttribPointerType'},
 'glVertexAttribLPointerEXT': {2: 'VertexAttribPointerType'},
 'glVertexAttribP1ui': {1: 'VertexAttribPointerType', 2: 'Boolean'},
 'glVertexAttribP1uiv': {1: 'VertexAttribPointerType', 2: 'Boolean'},
 'glVertexAttribP2ui': {1: 'VertexAttribPointerType', 2: 'Boolean'},
 'glVertexAttribP2uiv': {1: 'VertexAttribPointerType', 2: 'Boolean'},
 'glVertexAttribP3ui': {1: 'VertexAttribPointerType', 2: 'Boolean'},
 'glVertexAttribP3uiv': {1: 'VertexAttribPointerType', 2: 'Boolean'},
 'glVertexAttribP4ui': {1: 'VertexAttribPointerType', 2: 'Boolean'},
 'glVertexAttribP4uiv': {1: 'VertexAttribPointerType', 2: 'Boolean'},
 'glVertexAttribPointer': {2: 'VertexAttribPointerType', 3: 'Boolean'},
 'glVertexAttribPointerARB': {2: 'VertexAttribPointerType', 3: 'Boolean'},
 'glVertexP2ui': {0: 'VertexPointerType'},
 'glVertexP2uiv': {0: 'VertexPointerType'},
 'glVertexP3ui': {0: 'VertexPointerType'},
 'glVertexP3uiv': {0: 'VertexPointerType'},
 'glVertexP4ui': {0: 'VertexPointerType'},
 'glVertexP4uiv': {0: 'VertexPointerType'},
 'glVertexPointer': {1: 'VertexPointerType'},
 'glVertexPointerEXT': {1: 'VertexPointerType'},
 'glVertexWeightPointerEXT': {1: 'VertexWeightPointerTypeEXT'},
 'glWaitSemaphoreEXT': {5: 'TextureLayout'},
 'glWeightPointerARB': {1: 'WeightPointerTypeARB'},
 'glWriteMaskEXT': {2: 'VertexShaderWriteMaskEXT',
                    3: 'VertexShaderWriteMaskEXT',
                    4: 'VertexShaderWriteMaskEXT',
                    5: 'VertexShaderWriteMaskEXT'}}
GL_CURRENT_BIT = 1
GL_POINT_BIT = 2
GL_LINE_BIT = 4
GL_POLYGON_BIT = 8
GL_POLYGON_STIPPLE_BIT = 16
GL_PIXEL_MODE_BIT = 32
GL_LIGHTING_BIT = 64
GL_FOG_BIT = 128
GL_DEPTH_BUFFER_BIT = 256
GL_ACCUM_BUFFER_BIT = 512
GL_STENCIL_BUFFER_BIT = 1024
GL_VIEWPORT_BIT = 2048
GL_TRANSFORM_BIT = 4096
GL_ENABLE_BIT = 8192
GL_COLOR_BUFFER_BIT = 16384
GL_HINT_BIT = 32768
GL_EVAL_BIT = 65536
GL_LIST_BIT = 131072
GL_TEXTURE_BIT = 262144
GL_SCISSOR_BIT = 524288
GL_MULTISAMPLE_BIT = 536870912
GL_MULTISAMPLE_BIT_ARB = 536870912
GL_MULTISAMPLE_BIT_EXT = 536870912
GL_MULTISAMPLE_BIT_3DFX = 536870912
GL_ALL_ATTRIB_BITS = 4294967295
GL_DYNAMIC_STORAGE_BIT = 256
GL_DYNAMIC_STORAGE_BIT_EXT = 256
GL_CLIENT_STORAGE_BIT = 512
GL_CLIENT_STORAGE_BIT_EXT = 512
GL_SPARSE_STORAGE_BIT_ARB = 1024
GL_LGPU_SEPARATE_STORAGE_BIT_NVX = 2048
GL_EXTERNAL_STORAGE_BIT_NVX = 8192
GL_CLIENT_PIXEL_STORE_BIT = 1
GL_CLIENT_VERTEX_ARRAY_BIT = 2
GL_CLIENT_ALL_ATTRIB_BITS = 4294967295
GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = 1
GL_CONTEXT_FLAG_DEBUG_BIT = 2
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT = 4
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB = 4
GL_CONTEXT_FLAG_NO_ERROR_BIT = 8
GL_CONTEXT_FLAG_PROTECTED_CONTENT_BIT_EXT = 16
GL_CONTEXT_CORE_PROFILE_BIT = 1
GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 2
GL_MAP_READ_BIT = 1
GL_MAP_READ_BIT_EXT = 1
GL_MAP_WRITE_BIT = 2
GL_MAP_WRITE_BIT_EXT = 2
GL_MAP_INVALIDATE_RANGE_BIT = 4
GL_MAP_INVALIDATE_RANGE_BIT_EXT = 4
GL_MAP_INVALIDATE_BUFFER_BIT = 8
GL_MAP_INVALIDATE_BUFFER_BIT_EXT = 8
GL_MAP_FLUSH_EXPLICIT_BIT = 16
GL_MAP_FLUSH_EXPLICIT_BIT_EXT = 16
GL_MAP_UNSYNCHRONIZED_BIT = 32
GL_MAP_UNSYNCHRONIZED_BIT_EXT = 32
GL_MAP_PERSISTENT_BIT = 64
GL_MAP_PERSISTENT_BIT_EXT = 64
GL_MAP_COHERENT_BIT = 128
GL_MAP_COHERENT_BIT_EXT = 128
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT = 1
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT_EXT = 1
GL_ELEMENT_ARRAY_BARRIER_BIT = 2
GL_ELEMENT_ARRAY_BARRIER_BIT_EXT = 2
GL_UNIFORM_BARRIER_BIT = 4
GL_UNIFORM_BARRIER_BIT_EXT = 4
GL_TEXTURE_FETCH_BARRIER_BIT = 8
GL_TEXTURE_FETCH_BARRIER_BIT_EXT = 8
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT = 32
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT_EXT = 32
GL_COMMAND_BARRIER_BIT = 64
GL_COMMAND_BARRIER_BIT_EXT = 64
GL_PIXEL_BUFFER_BARRIER_BIT = 128
GL_PIXEL_BUFFER_BARRIER_BIT_EXT = 128
GL_TEXTURE_UPDATE_BARRIER_BIT = 256
GL_TEXTURE_UPDATE_BARRIER_BIT_EXT = 256
GL_BUFFER_UPDATE_BARRIER_BIT = 512
GL_BUFFER_UPDATE_BARRIER_BIT_EXT = 512
GL_FRAMEBUFFER_BARRIER_BIT = 1024
GL_FRAMEBUFFER_BARRIER_BIT_EXT = 1024
GL_TRANSFORM_FEEDBACK_BARRIER_BIT = 2048
GL_TRANSFORM_FEEDBACK_BARRIER_BIT_EXT = 2048
GL_ATOMIC_COUNTER_BARRIER_BIT = 4096
GL_ATOMIC_COUNTER_BARRIER_BIT_EXT = 4096
GL_SHADER_STORAGE_BARRIER_BIT = 8192
GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT = 16384
GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT_EXT = 16384
GL_QUERY_BUFFER_BARRIER_BIT = 32768
GL_ALL_BARRIER_BITS = 4294967295
GL_ALL_BARRIER_BITS_EXT = 4294967295
GL_SYNC_FLUSH_COMMANDS_BIT = 1
GL_VERTEX_SHADER_BIT = 1
GL_VERTEX_SHADER_BIT_EXT = 1
GL_FRAGMENT_SHADER_BIT = 2
GL_FRAGMENT_SHADER_BIT_EXT = 2
GL_GEOMETRY_SHADER_BIT = 4
GL_GEOMETRY_SHADER_BIT_EXT = 4
GL_TESS_CONTROL_SHADER_BIT = 8
GL_TESS_CONTROL_SHADER_BIT_EXT = 8
GL_TESS_EVALUATION_SHADER_BIT = 16
GL_TESS_EVALUATION_SHADER_BIT_EXT = 16
GL_COMPUTE_SHADER_BIT = 32
GL_ALL_SHADER_BITS = 4294967295
GL_ALL_SHADER_BITS_EXT = 4294967295
GL_FALSE = 0
GL_NO_ERROR = 0
GL_ZERO = 0
GL_NONE = 0
GL_TRUE = 1
GL_ONE = 1
GL_INVALID_INDEX = 4294967295
GL_TIMEOUT_IGNORED = 18446744073709551615
GL_VERSION_ES_CL_1_0 = 1
GL_VERSION_ES_CM_1_1 = 1
GL_VERSION_ES_CL_1_1 = 1
GL_UUID_SIZE_EXT = 16
GL_LUID_SIZE_EXT = 8
GL_POINTS = 0
GL_LINES = 1
GL_LINE_LOOP = 2
GL_LINE_STRIP = 3
GL_TRIANGLES = 4
GL_TRIANGLE_STRIP = 5
GL_TRIANGLE_FAN = 6
GL_QUADS = 7
GL_QUADS_EXT = 7
GL_QUAD_STRIP = 8
GL_POLYGON = 9
GL_LINES_ADJACENCY = 10
GL_LINES_ADJACENCY_ARB = 10
GL_LINES_ADJACENCY_EXT = 10
GL_LINE_STRIP_ADJACENCY = 11
GL_LINE_STRIP_ADJACENCY_ARB = 11
GL_LINE_STRIP_ADJACENCY_EXT = 11
GL_TRIANGLES_ADJACENCY = 12
GL_TRIANGLES_ADJACENCY_ARB = 12
GL_TRIANGLES_ADJACENCY_EXT = 12
GL_TRIANGLE_STRIP_ADJACENCY = 13
GL_TRIANGLE_STRIP_ADJACENCY_ARB = 13
GL_TRIANGLE_STRIP_ADJACENCY_EXT = 13
GL_PATCHES = 14
GL_PATCHES_EXT = 14
GL_ACCUM = 256
GL_LOAD = 257
GL_RETURN = 258
GL_MULT = 259
GL_ADD = 260
GL_NEVER = 512
GL_LESS = 513
GL_EQUAL = 514
GL_LEQUAL = 515
GL_GREATER = 516
GL_NOTEQUAL = 517
GL_GEQUAL = 518
GL_ALWAYS = 519
GL_SRC_COLOR = 768
GL_ONE_MINUS_SRC_COLOR = 769
GL_SRC_ALPHA = 770
GL_ONE_MINUS_SRC_ALPHA = 771
GL_DST_ALPHA = 772
GL_ONE_MINUS_DST_ALPHA = 773
GL_DST_COLOR = 774
GL_ONE_MINUS_DST_COLOR = 775
GL_SRC_ALPHA_SATURATE = 776
GL_SRC_ALPHA_SATURATE_EXT = 776
GL_FRONT_LEFT = 1024
GL_FRONT_RIGHT = 1025
GL_BACK_LEFT = 1026
GL_BACK_RIGHT = 1027
GL_FRONT = 1028
GL_BACK = 1029
GL_LEFT = 1030
GL_RIGHT = 1031
GL_FRONT_AND_BACK = 1032
GL_AUX0 = 1033
GL_AUX1 = 1034
GL_AUX2 = 1035
GL_AUX3 = 1036
GL_INVALID_ENUM = 1280
GL_INVALID_VALUE = 1281
GL_INVALID_OPERATION = 1282
GL_STACK_OVERFLOW = 1283
GL_STACK_UNDERFLOW = 1284
GL_OUT_OF_MEMORY = 1285
GL_INVALID_FRAMEBUFFER_OPERATION = 1286
GL_INVALID_FRAMEBUFFER_OPERATION_EXT = 1286
GL_CONTEXT_LOST = 1287
GL_2D = 1536
GL_3D = 1537
GL_3D_COLOR = 1538
GL_3D_COLOR_TEXTURE = 1539
GL_4D_COLOR_TEXTURE = 1540
GL_PASS_THROUGH_TOKEN = 1792
GL_POINT_TOKEN = 1793
GL_LINE_TOKEN = 1794
GL_POLYGON_TOKEN = 1795
GL_BITMAP_TOKEN = 1796
GL_DRAW_PIXEL_TOKEN = 1797
GL_COPY_PIXEL_TOKEN = 1798
GL_LINE_RESET_TOKEN = 1799
GL_EXP = 2048
GL_EXP2 = 2049
GL_CW = 2304
GL_CCW = 2305
GL_COEFF = 2560
GL_ORDER = 2561
GL_DOMAIN = 2562
GL_CURRENT_COLOR = 2816
GL_CURRENT_INDEX = 2817
GL_CURRENT_NORMAL = 2818
GL_CURRENT_TEXTURE_COORDS = 2819
GL_CURRENT_RASTER_COLOR = 2820
GL_CURRENT_RASTER_INDEX = 2821
GL_CURRENT_RASTER_TEXTURE_COORDS = 2822
GL_CURRENT_RASTER_POSITION = 2823
GL_CURRENT_RASTER_POSITION_VALID = 2824
GL_CURRENT_RASTER_DISTANCE = 2825
GL_POINT_SMOOTH = 2832
GL_POINT_SIZE = 2833
GL_POINT_SIZE_RANGE = 2834
GL_SMOOTH_POINT_SIZE_RANGE = 2834
GL_POINT_SIZE_GRANULARITY = 2835
GL_SMOOTH_POINT_SIZE_GRANULARITY = 2835
GL_LINE_SMOOTH = 2848
GL_LINE_WIDTH = 2849
GL_LINE_WIDTH_RANGE = 2850
GL_SMOOTH_LINE_WIDTH_RANGE = 2850
GL_LINE_WIDTH_GRANULARITY = 2851
GL_SMOOTH_LINE_WIDTH_GRANULARITY = 2851
GL_LINE_STIPPLE = 2852
GL_LINE_STIPPLE_PATTERN = 2853
GL_LINE_STIPPLE_REPEAT = 2854
GL_LIST_MODE = 2864
GL_MAX_LIST_NESTING = 2865
GL_LIST_BASE = 2866
GL_LIST_INDEX = 2867
GL_POLYGON_MODE = 2880
GL_POLYGON_SMOOTH = 2881
GL_POLYGON_STIPPLE = 2882
GL_EDGE_FLAG = 2883
GL_CULL_FACE = 2884
GL_CULL_FACE_MODE = 2885
GL_FRONT_FACE = 2886
GL_LIGHTING = 2896
GL_LIGHT_MODEL_LOCAL_VIEWER = 2897
GL_LIGHT_MODEL_TWO_SIDE = 2898
GL_LIGHT_MODEL_AMBIENT = 2899
GL_SHADE_MODEL = 2900
GL_COLOR_MATERIAL_FACE = 2901
GL_COLOR_MATERIAL_PARAMETER = 2902
GL_COLOR_MATERIAL = 2903
GL_FOG = 2912
GL_FOG_INDEX = 2913
GL_FOG_DENSITY = 2914
GL_FOG_START = 2915
GL_FOG_END = 2916
GL_FOG_MODE = 2917
GL_FOG_COLOR = 2918
GL_DEPTH_RANGE = 2928
GL_DEPTH_TEST = 2929
GL_DEPTH_WRITEMASK = 2930
GL_DEPTH_CLEAR_VALUE = 2931
GL_DEPTH_FUNC = 2932
GL_ACCUM_CLEAR_VALUE = 2944
GL_STENCIL_TEST = 2960
GL_STENCIL_CLEAR_VALUE = 2961
GL_STENCIL_FUNC = 2962
GL_STENCIL_VALUE_MASK = 2963
GL_STENCIL_FAIL = 2964
GL_STENCIL_PASS_DEPTH_FAIL = 2965
GL_STENCIL_PASS_DEPTH_PASS = 2966
GL_STENCIL_REF = 2967
GL_STENCIL_WRITEMASK = 2968
GL_MATRIX_MODE = 2976
GL_NORMALIZE = 2977
GL_VIEWPORT = 2978
GL_MODELVIEW_STACK_DEPTH = 2979
GL_MODELVIEW0_STACK_DEPTH_EXT = 2979
GL_PROJECTION_STACK_DEPTH = 2980
GL_TEXTURE_STACK_DEPTH = 2981
GL_MODELVIEW_MATRIX = 2982
GL_MODELVIEW0_MATRIX_EXT = 2982
GL_PROJECTION_MATRIX = 2983
GL_TEXTURE_MATRIX = 2984
GL_ATTRIB_STACK_DEPTH = 2992
GL_CLIENT_ATTRIB_STACK_DEPTH = 2993
GL_ALPHA_TEST = 3008
GL_ALPHA_TEST_FUNC = 3009
GL_ALPHA_TEST_REF = 3010
GL_DITHER = 3024
GL_BLEND_DST = 3040
GL_BLEND_SRC = 3041
GL_BLEND = 3042
GL_LOGIC_OP_MODE = 3056
GL_INDEX_LOGIC_OP = 3057
GL_LOGIC_OP = 3057
GL_COLOR_LOGIC_OP = 3058
GL_AUX_BUFFERS = 3072
GL_DRAW_BUFFER = 3073
GL_DRAW_BUFFER_EXT = 3073
GL_READ_BUFFER = 3074
GL_READ_BUFFER_EXT = 3074
GL_SCISSOR_BOX = 3088
GL_SCISSOR_TEST = 3089
GL_INDEX_CLEAR_VALUE = 3104
GL_INDEX_WRITEMASK = 3105
GL_COLOR_CLEAR_VALUE = 3106
GL_COLOR_WRITEMASK = 3107
GL_INDEX_MODE = 3120
GL_RGBA_MODE = 3121
GL_DOUBLEBUFFER = 3122
GL_STEREO = 3123
GL_RENDER_MODE = 3136
GL_PERSPECTIVE_CORRECTION_HINT = 3152
GL_POINT_SMOOTH_HINT = 3153
GL_LINE_SMOOTH_HINT = 3154
GL_POLYGON_SMOOTH_HINT = 3155
GL_FOG_HINT = 3156
GL_TEXTURE_GEN_S = 3168
GL_TEXTURE_GEN_T = 3169
GL_TEXTURE_GEN_R = 3170
GL_TEXTURE_GEN_Q = 3171
GL_PIXEL_MAP_I_TO_I = 3184
GL_PIXEL_MAP_S_TO_S = 3185
GL_PIXEL_MAP_I_TO_R = 3186
GL_PIXEL_MAP_I_TO_G = 3187
GL_PIXEL_MAP_I_TO_B = 3188
GL_PIXEL_MAP_I_TO_A = 3189
GL_PIXEL_MAP_R_TO_R = 3190
GL_PIXEL_MAP_G_TO_G = 3191
GL_PIXEL_MAP_B_TO_B = 3192
GL_PIXEL_MAP_A_TO_A = 3193
GL_PIXEL_MAP_I_TO_I_SIZE = 3248
GL_PIXEL_MAP_S_TO_S_SIZE = 3249
GL_PIXEL_MAP_I_TO_R_SIZE = 3250
GL_PIXEL_MAP_I_TO_G_SIZE = 3251
GL_PIXEL_MAP_I_TO_B_SIZE = 3252
GL_PIXEL_MAP_I_TO_A_SIZE = 3253
GL_PIXEL_MAP_R_TO_R_SIZE = 3254
GL_PIXEL_MAP_G_TO_G_SIZE = 3255
GL_PIXEL_MAP_B_TO_B_SIZE = 3256
GL_PIXEL_MAP_A_TO_A_SIZE = 3257
GL_UNPACK_SWAP_BYTES = 3312
GL_UNPACK_LSB_FIRST = 3313
GL_UNPACK_ROW_LENGTH = 3314
GL_UNPACK_ROW_LENGTH_EXT = 3314
GL_UNPACK_SKIP_ROWS = 3315
GL_UNPACK_SKIP_ROWS_EXT = 3315
GL_UNPACK_SKIP_PIXELS = 3316
GL_UNPACK_SKIP_PIXELS_EXT = 3316
GL_UNPACK_ALIGNMENT = 3317
GL_PACK_SWAP_BYTES = 3328
GL_PACK_LSB_FIRST = 3329
GL_PACK_ROW_LENGTH = 3330
GL_PACK_SKIP_ROWS = 3331
GL_PACK_SKIP_PIXELS = 3332
GL_PACK_ALIGNMENT = 3333
GL_MAP_COLOR = 3344
GL_MAP_STENCIL = 3345
GL_INDEX_SHIFT = 3346
GL_INDEX_OFFSET = 3347
GL_RED_SCALE = 3348
GL_RED_BIAS = 3349
GL_ZOOM_X = 3350
GL_ZOOM_Y = 3351
GL_GREEN_SCALE = 3352
GL_GREEN_BIAS = 3353
GL_BLUE_SCALE = 3354
GL_BLUE_BIAS = 3355
GL_ALPHA_SCALE = 3356
GL_ALPHA_BIAS = 3357
GL_DEPTH_SCALE = 3358
GL_DEPTH_BIAS = 3359
GL_MAX_EVAL_ORDER = 3376
GL_MAX_LIGHTS = 3377
GL_MAX_CLIP_PLANES = 3378
GL_MAX_CLIP_PLANES_IMG = 3378
GL_MAX_CLIP_DISTANCES = 3378
GL_MAX_CLIP_DISTANCES_EXT = 3378
GL_MAX_TEXTURE_SIZE = 3379
GL_MAX_PIXEL_MAP_TABLE = 3380
GL_MAX_ATTRIB_STACK_DEPTH = 3381
GL_MAX_MODELVIEW_STACK_DEPTH = 3382
GL_MAX_NAME_STACK_DEPTH = 3383
GL_MAX_PROJECTION_STACK_DEPTH = 3384
GL_MAX_TEXTURE_STACK_DEPTH = 3385
GL_MAX_VIEWPORT_DIMS = 3386
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 3387
GL_SUBPIXEL_BITS = 3408
GL_INDEX_BITS = 3409
GL_RED_BITS = 3410
GL_GREEN_BITS = 3411
GL_BLUE_BITS = 3412
GL_ALPHA_BITS = 3413
GL_DEPTH_BITS = 3414
GL_STENCIL_BITS = 3415
GL_ACCUM_RED_BITS = 3416
GL_ACCUM_GREEN_BITS = 3417
GL_ACCUM_BLUE_BITS = 3418
GL_ACCUM_ALPHA_BITS = 3419
GL_NAME_STACK_DEPTH = 3440
GL_AUTO_NORMAL = 3456
GL_MAP1_COLOR_4 = 3472
GL_MAP1_INDEX = 3473
GL_MAP1_NORMAL = 3474
GL_MAP1_TEXTURE_COORD_1 = 3475
GL_MAP1_TEXTURE_COORD_2 = 3476
GL_MAP1_TEXTURE_COORD_3 = 3477
GL_MAP1_TEXTURE_COORD_4 = 3478
GL_MAP1_VERTEX_3 = 3479
GL_MAP1_VERTEX_4 = 3480
GL_MAP2_COLOR_4 = 3504
GL_MAP2_INDEX = 3505
GL_MAP2_NORMAL = 3506
GL_MAP2_TEXTURE_COORD_1 = 3507
GL_MAP2_TEXTURE_COORD_2 = 3508
GL_MAP2_TEXTURE_COORD_3 = 3509
GL_MAP2_TEXTURE_COORD_4 = 3510
GL_MAP2_VERTEX_3 = 3511
GL_MAP2_VERTEX_4 = 3512
GL_MAP1_GRID_DOMAIN = 3536
GL_MAP1_GRID_SEGMENTS = 3537
GL_MAP2_GRID_DOMAIN = 3538
GL_MAP2_GRID_SEGMENTS = 3539
GL_TEXTURE_1D = 3552
GL_TEXTURE_2D = 3553
GL_FEEDBACK_BUFFER_POINTER = 3568
GL_FEEDBACK_BUFFER_SIZE = 3569
GL_FEEDBACK_BUFFER_TYPE = 3570
GL_SELECTION_BUFFER_POINTER = 3571
GL_SELECTION_BUFFER_SIZE = 3572
GL_TEXTURE_WIDTH = 4096
GL_TEXTURE_HEIGHT = 4097
GL_TEXTURE_INTERNAL_FORMAT = 4099
GL_TEXTURE_COMPONENTS = 4099
GL_TEXTURE_BORDER_COLOR = 4100
GL_TEXTURE_BORDER_COLOR_EXT = 4100
GL_TEXTURE_BORDER = 4101
GL_TEXTURE_TARGET = 4102
GL_DONT_CARE = 4352
GL_FASTEST = 4353
GL_NICEST = 4354
GL_AMBIENT = 4608
GL_DIFFUSE = 4609
GL_SPECULAR = 4610
GL_POSITION = 4611
GL_SPOT_DIRECTION = 4612
GL_SPOT_EXPONENT = 4613
GL_SPOT_CUTOFF = 4614
GL_CONSTANT_ATTENUATION = 4615
GL_LINEAR_ATTENUATION = 4616
GL_QUADRATIC_ATTENUATION = 4617
GL_COMPILE = 4864
GL_COMPILE_AND_EXECUTE = 4865
GL_BYTE = 5120
GL_UNSIGNED_BYTE = 5121
GL_SHORT = 5122
GL_UNSIGNED_SHORT = 5123
GL_INT = 5124
GL_UNSIGNED_INT = 5125
GL_FLOAT = 5126
GL_2_BYTES = 5127
GL_3_BYTES = 5128
GL_4_BYTES = 5129
GL_DOUBLE = 5130
GL_DOUBLE_EXT = 5130
GL_HALF_FLOAT = 5131
GL_HALF_FLOAT_ARB = 5131
GL_FIXED = 5132
GL_INT64_ARB = 5134
GL_UNSIGNED_INT64_ARB = 5135
GL_CLEAR = 5376
GL_AND = 5377
GL_AND_REVERSE = 5378
GL_COPY = 5379
GL_AND_INVERTED = 5380
GL_NOOP = 5381
GL_XOR = 5382
GL_OR = 5383
GL_NOR = 5384
GL_EQUIV = 5385
GL_INVERT = 5386
GL_OR_REVERSE = 5387
GL_COPY_INVERTED = 5388
GL_OR_INVERTED = 5389
GL_NAND = 5390
GL_SET = 5391
GL_EMISSION = 5632
GL_SHININESS = 5633
GL_AMBIENT_AND_DIFFUSE = 5634
GL_COLOR_INDEXES = 5635
GL_MODELVIEW = 5888
GL_MODELVIEW0_ARB = 5888
GL_MODELVIEW0_EXT = 5888
GL_PROJECTION = 5889
GL_TEXTURE = 5890
GL_COLOR = 6144
GL_COLOR_EXT = 6144
GL_DEPTH = 6145
GL_DEPTH_EXT = 6145
GL_STENCIL = 6146
GL_STENCIL_EXT = 6146
GL_COLOR_INDEX = 6400
GL_STENCIL_INDEX = 6401
GL_DEPTH_COMPONENT = 6402
GL_RED = 6403
GL_RED_EXT = 6403
GL_GREEN = 6404
GL_BLUE = 6405
GL_ALPHA = 6406
GL_RGB = 6407
GL_RGBA = 6408
GL_LUMINANCE = 6409
GL_LUMINANCE_ALPHA = 6410
GL_BITMAP = 6656
GL_POINT = 6912
GL_LINE = 6913
GL_FILL = 6914
GL_RENDER = 7168
GL_FEEDBACK = 7169
GL_SELECT = 7170
GL_FLAT = 7424
GL_SMOOTH = 7425
GL_KEEP = 7680
GL_REPLACE = 7681
GL_INCR = 7682
GL_DECR = 7683
GL_VENDOR = 7936
GL_RENDERER = 7937
GL_VERSION = 7938
GL_EXTENSIONS = 7939
GL_S = 8192
GL_T = 8193
GL_R = 8194
GL_Q = 8195
GL_MODULATE = 8448
GL_DECAL = 8449
GL_TEXTURE_ENV_MODE = 8704
GL_TEXTURE_ENV_COLOR = 8705
GL_EYE_LINEAR = 9216
GL_OBJECT_LINEAR = 9217
GL_SPHERE_MAP = 9218
GL_TEXTURE_GEN_MODE = 9472
GL_OBJECT_PLANE = 9473
GL_EYE_PLANE = 9474
GL_NEAREST = 9728
GL_LINEAR = 9729
GL_NEAREST_MIPMAP_NEAREST = 9984
GL_LINEAR_MIPMAP_NEAREST = 9985
GL_NEAREST_MIPMAP_LINEAR = 9986
GL_LINEAR_MIPMAP_LINEAR = 9987
GL_TEXTURE_MAG_FILTER = 10240
GL_TEXTURE_MIN_FILTER = 10241
GL_TEXTURE_WRAP_S = 10242
GL_TEXTURE_WRAP_T = 10243
GL_CLAMP = 10496
GL_REPEAT = 10497
GL_POLYGON_OFFSET_UNITS = 10752
GL_POLYGON_OFFSET_POINT = 10753
GL_POLYGON_OFFSET_LINE = 10754
GL_R3_G3_B2 = 10768
GL_V2F = 10784
GL_V3F = 10785
GL_C4UB_V2F = 10786
GL_C4UB_V3F = 10787
GL_C3F_V3F = 10788
GL_N3F_V3F = 10789
GL_C4F_N3F_V3F = 10790
GL_T2F_V3F = 10791
GL_T4F_V4F = 10792
GL_T2F_C4UB_V3F = 10793
GL_T2F_C3F_V3F = 10794
GL_T2F_N3F_V3F = 10795
GL_T2F_C4F_N3F_V3F = 10796
GL_T4F_C4F_N3F_V4F = 10797
GL_CLIP_PLANE0 = 12288
GL_CLIP_PLANE0_IMG = 12288
GL_CLIP_DISTANCE0 = 12288
GL_CLIP_DISTANCE0_EXT = 12288
GL_CLIP_PLANE1 = 12289
GL_CLIP_PLANE1_IMG = 12289
GL_CLIP_DISTANCE1 = 12289
GL_CLIP_DISTANCE1_EXT = 12289
GL_CLIP_PLANE2 = 12290
GL_CLIP_PLANE2_IMG = 12290
GL_CLIP_DISTANCE2 = 12290
GL_CLIP_DISTANCE2_EXT = 12290
GL_CLIP_PLANE3 = 12291
GL_CLIP_PLANE3_IMG = 12291
GL_CLIP_DISTANCE3 = 12291
GL_CLIP_DISTANCE3_EXT = 12291
GL_CLIP_PLANE4 = 12292
GL_CLIP_PLANE4_IMG = 12292
GL_CLIP_DISTANCE4 = 12292
GL_CLIP_DISTANCE4_EXT = 12292
GL_CLIP_PLANE5 = 12293
GL_CLIP_PLANE5_IMG = 12293
GL_CLIP_DISTANCE5 = 12293
GL_CLIP_DISTANCE5_EXT = 12293
GL_CLIP_DISTANCE6 = 12294
GL_CLIP_DISTANCE6_EXT = 12294
GL_CLIP_DISTANCE7 = 12295
GL_CLIP_DISTANCE7_EXT = 12295
GL_LIGHT0 = 16384
GL_LIGHT1 = 16385
GL_LIGHT2 = 16386
GL_LIGHT3 = 16387
GL_LIGHT4 = 16388
GL_LIGHT5 = 16389
GL_LIGHT6 = 16390
GL_LIGHT7 = 16391
GL_ABGR_EXT = 32768
GL_CONSTANT_COLOR = 32769
GL_CONSTANT_COLOR_EXT = 32769
GL_ONE_MINUS_CONSTANT_COLOR = 32770
GL_ONE_MINUS_CONSTANT_COLOR_EXT = 32770
GL_CONSTANT_ALPHA = 32771
GL_CONSTANT_ALPHA_EXT = 32771
GL_ONE_MINUS_CONSTANT_ALPHA = 32772
GL_ONE_MINUS_CONSTANT_ALPHA_EXT = 32772
GL_BLEND_COLOR = 32773
GL_BLEND_COLOR_EXT = 32773
GL_FUNC_ADD = 32774
GL_FUNC_ADD_EXT = 32774
GL_MIN = 32775
GL_MIN_EXT = 32775
GL_MAX = 32776
GL_MAX_EXT = 32776
GL_BLEND_EQUATION = 32777
GL_BLEND_EQUATION_EXT = 32777
GL_BLEND_EQUATION_RGB = 32777
GL_BLEND_EQUATION_RGB_EXT = 32777
GL_FUNC_SUBTRACT = 32778
GL_FUNC_SUBTRACT_EXT = 32778
GL_FUNC_REVERSE_SUBTRACT = 32779
GL_FUNC_REVERSE_SUBTRACT_EXT = 32779
GL_CMYK_EXT = 32780
GL_CMYKA_EXT = 32781
GL_PACK_CMYK_HINT_EXT = 32782
GL_UNPACK_CMYK_HINT_EXT = 32783
GL_CONVOLUTION_1D = 32784
GL_CONVOLUTION_1D_EXT = 32784
GL_CONVOLUTION_2D = 32785
GL_CONVOLUTION_2D_EXT = 32785
GL_SEPARABLE_2D = 32786
GL_SEPARABLE_2D_EXT = 32786
GL_CONVOLUTION_BORDER_MODE = 32787
GL_CONVOLUTION_BORDER_MODE_EXT = 32787
GL_CONVOLUTION_FILTER_SCALE = 32788
GL_CONVOLUTION_FILTER_SCALE_EXT = 32788
GL_CONVOLUTION_FILTER_BIAS = 32789
GL_CONVOLUTION_FILTER_BIAS_EXT = 32789
GL_REDUCE = 32790
GL_REDUCE_EXT = 32790
GL_CONVOLUTION_FORMAT = 32791
GL_CONVOLUTION_FORMAT_EXT = 32791
GL_CONVOLUTION_WIDTH = 32792
GL_CONVOLUTION_WIDTH_EXT = 32792
GL_CONVOLUTION_HEIGHT = 32793
GL_CONVOLUTION_HEIGHT_EXT = 32793
GL_MAX_CONVOLUTION_WIDTH = 32794
GL_MAX_CONVOLUTION_WIDTH_EXT = 32794
GL_MAX_CONVOLUTION_HEIGHT = 32795
GL_MAX_CONVOLUTION_HEIGHT_EXT = 32795
GL_POST_CONVOLUTION_RED_SCALE = 32796
GL_POST_CONVOLUTION_RED_SCALE_EXT = 32796
GL_POST_CONVOLUTION_GREEN_SCALE = 32797
GL_POST_CONVOLUTION_GREEN_SCALE_EXT = 32797
GL_POST_CONVOLUTION_BLUE_SCALE = 32798
GL_POST_CONVOLUTION_BLUE_SCALE_EXT = 32798
GL_POST_CONVOLUTION_ALPHA_SCALE = 32799
GL_POST_CONVOLUTION_ALPHA_SCALE_EXT = 32799
GL_POST_CONVOLUTION_RED_BIAS = 32800
GL_POST_CONVOLUTION_RED_BIAS_EXT = 32800
GL_POST_CONVOLUTION_GREEN_BIAS = 32801
GL_POST_CONVOLUTION_GREEN_BIAS_EXT = 32801
GL_POST_CONVOLUTION_BLUE_BIAS = 32802
GL_POST_CONVOLUTION_BLUE_BIAS_EXT = 32802
GL_POST_CONVOLUTION_ALPHA_BIAS = 32803
GL_POST_CONVOLUTION_ALPHA_BIAS_EXT = 32803
GL_HISTOGRAM = 32804
GL_HISTOGRAM_EXT = 32804
GL_PROXY_HISTOGRAM = 32805
GL_PROXY_HISTOGRAM_EXT = 32805
GL_HISTOGRAM_WIDTH = 32806
GL_HISTOGRAM_WIDTH_EXT = 32806
GL_HISTOGRAM_FORMAT = 32807
GL_HISTOGRAM_FORMAT_EXT = 32807
GL_HISTOGRAM_RED_SIZE = 32808
GL_HISTOGRAM_RED_SIZE_EXT = 32808
GL_HISTOGRAM_GREEN_SIZE = 32809
GL_HISTOGRAM_GREEN_SIZE_EXT = 32809
GL_HISTOGRAM_BLUE_SIZE = 32810
GL_HISTOGRAM_BLUE_SIZE_EXT = 32810
GL_HISTOGRAM_ALPHA_SIZE = 32811
GL_HISTOGRAM_ALPHA_SIZE_EXT = 32811
GL_HISTOGRAM_LUMINANCE_SIZE = 32812
GL_HISTOGRAM_LUMINANCE_SIZE_EXT = 32812
GL_HISTOGRAM_SINK = 32813
GL_HISTOGRAM_SINK_EXT = 32813
GL_MINMAX = 32814
GL_MINMAX_EXT = 32814
GL_MINMAX_FORMAT = 32815
GL_MINMAX_FORMAT_EXT = 32815
GL_MINMAX_SINK = 32816
GL_MINMAX_SINK_EXT = 32816
GL_TABLE_TOO_LARGE_EXT = 32817
GL_TABLE_TOO_LARGE = 32817
GL_UNSIGNED_BYTE_3_3_2 = 32818
GL_UNSIGNED_BYTE_3_3_2_EXT = 32818
GL_UNSIGNED_SHORT_4_4_4_4 = 32819
GL_UNSIGNED_SHORT_4_4_4_4_EXT = 32819
GL_UNSIGNED_SHORT_5_5_5_1 = 32820
GL_UNSIGNED_SHORT_5_5_5_1_EXT = 32820
GL_UNSIGNED_INT_8_8_8_8 = 32821
GL_UNSIGNED_INT_8_8_8_8_EXT = 32821
GL_UNSIGNED_INT_10_10_10_2 = 32822
GL_UNSIGNED_INT_10_10_10_2_EXT = 32822
GL_POLYGON_OFFSET_EXT = 32823
GL_POLYGON_OFFSET_FILL = 32823
GL_POLYGON_OFFSET_FACTOR = 32824
GL_POLYGON_OFFSET_FACTOR_EXT = 32824
GL_POLYGON_OFFSET_BIAS_EXT = 32825
GL_RESCALE_NORMAL = 32826
GL_RESCALE_NORMAL_EXT = 32826
GL_ALPHA4 = 32827
GL_ALPHA4_EXT = 32827
GL_ALPHA8 = 32828
GL_ALPHA8_EXT = 32828
GL_ALPHA12 = 32829
GL_ALPHA12_EXT = 32829
GL_ALPHA16 = 32830
GL_ALPHA16_EXT = 32830
GL_LUMINANCE4 = 32831
GL_LUMINANCE4_EXT = 32831
GL_LUMINANCE8 = 32832
GL_LUMINANCE8_EXT = 32832
GL_LUMINANCE12 = 32833
GL_LUMINANCE12_EXT = 32833
GL_LUMINANCE16 = 32834
GL_LUMINANCE16_EXT = 32834
GL_LUMINANCE4_ALPHA4 = 32835
GL_LUMINANCE4_ALPHA4_EXT = 32835
GL_LUMINANCE6_ALPHA2 = 32836
GL_LUMINANCE6_ALPHA2_EXT = 32836
GL_LUMINANCE8_ALPHA8 = 32837
GL_LUMINANCE8_ALPHA8_EXT = 32837
GL_LUMINANCE12_ALPHA4 = 32838
GL_LUMINANCE12_ALPHA4_EXT = 32838
GL_LUMINANCE12_ALPHA12 = 32839
GL_LUMINANCE12_ALPHA12_EXT = 32839
GL_LUMINANCE16_ALPHA16 = 32840
GL_LUMINANCE16_ALPHA16_EXT = 32840
GL_INTENSITY = 32841
GL_INTENSITY_EXT = 32841
GL_INTENSITY4 = 32842
GL_INTENSITY4_EXT = 32842
GL_INTENSITY8 = 32843
GL_INTENSITY8_EXT = 32843
GL_INTENSITY12 = 32844
GL_INTENSITY12_EXT = 32844
GL_INTENSITY16 = 32845
GL_INTENSITY16_EXT = 32845
GL_RGB2_EXT = 32846
GL_RGB4 = 32847
GL_RGB4_EXT = 32847
GL_RGB5 = 32848
GL_RGB5_EXT = 32848
GL_RGB8 = 32849
GL_RGB8_EXT = 32849
GL_RGB10 = 32850
GL_RGB10_EXT = 32850
GL_RGB12 = 32851
GL_RGB12_EXT = 32851
GL_RGB16 = 32852
GL_RGB16_EXT = 32852
GL_RGBA2 = 32853
GL_RGBA2_EXT = 32853
GL_RGBA4 = 32854
GL_RGBA4_EXT = 32854
GL_RGB5_A1 = 32855
GL_RGB5_A1_EXT = 32855
GL_RGBA8 = 32856
GL_RGBA8_EXT = 32856
GL_RGB10_A2 = 32857
GL_RGB10_A2_EXT = 32857
GL_RGBA12 = 32858
GL_RGBA12_EXT = 32858
GL_RGBA16 = 32859
GL_RGBA16_EXT = 32859
GL_TEXTURE_RED_SIZE = 32860
GL_TEXTURE_RED_SIZE_EXT = 32860
GL_TEXTURE_GREEN_SIZE = 32861
GL_TEXTURE_GREEN_SIZE_EXT = 32861
GL_TEXTURE_BLUE_SIZE = 32862
GL_TEXTURE_BLUE_SIZE_EXT = 32862
GL_TEXTURE_ALPHA_SIZE = 32863
GL_TEXTURE_ALPHA_SIZE_EXT = 32863
GL_TEXTURE_LUMINANCE_SIZE = 32864
GL_TEXTURE_LUMINANCE_SIZE_EXT = 32864
GL_TEXTURE_INTENSITY_SIZE = 32865
GL_TEXTURE_INTENSITY_SIZE_EXT = 32865
GL_REPLACE_EXT = 32866
GL_PROXY_TEXTURE_1D = 32867
GL_PROXY_TEXTURE_1D_EXT = 32867
GL_PROXY_TEXTURE_2D = 32868
GL_PROXY_TEXTURE_2D_EXT = 32868
GL_TEXTURE_TOO_LARGE_EXT = 32869
GL_TEXTURE_PRIORITY = 32870
GL_TEXTURE_PRIORITY_EXT = 32870
GL_TEXTURE_RESIDENT = 32871
GL_TEXTURE_RESIDENT_EXT = 32871
GL_TEXTURE_1D_BINDING_EXT = 32872
GL_TEXTURE_BINDING_1D = 32872
GL_TEXTURE_2D_BINDING_EXT = 32873
GL_TEXTURE_BINDING_2D = 32873
GL_TEXTURE_3D_BINDING_EXT = 32874
GL_TEXTURE_BINDING_3D = 32874
GL_PACK_SKIP_IMAGES = 32875
GL_PACK_SKIP_IMAGES_EXT = 32875
GL_PACK_IMAGE_HEIGHT = 32876
GL_PACK_IMAGE_HEIGHT_EXT = 32876
GL_UNPACK_SKIP_IMAGES = 32877
GL_UNPACK_SKIP_IMAGES_EXT = 32877
GL_UNPACK_IMAGE_HEIGHT = 32878
GL_UNPACK_IMAGE_HEIGHT_EXT = 32878
GL_TEXTURE_3D = 32879
GL_TEXTURE_3D_EXT = 32879
GL_PROXY_TEXTURE_3D = 32880
GL_PROXY_TEXTURE_3D_EXT = 32880
GL_TEXTURE_DEPTH = 32881
GL_TEXTURE_DEPTH_EXT = 32881
GL_TEXTURE_WRAP_R = 32882
GL_TEXTURE_WRAP_R_EXT = 32882
GL_MAX_3D_TEXTURE_SIZE = 32883
GL_MAX_3D_TEXTURE_SIZE_EXT = 32883
GL_VERTEX_ARRAY = 32884
GL_VERTEX_ARRAY_EXT = 32884
GL_NORMAL_ARRAY = 32885
GL_NORMAL_ARRAY_EXT = 32885
GL_COLOR_ARRAY = 32886
GL_COLOR_ARRAY_EXT = 32886
GL_INDEX_ARRAY = 32887
GL_INDEX_ARRAY_EXT = 32887
GL_TEXTURE_COORD_ARRAY = 32888
GL_TEXTURE_COORD_ARRAY_EXT = 32888
GL_EDGE_FLAG_ARRAY = 32889
GL_EDGE_FLAG_ARRAY_EXT = 32889
GL_VERTEX_ARRAY_SIZE = 32890
GL_VERTEX_ARRAY_SIZE_EXT = 32890
GL_VERTEX_ARRAY_TYPE = 32891
GL_VERTEX_ARRAY_TYPE_EXT = 32891
GL_VERTEX_ARRAY_STRIDE = 32892
GL_VERTEX_ARRAY_STRIDE_EXT = 32892
GL_VERTEX_ARRAY_COUNT_EXT = 32893
GL_NORMAL_ARRAY_TYPE = 32894
GL_NORMAL_ARRAY_TYPE_EXT = 32894
GL_NORMAL_ARRAY_STRIDE = 32895
GL_NORMAL_ARRAY_STRIDE_EXT = 32895
GL_NORMAL_ARRAY_COUNT_EXT = 32896
GL_COLOR_ARRAY_SIZE = 32897
GL_COLOR_ARRAY_SIZE_EXT = 32897
GL_COLOR_ARRAY_TYPE = 32898
GL_COLOR_ARRAY_TYPE_EXT = 32898
GL_COLOR_ARRAY_STRIDE = 32899
GL_COLOR_ARRAY_STRIDE_EXT = 32899
GL_COLOR_ARRAY_COUNT_EXT = 32900
GL_INDEX_ARRAY_TYPE = 32901
GL_INDEX_ARRAY_TYPE_EXT = 32901
GL_INDEX_ARRAY_STRIDE = 32902
GL_INDEX_ARRAY_STRIDE_EXT = 32902
GL_INDEX_ARRAY_COUNT_EXT = 32903
GL_TEXTURE_COORD_ARRAY_SIZE = 32904
GL_TEXTURE_COORD_ARRAY_SIZE_EXT = 32904
GL_TEXTURE_COORD_ARRAY_TYPE = 32905
GL_TEXTURE_COORD_ARRAY_TYPE_EXT = 32905
GL_TEXTURE_COORD_ARRAY_STRIDE = 32906
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT = 32906
GL_TEXTURE_COORD_ARRAY_COUNT_EXT = 32907
GL_EDGE_FLAG_ARRAY_STRIDE = 32908
GL_EDGE_FLAG_ARRAY_STRIDE_EXT = 32908
GL_EDGE_FLAG_ARRAY_COUNT_EXT = 32909
GL_VERTEX_ARRAY_POINTER = 32910
GL_VERTEX_ARRAY_POINTER_EXT = 32910
GL_NORMAL_ARRAY_POINTER = 32911
GL_NORMAL_ARRAY_POINTER_EXT = 32911
GL_COLOR_ARRAY_POINTER = 32912
GL_COLOR_ARRAY_POINTER_EXT = 32912
GL_INDEX_ARRAY_POINTER = 32913
GL_INDEX_ARRAY_POINTER_EXT = 32913
GL_TEXTURE_COORD_ARRAY_POINTER = 32914
GL_TEXTURE_COORD_ARRAY_POINTER_EXT = 32914
GL_EDGE_FLAG_ARRAY_POINTER = 32915
GL_EDGE_FLAG_ARRAY_POINTER_EXT = 32915
GL_MULTISAMPLE = 32925
GL_MULTISAMPLE_ARB = 32925
GL_MULTISAMPLE_EXT = 32925
GL_SAMPLE_ALPHA_TO_COVERAGE = 32926
GL_SAMPLE_ALPHA_TO_COVERAGE_ARB = 32926
GL_SAMPLE_ALPHA_TO_MASK_EXT = 32926
GL_SAMPLE_ALPHA_TO_ONE = 32927
GL_SAMPLE_ALPHA_TO_ONE_ARB = 32927
GL_SAMPLE_ALPHA_TO_ONE_EXT = 32927
GL_SAMPLE_COVERAGE = 32928
GL_SAMPLE_COVERAGE_ARB = 32928
GL_SAMPLE_MASK_EXT = 32928
GL_1PASS_EXT = 32929
GL_2PASS_0_EXT = 32930
GL_2PASS_1_EXT = 32931
GL_4PASS_0_EXT = 32932
GL_4PASS_1_EXT = 32933
GL_4PASS_2_EXT = 32934
GL_4PASS_3_EXT = 32935
GL_SAMPLE_BUFFERS = 32936
GL_SAMPLE_BUFFERS_ARB = 32936
GL_SAMPLE_BUFFERS_EXT = 32936
GL_SAMPLES = 32937
GL_SAMPLES_ARB = 32937
GL_SAMPLES_EXT = 32937
GL_SAMPLE_COVERAGE_VALUE = 32938
GL_SAMPLE_COVERAGE_VALUE_ARB = 32938
GL_SAMPLE_MASK_VALUE_EXT = 32938
GL_SAMPLE_COVERAGE_INVERT = 32939
GL_SAMPLE_COVERAGE_INVERT_ARB = 32939
GL_SAMPLE_MASK_INVERT_EXT = 32939
GL_SAMPLE_PATTERN_EXT = 32940
GL_COLOR_MATRIX = 32945
GL_COLOR_MATRIX_STACK_DEPTH = 32946
GL_MAX_COLOR_MATRIX_STACK_DEPTH = 32947
GL_POST_COLOR_MATRIX_RED_SCALE = 32948
GL_POST_COLOR_MATRIX_GREEN_SCALE = 32949
GL_POST_COLOR_MATRIX_BLUE_SCALE = 32950
GL_POST_COLOR_MATRIX_ALPHA_SCALE = 32951
GL_POST_COLOR_MATRIX_RED_BIAS = 32952
GL_POST_COLOR_MATRIX_GREEN_BIAS = 32953
GL_POST_COLOR_MATRIX_BLUE_BIAS = 32954
GL_POST_COLOR_MATRIX_ALPHA_BIAS = 32955
GL_TEXTURE_COMPARE_FAIL_VALUE_ARB = 32959
GL_BLEND_DST_RGB = 32968
GL_BLEND_DST_RGB_EXT = 32968
GL_BLEND_SRC_RGB = 32969
GL_BLEND_SRC_RGB_EXT = 32969
GL_BLEND_DST_ALPHA = 32970
GL_BLEND_DST_ALPHA_EXT = 32970
GL_BLEND_SRC_ALPHA = 32971
GL_BLEND_SRC_ALPHA_EXT = 32971
GL_422_EXT = 32972
GL_422_REV_EXT = 32973
GL_422_AVERAGE_EXT = 32974
GL_422_REV_AVERAGE_EXT = 32975
GL_COLOR_TABLE = 32976
GL_POST_CONVOLUTION_COLOR_TABLE = 32977
GL_POST_COLOR_MATRIX_COLOR_TABLE = 32978
GL_PROXY_COLOR_TABLE = 32979
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = 32980
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = 32981
GL_COLOR_TABLE_SCALE = 32982
GL_COLOR_TABLE_BIAS = 32983
GL_COLOR_TABLE_FORMAT = 32984
GL_COLOR_TABLE_WIDTH = 32985
GL_COLOR_TABLE_RED_SIZE = 32986
GL_COLOR_TABLE_GREEN_SIZE = 32987
GL_COLOR_TABLE_BLUE_SIZE = 32988
GL_COLOR_TABLE_ALPHA_SIZE = 32989
GL_COLOR_TABLE_LUMINANCE_SIZE = 32990
GL_COLOR_TABLE_INTENSITY_SIZE = 32991
GL_BGR = 32992
GL_BGR_EXT = 32992
GL_BGRA = 32993
GL_BGRA_EXT = 32993
GL_BGRA_IMG = 32993
GL_COLOR_INDEX1_EXT = 32994
GL_COLOR_INDEX2_EXT = 32995
GL_COLOR_INDEX4_EXT = 32996
GL_COLOR_INDEX8_EXT = 32997
GL_COLOR_INDEX12_EXT = 32998
GL_COLOR_INDEX16_EXT = 32999
GL_MAX_ELEMENTS_VERTICES = 33000
GL_MAX_ELEMENTS_VERTICES_EXT = 33000
GL_MAX_ELEMENTS_INDICES = 33001
GL_MAX_ELEMENTS_INDICES_EXT = 33001
GL_PHONG_WIN = 33002
GL_PHONG_HINT_WIN = 33003
GL_FOG_SPECULAR_TEXTURE_WIN = 33004
GL_TEXTURE_INDEX_SIZE_EXT = 33005
GL_PARAMETER_BUFFER = 33006
GL_PARAMETER_BUFFER_ARB = 33006
GL_PARAMETER_BUFFER_BINDING = 33007
GL_PARAMETER_BUFFER_BINDING_ARB = 33007
GL_CLIP_VOLUME_CLIPPING_HINT_EXT = 33008
GL_POINT_SIZE_MIN = 33062
GL_POINT_SIZE_MIN_ARB = 33062
GL_POINT_SIZE_MIN_EXT = 33062
GL_POINT_SIZE_MAX = 33063
GL_POINT_SIZE_MAX_ARB = 33063
GL_POINT_SIZE_MAX_EXT = 33063
GL_POINT_FADE_THRESHOLD_SIZE = 33064
GL_POINT_FADE_THRESHOLD_SIZE_ARB = 33064
GL_POINT_FADE_THRESHOLD_SIZE_EXT = 33064
GL_DISTANCE_ATTENUATION_EXT = 33065
GL_POINT_DISTANCE_ATTENUATION = 33065
GL_POINT_DISTANCE_ATTENUATION_ARB = 33065
GL_CLAMP_TO_BORDER = 33069
GL_CLAMP_TO_BORDER_ARB = 33069
GL_CLAMP_TO_BORDER_EXT = 33069
GL_CLAMP_TO_EDGE = 33071
GL_TEXTURE_MIN_LOD = 33082
GL_TEXTURE_MAX_LOD = 33083
GL_TEXTURE_BASE_LEVEL = 33084
GL_TEXTURE_MAX_LEVEL = 33085
GL_IGNORE_BORDER_HP = 33104
GL_CONSTANT_BORDER = 33105
GL_CONSTANT_BORDER_HP = 33105
GL_REPLICATE_BORDER = 33107
GL_REPLICATE_BORDER_HP = 33107
GL_CONVOLUTION_BORDER_COLOR = 33108
GL_CONVOLUTION_BORDER_COLOR_HP = 33108
GL_IMAGE_SCALE_X_HP = 33109
GL_IMAGE_SCALE_Y_HP = 33110
GL_IMAGE_TRANSLATE_X_HP = 33111
GL_IMAGE_TRANSLATE_Y_HP = 33112
GL_IMAGE_ROTATE_ANGLE_HP = 33113
GL_IMAGE_ROTATE_ORIGIN_X_HP = 33114
GL_IMAGE_ROTATE_ORIGIN_Y_HP = 33115
GL_IMAGE_MAG_FILTER_HP = 33116
GL_IMAGE_MIN_FILTER_HP = 33117
GL_IMAGE_CUBIC_WEIGHT_HP = 33118
GL_CUBIC_HP = 33119
GL_AVERAGE_HP = 33120
GL_IMAGE_TRANSFORM_2D_HP = 33121
GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = 33122
GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = 33123
GL_OCCLUSION_TEST_HP = 33125
GL_OCCLUSION_TEST_RESULT_HP = 33126
GL_TEXTURE_LIGHTING_MODE_HP = 33127
GL_TEXTURE_POST_SPECULAR_HP = 33128
GL_TEXTURE_PRE_SPECULAR_HP = 33129
GL_GENERATE_MIPMAP = 33169
GL_GENERATE_MIPMAP_HINT = 33170
GL_DEPTH_COMPONENT16 = 33189
GL_DEPTH_COMPONENT16_ARB = 33189
GL_DEPTH_COMPONENT24 = 33190
GL_DEPTH_COMPONENT24_ARB = 33190
GL_DEPTH_COMPONENT32 = 33191
GL_DEPTH_COMPONENT32_ARB = 33191
GL_ARRAY_ELEMENT_LOCK_FIRST_EXT = 33192
GL_ARRAY_ELEMENT_LOCK_COUNT_EXT = 33193
GL_CULL_VERTEX_EXT = 33194
GL_CULL_VERTEX_EYE_POSITION_EXT = 33195
GL_CULL_VERTEX_OBJECT_POSITION_EXT = 33196
GL_IUI_V2F_EXT = 33197
GL_IUI_V3F_EXT = 33198
GL_IUI_N3F_V2F_EXT = 33199
GL_IUI_N3F_V3F_EXT = 33200
GL_T2F_IUI_V2F_EXT = 33201
GL_T2F_IUI_V3F_EXT = 33202
GL_T2F_IUI_N3F_V2F_EXT = 33203
GL_T2F_IUI_N3F_V3F_EXT = 33204
GL_INDEX_TEST_EXT = 33205
GL_INDEX_TEST_FUNC_EXT = 33206
GL_INDEX_TEST_REF_EXT = 33207
GL_INDEX_MATERIAL_EXT = 33208
GL_INDEX_MATERIAL_PARAMETER_EXT = 33209
GL_INDEX_MATERIAL_FACE_EXT = 33210
GL_UNPACK_CONSTANT_DATA_SUNX = 33237
GL_TEXTURE_CONSTANT_DATA_SUNX = 33238
GL_LIGHT_MODEL_COLOR_CONTROL = 33272
GL_LIGHT_MODEL_COLOR_CONTROL_EXT = 33272
GL_SINGLE_COLOR = 33273
GL_SINGLE_COLOR_EXT = 33273
GL_SEPARATE_SPECULAR_COLOR = 33274
GL_SEPARATE_SPECULAR_COLOR_EXT = 33274
GL_SHARED_TEXTURE_PALETTE_EXT = 33275
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 33296
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT = 33296
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 33297
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT = 33297
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 33298
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 33299
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 33300
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 33301
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 33302
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 33303
GL_FRAMEBUFFER_DEFAULT = 33304
GL_FRAMEBUFFER_UNDEFINED = 33305
GL_DEPTH_STENCIL_ATTACHMENT = 33306
GL_MAJOR_VERSION = 33307
GL_MINOR_VERSION = 33308
GL_NUM_EXTENSIONS = 33309
GL_CONTEXT_FLAGS = 33310
GL_BUFFER_IMMUTABLE_STORAGE = 33311
GL_BUFFER_IMMUTABLE_STORAGE_EXT = 33311
GL_BUFFER_STORAGE_FLAGS = 33312
GL_BUFFER_STORAGE_FLAGS_EXT = 33312
GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED = 33313
GL_INDEX = 33314
GL_COMPRESSED_RED = 33317
GL_COMPRESSED_RG = 33318
GL_RG = 33319
GL_RG_EXT = 33319
GL_RG_INTEGER = 33320
GL_R8 = 33321
GL_R8_EXT = 33321
GL_R16 = 33322
GL_R16_EXT = 33322
GL_RG8 = 33323
GL_RG8_EXT = 33323
GL_RG16 = 33324
GL_RG16_EXT = 33324
GL_R16F = 33325
GL_R16F_EXT = 33325
GL_R32F = 33326
GL_R32F_EXT = 33326
GL_RG16F = 33327
GL_RG16F_EXT = 33327
GL_RG32F = 33328
GL_RG32F_EXT = 33328
GL_R8I = 33329
GL_R8UI = 33330
GL_R16I = 33331
GL_R16UI = 33332
GL_R32I = 33333
GL_R32UI = 33334
GL_RG8I = 33335
GL_RG8UI = 33336
GL_RG16I = 33337
GL_RG16UI = 33338
GL_RG32I = 33339
GL_RG32UI = 33340
GL_SYNC_CL_EVENT_ARB = 33344
GL_SYNC_CL_EVENT_COMPLETE_ARB = 33345
GL_DEBUG_OUTPUT_SYNCHRONOUS = 33346
GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB = 33346
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH = 33347
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB = 33347
GL_DEBUG_CALLBACK_FUNCTION = 33348
GL_DEBUG_CALLBACK_FUNCTION_ARB = 33348
GL_DEBUG_CALLBACK_USER_PARAM = 33349
GL_DEBUG_CALLBACK_USER_PARAM_ARB = 33349
GL_DEBUG_SOURCE_API = 33350
GL_DEBUG_SOURCE_API_ARB = 33350
GL_DEBUG_SOURCE_WINDOW_SYSTEM = 33351
GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB = 33351
GL_DEBUG_SOURCE_SHADER_COMPILER = 33352
GL_DEBUG_SOURCE_SHADER_COMPILER_ARB = 33352
GL_DEBUG_SOURCE_THIRD_PARTY = 33353
GL_DEBUG_SOURCE_THIRD_PARTY_ARB = 33353
GL_DEBUG_SOURCE_APPLICATION = 33354
GL_DEBUG_SOURCE_APPLICATION_ARB = 33354
GL_DEBUG_SOURCE_OTHER = 33355
GL_DEBUG_SOURCE_OTHER_ARB = 33355
GL_DEBUG_TYPE_ERROR = 33356
GL_DEBUG_TYPE_ERROR_ARB = 33356
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR = 33357
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB = 33357
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR = 33358
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB = 33358
GL_DEBUG_TYPE_PORTABILITY = 33359
GL_DEBUG_TYPE_PORTABILITY_ARB = 33359
GL_DEBUG_TYPE_PERFORMANCE = 33360
GL_DEBUG_TYPE_PERFORMANCE_ARB = 33360
GL_DEBUG_TYPE_OTHER = 33361
GL_DEBUG_TYPE_OTHER_ARB = 33361
GL_LOSE_CONTEXT_ON_RESET = 33362
GL_LOSE_CONTEXT_ON_RESET_ARB = 33362
GL_LOSE_CONTEXT_ON_RESET_EXT = 33362
GL_GUILTY_CONTEXT_RESET = 33363
GL_GUILTY_CONTEXT_RESET_ARB = 33363
GL_GUILTY_CONTEXT_RESET_EXT = 33363
GL_INNOCENT_CONTEXT_RESET = 33364
GL_INNOCENT_CONTEXT_RESET_ARB = 33364
GL_INNOCENT_CONTEXT_RESET_EXT = 33364
GL_UNKNOWN_CONTEXT_RESET = 33365
GL_UNKNOWN_CONTEXT_RESET_ARB = 33365
GL_UNKNOWN_CONTEXT_RESET_EXT = 33365
GL_RESET_NOTIFICATION_STRATEGY = 33366
GL_RESET_NOTIFICATION_STRATEGY_ARB = 33366
GL_RESET_NOTIFICATION_STRATEGY_EXT = 33366
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 33367
GL_PROGRAM_SEPARABLE = 33368
GL_PROGRAM_SEPARABLE_EXT = 33368
GL_ACTIVE_PROGRAM = 33369
GL_ACTIVE_PROGRAM_EXT = 35725
GL_PROGRAM_PIPELINE_BINDING = 33370
GL_PROGRAM_PIPELINE_BINDING_EXT = 33370
GL_MAX_VIEWPORTS = 33371
GL_VIEWPORT_SUBPIXEL_BITS = 33372
GL_VIEWPORT_SUBPIXEL_BITS_EXT = 33372
GL_VIEWPORT_BOUNDS_RANGE = 33373
GL_VIEWPORT_BOUNDS_RANGE_EXT = 33373
GL_LAYER_PROVOKING_VERTEX = 33374
GL_LAYER_PROVOKING_VERTEX_EXT = 33374
GL_VIEWPORT_INDEX_PROVOKING_VERTEX = 33375
GL_VIEWPORT_INDEX_PROVOKING_VERTEX_EXT = 33375
GL_UNDEFINED_VERTEX = 33376
GL_UNDEFINED_VERTEX_EXT = 33376
GL_NO_RESET_NOTIFICATION = 33377
GL_NO_RESET_NOTIFICATION_ARB = 33377
GL_NO_RESET_NOTIFICATION_EXT = 33377
GL_MAX_COMPUTE_SHARED_MEMORY_SIZE = 33378
GL_MAX_COMPUTE_UNIFORM_COMPONENTS = 33379
GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = 33380
GL_MAX_COMPUTE_ATOMIC_COUNTERS = 33381
GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = 33382
GL_COMPUTE_WORK_GROUP_SIZE = 33383
GL_DEBUG_TYPE_MARKER = 33384
GL_DEBUG_TYPE_PUSH_GROUP = 33385
GL_DEBUG_TYPE_POP_GROUP = 33386
GL_DEBUG_SEVERITY_NOTIFICATION = 33387
GL_MAX_DEBUG_GROUP_STACK_DEPTH = 33388
GL_DEBUG_GROUP_STACK_DEPTH = 33389
GL_MAX_UNIFORM_LOCATIONS = 33390
GL_INTERNALFORMAT_SUPPORTED = 33391
GL_INTERNALFORMAT_PREFERRED = 33392
GL_INTERNALFORMAT_RED_SIZE = 33393
GL_INTERNALFORMAT_GREEN_SIZE = 33394
GL_INTERNALFORMAT_BLUE_SIZE = 33395
GL_INTERNALFORMAT_ALPHA_SIZE = 33396
GL_INTERNALFORMAT_DEPTH_SIZE = 33397
GL_INTERNALFORMAT_STENCIL_SIZE = 33398
GL_INTERNALFORMAT_SHARED_SIZE = 33399
GL_INTERNALFORMAT_RED_TYPE = 33400
GL_INTERNALFORMAT_GREEN_TYPE = 33401
GL_INTERNALFORMAT_BLUE_TYPE = 33402
GL_INTERNALFORMAT_ALPHA_TYPE = 33403
GL_INTERNALFORMAT_DEPTH_TYPE = 33404
GL_INTERNALFORMAT_STENCIL_TYPE = 33405
GL_MAX_WIDTH = 33406
GL_MAX_HEIGHT = 33407
GL_MAX_DEPTH = 33408
GL_MAX_LAYERS = 33409
GL_MAX_COMBINED_DIMENSIONS = 33410
GL_COLOR_COMPONENTS = 33411
GL_DEPTH_COMPONENTS = 33412
GL_STENCIL_COMPONENTS = 33413
GL_COLOR_RENDERABLE = 33414
GL_DEPTH_RENDERABLE = 33415
GL_STENCIL_RENDERABLE = 33416
GL_FRAMEBUFFER_RENDERABLE = 33417
GL_FRAMEBUFFER_RENDERABLE_LAYERED = 33418
GL_FRAMEBUFFER_BLEND = 33419
GL_READ_PIXELS = 33420
GL_READ_PIXELS_FORMAT = 33421
GL_READ_PIXELS_TYPE = 33422
GL_TEXTURE_IMAGE_FORMAT = 33423
GL_TEXTURE_IMAGE_TYPE = 33424
GL_GET_TEXTURE_IMAGE_FORMAT = 33425
GL_GET_TEXTURE_IMAGE_TYPE = 33426
GL_MIPMAP = 33427
GL_MANUAL_GENERATE_MIPMAP = 33428
GL_AUTO_GENERATE_MIPMAP = 33429
GL_COLOR_ENCODING = 33430
GL_SRGB_READ = 33431
GL_SRGB_WRITE = 33432
GL_SRGB_DECODE_ARB = 33433
GL_FILTER = 33434
GL_VERTEX_TEXTURE = 33435
GL_TESS_CONTROL_TEXTURE = 33436
GL_TESS_EVALUATION_TEXTURE = 33437
GL_GEOMETRY_TEXTURE = 33438
GL_FRAGMENT_TEXTURE = 33439
GL_COMPUTE_TEXTURE = 33440
GL_TEXTURE_SHADOW = 33441
GL_TEXTURE_GATHER = 33442
GL_TEXTURE_GATHER_SHADOW = 33443
GL_SHADER_IMAGE_LOAD = 33444
GL_SHADER_IMAGE_STORE = 33445
GL_SHADER_IMAGE_ATOMIC = 33446
GL_IMAGE_TEXEL_SIZE = 33447
GL_IMAGE_COMPATIBILITY_CLASS = 33448
GL_IMAGE_PIXEL_FORMAT = 33449
GL_IMAGE_PIXEL_TYPE = 33450
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST = 33452
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST = 33453
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE = 33454
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE = 33455
GL_TEXTURE_COMPRESSED_BLOCK_WIDTH = 33457
GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT = 33458
GL_TEXTURE_COMPRESSED_BLOCK_SIZE = 33459
GL_CLEAR_BUFFER = 33460
GL_TEXTURE_VIEW = 33461
GL_VIEW_COMPATIBILITY_CLASS = 33462
GL_FULL_SUPPORT = 33463
GL_CAVEAT_SUPPORT = 33464
GL_IMAGE_CLASS_4_X_32 = 33465
GL_IMAGE_CLASS_2_X_32 = 33466
GL_IMAGE_CLASS_1_X_32 = 33467
GL_IMAGE_CLASS_4_X_16 = 33468
GL_IMAGE_CLASS_2_X_16 = 33469
GL_IMAGE_CLASS_1_X_16 = 33470
GL_IMAGE_CLASS_4_X_8 = 33471
GL_IMAGE_CLASS_2_X_8 = 33472
GL_IMAGE_CLASS_1_X_8 = 33473
GL_IMAGE_CLASS_11_11_10 = 33474
GL_IMAGE_CLASS_10_10_10_2 = 33475
GL_VIEW_CLASS_128_BITS = 33476
GL_VIEW_CLASS_96_BITS = 33477
GL_VIEW_CLASS_64_BITS = 33478
GL_VIEW_CLASS_48_BITS = 33479
GL_VIEW_CLASS_32_BITS = 33480
GL_VIEW_CLASS_24_BITS = 33481
GL_VIEW_CLASS_16_BITS = 33482
GL_VIEW_CLASS_8_BITS = 33483
GL_VIEW_CLASS_S3TC_DXT1_RGB = 33484
GL_VIEW_CLASS_S3TC_DXT1_RGBA = 33485
GL_VIEW_CLASS_S3TC_DXT3_RGBA = 33486
GL_VIEW_CLASS_S3TC_DXT5_RGBA = 33487
GL_VIEW_CLASS_RGTC1_RED = 33488
GL_VIEW_CLASS_RGTC2_RG = 33489
GL_VIEW_CLASS_BPTC_UNORM = 33490
GL_VIEW_CLASS_BPTC_FLOAT = 33491
GL_VERTEX_ATTRIB_BINDING = 33492
GL_VERTEX_ATTRIB_RELATIVE_OFFSET = 33493
GL_VERTEX_BINDING_DIVISOR = 33494
GL_VERTEX_BINDING_OFFSET = 33495
GL_VERTEX_BINDING_STRIDE = 33496
GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = 33497
GL_MAX_VERTEX_ATTRIB_BINDINGS = 33498
GL_TEXTURE_VIEW_MIN_LEVEL = 33499
GL_TEXTURE_VIEW_MIN_LEVEL_EXT = 33499
GL_TEXTURE_VIEW_NUM_LEVELS = 33500
GL_TEXTURE_VIEW_NUM_LEVELS_EXT = 33500
GL_TEXTURE_VIEW_MIN_LAYER = 33501
GL_TEXTURE_VIEW_MIN_LAYER_EXT = 33501
GL_TEXTURE_VIEW_NUM_LAYERS = 33502
GL_TEXTURE_VIEW_NUM_LAYERS_EXT = 33502
GL_TEXTURE_IMMUTABLE_LEVELS = 33503
GL_BUFFER = 33504
GL_SHADER = 33505
GL_PROGRAM = 33506
GL_QUERY = 33507
GL_PROGRAM_PIPELINE = 33508
GL_MAX_VERTEX_ATTRIB_STRIDE = 33509
GL_SAMPLER = 33510
GL_DISPLAY_LIST = 33511
GL_MAX_LABEL_LENGTH = 33512
GL_NUM_SHADING_LANGUAGE_VERSIONS = 33513
GL_QUERY_TARGET = 33514
GL_TRANSFORM_FEEDBACK_OVERFLOW = 33516
GL_TRANSFORM_FEEDBACK_OVERFLOW_ARB = 33516
GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW = 33517
GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW_ARB = 33517
GL_VERTICES_SUBMITTED = 33518
GL_VERTICES_SUBMITTED_ARB = 33518
GL_PRIMITIVES_SUBMITTED = 33519
GL_PRIMITIVES_SUBMITTED_ARB = 33519
GL_VERTEX_SHADER_INVOCATIONS = 33520
GL_VERTEX_SHADER_INVOCATIONS_ARB = 33520
GL_TESS_CONTROL_SHADER_PATCHES = 33521
GL_TESS_CONTROL_SHADER_PATCHES_ARB = 33521
GL_TESS_EVALUATION_SHADER_INVOCATIONS = 33522
GL_TESS_EVALUATION_SHADER_INVOCATIONS_ARB = 33522
GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED = 33523
GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED_ARB = 33523
GL_FRAGMENT_SHADER_INVOCATIONS = 33524
GL_FRAGMENT_SHADER_INVOCATIONS_ARB = 33524
GL_COMPUTE_SHADER_INVOCATIONS = 33525
GL_COMPUTE_SHADER_INVOCATIONS_ARB = 33525
GL_CLIPPING_INPUT_PRIMITIVES = 33526
GL_CLIPPING_INPUT_PRIMITIVES_ARB = 33526
GL_CLIPPING_OUTPUT_PRIMITIVES = 33527
GL_CLIPPING_OUTPUT_PRIMITIVES_ARB = 33527
GL_SPARSE_BUFFER_PAGE_SIZE_ARB = 33528
GL_MAX_CULL_DISTANCES = 33529
GL_MAX_CULL_DISTANCES_EXT = 33529
GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES = 33530
GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES_EXT = 33530
GL_CONTEXT_RELEASE_BEHAVIOR = 33531
GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH = 33532
GL_PIXEL_TRANSFORM_2D_EXT = 33584
GL_PIXEL_MAG_FILTER_EXT = 33585
GL_PIXEL_MIN_FILTER_EXT = 33586
GL_PIXEL_CUBIC_WEIGHT_EXT = 33587
GL_CUBIC_EXT = 33588
GL_AVERAGE_EXT = 33589
GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = 33590
GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = 33591
GL_PIXEL_TRANSFORM_2D_MATRIX_EXT = 33592
GL_FRAGMENT_MATERIAL_EXT = 33609
GL_FRAGMENT_NORMAL_EXT = 33610
GL_FRAGMENT_COLOR_EXT = 33612
GL_ATTENUATION_EXT = 33613
GL_SHADOW_ATTENUATION_EXT = 33614
GL_TEXTURE_APPLICATION_MODE_EXT = 33615
GL_TEXTURE_LIGHT_EXT = 33616
GL_TEXTURE_MATERIAL_FACE_EXT = 33617
GL_TEXTURE_MATERIAL_PARAMETER_EXT = 33618
GL_UNSIGNED_BYTE_2_3_3_REV = 33634
GL_UNSIGNED_BYTE_2_3_3_REV_EXT = 33634
GL_UNSIGNED_SHORT_5_6_5 = 33635
GL_UNSIGNED_SHORT_5_6_5_EXT = 33635
GL_UNSIGNED_SHORT_5_6_5_REV = 33636
GL_UNSIGNED_SHORT_5_6_5_REV_EXT = 33636
GL_UNSIGNED_SHORT_4_4_4_4_REV = 33637
GL_UNSIGNED_SHORT_4_4_4_4_REV_EXT = 33637
GL_UNSIGNED_SHORT_4_4_4_4_REV_IMG = 33637
GL_UNSIGNED_SHORT_1_5_5_5_REV = 33638
GL_UNSIGNED_SHORT_1_5_5_5_REV_EXT = 33638
GL_UNSIGNED_INT_8_8_8_8_REV = 33639
GL_UNSIGNED_INT_8_8_8_8_REV_EXT = 33639
GL_UNSIGNED_INT_2_10_10_10_REV = 33640
GL_UNSIGNED_INT_2_10_10_10_REV_EXT = 33640
GL_MIRRORED_REPEAT = 33648
GL_MIRRORED_REPEAT_ARB = 33648
GL_RGB_S3TC = 33696
GL_RGB4_S3TC = 33697
GL_RGBA_S3TC = 33698
GL_RGBA4_S3TC = 33699
GL_RGBA_DXT5_S3TC = 33700
GL_RGBA4_DXT5_S3TC = 33701
GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 33776
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 33777
GL_COMPRESSED_RGBA_S3TC_DXT3_ANGLE = 33778
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = 33778
GL_COMPRESSED_RGBA_S3TC_DXT5_ANGLE = 33779
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = 33779
GL_TANGENT_ARRAY_EXT = 33849
GL_BINORMAL_ARRAY_EXT = 33850
GL_CURRENT_TANGENT_EXT = 33851
GL_CURRENT_BINORMAL_EXT = 33852
GL_TANGENT_ARRAY_TYPE_EXT = 33854
GL_TANGENT_ARRAY_STRIDE_EXT = 33855
GL_BINORMAL_ARRAY_TYPE_EXT = 33856
GL_BINORMAL_ARRAY_STRIDE_EXT = 33857
GL_TANGENT_ARRAY_POINTER_EXT = 33858
GL_BINORMAL_ARRAY_POINTER_EXT = 33859
GL_MAP1_TANGENT_EXT = 33860
GL_MAP2_TANGENT_EXT = 33861
GL_MAP1_BINORMAL_EXT = 33862
GL_MAP2_BINORMAL_EXT = 33863
GL_FOG_COORDINATE_SOURCE = 33872
GL_FOG_COORDINATE_SOURCE_EXT = 33872
GL_FOG_COORD_SRC = 33872
GL_FOG_COORDINATE = 33873
GL_FOG_COORD = 33873
GL_FOG_COORDINATE_EXT = 33873
GL_FRAGMENT_DEPTH = 33874
GL_FRAGMENT_DEPTH_EXT = 33874
GL_CURRENT_FOG_COORDINATE = 33875
GL_CURRENT_FOG_COORD = 33875
GL_CURRENT_FOG_COORDINATE_EXT = 33875
GL_FOG_COORDINATE_ARRAY_TYPE = 33876
GL_FOG_COORDINATE_ARRAY_TYPE_EXT = 33876
GL_FOG_COORD_ARRAY_TYPE = 33876
GL_FOG_COORDINATE_ARRAY_STRIDE = 33877
GL_FOG_COORDINATE_ARRAY_STRIDE_EXT = 33877
GL_FOG_COORD_ARRAY_STRIDE = 33877
GL_FOG_COORDINATE_ARRAY_POINTER = 33878
GL_FOG_COORDINATE_ARRAY_POINTER_EXT = 33878
GL_FOG_COORD_ARRAY_POINTER = 33878
GL_FOG_COORDINATE_ARRAY = 33879
GL_FOG_COORDINATE_ARRAY_EXT = 33879
GL_FOG_COORD_ARRAY = 33879
GL_COLOR_SUM = 33880
GL_COLOR_SUM_ARB = 33880
GL_COLOR_SUM_EXT = 33880
GL_CURRENT_SECONDARY_COLOR = 33881
GL_CURRENT_SECONDARY_COLOR_EXT = 33881
GL_SECONDARY_COLOR_ARRAY_SIZE = 33882
GL_SECONDARY_COLOR_ARRAY_SIZE_EXT = 33882
GL_SECONDARY_COLOR_ARRAY_TYPE = 33883
GL_SECONDARY_COLOR_ARRAY_TYPE_EXT = 33883
GL_SECONDARY_COLOR_ARRAY_STRIDE = 33884
GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT = 33884
GL_SECONDARY_COLOR_ARRAY_POINTER = 33885
GL_SECONDARY_COLOR_ARRAY_POINTER_EXT = 33885
GL_SECONDARY_COLOR_ARRAY = 33886
GL_SECONDARY_COLOR_ARRAY_EXT = 33886
GL_CURRENT_RASTER_SECONDARY_COLOR = 33887
GL_ALIASED_POINT_SIZE_RANGE = 33901
GL_ALIASED_LINE_WIDTH_RANGE = 33902
GL_SCREEN_COORDINATES_REND = 33936
GL_INVERTED_SCREEN_W_REND = 33937
GL_TEXTURE0 = 33984
GL_TEXTURE0_ARB = 33984
GL_TEXTURE1 = 33985
GL_TEXTURE1_ARB = 33985
GL_TEXTURE2 = 33986
GL_TEXTURE2_ARB = 33986
GL_TEXTURE3 = 33987
GL_TEXTURE3_ARB = 33987
GL_TEXTURE4 = 33988
GL_TEXTURE4_ARB = 33988
GL_TEXTURE5 = 33989
GL_TEXTURE5_ARB = 33989
GL_TEXTURE6 = 33990
GL_TEXTURE6_ARB = 33990
GL_TEXTURE7 = 33991
GL_TEXTURE7_ARB = 33991
GL_TEXTURE8 = 33992
GL_TEXTURE8_ARB = 33992
GL_TEXTURE9 = 33993
GL_TEXTURE9_ARB = 33993
GL_TEXTURE10 = 33994
GL_TEXTURE10_ARB = 33994
GL_TEXTURE11 = 33995
GL_TEXTURE11_ARB = 33995
GL_TEXTURE12 = 33996
GL_TEXTURE12_ARB = 33996
GL_TEXTURE13 = 33997
GL_TEXTURE13_ARB = 33997
GL_TEXTURE14 = 33998
GL_TEXTURE14_ARB = 33998
GL_TEXTURE15 = 33999
GL_TEXTURE15_ARB = 33999
GL_TEXTURE16 = 34000
GL_TEXTURE16_ARB = 34000
GL_TEXTURE17 = 34001
GL_TEXTURE17_ARB = 34001
GL_TEXTURE18 = 34002
GL_TEXTURE18_ARB = 34002
GL_TEXTURE19 = 34003
GL_TEXTURE19_ARB = 34003
GL_TEXTURE20 = 34004
GL_TEXTURE20_ARB = 34004
GL_TEXTURE21 = 34005
GL_TEXTURE21_ARB = 34005
GL_TEXTURE22 = 34006
GL_TEXTURE22_ARB = 34006
GL_TEXTURE23 = 34007
GL_TEXTURE23_ARB = 34007
GL_TEXTURE24 = 34008
GL_TEXTURE24_ARB = 34008
GL_TEXTURE25 = 34009
GL_TEXTURE25_ARB = 34009
GL_TEXTURE26 = 34010
GL_TEXTURE26_ARB = 34010
GL_TEXTURE27 = 34011
GL_TEXTURE27_ARB = 34011
GL_TEXTURE28 = 34012
GL_TEXTURE28_ARB = 34012
GL_TEXTURE29 = 34013
GL_TEXTURE29_ARB = 34013
GL_TEXTURE30 = 34014
GL_TEXTURE30_ARB = 34014
GL_TEXTURE31 = 34015
GL_TEXTURE31_ARB = 34015
GL_ACTIVE_TEXTURE = 34016
GL_ACTIVE_TEXTURE_ARB = 34016
GL_CLIENT_ACTIVE_TEXTURE = 34017
GL_CLIENT_ACTIVE_TEXTURE_ARB = 34017
GL_MAX_TEXTURE_UNITS = 34018
GL_MAX_TEXTURE_UNITS_ARB = 34018
GL_TRANSPOSE_MODELVIEW_MATRIX = 34019
GL_TRANSPOSE_MODELVIEW_MATRIX_ARB = 34019
GL_TRANSPOSE_PROJECTION_MATRIX = 34020
GL_TRANSPOSE_PROJECTION_MATRIX_ARB = 34020
GL_TRANSPOSE_TEXTURE_MATRIX = 34021
GL_TRANSPOSE_TEXTURE_MATRIX_ARB = 34021
GL_TRANSPOSE_COLOR_MATRIX = 34022
GL_TRANSPOSE_COLOR_MATRIX_ARB = 34022
GL_SUBTRACT = 34023
GL_SUBTRACT_ARB = 34023
GL_MAX_RENDERBUFFER_SIZE = 34024
GL_MAX_RENDERBUFFER_SIZE_EXT = 34024
GL_COMPRESSED_ALPHA = 34025
GL_COMPRESSED_ALPHA_ARB = 34025
GL_COMPRESSED_LUMINANCE = 34026
GL_COMPRESSED_LUMINANCE_ARB = 34026
GL_COMPRESSED_LUMINANCE_ALPHA = 34027
GL_COMPRESSED_LUMINANCE_ALPHA_ARB = 34027
GL_COMPRESSED_INTENSITY = 34028
GL_COMPRESSED_INTENSITY_ARB = 34028
GL_COMPRESSED_RGB = 34029
GL_COMPRESSED_RGB_ARB = 34029
GL_COMPRESSED_RGBA = 34030
GL_COMPRESSED_RGBA_ARB = 34030
GL_TEXTURE_COMPRESSION_HINT = 34031
GL_TEXTURE_COMPRESSION_HINT_ARB = 34031
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER = 34032
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER = 34033
GL_TEXTURE_RECTANGLE = 34037
GL_TEXTURE_RECTANGLE_ARB = 34037
GL_TEXTURE_BINDING_RECTANGLE = 34038
GL_TEXTURE_BINDING_RECTANGLE_ARB = 34038
GL_PROXY_TEXTURE_RECTANGLE = 34039
GL_PROXY_TEXTURE_RECTANGLE_ARB = 34039
GL_MAX_RECTANGLE_TEXTURE_SIZE = 34040
GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB = 34040
GL_DEPTH_STENCIL = 34041
GL_DEPTH_STENCIL_EXT = 34041
GL_UNSIGNED_INT_24_8 = 34042
GL_UNSIGNED_INT_24_8_EXT = 34042
GL_MAX_TEXTURE_LOD_BIAS = 34045
GL_MAX_TEXTURE_LOD_BIAS_EXT = 34045
GL_TEXTURE_MAX_ANISOTROPY = 34046
GL_TEXTURE_MAX_ANISOTROPY_EXT = 34046
GL_MAX_TEXTURE_MAX_ANISOTROPY = 34047
GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT = 34047
GL_TEXTURE_FILTER_CONTROL = 34048
GL_TEXTURE_FILTER_CONTROL_EXT = 34048
GL_TEXTURE_LOD_BIAS = 34049
GL_TEXTURE_LOD_BIAS_EXT = 34049
GL_MODELVIEW1_STACK_DEPTH_EXT = 34050
GL_MODELVIEW1_MATRIX_EXT = 34054
GL_INCR_WRAP = 34055
GL_INCR_WRAP_EXT = 34055
GL_DECR_WRAP = 34056
GL_DECR_WRAP_EXT = 34056
GL_VERTEX_WEIGHTING_EXT = 34057
GL_MODELVIEW1_ARB = 34058
GL_MODELVIEW1_EXT = 34058
GL_CURRENT_VERTEX_WEIGHT_EXT = 34059
GL_VERTEX_WEIGHT_ARRAY_EXT = 34060
GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT = 34061
GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT = 34062
GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT = 34063
GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT = 34064
GL_NORMAL_MAP = 34065
GL_NORMAL_MAP_ARB = 34065
GL_NORMAL_MAP_EXT = 34065
GL_REFLECTION_MAP = 34066
GL_REFLECTION_MAP_ARB = 34066
GL_REFLECTION_MAP_EXT = 34066
GL_TEXTURE_CUBE_MAP = 34067
GL_TEXTURE_CUBE_MAP_ARB = 34067
GL_TEXTURE_CUBE_MAP_EXT = 34067
GL_TEXTURE_BINDING_CUBE_MAP = 34068
GL_TEXTURE_BINDING_CUBE_MAP_ARB = 34068
GL_TEXTURE_BINDING_CUBE_MAP_EXT = 34068
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 34069
GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = 34069
GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT = 34069
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 34070
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = 34070
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT = 34070
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 34071
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = 34071
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT = 34071
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 34072
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = 34072
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT = 34072
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 34073
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = 34073
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT = 34073
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 34074
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = 34074
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT = 34074
GL_PROXY_TEXTURE_CUBE_MAP = 34075
GL_PROXY_TEXTURE_CUBE_MAP_ARB = 34075
GL_PROXY_TEXTURE_CUBE_MAP_EXT = 34075
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 34076
GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB = 34076
GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT = 34076
GL_RED_MIN_CLAMP_INGR = 34144
GL_GREEN_MIN_CLAMP_INGR = 34145
GL_BLUE_MIN_CLAMP_INGR = 34146
GL_ALPHA_MIN_CLAMP_INGR = 34147
GL_RED_MAX_CLAMP_INGR = 34148
GL_GREEN_MAX_CLAMP_INGR = 34149
GL_BLUE_MAX_CLAMP_INGR = 34150
GL_ALPHA_MAX_CLAMP_INGR = 34151
GL_INTERLACE_READ_INGR = 34152
GL_COMBINE = 34160
GL_COMBINE_ARB = 34160
GL_COMBINE_EXT = 34160
GL_COMBINE_RGB = 34161
GL_COMBINE_RGB_ARB = 34161
GL_COMBINE_RGB_EXT = 34161
GL_COMBINE_ALPHA = 34162
GL_COMBINE_ALPHA_ARB = 34162
GL_COMBINE_ALPHA_EXT = 34162
GL_RGB_SCALE = 34163
GL_RGB_SCALE_ARB = 34163
GL_RGB_SCALE_EXT = 34163
GL_ADD_SIGNED = 34164
GL_ADD_SIGNED_ARB = 34164
GL_ADD_SIGNED_EXT = 34164
GL_INTERPOLATE = 34165
GL_INTERPOLATE_ARB = 34165
GL_INTERPOLATE_EXT = 34165
GL_CONSTANT = 34166
GL_CONSTANT_ARB = 34166
GL_CONSTANT_EXT = 34166
GL_PRIMARY_COLOR = 34167
GL_PRIMARY_COLOR_ARB = 34167
GL_PRIMARY_COLOR_EXT = 34167
GL_PREVIOUS = 34168
GL_PREVIOUS_ARB = 34168
GL_PREVIOUS_EXT = 34168
GL_SOURCE0_RGB = 34176
GL_SOURCE0_RGB_ARB = 34176
GL_SOURCE0_RGB_EXT = 34176
GL_SRC0_RGB = 34176
GL_SOURCE1_RGB = 34177
GL_SOURCE1_RGB_ARB = 34177
GL_SOURCE1_RGB_EXT = 34177
GL_SRC1_RGB = 34177
GL_SOURCE2_RGB = 34178
GL_SOURCE2_RGB_ARB = 34178
GL_SOURCE2_RGB_EXT = 34178
GL_SRC2_RGB = 34178
GL_SOURCE0_ALPHA = 34184
GL_SOURCE0_ALPHA_ARB = 34184
GL_SOURCE0_ALPHA_EXT = 34184
GL_SRC0_ALPHA = 34184
GL_SOURCE1_ALPHA = 34185
GL_SOURCE1_ALPHA_ARB = 34185
GL_SOURCE1_ALPHA_EXT = 34185
GL_SRC1_ALPHA = 34185
GL_SRC1_ALPHA_EXT = 34185
GL_SOURCE2_ALPHA = 34186
GL_SOURCE2_ALPHA_ARB = 34186
GL_SOURCE2_ALPHA_EXT = 34186
GL_SRC2_ALPHA = 34186
GL_OPERAND0_RGB = 34192
GL_OPERAND0_RGB_ARB = 34192
GL_OPERAND0_RGB_EXT = 34192
GL_OPERAND1_RGB = 34193
GL_OPERAND1_RGB_ARB = 34193
GL_OPERAND1_RGB_EXT = 34193
GL_OPERAND2_RGB = 34194
GL_OPERAND2_RGB_ARB = 34194
GL_OPERAND2_RGB_EXT = 34194
GL_OPERAND0_ALPHA = 34200
GL_OPERAND0_ALPHA_ARB = 34200
GL_OPERAND0_ALPHA_EXT = 34200
GL_OPERAND1_ALPHA = 34201
GL_OPERAND1_ALPHA_ARB = 34201
GL_OPERAND1_ALPHA_EXT = 34201
GL_OPERAND2_ALPHA = 34202
GL_OPERAND2_ALPHA_ARB = 34202
GL_OPERAND2_ALPHA_EXT = 34202
GL_PERTURB_EXT = 34222
GL_TEXTURE_NORMAL_EXT = 34223
GL_VERTEX_ARRAY_BINDING = 34229
GL_VERTEX_PROGRAM_ARB = 34336
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 34338
GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB = 34338
GL_VERTEX_ATTRIB_ARRAY_SIZE = 34339
GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB = 34339
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 34340
GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB = 34340
GL_VERTEX_ATTRIB_ARRAY_TYPE = 34341
GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB = 34341
GL_CURRENT_VERTEX_ATTRIB = 34342
GL_CURRENT_VERTEX_ATTRIB_ARB = 34342
GL_PROGRAM_LENGTH_ARB = 34343
GL_PROGRAM_STRING_ARB = 34344
GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB = 34350
GL_MAX_PROGRAM_MATRICES_ARB = 34351
GL_CURRENT_MATRIX_STACK_DEPTH_ARB = 34368
GL_CURRENT_MATRIX_ARB = 34369
GL_VERTEX_PROGRAM_POINT_SIZE = 34370
GL_VERTEX_PROGRAM_POINT_SIZE_ARB = 34370
GL_PROGRAM_POINT_SIZE = 34370
GL_PROGRAM_POINT_SIZE_ARB = 34370
GL_PROGRAM_POINT_SIZE_EXT = 34370
GL_VERTEX_PROGRAM_TWO_SIDE = 34371
GL_VERTEX_PROGRAM_TWO_SIDE_ARB = 34371
GL_VERTEX_ATTRIB_ARRAY_POINTER = 34373
GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB = 34373
GL_PROGRAM_ERROR_POSITION_ARB = 34379
GL_DEPTH_CLAMP = 34383
GL_DEPTH_CLAMP_EXT = 34383
GL_PROGRAM_BINDING_ARB = 34423
GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 34464
GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB = 34464
GL_TEXTURE_COMPRESSED = 34465
GL_TEXTURE_COMPRESSED_ARB = 34465
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 34466
GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB = 34466
GL_COMPRESSED_TEXTURE_FORMATS = 34467
GL_COMPRESSED_TEXTURE_FORMATS_ARB = 34467
GL_MAX_VERTEX_UNITS_ARB = 34468
GL_ACTIVE_VERTEX_UNITS_ARB = 34469
GL_WEIGHT_SUM_UNITY_ARB = 34470
GL_VERTEX_BLEND_ARB = 34471
GL_CURRENT_WEIGHT_ARB = 34472
GL_WEIGHT_ARRAY_TYPE_ARB = 34473
GL_WEIGHT_ARRAY_STRIDE_ARB = 34474
GL_WEIGHT_ARRAY_SIZE_ARB = 34475
GL_WEIGHT_ARRAY_POINTER_ARB = 34476
GL_WEIGHT_ARRAY_ARB = 34477
GL_DOT3_RGB = 34478
GL_DOT3_RGB_ARB = 34478
GL_DOT3_RGBA = 34479
GL_DOT3_RGBA_ARB = 34479
GL_DOT3_RGBA_IMG = 34479
GL_COMPRESSED_RGB_FXT1_3DFX = 34480
GL_COMPRESSED_RGBA_FXT1_3DFX = 34481
GL_MULTISAMPLE_3DFX = 34482
GL_SAMPLE_BUFFERS_3DFX = 34483
GL_SAMPLES_3DFX = 34484
GL_MODELVIEW2_ARB = 34594
GL_MODELVIEW3_ARB = 34595
GL_MODELVIEW4_ARB = 34596
GL_MODELVIEW5_ARB = 34597
GL_MODELVIEW6_ARB = 34598
GL_MODELVIEW7_ARB = 34599
GL_MODELVIEW8_ARB = 34600
GL_MODELVIEW9_ARB = 34601
GL_MODELVIEW10_ARB = 34602
GL_MODELVIEW11_ARB = 34603
GL_MODELVIEW12_ARB = 34604
GL_MODELVIEW13_ARB = 34605
GL_MODELVIEW14_ARB = 34606
GL_MODELVIEW15_ARB = 34607
GL_MODELVIEW16_ARB = 34608
GL_MODELVIEW17_ARB = 34609
GL_MODELVIEW18_ARB = 34610
GL_MODELVIEW19_ARB = 34611
GL_MODELVIEW20_ARB = 34612
GL_MODELVIEW21_ARB = 34613
GL_MODELVIEW22_ARB = 34614
GL_MODELVIEW23_ARB = 34615
GL_MODELVIEW24_ARB = 34616
GL_MODELVIEW25_ARB = 34617
GL_MODELVIEW26_ARB = 34618
GL_MODELVIEW27_ARB = 34619
GL_MODELVIEW28_ARB = 34620
GL_MODELVIEW29_ARB = 34621
GL_MODELVIEW30_ARB = 34622
GL_MODELVIEW31_ARB = 34623
GL_DOT3_RGB_EXT = 34624
GL_DOT3_RGBA_EXT = 34625
GL_PROGRAM_BINARY_LENGTH = 34625
GL_MIRROR_CLAMP_EXT = 34626
GL_MIRROR_CLAMP_TO_EDGE = 34627
GL_MIRROR_CLAMP_TO_EDGE_EXT = 34627
GL_VERTEX_ATTRIB_ARRAY_LONG = 34638
GL_TEXTURE_1D_STACK_MESAX = 34649
GL_TEXTURE_2D_STACK_MESAX = 34650
GL_PROXY_TEXTURE_1D_STACK_MESAX = 34651
GL_PROXY_TEXTURE_2D_STACK_MESAX = 34652
GL_TEXTURE_1D_STACK_BINDING_MESAX = 34653
GL_TEXTURE_2D_STACK_BINDING_MESAX = 34654
GL_BUFFER_SIZE = 34660
GL_BUFFER_SIZE_ARB = 34660
GL_BUFFER_USAGE = 34661
GL_BUFFER_USAGE_ARB = 34661
GL_VERTEX_SHADER_EXT = 34688
GL_VERTEX_SHADER_BINDING_EXT = 34689
GL_OP_INDEX_EXT = 34690
GL_OP_NEGATE_EXT = 34691
GL_OP_DOT3_EXT = 34692
GL_OP_DOT4_EXT = 34693
GL_OP_MUL_EXT = 34694
GL_OP_ADD_EXT = 34695
GL_OP_MADD_EXT = 34696
GL_OP_FRAC_EXT = 34697
GL_OP_MAX_EXT = 34698
GL_OP_MIN_EXT = 34699
GL_OP_SET_GE_EXT = 34700
GL_OP_SET_LT_EXT = 34701
GL_OP_CLAMP_EXT = 34702
GL_OP_FLOOR_EXT = 34703
GL_OP_ROUND_EXT = 34704
GL_OP_EXP_BASE_2_EXT = 34705
GL_OP_LOG_BASE_2_EXT = 34706
GL_OP_POWER_EXT = 34707
GL_OP_RECIP_EXT = 34708
GL_OP_RECIP_SQRT_EXT = 34709
GL_OP_SUB_EXT = 34710
GL_OP_CROSS_PRODUCT_EXT = 34711
GL_OP_MULTIPLY_MATRIX_EXT = 34712
GL_OP_MOV_EXT = 34713
GL_OUTPUT_VERTEX_EXT = 34714
GL_OUTPUT_COLOR0_EXT = 34715
GL_OUTPUT_COLOR1_EXT = 34716
GL_OUTPUT_TEXTURE_COORD0_EXT = 34717
GL_OUTPUT_TEXTURE_COORD1_EXT = 34718
GL_OUTPUT_TEXTURE_COORD2_EXT = 34719
GL_OUTPUT_TEXTURE_COORD3_EXT = 34720
GL_OUTPUT_TEXTURE_COORD4_EXT = 34721
GL_OUTPUT_TEXTURE_COORD5_EXT = 34722
GL_OUTPUT_TEXTURE_COORD6_EXT = 34723
GL_OUTPUT_TEXTURE_COORD7_EXT = 34724
GL_OUTPUT_TEXTURE_COORD8_EXT = 34725
GL_OUTPUT_TEXTURE_COORD9_EXT = 34726
GL_OUTPUT_TEXTURE_COORD10_EXT = 34727
GL_OUTPUT_TEXTURE_COORD11_EXT = 34728
GL_OUTPUT_TEXTURE_COORD12_EXT = 34729
GL_OUTPUT_TEXTURE_COORD13_EXT = 34730
GL_OUTPUT_TEXTURE_COORD14_EXT = 34731
GL_OUTPUT_TEXTURE_COORD15_EXT = 34732
GL_OUTPUT_TEXTURE_COORD16_EXT = 34733
GL_OUTPUT_TEXTURE_COORD17_EXT = 34734
GL_OUTPUT_TEXTURE_COORD18_EXT = 34735
GL_OUTPUT_TEXTURE_COORD19_EXT = 34736
GL_OUTPUT_TEXTURE_COORD20_EXT = 34737
GL_OUTPUT_TEXTURE_COORD21_EXT = 34738
GL_OUTPUT_TEXTURE_COORD22_EXT = 34739
GL_OUTPUT_TEXTURE_COORD23_EXT = 34740
GL_OUTPUT_TEXTURE_COORD24_EXT = 34741
GL_OUTPUT_TEXTURE_COORD25_EXT = 34742
GL_OUTPUT_TEXTURE_COORD26_EXT = 34743
GL_OUTPUT_TEXTURE_COORD27_EXT = 34744
GL_OUTPUT_TEXTURE_COORD28_EXT = 34745
GL_OUTPUT_TEXTURE_COORD29_EXT = 34746
GL_OUTPUT_TEXTURE_COORD30_EXT = 34747
GL_OUTPUT_TEXTURE_COORD31_EXT = 34748
GL_OUTPUT_FOG_EXT = 34749
GL_SCALAR_EXT = 34750
GL_VECTOR_EXT = 34751
GL_MATRIX_EXT = 34752
GL_VARIANT_EXT = 34753
GL_INVARIANT_EXT = 34754
GL_LOCAL_CONSTANT_EXT = 34755
GL_LOCAL_EXT = 34756
GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = 34757
GL_MAX_VERTEX_SHADER_VARIANTS_EXT = 34758
GL_MAX_VERTEX_SHADER_INVARIANTS_EXT = 34759
GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34760
GL_MAX_VERTEX_SHADER_LOCALS_EXT = 34761
GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = 34762
GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = 34763
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34764
GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT = 34765
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = 34766
GL_VERTEX_SHADER_INSTRUCTIONS_EXT = 34767
GL_VERTEX_SHADER_VARIANTS_EXT = 34768
GL_VERTEX_SHADER_INVARIANTS_EXT = 34769
GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 34770
GL_VERTEX_SHADER_LOCALS_EXT = 34771
GL_VERTEX_SHADER_OPTIMIZED_EXT = 34772
GL_X_EXT = 34773
GL_Y_EXT = 34774
GL_Z_EXT = 34775
GL_W_EXT = 34776
GL_NEGATIVE_X_EXT = 34777
GL_NEGATIVE_Y_EXT = 34778
GL_NEGATIVE_Z_EXT = 34779
GL_NEGATIVE_W_EXT = 34780
GL_ZERO_EXT = 34781
GL_ONE_EXT = 34782
GL_NEGATIVE_ONE_EXT = 34783
GL_NORMALIZED_RANGE_EXT = 34784
GL_FULL_RANGE_EXT = 34785
GL_CURRENT_VERTEX_EXT = 34786
GL_MVP_MATRIX_EXT = 34787
GL_VARIANT_VALUE_EXT = 34788
GL_VARIANT_DATATYPE_EXT = 34789
GL_VARIANT_ARRAY_STRIDE_EXT = 34790
GL_VARIANT_ARRAY_TYPE_EXT = 34791
GL_VARIANT_ARRAY_EXT = 34792
GL_VARIANT_ARRAY_POINTER_EXT = 34793
GL_INVARIANT_VALUE_EXT = 34794
GL_INVARIANT_DATATYPE_EXT = 34795
GL_LOCAL_CONSTANT_VALUE_EXT = 34796
GL_LOCAL_CONSTANT_DATATYPE_EXT = 34797
GL_NUM_PROGRAM_BINARY_FORMATS = 34814
GL_PROGRAM_BINARY_FORMATS = 34815
GL_STENCIL_BACK_FUNC = 34816
GL_STENCIL_BACK_FAIL = 34817
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 34818
GL_STENCIL_BACK_PASS_DEPTH_PASS = 34819
GL_FRAGMENT_PROGRAM_ARB = 34820
GL_PROGRAM_ALU_INSTRUCTIONS_ARB = 34821
GL_PROGRAM_TEX_INSTRUCTIONS_ARB = 34822
GL_PROGRAM_TEX_INDIRECTIONS_ARB = 34823
GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 34824
GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 34825
GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 34826
GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB = 34827
GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB = 34828
GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB = 34829
GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 34830
GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 34831
GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 34832
GL_RGBA32F = 34836
GL_RGBA32F_ARB = 34836
GL_RGBA32F_EXT = 34836
GL_RGB32F = 34837
GL_RGB32F_ARB = 34837
GL_RGB32F_EXT = 34837
GL_ALPHA32F_ARB = 34838
GL_ALPHA32F_EXT = 34838
GL_INTENSITY32F_ARB = 34839
GL_LUMINANCE32F_ARB = 34840
GL_LUMINANCE32F_EXT = 34840
GL_LUMINANCE_ALPHA32F_ARB = 34841
GL_LUMINANCE_ALPHA32F_EXT = 34841
GL_RGBA16F = 34842
GL_RGBA16F_ARB = 34842
GL_RGBA16F_EXT = 34842
GL_RGB16F = 34843
GL_RGB16F_ARB = 34843
GL_RGB16F_EXT = 34843
GL_ALPHA16F_ARB = 34844
GL_ALPHA16F_EXT = 34844
GL_INTENSITY16F_ARB = 34845
GL_LUMINANCE16F_ARB = 34846
GL_LUMINANCE16F_EXT = 34846
GL_LUMINANCE_ALPHA16F_ARB = 34847
GL_LUMINANCE_ALPHA16F_EXT = 34847
GL_RGBA_FLOAT_MODE_ARB = 34848
GL_MAX_DRAW_BUFFERS = 34852
GL_MAX_DRAW_BUFFERS_ARB = 34852
GL_MAX_DRAW_BUFFERS_EXT = 34852
GL_DRAW_BUFFER0 = 34853
GL_DRAW_BUFFER0_ARB = 34853
GL_DRAW_BUFFER0_EXT = 34853
GL_DRAW_BUFFER1 = 34854
GL_DRAW_BUFFER1_ARB = 34854
GL_DRAW_BUFFER1_EXT = 34854
GL_DRAW_BUFFER2 = 34855
GL_DRAW_BUFFER2_ARB = 34855
GL_DRAW_BUFFER2_EXT = 34855
GL_DRAW_BUFFER3 = 34856
GL_DRAW_BUFFER3_ARB = 34856
GL_DRAW_BUFFER3_EXT = 34856
GL_DRAW_BUFFER4 = 34857
GL_DRAW_BUFFER4_ARB = 34857
GL_DRAW_BUFFER4_EXT = 34857
GL_DRAW_BUFFER5 = 34858
GL_DRAW_BUFFER5_ARB = 34858
GL_DRAW_BUFFER5_EXT = 34858
GL_DRAW_BUFFER6 = 34859
GL_DRAW_BUFFER6_ARB = 34859
GL_DRAW_BUFFER6_EXT = 34859
GL_DRAW_BUFFER7 = 34860
GL_DRAW_BUFFER7_ARB = 34860
GL_DRAW_BUFFER7_EXT = 34860
GL_DRAW_BUFFER8 = 34861
GL_DRAW_BUFFER8_ARB = 34861
GL_DRAW_BUFFER8_EXT = 34861
GL_DRAW_BUFFER9 = 34862
GL_DRAW_BUFFER9_ARB = 34862
GL_DRAW_BUFFER9_EXT = 34862
GL_DRAW_BUFFER10 = 34863
GL_DRAW_BUFFER10_ARB = 34863
GL_DRAW_BUFFER10_EXT = 34863
GL_DRAW_BUFFER11 = 34864
GL_DRAW_BUFFER11_ARB = 34864
GL_DRAW_BUFFER11_EXT = 34864
GL_DRAW_BUFFER12 = 34865
GL_DRAW_BUFFER12_ARB = 34865
GL_DRAW_BUFFER12_EXT = 34865
GL_DRAW_BUFFER13 = 34866
GL_DRAW_BUFFER13_ARB = 34866
GL_DRAW_BUFFER13_EXT = 34866
GL_DRAW_BUFFER14 = 34867
GL_DRAW_BUFFER14_ARB = 34867
GL_DRAW_BUFFER14_EXT = 34867
GL_DRAW_BUFFER15 = 34868
GL_DRAW_BUFFER15_ARB = 34868
GL_DRAW_BUFFER15_EXT = 34868
GL_BLEND_EQUATION_ALPHA = 34877
GL_BLEND_EQUATION_ALPHA_EXT = 34877
GL_MATRIX_PALETTE_ARB = 34880
GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB = 34881
GL_MAX_PALETTE_MATRICES_ARB = 34882
GL_CURRENT_PALETTE_MATRIX_ARB = 34883
GL_MATRIX_INDEX_ARRAY_ARB = 34884
GL_CURRENT_MATRIX_INDEX_ARB = 34885
GL_MATRIX_INDEX_ARRAY_SIZE_ARB = 34886
GL_MATRIX_INDEX_ARRAY_TYPE_ARB = 34887
GL_MATRIX_INDEX_ARRAY_STRIDE_ARB = 34888
GL_MATRIX_INDEX_ARRAY_POINTER_ARB = 34889
GL_TEXTURE_DEPTH_SIZE = 34890
GL_TEXTURE_DEPTH_SIZE_ARB = 34890
GL_DEPTH_TEXTURE_MODE = 34891
GL_DEPTH_TEXTURE_MODE_ARB = 34891
GL_TEXTURE_COMPARE_MODE = 34892
GL_TEXTURE_COMPARE_MODE_ARB = 34892
GL_TEXTURE_COMPARE_MODE_EXT = 34892
GL_TEXTURE_COMPARE_FUNC = 34893
GL_TEXTURE_COMPARE_FUNC_ARB = 34893
GL_TEXTURE_COMPARE_FUNC_EXT = 34893
GL_COMPARE_R_TO_TEXTURE = 34894
GL_COMPARE_R_TO_TEXTURE_ARB = 34894
GL_COMPARE_REF_DEPTH_TO_TEXTURE_EXT = 34894
GL_COMPARE_REF_TO_TEXTURE = 34894
GL_COMPARE_REF_TO_TEXTURE_EXT = 34894
GL_TEXTURE_CUBE_MAP_SEAMLESS = 34895
GL_POINT_SPRITE = 34913
GL_POINT_SPRITE_ARB = 34913
GL_COORD_REPLACE = 34914
GL_COORD_REPLACE_ARB = 34914
GL_QUERY_COUNTER_BITS = 34916
GL_QUERY_COUNTER_BITS_ARB = 34916
GL_QUERY_COUNTER_BITS_EXT = 34916
GL_CURRENT_QUERY = 34917
GL_CURRENT_QUERY_ARB = 34917
GL_CURRENT_QUERY_EXT = 34917
GL_QUERY_RESULT = 34918
GL_QUERY_RESULT_ARB = 34918
GL_QUERY_RESULT_EXT = 34918
GL_QUERY_RESULT_AVAILABLE = 34919
GL_QUERY_RESULT_AVAILABLE_ARB = 34919
GL_QUERY_RESULT_AVAILABLE_EXT = 34919
GL_MAX_VERTEX_ATTRIBS = 34921
GL_MAX_VERTEX_ATTRIBS_ARB = 34921
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 34922
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB = 34922
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS = 34924
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS_EXT = 34924
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS = 34925
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS_EXT = 34925
GL_MAX_TEXTURE_COORDS = 34929
GL_MAX_TEXTURE_COORDS_ARB = 34929
GL_MAX_TEXTURE_IMAGE_UNITS = 34930
GL_MAX_TEXTURE_IMAGE_UNITS_ARB = 34930
GL_PROGRAM_ERROR_STRING_ARB = 34932
GL_PROGRAM_FORMAT_ASCII_ARB = 34933
GL_PROGRAM_FORMAT_ARB = 34934
GL_GEOMETRY_SHADER_INVOCATIONS = 34943
GL_GEOMETRY_SHADER_INVOCATIONS_EXT = 34943
GL_DEPTH_BOUNDS_TEST_EXT = 34960
GL_DEPTH_BOUNDS_EXT = 34961
GL_ARRAY_BUFFER = 34962
GL_ARRAY_BUFFER_ARB = 34962
GL_ELEMENT_ARRAY_BUFFER = 34963
GL_ELEMENT_ARRAY_BUFFER_ARB = 34963
GL_ARRAY_BUFFER_BINDING = 34964
GL_ARRAY_BUFFER_BINDING_ARB = 34964
GL_ELEMENT_ARRAY_BUFFER_BINDING = 34965
GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = 34965
GL_VERTEX_ARRAY_BUFFER_BINDING = 34966
GL_VERTEX_ARRAY_BUFFER_BINDING_ARB = 34966
GL_NORMAL_ARRAY_BUFFER_BINDING = 34967
GL_NORMAL_ARRAY_BUFFER_BINDING_ARB = 34967
GL_COLOR_ARRAY_BUFFER_BINDING = 34968
GL_COLOR_ARRAY_BUFFER_BINDING_ARB = 34968
GL_INDEX_ARRAY_BUFFER_BINDING = 34969
GL_INDEX_ARRAY_BUFFER_BINDING_ARB = 34969
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 34970
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = 34970
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 34971
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = 34971
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 34972
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = 34972
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = 34973
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 34973
GL_FOG_COORD_ARRAY_BUFFER_BINDING = 34973
GL_WEIGHT_ARRAY_BUFFER_BINDING = 34974
GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = 34974
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 34975
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB = 34975
GL_PROGRAM_INSTRUCTIONS_ARB = 34976
GL_MAX_PROGRAM_INSTRUCTIONS_ARB = 34977
GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB = 34978
GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB = 34979
GL_PROGRAM_TEMPORARIES_ARB = 34980
GL_MAX_PROGRAM_TEMPORARIES_ARB = 34981
GL_PROGRAM_NATIVE_TEMPORARIES_ARB = 34982
GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB = 34983
GL_PROGRAM_PARAMETERS_ARB = 34984
GL_MAX_PROGRAM_PARAMETERS_ARB = 34985
GL_PROGRAM_NATIVE_PARAMETERS_ARB = 34986
GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB = 34987
GL_PROGRAM_ATTRIBS_ARB = 34988
GL_MAX_PROGRAM_ATTRIBS_ARB = 34989
GL_PROGRAM_NATIVE_ATTRIBS_ARB = 34990
GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB = 34991
GL_PROGRAM_ADDRESS_REGISTERS_ARB = 34992
GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB = 34993
GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = 34994
GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = 34995
GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB = 34996
GL_MAX_PROGRAM_ENV_PARAMETERS_ARB = 34997
GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB = 34998
GL_TRANSPOSE_CURRENT_MATRIX_ARB = 34999
GL_READ_ONLY = 35000
GL_READ_ONLY_ARB = 35000
GL_WRITE_ONLY = 35001
GL_WRITE_ONLY_ARB = 35001
GL_READ_WRITE = 35002
GL_READ_WRITE_ARB = 35002
GL_BUFFER_ACCESS = 35003
GL_BUFFER_ACCESS_ARB = 35003
GL_BUFFER_MAPPED = 35004
GL_BUFFER_MAPPED_ARB = 35004
GL_BUFFER_MAP_POINTER = 35005
GL_BUFFER_MAP_POINTER_ARB = 35005
GL_TIME_ELAPSED = 35007
GL_TIME_ELAPSED_EXT = 35007
GL_MATRIX0_ARB = 35008
GL_MATRIX1_ARB = 35009
GL_MATRIX2_ARB = 35010
GL_MATRIX3_ARB = 35011
GL_MATRIX4_ARB = 35012
GL_MATRIX5_ARB = 35013
GL_MATRIX6_ARB = 35014
GL_MATRIX7_ARB = 35015
GL_MATRIX8_ARB = 35016
GL_MATRIX9_ARB = 35017
GL_MATRIX10_ARB = 35018
GL_MATRIX11_ARB = 35019
GL_MATRIX12_ARB = 35020
GL_MATRIX13_ARB = 35021
GL_MATRIX14_ARB = 35022
GL_MATRIX15_ARB = 35023
GL_MATRIX16_ARB = 35024
GL_MATRIX17_ARB = 35025
GL_MATRIX18_ARB = 35026
GL_MATRIX19_ARB = 35027
GL_MATRIX20_ARB = 35028
GL_MATRIX21_ARB = 35029
GL_MATRIX22_ARB = 35030
GL_MATRIX23_ARB = 35031
GL_MATRIX24_ARB = 35032
GL_MATRIX25_ARB = 35033
GL_MATRIX26_ARB = 35034
GL_MATRIX27_ARB = 35035
GL_MATRIX28_ARB = 35036
GL_MATRIX29_ARB = 35037
GL_MATRIX30_ARB = 35038
GL_MATRIX31_ARB = 35039
GL_STREAM_DRAW = 35040
GL_STREAM_DRAW_ARB = 35040
GL_STREAM_READ = 35041
GL_STREAM_READ_ARB = 35041
GL_STREAM_COPY = 35042
GL_STREAM_COPY_ARB = 35042
GL_STATIC_DRAW = 35044
GL_STATIC_DRAW_ARB = 35044
GL_STATIC_READ = 35045
GL_STATIC_READ_ARB = 35045
GL_STATIC_COPY = 35046
GL_STATIC_COPY_ARB = 35046
GL_DYNAMIC_DRAW = 35048
GL_DYNAMIC_DRAW_ARB = 35048
GL_DYNAMIC_READ = 35049
GL_DYNAMIC_READ_ARB = 35049
GL_DYNAMIC_COPY = 35050
GL_DYNAMIC_COPY_ARB = 35050
GL_PIXEL_PACK_BUFFER = 35051
GL_PIXEL_PACK_BUFFER_ARB = 35051
GL_PIXEL_PACK_BUFFER_EXT = 35051
GL_PIXEL_UNPACK_BUFFER = 35052
GL_PIXEL_UNPACK_BUFFER_ARB = 35052
GL_PIXEL_UNPACK_BUFFER_EXT = 35052
GL_PIXEL_PACK_BUFFER_BINDING = 35053
GL_PIXEL_PACK_BUFFER_BINDING_ARB = 35053
GL_PIXEL_PACK_BUFFER_BINDING_EXT = 35053
GL_PIXEL_UNPACK_BUFFER_BINDING = 35055
GL_PIXEL_UNPACK_BUFFER_BINDING_ARB = 35055
GL_PIXEL_UNPACK_BUFFER_BINDING_EXT = 35055
GL_DEPTH24_STENCIL8 = 35056
GL_DEPTH24_STENCIL8_EXT = 35056
GL_TEXTURE_STENCIL_SIZE = 35057
GL_TEXTURE_STENCIL_SIZE_EXT = 35057
GL_STENCIL_TAG_BITS_EXT = 35058
GL_STENCIL_CLEAR_TAG_VALUE_EXT = 35059
GL_SRC1_COLOR = 35065
GL_SRC1_COLOR_EXT = 35065
GL_ONE_MINUS_SRC1_COLOR = 35066
GL_ONE_MINUS_SRC1_COLOR_EXT = 35066
GL_ONE_MINUS_SRC1_ALPHA = 35067
GL_ONE_MINUS_SRC1_ALPHA_EXT = 35067
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 35068
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS_EXT = 35068
GL_VERTEX_ATTRIB_ARRAY_INTEGER = 35069
GL_VERTEX_ATTRIB_ARRAY_INTEGER_EXT = 35069
GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 35070
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE = 35070
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB = 35070
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_EXT = 35070
GL_MAX_ARRAY_TEXTURE_LAYERS = 35071
GL_MAX_ARRAY_TEXTURE_LAYERS_EXT = 35071
GL_MIN_PROGRAM_TEXEL_OFFSET = 35076
GL_MIN_PROGRAM_TEXEL_OFFSET_EXT = 35076
GL_MAX_PROGRAM_TEXEL_OFFSET = 35077
GL_MAX_PROGRAM_TEXEL_OFFSET_EXT = 35077
GL_STENCIL_TEST_TWO_SIDE_EXT = 35088
GL_ACTIVE_STENCIL_FACE_EXT = 35089
GL_MIRROR_CLAMP_TO_BORDER_EXT = 35090
GL_SAMPLES_PASSED = 35092
GL_SAMPLES_PASSED_ARB = 35092
GL_GEOMETRY_VERTICES_OUT = 35094
GL_GEOMETRY_LINKED_VERTICES_OUT_EXT = 35094
GL_GEOMETRY_INPUT_TYPE = 35095
GL_GEOMETRY_LINKED_INPUT_TYPE_EXT = 35095
GL_GEOMETRY_OUTPUT_TYPE = 35096
GL_GEOMETRY_LINKED_OUTPUT_TYPE_EXT = 35096
GL_SAMPLER_BINDING = 35097
GL_CLAMP_VERTEX_COLOR = 35098
GL_CLAMP_VERTEX_COLOR_ARB = 35098
GL_CLAMP_FRAGMENT_COLOR = 35099
GL_CLAMP_FRAGMENT_COLOR_ARB = 35099
GL_CLAMP_READ_COLOR = 35100
GL_CLAMP_READ_COLOR_ARB = 35100
GL_FIXED_ONLY = 35101
GL_FIXED_ONLY_ARB = 35101
GL_INTERLACE_OML = 35200
GL_INTERLACE_READ_OML = 35201
GL_FORMAT_SUBSAMPLE_24_24_OML = 35202
GL_FORMAT_SUBSAMPLE_244_244_OML = 35203
GL_PACK_RESAMPLE_OML = 35204
GL_UNPACK_RESAMPLE_OML = 35205
GL_RESAMPLE_REPLICATE_OML = 35206
GL_RESAMPLE_ZERO_FILL_OML = 35207
GL_RESAMPLE_AVERAGE_OML = 35208
GL_RESAMPLE_DECIMATE_OML = 35209
GL_UNIFORM_BUFFER = 35345
GL_UNIFORM_BUFFER_BINDING = 35368
GL_UNIFORM_BUFFER_START = 35369
GL_UNIFORM_BUFFER_SIZE = 35370
GL_MAX_VERTEX_UNIFORM_BLOCKS = 35371
GL_MAX_GEOMETRY_UNIFORM_BLOCKS = 35372
GL_MAX_GEOMETRY_UNIFORM_BLOCKS_EXT = 35372
GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 35373
GL_MAX_COMBINED_UNIFORM_BLOCKS = 35374
GL_MAX_UNIFORM_BUFFER_BINDINGS = 35375
GL_MAX_UNIFORM_BLOCK_SIZE = 35376
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 35377
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 35378
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS_EXT = 35378
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 35379
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 35380
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 35381
GL_ACTIVE_UNIFORM_BLOCKS = 35382
GL_UNIFORM_TYPE = 35383
GL_UNIFORM_SIZE = 35384
GL_UNIFORM_NAME_LENGTH = 35385
GL_UNIFORM_BLOCK_INDEX = 35386
GL_UNIFORM_OFFSET = 35387
GL_UNIFORM_ARRAY_STRIDE = 35388
GL_UNIFORM_MATRIX_STRIDE = 35389
GL_UNIFORM_IS_ROW_MAJOR = 35390
GL_UNIFORM_BLOCK_BINDING = 35391
GL_UNIFORM_BLOCK_DATA_SIZE = 35392
GL_UNIFORM_BLOCK_NAME_LENGTH = 35393
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 35394
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 35395
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 35396
GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 35397
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 35398
GL_TEXTURE_SRGB_DECODE_EXT = 35400
GL_DECODE_EXT = 35401
GL_SKIP_DECODE_EXT = 35402
GL_PROGRAM_PIPELINE_OBJECT_EXT = 35407
GL_FRAGMENT_SHADER_DISCARDS_SAMPLES_EXT = 35410
GL_COMPRESSED_SRGB_PVRTC_2BPPV1_EXT = 35412
GL_COMPRESSED_SRGB_PVRTC_4BPPV1_EXT = 35413
GL_COMPRESSED_SRGB_ALPHA_PVRTC_2BPPV1_EXT = 35414
GL_COMPRESSED_SRGB_ALPHA_PVRTC_4BPPV1_EXT = 35415
GL_FRAGMENT_SHADER = 35632
GL_FRAGMENT_SHADER_ARB = 35632
GL_VERTEX_SHADER = 35633
GL_VERTEX_SHADER_ARB = 35633
GL_PROGRAM_OBJECT_ARB = 35648
GL_PROGRAM_OBJECT_EXT = 35648
GL_SHADER_OBJECT_ARB = 35656
GL_SHADER_OBJECT_EXT = 35656
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 35657
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB = 35657
GL_MAX_VERTEX_UNIFORM_COMPONENTS = 35658
GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB = 35658
GL_MAX_VARYING_FLOATS = 35659
GL_MAX_VARYING_COMPONENTS = 35659
GL_MAX_VARYING_COMPONENTS_EXT = 35659
GL_MAX_VARYING_FLOATS_ARB = 35659
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 35660
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB = 35660
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 35661
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB = 35661
GL_OBJECT_TYPE_ARB = 35662
GL_SHADER_TYPE = 35663
GL_OBJECT_SUBTYPE_ARB = 35663
GL_FLOAT_VEC2 = 35664
GL_FLOAT_VEC2_ARB = 35664
GL_FLOAT_VEC3 = 35665
GL_FLOAT_VEC3_ARB = 35665
GL_FLOAT_VEC4 = 35666
GL_FLOAT_VEC4_ARB = 35666
GL_INT_VEC2 = 35667
GL_INT_VEC2_ARB = 35667
GL_INT_VEC3 = 35668
GL_INT_VEC3_ARB = 35668
GL_INT_VEC4 = 35669
GL_INT_VEC4_ARB = 35669
GL_BOOL = 35670
GL_BOOL_ARB = 35670
GL_BOOL_VEC2 = 35671
GL_BOOL_VEC2_ARB = 35671
GL_BOOL_VEC3 = 35672
GL_BOOL_VEC3_ARB = 35672
GL_BOOL_VEC4 = 35673
GL_BOOL_VEC4_ARB = 35673
GL_FLOAT_MAT2 = 35674
GL_FLOAT_MAT2_ARB = 35674
GL_FLOAT_MAT3 = 35675
GL_FLOAT_MAT3_ARB = 35675
GL_FLOAT_MAT4 = 35676
GL_FLOAT_MAT4_ARB = 35676
GL_SAMPLER_1D = 35677
GL_SAMPLER_1D_ARB = 35677
GL_SAMPLER_2D = 35678
GL_SAMPLER_2D_ARB = 35678
GL_SAMPLER_3D = 35679
GL_SAMPLER_3D_ARB = 35679
GL_SAMPLER_CUBE = 35680
GL_SAMPLER_CUBE_ARB = 35680
GL_SAMPLER_1D_SHADOW = 35681
GL_SAMPLER_1D_SHADOW_ARB = 35681
GL_SAMPLER_2D_SHADOW = 35682
GL_SAMPLER_2D_SHADOW_ARB = 35682
GL_SAMPLER_2D_SHADOW_EXT = 35682
GL_SAMPLER_2D_RECT = 35683
GL_SAMPLER_2D_RECT_ARB = 35683
GL_SAMPLER_2D_RECT_SHADOW = 35684
GL_SAMPLER_2D_RECT_SHADOW_ARB = 35684
GL_FLOAT_MAT2x3 = 35685
GL_FLOAT_MAT2x4 = 35686
GL_FLOAT_MAT3x2 = 35687
GL_FLOAT_MAT3x4 = 35688
GL_FLOAT_MAT4x2 = 35689
GL_FLOAT_MAT4x3 = 35690
GL_DELETE_STATUS = 35712
GL_OBJECT_DELETE_STATUS_ARB = 35712
GL_COMPILE_STATUS = 35713
GL_OBJECT_COMPILE_STATUS_ARB = 35713
GL_LINK_STATUS = 35714
GL_OBJECT_LINK_STATUS_ARB = 35714
GL_VALIDATE_STATUS = 35715
GL_OBJECT_VALIDATE_STATUS_ARB = 35715
GL_INFO_LOG_LENGTH = 35716
GL_OBJECT_INFO_LOG_LENGTH_ARB = 35716
GL_ATTACHED_SHADERS = 35717
GL_OBJECT_ATTACHED_OBJECTS_ARB = 35717
GL_ACTIVE_UNIFORMS = 35718
GL_OBJECT_ACTIVE_UNIFORMS_ARB = 35718
GL_ACTIVE_UNIFORM_MAX_LENGTH = 35719
GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = 35719
GL_SHADER_SOURCE_LENGTH = 35720
GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = 35720
GL_ACTIVE_ATTRIBUTES = 35721
GL_OBJECT_ACTIVE_ATTRIBUTES_ARB = 35721
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 35722
GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB = 35722
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 35723
GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB = 35723
GL_SHADING_LANGUAGE_VERSION = 35724
GL_SHADING_LANGUAGE_VERSION_ARB = 35724
GL_CURRENT_PROGRAM = 35725
GL_IMPLEMENTATION_COLOR_READ_TYPE = 35738
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 35739
GL_STATE_RESTORE = 35804
GL_SAMPLER_EXTERNAL_2D_Y2Y_EXT = 35815
GL_TEXTURE_PROTECTED_EXT = 35834
GL_COMPRESSED_RGB_PVRTC_4BPPV1_IMG = 35840
GL_COMPRESSED_RGB_PVRTC_2BPPV1_IMG = 35841
GL_COMPRESSED_RGBA_PVRTC_4BPPV1_IMG = 35842
GL_COMPRESSED_RGBA_PVRTC_2BPPV1_IMG = 35843
GL_MODULATE_COLOR_IMG = 35844
GL_RECIP_ADD_SIGNED_ALPHA_IMG = 35845
GL_TEXTURE_ALPHA_MODULATE_IMG = 35846
GL_FACTOR_ALPHA_MODULATE_IMG = 35847
GL_FRAGMENT_ALPHA_MODULATE_IMG = 35848
GL_ADD_BLEND_IMG = 35849
GL_SGX_BINARY_IMG = 35850
GL_TEXTURE_RED_TYPE = 35856
GL_TEXTURE_RED_TYPE_ARB = 35856
GL_TEXTURE_GREEN_TYPE = 35857
GL_TEXTURE_GREEN_TYPE_ARB = 35857
GL_TEXTURE_BLUE_TYPE = 35858
GL_TEXTURE_BLUE_TYPE_ARB = 35858
GL_TEXTURE_ALPHA_TYPE = 35859
GL_TEXTURE_ALPHA_TYPE_ARB = 35859
GL_TEXTURE_LUMINANCE_TYPE = 35860
GL_TEXTURE_LUMINANCE_TYPE_ARB = 35860
GL_TEXTURE_INTENSITY_TYPE = 35861
GL_TEXTURE_INTENSITY_TYPE_ARB = 35861
GL_TEXTURE_DEPTH_TYPE = 35862
GL_TEXTURE_DEPTH_TYPE_ARB = 35862
GL_UNSIGNED_NORMALIZED = 35863
GL_UNSIGNED_NORMALIZED_ARB = 35863
GL_UNSIGNED_NORMALIZED_EXT = 35863
GL_TEXTURE_1D_ARRAY = 35864
GL_TEXTURE_1D_ARRAY_EXT = 35864
GL_PROXY_TEXTURE_1D_ARRAY = 35865
GL_PROXY_TEXTURE_1D_ARRAY_EXT = 35865
GL_TEXTURE_2D_ARRAY = 35866
GL_TEXTURE_2D_ARRAY_EXT = 35866
GL_PROXY_TEXTURE_2D_ARRAY = 35867
GL_PROXY_TEXTURE_2D_ARRAY_EXT = 35867
GL_TEXTURE_BINDING_1D_ARRAY = 35868
GL_TEXTURE_BINDING_1D_ARRAY_EXT = 35868
GL_TEXTURE_BINDING_2D_ARRAY = 35869
GL_TEXTURE_BINDING_2D_ARRAY_EXT = 35869
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 35881
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB = 35881
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT = 35881
GL_TEXTURE_BUFFER = 35882
GL_TEXTURE_BUFFER_ARB = 35882
GL_TEXTURE_BUFFER_EXT = 35882
GL_TEXTURE_BUFFER_BINDING = 35882
GL_TEXTURE_BUFFER_BINDING_EXT = 35882
GL_MAX_TEXTURE_BUFFER_SIZE = 35883
GL_MAX_TEXTURE_BUFFER_SIZE_ARB = 35883
GL_MAX_TEXTURE_BUFFER_SIZE_EXT = 35883
GL_TEXTURE_BINDING_BUFFER = 35884
GL_TEXTURE_BINDING_BUFFER_ARB = 35884
GL_TEXTURE_BINDING_BUFFER_EXT = 35884
GL_TEXTURE_BUFFER_DATA_STORE_BINDING = 35885
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB = 35885
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT = 35885
GL_TEXTURE_BUFFER_FORMAT_ARB = 35886
GL_TEXTURE_BUFFER_FORMAT_EXT = 35886
GL_ANY_SAMPLES_PASSED = 35887
GL_ANY_SAMPLES_PASSED_EXT = 35887
GL_SAMPLE_SHADING = 35894
GL_SAMPLE_SHADING_ARB = 35894
GL_MIN_SAMPLE_SHADING_VALUE = 35895
GL_MIN_SAMPLE_SHADING_VALUE_ARB = 35895
GL_R11F_G11F_B10F = 35898
GL_R11F_G11F_B10F_EXT = 35898
GL_UNSIGNED_INT_10F_11F_11F_REV = 35899
GL_UNSIGNED_INT_10F_11F_11F_REV_EXT = 35899
GL_RGBA_SIGNED_COMPONENTS_EXT = 35900
GL_RGB9_E5 = 35901
GL_RGB9_E5_EXT = 35901
GL_UNSIGNED_INT_5_9_9_9_REV = 35902
GL_UNSIGNED_INT_5_9_9_9_REV_EXT = 35902
GL_TEXTURE_SHARED_SIZE = 35903
GL_TEXTURE_SHARED_SIZE_EXT = 35903
GL_SRGB = 35904
GL_SRGB_EXT = 35904
GL_SRGB8 = 35905
GL_SRGB8_EXT = 35905
GL_SRGB_ALPHA = 35906
GL_SRGB_ALPHA_EXT = 35906
GL_SRGB8_ALPHA8 = 35907
GL_SRGB8_ALPHA8_EXT = 35907
GL_SLUMINANCE_ALPHA = 35908
GL_SLUMINANCE_ALPHA_EXT = 35908
GL_SLUMINANCE8_ALPHA8 = 35909
GL_SLUMINANCE8_ALPHA8_EXT = 35909
GL_SLUMINANCE = 35910
GL_SLUMINANCE_EXT = 35910
GL_SLUMINANCE8 = 35911
GL_SLUMINANCE8_EXT = 35911
GL_COMPRESSED_SRGB = 35912
GL_COMPRESSED_SRGB_EXT = 35912
GL_COMPRESSED_SRGB_ALPHA = 35913
GL_COMPRESSED_SRGB_ALPHA_EXT = 35913
GL_COMPRESSED_SLUMINANCE = 35914
GL_COMPRESSED_SLUMINANCE_EXT = 35914
GL_COMPRESSED_SLUMINANCE_ALPHA = 35915
GL_COMPRESSED_SLUMINANCE_ALPHA_EXT = 35915
GL_COMPRESSED_SRGB_S3TC_DXT1_EXT = 35916
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT = 35917
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT = 35918
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT = 35919
GL_COMPRESSED_LUMINANCE_LATC1_EXT = 35952
GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT = 35953
GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT = 35954
GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT = 35955
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 35958
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT = 35958
GL_TRANSFORM_FEEDBACK_BUFFER_MODE = 35967
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT = 35967
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 35968
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT = 35968
GL_TRANSFORM_FEEDBACK_VARYINGS = 35971
GL_TRANSFORM_FEEDBACK_VARYINGS_EXT = 35971
GL_TRANSFORM_FEEDBACK_BUFFER_START = 35972
GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT = 35972
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = 35973
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT = 35973
GL_PRIMITIVES_GENERATED = 35975
GL_PRIMITIVES_GENERATED_EXT = 35975
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 35976
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT = 35976
GL_RASTERIZER_DISCARD = 35977
GL_RASTERIZER_DISCARD_EXT = 35977
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 35978
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT = 35978
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 35979
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT = 35979
GL_INTERLEAVED_ATTRIBS = 35980
GL_INTERLEAVED_ATTRIBS_EXT = 35980
GL_SEPARATE_ATTRIBS = 35981
GL_SEPARATE_ATTRIBS_EXT = 35981
GL_TRANSFORM_FEEDBACK_BUFFER = 35982
GL_TRANSFORM_FEEDBACK_BUFFER_EXT = 35982
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = 35983
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT = 35983
GL_POINT_SPRITE_COORD_ORIGIN = 36000
GL_LOWER_LEFT = 36001
GL_LOWER_LEFT_EXT = 36001
GL_UPPER_LEFT = 36002
GL_UPPER_LEFT_EXT = 36002
GL_STENCIL_BACK_REF = 36003
GL_STENCIL_BACK_VALUE_MASK = 36004
GL_STENCIL_BACK_WRITEMASK = 36005
GL_DRAW_FRAMEBUFFER_BINDING = 36006
GL_DRAW_FRAMEBUFFER_BINDING_ANGLE = 36006
GL_DRAW_FRAMEBUFFER_BINDING_EXT = 36006
GL_FRAMEBUFFER_BINDING = 36006
GL_FRAMEBUFFER_BINDING_ANGLE = 36006
GL_FRAMEBUFFER_BINDING_EXT = 36006
GL_RENDERBUFFER_BINDING = 36007
GL_RENDERBUFFER_BINDING_ANGLE = 36007
GL_RENDERBUFFER_BINDING_EXT = 36007
GL_READ_FRAMEBUFFER = 36008
GL_READ_FRAMEBUFFER_ANGLE = 36008
GL_READ_FRAMEBUFFER_EXT = 36008
GL_DRAW_FRAMEBUFFER = 36009
GL_DRAW_FRAMEBUFFER_ANGLE = 36009
GL_DRAW_FRAMEBUFFER_EXT = 36009
GL_READ_FRAMEBUFFER_BINDING = 36010
GL_READ_FRAMEBUFFER_BINDING_ANGLE = 36010
GL_READ_FRAMEBUFFER_BINDING_EXT = 36010
GL_RENDERBUFFER_SAMPLES = 36011
GL_RENDERBUFFER_SAMPLES_ANGLE = 36011
GL_RENDERBUFFER_SAMPLES_EXT = 36011
GL_DEPTH_COMPONENT32F = 36012
GL_DEPTH32F_STENCIL8 = 36013
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 36048
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT = 36048
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 36049
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT = 36049
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 36050
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT = 36050
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 36051
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT = 36051
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT = 36052
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 36052
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT = 36052
GL_FRAMEBUFFER_COMPLETE = 36053
GL_FRAMEBUFFER_COMPLETE_EXT = 36053
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 36054
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT = 36054
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 36055
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT = 36055
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 36057
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT = 36057
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT = 36058
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 36059
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT = 36059
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 36060
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT = 36060
GL_FRAMEBUFFER_UNSUPPORTED = 36061
GL_FRAMEBUFFER_UNSUPPORTED_EXT = 36061
GL_MAX_COLOR_ATTACHMENTS = 36063
GL_MAX_COLOR_ATTACHMENTS_EXT = 36063
GL_COLOR_ATTACHMENT0 = 36064
GL_COLOR_ATTACHMENT0_EXT = 36064
GL_COLOR_ATTACHMENT1 = 36065
GL_COLOR_ATTACHMENT1_EXT = 36065
GL_COLOR_ATTACHMENT2 = 36066
GL_COLOR_ATTACHMENT2_EXT = 36066
GL_COLOR_ATTACHMENT3 = 36067
GL_COLOR_ATTACHMENT3_EXT = 36067
GL_COLOR_ATTACHMENT4 = 36068
GL_COLOR_ATTACHMENT4_EXT = 36068
GL_COLOR_ATTACHMENT5 = 36069
GL_COLOR_ATTACHMENT5_EXT = 36069
GL_COLOR_ATTACHMENT6 = 36070
GL_COLOR_ATTACHMENT6_EXT = 36070
GL_COLOR_ATTACHMENT7 = 36071
GL_COLOR_ATTACHMENT7_EXT = 36071
GL_COLOR_ATTACHMENT8 = 36072
GL_COLOR_ATTACHMENT8_EXT = 36072
GL_COLOR_ATTACHMENT9 = 36073
GL_COLOR_ATTACHMENT9_EXT = 36073
GL_COLOR_ATTACHMENT10 = 36074
GL_COLOR_ATTACHMENT10_EXT = 36074
GL_COLOR_ATTACHMENT11 = 36075
GL_COLOR_ATTACHMENT11_EXT = 36075
GL_COLOR_ATTACHMENT12 = 36076
GL_COLOR_ATTACHMENT12_EXT = 36076
GL_COLOR_ATTACHMENT13 = 36077
GL_COLOR_ATTACHMENT13_EXT = 36077
GL_COLOR_ATTACHMENT14 = 36078
GL_COLOR_ATTACHMENT14_EXT = 36078
GL_COLOR_ATTACHMENT15 = 36079
GL_COLOR_ATTACHMENT15_EXT = 36079
GL_COLOR_ATTACHMENT16 = 36080
GL_COLOR_ATTACHMENT17 = 36081
GL_COLOR_ATTACHMENT18 = 36082
GL_COLOR_ATTACHMENT19 = 36083
GL_COLOR_ATTACHMENT20 = 36084
GL_COLOR_ATTACHMENT21 = 36085
GL_COLOR_ATTACHMENT22 = 36086
GL_COLOR_ATTACHMENT23 = 36087
GL_COLOR_ATTACHMENT24 = 36088
GL_COLOR_ATTACHMENT25 = 36089
GL_COLOR_ATTACHMENT26 = 36090
GL_COLOR_ATTACHMENT27 = 36091
GL_COLOR_ATTACHMENT28 = 36092
GL_COLOR_ATTACHMENT29 = 36093
GL_COLOR_ATTACHMENT30 = 36094
GL_COLOR_ATTACHMENT31 = 36095
GL_DEPTH_ATTACHMENT = 36096
GL_DEPTH_ATTACHMENT_EXT = 36096
GL_STENCIL_ATTACHMENT = 36128
GL_STENCIL_ATTACHMENT_EXT = 36128
GL_FRAMEBUFFER = 36160
GL_FRAMEBUFFER_EXT = 36160
GL_RENDERBUFFER = 36161
GL_RENDERBUFFER_EXT = 36161
GL_RENDERBUFFER_WIDTH = 36162
GL_RENDERBUFFER_WIDTH_EXT = 36162
GL_RENDERBUFFER_HEIGHT = 36163
GL_RENDERBUFFER_HEIGHT_EXT = 36163
GL_RENDERBUFFER_INTERNAL_FORMAT = 36164
GL_RENDERBUFFER_INTERNAL_FORMAT_EXT = 36164
GL_STENCIL_INDEX1 = 36166
GL_STENCIL_INDEX1_EXT = 36166
GL_STENCIL_INDEX4 = 36167
GL_STENCIL_INDEX4_EXT = 36167
GL_STENCIL_INDEX8 = 36168
GL_STENCIL_INDEX8_EXT = 36168
GL_STENCIL_INDEX16 = 36169
GL_STENCIL_INDEX16_EXT = 36169
GL_RENDERBUFFER_RED_SIZE = 36176
GL_RENDERBUFFER_RED_SIZE_EXT = 36176
GL_RENDERBUFFER_GREEN_SIZE = 36177
GL_RENDERBUFFER_GREEN_SIZE_EXT = 36177
GL_RENDERBUFFER_BLUE_SIZE = 36178
GL_RENDERBUFFER_BLUE_SIZE_EXT = 36178
GL_RENDERBUFFER_ALPHA_SIZE = 36179
GL_RENDERBUFFER_ALPHA_SIZE_EXT = 36179
GL_RENDERBUFFER_DEPTH_SIZE = 36180
GL_RENDERBUFFER_DEPTH_SIZE_EXT = 36180
GL_RENDERBUFFER_STENCIL_SIZE = 36181
GL_RENDERBUFFER_STENCIL_SIZE_EXT = 36181
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 36182
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_ANGLE = 36182
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT = 36182
GL_MAX_SAMPLES = 36183
GL_MAX_SAMPLES_ANGLE = 36183
GL_MAX_SAMPLES_EXT = 36183
GL_RGB565 = 36194
GL_PRIMITIVE_RESTART_FIXED_INDEX = 36201
GL_ANY_SAMPLES_PASSED_CONSERVATIVE = 36202
GL_ANY_SAMPLES_PASSED_CONSERVATIVE_EXT = 36202
GL_MAX_ELEMENT_INDEX = 36203
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT = 36204
GL_RGBA32UI = 36208
GL_RGBA32UI_EXT = 36208
GL_RGB32UI = 36209
GL_RGB32UI_EXT = 36209
GL_ALPHA32UI_EXT = 36210
GL_INTENSITY32UI_EXT = 36211
GL_LUMINANCE32UI_EXT = 36212
GL_LUMINANCE_ALPHA32UI_EXT = 36213
GL_RGBA16UI = 36214
GL_RGBA16UI_EXT = 36214
GL_RGB16UI = 36215
GL_RGB16UI_EXT = 36215
GL_ALPHA16UI_EXT = 36216
GL_INTENSITY16UI_EXT = 36217
GL_LUMINANCE16UI_EXT = 36218
GL_LUMINANCE_ALPHA16UI_EXT = 36219
GL_RGBA8UI = 36220
GL_RGBA8UI_EXT = 36220
GL_RGB8UI = 36221
GL_RGB8UI_EXT = 36221
GL_ALPHA8UI_EXT = 36222
GL_INTENSITY8UI_EXT = 36223
GL_LUMINANCE8UI_EXT = 36224
GL_LUMINANCE_ALPHA8UI_EXT = 36225
GL_RGBA32I = 36226
GL_RGBA32I_EXT = 36226
GL_RGB32I = 36227
GL_RGB32I_EXT = 36227
GL_ALPHA32I_EXT = 36228
GL_INTENSITY32I_EXT = 36229
GL_LUMINANCE32I_EXT = 36230
GL_LUMINANCE_ALPHA32I_EXT = 36231
GL_RGBA16I = 36232
GL_RGBA16I_EXT = 36232
GL_RGB16I = 36233
GL_RGB16I_EXT = 36233
GL_ALPHA16I_EXT = 36234
GL_INTENSITY16I_EXT = 36235
GL_LUMINANCE16I_EXT = 36236
GL_LUMINANCE_ALPHA16I_EXT = 36237
GL_RGBA8I = 36238
GL_RGBA8I_EXT = 36238
GL_RGB8I = 36239
GL_RGB8I_EXT = 36239
GL_ALPHA8I_EXT = 36240
GL_INTENSITY8I_EXT = 36241
GL_LUMINANCE8I_EXT = 36242
GL_LUMINANCE_ALPHA8I_EXT = 36243
GL_RED_INTEGER = 36244
GL_RED_INTEGER_EXT = 36244
GL_GREEN_INTEGER = 36245
GL_GREEN_INTEGER_EXT = 36245
GL_BLUE_INTEGER = 36246
GL_BLUE_INTEGER_EXT = 36246
GL_ALPHA_INTEGER = 36247
GL_ALPHA_INTEGER_EXT = 36247
GL_RGB_INTEGER = 36248
GL_RGB_INTEGER_EXT = 36248
GL_RGBA_INTEGER = 36249
GL_RGBA_INTEGER_EXT = 36249
GL_BGR_INTEGER = 36250
GL_BGR_INTEGER_EXT = 36250
GL_BGRA_INTEGER = 36251
GL_BGRA_INTEGER_EXT = 36251
GL_LUMINANCE_INTEGER_EXT = 36252
GL_LUMINANCE_ALPHA_INTEGER_EXT = 36253
GL_RGBA_INTEGER_MODE_EXT = 36254
GL_INT_2_10_10_10_REV = 36255
GL_FRAMEBUFFER_ATTACHMENT_LAYERED = 36263
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB = 36263
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT = 36263
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 36264
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB = 36264
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT = 36264
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB = 36265
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT = 36265
GL_FLOAT_32_UNSIGNED_INT_24_8_REV = 36269
GL_SHADER_INCLUDE_ARB = 36270
GL_FRAMEBUFFER_SRGB = 36281
GL_FRAMEBUFFER_SRGB_EXT = 36281
GL_FRAMEBUFFER_SRGB_CAPABLE_EXT = 36282
GL_COMPRESSED_RED_RGTC1 = 36283
GL_COMPRESSED_RED_RGTC1_EXT = 36283
GL_COMPRESSED_SIGNED_RED_RGTC1 = 36284
GL_COMPRESSED_SIGNED_RED_RGTC1_EXT = 36284
GL_COMPRESSED_RED_GREEN_RGTC2_EXT = 36285
GL_COMPRESSED_RG_RGTC2 = 36285
GL_COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT = 36286
GL_COMPRESSED_SIGNED_RG_RGTC2 = 36286
GL_SAMPLER_1D_ARRAY = 36288
GL_SAMPLER_1D_ARRAY_EXT = 36288
GL_SAMPLER_2D_ARRAY = 36289
GL_SAMPLER_2D_ARRAY_EXT = 36289
GL_SAMPLER_BUFFER = 36290
GL_SAMPLER_BUFFER_EXT = 36290
GL_SAMPLER_1D_ARRAY_SHADOW = 36291
GL_SAMPLER_1D_ARRAY_SHADOW_EXT = 36291
GL_SAMPLER_2D_ARRAY_SHADOW = 36292
GL_SAMPLER_2D_ARRAY_SHADOW_EXT = 36292
GL_SAMPLER_CUBE_SHADOW = 36293
GL_SAMPLER_CUBE_SHADOW_EXT = 36293
GL_UNSIGNED_INT_VEC2 = 36294
GL_UNSIGNED_INT_VEC2_EXT = 36294
GL_UNSIGNED_INT_VEC3 = 36295
GL_UNSIGNED_INT_VEC3_EXT = 36295
GL_UNSIGNED_INT_VEC4 = 36296
GL_UNSIGNED_INT_VEC4_EXT = 36296
GL_INT_SAMPLER_1D = 36297
GL_INT_SAMPLER_1D_EXT = 36297
GL_INT_SAMPLER_2D = 36298
GL_INT_SAMPLER_2D_EXT = 36298
GL_INT_SAMPLER_3D = 36299
GL_INT_SAMPLER_3D_EXT = 36299
GL_INT_SAMPLER_CUBE = 36300
GL_INT_SAMPLER_CUBE_EXT = 36300
GL_INT_SAMPLER_2D_RECT = 36301
GL_INT_SAMPLER_2D_RECT_EXT = 36301
GL_INT_SAMPLER_1D_ARRAY = 36302
GL_INT_SAMPLER_1D_ARRAY_EXT = 36302
GL_INT_SAMPLER_2D_ARRAY = 36303
GL_INT_SAMPLER_2D_ARRAY_EXT = 36303
GL_INT_SAMPLER_BUFFER = 36304
GL_INT_SAMPLER_BUFFER_EXT = 36304
GL_UNSIGNED_INT_SAMPLER_1D = 36305
GL_UNSIGNED_INT_SAMPLER_1D_EXT = 36305
GL_UNSIGNED_INT_SAMPLER_2D = 36306
GL_UNSIGNED_INT_SAMPLER_2D_EXT = 36306
GL_UNSIGNED_INT_SAMPLER_3D = 36307
GL_UNSIGNED_INT_SAMPLER_3D_EXT = 36307
GL_UNSIGNED_INT_SAMPLER_CUBE = 36308
GL_UNSIGNED_INT_SAMPLER_CUBE_EXT = 36308
GL_UNSIGNED_INT_SAMPLER_2D_RECT = 36309
GL_UNSIGNED_INT_SAMPLER_2D_RECT_EXT = 36309
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = 36310
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY_EXT = 36310
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 36311
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY_EXT = 36311
GL_UNSIGNED_INT_SAMPLER_BUFFER = 36312
GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT = 36312
GL_GEOMETRY_SHADER = 36313
GL_GEOMETRY_SHADER_ARB = 36313
GL_GEOMETRY_SHADER_EXT = 36313
GL_GEOMETRY_VERTICES_OUT_ARB = 36314
GL_GEOMETRY_VERTICES_OUT_EXT = 36314
GL_GEOMETRY_INPUT_TYPE_ARB = 36315
GL_GEOMETRY_INPUT_TYPE_EXT = 36315
GL_GEOMETRY_OUTPUT_TYPE_ARB = 36316
GL_GEOMETRY_OUTPUT_TYPE_EXT = 36316
GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB = 36317
GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT = 36317
GL_MAX_VERTEX_VARYING_COMPONENTS_ARB = 36318
GL_MAX_VERTEX_VARYING_COMPONENTS_EXT = 36318
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = 36319
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB = 36319
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT = 36319
GL_MAX_GEOMETRY_OUTPUT_VERTICES = 36320
GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB = 36320
GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT = 36320
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 36321
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB = 36321
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT = 36321
GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT = 36322
GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT = 36323
GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT = 36324
GL_ACTIVE_SUBROUTINES = 36325
GL_ACTIVE_SUBROUTINE_UNIFORMS = 36326
GL_MAX_SUBROUTINES = 36327
GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS = 36328
GL_NAMED_STRING_LENGTH_ARB = 36329
GL_NAMED_STRING_TYPE_ARB = 36330
GL_MAX_BINDABLE_UNIFORM_SIZE_EXT = 36333
GL_UNIFORM_BUFFER_EXT = 36334
GL_UNIFORM_BUFFER_BINDING_EXT = 36335
GL_LOW_FLOAT = 36336
GL_MEDIUM_FLOAT = 36337
GL_HIGH_FLOAT = 36338
GL_LOW_INT = 36339
GL_MEDIUM_INT = 36340
GL_HIGH_INT = 36341
GL_SHADER_BINARY_FORMATS = 36344
GL_NUM_SHADER_BINARY_FORMATS = 36345
GL_SHADER_COMPILER = 36346
GL_MAX_VERTEX_UNIFORM_VECTORS = 36347
GL_MAX_VARYING_VECTORS = 36348
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 36349
GL_QUERY_WAIT = 36371
GL_QUERY_NO_WAIT = 36372
GL_QUERY_BY_REGION_WAIT = 36373
GL_QUERY_BY_REGION_NO_WAIT = 36374
GL_QUERY_WAIT_INVERTED = 36375
GL_QUERY_NO_WAIT_INVERTED = 36376
GL_QUERY_BY_REGION_WAIT_INVERTED = 36377
GL_QUERY_BY_REGION_NO_WAIT_INVERTED = 36378
GL_POLYGON_OFFSET_CLAMP = 36379
GL_POLYGON_OFFSET_CLAMP_EXT = 36379
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 36382
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS_EXT = 36382
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 36383
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT = 36383
GL_TRANSFORM_FEEDBACK = 36386
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED = 36387
GL_TRANSFORM_FEEDBACK_PAUSED = 36387
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE = 36388
GL_TRANSFORM_FEEDBACK_ACTIVE = 36388
GL_TRANSFORM_FEEDBACK_BINDING = 36389
GL_TIMESTAMP = 36392
GL_TIMESTAMP_EXT = 36392
GL_PROGRAM_MATRIX_EXT = 36397
GL_TRANSPOSE_PROGRAM_MATRIX_EXT = 36398
GL_PROGRAM_MATRIX_STACK_DEPTH_EXT = 36399
GL_TEXTURE_SWIZZLE_R = 36418
GL_TEXTURE_SWIZZLE_R_EXT = 36418
GL_TEXTURE_SWIZZLE_G = 36419
GL_TEXTURE_SWIZZLE_G_EXT = 36419
GL_TEXTURE_SWIZZLE_B = 36420
GL_TEXTURE_SWIZZLE_B_EXT = 36420
GL_TEXTURE_SWIZZLE_A = 36421
GL_TEXTURE_SWIZZLE_A_EXT = 36421
GL_TEXTURE_SWIZZLE_RGBA = 36422
GL_TEXTURE_SWIZZLE_RGBA_EXT = 36422
GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS = 36423
GL_ACTIVE_SUBROUTINE_MAX_LENGTH = 36424
GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH = 36425
GL_NUM_COMPATIBLE_SUBROUTINES = 36426
GL_COMPATIBLE_SUBROUTINES = 36427
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION = 36428
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION_EXT = 36428
GL_FIRST_VERTEX_CONVENTION = 36429
GL_FIRST_VERTEX_CONVENTION_EXT = 36429
GL_LAST_VERTEX_CONVENTION = 36430
GL_LAST_VERTEX_CONVENTION_EXT = 36430
GL_PROVOKING_VERTEX = 36431
GL_PROVOKING_VERTEX_EXT = 36431
GL_SAMPLE_POSITION = 36432
GL_SAMPLE_LOCATION_ARB = 36432
GL_SAMPLE_MASK = 36433
GL_SAMPLE_MASK_VALUE = 36434
GL_MAX_SAMPLE_MASK_WORDS = 36441
GL_MAX_GEOMETRY_SHADER_INVOCATIONS = 36442
GL_MAX_GEOMETRY_SHADER_INVOCATIONS_EXT = 36442
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = 36443
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = 36444
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = 36445
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 36446
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 36446
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 36447
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 36447
GL_MAX_TRANSFORM_FEEDBACK_BUFFERS = 36464
GL_MAX_VERTEX_STREAMS = 36465
GL_PATCH_VERTICES = 36466
GL_PATCH_VERTICES_EXT = 36466
GL_PATCH_DEFAULT_INNER_LEVEL = 36467
GL_PATCH_DEFAULT_INNER_LEVEL_EXT = 36467
GL_PATCH_DEFAULT_OUTER_LEVEL = 36468
GL_PATCH_DEFAULT_OUTER_LEVEL_EXT = 36468
GL_TESS_CONTROL_OUTPUT_VERTICES = 36469
GL_TESS_CONTROL_OUTPUT_VERTICES_EXT = 36469
GL_TESS_GEN_MODE = 36470
GL_TESS_GEN_MODE_EXT = 36470
GL_TESS_GEN_SPACING = 36471
GL_TESS_GEN_SPACING_EXT = 36471
GL_TESS_GEN_VERTEX_ORDER = 36472
GL_TESS_GEN_VERTEX_ORDER_EXT = 36472
GL_TESS_GEN_POINT_MODE = 36473
GL_TESS_GEN_POINT_MODE_EXT = 36473
GL_ISOLINES = 36474
GL_ISOLINES_EXT = 36474
GL_FRACTIONAL_ODD = 36475
GL_FRACTIONAL_ODD_EXT = 36475
GL_FRACTIONAL_EVEN = 36476
GL_FRACTIONAL_EVEN_EXT = 36476
GL_MAX_PATCH_VERTICES = 36477
GL_MAX_PATCH_VERTICES_EXT = 36477
GL_MAX_TESS_GEN_LEVEL = 36478
GL_MAX_TESS_GEN_LEVEL_EXT = 36478
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 36479
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS_EXT = 36479
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 36480
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT = 36480
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 36481
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS_EXT = 36481
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 36482
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS_EXT = 36482
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 36483
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS_EXT = 36483
GL_MAX_TESS_PATCH_COMPONENTS = 36484
GL_MAX_TESS_PATCH_COMPONENTS_EXT = 36484
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 36485
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS_EXT = 36485
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 36486
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS_EXT = 36486
GL_TESS_EVALUATION_SHADER = 36487
GL_TESS_EVALUATION_SHADER_EXT = 36487
GL_TESS_CONTROL_SHADER = 36488
GL_TESS_CONTROL_SHADER_EXT = 36488
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS = 36489
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS_EXT = 36489
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 36490
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS_EXT = 36490
GL_COMPRESSED_RGBA_BPTC_UNORM = 36492
GL_COMPRESSED_RGBA_BPTC_UNORM_ARB = 36492
GL_COMPRESSED_RGBA_BPTC_UNORM_EXT = 36492
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM = 36493
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB = 36493
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT = 36493
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT = 36494
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB = 36494
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT = 36494
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT = 36495
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB = 36495
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT = 36495
GL_INCLUSIVE_EXT = 36624
GL_EXCLUSIVE_EXT = 36625
GL_WINDOW_RECTANGLE_EXT = 36626
GL_WINDOW_RECTANGLE_MODE_EXT = 36627
GL_MAX_WINDOW_RECTANGLES_EXT = 36628
GL_NUM_WINDOW_RECTANGLES_EXT = 36629
GL_COPY_READ_BUFFER = 36662
GL_COPY_READ_BUFFER_BINDING = 36662
GL_COPY_WRITE_BUFFER = 36663
GL_COPY_WRITE_BUFFER_BINDING = 36663
GL_MAX_IMAGE_UNITS = 36664
GL_MAX_IMAGE_UNITS_EXT = 36664
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS = 36665
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS_EXT = 36665
GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES = 36665
GL_IMAGE_BINDING_NAME = 36666
GL_IMAGE_BINDING_NAME_EXT = 36666
GL_IMAGE_BINDING_LEVEL = 36667
GL_IMAGE_BINDING_LEVEL_EXT = 36667
GL_IMAGE_BINDING_LAYERED = 36668
GL_IMAGE_BINDING_LAYERED_EXT = 36668
GL_IMAGE_BINDING_LAYER = 36669
GL_IMAGE_BINDING_LAYER_EXT = 36669
GL_IMAGE_BINDING_ACCESS = 36670
GL_IMAGE_BINDING_ACCESS_EXT = 36670
GL_DRAW_INDIRECT_BUFFER = 36671
GL_DRAW_INDIRECT_BUFFER_BINDING = 36675
GL_DOUBLE_MAT2 = 36678
GL_DOUBLE_MAT2_EXT = 36678
GL_DOUBLE_MAT3 = 36679
GL_DOUBLE_MAT3_EXT = 36679
GL_DOUBLE_MAT4 = 36680
GL_DOUBLE_MAT4_EXT = 36680
GL_DOUBLE_MAT2x3 = 36681
GL_DOUBLE_MAT2x3_EXT = 36681
GL_DOUBLE_MAT2x4 = 36682
GL_DOUBLE_MAT2x4_EXT = 36682
GL_DOUBLE_MAT3x2 = 36683
GL_DOUBLE_MAT3x2_EXT = 36683
GL_DOUBLE_MAT3x4 = 36684
GL_DOUBLE_MAT3x4_EXT = 36684
GL_DOUBLE_MAT4x2 = 36685
GL_DOUBLE_MAT4x2_EXT = 36685
GL_DOUBLE_MAT4x3 = 36686
GL_DOUBLE_MAT4x3_EXT = 36686
GL_VERTEX_BINDING_BUFFER = 36687
GL_MALI_SHADER_BINARY_ARM = 36704
GL_MALI_PROGRAM_BINARY_ARM = 36705
GL_MAX_SHADER_PIXEL_LOCAL_STORAGE_FAST_SIZE_EXT = 36707
GL_SHADER_PIXEL_LOCAL_STORAGE_EXT = 36708
GL_FETCH_PER_SAMPLE_ARM = 36709
GL_FRAGMENT_SHADER_FRAMEBUFFER_FETCH_MRT_ARM = 36710
GL_MAX_SHADER_PIXEL_LOCAL_STORAGE_SIZE_EXT = 36711
GL_TEXTURE_ASTC_DECODE_PRECISION_EXT = 36713
GL_RED_SNORM = 36752
GL_RG_SNORM = 36753
GL_RGB_SNORM = 36754
GL_RGBA_SNORM = 36755
GL_R8_SNORM = 36756
GL_RG8_SNORM = 36757
GL_RGB8_SNORM = 36758
GL_RGBA8_SNORM = 36759
GL_R16_SNORM = 36760
GL_R16_SNORM_EXT = 36760
GL_RG16_SNORM = 36761
GL_RG16_SNORM_EXT = 36761
GL_RGB16_SNORM = 36762
GL_RGB16_SNORM_EXT = 36762
GL_RGBA16_SNORM = 36763
GL_RGBA16_SNORM_EXT = 36763
GL_SIGNED_NORMALIZED = 36764
GL_PRIMITIVE_RESTART = 36765
GL_PRIMITIVE_RESTART_INDEX = 36766
GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB = 36767
GL_GPU_DISJOINT_EXT = 36795
GL_SR8_EXT = 36797
GL_SRG8_EXT = 36798
GL_TEXTURE_FORMAT_SRGB_OVERRIDE_EXT = 36799
GL_SHADER_BINARY_VIV = 36804
GL_INT64_VEC2_ARB = 36841
GL_INT64_VEC3_ARB = 36842
GL_INT64_VEC4_ARB = 36843
GL_UNSIGNED_INT64_VEC2_ARB = 36853
GL_UNSIGNED_INT64_VEC3_ARB = 36854
GL_UNSIGNED_INT64_VEC4_ARB = 36855
GL_DOUBLE_VEC2 = 36860
GL_DOUBLE_VEC2_EXT = 36860
GL_DOUBLE_VEC3 = 36861
GL_DOUBLE_VEC3_EXT = 36861
GL_DOUBLE_VEC4 = 36862
GL_DOUBLE_VEC4_EXT = 36862
GL_TEXTURE_CUBE_MAP_ARRAY = 36873
GL_TEXTURE_CUBE_MAP_ARRAY_ARB = 36873
GL_TEXTURE_CUBE_MAP_ARRAY_EXT = 36873
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 36874
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB = 36874
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_EXT = 36874
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY = 36875
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB = 36875
GL_SAMPLER_CUBE_MAP_ARRAY = 36876
GL_SAMPLER_CUBE_MAP_ARRAY_ARB = 36876
GL_SAMPLER_CUBE_MAP_ARRAY_EXT = 36876
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW = 36877
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB = 36877
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_EXT = 36877
GL_INT_SAMPLER_CUBE_MAP_ARRAY = 36878
GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 36878
GL_INT_SAMPLER_CUBE_MAP_ARRAY_EXT = 36878
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 36879
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 36879
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_EXT = 36879
GL_ALPHA_SNORM = 36880
GL_LUMINANCE_SNORM = 36881
GL_LUMINANCE_ALPHA_SNORM = 36882
GL_INTENSITY_SNORM = 36883
GL_ALPHA8_SNORM = 36884
GL_LUMINANCE8_SNORM = 36885
GL_LUMINANCE8_ALPHA8_SNORM = 36886
GL_INTENSITY8_SNORM = 36887
GL_ALPHA16_SNORM = 36888
GL_LUMINANCE16_SNORM = 36889
GL_LUMINANCE16_ALPHA16_SNORM = 36890
GL_INTENSITY16_SNORM = 36891
GL_GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX = 36935
GL_GPU_MEMORY_INFO_TOTAL_AVAILABLE_MEMORY_NVX = 36936
GL_GPU_MEMORY_INFO_CURRENT_AVAILABLE_VIDMEM_NVX = 36937
GL_GPU_MEMORY_INFO_EVICTION_COUNT_NVX = 36938
GL_GPU_MEMORY_INFO_EVICTED_MEMORY_NVX = 36939
GL_IMAGE_1D = 36940
GL_IMAGE_1D_EXT = 36940
GL_IMAGE_2D = 36941
GL_IMAGE_2D_EXT = 36941
GL_IMAGE_3D = 36942
GL_IMAGE_3D_EXT = 36942
GL_IMAGE_2D_RECT = 36943
GL_IMAGE_2D_RECT_EXT = 36943
GL_IMAGE_CUBE = 36944
GL_IMAGE_CUBE_EXT = 36944
GL_IMAGE_BUFFER = 36945
GL_IMAGE_BUFFER_EXT = 36945
GL_IMAGE_1D_ARRAY = 36946
GL_IMAGE_1D_ARRAY_EXT = 36946
GL_IMAGE_2D_ARRAY = 36947
GL_IMAGE_2D_ARRAY_EXT = 36947
GL_IMAGE_CUBE_MAP_ARRAY = 36948
GL_IMAGE_CUBE_MAP_ARRAY_EXT = 36948
GL_IMAGE_2D_MULTISAMPLE = 36949
GL_IMAGE_2D_MULTISAMPLE_EXT = 36949
GL_IMAGE_2D_MULTISAMPLE_ARRAY = 36950
GL_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 36950
GL_INT_IMAGE_1D = 36951
GL_INT_IMAGE_1D_EXT = 36951
GL_INT_IMAGE_2D = 36952
GL_INT_IMAGE_2D_EXT = 36952
GL_INT_IMAGE_3D = 36953
GL_INT_IMAGE_3D_EXT = 36953
GL_INT_IMAGE_2D_RECT = 36954
GL_INT_IMAGE_2D_RECT_EXT = 36954
GL_INT_IMAGE_CUBE = 36955
GL_INT_IMAGE_CUBE_EXT = 36955
GL_INT_IMAGE_BUFFER = 36956
GL_INT_IMAGE_BUFFER_EXT = 36956
GL_INT_IMAGE_1D_ARRAY = 36957
GL_INT_IMAGE_1D_ARRAY_EXT = 36957
GL_INT_IMAGE_2D_ARRAY = 36958
GL_INT_IMAGE_2D_ARRAY_EXT = 36958
GL_INT_IMAGE_CUBE_MAP_ARRAY = 36959
GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT = 36959
GL_INT_IMAGE_2D_MULTISAMPLE = 36960
GL_INT_IMAGE_2D_MULTISAMPLE_EXT = 36960
GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 36961
GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 36961
GL_UNSIGNED_INT_IMAGE_1D = 36962
GL_UNSIGNED_INT_IMAGE_1D_EXT = 36962
GL_UNSIGNED_INT_IMAGE_2D = 36963
GL_UNSIGNED_INT_IMAGE_2D_EXT = 36963
GL_UNSIGNED_INT_IMAGE_3D = 36964
GL_UNSIGNED_INT_IMAGE_3D_EXT = 36964
GL_UNSIGNED_INT_IMAGE_2D_RECT = 36965
GL_UNSIGNED_INT_IMAGE_2D_RECT_EXT = 36965
GL_UNSIGNED_INT_IMAGE_CUBE = 36966
GL_UNSIGNED_INT_IMAGE_CUBE_EXT = 36966
GL_UNSIGNED_INT_IMAGE_BUFFER = 36967
GL_UNSIGNED_INT_IMAGE_BUFFER_EXT = 36967
GL_UNSIGNED_INT_IMAGE_1D_ARRAY = 36968
GL_UNSIGNED_INT_IMAGE_1D_ARRAY_EXT = 36968
GL_UNSIGNED_INT_IMAGE_2D_ARRAY = 36969
GL_UNSIGNED_INT_IMAGE_2D_ARRAY_EXT = 36969
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY = 36970
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT = 36970
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE = 36971
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_EXT = 36971
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 36972
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 36972
GL_MAX_IMAGE_SAMPLES = 36973
GL_MAX_IMAGE_SAMPLES_EXT = 36973
GL_IMAGE_BINDING_FORMAT = 36974
GL_IMAGE_BINDING_FORMAT_EXT = 36974
GL_RGB10_A2UI = 36975
GL_SCALED_RESOLVE_FASTEST_EXT = 37050
GL_SCALED_RESOLVE_NICEST_EXT = 37051
GL_MIN_MAP_BUFFER_ALIGNMENT = 37052
GL_IMAGE_FORMAT_COMPATIBILITY_TYPE = 37063
GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE = 37064
GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS = 37065
GL_MAX_VERTEX_IMAGE_UNIFORMS = 37066
GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS = 37067
GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS_EXT = 37067
GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS = 37068
GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS_EXT = 37068
GL_MAX_GEOMETRY_IMAGE_UNIFORMS = 37069
GL_MAX_GEOMETRY_IMAGE_UNIFORMS_EXT = 37069
GL_MAX_FRAGMENT_IMAGE_UNIFORMS = 37070
GL_MAX_COMBINED_IMAGE_UNIFORMS = 37071
GL_SHADER_STORAGE_BUFFER = 37074
GL_SHADER_STORAGE_BUFFER_BINDING = 37075
GL_SHADER_STORAGE_BUFFER_START = 37076
GL_SHADER_STORAGE_BUFFER_SIZE = 37077
GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS = 37078
GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS = 37079
GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS_EXT = 37079
GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS = 37080
GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS_EXT = 37080
GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS = 37081
GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS_EXT = 37081
GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS = 37082
GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS = 37083
GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS = 37084
GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS = 37085
GL_MAX_SHADER_STORAGE_BLOCK_SIZE = 37086
GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT = 37087
GL_SYNC_X11_FENCE_EXT = 37089
GL_DEPTH_STENCIL_TEXTURE_MODE = 37098
GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS = 37099
GL_MAX_COMPUTE_FIXED_GROUP_INVOCATIONS_ARB = 37099
GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER = 37100
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER = 37101
GL_DISPATCH_INDIRECT_BUFFER = 37102
GL_DISPATCH_INDIRECT_BUFFER_BINDING = 37103
GL_COLOR_ATTACHMENT_EXT = 37104
GL_MULTIVIEW_EXT = 37105
GL_MAX_MULTIVIEW_BUFFERS_EXT = 37106
GL_CONTEXT_ROBUST_ACCESS = 37107
GL_CONTEXT_ROBUST_ACCESS_EXT = 37107
GL_TEXTURE_2D_MULTISAMPLE = 37120
GL_PROXY_TEXTURE_2D_MULTISAMPLE = 37121
GL_TEXTURE_2D_MULTISAMPLE_ARRAY = 37122
GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY = 37123
GL_TEXTURE_BINDING_2D_MULTISAMPLE = 37124
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 37125
GL_TEXTURE_SAMPLES = 37126
GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = 37127
GL_SAMPLER_2D_MULTISAMPLE = 37128
GL_INT_SAMPLER_2D_MULTISAMPLE = 37129
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 37130
GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 37131
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 37132
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 37133
GL_MAX_COLOR_TEXTURE_SAMPLES = 37134
GL_MAX_DEPTH_TEXTURE_SAMPLES = 37135
GL_MAX_INTEGER_SAMPLES = 37136
GL_MAX_SERVER_WAIT_TIMEOUT = 37137
GL_OBJECT_TYPE = 37138
GL_SYNC_CONDITION = 37139
GL_SYNC_STATUS = 37140
GL_SYNC_FLAGS = 37141
GL_SYNC_FENCE = 37142
GL_SYNC_GPU_COMMANDS_COMPLETE = 37143
GL_UNSIGNALED = 37144
GL_SIGNALED = 37145
GL_ALREADY_SIGNALED = 37146
GL_TIMEOUT_EXPIRED = 37147
GL_CONDITION_SATISFIED = 37148
GL_WAIT_FAILED = 37149
GL_BUFFER_ACCESS_FLAGS = 37151
GL_BUFFER_MAP_LENGTH = 37152
GL_BUFFER_MAP_OFFSET = 37153
GL_MAX_VERTEX_OUTPUT_COMPONENTS = 37154
GL_MAX_GEOMETRY_INPUT_COMPONENTS = 37155
GL_MAX_GEOMETRY_INPUT_COMPONENTS_EXT = 37155
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = 37156
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS_EXT = 37156
GL_MAX_FRAGMENT_INPUT_COMPONENTS = 37157
GL_CONTEXT_PROFILE_MASK = 37158
GL_UNPACK_COMPRESSED_BLOCK_WIDTH = 37159
GL_UNPACK_COMPRESSED_BLOCK_HEIGHT = 37160
GL_UNPACK_COMPRESSED_BLOCK_DEPTH = 37161
GL_UNPACK_COMPRESSED_BLOCK_SIZE = 37162
GL_PACK_COMPRESSED_BLOCK_WIDTH = 37163
GL_PACK_COMPRESSED_BLOCK_HEIGHT = 37164
GL_PACK_COMPRESSED_BLOCK_DEPTH = 37165
GL_PACK_COMPRESSED_BLOCK_SIZE = 37166
GL_TEXTURE_IMMUTABLE_FORMAT = 37167
GL_TEXTURE_IMMUTABLE_FORMAT_EXT = 37167
GL_SGX_PROGRAM_BINARY_IMG = 37168
GL_RENDERBUFFER_SAMPLES_IMG = 37171
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_IMG = 37172
GL_MAX_SAMPLES_IMG = 37173
GL_TEXTURE_SAMPLES_IMG = 37174
GL_COMPRESSED_RGBA_PVRTC_2BPPV2_IMG = 37175
GL_COMPRESSED_RGBA_PVRTC_4BPPV2_IMG = 37176
GL_CUBIC_IMG = 37177
GL_CUBIC_MIPMAP_NEAREST_IMG = 37178
GL_CUBIC_MIPMAP_LINEAR_IMG = 37179
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_AND_DOWNSAMPLE_IMG = 37180
GL_NUM_DOWNSAMPLE_SCALES_IMG = 37181
GL_DOWNSAMPLE_SCALES_IMG = 37182
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SCALE_IMG = 37183
GL_MAX_DEBUG_MESSAGE_LENGTH = 37187
GL_MAX_DEBUG_MESSAGE_LENGTH_ARB = 37187
GL_MAX_DEBUG_LOGGED_MESSAGES = 37188
GL_MAX_DEBUG_LOGGED_MESSAGES_ARB = 37188
GL_DEBUG_LOGGED_MESSAGES = 37189
GL_DEBUG_LOGGED_MESSAGES_ARB = 37189
GL_DEBUG_SEVERITY_HIGH = 37190
GL_DEBUG_SEVERITY_HIGH_ARB = 37190
GL_DEBUG_SEVERITY_MEDIUM = 37191
GL_DEBUG_SEVERITY_MEDIUM_ARB = 37191
GL_DEBUG_SEVERITY_LOW = 37192
GL_DEBUG_SEVERITY_LOW_ARB = 37192
GL_BUFFER_OBJECT_EXT = 37201
GL_QUERY_OBJECT_EXT = 37203
GL_VERTEX_ARRAY_OBJECT_EXT = 37204
GL_QUERY_BUFFER = 37266
GL_QUERY_BUFFER_BINDING = 37267
GL_QUERY_RESULT_NO_WAIT = 37268
GL_VIRTUAL_PAGE_SIZE_X_ARB = 37269
GL_VIRTUAL_PAGE_SIZE_X_EXT = 37269
GL_VIRTUAL_PAGE_SIZE_Y_ARB = 37270
GL_VIRTUAL_PAGE_SIZE_Y_EXT = 37270
GL_VIRTUAL_PAGE_SIZE_Z_ARB = 37271
GL_VIRTUAL_PAGE_SIZE_Z_EXT = 37271
GL_MAX_SPARSE_TEXTURE_SIZE_ARB = 37272
GL_MAX_SPARSE_TEXTURE_SIZE_EXT = 37272
GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB = 37273
GL_MAX_SPARSE_3D_TEXTURE_SIZE_EXT = 37273
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS = 37274
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB = 37274
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_EXT = 37274
GL_TEXTURE_BUFFER_OFFSET = 37277
GL_TEXTURE_BUFFER_OFFSET_EXT = 37277
GL_TEXTURE_BUFFER_SIZE = 37278
GL_TEXTURE_BUFFER_SIZE_EXT = 37278
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT = 37279
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT_EXT = 37279
GL_TEXTURE_SPARSE_ARB = 37286
GL_TEXTURE_SPARSE_EXT = 37286
GL_VIRTUAL_PAGE_SIZE_INDEX_ARB = 37287
GL_VIRTUAL_PAGE_SIZE_INDEX_EXT = 37287
GL_NUM_VIRTUAL_PAGE_SIZES_ARB = 37288
GL_NUM_VIRTUAL_PAGE_SIZES_EXT = 37288
GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB = 37289
GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_EXT = 37289
GL_NUM_SPARSE_LEVELS_ARB = 37290
GL_NUM_SPARSE_LEVELS_EXT = 37290
GL_MAX_SHADER_COMPILER_THREADS_ARB = 37296
GL_COMPLETION_STATUS_ARB = 37297
GL_COMPUTE_SHADER = 37305
GL_MAX_COMPUTE_UNIFORM_BLOCKS = 37307
GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS = 37308
GL_MAX_COMPUTE_IMAGE_UNIFORMS = 37309
GL_MAX_COMPUTE_WORK_GROUP_COUNT = 37310
GL_MAX_COMPUTE_WORK_GROUP_SIZE = 37311
GL_MAX_COMPUTE_FIXED_GROUP_SIZE_ARB = 37311
GL_UNPACK_FLIP_Y_WEBGL = 37440
GL_UNPACK_PREMULTIPLY_ALPHA_WEBGL = 37441
GL_CONTEXT_LOST_WEBGL = 37442
GL_UNPACK_COLORSPACE_CONVERSION_WEBGL = 37443
GL_BROWSER_DEFAULT_WEBGL = 37444
GL_SHADER_BINARY_DMP = 37456
GL_SMAPHS30_PROGRAM_BINARY_DMP = 37457
GL_SMAPHS_PROGRAM_BINARY_DMP = 37458
GL_DMP_PROGRAM_BINARY_DMP = 37459
GL_GCCSO_SHADER_BINARY_FJ = 37472
GL_COMPRESSED_R11_EAC = 37488
GL_COMPRESSED_SIGNED_R11_EAC = 37489
GL_COMPRESSED_RG11_EAC = 37490
GL_COMPRESSED_SIGNED_RG11_EAC = 37491
GL_COMPRESSED_RGB8_ETC2 = 37492
GL_COMPRESSED_SRGB8_ETC2 = 37493
GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 37494
GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 37495
GL_COMPRESSED_RGBA8_ETC2_EAC = 37496
GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 37497
GL_MULTIPLY = 37524
GL_SCREEN = 37525
GL_OVERLAY = 37526
GL_DARKEN = 37527
GL_LIGHTEN = 37528
GL_COLORDODGE = 37529
GL_COLORBURN = 37530
GL_HARDLIGHT = 37531
GL_SOFTLIGHT = 37532
GL_DIFFERENCE = 37534
GL_EXCLUSION = 37536
GL_HSL_HUE = 37549
GL_HSL_SATURATION = 37550
GL_HSL_COLOR = 37551
GL_HSL_LUMINOSITY = 37552
GL_MAX_LGPU_GPUS_NVX = 37562
GL_PRIMITIVE_BOUNDING_BOX_ARB = 37566
GL_PRIMITIVE_BOUNDING_BOX = 37566
GL_PRIMITIVE_BOUNDING_BOX_EXT = 37566
GL_ATOMIC_COUNTER_BUFFER = 37568
GL_ATOMIC_COUNTER_BUFFER_BINDING = 37569
GL_ATOMIC_COUNTER_BUFFER_START = 37570
GL_ATOMIC_COUNTER_BUFFER_SIZE = 37571
GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE = 37572
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS = 37573
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES = 37574
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER = 37575
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER = 37576
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER = 37577
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER = 37578
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER = 37579
GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS = 37580
GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS = 37581
GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS_EXT = 37581
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS = 37582
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS_EXT = 37582
GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS = 37583
GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS_EXT = 37583
GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS = 37584
GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS = 37585
GL_MAX_VERTEX_ATOMIC_COUNTERS = 37586
GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS = 37587
GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS_EXT = 37587
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS = 37588
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS_EXT = 37588
GL_MAX_GEOMETRY_ATOMIC_COUNTERS = 37589
GL_MAX_GEOMETRY_ATOMIC_COUNTERS_EXT = 37589
GL_MAX_FRAGMENT_ATOMIC_COUNTERS = 37590
GL_MAX_COMBINED_ATOMIC_COUNTERS = 37591
GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE = 37592
GL_ACTIVE_ATOMIC_COUNTER_BUFFERS = 37593
GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX = 37594
GL_UNSIGNED_INT_ATOMIC_COUNTER = 37595
GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS = 37596
GL_DEBUG_OUTPUT = 37600
GL_UNIFORM = 37601
GL_UNIFORM_BLOCK = 37602
GL_PROGRAM_INPUT = 37603
GL_PROGRAM_OUTPUT = 37604
GL_BUFFER_VARIABLE = 37605
GL_SHADER_STORAGE_BLOCK = 37606
GL_IS_PER_PATCH = 37607
GL_IS_PER_PATCH_EXT = 37607
GL_VERTEX_SUBROUTINE = 37608
GL_TESS_CONTROL_SUBROUTINE = 37609
GL_TESS_EVALUATION_SUBROUTINE = 37610
GL_GEOMETRY_SUBROUTINE = 37611
GL_FRAGMENT_SUBROUTINE = 37612
GL_COMPUTE_SUBROUTINE = 37613
GL_VERTEX_SUBROUTINE_UNIFORM = 37614
GL_TESS_CONTROL_SUBROUTINE_UNIFORM = 37615
GL_TESS_EVALUATION_SUBROUTINE_UNIFORM = 37616
GL_GEOMETRY_SUBROUTINE_UNIFORM = 37617
GL_FRAGMENT_SUBROUTINE_UNIFORM = 37618
GL_COMPUTE_SUBROUTINE_UNIFORM = 37619
GL_TRANSFORM_FEEDBACK_VARYING = 37620
GL_ACTIVE_RESOURCES = 37621
GL_MAX_NAME_LENGTH = 37622
GL_MAX_NUM_ACTIVE_VARIABLES = 37623
GL_MAX_NUM_COMPATIBLE_SUBROUTINES = 37624
GL_NAME_LENGTH = 37625
GL_TYPE = 37626
GL_ARRAY_SIZE = 37627
GL_OFFSET = 37628
GL_BLOCK_INDEX = 37629
GL_ARRAY_STRIDE = 37630
GL_MATRIX_STRIDE = 37631
GL_IS_ROW_MAJOR = 37632
GL_ATOMIC_COUNTER_BUFFER_INDEX = 37633
GL_BUFFER_BINDING = 37634
GL_BUFFER_DATA_SIZE = 37635
GL_NUM_ACTIVE_VARIABLES = 37636
GL_ACTIVE_VARIABLES = 37637
GL_REFERENCED_BY_VERTEX_SHADER = 37638
GL_REFERENCED_BY_TESS_CONTROL_SHADER = 37639
GL_REFERENCED_BY_TESS_CONTROL_SHADER_EXT = 37639
GL_REFERENCED_BY_TESS_EVALUATION_SHADER = 37640
GL_REFERENCED_BY_TESS_EVALUATION_SHADER_EXT = 37640
GL_REFERENCED_BY_GEOMETRY_SHADER = 37641
GL_REFERENCED_BY_GEOMETRY_SHADER_EXT = 37641
GL_REFERENCED_BY_FRAGMENT_SHADER = 37642
GL_REFERENCED_BY_COMPUTE_SHADER = 37643
GL_TOP_LEVEL_ARRAY_SIZE = 37644
GL_TOP_LEVEL_ARRAY_STRIDE = 37645
GL_LOCATION = 37646
GL_LOCATION_INDEX = 37647
GL_LOCATION_INDEX_EXT = 37647
GL_FRAMEBUFFER_DEFAULT_WIDTH = 37648
GL_FRAMEBUFFER_DEFAULT_HEIGHT = 37649
GL_FRAMEBUFFER_DEFAULT_LAYERS = 37650
GL_FRAMEBUFFER_DEFAULT_LAYERS_EXT = 37650
GL_FRAMEBUFFER_DEFAULT_SAMPLES = 37651
GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS = 37652
GL_MAX_FRAMEBUFFER_WIDTH = 37653
GL_MAX_FRAMEBUFFER_HEIGHT = 37654
GL_MAX_FRAMEBUFFER_LAYERS = 37655
GL_MAX_FRAMEBUFFER_LAYERS_EXT = 37655
GL_MAX_FRAMEBUFFER_SAMPLES = 37656
GL_RASTER_MULTISAMPLE_EXT = 37671
GL_RASTER_SAMPLES_EXT = 37672
GL_MAX_RASTER_SAMPLES_EXT = 37673
GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT = 37674
GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT = 37675
GL_EFFECTIVE_RASTER_SAMPLES_EXT = 37676
GL_SAMPLE_LOCATION_SUBPIXEL_BITS_ARB = 37693
GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_ARB = 37694
GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_ARB = 37695
GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_ARB = 37696
GL_PROGRAMMABLE_SAMPLE_LOCATION_ARB = 37697
GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_ARB = 37698
GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_ARB = 37699
GL_MAX_COMPUTE_VARIABLE_GROUP_INVOCATIONS_ARB = 37700
GL_MAX_COMPUTE_VARIABLE_GROUP_SIZE_ARB = 37701
GL_LOCATION_COMPONENT = 37706
GL_TRANSFORM_FEEDBACK_BUFFER_INDEX = 37707
GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE = 37708
GL_CLIP_ORIGIN = 37724
GL_CLIP_ORIGIN_EXT = 37724
GL_CLIP_DEPTH_MODE = 37725
GL_CLIP_DEPTH_MODE_EXT = 37725
GL_NEGATIVE_ONE_TO_ONE = 37726
GL_NEGATIVE_ONE_TO_ONE_EXT = 37726
GL_ZERO_TO_ONE = 37727
GL_ZERO_TO_ONE_EXT = 37727
GL_CLEAR_TEXTURE = 37733
GL_TEXTURE_REDUCTION_MODE_ARB = 37734
GL_TEXTURE_REDUCTION_MODE_EXT = 37734
GL_WEIGHTED_AVERAGE_ARB = 37735
GL_WEIGHTED_AVERAGE_EXT = 37735
GL_NUM_SAMPLE_COUNTS = 37760
GL_MULTISAMPLE_LINE_WIDTH_RANGE_ARB = 37761
GL_MULTISAMPLE_LINE_WIDTH_RANGE = 37761
GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY_ARB = 37762
GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY = 37762
GL_VIEW_CLASS_EAC_R11 = 37763
GL_VIEW_CLASS_EAC_RG11 = 37764
GL_VIEW_CLASS_ETC2_RGB = 37765
GL_VIEW_CLASS_ETC2_RGBA = 37766
GL_VIEW_CLASS_ETC2_EAC_RGBA = 37767
GL_VIEW_CLASS_ASTC_4x4_RGBA = 37768
GL_VIEW_CLASS_ASTC_5x4_RGBA = 37769
GL_VIEW_CLASS_ASTC_5x5_RGBA = 37770
GL_VIEW_CLASS_ASTC_6x5_RGBA = 37771
GL_VIEW_CLASS_ASTC_6x6_RGBA = 37772
GL_VIEW_CLASS_ASTC_8x5_RGBA = 37773
GL_VIEW_CLASS_ASTC_8x6_RGBA = 37774
GL_VIEW_CLASS_ASTC_8x8_RGBA = 37775
GL_VIEW_CLASS_ASTC_10x5_RGBA = 37776
GL_VIEW_CLASS_ASTC_10x6_RGBA = 37777
GL_VIEW_CLASS_ASTC_10x8_RGBA = 37778
GL_VIEW_CLASS_ASTC_10x10_RGBA = 37779
GL_VIEW_CLASS_ASTC_12x10_RGBA = 37780
GL_VIEW_CLASS_ASTC_12x12_RGBA = 37781
GL_TRANSLATED_SHADER_SOURCE_LENGTH_ANGLE = 37792
GL_BGRA8_EXT = 37793
GL_TEXTURE_USAGE_ANGLE = 37794
GL_FRAMEBUFFER_ATTACHMENT_ANGLE = 37795
GL_PACK_REVERSE_ROW_ORDER_ANGLE = 37796
GL_PROGRAM_BINARY_ANGLE = 37798
GL_COMPRESSED_RGBA_ASTC_4x4 = 37808
GL_COMPRESSED_RGBA_ASTC_5x4 = 37809
GL_COMPRESSED_RGBA_ASTC_5x5 = 37810
GL_COMPRESSED_RGBA_ASTC_6x5 = 37811
GL_COMPRESSED_RGBA_ASTC_6x6 = 37812
GL_COMPRESSED_RGBA_ASTC_8x5 = 37813
GL_COMPRESSED_RGBA_ASTC_8x6 = 37814
GL_COMPRESSED_RGBA_ASTC_8x8 = 37815
GL_COMPRESSED_RGBA_ASTC_10x5 = 37816
GL_COMPRESSED_RGBA_ASTC_10x6 = 37817
GL_COMPRESSED_RGBA_ASTC_10x8 = 37818
GL_COMPRESSED_RGBA_ASTC_10x10 = 37819
GL_COMPRESSED_RGBA_ASTC_12x10 = 37820
GL_COMPRESSED_RGBA_ASTC_12x12 = 37821
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4 = 37840
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4 = 37841
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5 = 37842
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5 = 37843
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6 = 37844
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5 = 37845
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6 = 37846
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8 = 37847
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5 = 37848
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6 = 37849
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8 = 37850
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10 = 37851
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10 = 37852
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12 = 37853
GL_COMPRESSED_SRGB_ALPHA_PVRTC_2BPPV2_IMG = 37872
GL_COMPRESSED_SRGB_ALPHA_PVRTC_4BPPV2_IMG = 37873
GL_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_EXT = 38192
GL_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_EXT = 38193
GL_UPLOAD_GPU_MASK_NVX = 38218
GL_SHADER_BINARY_FORMAT_SPIR_V = 38225
GL_SHADER_BINARY_FORMAT_SPIR_V_ARB = 38225
GL_SPIR_V_BINARY = 38226
GL_SPIR_V_BINARY_ARB = 38226
GL_SPIR_V_EXTENSIONS = 38227
GL_NUM_SPIR_V_EXTENSIONS = 38228
GL_TEXTURE_TILING_EXT = 38272
GL_DEDICATED_MEMORY_OBJECT_EXT = 38273
GL_NUM_TILING_TYPES_EXT = 38274
GL_TILING_TYPES_EXT = 38275
GL_OPTIMAL_TILING_EXT = 38276
GL_LINEAR_TILING_EXT = 38277
GL_HANDLE_TYPE_OPAQUE_FD_EXT = 38278
GL_HANDLE_TYPE_OPAQUE_WIN32_EXT = 38279
GL_HANDLE_TYPE_OPAQUE_WIN32_KMT_EXT = 38280
GL_HANDLE_TYPE_D3D12_TILEPOOL_EXT = 38281
GL_HANDLE_TYPE_D3D12_RESOURCE_EXT = 38282
GL_HANDLE_TYPE_D3D11_IMAGE_EXT = 38283
GL_HANDLE_TYPE_D3D11_IMAGE_KMT_EXT = 38284
GL_LAYOUT_GENERAL_EXT = 38285
GL_LAYOUT_COLOR_ATTACHMENT_EXT = 38286
GL_LAYOUT_DEPTH_STENCIL_ATTACHMENT_EXT = 38287
GL_LAYOUT_DEPTH_STENCIL_READ_ONLY_EXT = 38288
GL_LAYOUT_SHADER_READ_ONLY_EXT = 38289
GL_LAYOUT_TRANSFER_SRC_EXT = 38290
GL_LAYOUT_TRANSFER_DST_EXT = 38291
GL_HANDLE_TYPE_D3D12_FENCE_EXT = 38292
GL_D3D12_FENCE_VALUE_EXT = 38293
GL_NUM_DEVICE_UUIDS_EXT = 38294
GL_DEVICE_UUID_EXT = 38295
GL_DRIVER_UUID_EXT = 38296
GL_DEVICE_LUID_EXT = 38297
GL_DEVICE_NODE_MASK_EXT = 38298
GL_PROTECTED_MEMORY_OBJECT_EXT = 38299
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR = 38448
GL_MAX_VIEWS_OVR = 38449
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR = 38450
GL_FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR = 38451
GL_GS_SHADER_BINARY_MTK = 38464
GL_GS_PROGRAM_BINARY_MTK = 38465
GL_MAX_SHADER_COMBINED_LOCAL_STORAGE_FAST_SIZE_EXT = 38480
GL_MAX_SHADER_COMBINED_LOCAL_STORAGE_SIZE_EXT = 38481
GL_FRAMEBUFFER_INCOMPLETE_INSUFFICIENT_SHADER_COMBINED_LOCAL_STORAGE_EXT = 38482

%module uuid_cbr_c
%{
  #include "uuid_cbr.h"
%}

%newobject generate;
%include <exception.i>

%typemap(in,numinputs=0) int *err (int myerr = 0) {
    $1 = &myerr;
}

%typemap(argout) int* err {
    if(*$1 != 0) {
        SWIG_exception(SWIG_ValueError,err_string(*$1));
    }
}
%include "uuid_cbr.h"

Ray Tracing in One Week
=======================

The python code here is inspired by the C++ code in the book "Ray Tracing in One
Weekend".  I will implement each exercise in the book in Python.  Also develop C
versions in parallel with the python.  Just for giggles.

The **python** folder holds the vanilla python code from the book.  This
includes writing a PPM file as output.  There will be at least one folder for
each chapter.  I will also attempt to write C code to do the same ray trace.

Got up to **write_PPM5b** in the C code before it got hard.  Adding a 'hit'
function pointer to the **hit_record** function in *hitable.h* is the way
forward, but that breaks all prexisting code which I don't want to do.  So the
C code stops at **write_PPM5b**.

The **numpy** folder holds versions of the above programs that attempt to use
*numpy* to speed up execution.  The basic code is in the **rt_numpy.py** file
and was found at http://excamera.com/sphinx/article-ray.html .  The program
**rt_numpy.py** id basically **rt3.py** from that page, with changes to use
*pillow*.

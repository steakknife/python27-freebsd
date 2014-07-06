--- Modules/fcntlmodule.c.orig	2014-06-29 19:05:43.000000000 -0700
+++ Modules/fcntlmodule.c	2014-07-05 22:51:47.000000000 -0700
@@ -104,14 +104,9 @@
        platforms) or a negative number on others (32-bit PyInt)
        whereas the system expects it to be a 32bit bit field value
        regardless of it being passed as an int or unsigned long on
-       various platforms.  See the termios.TIOCSWINSZ constant across
-       platforms for an example of this.
-
-       If any of the 64bit platforms ever decide to use more than 32bits
-       in their unsigned long ioctl codes this will break and need
-       special casing based on the platform being built on.
+       various platforms.
      */
-    unsigned int code;
+    unsigned long code;
     int arg;
     int ret;
     char *str;
@@ -119,7 +114,7 @@
     int mutate_arg = 1;
     char buf[IOCTL_BUFSZ+1];  /* argument plus NUL byte */
 
-    if (PyArg_ParseTuple(args, "O&Iw#|i:ioctl",
+    if (PyArg_ParseTuple(args, "O&kw#|i:ioctl",
                          conv_descriptor, &fd, &code,
                          &str, &len, &mutate_arg)) {
         char *arg;
@@ -170,7 +165,7 @@
     }
 
     PyErr_Clear();
-    if (PyArg_ParseTuple(args, "O&Is#:ioctl",
+    if (PyArg_ParseTuple(args, "O&ks#:ioctl",
                          conv_descriptor, &fd, &code, &str, &len)) {
         if (len > IOCTL_BUFSZ) {
             PyErr_SetString(PyExc_ValueError,
@@ -192,7 +187,7 @@
     PyErr_Clear();
     arg = 0;
     if (!PyArg_ParseTuple(args,
-         "O&I|i;ioctl requires a file or file descriptor,"
+         "O&k|i;ioctl requires a file or file descriptor,"
          " an integer and optionally an integer or buffer argument",
                           conv_descriptor, &fd, &code, &arg)) {
       return NULL;

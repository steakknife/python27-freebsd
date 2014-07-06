--- setup.py.orig	2014-06-29 19:05:48.000000000 -0700
+++ setup.py	2014-07-05 23:01:53.000000000 -0700
@@ -33,7 +33,7 @@
 COMPILED_WITH_PYDEBUG = ('--with-pydebug' in sysconfig.get_config_var("CONFIG_ARGS"))
 
 # This global variable is used to hold the list of modules to be disabled.
-disabled_module_list = []
+disabled_module_list = ["_bsddb", "_sqlite3", "_tkinter", "gdbm", "mpz"]
 
 def add_dir_to_list(dirlist, dir):
     """Add the directory 'dir' to the list 'dirlist' (at the front) if
@@ -723,7 +723,7 @@
         # use the same library for the readline and curses modules.
         if 'curses' in readline_termcap_library:
             curses_library = readline_termcap_library
-        elif self.compiler.find_library_file(lib_dirs, 'ncursesw'):
+        elif self.compiler.find_library_file(lib_dirs, 'xxxncursesw'):
             curses_library = 'ncursesw'
         elif self.compiler.find_library_file(lib_dirs, 'ncurses'):
             curses_library = 'ncurses'
@@ -764,7 +764,7 @@
                                                      'termcap'):
                 readline_libs.append('termcap')
             exts.append( Extension('readline', ['readline.c'],
-                                   library_dirs=['/usr/lib/termcap'],
+                                   library_dirs=['/usr/lib', '/usr/lib/termcap'],
                                    extra_link_args=readline_extra_link_args,
                                    libraries=readline_libs) )
         else:
@@ -867,6 +867,8 @@
             # OpenSSL doesn't do these until 0.9.8 so we'll bring our own hash
             exts.append( Extension('_sha256', ['sha256module.c']) )
             exts.append( Extension('_sha512', ['sha512module.c']) )
+        else:
+            open('.without_own_sha', 'w')
 
         # Modules that provide persistent dictionary-like semantics.  You will
         # probably want to arrange for at least one of them to be available on
@@ -1212,7 +1214,7 @@
                 sysroot = macosx_sdk_root()
                 f = os.path.join(sysroot, f[1:])
 
-        if os.path.exists(f) and not db_incs:
+        if os.path.exists(f):
             data = open(f).read()
             m = re.search(r"#s*define\s+HASHVERSION\s+2\s*", data)
             if m is not None:
@@ -1343,7 +1345,7 @@
         panel_library = 'panel'
         curses_incs = None
         if curses_library.startswith('ncurses'):
-            if curses_library == 'ncursesw':
+            if curses_library == 'xxxncursesw':
                 # Bug 1464056: If _curses.so links with ncursesw,
                 # _curses_panel.so must link with panelw.
                 panel_library = 'panelw'
@@ -1352,6 +1354,7 @@
                                     [os.path.join(d, 'ncursesw') for d in inc_dirs])
             exts.append( Extension('_curses', ['_cursesmodule.c'],
                                    include_dirs = curses_incs,
+                                   library_dirs = ['/usr/lib'],
                                    libraries = curses_libs) )
         elif curses_library == 'curses' and host_platform != 'darwin':
                 # OSX has an old Berkeley curses, not good enough for
@@ -1364,6 +1367,7 @@
                 curses_libs = ['curses']
 
             exts.append( Extension('_curses', ['_cursesmodule.c'],
+                                   library_dirs = ['/usr/lib'],
                                    libraries = curses_libs) )
         else:
             missing.append('_curses')
@@ -1551,7 +1555,7 @@
             macros = dict()
             libraries = []
 
-        elif host_platform in ('freebsd4', 'freebsd5', 'freebsd6', 'freebsd7', 'freebsd8'):
+        elif host_platform in ('freebsd4', 'freebsd5', 'freebsd6', 'freebsd7', 'freebsd8', 'freebsd9', 'freebsd10', 'freebsd11'):
             # FreeBSD's P1003.1b semaphore support is very experimental
             # and has many known problems. (as of June 2008)
             macros = dict()
@@ -1603,7 +1607,7 @@
             missing.append('linuxaudiodev')
 
         if (host_platform in ('linux2', 'freebsd4', 'freebsd5', 'freebsd6',
-                        'freebsd7', 'freebsd8')
+                        'freebsd7', 'freebsd8', 'freebsd9', 'freebsd10', 'freebsd11')
             or host_platform.startswith("gnukfreebsd")):
             exts.append( Extension('ossaudiodev', ['ossaudiodev.c']) )
         else:
@@ -2228,9 +2232,7 @@
           ext_modules=[Extension('_struct', ['_struct.c'])],
 
           # Scripts to install
-          scripts = ['Tools/scripts/pydoc', 'Tools/scripts/idle',
-                     'Tools/scripts/2to3',
-                     'Lib/smtpd.py']
+          scripts = []
         )
 
 # --install-platlib

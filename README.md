# Introduction
This is a visualizer specifically for Convex Layers.

# Code setup

The code is written in Python and c++.
The code was written using Visual Studio and Pycharm.
For Python you need an interpreter with pygame installed.
For c++ you need to take one of 2 approaches.
# 1 Install Boost and CGAL under C:/
The c++ code uses CGAL and Boost(as a dependency for CGAL).
The project is configured to look for CGAL-5.4.1 and boost_1_79_0 under C:/.
If you install them there as well the project should run.
# 2 Install the libraries wherever you want and configure Visual Studio to look in your custom location or make you own makefile
If you have the libraries already installed you can manually configure the project to look for them. 

Note: You must also install gmp and gdb as optional dependencies for CGAL and link against the gmp dlls

If you just want to run the app you can download it from the release and run main.exe

# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/abc/apriltag_python/apriltag

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/abc/apriltag_python/apriltag/build

# Include any dependencies generated for this target.
include core/CMakeFiles/lm_test.dir/depend.make

# Include the progress variables for this target.
include core/CMakeFiles/lm_test.dir/progress.make

# Include the compile flags for this target's objects.
include core/CMakeFiles/lm_test.dir/flags.make

core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o: core/CMakeFiles/lm_test.dir/flags.make
core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o: ../core/contrib/lm_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/abc/apriltag_python/apriltag/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o"
	cd /home/abc/apriltag_python/apriltag/build/core && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o -c /home/abc/apriltag_python/apriltag/core/contrib/lm_test.cpp

core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/lm_test.dir/contrib/lm_test.cpp.i"
	cd /home/abc/apriltag_python/apriltag/build/core && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/abc/apriltag_python/apriltag/core/contrib/lm_test.cpp > CMakeFiles/lm_test.dir/contrib/lm_test.cpp.i

core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/lm_test.dir/contrib/lm_test.cpp.s"
	cd /home/abc/apriltag_python/apriltag/build/core && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/abc/apriltag_python/apriltag/core/contrib/lm_test.cpp -o CMakeFiles/lm_test.dir/contrib/lm_test.cpp.s

core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.requires:

.PHONY : core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.requires

core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.provides: core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.requires
	$(MAKE) -f core/CMakeFiles/lm_test.dir/build.make core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.provides.build
.PHONY : core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.provides

core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.provides.build: core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o


# Object files for target lm_test
lm_test_OBJECTS = \
"CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o"

# External object files for target lm_test
lm_test_EXTERNAL_OBJECTS =

lm_test: core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o
lm_test: core/CMakeFiles/lm_test.dir/build.make
lm_test: lib/libapriltag.so
lm_test: core/CMakeFiles/lm_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/abc/apriltag_python/apriltag/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../lm_test"
	cd /home/abc/apriltag_python/apriltag/build/core && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/lm_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
core/CMakeFiles/lm_test.dir/build: lm_test

.PHONY : core/CMakeFiles/lm_test.dir/build

core/CMakeFiles/lm_test.dir/requires: core/CMakeFiles/lm_test.dir/contrib/lm_test.cpp.o.requires

.PHONY : core/CMakeFiles/lm_test.dir/requires

core/CMakeFiles/lm_test.dir/clean:
	cd /home/abc/apriltag_python/apriltag/build/core && $(CMAKE_COMMAND) -P CMakeFiles/lm_test.dir/cmake_clean.cmake
.PHONY : core/CMakeFiles/lm_test.dir/clean

core/CMakeFiles/lm_test.dir/depend:
	cd /home/abc/apriltag_python/apriltag/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/abc/apriltag_python/apriltag /home/abc/apriltag_python/apriltag/core /home/abc/apriltag_python/apriltag/build /home/abc/apriltag_python/apriltag/build/core /home/abc/apriltag_python/apriltag/build/core/CMakeFiles/lm_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : core/CMakeFiles/lm_test.dir/depend


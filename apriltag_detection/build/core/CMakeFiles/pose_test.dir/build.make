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
include core/CMakeFiles/pose_test.dir/depend.make

# Include the progress variables for this target.
include core/CMakeFiles/pose_test.dir/progress.make

# Include the compile flags for this target's objects.
include core/CMakeFiles/pose_test.dir/flags.make

core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o: core/CMakeFiles/pose_test.dir/flags.make
core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o: ../core/contrib/pose_test.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/abc/apriltag_python/apriltag/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o"
	cd /home/abc/apriltag_python/apriltag/build/core && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/pose_test.dir/contrib/pose_test.c.o   -c /home/abc/apriltag_python/apriltag/core/contrib/pose_test.c

core/CMakeFiles/pose_test.dir/contrib/pose_test.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/pose_test.dir/contrib/pose_test.c.i"
	cd /home/abc/apriltag_python/apriltag/build/core && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/abc/apriltag_python/apriltag/core/contrib/pose_test.c > CMakeFiles/pose_test.dir/contrib/pose_test.c.i

core/CMakeFiles/pose_test.dir/contrib/pose_test.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/pose_test.dir/contrib/pose_test.c.s"
	cd /home/abc/apriltag_python/apriltag/build/core && /usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/abc/apriltag_python/apriltag/core/contrib/pose_test.c -o CMakeFiles/pose_test.dir/contrib/pose_test.c.s

core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o.requires:

.PHONY : core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o.requires

core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o.provides: core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o.requires
	$(MAKE) -f core/CMakeFiles/pose_test.dir/build.make core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o.provides.build
.PHONY : core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o.provides

core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o.provides.build: core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o


# Object files for target pose_test
pose_test_OBJECTS = \
"CMakeFiles/pose_test.dir/contrib/pose_test.c.o"

# External object files for target pose_test
pose_test_EXTERNAL_OBJECTS =

pose_test: core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o
pose_test: core/CMakeFiles/pose_test.dir/build.make
pose_test: lib/libapriltag.so
pose_test: core/CMakeFiles/pose_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/abc/apriltag_python/apriltag/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ../pose_test"
	cd /home/abc/apriltag_python/apriltag/build/core && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pose_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
core/CMakeFiles/pose_test.dir/build: pose_test

.PHONY : core/CMakeFiles/pose_test.dir/build

core/CMakeFiles/pose_test.dir/requires: core/CMakeFiles/pose_test.dir/contrib/pose_test.c.o.requires

.PHONY : core/CMakeFiles/pose_test.dir/requires

core/CMakeFiles/pose_test.dir/clean:
	cd /home/abc/apriltag_python/apriltag/build/core && $(CMAKE_COMMAND) -P CMakeFiles/pose_test.dir/cmake_clean.cmake
.PHONY : core/CMakeFiles/pose_test.dir/clean

core/CMakeFiles/pose_test.dir/depend:
	cd /home/abc/apriltag_python/apriltag/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/abc/apriltag_python/apriltag /home/abc/apriltag_python/apriltag/core /home/abc/apriltag_python/apriltag/build /home/abc/apriltag_python/apriltag/build/core /home/abc/apriltag_python/apriltag/build/core/CMakeFiles/pose_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : core/CMakeFiles/pose_test.dir/depend


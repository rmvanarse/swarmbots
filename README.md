# Swarmbots

The project aims to automate a decentralized swarm of autonomous mobile robots to carry out different tasks. 

The system is completelly decentralized. Each robot only knows its position and the position of the robots within a speciific neighbourhood radius. The bots do not communicate with each other, and perform tasks through 'collective decision making' algorithms.

Various swarm tasks are divided into the following basic tasks:
- Aggregation/ Clustering
- Area Coverage
- Line Formation
- Shape Formation
- Forraging
- Flocking
- Collective decision making

Complex tasks can be performed through combinations of the above tasks. The project contains implementations of algorithms for simulating these tasks and ROS-packages for implementing them on a physical swarm

## Getting Started

Create a local copy of the repository by running the following command:

```git clone https://github.com/rmvanarse/swarmbots```

### Prerequisites

- **Python 3 -** for Pyplot simulations
- **Ubuntu 16.04 -** for using ROS packages
- **ROS Kinetic**
- **STDR -** (Simulator for 2D Robots) http://wiki.ros.org/stdr_simulator/Tutorials/Set%20up%20STDR%20Simulator
- **ROS Multimaster -** For deployment on a physical swarm http://wiki.ros.org/multimaster_fkie/Tutorials/Setup%20a%20ROS%20master%20synchronization

**Python libraries required for algorithm simulations -** numpy, matplotlib, math, cv2

## Running the Tests

The _simulate_pyplot.py_ file can be used to test a graphical simulation of N bots for a particular task.

```python3 algorithm_simulation/simulate_pyplot.py```

The number of bots can be varied by varying the parameter in _initialize_swarm()_ function. The initialization function can be replaced by any other initialization function from _initialize_swarm.py_ (imported).

The size of the arena can be varied by changing the values of the corresponding global parameters in _swarm_lib.py_ (imported).

The value of _task_func_ in _generate_points()_ decides the task to be carried out. The value could be the name of any of the ask functions from the imported files: aggregation.py, area_coverage.py, formations.py.

2-state decision making is simulated using the _simulate_state.py_ file on terminal (not pyplot) in a similar way.

## Description of the Stack

### File Structure:

**algorithm_simulation -** Contains a files for simulating basic algorithms on pyplot. The user can choose the initial configuration, number of bots, arena size, etc. Each basic task has a python file containing different implementations of the task. A library ( _swarm_lib.py_ ) includes all general functions required for simulating the swarm.

The following tasks have been implemented crrently: Aggregation, Area COverage, Circle formation, Line Formation and 2-state decision making

**stdr-codes -** Contains files for simulating individual bots on ROS. Each bot has its own namespace. The algorithms will publish velocity commands on _cmd_vel_ for each robot. The folder also contains resources (Maps, yaml files) and their corresponding launch files.

**apriltag_detection -** Attempt to carry out localization using April Tags and OpenCV-2.0 ( _in progress_ )
**bash -** Bash files for directly running the required rosmasters ( _in progress_ )

### Current Stage of Development
The algorithm simulation files are stable and ready to use. Implementations for Aggregation (2 implemntations), Area Coverage, Line Formation, Circle formation and 2-state decision making are complete. The ROS packages are in progress and are not ready to use directly. Simultaneously, more algorithms are being added to _algorithm_simulations_ and simulation results are being studied

### Authors:
**Rishikesh Vanarse** ( [rmvanarse](https://github.com/rmvanarse) ) - 
_Sub-Coordinator, Electronics & Robotics Club, BITS Goa_ ( [ERC-BPGC](https://github.com/ERC-BPGC/) )



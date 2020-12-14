# Visual SLAM in Urban Environments
**Team Members:** Joshua Liu (jxliu), Tyler Johnson (tgj), Thomas Wang (thomasw2), Elias Lu (zixul)

**Note**: We used the original ORB-SLAM2 repository as a baseline, which can be found [here](https://github.com/raulmur/ORB_SLAM2)

**Abstract**: Visual SLAM is a growing research topic due to the economic benefits of cameras compared to lidars. Autonomous driving solutions have begun to incorporate cameras in their arsenal of sensors to help navigate through complex urban environments. ORB-SLAM2 has remained at the forefront of state-of-the-art (SOTA) methods for many years, due to its versatility and capabilities of computing accurate real-time camera trajectory and sparse 3D scene reconstructions. One major drawback, however, is its lack of robustness to motion effects induced by motion blur during vehicle motion. In this project we investigated various methods of our own to reduce the adverse effects of motion blur, and were ultimately able to demonstrate increased motion blur robustness through a variation of pre-processing methods. The proposed approach was evaluated on the [KITTI Stereo Evaluation 2015 dataset](http://www.cvlibs.net/datasets/kitti/eval_odometry.php).

# 1. Citations

We used the ORB-SLAM2 (Stereo) method for our project:

    @article{murORB2,
      title={{ORB-SLAM2}: an Open-Source {SLAM} System for Monocular, Stereo and {RGB-D} Cameras},
      author={Mur-Artal, Ra\'ul and Tard\'os, Juan D.},
      journal={IEEE Transactions on Robotics},
      volume={33},
      number={5},
      pages={1255--1262},
      doi = {10.1109/TRO.2017.2705103},
      year={2017}
     }

# 2. Prerequisites
The library was tested by the original authors in **Ubuntu 12.04**, **14.04** and **16.04**, but it should be easy to compile in other platforms. A powerful computer (e.g. i7) will ensure real-time performance and provide more stable and accurate results.

As a note, we were able to successfully run the library with **Ubuntu 20.04** and **opencv 3.0**, and **Ubuntu 18.04** and **opencv 3.2**.

## C++11 or C++0x Compiler
We use the new thread and chrono functionalities of C++11.

## Pangolin
We use [Pangolin](https://github.com/stevenlovegrove/Pangolin) for visualization and user interface. Dowload and install instructions can be found at: https://github.com/stevenlovegrove/Pangolin.

## OpenCV
We use [OpenCV](http://opencv.org) to manipulate images and features. Dowload and install instructions can be found at: http://opencv.org. **Required at leat 2.4.3. Tested with OpenCV 2.4.11 and OpenCV 3.2**.

## Eigen3
Required by g2o (see below). Download and install instructions can be found at: http://eigen.tuxfamily.org. **Required at least 3.1.0**.

## DBoW2 and g2o (Included in Thirdparty folder)
We use modified versions of the [DBoW2](https://github.com/dorian3d/DBoW2) library to perform place recognition and [g2o](https://github.com/RainerKuemmerle/g2o) library to perform non-linear optimizations. Both modified libraries (which are BSD) are included in the *Thirdparty* folder.

## ROS (optional)
We provide some examples to process the live input of a monocular, stereo or RGB-D camera using [ROS](ros.org). Building these examples is optional. In case you want to use ROS, a version Hydro or newer is needed.

# 3. Building ORB-SLAM2 Library

Clone this repository:
```
git clone https://github.com/joshliu11/16833_Final_Project.git
```

The original authors provided a script `build.sh` to build the *Thirdparty* libraries and *ORB-SLAM2*. Please make sure you have installed all required dependencies (see section 2). Execute:
```
cd ORB_SLAM2
chmod +x build.sh
./build.sh
```

This will create **libORB_SLAM2.so**  at *lib* folder and the executables **mono_tum**, **mono_kitti**, **rgbd_tum**, **stereo_kitti**, **mono_euroc** and **stereo_euroc** in *Examples* folder.

# 4. Running the Code (Stereo)

## KITTI Dataset

1. Download the dataset (grayscale images) from http://www.cvlibs.net/datasets/kitti/eval_odometry.php into the KITTI_Dataset folder

2. Apply preprocessing
```
python KITTI_Dataset/preprocess.py
```

3. Execute the following command. Change `KITTIX.yaml`to KITTI00-02.yaml, KITTI03.yaml or KITTI04-12.yaml for sequence 0 to 2, 3, and 4 to 12 respectively. Change `PATH_TO_DATASET_FOLDER` to the uncompressed dataset folder. Change `SEQUENCE_NUMBER` to 00, 01, 02,.., 11. 
```
./Examples/Stereo/stereo_kitti Vocabulary/ORBvoc.txt Examples/Stereo/KITTIX.yaml PATH_TO_DATASET_FOLDER/dataset/sequences/SEQUENCE_NUMBER
```

# 5. Running the devkit

## KITTI development Kit

1. The development kit can be found [here](http://www.cvlibs.net/datasets/kitti/eval_scene_flow.php?benchmark=stereo) but we already include it in this repository.

2. Execute the following commands to run the devkit:
```
g++ -O3 -DNDEBUG -o evaluate_odometry evaluate_odometry.cpp matrix.cpp
```

```
./evaluate_odometry test_results
```

# 6. Results

## TODO

# MLE_Object_Tracking
---
## Introduction:
The following code uploads the video and takes from a json file the number and initial position of the objects to be tracked.

## Requirements:
1. Python (3.9)
2. OpenCV (4.2)

    ### Conda environment:
    If you use conda you can import the environment of this project.
    ```bash
    conda env create -f environment.yml
    ```
    And then activate the conda environment
    ```bash
    conda activate Epic_iO
    ```
    
## Commands to run tracking:
  To run this code is necessary to put the following parameters in the terminal:
 -j = full path of json file
 -v = full path of video
 -t = type of tracking (csrt or kcf)

Open a terminal in the folder of project and type:

```bash
python ./main.py -j "Full path of json file" -h "Full path of video" -t "csrt or kcf"
```

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import json

import h5py
import numpy as np

data = h5py.File("benchmark_results/osc_pose/data.hdf5", "r")

reached_error = []
reached_error_in_additional_steps = []
for key in data["data"].keys():
    # print(len(data[f"data/{key}"]["state_history"]))
    traj_config = json.loads(data[f"data/{key}"].attrs["config"])
    reached_error.append(
        np.abs(np.array(traj_config["reached_pose"]) - np.array(traj_config["target_pose"]))
    )
    reached_error_in_additional_steps.append(
        np.abs(
            np.array(traj_config["reached_pose_in_additional_steps"])
            - np.array(traj_config["target_pose"]) # TODO Not sure why we subtract this
        )
    )

    print(np.mean(reached_error, axis=0))
    print(np.mean(reached_error_in_additional_steps, axis=0))
    print("=========================")

import os
import numpy as np

CLASSES = ["Walking", "Jogging", "Upstairs", "Downstairs", "Sitting",
           "Standing"]

data_path = os.path.join(os.path.dirname(__file__), 'accel_dataset.npy')
all_data = np.load(data_path)
wisdm_train_x, wisdm_train_y = all_data[0]
wisdm_val_x, wisdm_val_y = all_data[1]
wisdm_test_x, wisdm_test_y = all_data[2]






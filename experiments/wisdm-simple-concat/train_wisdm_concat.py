import numpy as np

from lib.datasource import wisdm_train_x, wisdm_test_x, wisdm_train_y, \
    wisdm_test_y
from lib.gan_unlabeled_classif import gan_unlabelled_classif

print wisdm_train_x[0], wisdm_train_x[0].shape

wisdm_train_x = wisdm_train_x.reshape((-1, 300))
wisdm_test_x = wisdm_test_x.reshape((-1, 300))
wisdm_train_y = np.argmax(wisdm_train_y, axis=1).astype(np.int32)
wisdm_test_y = np.argmax(wisdm_test_y, axis=1).astype(np.int32)

print wisdm_train_x[0], wisdm_train_x[0].shape
print wisdm_train_x.shape, wisdm_test_x.shape


gan_unlabelled_classif(wisdm_train_x, wisdm_train_y,
                       wisdm_test_x, wisdm_test_y,
                       6, 300, 6000)



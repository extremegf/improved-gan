import numpy as np

# # load MNIST data
from experiment_gan_unlabeled_classif import gan_unlabelled_classif

LABEL_CNT = 9
INP_SIZE = 27 * 32
EXP_TRAIN_CASES = 60000


def reduce_labels(d):
    for i in range(d.shape[0]):
        if d[i] > LABEL_CNT - 1:
            d[i] = LABEL_CNT - 1


def npshow(s):
    for r in range(s.shape[0]):
        for e in s[r]:
            if int(e * 10) == 0:
                print '.',
            else:
                print int(e * 10),
        print


def convert_to_size(x):
    _trainx = []
    x = x.reshape((-1, 28, 28))
    for i in range(x.shape[0]):
        rows = []
        for r in range(27):
            row = x[i][r]
            row = np.append(row, [0.0] * 4)
            rows.append(row)
        _trainx.append(np.concatenate(rows))
    x = np.concatenate(_trainx)
    return x.reshape((-1, 27 * 32))


data = np.load('mnist.npz')

trainx = np.concatenate([data['x_train'], data['x_valid']], axis=0).astype(np.float32)
trainx = convert_to_size(trainx)

testx = data['x_test'].astype(np.float32)
testx = convert_to_size(testx)

trainy = np.concatenate([data['y_train'], data['y_valid']]).astype(np.int32)
reduce_labels(trainy)

testy = data['y_test'].astype(np.int32)
reduce_labels(testy)

gan_unlabelled_classif(trainx, trainy, testx, testy, LABEL_CNT, INP_SIZE, EXP_TRAIN_CASES)

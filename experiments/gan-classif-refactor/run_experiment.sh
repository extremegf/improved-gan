export THEANO_FLAGS='floatX=float32,device=gpu0,lib.cnmem=0.4'
python train_mnist_resized.py > runlog.txt

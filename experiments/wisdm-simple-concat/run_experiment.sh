export THEANO_FLAGS='floatX=float32,device=gpu0,lib.cnmem=0.5'
export PYTHONPATH=../:$PYTHONPATH
python train_wisdm_concat.py > log.txt

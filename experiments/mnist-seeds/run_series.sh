A=$1
B=$2
STEP=$3
export THEANO_FLAGS='floatX=float32,device=gpu0,lib.cnmem=0.2'


trap 'exit 1' INT

for ((i=$A; i < $B; i+=$STEP))
do
    echo 'Testing seed' $i
    cd ../../mnist_svhn_cifar10/
    python train_mnist_feature_matching.py \
        --seed=$i --seed_data=$i --iter_limit=80
done

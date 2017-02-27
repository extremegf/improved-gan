export THEANO_FLAGS='floatX=float32,device=gpu0,lib.cnmem=0.9'
export PYTHONPATH=../:$PYTHONPATH

for COUNT in 100 300
do
    for SF in 1 2 4 8 16 32
    do
        python at_on_cifar.py --count=$COUNT --net_scale_factor=$SF \
          | tee log_count_${COUNT}_sf_${SF}.txt
    done
done


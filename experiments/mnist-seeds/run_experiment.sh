for ((i=0; i < 4; i++)) 
do
    ./run_series.sh $i 20 4 > series_${i}_result.txt &
done

trap 'echo "If you terminate this, you will leave a mess."' INT
trap 'echo "If you terminate this, you will leave a mess."' TERM

echo Press any key to terminate the experiment
read line
kill -KILL $(jobs -p)
killall python


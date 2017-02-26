for ((i=0; i < 4; i++)) 
do
    ./run_series.sh $i 20 4 > series_${i}_result.txt &
done

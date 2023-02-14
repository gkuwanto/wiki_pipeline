module load python3

id=$1
name=$2
if [[ "$id" == "UNUSED" ]]; then
    echo "Done Downloading"
else
    python download_gdown.py $id $name
    ./unzip.sh $name
fi
left=$1
right=$2
mkdir -p ./data_dir

module load python3
python3 -m venv env
source  env/bin/activate
pip install -r requirements.txt

if ! ( [[ -f ./data_dir/wiki.${left} ]] && [[ -f ./data_dir/wiki.${right} ]] ); then
    ./download_wiki/download.sh $left $right
    ./preprocess_wiki_dict/unzip_wiki.sh $left $right
    ./preprocess_wiki_dict/pickle_wiki.sh $left $right
    ./preprocess_wiki_dict/get_monolingual.sh $left $right
fi
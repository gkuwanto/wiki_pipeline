left=$1
right=$2

if ! [ -f ./data_dir/wiki.${left} ]; then
    python preprocess_wiki_dict/get_mono.py ./data_dir/${left}-dump.pickle ./data_dir/wiki.${left}
fi

if ! [ -f ./data_dir/wiki.${right} ]; then
    python preprocess_wiki_dict/get_mono.py ./data_dir/${right}-dump.pickle ./data_dir/wiki.${right}
fi
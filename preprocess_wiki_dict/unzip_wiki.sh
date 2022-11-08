left=$1
right=$2

bzip2 -dk ./data_dir/wiki.${left}.xml.bz2
bzip2 -dk ./data_dir/wiki.${right}.xml.bz2

python -m wikiextractor.WikiExtractor --processes 2 -b 1G -o ./data_dir/${left} -l ./data_dir/wiki.${left}.xml
python -m wikiextractor.WikiExtractor --processes 2 -b 1G -o ./data_dir/${right} -l ./data_dir/wiki.${right}.xml

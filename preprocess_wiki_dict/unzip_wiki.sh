left=$1
right=$2


if ! [ -f ./data_dir/wiki.${left}.xml ]; then
    bzip2 -dk ./data_dir/wiki.${left}.xml.bz2
fi

if ! [ -f ./data_dir/wiki.${left}.xml ]; then
    bzip2 -dk ./data_dir/wiki.${right}.xml.bz2
fi
if [ ! -d ./data_dir/wiki-${left} ];
    python -m wikiextractor.WikiExtractor --processes 2 -b 1G -o ./data_dir/wiki-${left} -l ./data_dir/wiki.${left}.xml
fi

if [ ! -d ./data_dir/wiki-${rigth} ];
    python -m wikiextractor.WikiExtractor --processes 2 -b 1G -o ./data_dir/wiki-${right} -l ./data_dir/wiki.${right}.xml
fi
left=$1
right=$2
mkdir -p ./data_dir

if ! [ -f ./data_dir/wiki.${left}.xml.bz2 ]; then
    wget https://dumps.wikimedia.org/${left}wiki/20221101/${left}wiki-20221101-pages-articles-multistream.xml.bz2 --no-check-certificate -O ./data_dir/wiki.${left}.xml.bz2
fi

if ! [ -f ./data_dir/wiki.${right}.xml.bz2 ]; then
    wget https://dumps.wikimedia.org/${right}wiki/20221101/${right}wiki-20221101-pages-articles-multistream.xml.bz2 --no-check-certificate -O ./data_dir/wiki.${right}.xml.bz2
fi
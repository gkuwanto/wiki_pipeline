left=$1
right=$2

if ![ -f ./data_dir/${left}/dump.pickle ]; then
    python get_pickle.py not_load ${left} ./data_dir
fi
if ![ -f ./data_dir/${right}/dump.pickle ]; then
    python get_pickle.py not_load ${right} ./data_dir
fi
archive=$1
has_parent=$(zipinfo -1 "$archive" | awk '{split($NF,a,"/");print a[1]}' | sort -u | wc -l)
dir="./$(basename ${archive%%.zip})"
mkdir "$dir"
if test "$has_parent" -eq 1; then
  unzip -d /tmp/ziptemp $archive 
  mv /tmp/ziptemp/*/* "$dir"
else
  unzip -d "$dir" $archive
fi
input=""
if [ -z "$1" ]
  then
    input=$(cat)
  else
    input=$1
fi

python3 cowtay.py "$input" | cowsay
if [ ! -d "./$2/day$1" ]; then
    source venv/bin/activate
    mkdir "./$2/day$1"
    cp a.py "./$2/day$1/a.py"
    aocd $1 $2 > "./$2/day$1/data.txt"
    aocd $1 $2 > "./$2/day$1/example.txt" --example
    cd "./$2/day$1"
    echo "./$2/day$1 created, and cwd changed"
else
    echo "Directory already exists"
fi
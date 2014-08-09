#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

find $DIR/../problems -type f -name solution.cpp | while read sol
do
    sol_dir=$(dirname $sol)
    echo "$sol"

    if [ -f "$sol_dir/checker.py" ]
    then
        $DIR/test_with_checker.sh "$sol"
    else
        $DIR/test.sh "$sol"
    fi
done


#!/bin/bash

FILE=$(readlink -f $1)
DIR=$(dirname $FILE)
EXE=/tmp/exe$RANDOM

g++ $FILE -o $EXE && for t in $DIR/tests/*.in; do
    echo "input: $(basename $t)"
    $EXE < $t | diff - ${t%*.in}.out
done

rm -f $EXE

#!/bin/bash

CUR=$(dirname $(readlink -f $0))
FILE=$(readlink -f $1)
DIR=$(dirname $FILE)
EXE=/tmp/exe$RANDOM

g++ $FILE -o $EXE && for t in $DIR/tests/*.in; do
    echo "input: $(basename $t)"
    OBT=/tmp/obt$RANDOM
    $EXE < $t > $OBT
    python2 "$CUR/run_checker.py" "$DIR/checker.py" "$OBT" "${t%*.in}.out"
    rm -f $OBT
done

rm -f $EXE

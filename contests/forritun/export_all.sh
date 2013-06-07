#!/bin/bash
for c in *.xml; do
    ../../manager/manager.py -c "forritun/${c%.*}" -d .
done

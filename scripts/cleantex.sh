#!/bin/bash

for f in *.log *.gz *.aux *.pre *.snm *.fdb_latexmk *.out *.fls
do
    if [ -e $f ] ; then
        rm $f
    fi
done

for f in *.tex
do
    echo ${f%.tex}
    for g in ${f%.tex}-*.asy ${f%.tex}-*.pdf
    do 
        if [ -e $g ] ; then
            rm $g
        fi
    done
done
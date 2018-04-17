#!/bin/bash
sed -E 's/ //g' $1 > csvFolder/temp.csv
rm $1
mv csvFolder/temp.csv $1

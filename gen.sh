#! /bin/bash

tree -R ./article/ -I "images" -P "*.html" > tree
find ./article/ -name "*.html" | sort > path
python ./pagegen.py ./index.html
rm tree
rm path



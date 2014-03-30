#! /bin/bash

tree -R ./article/ -I "images" -P "*.html" > tree
find ./article/ -name "*.html" | sort > path

# 首先去掉上次留下的超链接，因为每次添加文章后，超链接有改动，我把它全部更新.
find ./article/ -name "*.html" | xargs -I {} \
		 sed -ri ':1;N;$!b1;s/(<!--PREVPAGE-->).*(<!--PRE_END-->)/\1\n\2/' {}

find ./article/ -name "*.html" | xargs -I {} \
		 sed -ri ':1;N;$!b1;s/(<!--NEXTPAGE-->).*(<!--NEXT_END-->)/\1\n\2/' {}

# 去掉主页的TREE_LIST之间的内容
sed -ri ':1;N;$!b1;s/(<!--TREE_LIST-->).*(<!--TREE_END-->)/\1\n\2/' ./index.html 
python ./pagegen.py ./index.html
rm tree
rm path



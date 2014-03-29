#! /usr/bin/python
#-*-coding:utf-8-*-

import re
import os
import string
import time
import sys

#=================Python start @ index.html files================
# Two files : tree, path. created by shell cmd: tree, find | sort
#================================================================
reg = '[0-9]{4}-[0-9]{2}-[0-9]{2}'  #use to match the xxxx-xx-xx-article_name.html files.
dirnamereg = '[a-z]{1}\..*$'


# Get the article file path from `./path` file 
def get_html_path():
	path = []
	fp = open('./path', 'r')
	lines = fp.readlines()
	for i in lines:
		i = str(i).replace('\n', '') # Mother Fuck.
		path.append(i)
	fp.close()
	return path

# Generate tree list HTML code from file `./tree`
def get_tree_list():
	date      = ''
	theme     = ''
	prefix    = ''
	tree_list = []
	idxpath   = 0
	path =get_html_path()

	fp_tree = open('./tree', 'r')
	lines   = fp_tree.readlines()
	fp_tree.close()

	for tl in lines:
		m   = re.search(reg, tl) 
		tl  = str(tl)
		pos = 0

		if m is not None: # This is an artile html file's path.
			
			# Get the Prefix string of article.
			ln = len (tl)
			for c in range(0, ln):
				if tl[c].isdigit():
					prefix = tl[:c-1]
					break

			# Get the Post date and article Theme.
			for c in range(0, ln):
				if tl[c] == '-':
					pos = pos + 1
					if pos == 3:
						date  = tl[c-10 : c] #Y? not c-1
						theme = tl[c+1:-6]
						break
		
			# Generate the tree html code for article.
			date_format = '%s%s' % (date, '  >>>> ')
			# do not use replace('\n', '\0'), error.
			filepath = str(path[idxpath]).replace('\n', '') 
			html_code = '%s%s%s%s%s%s%s' % (prefix, date_format,\
			       '<font color="#0000c6"><a href="', filepath,\
			       '">', theme, '</a></font>' )
			idxpath  = idxpath + 1
		# It's not a article, it is a catalog  directory.
		elif (re.search( dirnamereg, tl )) :  
			''' ├── c.python_language
			 	We change the color of catalog directory.
			 	├──    <font color="#0000cd", style="font-size:100%">c.python_language</font>
			 	-tl[:10]-------HTML color and style code-------------Dir_name---------End---- 
			'''

			dir_name      = str(tl[10:]).replace('\n', '')
			html_code = '%s%s%s%s' % (tl[:10], '<font color="#ffffff", style="font-size:100%">', \
					dir_name, '</font>')
		else:
			html_code = tl.replace('\n', '')
		html_code = '%s%s' % ( html_code, os.linesep )

		tree_list.append( html_code )
	return tree_list

# Open Index_File and  write tree_list code to it.
def write_tree_list( index_file ):
	fp = open( index_file, 'r')
	lines = fp.readlines()
	fp.close()
	tree_code = []
	for l in lines:
		if re.search('\TREE_LIST', l):
			tree_code.append( '%s%s' % ("<pre>", os.linesep) )
			tree_list = get_tree_list()
			for c in tree_list:
				tree_code.append (c)
			tree_code.append( '%s%s' % ("</pre>", os.linesep) )
		else:
			tree_code.append(l) 

	fp = open( index_file, 'w')
	for l in tree_code:
		fp.write(l)
	fp.close()

# Upate the next page and prevpage of every article.
def update_link( ):
	path = get_html_path()
	link = {}
	art_cnt = 0
	path_id = 0
	new_html = []

	fp = open ('./tree', 'r')
	lines = fp.readlines()
	fp.close()
	
	for i in lines:
		i = i.replace('\n', '')
		ret = re.search(reg, i)

		link[0] = ('./404.html') # For hyperlink list head.
		# Find an artilce.
		if ret is not None:
			art_cnt  = art_cnt + 1	
			art_path = path[ path_id ]
			path_id  = path_id + 1
			link[ art_cnt ] = art_path


		# This is a catalog directory
		else:
			if art_cnt > 0:
				link[ art_cnt + 1 ] = ('./404.html') # For hyperlink list tail.
				for c in link.keys():
					if (c > 0) and (link[c] != './404.html'):
						fp = open( link[c], 'r')
						print 'open file: %s' % link[c]
						lines = fp.readlines()
						fp.close()
						for l in lines:
							l = str(l).replace('\n', '')
							if re.search( '\NEXTPAGE', l ): 
								html = '%s%s%s' % ("<a href=\"../.", 
										link[ c+1 ], "\"  class=\"button\"> " )
							elif re.search('\PREVPAGE', l ):
								html = '%s%s%s' % ("<a href=\"../.", 
										link[ c-1 ], "\"  class=\"button\"\> " )
							else:
								html = l
							new_html.append('%s%s' %( html, os.linesep ) )
						fp = open( link[c], 'w' )
						for lines in new_html:
							fp.write( lines )
						fp.close()
						new_html = []

				art_cnt = 0
				link = {} 

update_link()
write_tree_list( sys.argv[1] )
print 'Generate Index file: [ %s ] OK! Have a Nice Day!' % sys.argv[1]

# ok, finish the index page !








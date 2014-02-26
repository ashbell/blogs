#! /usr/bin/python
#-*-coding:utf-8-*-

import re
import os
import string

#=============================
# The head_part of index_page
#=============================
index_start = '''

<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link href='https://fonts.googleapis.com/css?family=Architects+Daughter' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="stylesheets/stylesheet.css" media="screen" />
    <link rel="stylesheet" type="text/css" href="stylesheets/pygment_trac.css" media="screen" />
    <link rel="stylesheet" type="text/css" href="stylesheets/print.css" media="print" />

    <!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <title>小生在此恭候多时了:)</title>
  </head>

  <body>
    <header>
      <div class="inner">
        <h2>你不努力，谁都给不了你想要的生活</h2>
       <font color="#3B0B0B"> <h3>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		&nbsp;&nbsp;&nbsp;Ashbell[2014.2.11,@Shenzhen]</h3> </font>
        <a href="https://github.com/ashbell/blogs" class="button"><small>View project on</small>GitHub</a>
      </div>
    </header>

    <div id="content-wrapper">
      <div class="inner clearfix">
        <section id="main-content">
          <h3>
<a name="welcome-to-github-pages" class="anchor" href="#welcome-to-github-pages"><span class="octicon octicon-link"></span></a>2014-02-11 >>>> 欢迎您，来自CyberWorld的朋友 ：P</h3>

<p>这是我在Github上的博客，今天决定把博客搬进这里来了，：P .本人Diaosi一个，今年24,目前大学本科毕业1年半，在深圳打工混日子，从事着和自己专业兴趣完全不对口的生产业. 喜欢Linux，C， Bash脚本，热爱编程，打算入职嵌入式程序员，本科学的是电子信息工程. 欢迎您的到来.
<h3>
<a name="delimiter" class="anchor" ><span class="octicon octicon-link"></span></a>----------------------------------------------------------------------------------------------------------</h3>
<pre><code> '''

#=============================
# The tail_part of index_page
#=============================
index_end = '''

既然你在22岁时贪图安逸，就不要抱怨自己在32岁时进退两难。

</code></pre>

        </section>

        <aside id="sidebar">
          <a href="https://github.com/ashbell/blogs/zipball/master" class="button">
            <small>Download</small>
            .zip file
          </a>
          <a href="https://github.com/ashbell/blogs/tarball/master" class="button">
            <small>Download</small>
            .tar.gz file
          </a>

          <p class="repo-owner"><a href="https://github.com/ashbell/blogs"></a> is maintained by <a href="https://github.com/ashbell">ashbell</a>.</p>

          <p>感谢<a href="https://github.com/"> Github </a>的免费提供.</p>
        </aside>
      </div>
    </div>

  
  </body>
</html> 
'''
#========Immovable HTML CODE of index_pagecode  END====================

#=================Python start @ index.html files================
# Two files : tree, path. created by shell cmd: tree, find | sort
#================================================================
reg = '[0-9]{4}-[0-9]{2}-[0-9]{2}'  #use to match the xxxx-xx-xx-article_name.html files.
Ltree = []
Lpath = []
idxpath = 0
index_out = './index.html'
Lque_hyperlk = [] 


Fp_path = open('./path', 'r')
lines = Fp_path.readlines()
for i in lines:
	Lpath.append(i)
Fp_path.close()

Fp_OtIndex = open(index_out, 'w')
Fp_OtIndex.write(index_start)

idx = 0
que_hyperlk.append('None')

Fp_tree = open('./tree', 'r')
lines = Fp_tree.readlines()
for tl in lines:
	m = re.search(reg, tl) 
	tl = str(tl)
	if m is not None: # We find the article html files' path.
		# The HTML in Browser look like this:
		# │   └──    2014-02-24  >>>> THE_ARTICLE_THEME
		#--tl[:18]---date_format------article_theme-----  
		# OK,we convert it  to HTML code:
		# │   ├── 2014-02-24  >>>> <font color="#0000c6"><a href="ARTICLE_PATH">THEMES</a></font>

		pre_arti = tl[:18]
		fmt_date_arti = '%s%s' % (tl[18:28], '  >>>> ')
		arti_html_start = '<font color="#0000c6"><a href="'
		strpath = str(path[idxpath]).replace('\n', '') # do not use replace('\n', '\0'), error.
		ahref_end = '">'
		arti_name = tl[29:-6]
		arti_html_end = '</a></font>'

		arti_html_out = '%s%s%s%s%s%s%s' % (pre_arti, fmt_date_arti, \
			arti_html_start, strpath, ahref_end, arti_name, arti_html_end )
		
		idxpath += 1
		outf.write('%s%s' %(arti_html_out, os.linesep))

		idx += 1

		que_hyperlk.append(strpath)

	else :
		if cmp('./article/\n', tl) == 0: #Oh, fuck, forget the '\n'
						 #cmp('./article/, tl) never equal.
			dir_html_out = tl.replace('\n','')
		else:
			pre_line = tl[:10] 
			html_start = '<font color="#0000cd", style="font-size:100%">'
			dir_name = tl[10:] 
			html_end = '</font>'

			dir_html_out = '%s%s%s%s' % (pre_line, html_start, \
					dir_name.replace('\n', ''), html_end)
		outf.write('%s%s' % (dir_html_out, os.linesep))
		if idx > 0:
			que_hyperlk.append('None') # for [0] [1] `[2]
			for i in range(1, idx + 1):
				f = open(que_hyperlk[i], 'r')
				fp = open('outfile', 'w')
				fread = f.readlines()
				t = 0
				for html_code in fread:
					if re.search("a href=.* class=\"button\"", html_code):
						t += 1
						if t == 1:
							tp = '%s%s%s%s' % ("<a href=\"", que_hyperlk[i-1],"\"", "  class=\"button\">")
					 	if t == 2:
							tp = '%s%s%s%s' % ("<a href=\"", que_hyperlk[i+1],"\"", "  class=\"button\">")
					 		
						print "the ", t, " times match"
					else:
					 	tp = html_code
					fp.write('%s%s' % (tp, os.linesep))
				f.close()
				fp.close()
				
				
			#print "Arti :", que_hyperlk[i]
			#print "Prevage :", que_hyperlk[i-1]," NextPage: ", que_hyperlk[i+1]
		que_hyperlk = [] 
		que_hyperlk.append('None') # for `[0] [1] [2]
		idx = 0

treef.close()
outf.write(index_end)
outf.close()

# ok, finish the index page !












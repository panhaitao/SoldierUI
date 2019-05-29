#!/usr/bin/env python3

import os
import re
import markdown

from flask import Flask
from flask import render_template

app = Flask(__name__)

nav_str='''
        <nav>
          <ol>
            <li><a href=/>深蓝笔记</a></li>
            <li><a href="/about">ABOUT</a></li>     
          </ol>
        </nav>
'''
def list_all_files(rootdir):
    _files = []
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

def get_md_title(filename):
    md_title=""
    with open(filename,'r') as f:
        for line in f:
            md_title=line.replace(" ","").replace("#","").replace("\n","")
            break
    return md_title

def get_md_category(filename):
    return filename.split('/')[2]

def get_md_content(filename):
    content=[]
    with open(filename,'r') as f:
        for line in f:
            if re.match(r'^#',line):
               content.append(line.replace("#","&nbsp;").replace("\n",""))
    return content


@app.route('/')
def index():
    data={ }
    main=""
    category=""
    H2_tmp=[]
    H2=[]
    i=1
    for f in list_all_files("./markdown"):
        title=get_md_title(f)
        category=get_md_category(f)
        data[i]=[category, title, f]
        i+=1
    for k in data.keys():
        H2_tmp.append(data[k][0])
    H2=list(set(H2_tmp))
    print(H2)

    return render_template('index.html', title="首页", page_nav=nav_str,data=data, H2=H2 )

@app.route('/about')
def about():
    main='''
    <a id=个人简介></a>
    <h1> 个人简介</h1>
    <p> 个人简介 xz@onwalk.net</p>
    <hr>

    '''
    content='''
    <ul>
      目录
      </br>
      <hr>
      <li><a href="#个人简介" target="_self" >个人简介</a></li>
    </ul>
    '''
    return render_template('page.html', title="简介", page_nav=nav_str, page_main=main, page_content=content)

@app.route('/<name>')
def page(name):
    data={ }
    content=[]
    i=1
    for f in list_all_files("./markdown"):
        title=get_md_title(f)
        data[i]=[title, f]
        i+=1

    title    = data[int(name)][0]
    filename = data[int(name)][1]
    content  = get_md_content(filename)

    md=open(filename).read()
    exts = ['markdown.extensions.extra','markdown.extensions.tables']
    ret=markdown.markdown(md,extensions=exts)
    return render_template('page.html',title=title, page_nav=nav_str, page_main=ret, content=content)

#!/usr/bin/env python3

import os
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
            md_title=line
            break
    return md_title

@app.route('/')
def index():
    data={ }
    main=""
    content=""
    i=1
    for f in list_all_files("./markdown"):
        title=get_md_title(f)
        data[i]=[title, f]
        i+=1

    return render_template('index.html', title="首页", page_nav=nav_str,data=data)

@app.route('/about')
def about():
    main='''
    <a id=个人简介></a>
    <h1> 个人简介</h1>
    <p> 个人简介 xz@onwalk.net</p>
    <hr>

    <a id=个人简历></a>
    <h1> 个人简历</h1>
    <p> 个人简历 xz@onwalk.net</p>
    <hr>
    '''
    content='''
    <ul>
      目录
      </br>
      <hr>
      <li><a href="#个人简介" target="_self" >个人简介</a></li>
      <li><a href="#个人简历" target="_self" >个人简历</a></li>
    </ul>
    '''
    return render_template('page.html', title="简介", page_nav=nav_str, page_main=main, page_content=content)

@app.route('/<name>')
def page(name):
    data={ }
    i=1
    for f in list_all_files("./markdown"):
        title=get_md_title(f)
        data[i]=[title, f]
        i+=1

    title    = data[int(name)][0]
    filename = data[int(name)][1]

    content='''
            <ul>
	  目录
	  </br>
	  <hr>
	  <li><a href="#议题背景">议题背景</a></li>
	  <li><a href="#主机操作">主机操作</a></li>
          <li><a href="#找出分区占用过大的主机">找出分区占用过大的主机</a></li>
          <li><a href="#查看所有主机运行状态">查看所有主机运行状态</a></li>
	  <li><a href="#为所有主机添加SSH-key">为所有主机添加SSH-key</a></li>
          <li><a href="#集群">集群</a></li>
	  <li><a href="#批量重启集群内所有服务">批量重启集群内所有服务</a></li>
	  <li><a href="#启/停部分节点的日志服务">启/停部分节点的日志服务</a></li>
	  <li><a href="#自动巡检">自动巡检</a></li>
	  <li><a href="#定期巡检k8s集群运行状态">定期巡检k8s集群运行状态</a></li>
	</ul>
    '''
    title=data[int(name)][0]
    filename=data[int(name)][1]
    md=open(filename).read()
    exts = ['markdown.extensions.extra','markdown.extensions.tables']
    ret=markdown.markdown(md,extensions=exts)
    return render_template('page.html',title=title, page_nav=nav_str, page_main=ret, page_content=content)

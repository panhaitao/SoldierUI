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


@app.route('/')
def index():
    main='''
    <a id=现场运维自动化></a>
    <h1> <a href="/test" target="_self" >现场运维自动化</a></li> </h1>
    <p>在客户现场运维的时候，经常面临各种各样的问题，有些甚至是不段重复的机械劳动,这个时候就需要我们想尽办法去偷懒，去达到即快又好的解决问题，又能让自己在客户现场运维的节奏更轻松，更自在些！</p>
    <hr>
    '''
    content='''
    <ul>
      目录
      </br>
      <hr>
      <li><a href="#现场运维自动化" target="_self" >现场运维自动化</a></li>
    </ul>
    '''
    return render_template('page.html', title="首页", page_nav=nav_str, page_main=main, page_content=content)

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

@app.route('/test')
def page():
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
    
    md=open('markdown/k8s-devops.md').read()
    exts = ['markdown.extensions.extra','markdown.extensions.tables']
    ret=markdown.markdown(md,extensions=exts)
    return render_template('page.html',title="现场运维自动化", page_nav=nav_str, page_main=ret, page_content=content)

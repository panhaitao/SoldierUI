# markdown blog

a python flask markdown blog with github repo! 

## HowTO

```
docker pull onwalk/markdownblog
git clone your_markdown_dos_repo /blog/markdown
docker run -d -t -i -v /blog/markdown/:/blog/markdown -p 80:5000 --name MarkdownBlog docker.io/onwalk/markdownblog
```

## Use helm/chart Deploy 

```
git clone https://github.com/panhaitao/charts/
cd charts/charts-for-k8s/
修改 blog/values.yaml 更改path: "/Users/shenlan/workspace/SoldierNote/Archive/" 为实际的路径 path: /xxx/Archive/
helm package blog
helm install blog-0.0.2.tgz  --generate-name
```

# reference

* helm v3 下载地址：<https://github.com/helm/helm/releases> 
* http://www.pythondoc.com/flask/templating.html#id4 

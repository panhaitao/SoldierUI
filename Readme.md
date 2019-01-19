# markdown blog

a python flask markdown blog with github repo! 

## HowTO

```
docker pull onwalk/markdownblog
git clone your_markdown_dos_repo /blog/markdown
docker run -d -t -i -v /blog/markdown/:/blog/markdown -p 80:5000 --name MarkdownBlog docker.io/onwalk/markdownblog
```

# reference

* http://www.pythondoc.com/flask/templating.html#id4 

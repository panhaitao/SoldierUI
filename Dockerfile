FROM alpine:latest
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk --update add python3-dev
RUN mkdir -pv /blog/markdown && cd /blog/ && pip3 install flask markdown
ADD app.py /blog/
ADD templates/ /blog/templates/
ADD static/css/main.css /blog/static/css/
ADD docker-entrypoint.sh /blog

VOLUME ['/blog/markdown/']  
EXPOSE 5000

WORKDIR /blog
ENTRYPOINT ["/blog/docker-entrypoint.sh"]

 


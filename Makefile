docker-run: build-image
	docker run -d -t -i -v /home/shenlan/workspaces/SoldierUI/markdown:/blog/markdown -p 80:5000 --name markdownblog soldierweb 
build-image:
	docker build -t soldierweb:latest .

local-run: install-dev
	flask run --host=0.0.0.0
install-dev:
	pip3 install markdown
	pip3 install flask
clean:
	docker rm markdownblog -f

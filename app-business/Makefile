path = docker

clean:
	docker system prune -a -f

build:
	docker build -f $(path)/Dockerfile --force-rm -t i-app-business .

compose:
	docker-compose up --build -d
stop:
	docker-compose stop

rebuild: clean build

run:
	docker run --rm i-app-business

rerun: rebuild run
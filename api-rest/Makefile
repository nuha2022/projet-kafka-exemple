path = docker

clean:
	docker system prune -a -f

build:
	docker build -f $(path)/Dockerfile --force-rm -t i-api-rest .

compose:
	docker-compose up --build -d
stop:
	docker-compose stop

rebuild: clean build

run:
	docker run --rm -p 9000:8080 i-api-rest

rerun: rebuild run
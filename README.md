# python-docker-assignment

A repository contains python script to take quiz and Dockerfile


### Prerequisities


In order to run this container you'll need docker installed , PFB usefull links.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage
Clone this repository to get started

```shell
git clone https://github.com/sagarhande/python-docker-assignment.git
```
go to the folder

```shell
cd  python-docker-assignment
```

build your image

```shell
docker build -t <put image name> 
```
run your container<br>
_note : -it option is mandatory as we are taking user inpute in our python code_

```shell
docker run -it <put image name> 
```




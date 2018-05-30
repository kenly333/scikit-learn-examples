
docker rmi jupyter-notebook-scipy:1.0
docker build -f dockerfile -t jupyter-notebook-scipy:1.0 .

docker run -it -p 8888:8888 -v /Users/kenly/python-learning:/notebooks jupyter-notebook-scipy:1.0


docker rmi python/anaconda3-jupyter:1.0
docker build -f dockerfile -t python/anaconda3-jupyter:1.0 .

docker run -i -t -p 8888:8888 -v /Users/kenly/python-learning:/notebooks python/anaconda3-jupyter:1.0
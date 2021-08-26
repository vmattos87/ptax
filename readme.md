<h2>install</h2>

Pull docker image
└─$ docker pull vmattos87/ptax-consulta:ptax                          1 ⨯


└─$ docker build --tag ptax


<h2>how to run</h2>

└─$ docker run -ti -v ${PWD}:/app ptax   
└─$ docker run -ti -v ${PWD}:/app vmattos87/ptax-consulta:ptax  







Docker Hub
└─$ docker build -t vmattos87/ptax-consulta:ptax .                                          1 ⨯
└─$ docker login -u "vmattos87" -p "5kYx7eB-~@*H;hZ" docker.io                              1 ⨯
└─$ docker push vmattos87/ptax-consulta:ptax                  
# docker-container-fastapi
A docker container for fastapi

# Create docker image
docker build -t myimage .

# Run docker container
docker run -d --name mycontainer -p 80:80 myimage
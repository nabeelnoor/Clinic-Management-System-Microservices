# start by pulling the python image
FROM python:3.9.7-alpine3.14
ENV PORT 8080
EXPOSE 8080
# by default azure web services, assumes that container is exposing on port 8080, so you have to make your container work on port 8080
# else you have to set WEBSITES_PORT=8000 # where 8000 can be any port number of your choice
# See azure doc for configuration of Port Number for "Azure web services" ----> https://docs.microsoft.com/en-us/azure/app-service/configure-custom-container?pivots=container-linux#configure-port-number

# for proper dockerhub push and containariaztion see this doc --> https://blog.logrocket.com/build-deploy-flask-app-using-docker/

RUN pip install --upgrade pip
# RUN pip install logging
# RUN pip install json
RUN pip install grpcio
RUN pip install flask

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT ["python"]

CMD ["app.py"]
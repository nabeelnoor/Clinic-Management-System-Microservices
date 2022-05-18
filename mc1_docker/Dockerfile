# start by pulling the python image
FROM python:3.9.7-alpine3.14

RUN pip install --upgrade pip
# RUN pip install logging
# RUN pip install json
RUN pip install grpcio
RUN pip install flask
RUN pip install future
RUN pip install pymongo
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
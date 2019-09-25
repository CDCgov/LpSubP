FROM ubuntu:18.04

COPY . /data/
WORKDIR /data/

#RUN apt-get update && \
#    apt-get upgrade -y && \
#    apt-get install -y git
#RUN git clone https://github.com/supark87/coregenescheme.git
RUN apt-get update && apt-get install -y ncbi-blast+=2.6.0-1
RUN apt-get update && apt-get install -y muscle
RUN apt-get install prodigal
RUN apt-get install -y raxml
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.7 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install matplotlib 
#RUN pip3 install pandas==0.23.4
#RUN pip3 install numpy==1.15.0
#RUN pip3 install Cython
RUN pip3 install biopython
RUN pip3 install wheel
RUN pip3 install ipython
#RUN pip3 install scipy==1.1.0
#RUN pip3 install seaborn==0.9.0
RUN pip3 install hdbscan==0.8.13
RUN pip3 install -r /data/requirements1.txt

#CMD ["python3", "/data/pipe.py","/data/test2/"]

ENTRYPOINT ["python3","/data/pipe.py"]
# FROM biocontainers/biocontainers:latest AS build


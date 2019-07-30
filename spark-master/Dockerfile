#Spark Master
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
 wget \
 default-jdk \
 python3 \
 scala && cd /home && mkdir spark && mkdir python-jobs && mkdir jobs-data && cd spark && \
 wget https://archive.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.6.tgz && \
 tar -xvf spark-2.4.3-bin-hadoop2.6.tgz 

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64 
ENV SPARK_HOME /home/spark/spark-2.4.3-bin-hadoop2.6
ENV PYSPARK_PYTHON /usr/bin/python3

ENTRYPOINT ["/home/spark/spark-2.4.3-bin-hadoop2.6/bin/spark-class","org.apache.spark.deploy.master.Master"]
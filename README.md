# iChooseU

# Intro
  This project is being used to study how to build data pipelines and use Big Data technologies, such as Apache Kafka, Apache Spark, Apache Beam and cloud services with GCP and Databricks. Furthemore, I'm using containers to study more about Docker, Docker Compose and then start to learn Kubernetes.
  
# Data source
  As a huge fan of Pokemon franchise, this project uses a free Pokemon API(this explains project's title :D) to get and simulate 'streaming data source' being captured and ingested in a data pipeline.

# Files
  We have three files so far: 
  * consumer_kafka_mongo.py: A simple implementation of a consumer that reads messages from kafka and insert into a MongoDB collection.
  * docker-compose.yml: Configuration file to build Kafka, Zookeeper, MySQL, MongoDB and Spark cluster containers.
  * PokeAPI test producer.ipynb: Python notebook to get PokeAPI data and send to Kafka topic.
  * spark-master/: This folder contains a Dockerfile to build a Spark-master image.
  * spark-worker/: This folder contains a Dockerfile to build a Spark-worker image.
  * jobs-data/: This folder contains sample data to use with jobs.
  * spark-jobs/: This folder contains pyspark jobs to be executed by Spark cluster.
  * mongo-data/: This folder contains data from MongoDB.
  
# Data Pipeline
  * Kafka -> MongoDB  
    This first step consists in read messages from Kafka and stores in MongoDB as backup of PokeAPI's messages.


# TO DO
  This README will be updated as implementations get done. Thus far, the first commit implements a data ingestion into a topic of Kafka's container.
  * <del>Test PokeAPI.</del>
  * <del>Create Kafka container and send messages to it.</del>
  * <del>Create MongoDB container.</del>
  * <del>Read messages from Kafka topic and write in MongoDB.</del>
  * <del>Create MySQL and Spark containers.</del>
  * <del>Test a Spark submit in cluster.</del>
  * Use Spark to do some transformations with data and store in a MySQL table.
  
# References
 * [PokeAPI Documentation](https://pokeapi.co/docs/v2.html)
 * [Kafka Container Documentation](https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html#getting-started-with-docker-compose)
 * [Mongo Documentation](https://docs.mongodb.com/)
 * [Mongo Docker Image Reference](https://hub.docker.com/_/mongo) 
 * [MySQL Image Documentation](https://hub.docker.com/_/mysql)
 * [Setting up Standalone Spark Cluster](https://spark.apache.org/docs/latest/spark-standalone.html)
 

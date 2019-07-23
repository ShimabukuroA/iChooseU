# iChooseU

## Introduction
  This project is being used to study how to build data pipelines and use Big Data technologies, such as Apache Kafka, Apache Spark, Apache Beam and cloud services with GCP and Databricks. Furthemore, I'm using containers to study more about Docker, Docker Compose and then start to learn Kubernetes.
  
## Data source
  As a huge fan of Pokemon franchise, this project uses a free Pokemon API(this explains project's title :D) to get and simulate 'streaming data source' being captured and ingested in a data pipeline.

## Files
  We have three files so far: 
  * consumer.py: A simple implementation of a consumer from Kafka topic.
  * docker-image-kafka/docker-compose.yml: Configuration file to build Kafka and Zookeeper containers.
  * PokeAPI test producer.ipynb: Python notebook to get PokeAPI data and send to Kafka topic.
  
## TO DO
  This README will be updated as implementations get done. Thus far, the first commit implements a data ingestion into a topic of Kafka's container.
  
## References
 * [PokeAPI Documentation](https://pokeapi.co/docs/v2.html)
 * [Kafka Container Documentation](https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html#getting-started-with-docker-compose)

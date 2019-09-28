# Data-Engineering
Masters Project

I.	Introduction:

This project is about creating a pipeline for live Twitter streams of current trending topics. 
The key highlights of this project are: 
1) Generating current trending topics in a location by calling the Twitter API.
2) Extracting live Twitter streams for the chosen topics in a location.
3) Using distributed streaming platform to create, store and ingest collected tweets in the form of messages.
4) Transfer the messages into a MongoDB database.
5) Finding solutions to few business questions on the data that has been ingested into the database.

In the sections below, the procedure required to build and run this pipeline are explained in detail. 

II.	Process Overview

1) Live-Streaming of Tweets:
Using the Twitter API call, we can figure out what are the trending topics in a particular
location. We took the top two trending topics as keywords and collected tweets based on them for a fixed period. The kafka producer then sends these tweets to the Kafka Broker in the form of messages to the topic name we assign to it.
2) Consuming Messages:
All the tweets stored as a topic in the broker are sent in the form of messages to the Kafka consumer.
3) Data Analysis:
Once all the tweets are consumed by the Kafka Consumer, they are to be ingested into the database in JSON format, after which queries can be run in order to find the solution to 5 business problems.

III.	Data Source Used: 

Twitter is an online news & social networking platform on which users or entities known as of ‘Twitter Handles’ interact with each other with messages known as ‘Tweets’. Each tweet can have a maximum of 280 characters. These tweets can be extracted by making a Twitter API call using Python’s Tweepy library. Each tweet structure is embedded in JSON format from which we get various parameters like the Tweeter handle from where it is posted, the tweet content, number of likes and shares, location and source from which it was posted etc. Using these details, we can perform various analysis on tweets or the twitter handle. 


IV.	Tools Utilized:

1) Docker:	Docker is a set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.	We used Docker images of kafka, MongoDb in order to execute various commands to achieve the pipeline.
2) Jupyter Notebook:	Jupyter Notebook is an open-source web application through which we could code, document as well as analyze, all at one place.	Building the entire pipeline, right from extracting tweets to analyzing them.
3) Kafka:	Kafka is a distributed streaming platform through which we could publish, subscribe, store and process streams of
records.	Storing, publishing and consuming streams of tweets collected using Twitter API.
4) MongoDB:	MongoDB is a NoSQL database using which we could store huge amounts of unstructured data and analyze them.	Storing tweets collected by the Kafka consumer and performing analysis on them.


V.	Libraries Utilized:

1.	Tweepy:	Used for accessing Twitter API	--> pip install tweepy
2.	Kafka-Python:	A Python client for the Apache Kafka stream processing system	--> pip install kafka-python
3.	PyMongo:	It contains various tools used for working with MongoDB, a NoSQL database	--> pip install pymongo
4.	Pandas:	An open sourced library which provides easy-to-use data-structures and data analysis tools for Python programming	--> pip install pandas
5.	Matplotlib:	Used for data visualization in a graphical format	--> pip install matplotlib
6.	TextBlob:	Provides a simple API for common natural language processing (NLP) tasks such as sentiment analysis, classification, translation, and more.	--> pip install textblob
7.	Numpy:	Used to handle multidimensional arrays.	--> pip install numpy


VI.	Docker Images Utilized:

"$docker pull imageName"  command can be used to pull an image. The following docker images have been used while creating the pipeline. 
1. Kafka:  Distributed streaming platform through which we could publish, subscribe, store and process streams of records.
2. Zookeeper: Centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.
3. Jupyter Notebook:  IDE used for analysis and visualization of twitter data obtained.
4. MongoDB: This NoSQL database is used to store the twitter data obtained.
5. Kafka-Producer: This is used to push the streaming of tweets from API to kafka Server.
6. Kafka-Consumer: This is used to receive the streaming of tweets from kafka Server and insert into MongoDB.

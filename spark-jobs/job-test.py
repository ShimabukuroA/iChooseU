from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Test job").setMaster("spark://spark-master:7077")
sc = SparkContext(conf=conf)

input = sc.textFile("file:///home/jobs-data/Book.txt")
words = input.flatMap(lambda x: x.split())
wordCount = words.countByValue()

for word, count in wordCount.items():
    cleanWord = word.encode('ascii', 'ignore')
    if(cleanWord):
        print(cleanWord, count)

sc.stop()
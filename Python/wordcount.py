from pyspark import SparkContext

sc = SparkContext("local", "wordcount")
wordfile = sc.textFile("./../README.md")
counts = wordfile.flatMap(lambda line:line.split(" ")).map(lambda word:(word,1)).reduceByKey(lambda a,b:a+b).sortByKey()
for word in counts.collect():
    print word

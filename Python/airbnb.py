from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "airbnb")
sqlContext = SQLContext(sc)
logFile = "./../rooms-part.json"
df = sqlContext.read.json(logFile)
df.registerTempTable("rooms")
df.groupBy("payload.country").count().sort("count").show(300)

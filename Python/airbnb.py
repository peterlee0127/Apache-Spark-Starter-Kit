from pyspark import SparkContext
from pyspark.sql import SQLContext
import pyspark.sql.functions as func

sc = SparkContext("local", "airbnb")
sqlContext = SQLContext(sc)
logFile = "./../rooms-part.json"
df = sqlContext.read.json(logFile)
df.registerTempTable("rooms")
#df.groupBy("payload.country").count().sort("count").show(300)
#price = price.agg(func.avg("calendar")).show(300)
result = sqlContext.sql("select calendar['price'] as prices,id from rooms order by prices")

#result.show(100)
#result = result.agg(func.avg("price"))
#result = result.agg({x:"sum" for x in df.columns})
#print '----------'
#for cal in result.collect():
#    print cal

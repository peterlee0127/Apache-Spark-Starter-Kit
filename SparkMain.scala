import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.rdd._

import java.util.Properties

import org.apache.log4j.Logger
import org.apache.log4j.Level
import org.apache.spark.Logging
import org.apache.spark.storage.StorageLevel

object FoodStoreALS {

  def main(args: Array[String]) {
  
  val textFile = spark.textFile("hdfs://...")
  val counts = textFile.flatMap(line => line.split(" "))
                   .map(word => (word, 1))
                   .reduceByKey(_ + _)
  counts.saveAsTextFile("hdfs://...")
  
  }
}

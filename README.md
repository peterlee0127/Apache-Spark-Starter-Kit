# Spark-SBT
<h3>Starter-kit for Apache Spark</h3>

<h2>Requirement</h2>

<a herf="http://www.scala-sbt.org/download.html">Install SBT</a>

<a herf="http://www.scala-lang.org/download/">Install Scala</a>

<a herf="http://www.oracle.com/technetwork/java/javase/downloads/index.html">Install JDK</a>

<a herf="http://spark.apache.org/downloads.html">Install Spark</a>


	for Spark 1.6.1 and lower, please install scala 2.10 first.

    for Spark 2.0 and later, please install scala 2.11 first.
    
    And install sbt first.
    
   


<hr>

<h3>Config</h3>
	version="0.2"  // your application version
	
	scalaVersion="2.10"
	
	filePath="$PWD"
	
	jarPath=$filePath/target/scala-$scalaVersion/SparkMain-assembly-$version.jar 
	
	Class="SimpleApp"  // Set your Class 
	
	master=master	// master path

<h3>Build</h3>
	./build.sh
	
	
<h3>Deploy</h3>
<h4>Local Mode</h4>
	./startSpark.sh local
<h4>Mesos Mode</h4>
	./startSpark.sh mesos
<h4>Mesos_cluster Mode</h4>
	./startSpark.sh mesos_cluster
<h4>Cluster Mode</h4>
	./startSpark.sh master
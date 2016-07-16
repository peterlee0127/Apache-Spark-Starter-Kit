# Spark-SBT
<h3>Starter-kit for Apache Spark</h3>

<h2>Requirement</h2>

[SBT](http://www.scala-sbt.org/download.html)
for compile and link Scala library.
	
[Scala](http://www.scala-lang.org/download/)
for running Scala program.
	
[Oracle JDK or OpenJDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html")
for Java Development Kit
	
[Apache Spark](http://spark.apache.org/downloads.html")
for Apache Spark

<h2>Environment Setup</h2>
	
   for Spark 1.x	
   
	use scala 2.10.

   for Spark 2.x
   
	use scala 2.11.
    


add PATH Environment to .bashrc or .zshrc
	
	export PATH=/home/user/scala/bin:$PATH
	export PATH=/home/user/sbt/bin:$PATH
	export PATH=/home/user/spark/bin:$PATH
	export PATH=/home/user/spark/sbin:$PATH

<hr>

<h1>Spark Starter-Kit</h1>

<h2>Deploy script Configuration(for Scala only)</h2>
	version="1.0"  // application version
	scalaVersion="2.11"
	filePath="$PWD"	
	jarPath=$filePath/target/scala-$scalaVersion/SparkMain-assembly-$version.jar 
	Class="SimpleApp"  // Set Class 
	master=master	// deploy path

<h3>Build</h3>
	./build.sh
	
<hr>
<h2>Deploy</h2>	
<h4>Local Mode</h4>
	./startSpark.sh local
<h4>Mesos Mode</h4>
	./startSpark.sh mesos
<h4>Mesos_cluster Mode</h4>
	./startSpark.sh mesos_cluster
<h4>Cluster Mode</h4>
	./startSpark.sh master
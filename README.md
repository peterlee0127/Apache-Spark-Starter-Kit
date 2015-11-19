# Spark-SBT
<h3>sbt for Apache Spark</h3>
	./build.sh
	
<h3>Config</h3>
	version="0.2"  // your application version
	scalaVersion="2.10"
	filePath="$PWD"
	jarPath=$filePath/target/scala-$scalaVersion/SparkMain-assembly-$version.jar 
	Class="SimpleApp"  // Set your Class 
	master=master	// master path
	
<h2>Deploy Script</h2>
<h4>Local Mode</h4>
	./startSpark.sh local
<h4>Mesos Mode</h4>
	./startSpark.sh mesos
<h4>Mesos_cluster Mode</h4>
	./startSpark.sh mesos_cluster
<h4>Cluster Mode</h4>
	./startSpark.sh master
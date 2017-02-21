# Here all experiment will go which we will use to optimize spark code
# Sources, stackoverflow(I'll keep updating this)


1. 
Details from spark site - [http://spark.apache.org/docs/latest/sql-programming-guide.html]
property - spark.sql.autoBroadcastJoinThreshold 	
default_value - 10485760 (10 MB) 	
description - Configures the maximum size in bytes for a table that will be broadcast to all worker nodes when performing a join. 
              By setting this value to -1 broadcasting can be disabled. 
              Note that currently statistics are only supported for Hive Metastore tables 
              where the command ANALYZE TABLE <tableName> COMPUTE STATISTICS noscan has been run. 
Han't tried it but since stats are only available in Hive, I am not sure, If I am not to test.

      
2.
I got this pretty interesting link - [http://blog.hydronitrogen.com/2016/05/13/shuffle-free-joins-in-spark-sql/], reagarding
reducing shuffling and getting query execution plan.
I'll update the result once I'll test it against 500GB of data set

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

      
2.

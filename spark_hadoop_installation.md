# Quick guide to install hadoop #
Open up your teminal and run the following commands

## Generate ssh key ##
``` ssh-keygen -t rsa -P "" ```

This will generate the key without any password. You can provide the password if you want, but then everytime you need to enter the password when hadoop daemon’s starts.

``` cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys ```

This will save the newly generate key to your ssh authorized keys.

``` ssh localhost ```
```
Output
--- Last login: Mon Mar 13 18:09:18 2017 from ::1 
```

If you see the above output, you are all set to install hadoop

### Note: ###
On ubuntu, I haven’t got any error on ssh but on MAC I was not able to do ssh, so if you too are not able to run above command. On MAC, follow the instruction to resolve this problem:
`Source:`  http://stackoverflow.com/questions/17335728/connect-to-host-localhost-port-22-connection-refused

## Installation ##

Create a dicrectory where you will put hadoop, spark and other big data tech like druid, cassandra etc.
For this tutorial, I have created a directory `bigdata_dir`, inside which I will be creating two folders for `hadoop` and `spark`

## Installation: hadoop-2.7.3 ##
`Hadoop Download:` http://hadoop.apache.org/releases.html and click on 2.7.3 binary tarball.

1. Create a hadoop folder inside `bigdata_dir` and copy the hadoop tarball
```
cp ../../downloads/hadoop-2.7.3.tar.gz ./
```

2. Untar hadoop:
```
tar -xvzf hadoop-2.7.3.tar.gz`
rm hadoop-2.7.3.tar.gz
```

3. Add the hadoo path in you `bashrc` or `bash_profile`,
```
export HADOOP_HOME=/Users/udayshankarsingh/Documents/work/personnel/bigdata_dir/hadoop-2.7.3
export PATH=$PATH:$HADOOP_HOME/bin
```

### Configuring hadoop files  ###
1. Edit your `core-site.xml`. Copy and Paste the following:
```
<property>
  <name>hadoop.tmp.dir</name>
  <value>/tmp/hadoop_tmp_dir</value>
  <description>A base for other temporary directories.</description>
</property>

<property>
  <name>fs.default.name</name>
  <value>hdfs://localhost:54310</value>
  <description>The name of the default file system.  A URI whose
  scheme and authority determine the FileSystem implementation.  The
  uri's scheme determines the config property (fs.SCHEME.impl) naming
  the FileSystem implementation class.  The uri's authority is used to
  determine the host, port, etc. for a filesystem.
  </description>
</property>
```

2. Edit your `hdfs-site.xml` and add the following, it will set the replication factor to 1 which by defualt is 3:

```
<property>
  <name>dfs.replication</name>
  <value>1</value>
  <description>Default block replication.
  The actual number of replications can be specified when the file is created.
  The default is used if replication is not specified in create time.
  </description>
</property>
```

3. Copy `mapred-site.xml.template` to `mapred-site.xml`
```
cp mapred-site.xml.template mapred-site.xml
```
4. Edit `mapred-site.xml` and add the following
```
<property>
  <name>mapred.job.tracker</name>
  <value>localhost:54311</value>
  <description>The host and port that the MapReduce job tracker runs
  at.  If "local", then jobs are run in-process as a single map
  and reduce task.
  </description>
</property>
```

### Bash file update ###
1. Update your `bashrc/bash_profile` to:
```
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

2. Adding `$HADOOP_HOME/sbin` to `bash_profile` file, so we don’t have to go to `hadoop` `sbin` folder everytime to start hadoop.

3. `Source` you `bash_profile` to load the changes we just made
```
source ~/.bash_profile
```
4. To check if everything is done properly
Type `start` and `press tab twice`. All hadoop commands mentioned below should be avilable
```
start-all.cmd
start-dfs.cmd
start-yarn.cmd
start-all.sh
start-dfs.sh
start-yarn.sh
start-balancer.sh
start-secure-dns.sh
startx
```

### Starting hadoop daemons ###
1.  Let's `Format namenode` via running the command:
```
hdfs namenode -format
```

2. Now, to `start hadoop`,
i. To start `SecondaryNameNode`, `NameNode` and `DataNode`
```
start-dfs.sh
```
ii. To start `NodeManager` and `ResouceManager`
```
start-yarn.sh
```

3. To `stop hadoop`,
i. To stop `SecondaryNameNode`, `NameNode` and `DataNode`
```
stop-dfs.sh
```
ii. To stop `NodeManager` and `ResouceManager`
```
stop-yarn.sh
```

# `NOTE:` #
Earlier we used to run `start-all.sh` to start all the hadoop daemon’s at once, and to stop hadoop we used to run `stop-all.sh`, both of these commands are deprecated now.

## `To Check:` ##
Run command:
```
jps
```
and if you see all the 5 daemons that we have started earlier, we are done with hadoop installation.

## `WEB UI:` ##

Web UIs for the Common User
The default Hadoop ports are as follows:

#### HDFS ####
```
 	Daemon	               Default Port	    Configuration Parameter
    Namenode	             50070	    dfs.http.address
    Datanodes	             50075	    dfs.datanode.http.address
    Secondarynamenode        50090	    dfs.secondary.http.address
    Backup/Checkpoint node?  50105	    dfs.backup.http.address
``` 
`? Replaces secondarynamenode in 0.21.`

#### MR ####

```
    Daemon	         Default Port	    Configuration Parameter
    Jobracker	       50030	    mapred.job.tracker.http.address
    Tasktrackers	   50060        mapred.task.tracker.http.address
```

*`source`: http://blog.cloudera.com/blog/2009/08/hadoop-default-ports-quick-reference/



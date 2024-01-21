# How To Run (Windows)

1. Download and install _Java 8_:
    * Add an environment variable `JAVA_HOME` with a path to your JDK folder, f.e. `C:\Program Files\Java\jdk-1.8`.
    * Add a new _path_ variable `%JAVA_HOME%\bin`.
2. Download and install _Spark 3.5_:
    * Add an environment variable `SPARK_HOME` with a path to your JDK folder, f.e. `C:\Spark\spark-3.5.0-bin-hadoop3`.
    * Add a new _path_ variable `%SPARK_HOME%\bin`.
3. Download and install _Hadoop 3.3.5_:
    * Download corresponding _Hadoop_ version from _[Github](https://github.com/cdarlint/winutils/tree/master)_. 
    * Add an environment variable `HADOOP_HOME` with a path to your JDK folder, f.e. `C:\Hadoop\hadoop-3.3.5`.
    * Add a new _path_ variable `%HADOOP_HOME%\bin`.
4. Install _Python 3.11_.
5. Install _Spark NLP_:
    * `> pip install numpy`
    * `> pip install pyspark`
    * `> pip install spark-nlp`
6. Run the program `> python main.py 'source.json' 'results.json'` where arguments are the following:

|Argument      |Required|Description                |Comment|
|--------------|--------|---------------------------|-------|
|main.py       |Yes     |Path to the executable file|
|'source.json' |Yes     |Source of analyzed messages|Enter the parameter in quotes to preserve the file extension
|'results.json'|No      |Results file               |Enter the parameter in quotes to preserve the file extension. If the file does not exist, it will be created.
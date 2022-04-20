

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext


data_file = "/tmp/pg_catalog.csv"

scSpark = spark.builder.appName("reading csv").config("spark.jars", "/tmp/postgresql-42.3.4.jar").config("spark.driver.extraClassPath", "/tmp/postgresql-42.3.4.jar").getOrCreate()
sdfData = spark.read.option("delimiter", ",").option("header", "true").option("multiLine", "true").csv(data_file)
sdfData.createOrReplaceTempView("catalog")
output=scSpark.sql('SELECT * from catalog WHERE Language ="es" ')
output.show()

output.write.format('jdbc').option("url", "jdbc:postgresql://localhost:5432/databasename").option("dbtable", "tablename").option("user", "username").option("password", "password").option("driver", "org.postgresql.Driver").mode('append').save()
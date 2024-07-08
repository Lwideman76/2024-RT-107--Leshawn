from pyspark.sql import SparkSession
from pyspark.sql.functions import 

# Step 1: Create Spark session
spark = SparkSession.builder \
    .appName("Real-Time Healthcare Data Processing") \
    .getOrCreate()

# Step 2: Define schema for the patient data
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("patient_id", StringType(), True),
    StructField("heart_rate", IntegerType(), True),
    StructField("blood_pressure", IntegerType(), True),
    StructField("timestamp", StringType(), True)
])

# Step 3: Read streaming data
df = spark.readStream \
    .format("csv") \
    .schema(schema) \
    .option("header", "true") \
    .load("C:/Users/Learner_9ZH3Z104/Downloads/chembl_34.fa/chembl_34.fa")

# Step 4: Process the data (e.g., filter patients with high heart rate)
processed_df = df.filter(col("heart_rate") > 100)

# Step 5: Write the processed data to the console
query = processed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()


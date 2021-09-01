from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("MoviesFreq").getOrCreate()

data = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("file:///F:/BioProject/Harmonized_Instrument_Data-002.csv")

def get_subsample(stimulus):
# stimulus = "Beats2014"
    subset = data.filter(data.StimName == stimulus)
    file_path = "F:\\BioProject\\Subsamples\\" + stimulus

    subset.coalesce(1).write.option("header", True).option("delimiter", ",").csv(file_path)

for stimulus in ["DumbTo", "Ouija"] :
    get_subsample(stimulus)

spark.stop()
from __future__ import print_function

import sys
from random import random
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    spark = SparkSession\
        .builder\
        .appName("PythonPi")\
        .getOrCreate()

    words = 'the quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog'
    seq = words.split()
    
    data = spark.sparkContext.parallelize(seq)
    
    counts = data.map(lambda word: (word, 1))
    
    counts = counts.reduceByKey(lambda a, b: a + b)
    
    counts = counts.collect()
    
    print(f"THE RESULT IS: {dict(counts)}")
     
    spark.stop()
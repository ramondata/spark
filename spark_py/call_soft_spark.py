#!/usr/bin/env python3

# important imports

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("nome_do_app") \
    .getOrCreate()


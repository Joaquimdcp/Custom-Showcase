from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch(hosts=['http://elasticsearch:9200'])

with open('data/catalog_image.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='data', doc_type='catalog-image')
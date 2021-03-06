#!/usr/bin/env bash

elasticdump --limit 5000 --concurrency 4 --overwrite \
  --input=http://127.0.0.1:9200/movies \
  --output=./movies_mapping.json \
  --type=mapping
elasticdump --limit 5000 --concurrency 4 --overwrite \
  --input=http://127.0.0.1:9200/movies \
  --output=./movies.json \
  --type=data

elasticdump --limit 5000 --concurrency 4 --overwrite \
  --input=http://127.0.0.1:9200/books \
  --output=./books_mapping.json \
  --type=mapping
elasticdump --limit 5000 --concurrency 4 --overwrite \
  --input=http://127.0.0.1:9200/books \
  --output=./books.json \
  --type=data

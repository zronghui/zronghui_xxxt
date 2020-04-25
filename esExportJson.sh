#!/usr/bin/env bash

elasticdump \
  --input=http://127.0.0.1:9200/movies \
  --output=./movies_mapping.json \
  --type=mapping
elasticdump \
  --input=http://127.0.0.1:9200/movies \
  --output=./movies.json \
  --type=data

elasticdump \
  --input=http://127.0.0.1:9200/books \
  --output=./books_mapping.json \
  --type=mapping
elasticdump \
  --input=http://127.0.0.1:9200/books \
  --output=./books.json \
  --type=data

#!/usr/bin/env bash

rsync -azvhP root@47.93.53.47:/root/code/zronghui_xxxt/movies.json data/
rsync -azvhP root@47.93.53.47:/root/code/zronghui_xxxt/books.json data/
rsync -azvhP root@47.93.53.47:/root/code/zronghui_xxxt/movies_mapping.json data/
rsync -azvhP root@47.93.53.47:/root/code/zronghui_xxxt/books_mapping.json data/

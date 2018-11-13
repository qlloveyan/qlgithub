#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : elasticsearch.py
# @Author: QUANLI
# @Date  : 2018/11/12 15:06
# @Desc  : python 操作elasticsearch学习
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=[{"host": "127.0.0.1", "port": 19200}])

doc = {
    'author': 'quanli',
    'text': 'my first docker elasticsearch example!',
    'timestamp': datetime.now(),
}

res = es.index(index='first-index', doc_type='tweet', id=1, body=doc)
print(res['result'])

res = es.get(index='first-index', id=1, doc_type='tweet')
print(res['_source'])

es.indices.refresh(index='first-index')
res = es.search(index="first-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
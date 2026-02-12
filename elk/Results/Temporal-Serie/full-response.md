# QUERY
```json
GET newsapi-*/_search
{
  "size": 0,
  "aggs": {
    "articles_over_time": {
      "date_histogram": {
        "field": "@timestamp",
        "calendar_interval": "day"
      }
    }
  }
}
```

# RESPONSE
``` json
{
  "took": 49,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 617,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "articles_over_time": {
      "buckets": [
        {
          "key_as_string": "2026-02-06T00:00:00.000Z",
          "key": 1770336000000,
          "doc_count": 296
        },
        {
          "key_as_string": "2026-02-07T00:00:00.000Z",
          "key": 1770422400000,
          "doc_count": 0
        },
        {
          "key_as_string": "2026-02-08T00:00:00.000Z",
          "key": 1770508800000,
          "doc_count": 0
        },
        {
          "key_as_string": "2026-02-09T00:00:00.000Z",
          "key": 1770595200000,
          "doc_count": 0
        },
        {
          "key_as_string": "2026-02-10T00:00:00.000Z",
          "key": 1770681600000,
          "doc_count": 0
        },
        {
          "key_as_string": "2026-02-11T00:00:00.000Z",
          "key": 1770768000000,
          "doc_count": 321
        }
      ]
    }
  }
}
```

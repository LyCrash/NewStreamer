# QUERY
```json
GET newsapi-*/_search
{
  "size": 0,
  "aggs": {
    "articles_by_author": {
      "terms": {
        "field": "author.keyword",
        "size": 5,
        "order": {
          "_count": "desc"
        }
      }
    }
  }
}
```
# RESPONSE

```json
{
  "took": 122,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 584,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "articles_by_author": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 497,
      "buckets": [
        {
          "key": "contact@airbyte.io",
          "doc_count": 21
        },
        {
          "key": "GlobeNewswire",
          "doc_count": 8
        },
        {
          "key": "AstuteAnalytica India Pvt. Ltd.",
          "doc_count": 7
        },
        {
          "key": "Business Wire",
          "doc_count": 6
        },
        {
          "key": "Research and Markets",
          "doc_count": 6
        }
      ]
    }
  }
}
```
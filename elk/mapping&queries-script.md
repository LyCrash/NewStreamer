### Check current indices
```json
GET _cat/indices?v
```

## CONFIGURATION STEP - MAPPING 

Define a template (mapping) that applies to all newsapi-* indices.

```json
PUT _index_template/newsapi_template
{
  "index_patterns": ["newsapi-*"],
  "template": {
    "settings": {
      "number_of_shards": 1,
      "analysis": {
        "filter": {
          "autocomplete_filter": {
            "type": "edge_ngram",
            "min_gram": 1,
            "max_gram": 20
          }
        },
        "analyzer": {
          "autocomplete": {
            "type": "custom",
            "tokenizer": "standard",
            "filter": [
              "lowercase",
              "autocomplete_filter"
            ]
          }
        }
      }
    },
    "mappings": {
      "properties": {
        "@timestamp": {
          "type": "date"
        },
        "created_at": {
          "type": "date",
          "format": "yyyy-MM-dd HH:mm:ss"
        },
        "published_at": {
          "type": "date"
        },
        "source": {
          "type": "keyword"
        },
        "author": {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword"
            }
          }
        },
        "title": {
          "type": "text",
          "analyzer": "standard",
          "fields": {
            "autocomplete": {
              "type": "text",
              "analyzer": "autocomplete"
            }
          }
        },
        "description": {
          "type": "text",
          "analyzer": "standard"
        },
        "content": {
          "type": "text",
          "analyzer": "standard"
        },
        "url": {
          "type": "keyword"
        }
      }
    }
  }
}
```

Templates apply only to new indices. So we need to delete previous indices and restart logstash as well `docker restard logstash`

To Enable wildcard deletion
```json
PUT /_cluster/settings
{
  "transient": {
    "action.destructive_requires_name": false
  }
}
```
```json
DELETE newsapi-*
```

Check the indices template
```json
GET /newsapi-2026.02
```


## QUERYING STEP 

### 1. Requête textuelle (full-text search)
Find articles talking about artificial intelligence
```json
GET newsapi-*/_search
{
  "query": {
    "multi_match": {
      "query": "artificial intelligence",
      "fields": ["title", "description", "content"]
    }
  }
}
```

### 2. Requête avec agrégation
Number of articles per source
```json
GET newsapi-*/_search
{
  "size": 0,
  "aggs": {
    "articles_by_source": {
      "terms": {
        "field": "source.keyword", // il faut mettre un keyword
        "size": 10
      }
    }
  }
}
```


### 3. Requête N-gram
Match partial words like "techn" → technology
```json
GET newsapi-*/_search
{
  "query": {
    "match": {
      "title.autocomplete": {
        "query": "techn"
      }
    }
  }
}
```
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
### 4. Requête floue (fuzzy search)
Typo-tolerant search (e.g. "artifical inteligence")
```json
GET newsapi-*/_search
{
  "query": {
    "match": {
      "title": {
        "query": "artifical inteligence",
        "fuzziness": "AUTO"
      }
    }
  }
}
```
### fetch all contents that contains the word business or close to it
GET newsapi-2026.02/_search
{
  "query": {
    "fuzzy": {
      "content": {"value":"buiness",
        "fuzziness": 2
      }
    }
  }
}

### 5. Série temporelle
Number of articles per day
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



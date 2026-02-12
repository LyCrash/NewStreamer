# QUERY
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

# REPONSE
```json
{
  "took": 75,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 19,
      "relation": "eq"
    },
    "max_score": 9.827233,
    "hits": [
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.globenewswire.com/news-release/2026/02/06/3233884/0/en/Global-AI-in-Hospital-Operations-Market-Set-to-Surge-to-USD-25-70-Billion-by-2030-MarketsandMarkets.html",
        "_score": 9.827233,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "GlobeNewswire",
          "content": "Delray Beach, FL, Feb. 06, 2026 (GLOBE NEWSWIRE) -- The Global AI in hospital operations market is projected to reach USD 25.70 billion by 2030 from USD 7.51 billion in 2025, at a CAGR of 27.9% from … [+12192 chars]",
          "author": "MarketsandMarkets Research Pvt. Ltd.",
          "event": {
            "original": """{"created_at": "2026-02-07 15:34:52", "source": "GlobeNewswire", "author": "MarketsandMarkets Research Pvt. Ltd.", "title": "Global AI in Hospital Operations Market Set to Surge to USD 25.70 Billion by 2030 | MarketsandMarkets\u2122", "description": "Strategic Deployment of Artificial Intelligence Technologies Enables Healthcare Systems to Address Staffing Crises, Administrative Burden, and Cost Pressures While Enhancing Patient Care Delivery Strategic Deployment of Artificial Intelligence Technologies En\u2026", "url": "https://www.globenewswire.com/news-release/2026/02/06/3233884/0/en/Global-AI-in-Hospital-Operations-Market-Set-to-Surge-to-USD-25-70-Billion-by-2030-MarketsandMarkets.html", "published_at": "2026-02-06T14:30:00Z", "content": "Delray Beach, FL, Feb. 06, 2026 (GLOBE NEWSWIRE) -- The Global AI in hospital operations market is projected to reach USD 25.70 billion by 2030 from USD 7.51 billion in 2025, at a CAGR of 27.9% from \u2026 [+12192 chars]"}"""
          },
          "published_at": "2026-02-06T14:30:00Z",
          "@version": "1",
          "created_at": "2026-02-07 15:34:52",
          "title": "Global AI in Hospital Operations Market Set to Surge to USD 25.70 Billion by 2030 | MarketsandMarkets™",
          "url": "https://www.globenewswire.com/news-release/2026/02/06/3233884/0/en/Global-AI-in-Hospital-Operations-Market-Set-to-Surge-to-USD-25-70-Billion-by-2030-MarketsandMarkets.html",
          "@timestamp": "2026-02-06T14:30:00.000Z",
          "description": "Strategic Deployment of Artificial Intelligence Technologies Enables Healthcare Systems to Address Staffing Crises, Administrative Burden, and Cost Pressures While Enhancing Patient Care Delivery Strategic Deployment of Artificial Intelligence Technologies En…"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://blogs.cisco.com/?p=485392",
        "_score": 9.146467,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Cisco.com",
          "content": "The modern airport is a complex ecosystem, constantly striving to balance efficiency, security, and an exceptional customer experience. As passenger volumes continue to rise, Artificial Intelligence … [+11647 chars]",
          "author": "Kyle Barnes",
          "event": {
            "original": """{"created_at": "2026-02-07 15:24:50", "source": "Cisco.com", "author": "Kyle Barnes", "title": "Soaring to New Heights: How AI is Redefining the Airport Customer Experience", "description": "Learn more about how artificial intelligence (AI) is changing every aspect of air travel.", "url": "https://blogs.cisco.com/?p=485392", "published_at": "2026-02-06T14:00:14Z", "content": "The modern airport is a complex ecosystem, constantly striving to balance efficiency, security, and an exceptional customer experience. As passenger volumes continue to rise, Artificial Intelligence \u2026 [+11647 chars]"}"""
          },
          "published_at": "2026-02-06T14:00:14Z",
          "@version": "1",
          "created_at": "2026-02-07 15:24:50",
          "title": "Soaring to New Heights: How AI is Redefining the Airport Customer Experience",
          "url": "https://blogs.cisco.com/?p=485392",
          "@timestamp": "2026-02-06T14:00:14.000Z",
          "description": "Learn more about how artificial intelligence (AI) is changing every aspect of air travel."
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.globenewswire.com/news-release/2026/02/11/3236359/0/en/AI-Inc-Stacks-Advisory-Board-With-Top-Tech-and-Media-Execs.html",
        "_score": 7.335775,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "GlobeNewswire",
          "title": "AI Inc. Stacks Advisory Board With Top Tech and Media Execs",
          "author": "AI Inc.",
          "content": "San Francisco, CA, Feb. 11, 2026 (GLOBE NEWSWIRE) -- Authentic Interactions, known as AI Inc., today announced the addition of four high-impact advisors to its leadership bench: Adam Cheyer, co-found… [+3721 chars]",
          "@version": "1",
          "created_at": "2026-02-12 15:18:38",
          "url": "https://www.globenewswire.com/news-release/2026/02/11/3236359/0/en/AI-Inc-Stacks-Advisory-Board-With-Top-Tech-and-Media-Execs.html",
          "event": {
            "original": """{"created_at": "2026-02-12 15:18:38", "source": "GlobeNewswire", "author": "AI Inc.", "title": "AI Inc. Stacks Advisory Board With Top Tech and Media Execs", "description": "New advisors to Artificial Intelligence leader AI Inc. include a Siri co-founder, a Pluto TV co-founder and former Paramount+ CEO and the former CEO of RED", "url": "https://www.globenewswire.com/news-release/2026/02/11/3236359/0/en/AI-Inc-Stacks-Advisory-Board-With-Top-Tech-and-Media-Execs.html", "published_at": "2026-02-11T14:03:00Z", "content": "San Francisco, CA, Feb. 11, 2026 (GLOBE NEWSWIRE) -- Authentic Interactions, known as AI Inc., today announced the addition of four high-impact advisors to its leadership bench: Adam Cheyer, co-found\u2026 [+3721 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:03:00.000Z",
          "description": "New advisors to Artificial Intelligence leader AI Inc. include a Siri co-founder, a Pluto TV co-founder and former Paramount+ CEO and the former CEO of RED",
          "published_at": "2026-02-11T14:03:00Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.prnewswire.co.uk/news-releases/mondevita-completes-acquisition-of-caruso-302681360.html",
        "_score": 7.2609644,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "PR Newswire UK",
          "content": """ITTIKAR, Mondevo Group's AI-native merchant bank, served as exclusive advisor, deploying proprietary artificial intelligence across due diligence and execution.
ABU DHABI, United Arab Emirates and M… [+5021 chars]""",
          "author": null,
          "event": {
            "original": """{"created_at": "2026-02-07 15:34:52", "source": "PR Newswire UK", "author": null, "title": "MondeVita Completes Acquisition of Caruso", "description": "ITTIKAR, Mondevo Group's AI-native merchant bank, served as exclusive advisor, deploying proprietary artificial intelligence across due diligence and execution. ABU DHABI, United Arab Emirates and MILAN, Feb. 6, 2026 /PRNewswire/ -- MondeVita, the lifestyle a\u2026", "url": "https://www.prnewswire.co.uk/news-releases/mondevita-completes-acquisition-of-caruso-302681360.html", "published_at": "2026-02-06T14:15:00Z", "content": "ITTIKAR, Mondevo Group's AI-native merchant bank, served as exclusive advisor, deploying proprietary artificial intelligence across due diligence and execution.\r\nABU DHABI, United Arab Emirates and M\u2026 [+5021 chars]"}"""
          },
          "published_at": "2026-02-06T14:15:00Z",
          "@version": "1",
          "created_at": "2026-02-07 15:34:52",
          "title": "MondeVita Completes Acquisition of Caruso",
          "url": "https://www.prnewswire.co.uk/news-releases/mondevita-completes-acquisition-of-caruso-302681360.html",
          "@timestamp": "2026-02-06T14:15:00.000Z",
          "description": "ITTIKAR, Mondevo Group's AI-native merchant bank, served as exclusive advisor, deploying proprietary artificial intelligence across due diligence and execution. ABU DHABI, United Arab Emirates and MILAN, Feb. 6, 2026 /PRNewswire/ -- MondeVita, the lifestyle a…"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://siliconangle.com/2026/02/06/portal26-targets-weak-enterprise-ai-returns-new-value-realization-platform/",
        "_score": 7.168615,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "SiliconANGLE News",
          "content": "Generative artificial intelligence security startup Portal26 Inc. today announced a new AI Value Realization solution aimed at helping enterprises close the widening gap between heavy generative AI i… [+3612 chars]",
          "author": "Duncan Riley",
          "event": {
            "original": """{"created_at": "2026-02-07 15:24:50", "source": "SiliconANGLE News", "author": "Duncan Riley", "title": "Portal26 targets weak enterprise AI returns with new Value Realization platform", "description": "Generative artificial intelligence security startup Portal26 Inc. today announced a new AI Value Realization solution aimed at helping enterprises close the widening gap between heavy generative AI investment and weak returns. The AI Value Realization module \u2026", "url": "https://siliconangle.com/2026/02/06/portal26-targets-weak-enterprise-ai-returns-new-value-realization-platform/", "published_at": "2026-02-06T14:00:31Z", "content": "Generative artificial intelligence security startup Portal26 Inc. today announced a new AI Value Realization solution aimed at helping enterprises close the widening gap between heavy generative AI i\u2026 [+3612 chars]"}"""
          },
          "published_at": "2026-02-06T14:00:31Z",
          "@version": "1",
          "created_at": "2026-02-07 15:24:50",
          "title": "Portal26 targets weak enterprise AI returns with new Value Realization platform",
          "url": "https://siliconangle.com/2026/02/06/portal26-targets-weak-enterprise-ai-returns-new-value-realization-platform/",
          "@timestamp": "2026-02-06T14:00:31.000Z",
          "description": "Generative artificial intelligence security startup Portal26 Inc. today announced a new AI Value Realization solution aimed at helping enterprises close the widening gap between heavy generative AI investment and weak returns. The AI Value Realization module …"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://socialnomics.net/2026/02/11/who-is-the-best-ai-keynote-speaker/",
        "_score": 7.0785837,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Socialnomics.net",
          "title": "Who Is the Best AI Keynote Speaker?",
          "author": "Gaby Allegues",
          "content": "The best AI keynote speaker is someone who can explain artificial intelligence clearly, connect it to leadership and real business outcomes, and inspire actionwithout overwhelming the audience with t… [+3265 chars]",
          "@version": "1",
          "created_at": "2026-02-12 15:18:38",
          "url": "https://socialnomics.net/2026/02/11/who-is-the-best-ai-keynote-speaker/",
          "event": {
            "original": """{"created_at": "2026-02-12 15:18:38", "source": "Socialnomics.net", "author": "Gaby Allegues", "title": "Who Is the Best AI Keynote Speaker?", "description": "Who Is the Best AI Keynote Speaker? The best AI keynote speaker is someone who can\u00a0explain artificial intelligence clearly,\u00a0connect it to leadership and real business outcomes, and\u00a0inspire action\u2014without overwhelming the audience with technical jargon. For or\u2026", "url": "https://socialnomics.net/2026/02/11/who-is-the-best-ai-keynote-speaker/", "published_at": "2026-02-11T14:00:17Z", "content": "The best AI keynote speaker is someone who can\u00a0explain artificial intelligence clearly,\u00a0connect it to leadership and real business outcomes, and\u00a0inspire actionwithout overwhelming the audience with t\u2026 [+3265 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:00:17.000Z",
          "description": "Who Is the Best AI Keynote Speaker? The best AI keynote speaker is someone who can explain artificial intelligence clearly, connect it to leadership and real business outcomes, and inspire action—without overwhelming the audience with technical jargon. For or…",
          "published_at": "2026-02-11T14:00:17Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://economictimes.indiatimes.com/tech/artificial-intelligence/the-dark-side-of-ai-weighs-on-the-stock-market/articleshow/128004564.cms",
        "_score": 7.0785837,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "published_at": "2026-02-06T18:30:52Z",
          "@version": "1",
          "source": "The Times of India",
          "title": "The dark side of AI weighs on the stock market",
          "event": {
            "original": """{"created_at": "2026-02-07 19:32:56", "source": "The Times of India", "author": "Joe Rennison, Mike Isaac", "title": "The dark side of AI weighs on the stock market", "description": "A washout hit software stocks as Wall Street realised the threat from artificial intelligence had arrived. New tools from a San Francisco startup triggered a sudden reckoning, pushing investors to sell. The sell-off dragged the broader market lower, briefly t\u2026", "url": "https://economictimes.indiatimes.com/tech/artificial-intelligence/the-dark-side-of-ai-weighs-on-the-stock-market/articleshow/128004564.cms", "published_at": "2026-02-06T18:30:52Z", "content": "A washout in the stocks of software companies has been flowing through Wall Street this week, as investors realized the threat that artificial intelligence will displace businesses had arrived.While \u2026 [+6632 chars]"}"""
          },
          "author": "Joe Rennison, Mike Isaac",
          "created_at": "2026-02-07 19:32:56",
          "description": "A washout hit software stocks as Wall Street realised the threat from artificial intelligence had arrived. New tools from a San Francisco startup triggered a sudden reckoning, pushing investors to sell. The sell-off dragged the broader market lower, briefly t…",
          "@timestamp": "2026-02-06T18:30:52.000Z",
          "url": "https://economictimes.indiatimes.com/tech/artificial-intelligence/the-dark-side-of-ai-weighs-on-the-stock-market/articleshow/128004564.cms",
          "content": "A washout in the stocks of software companies has been flowing through Wall Street this week, as investors realized the threat that artificial intelligence will displace businesses had arrived.While … [+6632 chars]"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://siliconangle.com/2026/02/11/apptronik-raises-520m-ramp-humanoid-apollo-robot-commercial-deployments/",
        "_score": 6.9907866,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "SiliconANGLE News",
          "title": "Apptronik raises $520M to produce humanoid Apollo robot commercial deployments",
          "author": "Kyt Dotson",
          "content": "Apptronik Inc., the maker of artificial intelligence-powered humanoid robots, today announced it has raised $520 million more in early-stage funding, bringing the total capital raised by the company … [+3977 chars]",
          "@version": "1",
          "created_at": "2026-02-12 15:18:38",
          "url": "https://siliconangle.com/2026/02/11/apptronik-raises-520m-ramp-humanoid-apollo-robot-commercial-deployments/",
          "event": {
            "original": """{"created_at": "2026-02-12 15:18:38", "source": "SiliconANGLE News", "author": "Kyt Dotson", "title": "Apptronik raises $520M to produce humanoid Apollo robot commercial deployments", "description": "Apptronik Inc., the maker of artificial intelligence-powered humanoid robots, today announced it has raised $520 million more in early-stage funding, bringing the total capital raised by the company to nearly $1 billion. The Series A-X extension round follows\u2026", "url": "https://siliconangle.com/2026/02/11/apptronik-raises-520m-ramp-humanoid-apollo-robot-commercial-deployments/", "published_at": "2026-02-11T14:00:31Z", "content": "Apptronik Inc., the maker of artificial intelligence-powered humanoid robots, today announced it has raised $520 million more in early-stage funding, bringing the total capital raised by the company \u2026 [+3977 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:00:31.000Z",
          "description": "Apptronik Inc., the maker of artificial intelligence-powered humanoid robots, today announced it has raised $520 million more in early-stage funding, bringing the total capital raised by the company to nearly $1 billion. The Series A-X extension round follows…",
          "published_at": "2026-02-11T14:00:31Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://siliconangle.com/2026/02/06/augment-code-makes-semantic-coding-capability-available-ai-agent/",
        "_score": 6.9907866,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "published_at": "2026-02-06T18:00:15Z",
          "@version": "1",
          "source": "SiliconANGLE News",
          "title": "Augment Code makes its semantic coding capability available for any AI agent",
          "event": {
            "original": """{"created_at": "2026-02-07 19:32:56", "source": "SiliconANGLE News", "author": "Kyt Dotson", "title": "Augment Code makes its semantic coding capability available for any AI agent", "description": "Augment Computing Inc., the maker of an agentic artificial intelligence coding tool for developers, today announced the launch of Model Context Protocol support for its service, which will enable AI coding agents and platforms to use its tools. Under the hood\u2026", "url": "https://siliconangle.com/2026/02/06/augment-code-makes-semantic-coding-capability-available-ai-agent/", "published_at": "2026-02-06T18:00:15Z", "content": "Augment Computing Inc., the maker of an agentic artificial intelligence coding tool for developers, today announced the launch of Model Context Protocol support for its service, which will enable AI \u2026 [+3818 chars]"}"""
          },
          "author": "Kyt Dotson",
          "created_at": "2026-02-07 19:32:56",
          "description": "Augment Computing Inc., the maker of an agentic artificial intelligence coding tool for developers, today announced the launch of Model Context Protocol support for its service, which will enable AI coding agents and platforms to use its tools. Under the hood…",
          "@timestamp": "2026-02-06T18:00:15.000Z",
          "url": "https://siliconangle.com/2026/02/06/augment-code-makes-semantic-coding-capability-available-ai-agent/",
          "content": "Augment Computing Inc., the maker of an agentic artificial intelligence coding tool for developers, today announced the launch of Model Context Protocol support for its service, which will enable AI … [+3818 chars]"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.livemint.com/companies/news/tech-giants-offer-as-much-as-600-000-to-promote-ai-but-some-creators-remain-unconvinced-heres-why-11770384060185.html",
        "_score": 6.905141,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Livemint",
          "content": "Major tech companies like Microsoft and Google are offering big cheques to social media influencers, hoping to turn them into promoters of their Artificial Intelligence (AI) products and lure more pe… [+3801 chars]",
          "author": "Eshita Gain",
          "event": {
            "original": """{"created_at": "2026-02-07 15:34:52", "source": "Livemint", "author": "Eshita Gain", "title": "Tech giants offer up to $600,000 to promote AI, but many creators are unconvinced \u2014 here's why", "description": "Tech giants like Microsoft and Google are paying influencers to promote their AI products, with payouts reaching up to $600,000. This trend is growing as AI companies ramp up digital ad spending, but some creators refuse deals due to ethical concerns and audi\u2026", "url": "https://www.livemint.com/companies/news/tech-giants-offer-as-much-as-600-000-to-promote-ai-but-some-creators-remain-unconvinced-heres-why-11770384060185.html", "published_at": "2026-02-06T14:28:42Z", "content": "Major tech companies like Microsoft and Google are offering big cheques to social media influencers, hoping to turn them into promoters of their Artificial Intelligence (AI) products and lure more pe\u2026 [+3801 chars]"}"""
          },
          "published_at": "2026-02-06T14:28:42Z",
          "@version": "1",
          "created_at": "2026-02-07 15:34:52",
          "title": "Tech giants offer up to $600,000 to promote AI, but many creators are unconvinced — here's why",
          "url": "https://www.livemint.com/companies/news/tech-giants-offer-as-much-as-600-000-to-promote-ai-but-some-creators-remain-unconvinced-heres-why-11770384060185.html",
          "@timestamp": "2026-02-06T14:28:42.000Z",
          "description": "Tech giants like Microsoft and Google are paying influencers to promote their AI products, with payouts reaching up to $600,000. This trend is growing as AI companies ramp up digital ad spending, but some creators refuse deals due to ethical concerns and audi…"
        }
      }
    ]
  }
}
```
# QUERY
```json
GET newsapi-2026.02/_search
{
  "query": {
    "fuzzy": {
      "content": 
      {
        "value":"buiness",
        "fuzziness": 2
      }
    }
  }
}
```

# RESPONSE
```json
{
  "took": 37,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 9,
      "relation": "eq"
    },
    "max_score": 5.0866957,
    "hits": [
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.hospitalitynet.org/news/4130778.html",
        "_score": 5.0866957,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Hospitality Net",
          "content": "Alexandria, VA The Global Business Travel Association (GBTA), the worlds leading voice representing the $1.57 trillion global business travel and meetings industry, is urging U.S. Customs and Border … [+4637 chars]",
          "author": "GBTA",
          "event": {
            "original": """{"created_at": "2026-02-07 15:34:52", "source": "Hospitality Net", "author": "GBTA", "title": "GBTA Calls for Balanced Approach to New ESTA Requirements, Citing Risks to Global Business Travel, U.S. Competitiveness, and International Data Privacy Compliance", "description": "The Global Business Travel Association (GBTA), the world\u2019s leading voice representing the $1.57 trillion global business travel and meetings industry, is urging U.S. Customs and Border Protection (CBP) to adopt a balanced and practical approach as it evaluate\u2026", "url": "https://www.hospitalitynet.org/news/4130778.html", "published_at": "2026-02-06T14:24:47Z", "content": "Alexandria, VA The Global Business Travel Association (GBTA), the worlds leading voice representing the $1.57 trillion global business travel and meetings industry, is urging U.S. Customs and Border \u2026 [+4637 chars]"}"""
          },
          "published_at": "2026-02-06T14:24:47Z",
          "@version": "1",
          "created_at": "2026-02-07 15:34:52",
          "title": "GBTA Calls for Balanced Approach to New ESTA Requirements, Citing Risks to Global Business Travel, U.S. Competitiveness, and International Data Privacy Compliance",
          "url": "https://www.hospitalitynet.org/news/4130778.html",
          "@timestamp": "2026-02-06T14:24:47.000Z",
          "description": "The Global Business Travel Association (GBTA), the world’s leading voice representing the $1.57 trillion global business travel and meetings industry, is urging U.S. Customs and Border Protection (CBP) to adopt a balanced and practical approach as it evaluate…"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://financialpost.com/pmn/business-wire-news-releases-pmn/andersen-consulting-expands-platform-in-north-america-with-addition-of-kezber",
        "_score": 3.8545895,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Financial Post",
          "title": "Andersen Consulting Expands Platform in North America with Addition of Kezber",
          "author": "Business Wire",
          "content": """SAN FRANCISCO Andersen Consulting strengthens its business transformation and cybersecurity offerings with the addition of Canadian-based collaborating firm Kezber.
THIS CONTENT IS RESERVED FOR SUBS… [+4106 chars]""",
          "@version": "1",
          "created_at": "2026-02-12 15:38:45",
          "url": "https://financialpost.com/pmn/business-wire-news-releases-pmn/andersen-consulting-expands-platform-in-north-america-with-addition-of-kezber",
          "event": {
            "original": """{"created_at": "2026-02-12 15:38:45", "source": "Financial Post", "author": "Business Wire", "title": "Andersen Consulting Expands Platform in North America with Addition of Kezber", "description": "SAN FRANCISCO \u2014 Andersen Consulting strengthens its business transformation and cybersecurity offerings with the addition of Canadian-based collaborating firm Kezber. Founded in 1996, Kezber specializes in providing a full suite of IT solutions including mana\u2026", "url": "https://financialpost.com/pmn/business-wire-news-releases-pmn/andersen-consulting-expands-platform-in-north-america-with-addition-of-kezber", "published_at": "2026-02-11T14:32:22Z", "content": "SAN FRANCISCO Andersen Consulting strengthens its business transformation and cybersecurity offerings with the addition of Canadian-based collaborating firm Kezber.\r\nTHIS CONTENT IS RESERVED FOR SUBS\u2026 [+4106 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:32:22.000Z",
          "description": "SAN FRANCISCO — Andersen Consulting strengthens its business transformation and cybersecurity offerings with the addition of Canadian-based collaborating firm Kezber. Founded in 1996, Kezber specializes in providing a full suite of IT solutions including mana…",
          "published_at": "2026-02-11T14:32:22Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.globenewswire.com/news-release/2026/02/11/3236320/36806/en/Aqua-Metals-Enters-Into-a-Term-Sheet-to-Acquire-Leading-Energy-Storage-Company-Lion-Energy.html",
        "_score": 3.8545895,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "GlobeNewswire",
          "title": "Aqua Metals Enters Into a Term Sheet to Acquire Leading Energy Storage Company Lion Energy",
          "author": "Aqua Metals",
          "content": """Combined Entity Would Integrate Energy Storage Products, Proprietary Energy Management Software, Recycling, and Battery Materials into a Single Platform
Lion Energy is a Revenue-Generating Business,… [+13474 chars]""",
          "@version": "1",
          "created_at": "2026-02-12 15:13:36",
          "url": "https://www.globenewswire.com/news-release/2026/02/11/3236320/36806/en/Aqua-Metals-Enters-Into-a-Term-Sheet-to-Acquire-Leading-Energy-Storage-Company-Lion-Energy.html",
          "event": {
            "original": """{"created_at": "2026-02-12 15:13:36", "source": "GlobeNewswire", "author": "Aqua Metals", "title": "Aqua Metals Enters Into a Term Sheet to Acquire Leading Energy Storage Company Lion Energy", "description": "Combined Entity Would Integrate Energy Storage Products, Proprietary Energy Management Software, Recycling, and Battery Materials into a Single Platform ...", "url": "https://www.globenewswire.com/news-release/2026/02/11/3236320/36806/en/Aqua-Metals-Enters-Into-a-Term-Sheet-to-Acquire-Leading-Energy-Storage-Company-Lion-Energy.html", "published_at": "2026-02-11T14:00:00Z", "content": "Combined Entity Would Integrate Energy Storage Products, Proprietary Energy Management Software, Recycling, and Battery Materials into a Single Platform\r\nLion Energy is a Revenue-Generating Business,\u2026 [+13474 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:00:00.000Z",
          "description": "Combined Entity Would Integrate Energy Storage Products, Proprietary Energy Management Software, Recycling, and Battery Materials into a Single Platform ...",
          "published_at": "2026-02-11T14:00:00Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.globenewswire.com/news-release/2026/02/11/3236273/0/en/Cycurion-Focuses-on-Growth-and-Continued-Cost-Efficiencies-Toward-Profitability-by-Saving-Over-2-2-Million-in-2026.html",
        "_score": 3.7570329,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "GlobeNewswire",
          "title": "Cycurion Focuses on Growth and Continued Cost Efficiencies Toward Profitability by Saving Over $2.2 Million in 2026",
          "author": "Cycurion",
          "content": "MCLEAN, Va., Feb. 11, 2026 (GLOBE NEWSWIRE) -- Cycurion, Inc. (Nasdaq: CYCU) (Cycurion or the Company), a trusted leader in IT cybersecurity solutions, today announced a strategic business reorganiza… [+6739 chars]",
          "@version": "1",
          "created_at": "2026-02-12 14:58:30",
          "url": "https://www.globenewswire.com/news-release/2026/02/11/3236273/0/en/Cycurion-Focuses-on-Growth-and-Continued-Cost-Efficiencies-Toward-Profitability-by-Saving-Over-2-2-Million-in-2026.html",
          "event": {
            "original": """{"created_at": "2026-02-12 14:58:30", "source": "GlobeNewswire", "author": "Cycurion", "title": "Cycurion Focuses on Growth and Continued Cost Efficiencies Toward Profitability by Saving Over $2.2 Million in 2026", "description": "Company Enhances Organizational Agility to Meet Evolving Cybersecurity Demands Company Enhances Organizational Agility to Meet Evolving Cybersecurity Demands", "url": "https://www.globenewswire.com/news-release/2026/02/11/3236273/0/en/Cycurion-Focuses-on-Growth-and-Continued-Cost-Efficiencies-Toward-Profitability-by-Saving-Over-2-2-Million-in-2026.html", "published_at": "2026-02-11T13:30:00Z", "content": "MCLEAN, Va., Feb. 11, 2026 (GLOBE NEWSWIRE) -- Cycurion, Inc. (Nasdaq: CYCU) (Cycurion or the Company), a trusted leader in IT cybersecurity solutions, today announced a strategic business reorganiza\u2026 [+6739 chars]"}"""
          },
          "@timestamp": "2026-02-11T13:30:00.000Z",
          "description": "Company Enhances Organizational Agility to Meet Evolving Cybersecurity Demands Company Enhances Organizational Agility to Meet Evolving Cybersecurity Demands",
          "published_at": "2026-02-11T13:30:00Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.livemint.com/companies/news/over-1-400-salesforce-employees-urge-tech-giant-to-drop-business-with-ice-authorities-say-we-are-deeply-troubled-11770811586354.html",
        "_score": 3.7570329,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Livemint",
          "title": "Over 1,400 Salesforce employees urge tech giant to drop business with ICE authorities; say ‘We are deeply troubled…’",
          "author": "Anubhav Mukherjee",
          "content": "US-based cloud services giant, Salesforce, employees are urging the company's Chief Executive Officer (CEO), Marc Benioff, to drop potential business opportunities with the US Immigration and Customs… [+3396 chars]",
          "@version": "1",
          "created_at": "2026-02-12 14:58:30",
          "url": "https://www.livemint.com/companies/news/over-1-400-salesforce-employees-urge-tech-giant-to-drop-business-with-ice-authorities-say-we-are-deeply-troubled-11770811586354.html",
          "event": {
            "original": """{"created_at": "2026-02-12 14:58:30", "source": "Livemint", "author": "Anubhav Mukherjee", "title": "Over 1,400 Salesforce employees urge tech giant to drop business with ICE authorities; say \u2018We are deeply troubled\u2026\u2019", "description": "More than 1,400 employees in a letter to Salesforce CEO Marc Benioff, urged the company to drop potential business opportunities with the US Immigration and Customs Enforcement (ICE) agency. Here's what you need to know about the appeal.&nbsp;", "url": "https://www.livemint.com/companies/news/over-1-400-salesforce-employees-urge-tech-giant-to-drop-business-with-ice-authorities-say-we-are-deeply-troubled-11770811586354.html", "published_at": "2026-02-11T13:20:20Z", "content": "US-based cloud services giant, Salesforce, employees are urging the company's Chief Executive Officer (CEO), Marc Benioff, to drop potential business opportunities with the US Immigration and Customs\u2026 [+3396 chars]"}"""
          },
          "@timestamp": "2026-02-11T13:20:20.000Z",
          "description": "More than 1,400 employees in a letter to Salesforce CEO Marc Benioff, urged the company to drop potential business opportunities with the US Immigration and Customs Enforcement (ICE) agency. Here's what you need to know about the appeal.&nbsp;",
          "published_at": "2026-02-11T13:20:20Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://socialnomics.net/2026/02/11/who-is-the-best-ai-keynote-speaker/",
        "_score": 3.7100825,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Socialnomics.net",
          "title": "Who Is the Best AI Keynote Speaker?",
          "author": "Gaby Allegues",
          "content": "The best AI keynote speaker is someone who can explain artificial intelligence clearly, connect it to leadership and real business outcomes, and inspire actionwithout overwhelming the audience with t… [+3265 chars]",
          "@version": "1",
          "created_at": "2026-02-12 15:23:41",
          "url": "https://socialnomics.net/2026/02/11/who-is-the-best-ai-keynote-speaker/",
          "event": {
            "original": """{"created_at": "2026-02-12 15:23:41", "source": "Socialnomics.net", "author": "Gaby Allegues", "title": "Who Is the Best AI Keynote Speaker?", "description": "Who Is the Best AI Keynote Speaker? The best AI keynote speaker is someone who can\u00a0explain artificial intelligence clearly,\u00a0connect it to leadership and real business outcomes, and\u00a0inspire action\u2014without overwhelming the audience with technical jargon. For or\u2026", "url": "https://socialnomics.net/2026/02/11/who-is-the-best-ai-keynote-speaker/", "published_at": "2026-02-11T14:00:17Z", "content": "The best AI keynote speaker is someone who can\u00a0explain artificial intelligence clearly,\u00a0connect it to leadership and real business outcomes, and\u00a0inspire actionwithout overwhelming the audience with t\u2026 [+3265 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:00:17.000Z",
          "description": "Who Is the Best AI Keynote Speaker? The best AI keynote speaker is someone who can explain artificial intelligence clearly, connect it to leadership and real business outcomes, and inspire action—without overwhelming the audience with technical jargon. For or…",
          "published_at": "2026-02-11T14:00:17Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.techtarget.com/searchsecurity/tip/Secure-MCP-servers-to-safeguard-AI-and-corporate-data",
        "_score": 3.6642914,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "published_at": "2026-02-06T18:00:00Z",
          "@version": "1",
          "source": "Techtarget.com",
          "title": "Secure MCP servers to safeguard AI and corporate data",
          "event": {
            "original": """{"created_at": "2026-02-07 19:32:56", "source": "Techtarget.com", "author": "Amy Larsen DeCarlo", "title": "Secure MCP servers to safeguard AI and corporate data", "description": "Model Context Protocol servers act as bridges between AI models and enterprise resources. But they can also give threat actors the keys to the castle if not secured.", "url": "https://www.techtarget.com/searchsecurity/tip/Secure-MCP-servers-to-safeguard-AI-and-corporate-data", "published_at": "2026-02-06T18:00:00Z", "content": "The deployment of AI for business use cases has become a major enterprise priority. But to reap AI's potentially game-changing productivity and innovation benefits, organizations must connect large l\u2026 [+3344 chars]"}"""
          },
          "author": "Amy Larsen DeCarlo",
          "created_at": "2026-02-07 19:32:56",
          "description": "Model Context Protocol servers act as bridges between AI models and enterprise resources. But they can also give threat actors the keys to the castle if not secured.",
          "@timestamp": "2026-02-06T18:00:00.000Z",
          "url": "https://www.techtarget.com/searchsecurity/tip/Secure-MCP-servers-to-safeguard-AI-and-corporate-data",
          "content": "The deployment of AI for business use cases has become a major enterprise priority. But to reap AI's potentially game-changing productivity and innovation benefits, organizations must connect large l… [+3344 chars]"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.blogto.com/tech/2026/02/3d-printing-canada/",
        "_score": 3.5760193,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "blogTO",
          "content": "3D printing has had quite the evolution over the past few years. What was once considered experimental has transformed into a reliable means of manufacturing for everyone from hobbyists to business p… [+2044 chars]",
          "author": "Kendall Bistretzan",
          "event": {
            "original": """{"created_at": "2026-02-07 15:34:52", "source": "blogTO", "author": "Kendall Bistretzan", "title": "GTA 3D printing shop is proving that IRL shopping and staff are always better", "description": "3D printing has had quite the evolution over the past few years. What was once considered experimental has transformed into a reliable means of manufacturing for everyone from hobbyists to business\u00a0professionals.And you don\u2019t have to go far \u2014 or rely solely o\u2026", "url": "https://www.blogto.com/tech/2026/02/3d-printing-canada/", "published_at": "2026-02-06T14:20:56Z", "content": "3D printing has had quite the evolution over the past few years. What was once considered experimental has transformed into a reliable means of manufacturing for everyone from hobbyists to business\u00a0p\u2026 [+2044 chars]"}"""
          },
          "published_at": "2026-02-06T14:20:56Z",
          "@version": "1",
          "created_at": "2026-02-07 15:34:52",
          "title": "GTA 3D printing shop is proving that IRL shopping and staff are always better",
          "url": "https://www.blogto.com/tech/2026/02/3d-printing-canada/",
          "@timestamp": "2026-02-06T14:20:56.000Z",
          "description": "3D printing has had quite the evolution over the past few years. What was once considered experimental has transformed into a reliable means of manufacturing for everyone from hobbyists to business professionals.And you don’t have to go far — or rely solely o…"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://financialpost.com/pmn/business-pmn/nike-ceo-hill-sees-turnaround-picking-up-from-europe-to-asia",
        "_score": 3.5334587,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Financial Post",
          "title": "Nike CEO Hill Sees Turnaround Picking Up From Europe to Asia",
          "author": "Bloomberg News",
          "content": "(Bloomberg) Nike Inc. expects its wholesale business to pick up steam across the world as it accelerates the launch of new footwear and apparel products and doubles down on its commitment to sports. … [+5184 chars]",
          "@version": "1",
          "created_at": "2026-02-12 14:58:30",
          "url": "https://financialpost.com/pmn/business-pmn/nike-ceo-hill-sees-turnaround-picking-up-from-europe-to-asia",
          "event": {
            "original": """{"created_at": "2026-02-12 14:58:30", "source": "Financial Post", "author": "Bloomberg News", "title": "Nike CEO Hill Sees Turnaround Picking Up From Europe to Asia", "description": "Nike Inc. expects its wholesale business to pick up steam across the world as it accelerates the launch of new footwear and apparel products and doubles down on its commitment to sports.", "url": "https://financialpost.com/pmn/business-pmn/nike-ceo-hill-sees-turnaround-picking-up-from-europe-to-asia", "published_at": "2026-02-11T13:41:38Z", "content": "(Bloomberg) Nike Inc. expects its wholesale business to pick up steam across the world as it accelerates the launch of new footwear and apparel products and doubles down on its commitment to sports.\u00a0\u2026 [+5184 chars]"}"""
          },
          "@timestamp": "2026-02-11T13:41:38.000Z",
          "description": "Nike Inc. expects its wholesale business to pick up steam across the world as it accelerates the launch of new footwear and apparel products and doubles down on its commitment to sports.",
          "published_at": "2026-02-11T13:41:38Z"
        }
      }
    ]
  }
}
```
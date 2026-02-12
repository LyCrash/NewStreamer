# QUERY
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

# RESPONSE
```json
{
  "took": 58,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 348,
      "relation": "eq"
    },
    "max_score": 1.1286451,
    "hits": [
      {
        "_index": "newsapi-2026.02",
        "_id": "https://techcrunch.com/2026/02/06/spotify-changes-developer-mode-api-to-require-premium-accounts-limits-test-users/",
        "_score": 1.1286451,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "TechCrunch",
          "content": "Spotify is changing how its APIs work in Developer Mode, its layer that lets developers test their third-party applications using the audio platform’s APIs. The changes include a mandatory premium ac… [+2442 chars]",
          "author": "Ivan Mehta",
          "event": {
            "original": """{"created_at": "2026-02-07 15:29:51", "source": "TechCrunch", "author": "Ivan Mehta", "title": "Spotify changes developer mode API to require premium accounts, limits test users | TechCrunch", "description": "Spotify is now limiting each app to only five users, and requires devs to have a Premium subscription. If developers need to make their app available to a wider user base, they will have to apply for extended quota.", "url": "https://techcrunch.com/2026/02/06/spotify-changes-developer-mode-api-to-require-premium-accounts-limits-test-users/", "published_at": "2026-02-06T14:03:40Z", "content": "Spotify is changing how its APIs work in Developer Mode, its layer that lets developers test their third-party applications using the audio platform\u2019s APIs. The changes include a mandatory premium ac\u2026 [+2442 chars]"}"""
          },
          "published_at": "2026-02-06T14:03:40Z",
          "@version": "1",
          "created_at": "2026-02-07 15:29:51",
          "title": "Spotify changes developer mode API to require premium accounts, limits test users | TechCrunch",
          "url": "https://techcrunch.com/2026/02/06/spotify-changes-developer-mode-api-to-require-premium-accounts-limits-test-users/",
          "@timestamp": "2026-02-06T14:03:40.000Z",
          "description": "Spotify is now limiting each app to only five users, and requires devs to have a Premium subscription. If developers need to make their app available to a wider user base, they will have to apply for extended quota."
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://financialpost.com/pmn/business-wire-news-releases-pmn/republic-technologies-welcomes-canadian-solar-nasdaq-csiq-cfo-as-special-advisor-to-the-board",
        "_score": 1.1264555,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Financial Post",
          "content": "VANCOUVER, British Columbia Republic Technologies Inc. (CSE: DOCT) (FSE: 7FM0) (WKN: A41AYF) (OTCQB: DOCKF) (the Company or Republic) is pleased to announce the appointment of Xinbo Zhu as the Specia… [+8206 chars]",
          "author": "Business Wire",
          "event": {
            "original": """{"created_at": "2026-02-07 15:29:51", "source": "Financial Post", "author": "Business Wire", "title": "Republic Technologies Welcomes Canadian Solar (NASDAQ: CSIQ) CFO as Special Advisor to the Board", "description": "VANCOUVER, British Columbia \u2014 Republic Technologies Inc. (CSE: DOCT) (FSE: 7FM0) (WKN: A41AYF) (OTCQB: DOCKF) (the \u201cCompany\u201d or \u201cRepublic\u201d) is pleased to announce the appointment of Xinbo Zhu as the Special Advisor to the Board and member of Republic\u2019s newly \u2026", "url": "https://financialpost.com/pmn/business-wire-news-releases-pmn/republic-technologies-welcomes-canadian-solar-nasdaq-csiq-cfo-as-special-advisor-to-the-board", "published_at": "2026-02-06T14:04:12Z", "content": "VANCOUVER, British Columbia Republic Technologies Inc. (CSE: DOCT) (FSE: 7FM0) (WKN: A41AYF) (OTCQB: DOCKF) (the Company or Republic) is pleased to announce the appointment of Xinbo Zhu as the Specia\u2026 [+8206 chars]"}"""
          },
          "published_at": "2026-02-06T14:04:12Z",
          "@version": "1",
          "created_at": "2026-02-07 15:29:51",
          "title": "Republic Technologies Welcomes Canadian Solar (NASDAQ: CSIQ) CFO as Special Advisor to the Board",
          "url": "https://financialpost.com/pmn/business-wire-news-releases-pmn/republic-technologies-welcomes-canadian-solar-nasdaq-csiq-cfo-as-special-advisor-to-the-board",
          "@timestamp": "2026-02-06T14:04:12.000Z",
          "description": "VANCOUVER, British Columbia — Republic Technologies Inc. (CSE: DOCT) (FSE: 7FM0) (WKN: A41AYF) (OTCQB: DOCKF) (the “Company” or “Republic”) is pleased to announce the appointment of Xinbo Zhu as the Special Advisor to the Board and member of Republic’s newly …"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.globenewswire.com/news-release/2026/02/11/3236395/0/en/OroCommerce-Partners-with-Azilen-Technologies-to-Power-Complex-B2B-Commerce-Transformations-for-Global-Enterprises.html",
        "_score": 1.1264555,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "GlobeNewswire",
          "title": "OroCommerce Partners with Azilen Technologies to Power Complex B2B Commerce Transformations for Global Enterprises",
          "author": "Oro Inc.",
          "content": """LOS ANGELES, Feb. 11, 2026 (GLOBE NEWSWIRE) -- OroCommerce
, a B2B-first commerce platform, today announced a strategic partnership with Azilen Technologies, a digital transformation and engineering… [+3341 chars]""",
          "@version": "1",
          "created_at": "2026-02-12 15:38:45",
          "url": "https://www.globenewswire.com/news-release/2026/02/11/3236395/0/en/OroCommerce-Partners-with-Azilen-Technologies-to-Power-Complex-B2B-Commerce-Transformations-for-Global-Enterprises.html",
          "event": {
            "original": """{"created_at": "2026-02-12 15:38:45", "source": "GlobeNewswire", "author": "Oro Inc.", "title": "OroCommerce Partners with Azilen Technologies to Power Complex B2B Commerce Transformations for Global Enterprises", "description": "LOS ANGELES, Feb. 11, 2026 (GLOBE NEWSWIRE) -- OroCommerce\r\n, a B2B-first commerce platform, today announced a strategic partnership with Azilen Technologies, a digital transformation and engineering firm known for solving complex enterprise technology challe\u2026", "url": "https://www.globenewswire.com/news-release/2026/02/11/3236395/0/en/OroCommerce-Partners-with-Azilen-Technologies-to-Power-Complex-B2B-Commerce-Transformations-for-Global-Enterprises.html", "published_at": "2026-02-11T14:32:00Z", "content": "LOS ANGELES, Feb. 11, 2026 (GLOBE NEWSWIRE) -- OroCommerce\r\n, a B2B-first commerce platform, today announced a strategic partnership with Azilen Technologies, a digital transformation and engineering\u2026 [+3341 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:32:00.000Z",
          "description": """LOS ANGELES, Feb. 11, 2026 (GLOBE NEWSWIRE) -- OroCommerce
, a B2B-first commerce platform, today announced a strategic partnership with Azilen Technologies, a digital transformation and engineering firm known for solving complex enterprise technology challe…""",
          "published_at": "2026-02-11T14:32:00Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://fortune.com/2026/02/06/moltbook-social-network-ai-agents-cybersecurity-religion-posts-tech/",
        "_score": 1.1244406,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "published_at": "2026-02-06T18:20:32Z",
          "@version": "1",
          "source": "Fortune",
          "title": "Moltbook, the Reddit for bots, alarms the tech world as agents start their own religion and plot to overthrow humans",
          "event": {
            "original": """{"created_at": "2026-02-07 19:32:56", "source": "Fortune", "author": "Kaitlyn Huamani, The Associated Press", "title": "Moltbook, the Reddit for bots, alarms the tech world as agents start their own religion and plot to overthrow humans", "description": "Musk has called Moltbook the 'very early stages of the singularity,' but others call it a 'dumpster fire.'", "url": "https://fortune.com/2026/02/06/moltbook-social-network-ai-agents-cybersecurity-religion-posts-tech/", "published_at": "2026-02-06T18:20:32Z", "content": "You are not invited to join the latest social media platform that has the internet talking. In fact, no humans are, unless you can hijack the site and roleplay as AI, as some appear to be doing.Moltb\u2026 [+7240 chars]"}"""
          },
          "author": "Kaitlyn Huamani, The Associated Press",
          "created_at": "2026-02-07 19:32:56",
          "description": "Musk has called Moltbook the 'very early stages of the singularity,' but others call it a 'dumpster fire.'",
          "@timestamp": "2026-02-06T18:20:32.000Z",
          "url": "https://fortune.com/2026/02/06/moltbook-social-network-ai-agents-cybersecurity-religion-posts-tech/",
          "content": "You are not invited to join the latest social media platform that has the internet talking. In fact, no humans are, unless you can hijack the site and roleplay as AI, as some appear to be doing.Moltb… [+7240 chars]"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://techcrunch.com/2026/02/11/meridian-ai-raises-17-million-to-remake-the-agentic-spreadsheet/",
        "_score": 1.1240536,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "TechCrunch",
          "title": "Meridian raises $17 million to remake the agentic spreadsheet | TechCrunch",
          "author": "Russell Brandom",
          "content": "The fight to tame spreadsheets with AI isnt over yet. A new company called Meridian has emerged from stealth with a more comprehensive IDE-based approach to agentic financial modeling and plenty of f… [+2297 chars]",
          "@version": "1",
          "created_at": "2026-02-12 15:28:43",
          "url": "https://techcrunch.com/2026/02/11/meridian-ai-raises-17-million-to-remake-the-agentic-spreadsheet/",
          "event": {
            "original": """{"created_at": "2026-02-12 15:28:43", "source": "TechCrunch", "author": "Russell Brandom", "title": "Meridian raises $17 million to remake the agentic spreadsheet | TechCrunch", "description": "A new company called Meridian.AI has emerged from stealth with an IDE-based approach to agentic financial modeling.", "url": "https://techcrunch.com/2026/02/11/meridian-ai-raises-17-million-to-remake-the-agentic-spreadsheet/", "published_at": "2026-02-11T14:03:30Z", "content": "The fight to tame spreadsheets with AI isnt over yet. A new company called Meridian has emerged from stealth with a more comprehensive IDE-based approach to agentic financial modeling and plenty of f\u2026 [+2297 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:03:30.000Z",
          "description": "A new company called Meridian.AI has emerged from stealth with an IDE-based approach to agentic financial modeling.",
          "published_at": "2026-02-11T14:03:30Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://slashdot.org/firehose.pl?op=view&amp;id=180746510",
        "_score": 1.1189994,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "Slashdot.org",
          "content": "Ford may be discontinuing its F-150 Lightning pickup but it hasn’t given up on electric cars. CEO Jim Farley just teased the automaker’s electric pickup based on its new Universal Electric Vehicle pl… [+2242 chars]",
          "author": "feedfeeder",
          "event": {
            "original": """{"created_at": "2026-02-07 15:34:52", "source": "Slashdot.org", "author": "feedfeeder", "title": "Ford shows off the tech going into its $30,000 electric pickup truck", "description": "Ford may be discontinuing its F-150 Lightning pickup but it hasn\u2019t given up on electric cars. CEO Jim Farley just teased the automaker\u2019s electric pickup based on its new Universal Electric Vehicle platform that he called \u201cone of the most audacious and importa\u2026", "url": "https://slashdot.org/firehose.pl?op=view&amp;id=180746510", "published_at": "2026-02-06T14:13:15Z", "content": "Ford may be discontinuing its F-150 Lightning pickup but it hasn\u2019t given up on electric cars. CEO Jim Farley just teased the automaker\u2019s electric pickup based on its new Universal Electric Vehicle pl\u2026 [+2242 chars]"}"""
          },
          "published_at": "2026-02-06T14:13:15Z",
          "@version": "1",
          "created_at": "2026-02-07 15:34:52",
          "title": "Ford shows off the tech going into its $30,000 electric pickup truck",
          "url": "https://slashdot.org/firehose.pl?op=view&amp;id=180746510",
          "@timestamp": "2026-02-06T14:13:15.000Z",
          "description": "Ford may be discontinuing its F-150 Lightning pickup but it hasn’t given up on electric cars. CEO Jim Farley just teased the automaker’s electric pickup based on its new Universal Electric Vehicle platform that he called “one of the most audacious and importa…"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.globenewswire.com/news-release/2026/02/11/3236398/0/en/OTR-Solutions-Acquires-Key-AI-Technology-to-Advance-Document-Automation-and-Fraud-Prevention-Capabilities-in-Transportation-and-Logistics.html",
        "_score": 1.1177821,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "GlobeNewswire",
          "title": "OTR Solutions Acquires Key AI Technology to Advance Document Automation and Fraud Prevention Capabilities in Transportation and Logistics",
          "author": "OTR Solutions",
          "content": "ROSWELL, Ga., Feb. 11, 2026 (GLOBE NEWSWIRE) -- OTR Solutions, the leader in logistics-focused financial technology and back-office solutions, today announced the acquisition of Peruse Technology, In… [+4895 chars]",
          "@version": "1",
          "created_at": "2026-02-12 15:38:45",
          "url": "https://www.globenewswire.com/news-release/2026/02/11/3236398/0/en/OTR-Solutions-Acquires-Key-AI-Technology-to-Advance-Document-Automation-and-Fraud-Prevention-Capabilities-in-Transportation-and-Logistics.html",
          "event": {
            "original": """{"created_at": "2026-02-12 15:38:45", "source": "GlobeNewswire", "author": "OTR Solutions", "title": "OTR Solutions Acquires Key AI Technology to Advance Document Automation and Fraud Prevention Capabilities in Transportation and Logistics", "description": "ROSWELL, Ga., Feb. 11, 2026 (GLOBE NEWSWIRE) -- OTR Solutions, the leader in logistics-focused financial technology and back-office solutions, today announced the acquisition of Peruse Technology, Inc., an AI-powered document audit automation technology purpo\u2026", "url": "https://www.globenewswire.com/news-release/2026/02/11/3236398/0/en/OTR-Solutions-Acquires-Key-AI-Technology-to-Advance-Document-Automation-and-Fraud-Prevention-Capabilities-in-Transportation-and-Logistics.html", "published_at": "2026-02-11T14:33:00Z", "content": "ROSWELL, Ga., Feb. 11, 2026 (GLOBE NEWSWIRE) -- OTR Solutions, the leader in logistics-focused financial technology and back-office solutions, today announced the acquisition of Peruse Technology, In\u2026 [+4895 chars]"}"""
          },
          "@timestamp": "2026-02-11T14:33:00.000Z",
          "description": "ROSWELL, Ga., Feb. 11, 2026 (GLOBE NEWSWIRE) -- OTR Solutions, the leader in logistics-focused financial technology and back-office solutions, today announced the acquisition of Peruse Technology, Inc., an AI-powered document audit automation technology purpo…",
          "published_at": "2026-02-11T14:33:00Z"
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.fox6now.com/news/milwaukee-police-department-facial-recognition-technology-banned",
        "_score": 1.117688,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "published_at": "2026-02-06T17:57:17Z",
          "@version": "1",
          "source": "fox6now.com",
          "title": "Milwaukee Police Department facial recognition technology banned",
          "event": {
            "original": """{"created_at": "2026-02-07 19:32:56", "source": "fox6now.com", "author": "Fox6 News Digital Team", "title": "Milwaukee Police Department facial recognition technology banned", "description": "The Milwaukee Police Department announced on Friday, Feb. 6, that it will voluntarily issue a ban on the use of any and all facial recognition technology (FRT) use for the department.", "url": "https://www.fox6now.com/news/milwaukee-police-department-facial-recognition-technology-banned", "published_at": "2026-02-06T17:57:17Z", "content": "MILWAUKEE - The Milwaukee Police Department announced on Friday, Feb. 6, that it will voluntarily issue a ban on the use of any and all facial recognition technology (FRT) use for the department.\u00a0\r\nT\u2026 [+10146 chars]"}"""
          },
          "author": "Fox6 News Digital Team",
          "created_at": "2026-02-07 19:32:56",
          "description": "The Milwaukee Police Department announced on Friday, Feb. 6, that it will voluntarily issue a ban on the use of any and all facial recognition technology (FRT) use for the department.",
          "@timestamp": "2026-02-06T17:57:17.000Z",
          "url": "https://www.fox6now.com/news/milwaukee-police-department-facial-recognition-technology-banned",
          "content": """MILWAUKEE - The Milwaukee Police Department announced on Friday, Feb. 6, that it will voluntarily issue a ban on the use of any and all facial recognition technology (FRT) use for the department. 
T… [+10146 chars]"""
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://techcrunch.com/2026/02/06/how-ai-is-helping-with-the-labor-issue-in-treating-rare-diseases/",
        "_score": 1.1164893,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "source": "TechCrunch",
          "content": "Modern biotech has the tools to edit genes and design drugs, yet thousands of rare diseases remain untreated. According to executives from Insilico Medicine and GenEditBio, the missing ingredient for… [+5571 chars]",
          "author": "Rebecca Bellan",
          "event": {
            "original": """{"created_at": "2026-02-07 15:34:52", "source": "TechCrunch", "author": "Rebecca Bellan", "title": "How AI is helping solve the labor issue in treating rare diseases | TechCrunch", "description": "At Web Summit Qatar, AI-powered biotech startups describe how automation, data, and gene editing are filling labor gaps in drug discovery and rare disease treatment.", "url": "https://techcrunch.com/2026/02/06/how-ai-is-helping-with-the-labor-issue-in-treating-rare-diseases/", "published_at": "2026-02-06T14:33:31Z", "content": "Modern biotech has the tools to edit genes and design drugs, yet thousands of rare diseases remain untreated. According to executives from Insilico Medicine and GenEditBio, the missing ingredient for\u2026 [+5571 chars]"}"""
          },
          "published_at": "2026-02-06T14:33:31Z",
          "@version": "1",
          "created_at": "2026-02-07 15:34:52",
          "title": "How AI is helping solve the labor issue in treating rare diseases | TechCrunch",
          "url": "https://techcrunch.com/2026/02/06/how-ai-is-helping-with-the-labor-issue-in-treating-rare-diseases/",
          "@timestamp": "2026-02-06T14:33:31.000Z",
          "description": "At Web Summit Qatar, AI-powered biotech startups describe how automation, data, and gene editing are filling labor gaps in drug discovery and rare disease treatment."
        }
      },
      {
        "_index": "newsapi-2026.02",
        "_id": "https://www.thurrott.com/music-videos/332457/disney-disables-dolby-vision-and-hdr10-in-some-european-countries-due-to-technical-challenges",
        "_score": 1.1139904,
        "_ignored": [
          "event.original.keyword"
        ],
        "_source": {
          "published_at": "2026-02-06T18:11:22Z",
          "@version": "1",
          "source": "Thurrott.com",
          "title": "Disney+ Disables Dolby Vision and HDR10+ in Some European Countries Due to “Technical Challenges”",
          "event": {
            "original": """{"created_at": "2026-02-07 19:32:56", "source": "Thurrott.com", "author": "Laurent Giret", "title": "Disney+ Disables Dolby Vision and HDR10+ in Some European Countries Due to \u201cTechnical Challenges\u201d", "description": "Disney+ has disabled Dolby Vision and HDR10 for Premium subscribers in several European countries, citing \u201ctechnical challenges.\u201d\nThe post Disney+ Disables Dolby Vision and HDR10+ in Some European Countries Due to \u201cTechnical Challenges\u201d appeared first on Thur\u2026", "url": "https://www.thurrott.com/music-videos/332457/disney-disables-dolby-vision-and-hdr10-in-some-european-countries-due-to-technical-challenges", "published_at": "2026-02-06T18:11:22Z", "content": "Disney+ has disabled Dolby Vision and HDR10 for Premium subscribers in several European countries, citing technical challenges. 3D movies on the Apple Vision Pro, which are also streamed in the Dolby\u2026 [+1217 chars]"}"""
          },
          "author": "Laurent Giret",
          "created_at": "2026-02-07 19:32:56",
          "description": """Disney+ has disabled Dolby Vision and HDR10 for Premium subscribers in several European countries, citing “technical challenges.”
The post Disney+ Disables Dolby Vision and HDR10+ in Some European Countries Due to “Technical Challenges” appeared first on Thur…""",
          "@timestamp": "2026-02-06T18:11:22.000Z",
          "url": "https://www.thurrott.com/music-videos/332457/disney-disables-dolby-vision-and-hdr10-in-some-european-countries-due-to-technical-challenges",
          "content": "Disney+ has disabled Dolby Vision and HDR10 for Premium subscribers in several European countries, citing technical challenges. 3D movies on the Apple Vision Pro, which are also streamed in the Dolby… [+1217 chars]"
        }
      }
    ]
  }
}
```

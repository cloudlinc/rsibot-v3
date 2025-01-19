Charles Schwab Logo
Developer Portal
Home
API Products
User Guides
Dashboard
Profile
Sign Out
Home
API Products
User Guides
Dashboard
Profile
Sign Out
API Products
Trader API - Individual
Market Data Production
Market Data Production
Specifications
Documentation
APIs to access Market Data
Market Data
 1.0.0 
OAS3
Trader API - Market data

Contact Schwab Trader API team
Servers

https://api.schwabapi.com/marketdata/v1
Quotes
Get Quotes Web Service.



GET
/quotes
Get Quotes by list of symbols.

Parameters
Name	Description
symbols
string
(query)
Comma separated list of symbol(s) to look up a quote

Example : MRAD,EATOF,EBIZ,AAPL,BAC,AAAHX,AAAIX,$DJI,$SPX,MVEN,SOBS,TOITF,CNSWF,AMZN 230317C01360000,DJX 231215C00290000,/ESH23,./ADUF23C0.55,AUD/CAD

MRAD,EATOF,EBIZ,AAPL,BAC,AAAHX,AAAIX,$DJI,$SPX,MVEN,SOBS,TOITF,CNSWF,AMZN  230317C01360000,DJX   231215C00290000,/ESH23,./ADUF23C0.55,AUD/CAD
fields
string
(query)
Request for subset of data by passing coma separated list of root nodes, possible root nodes are quote, fundamental, extended, reference, regular. Sending quote, fundamental in request will return quote and fundamental data in response. Dont send this attribute for full response.

Default value : all

quote,reference
indicative
boolean
(query)
Include indicative symbol quotes for all ETF symbols in request. If ETF symbol ABC is in request and indicative=true API will return quotes for ABC and its corresponding indicative quote for $ABC.IV

Available values : true, false

Example : false


false
Responses
Code	Description	Links
200	
Quote Response

Media type

application/json
Controls Accept header.
Examples

Search by Symbols+Cusips+SSIDs
Example Value
Schema
{
  "AAPL": {
    "assetMainType": "EQUITY",
    "symbol": "AAPL",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 1973757747,
    "reference": {
      "cusip": "037833100",
      "description": "Apple Inc",
      "exchange": "Q",
      "exchangeName": "NASDAQ"
    },
    "quote": {
      "52WeekHigh": 169,
      "52WeekLow": 1.1,
      "askMICId": "MEMX",
      "askPrice": 168.41,
      "askSize": 400,
      "askTime": 1644854683672,
      "bidMICId": "IEGX",
      "bidPrice": 168.4,
      "bidSize": 400,
      "bidTime": 1644854683633,
      "closePrice": 177.57,
      "highPrice": 169,
      "lastMICId": "XADF",
      "lastPrice": 168.405,
      "lastSize": 200,
      "lowPrice": 167.09,
      "mark": 168.405,
      "markChange": -9.164999999999992,
      "markPercentChange": -5.161344821760428,
      "netChange": -9.165,
      "netPercentChange": -5.161344821760428,
      "openPrice": 167.37,
      "quoteTime": 1644854683672,
      "securityStatus": "Normal",
      "totalVolume": 22361159,
      "tradeTime": 1644854683408,
      "volatility": 0.0347
    },
    "regular": {
      "regularMarketLastPrice": 168.405,
      "regularMarketLastSize": 2,
      "regularMarketNetChange": -9.165,
      "regularMarketPercentChange": -5.161344821760428,
      "regularMarketTradeTime": 1644854683408
    },
    "fundamental": {
      "avg10DaysVolume": 1,
      "avg1YearVolume": 0,
      "divAmount": 1.1,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 1.1,
      "eps": 0,
      "fundLeverageFactor": 1.1,
      "peRatio": 1.1
    }
  },
  "AAAIX": {
    "assetMainType": "MUTUAL_FUND",
    "symbol": "AAAIX",
    "realtime": true,
    "ssid": -1,
    "reference": {
      "cusip": "025085853",
      "description": "American Century Strategic Allocation: Aggressive Fund - I Class",
      "exchange": "3",
      "exchangeName": "Mutual Fund"
    },
    "quote": {
      "52WeekHigh": 9.24,
      "52WeekLow": 7.48,
      "closePrice": 9.12,
      "nAV": 0,
      "netChange": -0.03,
      "netPercentChange": -0.32894736842104566,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 0
    },
    "fundamental": {
      "avg10DaysVolume": 0,
      "avg1YearVolume": 0,
      "divAmount": 0,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 0.83059,
      "eps": 0,
      "fundLeverageFactor": 0,
      "peRatio": 0
    }
  },
  "AAAHX": {
    "assetMainType": "MUTUAL_FUND",
    "symbol": "AAAHX",
    "realtime": true,
    "ssid": -1,
    "reference": {
      "cusip": "02507J789",
      "description": "One Choice Blend+ 2015 Portfolio  I Class",
      "exchange": "3",
      "exchangeName": "Mutual Fund"
    },
    "quote": {
      "52WeekHigh": 10.64,
      "52WeekLow": 9.95,
      "closePrice": 10.53,
      "nAV": 0,
      "netChange": 0,
      "netPercentChange": 0,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 0
    },
    "fundamental": {
      "avg10DaysVolume": 0,
      "avg1YearVolume": 0,
      "divAmount": 0,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 0,
      "eps": 0,
      "fundLeverageFactor": 0,
      "peRatio": 0
    }
  },
  "BAC": {
    "assetMainType": "EQUITY",
    "symbol": "BAC",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 851234497,
    "reference": {
      "cusip": "060505104",
      "description": "Bank Of America Corp",
      "exchange": "N",
      "exchangeName": "NYSE"
    },
    "quote": {
      "52WeekHigh": 48.185,
      "52WeekLow": 22.95,
      "askMICId": "XNYS",
      "askPrice": 47.2,
      "askSize": 2100,
      "askTime": 1644854683639,
      "bidMICId": "XNYS",
      "bidPrice": 47.19,
      "bidSize": 3700,
      "bidTime": 1644854683640,
      "closePrice": 44.49,
      "highPrice": 48.185,
      "lastMICId": "ARCX",
      "lastPrice": 47.195,
      "lastSize": 200,
      "lowPrice": 47.06,
      "mark": 47.195,
      "markChange": 2.7049999999999983,
      "markPercentChange": 6.080017981568888,
      "netChange": 2.705,
      "netPercentChange": 6.080017981568888,
      "openPrice": 48.02,
      "quoteTime": 1644854683640,
      "securityStatus": "Normal",
      "totalVolume": 13573182,
      "tradeTime": 1644854683638,
      "volatility": 0.0206
    },
    "regular": {
      "regularMarketLastPrice": 47.195,
      "regularMarketLastSize": 2,
      "regularMarketNetChange": 2.705,
      "regularMarketPercentChange": 6.080017981568888,
      "regularMarketTradeTime": 1644854683638
    },
    "fundamental": {
      "avg10DaysVolume": 43411957,
      "avg1YearVolume": 40653250,
      "declarationDate": "2021-07-21T05:00:00Z",
      "divAmount": 0.75,
      "divExDate": "2021-09-02T05:00:00Z",
      "divFreq": 4,
      "divPayAmount": 0.75,
      "divPayDate": "2021-09-24T05:00:00Z",
      "divYield": 1.77,
      "eps": 2.996,
      "fundLeverageFactor": 0,
      "nextDivExDate": "2021-12-27T06:00:00Z",
      "nextDivPayDate": "2021-12-27T06:00:00Z",
      "peRatio": 13.50133
    }
  },
  "$SPX": {
    "assetMainType": "INDEX",
    "symbol": "$SPX",
    "realtime": true,
    "ssid": 1819771877,
    "reference": {
      "description": "S&P DOW JONES INDEX            S&P 500",
      "exchange": "0",
      "exchangeName": "Index"
    },
    "quote": {
      "52WeekHigh": 4423.46,
      "52WeekLow": 4385.52,
      "closePrice": 4766.18,
      "highPrice": 4423.46,
      "lastPrice": 4396.2,
      "lowPrice": 4385.52,
      "netChange": -369.98,
      "netPercentChange": -7.762610728088331,
      "openPrice": 4412.61,
      "securityStatus": "Unknown",
      "totalVolume": 628009977,
      "tradeTime": 1644854683056
    }
  },
  "MRAD": {
    "assetMainType": "EQUITY",
    "assetSubType": "ETF",
    "symbol": "MRAD",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 67229687,
    "reference": {
      "cusip": "402031868",
      "description": "Guinness Atkinson Fds SMART ETFS ADVERTISING MKT TCH ETF",
      "exchange": "P",
      "exchangeName": "NYSE Arca"
    },
    "quote": {
      "52WeekHigh": 31.96,
      "52WeekLow": 22.18,
      "askMICId": "IEGX",
      "askPrice": 22.29,
      "askSize": 500,
      "askTime": 1644854676848,
      "bidMICId": "EDGX",
      "bidPrice": 22.22,
      "bidSize": 500,
      "bidTime": 1644854681062,
      "closePrice": 26.8633,
      "highPrice": 22.18,
      "lastPrice": 22.18,
      "lastSize": 100,
      "lowPrice": 22.18,
      "mark": 22.22,
      "markChange": -4.6433,
      "markPercentChange": -17.284920318799255,
      "netChange": -4.6833,
      "netPercentChange": -17.433822352428777,
      "openPrice": 22.18,
      "quoteTime": 1644854681062,
      "securityStatus": "Normal",
      "totalVolume": 100,
      "tradeTime": 1644851921969,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 22.18,
      "regularMarketLastSize": 1,
      "regularMarketNetChange": -4.6833,
      "regularMarketPercentChange": -17.433822352428777,
      "regularMarketTradeTime": 1644851921969
    },
    "fundamental": {
      "avg10DaysVolume": 1606,
      "avg1YearVolume": 0,
      "divAmount": 0,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 0,
      "eps": 0,
      "fundLeverageFactor": 0,
      "fundStrategy": "A",
      "peRatio": 0
    }
  },
  "EBIZ": {
    "assetMainType": "EQUITY",
    "assetSubType": "ETF",
    "symbol": "EBIZ",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 52313178,
    "reference": {
      "cusip": "37954Y467",
      "description": "GLOBAL X E-COMMERCE ETF",
      "exchange": "Q",
      "exchangeName": "NASDAQ"
    },
    "quote": {
      "52WeekHigh": 37.9754,
      "52WeekLow": 24.52,
      "askMICId": "XNAS",
      "askPrice": 24.85,
      "askSize": 200,
      "askTime": 1644854683318,
      "bidMICId": "XNAS",
      "bidPrice": 24.79,
      "bidSize": 200,
      "bidTime": 1644854683318,
      "closePrice": 27.45,
      "highPrice": 24.8303,
      "lastMICId": "XADF",
      "lastPrice": 24.8303,
      "lastSize": 100,
      "lowPrice": 24.52,
      "mark": 24.8303,
      "markChange": -2.619699999999998,
      "markPercentChange": -9.543533697632052,
      "netChange": -2.6197,
      "netPercentChange": -9.543533697632052,
      "openPrice": 24.55,
      "quoteTime": 1644854683318,
      "securityStatus": "Normal",
      "totalVolume": 1626,
      "tradeTime": 1644850278470,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 24.8303,
      "regularMarketLastSize": 1,
      "regularMarketNetChange": -2.6197,
      "regularMarketPercentChange": -9.543533697632052,
      "regularMarketTradeTime": 1644850278470
    },
    "fundamental": {
      "avg10DaysVolume": 0,
      "avg1YearVolume": 0,
      "declarationDate": "2020-12-29T06:00:00Z",
      "divAmount": 0,
      "divExDate": "2020-12-30T06:00:00Z",
      "divFreq": 1,
      "divPayAmount": 0.26641,
      "divPayDate": "2021-01-08T06:00:00Z",
      "divYield": 0.88276,
      "eps": 0,
      "fundLeverageFactor": 0,
      "fundStrategy": "P",
      "nextDivExDate": "2022-01-10T06:00:00Z",
      "nextDivPayDate": "2022-01-10T06:00:00Z",
      "peRatio": 0
    }
  },
  "$DJI": {
    "assetMainType": "INDEX",
    "symbol": "$DJI",
    "realtime": true,
    "ssid": 0,
    "reference": {
      "description": "Dow Jones Industrial Average",
      "exchange": "0",
      "exchangeName": "Index"
    },
    "quote": {
      "52WeekHigh": 34744.56,
      "52WeekLow": 34364.39,
      "closePrice": 34738.06,
      "highPrice": 34744.56,
      "lastPrice": 34436.13,
      "lowPrice": 34364.39,
      "netChange": -301.93,
      "netPercentChange": -0.8691619508976618,
      "openPrice": 34694.5,
      "securityStatus": "Unknown",
      "totalVolume": 106647543,
      "tradeTime": 1644854683055
    }
  },
  "AMZN  220617C03170000": {
    "assetMainType": "OPTION",
    "symbol": "AMZN  220617C03170000",
    "realtime": true,
    "ssid": 72507798,
    "reference": {
      "contractType": "C",
      "daysToExpiration": 123,
      "description": "Amazon.com Inc 06/17/2022 $3170 Call",
      "exchange": "o",
      "exchangeName": "OPR",
      "expirationDay": 17,
      "expirationMonth": 6,
      "expirationYear": 2022,
      "isPennyPilot": true,
      "lastTradingDay": 1655510400000,
      "multiplier": 100,
      "settlementType": "P",
      "strikePrice": 3170,
      "underlying": "AMZN",
      "uvExpirationType": "S"
    },
    "quote": {
      "askPrice": 223,
      "askSize": 2,
      "askTime": 0,
      "bidPrice": 217.65,
      "bidSize": 2,
      "bidTime": 0,
      "closePrice": 357.75,
      "delta": 0.5106,
      "gamma": 0.0007,
      "highPrice": 0,
      "impliedYield": 0.042,
      "indAskPrice": 0,
      "indBidPrice": 0,
      "indQuoteTime": 0,
      "lastPrice": 0,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 220.325,
      "markChange": -137.425,
      "markPercentChange": -38.41369671558351,
      "moneyIntrinsicValue": -40.795,
      "netChange": 0,
      "netPercentChange": 0,
      "openInterest": 0,
      "openPrice": 0,
      "quoteTime": 1644854683379,
      "rho": 4.5173,
      "securityStatus": "Normal",
      "theoreticalOptionValue": 221.4,
      "theta": -0.9619,
      "timeValue": 220.325,
      "totalVolume": 0,
      "tradeTime": 0,
      "underlyingPrice": 3129.205,
      "vega": 7.1633,
      "volatility": 32.8918
    }
  },
  "DJX   231215C00290000": {
    "assetMainType": "OPTION",
    "symbol": "DJX   231215C00290000",
    "realtime": true,
    "ssid": 69272575,
    "reference": {
      "contractType": "C",
      "daysToExpiration": 669,
      "description": "DOW JONES INDUS IND 12/15/2023 $290 Call",
      "exchange": "o",
      "exchangeName": "OPR",
      "expirationDay": 15,
      "expirationMonth": 12,
      "expirationYear": 2023,
      "isPennyPilot": true,
      "lastTradingDay": 1702602000000,
      "multiplier": 100,
      "settlementType": "A",
      "strikePrice": 290,
      "underlying": "$DJX",
      "uvExpirationType": "S"
    },
    "quote": {
      "askPrice": 76.95,
      "askSize": 11,
      "askTime": 0,
      "bidPrice": 70.9,
      "bidSize": 11,
      "bidTime": 0,
      "closePrice": 86.2,
      "delta": 0,
      "gamma": 0,
      "highPrice": 0,
      "impliedYield": 0,
      "indAskPrice": 79.55,
      "indBidPrice": 73.25,
      "indQuoteTime": 1644614546536,
      "lastPrice": 0,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 73.925,
      "markChange": -12.274999999999991,
      "markPercentChange": -14.24013921113688,
      "moneyIntrinsicValue": 0,
      "netChange": 0,
      "netPercentChange": 0,
      "openInterest": 0,
      "openPrice": 0,
      "quoteTime": 1644854648305,
      "rho": 0,
      "securityStatus": "Normal",
      "theoreticalOptionValue": 0,
      "theta": 0,
      "timeValue": 0,
      "totalVolume": 0,
      "tradeTime": 0,
      "underlyingPrice": 0,
      "vega": -999,
      "volatility": 0
    }
  },
  "TOITF": {
    "assetMainType": "EQUITY",
    "symbol": "TOITF",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 68444487,
    "reference": {
      "cusip": "89072T102",
      "description": "TOPICUS COM INC",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "PC"
    },
    "quote": {
      "52WeekHigh": 75.702,
      "52WeekLow": 45.3933,
      "askPrice": 75.978,
      "askSize": 10000,
      "askTime": 1644849000209,
      "bidPrice": 72.5951,
      "bidSize": 10000,
      "bidTime": 1644849000209,
      "closePrice": 92.7,
      "highPrice": 75.702,
      "lastPrice": 75.702,
      "lastSize": 100,
      "lowPrice": 72.5478,
      "mark": 75.702,
      "netChange": -16.998,
      "openPrice": 74.8977,
      "quoteTime": 1644854676927,
      "securityStatus": "Normal",
      "totalVolume": 4274,
      "tradeTime": 1644854585000,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 75.702,
      "regularMarketLastSize": 1,
      "regularMarketNetChange": -16.998,
      "regularMarketTradeTime": 1644854585000
    }
  },
  "EATOF": {
    "assetMainType": "EQUITY",
    "assetSubType": "ETF",
    "symbol": "EATOF",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 43253301,
    "reference": {
      "cusip": "30052J102",
      "description": "EVOLVE AUTMBL INVTN INDX ETF",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "EM"
    },
    "quote": {
      "52WeekHigh": 47.1993,
      "52WeekLow": 24.2835,
      "askPrice": 33.1512,
      "askSize": 400000,
      "askTime": 1644849000044,
      "bidPrice": 33.0487,
      "bidSize": 250000,
      "bidTime": 1644849000044,
      "closePrice": 40.198,
      "highPrice": 33.1196,
      "lastPrice": 33.1196,
      "lastSize": 200,
      "lowPrice": 32.82,
      "mark": 33.1196,
      "netChange": -7.0784,
      "openPrice": 32.82,
      "quoteTime": 1644854660496,
      "securityStatus": "Normal",
      "totalVolume": 1017,
      "tradeTime": 1644850274000,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 33.1196,
      "regularMarketLastSize": 2,
      "regularMarketNetChange": -7.0784,
      "regularMarketTradeTime": 1644850274000
    }
  },
  "CNSWF": {
    "assetMainType": "EQUITY",
    "symbol": "CNSWF",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 807850646,
    "reference": {
      "cusip": "21037X100",
      "description": "Constellation Softwr",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "PC"
    },
    "quote": {
      "52WeekHigh": 1709.738,
      "52WeekLow": 904.0901,
      "askPrice": 1693.4699,
      "askSize": 30000,
      "askTime": 1644849000567,
      "bidPrice": 1688.4547,
      "bidSize": 20000,
      "bidTime": 1644849000567,
      "closePrice": 1856.4626,
      "highPrice": 1709.738,
      "lastPrice": 1693.4541,
      "lastSize": 100,
      "lowPrice": 1680.1511,
      "mark": 1693.4541,
      "netChange": -163.0084,
      "openPrice": 1682.0121,
      "quoteTime": 1644854655233,
      "securityStatus": "Normal",
      "totalVolume": 13901,
      "tradeTime": 1644854560000,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 1693.4541,
      "regularMarketLastSize": 1,
      "regularMarketNetChange": -163.0084,
      "regularMarketTradeTime": 1644854560000
    }
  },
  "MVEN": {
    "assetMainType": "EQUITY",
    "symbol": "MVEN",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 39225080,
    "reference": {
      "cusip": "88339B102",
      "description": "Themaven Inc",
      "exchange": "u",
      "exchangeName": "Nasdaq OTCBB",
      "otcMarketTier": "QX"
    },
    "quote": {
      "52WeekHigh": 3,
      "52WeekLow": 0.42,
      "askPrice": 0,
      "askSize": 0,
      "askTime": 0,
      "bidPrice": 0,
      "bidSize": 0,
      "bidTime": 0,
      "closePrice": 13.42,
      "highPrice": 0,
      "lastPrice": 0.42,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 0.42,
      "markChange": -13,
      "markPercentChange": -96.87034277198212,
      "netChange": -13,
      "netPercentChange": -96.87034277198212,
      "openPrice": 0,
      "quoteTime": 0,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 1644353952708,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 0.42,
      "regularMarketLastSize": 0,
      "regularMarketNetChange": -13,
      "regularMarketPercentChange": -96.87034277198212,
      "regularMarketTradeTime": 1644353952708
    },
    "fundamental": {
      "avg10DaysVolume": 299530,
      "avg1YearVolume": 430760,
      "divAmount": 0,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 0,
      "eps": 0,
      "fundLeverageFactor": 0,
      "peRatio": -0.68777
    }
  },
  "SOBS": {
    "assetMainType": "EQUITY",
    "symbol": "SOBS",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 561081427,
    "reference": {
      "cusip": "83441Q105",
      "description": "Solvay Bank Corp Sol",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "PC"
    },
    "quote": {
      "52WeekHigh": 43,
      "52WeekLow": 30.28,
      "askPrice": 45,
      "askSize": 200,
      "askTime": 0,
      "bidPrice": 39,
      "bidSize": 100,
      "bidTime": 0,
      "closePrice": 38.219,
      "highPrice": 0,
      "lastPrice": 38.219,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 38.219,
      "markChange": 0,
      "markPercentChange": 0,
      "netChange": 0,
      "netPercentChange": 0,
      "openPrice": 0,
      "quoteTime": 1644613200189,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 0,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 38.219,
      "regularMarketLastSize": 0,
      "regularMarketNetChange": 0,
      "regularMarketPercentChange": 0,
      "regularMarketTradeTime": 0
    },
    "fundamental": {
      "avg10DaysVolume": 1296,
      "avg1YearVolume": 0,
      "declarationDate": "2021-09-21T05:00:00Z",
      "divAmount": 1.48,
      "divExDate": "2021-09-30T05:00:00Z",
      "divFreq": 4,
      "divPayAmount": 1.47,
      "divPayDate": "2021-10-29T05:00:00Z",
      "divYield": 3.869,
      "eps": 0,
      "fundLeverageFactor": 0,
      "nextDivExDate": "2022-01-31T06:00:00Z",
      "nextDivPayDate": "2022-01-31T06:00:00Z",
      "peRatio": 0
    }
  },
  "/ESZ21": {
    "assetMainType": "FUTURE",
    "symbol": "/ESZ21",
    "realtime": true,
    "ssid": 0,
    "reference": {
      "description": "E-mini S&P 500 Index Futures,Dec-2021,ETH",
      "exchange": "@",
      "exchangeName": "XCME",
      "futureActiveSymbol": "/ESZ21",
      "futureExpirationDate": 1639717200000,
      "futureIsActive": true,
      "futureIsTradable": true,
      "futureMultiplier": 50,
      "futurePriceFormat": "D,D",
      "futureSettlementPrice": 4696,
      "futureTradingHours": "GLBX(de=1640;0=-17001600;1=r-17001600d-15551640;7=d-16401555)",
      "product": "/ES"
    },
    "quote": {
      "askPrice": 4694.5,
      "askSize": 113,
      "askTime": 0,
      "bidPrice": 4694.25,
      "bidSize": 57,
      "bidTime": 0,
      "netChange": -1.5,
      "closePrice": 4696,
      "futurePercentChange": -0.0003,
      "highPrice": 4701,
      "lastPrice": 4694.5,
      "lastSize": 3,
      "lowPrice": 4679.25,
      "mark": 0,
      "openInterest": 2328678,
      "openPrice": 4696.5,
      "quoteTime": 1637168671400,
      "securityStatus": "Unknown",
      "settleTime": 0,
      "tick": 0.25,
      "tickAmount": 12.5,
      "totalVolume": 550778,
      "tradeTime": 1637168671399
    }
  },
  "EUR/USD": {
    "assetMainType": "FOREX",
    "symbol": "EUR/USD",
    "ssid": 1,
    "realtime": true,
    "reference": {
      "description": "Euro/USDollar Spot",
      "exchange": "T",
      "exchangeName": "GFT",
      "isTradable": false,
      "marketMaker": "",
      "product": "",
      "tradingHours": ""
    },
    "quote": {
      "52WeekHigh": 1.135,
      "52WeekLow": 1.1331,
      "askPrice": 1.13456,
      "askSize": 1000000,
      "bidPrice": 1.13434,
      "bidSize": 1000000,
      "netChange": 0.00254,
      "closePrice": 1.13191,
      "highPrice": 1.135,
      "lastPrice": 1.13445,
      "lastSize": 0,
      "lowPrice": 1.1331,
      "mark": 1.13445,
      "openPrice": 1.13324,
      "netPercentChange": 0,
      "quoteTime": 1637236739892,
      "securityStatus": "Unknown",
      "tick": 0,
      "tickAmount": 0,
      "totalVolume": 0,
      "tradeTime": 1637236739892
    }
  }
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Used to identify an individual request throughout the lifetime of the request and across systems.

string
Example: 0a7f446a-7d74-49c8-a1e5-ca8ed59a3386
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links

GET
/{symbol_id}/quotes
Get Quote by single symbol.

Parameters
Name	Description
symbol_id *
string
(path)
Symbol of instrument

Example : TSLA

TSLA
fields
string
(query)
Request for subset of data by passing coma separated list of root nodes, possible root nodes are quote, fundamental, extended, reference, regular. Sending quote, fundamental in request will return quote and fundamental data in response. Dont send this attribute for full response.

Default value : all

quote,reference
Responses
Code	Description	Links
200	
Quote Response

Media type

application/json
Controls Accept header.
Examples

Search by symbol AAPL
Example Value
Schema
{
  "symbol": "AAPL",
  "empty": false,
  "previousClose": 174.56,
  "previousCloseDate": 1639029600000,
  "candles": [
    {
      "open": 175.01,
      "high": 175.15,
      "low": 175.01,
      "close": 175.04,
      "volume": 10719,
      "datetime": 1639137600000
    },
    {
      "open": 175.08,
      "high": 175.09,
      "low": 175.05,
      "close": 175.05,
      "volume": 500,
      "datetime": 1639137660000
    },
    {
      "open": 176.22,
      "high": 176.27,
      "low": 176.22,
      "close": 176.25,
      "volume": 3395,
      "datetime": 1640307300000
    },
    {
      "open": 176.26,
      "high": 176.27,
      "low": 176.26,
      "close": 176.26,
      "volume": 2174,
      "datetime": 1640307360000
    },
    {
      "open": 176.26,
      "high": 176.31,
      "low": 176.26,
      "close": 176.3,
      "volume": 15401,
      "datetime": 1640307420000
    },
    {
      "open": 176.3,
      "high": 176.3,
      "low": 176.3,
      "close": 176.3,
      "volume": 1700,
      "datetime": 1640307480000
    },
    {
      "open": 176.3,
      "high": 176.5,
      "low": 176.3,
      "close": 176.32,
      "volume": 5941,
      "datetime": 1640307540000
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Used to identify an individual request throughout the lifetime of the request and across systems.

string
Example: 0a7f446a-7d74-49c8-a1e5-ca8ed59a3386
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
404	
Error response for 404 Not Found

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 404,
      "title": "Not Found",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
Option Chains
Get Option Chains Web Service.



GET
/chains
Get option chain for an optionable Symbol

Get Option Chain including information on options contracts associated with each expiration.

Parameters
Name	Description
symbol *
string
(query)
Enter one symbol

Example : AAPL

AAPL
contractType
string
(query)
Contract Type

Available values : CALL, PUT, ALL


--
strikeCount
integer
(query)
The Number of strikes to return above or below the at-the-money price

strikeCount
includeUnderlyingQuote
boolean
(query)
Underlying quotes to be included


--
strategy
string
(query)
OptionChain strategy. Default is SINGLE. ANALYTICAL allows the use of volatility, underlyingPrice, interestRate, and daysToExpiration params to calculate theoretical values.

Available values : SINGLE, ANALYTICAL, COVERED, VERTICAL, CALENDAR, STRANGLE, STRADDLE, BUTTERFLY, CONDOR, DIAGONAL, COLLAR, ROLL


--
interval
number($double)
(query)
Strike interval for spread strategy chains (see strategy param)

interval
strike
number($double)
(query)
Strike Price

strike
range
string
(query)
Range(ITM/NTM/OTM etc.)

range
fromDate
string($date)
(query)
From date(pattern: yyyy-MM-dd)

fromDate
toDate
string($date)
(query)
To date (pattern: yyyy-MM-dd)

toDate
volatility
number($double)
(query)
Volatility to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param)

volatility
underlyingPrice
number($double)
(query)
Underlying price to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param)

underlyingPrice
interestRate
number($double)
(query)
Interest rate to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param)

interestRate
daysToExpiration
integer($int32)
(query)
Days to expiration to use in calculations. Applies only to ANALYTICAL strategy chains (see strategy param)

daysToExpiration
expMonth
string
(query)
Expiration month

Available values : JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, ALL


--
optionType
string
(query)
Option Type

optionType
entitlement
string
(query)
Applicable only if its retail token, entitlement of client PP-PayingPro, NP-NonPro and PN-NonPayingPro

Available values : PN, NP, PP


--
Responses
Code	Description	Links
200	
The Chain for the symbol was returned successfully.

Media type

application/json
Controls Accept header.
Example Value
Schema
{
  "symbol": "string",
  "status": "string",
  "underlying": {
    "ask": 0,
    "askSize": 0,
    "bid": 0,
    "bidSize": 0,
    "change": 0,
    "close": 0,
    "delayed": true,
    "description": "string",
    "exchangeName": "IND",
    "fiftyTwoWeekHigh": 0,
    "fiftyTwoWeekLow": 0,
    "highPrice": 0,
    "last": 0,
    "lowPrice": 0,
    "mark": 0,
    "markChange": 0,
    "markPercentChange": 0,
    "openPrice": 0,
    "percentChange": 0,
    "quoteTime": 0,
    "symbol": "string",
    "totalVolume": 0,
    "tradeTime": 0
  },
  "strategy": "SINGLE",
  "interval": 0,
  "isDelayed": true,
  "isIndex": true,
  "daysToExpiration": 0,
  "interestRate": 0,
  "underlyingPrice": 0,
  "volatility": 0,
  "callExpDateMap": {
    "additionalProp1": {
      "additionalProp1": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp2": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp3": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      }
    },
    "additionalProp2": {
      "additionalProp1": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp2": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp3": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      }
    },
    "additionalProp3": {
      "additionalProp1": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp2": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp3": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      }
    }
  },
  "putExpDateMap": {
    "additionalProp1": {
      "additionalProp1": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp2": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp3": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      }
    },
    "additionalProp2": {
      "additionalProp1": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp2": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp3": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      }
    },
    "additionalProp3": {
      "additionalProp1": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp2": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      },
      "additionalProp3": {
        "putCall": "PUT",
        "symbol": "string",
        "description": "string",
        "exchangeName": "string",
        "bidPrice": 0,
        "askPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "bidSize": 0,
        "askSize": 0,
        "lastSize": 0,
        "highPrice": 0,
        "lowPrice": 0,
        "openPrice": 0,
        "closePrice": 0,
        "totalVolume": 0,
        "tradeDate": 0,
        "quoteTimeInLong": 0,
        "tradeTimeInLong": 0,
        "netChange": 0,
        "volatility": 0,
        "delta": 0,
        "gamma": 0,
        "theta": 0,
        "vega": 0,
        "rho": 0,
        "timeValue": 0,
        "openInterest": 0,
        "isInTheMoney": true,
        "theoreticalOptionValue": 0,
        "theoreticalVolatility": 0,
        "isMini": true,
        "isNonStandard": true,
        "optionDeliverablesList": [
          {
            "symbol": "string",
            "assetType": "string",
            "deliverableUnits": "string",
            "currencyType": "string"
          }
        ],
        "strikePrice": 0,
        "expirationDate": "string",
        "daysToExpiration": 0,
        "expirationType": "M",
        "lastTradingDay": 0,
        "multiplier": 0,
        "settlementType": "A",
        "deliverableNote": "string",
        "isIndexOption": true,
        "percentChange": 0,
        "markChange": 0,
        "markPercentChange": 0,
        "isPennyPilot": true,
        "intrinsicValue": 0,
        "optionRoot": "string"
      }
    }
  }
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Used to identify an individual request throughout the lifetime of the request and across systems.

string
Example: 0a7f446a-7d74-49c8-a1e5-ca8ed59a3386
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
404	
Error response for 404 Not Found

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 404,
      "title": "Not Found",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
Option Expiration Chain
Get Option Expiration Chain Web Service.



GET
/expirationchain
Get option expiration chain for an optionable symbol

Get Option Expiration (Series) information for an optionable symbol. Does not include individual options contracts for the underlying.

Parameters
Name	Description
symbol *
string
(query)
Enter one symbol

Example : AAPL

AAPL
Responses
Code	Description	Links
200	
The Expiration Chain for the symbol was returned successfully.

Media type

application/json
Controls Accept header.
Examples

Get ExpirationChain for AAPL
Example Value
Schema
{
  "expirationList": [
    {
      "expirationDate": "2022-01-07",
      "daysToExpiration": 2,
      "expirationType": "W",
      "standard": true
    },
    {
      "expirationDate": "2022-01-14",
      "daysToExpiration": 9,
      "expirationType": "W",
      "standard": true
    },
    {
      "expirationDate": "2022-01-21",
      "daysToExpiration": 16,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2022-01-28",
      "daysToExpiration": 23,
      "expirationType": "W",
      "standard": true
    },
    {
      "expirationDate": "2022-02-04",
      "daysToExpiration": 30,
      "expirationType": "W",
      "standard": true
    },
    {
      "expirationDate": "2022-02-11",
      "daysToExpiration": 37,
      "expirationType": "W",
      "standard": true
    },
    {
      "expirationDate": "2022-02-18",
      "daysToExpiration": 44,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2022-03-18",
      "daysToExpiration": 72,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2022-04-14",
      "daysToExpiration": 99,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2022-05-20",
      "daysToExpiration": 135,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2022-06-17",
      "daysToExpiration": 163,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2022-07-15",
      "daysToExpiration": 191,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2022-09-16",
      "daysToExpiration": 254,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2023-01-20",
      "daysToExpiration": 380,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2023-03-17",
      "daysToExpiration": 436,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2023-06-16",
      "daysToExpiration": 527,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2023-09-15",
      "daysToExpiration": 618,
      "expirationType": "S",
      "standard": true
    },
    {
      "expirationDate": "2024-01-19",
      "daysToExpiration": 744,
      "expirationType": "S",
      "standard": true
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Used to identify an individual request throughout the lifetime of the request and across systems.

string
Example: 0a7f446a-7d74-49c8-a1e5-ca8ed59a3386
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
404	
Error response for 404 Not Found

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 404,
      "title": "Not Found",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
PriceHistory
Get Price History Web Service.



GET
/pricehistory
Get PriceHistory for a single symbol and date ranges.

Get historical Open, High, Low, Close, and Volume for a given frequency (i.e. aggregation). Frequency available is dependent on periodType selected. The datetime format is in EPOCH milliseconds.

Parameters
Name	Description
symbol *
string
(query)
The Equity symbol used to look up price history

Example : AAPL

AAPL
periodType
string
(query)
The chart period being requested.

Available values : day, month, year, ytd


--
period
integer($int32)
(query)
The number of chart period types.

If the periodType is
• day - valid values are 1, 2, 3, 4, 5, 10
• month - valid values are 1, 2, 3, 6
• year - valid values are 1, 2, 3, 5, 10, 15, 20
• ytd - valid values are 1

If the period is not specified and the periodType is
• day - default period is 10.
• month - default period is 1.
• year - default period is 1.
• ytd - default period is 1.

period
frequencyType
string
(query)
The time frequencyType

If the periodType is
• day - valid value is minute
• month - valid values are daily, weekly
• year - valid values are daily, weekly, monthly
• ytd - valid values are daily, weekly

If frequencyType is not specified, default value depends on the periodType
• day - defaulted to minute.
• month - defaulted to weekly.
• year - defaulted to monthly.
• ytd - defaulted to weekly.

Available values : minute, daily, weekly, monthly


--
frequency
integer($int32)
(query)
The time frequency duration

If the frequencyType is
• minute - valid values are 1, 5, 10, 15, 30
• daily - valid value is 1
• weekly - valid value is 1
• monthly - valid value is 1

If frequency is not specified, default value is 1

frequency
startDate
integer($int64)
(query)
The start date, Time in milliseconds since the UNIX epoch eg 1451624400000
If not specified startDate will be (endDate - period) excluding weekends and holidays.

startDate
endDate
integer($int64)
(query)
The end date, Time in milliseconds since the UNIX epoch eg 1451624400000
If not specified, the endDate will default to the market close of previous business day.

endDate
needExtendedHoursData
boolean
(query)
Need extended hours data


--
needPreviousClose
boolean
(query)
Need previous close price/date


--
Responses
Code	Description	Links
200	
Get all candles for given date range

Media type

application/json
Controls Accept header.
Examples

Search by symbol AAPL
Example Value
Schema
{
  "symbol": "AAPL",
  "empty": false,
  "previousClose": 174.56,
  "previousCloseDate": 1639029600000,
  "candles": [
    {
      "open": 175.01,
      "high": 175.15,
      "low": 175.01,
      "close": 175.04,
      "volume": 10719,
      "datetime": 1639137600000
    },
    {
      "open": 175.08,
      "high": 175.09,
      "low": 175.05,
      "close": 175.05,
      "volume": 500,
      "datetime": 1639137660000
    },
    {
      "open": 176.22,
      "high": 176.27,
      "low": 176.22,
      "close": 176.25,
      "volume": 3395,
      "datetime": 1640307300000
    },
    {
      "open": 176.26,
      "high": 176.27,
      "low": 176.26,
      "close": 176.26,
      "volume": 2174,
      "datetime": 1640307360000
    },
    {
      "open": 176.26,
      "high": 176.31,
      "low": 176.26,
      "close": 176.3,
      "volume": 15401,
      "datetime": 1640307420000
    },
    {
      "open": 176.3,
      "high": 176.3,
      "low": 176.3,
      "close": 176.3,
      "volume": 1700,
      "datetime": 1640307480000
    },
    {
      "open": 176.3,
      "high": 176.5,
      "low": 176.3,
      "close": 176.32,
      "volume": 5941,
      "datetime": 1640307540000
    }
  ]
}
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
404	
Error response for 404 Not Found

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 404,
      "title": "Not Found",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
Movers
Get Movers Web Service.



GET
/movers/{symbol_id}
Get Movers for a specific index.

Get a list of top 10 securities movement for a specific index.

Parameters
Name	Description
symbol_id *
string
(path)
Index Symbol

Available values : $DJI, $COMPX, $SPX, NYSE, NASDAQ, OTCBB, INDEX_ALL, EQUITY_ALL, OPTION_ALL, OPTION_PUT, OPTION_CALL

Example : $DJI


$DJI
sort
string
(query)
Sort by a particular attribute

Available values : VOLUME, TRADES, PERCENT_CHANGE_UP, PERCENT_CHANGE_DOWN

Example : VOLUME


VOLUME
frequency
integer($int32)
(query)
To return movers with the specified directions of up or down

Available values : 0, 1, 5, 10, 30, 60

Default value : 0


0
Responses
Code	Description	Links
200	
Analytics for the symbol was returned successfully.

Media type

application/json
Controls Accept header.
Examples

Search by "$DJI"
Example Value
Schema
{
  "screeners": [
    {
      "change": 10,
      "description": "Dow jones",
      "direction": "up",
      "last": 100,
      "symbol": "$DJI",
      "totalVolume": 100
    },
    {
      "change": 10,
      "description": "Dow jones",
      "direction": "up",
      "last": 100,
      "symbol": "$DJI",
      "totalVolume": 100
    },
    {
      "change": 10,
      "description": "Dow jones",
      "direction": "up",
      "last": 100,
      "symbol": "$DJI",
      "totalVolume": 100
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Used to identify an individual request throughout the lifetime of the request and across systems.

string
Example: 0a7f446a-7d74-49c8-a1e5-ca8ed59a3386
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
404	
Error response for 404 Not Found

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 404,
      "title": "Not Found",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
MarketHours
Get MarketHours Web Service.



GET
/markets
Get Market Hours for different markets.

Get Market Hours for dates in the future across different markets.

Parameters
Name	Description
markets *
array[string]
(query)
List of markets

Available values : equity, option, bond, future, forex

equityoptionbondfutureforex
date
string($date)
(query)
Valid date range is from currentdate to 1 year from today. It will default to current day if not entered. Date format:YYYY-MM-DD

date
Responses
Code	Description	Links
200	
OK

Media type

application/json
Controls Accept header.
Examples

Get getMarketHours for EQUITY and OPTION
Example Value
Schema
{
  "equity": {
    "EQ": {
      "date": "2022-04-14",
      "marketType": "EQUITY",
      "product": "EQ",
      "productName": "equity",
      "isOpen": true,
      "sessionHours": {
        "preMarket": [
          {
            "start": "2022-04-14T07:00:00-04:00",
            "end": "2022-04-14T09:30:00-04:00"
          }
        ],
        "regularMarket": [
          {
            "start": "2022-04-14T09:30:00-04:00",
            "end": "2022-04-14T16:00:00-04:00"
          }
        ],
        "postMarket": [
          {
            "start": "2022-04-14T16:00:00-04:00",
            "end": "2022-04-14T20:00:00-04:00"
          }
        ]
      }
    }
  },
  "option": {
    "EQO": {
      "date": "2022-04-14",
      "marketType": "OPTION",
      "product": "EQO",
      "productName": "equity option",
      "isOpen": true,
      "sessionHours": {
        "regularMarket": [
          {
            "start": "2022-04-14T09:30:00-04:00",
            "end": "2022-04-14T16:00:00-04:00"
          }
        ]
      }
    },
    "IND": {
      "date": "2022-04-14",
      "marketType": "OPTION",
      "product": "IND",
      "productName": "index option",
      "isOpen": true,
      "sessionHours": {
        "regularMarket": [
          {
            "start": "2022-04-14T09:30:00-04:00",
            "end": "2022-04-14T16:15:00-04:00"
          }
        ]
      }
    }
  }
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The generated GUID can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links

GET
/markets/{market_id}
Get Market Hours for a single market.

Get Market Hours for dates in the future for a single market.

Parameters
Name	Description
market_id *
string
(path)
market id

Available values : equity, option, bond, future, forex


equity
date
string($date)
(query)
Valid date range is from currentdate to 1 year from today. It will default to current day if not entered. Date format:YYYY-MM-DD

date
Responses
Code	Description	Links
200	
OK

Media type

application/json
Controls Accept header.
Examples

Get market hours for equity market
Example Value
Schema
{
  "equity": {
    "EQ": {
      "date": "2022-04-14",
      "marketType": "EQUITY",
      "exchange": "NULL",
      "category": "NULL",
      "product": "EQ",
      "productName": "equity",
      "isOpen": true,
      "sessionHours": {
        "preMarket": [
          {
            "start": "2022-04-14T07:00:00-04:00",
            "end": "2022-04-14T09:30:00-04:00"
          }
        ],
        "regularMarket": [
          {
            "start": "2022-04-14T09:30:00-04:00",
            "end": "2022-04-14T16:00:00-04:00"
          }
        ],
        "postMarket": [
          {
            "start": "2022-04-14T16:00:00-04:00",
            "end": "2022-04-14T20:00:00-04:00"
          }
        ]
      }
    }
  }
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The generated GUID can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
404	
Error response for 404 Not Found

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 404,
      "title": "Not Found",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
Instruments
Get Instruments Web Service.



GET
/instruments
Get Instruments by symbols and projections.

Get Instruments details by using different projections. Get more specific fundamental instrument data by using fundamental as the projection.

Parameters
Name	Description
symbol *
string
(query)
symbol of a security

symbol
projection *
string
(query)
search by

Available values : symbol-search, symbol-regex, desc-search, desc-regex, search, fundamental


symbol-search
Responses
Code	Description	Links
200	
OK

Media type

application/json
Controls Accept header.
Examples

symbol=AAPL,BAC&projection=symbol-search
Example Value
Schema
{
  "instruments": [
    {
      "cusip": "037833100",
      "symbol": "AAPL",
      "description": "Apple Inc",
      "exchange": "NASDAQ",
      "assetType": "EQUITY"
    },
    {
      "cusip": "060505104",
      "symbol": "BAC",
      "description": "Bank Of America Corp",
      "exchange": "NYSE",
      "assetType": "EQUITY"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Resource-Version	
Used to identify desired and returned version of an API resource

integer
Example: 3
Schwab-Client-CorrelId	
Used to identify an individual request throughout the lifetime of the request and across systems.

string
Example: 0a7f446a-7d74-49c8-a1e5-ca8ed59a3386
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links

GET
/instruments/{cusip_id}
Get Instrument by specific cusip

Get basic instrument details by cusip

Parameters
Name	Description
cusip_id *
string
(path)
cusip of a security

cusip_id
Responses
Code	Description	Links
200	
OK

Media type

application/json
Controls Accept header.
Examples

Get getinstruments for cusip
Example Value
Schema
{
  "cusip": "037833100",
  "symbol": "AAPL",
  "description": "Apple Inc",
  "exchange": "NASDAQ",
  "assetType": "EQUITY"
}
Headers:
Name	Description	Type
Schwab-Resource-Version	
Used to identify desired and returned version of an API resource

integer
Example: 3
Schwab-Client-CorrelId	
Used to identify an individual request throughout the lifetime of the request and across systems.

string
Example: 0a7f446a-7d74-49c8-a1e5-ca8ed59a3386
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
404	
Error response for 404 Not Found

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 404,
      "title": "Not Found",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links

Schemas
Bond
FundamentalInst
Instrument
InstrumentResponse
Hours{
date	[...]
marketType	[...]
exchange	[...]
category	[...]
product	[...]
productName	[...]
isOpen	[...]
sessionHours	{...}
}
Interval{
start	[...]
end	[...]
}
Screener{
description:	
Security info of most moved with in an index

change	[...]
description	[...]
direction	[...]
last	[...]
symbol	[...]
totalVolume	[...]
}
Candle{
close	[...]
datetime	[...]
datetimeISO8601	[...]
high	[...]
low	[...]
open	[...]
volume	[...]
}
CandleList{
candles	[...]
empty	[...]
previousClose	[...]
previousCloseDate	[...]
previousCloseDateISO8601	[...]
symbol	[...]
}
EquityResponse
QuoteError
ExtendedMarket{
description:	
Quote data for extended hours

askPrice	[...]
askSize	[...]
bidPrice	[...]
bidSize	[...]
lastPrice	[...]
lastSize	[...]
mark	[...]
quoteTime	[...]
totalVolume	[...]
tradeTime	[...]
}
ForexResponse
Fundamental
FutureOptionResponse
FutureResponse
IndexResponse
MutualFundResponse
OptionResponse
QuoteEquity
QuoteForex
QuoteFuture
QuoteFutureOption
QuoteIndex
QuoteMutualFund
QuoteOption
QuoteRequest
QuoteResponse
QuoteResponseObject
ReferenceEquity
ReferenceForex
ReferenceFuture
ReferenceFutureOption
ReferenceIndex
ReferenceMutualFund
ReferenceOption
RegularMarket
AssetMainType
EquityAssetSubType
MutualFundAssetSubType
ContractType
SettlementType
ExpirationType
FundStrategy
ExerciseType
DivFreq
QuoteType
ErrorResponse
Error{
id	[...]
status	[...]
title	[...]
detail	[...]
source	ErrorSource{...}
}
ErrorSource
OptionChain
OptionContractMap
Underlying
OptionDeliverables
OptionContract
ExpirationChain
Expiration
Terms Of Use
|
Privacy Notice
© 2025 Charles Schwab & Co., Inc. All rights reserved. Member SIPC. Unauthorized access is prohibited. Usage is monitored.

Quotes
Get Quotes Web Service.



GET
/quotes
Get Quotes by list of symbols.

Parameters
Name	Description
symbols
string
(query)
Comma separated list of symbol(s) to look up a quote

BITI,AAPL,BAC,AAAHX,AAAIX,$DJI,$SPX,MVEN,SOBS,TOITF,CNSWF,AMZN  230317C01360000,DJX   231215C00290000,/ESH23,./ADUF23C0.55,AUD/CAD
fields
string
(query)
Request for subset of data by passing coma separated list of root nodes, possible root nodes are quote, fundamental, extended, reference, regular. Sending quote, fundamental in request will return quote and fundamental data in response. Dont send this attribute for full response.

quote,reference
indicative
boolean
(query)
Include indicative symbol quotes for all ETF symbols in request. If ETF symbol ABC is in request and indicative=true API will return quotes for ABC and its corresponding indicative quote for $ABC.IV


false
Responses
Curl

curl -X 'GET' \
  'https://api.schwabapi.com/marketdata/v1/quotes?symbols=BITI%2CAAPL%2CBAC%2CAAAHX%2CAAAIX%2C%24DJI%2C%24SPX%2CMVEN%2CSOBS%2CTOITF%2CCNSWF%2CAMZN%20%20230317C01360000%2CDJX%20%20%20231215C00290000%2C%2FESH23%2C.%2FADUF23C0.55%2CAUD%2FCAD&fields=quote%2Creference&indicative=false' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer I0.b2F1dGgyLmNkYy5zY2h3YWIuY29t.Rg065wgsucrjWm6dwVRUrkr6mUvBjlc4c8kMn8EfU9w@'
Request URL
https://api.schwabapi.com/marketdata/v1/quotes?symbols=BITI%2CAAPL%2CBAC%2CAAAHX%2CAAAIX%2C%24DJI%2C%24SPX%2CMVEN%2CSOBS%2CTOITF%2CCNSWF%2CAMZN%20%20230317C01360000%2CDJX%20%20%20231215C00290000%2C%2FESH23%2C.%2FADUF23C0.55%2CAUD%2FCAD&fields=quote%2Creference&indicative=false
Server response
Code	Details
200	
Response body
Download
{
  "BITI": {
    "assetMainType": "EQUITY",
    "assetSubType": "ETF",
    "quoteType": "NFL",
    "realtime": false,
    "ssid": 104236055,
    "symbol": "BITI",
    "quote": {
      "52WeekHigh": 71.0495,
      "52WeekLow": 20.76,
      "askMICId": "BATS",
      "askPrice": 21.42,
      "askSize": 0,
      "askTime": 1737161912940,
      "bidMICId": "BATS",
      "bidPrice": 21.12,
      "bidSize": 0,
      "bidTime": 1737161912940,
      "closePrice": 22.18,
      "highPrice": 21.74,
      "lastMICId": "LTSE",
      "lastPrice": 21.2,
      "lastSize": 63,
      "lowPrice": 20.92,
      "mark": 21.21,
      "markChange": -0.97,
      "markPercentChange": -4.37330929,
      "netChange": -0.98,
      "netPercentChange": -4.41839495,
      "openPrice": 21.64,
      "postMarketChange": -0.01,
      "postMarketPercentChange": -0.04714757,
      "quoteTime": 1737161912940,
      "securityStatus": "Normal",
      "totalVolume": 2325146,
      "tradeTime": 1737161970740
    },
    "reference": {
      "cusip": "74347G184",
      "description": "PROSHARES SHORT BITCOIN ETF",
      "exchange": "P",
      "exchangeName": "NYSE Arca",
      "isHardToBorrow": true,
      "isShortable": true,
      "htbRate": -6.5
    }
  },
  "AAPL": {
    "assetMainType": "EQUITY",
    "assetSubType": "COE",
    "quoteType": "NFL",
    "realtime": false,
    "ssid": 1973757747,
    "symbol": "AAPL",
    "quote": {
      "52WeekHigh": 260.1,
      "52WeekLow": 164.075,
      "askMICId": "BATS",
      "askPrice": 229.85,
      "askSize": 0,
      "askTime": 1737161982475,
      "bidMICId": "BATS",
      "bidPrice": 229.47,
      "bidSize": 0,
      "bidTime": 1737161982475,
      "closePrice": 228.26,
      "highPrice": 232.29,
      "lastMICId": "LTSE",
      "lastPrice": 229.499,
      "lastSize": 40,
      "lowPrice": 228.48,
      "mark": 229.98,
      "markChange": 1.72,
      "markPercentChange": 0.75352668,
      "netChange": 1.239,
      "netPercentChange": 0.54280207,
      "openPrice": 232.09,
      "postMarketChange": -0.481,
      "postMarketPercentChange": -0.20914862,
      "quoteTime": 1737161982475,
      "securityStatus": "Normal",
      "totalVolume": 68488301,
      "tradeTime": 1737161996865
    },
    "reference": {
      "cusip": "037833100",
      "description": "APPLE INC",
      "exchange": "Q",
      "exchangeName": "NASDAQ",
      "isHardToBorrow": false,
      "isShortable": true,
      "htbRate": 0
    }
  },
  "BAC": {
    "assetMainType": "EQUITY",
    "assetSubType": "COE",
    "quoteType": "NFL",
    "realtime": false,
    "ssid": 851234497,
    "symbol": "BAC",
    "quote": {
      "52WeekHigh": 48.08,
      "52WeekLow": 31.4,
      "askMICId": "BATS",
      "askPrice": 46.7,
      "askSize": 11,
      "askTime": 1737161273452,
      "bidMICId": "XNAS",
      "bidPrice": 46.53,
      "bidSize": 4,
      "bidTime": 1737161273452,
      "closePrice": 46.64,
      "highPrice": 46.88,
      "lastMICId": "LTSE",
      "lastPrice": 46.6004,
      "lastSize": 200,
      "lowPrice": 46.08,
      "mark": 46.53,
      "markChange": -0.11,
      "markPercentChange": -0.23584906,
      "netChange": -0.0396,
      "netPercentChange": -0.08490566,
      "openPrice": 46.48,
      "postMarketChange": 0.0704,
      "postMarketPercentChange": 0.15130024,
      "quoteTime": 1737161273452,
      "securityStatus": "Normal",
      "totalVolume": 44486094,
      "tradeTime": 1737161902458
    },
    "reference": {
      "cusip": "060505104",
      "description": "BANK OF AMERICA CORP",
      "exchange": "N",
      "exchangeName": "NYSE",
      "isHardToBorrow": false,
      "isShortable": true,
      "htbRate": 0
    }
  },
  "AAAHX": {
    "assetMainType": "MUTUAL_FUND",
    "assetSubType": "OEF",
    "realtime": true,
    "ssid": 69527084,
    "symbol": "AAAHX",
    "quote": {
      "52WeekHigh": 10.42,
      "52WeekLow": 9.4,
      "lastPrice": 9.86,
      "closePrice": 9.83,
      "nAV": 9.86,
      "netChange": 0.03,
      "netPercentChange": 0.3051882,
      "securityStatus": "Normal",
      "tradeTime": 1737157500000
    },
    "reference": {
      "cusip": "02507J789",
      "description": "AMERICAN CENTURY ONE CHC BLND+ 2015 I",
      "exchange": "3",
      "exchangeName": "Mutual Fund"
    }
  },
  "AAAIX": {
    "assetMainType": "MUTUAL_FUND",
    "assetSubType": "OEF",
    "realtime": true,
    "ssid": 1271526288,
    "symbol": "AAAIX",
    "quote": {
      "52WeekHigh": 8.69,
      "52WeekLow": 7.27,
      "lastPrice": 7.91,
      "closePrice": 7.87,
      "nAV": 7.91,
      "netChange": 0.04,
      "netPercentChange": 0.50825921,
      "securityStatus": "Normal",
      "tradeTime": 1737157500000
    },
    "reference": {
      "cusip": "025085853",
      "description": "AMERICAN CENTURY STRAT ALLC: AGRSV I",
      "exchange": "3",
      "exchangeName": "Mutual Fund"
    }
  },
  "$DJI": {
    "assetMainType": "INDEX",
    "realtime": true,
    "ssid": 107184833,
    "symbol": "$DJI",
    "quote": {
      "52WeekHigh": 45073.63,
      "52WeekLow": 37122.95,
      "closePrice": 43487.83,
      "highPrice": 43653.25,
      "lastPrice": 43487.83,
      "lowPrice": 43312.55,
      "netChange": 0,
      "netPercentChange": 0,
      "openPrice": 43312.55,
      "securityStatus": "Closed",
      "totalVolume": 558951378,
      "tradeTime": 1737151905000
    },
    "reference": {
      "description": "Dow Jones Industrial Average",
      "exchange": "0",
      "exchangeName": "Index"
    }
  },
  "$SPX": {
    "assetMainType": "INDEX",
    "realtime": true,
    "ssid": 1819771877,
    "symbol": "$SPX",
    "quote": {
      "52WeekHigh": 6099.97,
      "52WeekLow": 4714.82,
      "closePrice": 5996.66,
      "highPrice": 6014.96,
      "lastPrice": 5996.66,
      "lowPrice": 5978.44,
      "netChange": 0,
      "netPercentChange": 0,
      "openPrice": 5995.4,
      "securityStatus": "Closed",
      "totalVolume": 2988514444,
      "tradeTime": 1737151905473
    },
    "reference": {
      "description": "S&P 500 INDEX",
      "exchange": "0",
      "exchangeName": "Index"
    }
  },
  "SOBS": {
    "assetMainType": "EQUITY",
    "assetSubType": "COE",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 561081427,
    "symbol": "SOBS",
    "quote": {
      "52WeekHigh": 32.7,
      "52WeekLow": 22.9,
      "askPrice": 34,
      "askSize": 0,
      "askTime": 1737151201028,
      "bidPrice": 25.05,
      "bidSize": 0,
      "bidTime": 1737151201028,
      "closePrice": 26.5,
      "highPrice": 0,
      "lastPrice": 26.5,
      "lastSize": 370,
      "lowPrice": 0,
      "mark": 26.5,
      "markChange": 0,
      "markPercentChange": 0,
      "netChange": 0,
      "netPercentChange": 0,
      "openPrice": 0,
      "postMarketChange": 0,
      "postMarketPercentChange": 0,
      "quoteTime": 1737151201028,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 1736970264648
    },
    "reference": {
      "cusip": "83441Q105",
      "description": "SOLVAY BK CORP SOLVA",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "Pink Current",
      "isHardToBorrow": true,
      "isShortable": true,
      "htbRate": 0
    }
  },
  "TOITF": {
    "assetMainType": "EQUITY",
    "assetSubType": "COE",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 68444487,
    "symbol": "TOITF",
    "quote": {
      "52WeekHigh": 103,
      "52WeekLow": 73.89,
      "askPrice": 135.98,
      "askSize": 0,
      "askTime": 1737151202076,
      "bidPrice": 89.99,
      "bidSize": 0,
      "bidTime": 1737151202076,
      "closePrice": 89.705,
      "highPrice": 91.0329,
      "lastMICId": "XOTC",
      "lastPrice": 91.594984,
      "lastSize": 3400,
      "lowPrice": 89.59,
      "mark": 90.76,
      "markChange": 1.055,
      "markPercentChange": 1.17607714,
      "netChange": 1.889984,
      "netPercentChange": 2.10688813,
      "openPrice": 89.59,
      "postMarketChange": 0.834984,
      "postMarketPercentChange": 0.91999119,
      "quoteTime": 1737151202076,
      "securityStatus": "Normal",
      "totalVolume": 13626,
      "tradeTime": 1737149787708
    },
    "reference": {
      "cusip": "89072T102",
      "description": "TOPICUS COM INC",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "Pink Current",
      "isHardToBorrow": true,
      "isShortable": true,
      "htbRate": 0
    }
  },
  "CNSWF": {
    "assetMainType": "EQUITY",
    "assetSubType": "COE",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 807850646,
    "symbol": "CNSWF",
    "quote": {
      "52WeekHigh": 3450,
      "52WeekLow": 2575.55,
      "askPrice": 3341.26,
      "askSize": 0,
      "askTime": 1737151203698,
      "bidPrice": 2766.42,
      "bidSize": 0,
      "bidTime": 1737151203698,
      "closePrice": 3063.517,
      "highPrice": 3085.1,
      "lastMICId": "XOTC",
      "lastPrice": 3032.366,
      "lastSize": 2,
      "lowPrice": 3030,
      "mark": 3032.366,
      "markChange": -31.151,
      "markPercentChange": -1.01683784,
      "netChange": -31.151,
      "netPercentChange": -1.01683784,
      "openPrice": 3046,
      "postMarketChange": 0,
      "postMarketPercentChange": 0,
      "quoteTime": 1737151203698,
      "securityStatus": "Normal",
      "totalVolume": 553,
      "tradeTime": 1737147571238
    },
    "reference": {
      "cusip": "21037X100",
      "description": "CONSTELLATION SOFTWA",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "Pink Current",
      "isHardToBorrow": true,
      "isShortable": true,
      "htbRate": 0
    }
  },
  "AUD/CAD": {
    "assetMainType": "FOREX",
    "realtime": true,
    "symbol": "AUD/CAD",
    "quote": {
      "52WeekHigh": 0,
      "52WeekLow": 0,
      "askPrice": 0,
      "askSize": 0,
      "bidPrice": 0,
      "bidSize": 0,
      "closePrice": 0.89401,
      "highPrice": 0,
      "lastPrice": 0,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 0,
      "netChange": -0.89401,
      "netPercentChange": -100,
      "openPrice": 0,
      "quoteTime": 0,
      "securityStatus": "Unknown",
      "tick": 0,
      "tickAmount": 0,
      "totalVolume": 0,
      "tradeTime": 0
    },
    "reference": {
      "description": "AusDollar/Canadian Dollar Spot",
      "exchange": "!",
      "exchangeName": "GFT",
      "isTradable": false
    }
  },
  "errors": {
    "invalidSymbols": [
      "MVEN",
      "AMZN  230317C01360000",
      "DJX   231215C00290000",
      "/ESH23",
      "./ADUF23C0.55"
    ]
  }
}
Response headers
 cache-control: no-store 
 content-length: 2080 
 content-type: application/json;charset=UTF-8 
 expires: -1 
 pragma: no-cache 
Responses
Code	Description	Links
200	
Quote Response

Media type

application/json
Controls Accept header.
Examples

Search by Symbols+Cusips+SSIDs
Example Value
Schema
{
  "AAPL": {
    "assetMainType": "EQUITY",
    "symbol": "AAPL",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 1973757747,
    "reference": {
      "cusip": "037833100",
      "description": "Apple Inc",
      "exchange": "Q",
      "exchangeName": "NASDAQ"
    },
    "quote": {
      "52WeekHigh": 169,
      "52WeekLow": 1.1,
      "askMICId": "MEMX",
      "askPrice": 168.41,
      "askSize": 400,
      "askTime": 1644854683672,
      "bidMICId": "IEGX",
      "bidPrice": 168.4,
      "bidSize": 400,
      "bidTime": 1644854683633,
      "closePrice": 177.57,
      "highPrice": 169,
      "lastMICId": "XADF",
      "lastPrice": 168.405,
      "lastSize": 200,
      "lowPrice": 167.09,
      "mark": 168.405,
      "markChange": -9.164999999999992,
      "markPercentChange": -5.161344821760428,
      "netChange": -9.165,
      "netPercentChange": -5.161344821760428,
      "openPrice": 167.37,
      "quoteTime": 1644854683672,
      "securityStatus": "Normal",
      "totalVolume": 22361159,
      "tradeTime": 1644854683408,
      "volatility": 0.0347
    },
    "regular": {
      "regularMarketLastPrice": 168.405,
      "regularMarketLastSize": 2,
      "regularMarketNetChange": -9.165,
      "regularMarketPercentChange": -5.161344821760428,
      "regularMarketTradeTime": 1644854683408
    },
    "fundamental": {
      "avg10DaysVolume": 1,
      "avg1YearVolume": 0,
      "divAmount": 1.1,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 1.1,
      "eps": 0,
      "fundLeverageFactor": 1.1,
      "peRatio": 1.1
    }
  },
  "AAAIX": {
    "assetMainType": "MUTUAL_FUND",
    "symbol": "AAAIX",
    "realtime": true,
    "ssid": -1,
    "reference": {
      "cusip": "025085853",
      "description": "American Century Strategic Allocation: Aggressive Fund - I Class",
      "exchange": "3",
      "exchangeName": "Mutual Fund"
    },
    "quote": {
      "52WeekHigh": 9.24,
      "52WeekLow": 7.48,
      "closePrice": 9.12,
      "nAV": 0,
      "netChange": -0.03,
      "netPercentChange": -0.32894736842104566,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 0
    },
    "fundamental": {
      "avg10DaysVolume": 0,
      "avg1YearVolume": 0,
      "divAmount": 0,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 0.83059,
      "eps": 0,
      "fundLeverageFactor": 0,
      "peRatio": 0
    }
  },
  "AAAHX": {
    "assetMainType": "MUTUAL_FUND",
    "symbol": "AAAHX",
    "realtime": true,
    "ssid": -1,
    "reference": {
      "cusip": "02507J789",
      "description": "One Choice Blend+ 2015 Portfolio  I Class",
      "exchange": "3",
      "exchangeName": "Mutual Fund"
    },
    "quote": {
      "52WeekHigh": 10.64,
      "52WeekLow": 9.95,
      "closePrice": 10.53,
      "nAV": 0,
      "netChange": 0,
      "netPercentChange": 0,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 0
    },
    "fundamental": {
      "avg10DaysVolume": 0,
      "avg1YearVolume": 0,
      "divAmount": 0,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 0,
      "eps": 0,
      "fundLeverageFactor": 0,
      "peRatio": 0
    }
  },
  "BAC": {
    "assetMainType": "EQUITY",
    "symbol": "BAC",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 851234497,
    "reference": {
      "cusip": "060505104",
      "description": "Bank Of America Corp",
      "exchange": "N",
      "exchangeName": "NYSE"
    },
    "quote": {
      "52WeekHigh": 48.185,
      "52WeekLow": 22.95,
      "askMICId": "XNYS",
      "askPrice": 47.2,
      "askSize": 2100,
      "askTime": 1644854683639,
      "bidMICId": "XNYS",
      "bidPrice": 47.19,
      "bidSize": 3700,
      "bidTime": 1644854683640,
      "closePrice": 44.49,
      "highPrice": 48.185,
      "lastMICId": "ARCX",
      "lastPrice": 47.195,
      "lastSize": 200,
      "lowPrice": 47.06,
      "mark": 47.195,
      "markChange": 2.7049999999999983,
      "markPercentChange": 6.080017981568888,
      "netChange": 2.705,
      "netPercentChange": 6.080017981568888,
      "openPrice": 48.02,
      "quoteTime": 1644854683640,
      "securityStatus": "Normal",
      "totalVolume": 13573182,
      "tradeTime": 1644854683638,
      "volatility": 0.0206
    },
    "regular": {
      "regularMarketLastPrice": 47.195,
      "regularMarketLastSize": 2,
      "regularMarketNetChange": 2.705,
      "regularMarketPercentChange": 6.080017981568888,
      "regularMarketTradeTime": 1644854683638
    },
    "fundamental": {
      "avg10DaysVolume": 43411957,
      "avg1YearVolume": 40653250,
      "declarationDate": "2021-07-21T05:00:00Z",
      "divAmount": 0.75,
      "divExDate": "2021-09-02T05:00:00Z",
      "divFreq": 4,
      "divPayAmount": 0.75,
      "divPayDate": "2021-09-24T05:00:00Z",
      "divYield": 1.77,
      "eps": 2.996,
      "fundLeverageFactor": 0,
      "nextDivExDate": "2021-12-27T06:00:00Z",
      "nextDivPayDate": "2021-12-27T06:00:00Z",
      "peRatio": 13.50133
    }
  },
  "$SPX": {
    "assetMainType": "INDEX",
    "symbol": "$SPX",
    "realtime": true,
    "ssid": 1819771877,
    "reference": {
      "description": "S&P DOW JONES INDEX            S&P 500",
      "exchange": "0",
      "exchangeName": "Index"
    },
    "quote": {
      "52WeekHigh": 4423.46,
      "52WeekLow": 4385.52,
      "closePrice": 4766.18,
      "highPrice": 4423.46,
      "lastPrice": 4396.2,
      "lowPrice": 4385.52,
      "netChange": -369.98,
      "netPercentChange": -7.762610728088331,
      "openPrice": 4412.61,
      "securityStatus": "Unknown",
      "totalVolume": 628009977,
      "tradeTime": 1644854683056
    }
  },
  "MRAD": {
    "assetMainType": "EQUITY",
    "assetSubType": "ETF",
    "symbol": "MRAD",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 67229687,
    "reference": {
      "cusip": "402031868",
      "description": "Guinness Atkinson Fds SMART ETFS ADVERTISING MKT TCH ETF",
      "exchange": "P",
      "exchangeName": "NYSE Arca"
    },
    "quote": {
      "52WeekHigh": 31.96,
      "52WeekLow": 22.18,
      "askMICId": "IEGX",
      "askPrice": 22.29,
      "askSize": 500,
      "askTime": 1644854676848,
      "bidMICId": "EDGX",
      "bidPrice": 22.22,
      "bidSize": 500,
      "bidTime": 1644854681062,
      "closePrice": 26.8633,
      "highPrice": 22.18,
      "lastPrice": 22.18,
      "lastSize": 100,
      "lowPrice": 22.18,
      "mark": 22.22,
      "markChange": -4.6433,
      "markPercentChange": -17.284920318799255,
      "netChange": -4.6833,
      "netPercentChange": -17.433822352428777,
      "openPrice": 22.18,
      "quoteTime": 1644854681062,
      "securityStatus": "Normal",
      "totalVolume": 100,
      "tradeTime": 1644851921969,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 22.18,
      "regularMarketLastSize": 1,
      "regularMarketNetChange": -4.6833,
      "regularMarketPercentChange": -17.433822352428777,
      "regularMarketTradeTime": 1644851921969
    },
    "fundamental": {
      "avg10DaysVolume": 1606,
      "avg1YearVolume": 0,
      "divAmount": 0,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 0,
      "eps": 0,
      "fundLeverageFactor": 0,
      "fundStrategy": "A",
      "peRatio": 0
    }
  },
  "EBIZ": {
    "assetMainType": "EQUITY",
    "assetSubType": "ETF",
    "symbol": "EBIZ",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 52313178,
    "reference": {
      "cusip": "37954Y467",
      "description": "GLOBAL X E-COMMERCE ETF",
      "exchange": "Q",
      "exchangeName": "NASDAQ"
    },
    "quote": {
      "52WeekHigh": 37.9754,
      "52WeekLow": 24.52,
      "askMICId": "XNAS",
      "askPrice": 24.85,
      "askSize": 200,
      "askTime": 1644854683318,
      "bidMICId": "XNAS",
      "bidPrice": 24.79,
      "bidSize": 200,
      "bidTime": 1644854683318,
      "closePrice": 27.45,
      "highPrice": 24.8303,
      "lastMICId": "XADF",
      "lastPrice": 24.8303,
      "lastSize": 100,
      "lowPrice": 24.52,
      "mark": 24.8303,
      "markChange": -2.619699999999998,
      "markPercentChange": -9.543533697632052,
      "netChange": -2.6197,
      "netPercentChange": -9.543533697632052,
      "openPrice": 24.55,
      "quoteTime": 1644854683318,
      "securityStatus": "Normal",
      "totalVolume": 1626,
      "tradeTime": 1644850278470,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 24.8303,
      "regularMarketLastSize": 1,
      "regularMarketNetChange": -2.6197,
      "regularMarketPercentChange": -9.543533697632052,
      "regularMarketTradeTime": 1644850278470
    },
    "fundamental": {
      "avg10DaysVolume": 0,
      "avg1YearVolume": 0,
      "declarationDate": "2020-12-29T06:00:00Z",
      "divAmount": 0,
      "divExDate": "2020-12-30T06:00:00Z",
      "divFreq": 1,
      "divPayAmount": 0.26641,
      "divPayDate": "2021-01-08T06:00:00Z",
      "divYield": 0.88276,
      "eps": 0,
      "fundLeverageFactor": 0,
      "fundStrategy": "P",
      "nextDivExDate": "2022-01-10T06:00:00Z",
      "nextDivPayDate": "2022-01-10T06:00:00Z",
      "peRatio": 0
    }
  },
  "$DJI": {
    "assetMainType": "INDEX",
    "symbol": "$DJI",
    "realtime": true,
    "ssid": 0,
    "reference": {
      "description": "Dow Jones Industrial Average",
      "exchange": "0",
      "exchangeName": "Index"
    },
    "quote": {
      "52WeekHigh": 34744.56,
      "52WeekLow": 34364.39,
      "closePrice": 34738.06,
      "highPrice": 34744.56,
      "lastPrice": 34436.13,
      "lowPrice": 34364.39,
      "netChange": -301.93,
      "netPercentChange": -0.8691619508976618,
      "openPrice": 34694.5,
      "securityStatus": "Unknown",
      "totalVolume": 106647543,
      "tradeTime": 1644854683055
    }
  },
  "AMZN  220617C03170000": {
    "assetMainType": "OPTION",
    "symbol": "AMZN  220617C03170000",
    "realtime": true,
    "ssid": 72507798,
    "reference": {
      "contractType": "C",
      "daysToExpiration": 123,
      "description": "Amazon.com Inc 06/17/2022 $3170 Call",
      "exchange": "o",
      "exchangeName": "OPR",
      "expirationDay": 17,
      "expirationMonth": 6,
      "expirationYear": 2022,
      "isPennyPilot": true,
      "lastTradingDay": 1655510400000,
      "multiplier": 100,
      "settlementType": "P",
      "strikePrice": 3170,
      "underlying": "AMZN",
      "uvExpirationType": "S"
    },
    "quote": {
      "askPrice": 223,
      "askSize": 2,
      "askTime": 0,
      "bidPrice": 217.65,
      "bidSize": 2,
      "bidTime": 0,
      "closePrice": 357.75,
      "delta": 0.5106,
      "gamma": 0.0007,
      "highPrice": 0,
      "impliedYield": 0.042,
      "indAskPrice": 0,
      "indBidPrice": 0,
      "indQuoteTime": 0,
      "lastPrice": 0,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 220.325,
      "markChange": -137.425,
      "markPercentChange": -38.41369671558351,
      "moneyIntrinsicValue": -40.795,
      "netChange": 0,
      "netPercentChange": 0,
      "openInterest": 0,
      "openPrice": 0,
      "quoteTime": 1644854683379,
      "rho": 4.5173,
      "securityStatus": "Normal",
      "theoreticalOptionValue": 221.4,
      "theta": -0.9619,
      "timeValue": 220.325,
      "totalVolume": 0,
      "tradeTime": 0,
      "underlyingPrice": 3129.205,
      "vega": 7.1633,
      "volatility": 32.8918
    }
  },
  "DJX   231215C00290000": {
    "assetMainType": "OPTION",
    "symbol": "DJX   231215C00290000",
    "realtime": true,
    "ssid": 69272575,
    "reference": {
      "contractType": "C",
      "daysToExpiration": 669,
      "description": "DOW JONES INDUS IND 12/15/2023 $290 Call",
      "exchange": "o",
      "exchangeName": "OPR",
      "expirationDay": 15,
      "expirationMonth": 12,
      "expirationYear": 2023,
      "isPennyPilot": true,
      "lastTradingDay": 1702602000000,
      "multiplier": 100,
      "settlementType": "A",
      "strikePrice": 290,
      "underlying": "$DJX",
      "uvExpirationType": "S"
    },
    "quote": {
      "askPrice": 76.95,
      "askSize": 11,
      "askTime": 0,
      "bidPrice": 70.9,
      "bidSize": 11,
      "bidTime": 0,
      "closePrice": 86.2,
      "delta": 0,
      "gamma": 0,
      "highPrice": 0,
      "impliedYield": 0,
      "indAskPrice": 79.55,
      "indBidPrice": 73.25,
      "indQuoteTime": 1644614546536,
      "lastPrice": 0,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 73.925,
      "markChange": -12.274999999999991,
      "markPercentChange": -14.24013921113688,
      "moneyIntrinsicValue": 0,
      "netChange": 0,
      "netPercentChange": 0,
      "openInterest": 0,
      "openPrice": 0,
      "quoteTime": 1644854648305,
      "rho": 0,
      "securityStatus": "Normal",
      "theoreticalOptionValue": 0,
      "theta": 0,
      "timeValue": 0,
      "totalVolume": 0,
      "tradeTime": 0,
      "underlyingPrice": 0,
      "vega": -999,
      "volatility": 0
    }
  },
  "TOITF": {
    "assetMainType": "EQUITY",
    "symbol": "TOITF",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 68444487,
    "reference": {
      "cusip": "89072T102",
      "description": "TOPICUS COM INC",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "PC"
    },
    "quote": {
      "52WeekHigh": 75.702,
      "52WeekLow": 45.3933,
      "askPrice": 75.978,
      "askSize": 10000,
      "askTime": 1644849000209,
      "bidPrice": 72.5951,
      "bidSize": 10000,
      "bidTime": 1644849000209,
      "closePrice": 92.7,
      "highPrice": 75.702,
      "lastPrice": 75.702,
      "lastSize": 100,
      "lowPrice": 72.5478,
      "mark": 75.702,
      "netChange": -16.998,
      "openPrice": 74.8977,
      "quoteTime": 1644854676927,
      "securityStatus": "Normal",
      "totalVolume": 4274,
      "tradeTime": 1644854585000,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 75.702,
      "regularMarketLastSize": 1,
      "regularMarketNetChange": -16.998,
      "regularMarketTradeTime": 1644854585000
    }
  },
  "EATOF": {
    "assetMainType": "EQUITY",
    "assetSubType": "ETF",
    "symbol": "EATOF",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 43253301,
    "reference": {
      "cusip": "30052J102",
      "description": "EVOLVE AUTMBL INVTN INDX ETF",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "EM"
    },
    "quote": {
      "52WeekHigh": 47.1993,
      "52WeekLow": 24.2835,
      "askPrice": 33.1512,
      "askSize": 400000,
      "askTime": 1644849000044,
      "bidPrice": 33.0487,
      "bidSize": 250000,
      "bidTime": 1644849000044,
      "closePrice": 40.198,
      "highPrice": 33.1196,
      "lastPrice": 33.1196,
      "lastSize": 200,
      "lowPrice": 32.82,
      "mark": 33.1196,
      "netChange": -7.0784,
      "openPrice": 32.82,
      "quoteTime": 1644854660496,
      "securityStatus": "Normal",
      "totalVolume": 1017,
      "tradeTime": 1644850274000,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 33.1196,
      "regularMarketLastSize": 2,
      "regularMarketNetChange": -7.0784,
      "regularMarketTradeTime": 1644850274000
    }
  },
  "CNSWF": {
    "assetMainType": "EQUITY",
    "symbol": "CNSWF",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 807850646,
    "reference": {
      "cusip": "21037X100",
      "description": "Constellation Softwr",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "PC"
    },
    "quote": {
      "52WeekHigh": 1709.738,
      "52WeekLow": 904.0901,
      "askPrice": 1693.4699,
      "askSize": 30000,
      "askTime": 1644849000567,
      "bidPrice": 1688.4547,
      "bidSize": 20000,
      "bidTime": 1644849000567,
      "closePrice": 1856.4626,
      "highPrice": 1709.738,
      "lastPrice": 1693.4541,
      "lastSize": 100,
      "lowPrice": 1680.1511,
      "mark": 1693.4541,
      "netChange": -163.0084,
      "openPrice": 1682.0121,
      "quoteTime": 1644854655233,
      "securityStatus": "Normal",
      "totalVolume": 13901,
      "tradeTime": 1644854560000,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 1693.4541,
      "regularMarketLastSize": 1,
      "regularMarketNetChange": -163.0084,
      "regularMarketTradeTime": 1644854560000
    }
  },
  "MVEN": {
    "assetMainType": "EQUITY",
    "symbol": "MVEN",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 39225080,
    "reference": {
      "cusip": "88339B102",
      "description": "Themaven Inc",
      "exchange": "u",
      "exchangeName": "Nasdaq OTCBB",
      "otcMarketTier": "QX"
    },
    "quote": {
      "52WeekHigh": 3,
      "52WeekLow": 0.42,
      "askPrice": 0,
      "askSize": 0,
      "askTime": 0,
      "bidPrice": 0,
      "bidSize": 0,
      "bidTime": 0,
      "closePrice": 13.42,
      "highPrice": 0,
      "lastPrice": 0.42,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 0.42,
      "markChange": -13,
      "markPercentChange": -96.87034277198212,
      "netChange": -13,
      "netPercentChange": -96.87034277198212,
      "openPrice": 0,
      "quoteTime": 0,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 1644353952708,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 0.42,
      "regularMarketLastSize": 0,
      "regularMarketNetChange": -13,
      "regularMarketPercentChange": -96.87034277198212,
      "regularMarketTradeTime": 1644353952708
    },
    "fundamental": {
      "avg10DaysVolume": 299530,
      "avg1YearVolume": 430760,
      "divAmount": 0,
      "divFreq": 0,
      "divPayAmount": 0,
      "divYield": 0,
      "eps": 0,
      "fundLeverageFactor": 0,
      "peRatio": -0.68777
    }
  },
  "SOBS": {
    "assetMainType": "EQUITY",
    "symbol": "SOBS",
    "quoteType": "NBBO",
    "realtime": true,
    "ssid": 561081427,
    "reference": {
      "cusip": "83441Q105",
      "description": "Solvay Bank Corp Sol",
      "exchange": "9",
      "exchangeName": "OTC Markets",
      "otcMarketTier": "PC"
    },
    "quote": {
      "52WeekHigh": 43,
      "52WeekLow": 30.28,
      "askPrice": 45,
      "askSize": 200,
      "askTime": 0,
      "bidPrice": 39,
      "bidSize": 100,
      "bidTime": 0,
      "closePrice": 38.219,
      "highPrice": 0,
      "lastPrice": 38.219,
      "lastSize": 0,
      "lowPrice": 0,
      "mark": 38.219,
      "markChange": 0,
      "markPercentChange": 0,
      "netChange": 0,
      "netPercentChange": 0,
      "openPrice": 0,
      "quoteTime": 1644613200189,
      "securityStatus": "Normal",
      "totalVolume": 0,
      "tradeTime": 0,
      "volatility": 0
    },
    "regular": {
      "regularMarketLastPrice": 38.219,
      "regularMarketLastSize": 0,
      "regularMarketNetChange": 0,
      "regularMarketPercentChange": 0,
      "regularMarketTradeTime": 0
    },
    "fundamental": {
      "avg10DaysVolume": 1296,
      "avg1YearVolume": 0,
      "declarationDate": "2021-09-21T05:00:00Z",
      "divAmount": 1.48,
      "divExDate": "2021-09-30T05:00:00Z",
      "divFreq": 4,
      "divPayAmount": 1.47,
      "divPayDate": "2021-10-29T05:00:00Z",
      "divYield": 3.869,
      "eps": 0,
      "fundLeverageFactor": 0,
      "nextDivExDate": "2022-01-31T06:00:00Z",
      "nextDivPayDate": "2022-01-31T06:00:00Z",
      "peRatio": 0
    }
  },
  "/ESZ21": {
    "assetMainType": "FUTURE",
    "symbol": "/ESZ21",
    "realtime": true,
    "ssid": 0,
    "reference": {
      "description": "E-mini S&P 500 Index Futures,Dec-2021,ETH",
      "exchange": "@",
      "exchangeName": "XCME",
      "futureActiveSymbol": "/ESZ21",
      "futureExpirationDate": 1639717200000,
      "futureIsActive": true,
      "futureIsTradable": true,
      "futureMultiplier": 50,
      "futurePriceFormat": "D,D",
      "futureSettlementPrice": 4696,
      "futureTradingHours": "GLBX(de=1640;0=-17001600;1=r-17001600d-15551640;7=d-16401555)",
      "product": "/ES"
    },
    "quote": {
      "askPrice": 4694.5,
      "askSize": 113,
      "askTime": 0,
      "bidPrice": 4694.25,
      "bidSize": 57,
      "bidTime": 0,
      "netChange": -1.5,
      "closePrice": 4696,
      "futurePercentChange": -0.0003,
      "highPrice": 4701,
      "lastPrice": 4694.5,
      "lastSize": 3,
      "lowPrice": 4679.25,
      "mark": 0,
      "openInterest": 2328678,
      "openPrice": 4696.5,
      "quoteTime": 1637168671400,
      "securityStatus": "Unknown",
      "settleTime": 0,
      "tick": 0.25,
      "tickAmount": 12.5,
      "totalVolume": 550778,
      "tradeTime": 1637168671399
    }
  },
  "EUR/USD": {
    "assetMainType": "FOREX",
    "symbol": "EUR/USD",
    "ssid": 1,
    "realtime": true,
    "reference": {
      "description": "Euro/USDollar Spot",
      "exchange": "T",
      "exchangeName": "GFT",
      "isTradable": false,
      "marketMaker": "",
      "product": "",
      "tradingHours": ""
    },
    "quote": {
      "52WeekHigh": 1.135,
      "52WeekLow": 1.1331,
      "askPrice": 1.13456,
      "askSize": 1000000,
      "bidPrice": 1.13434,
      "bidSize": 1000000,
      "netChange": 0.00254,
      "closePrice": 1.13191,
      "highPrice": 1.135,
      "lastPrice": 1.13445,
      "lastSize": 0,
      "lowPrice": 1.1331,
      "mark": 1.13445,
      "openPrice": 1.13324,
      "netPercentChange": 0,
      "quoteTime": 1637236739892,
      "securityStatus": "Unknown",
      "tick": 0,
      "tickAmount": 0,
      "totalVolume": 0,
      "tradeTime": 1637236739892
    }
  }
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Used to identify an individual request throughout the lifetime of the request and across systems.

string
Example: 0a7f446a-7d74-49c8-a1e5-ca8ed59a3386
No links
400	
Error response for generic client error 400

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "6808262e-52bb-4421-9d31-6c0e762e7dd5",
      "status": "400",
      "title": "Bad Request",
      "detail": "Missing header",
      "source": {
        "header": "Authorization"
      }
    },
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": "400",
      "title": "Bad Request",
      "detail": "Search combination should have min of 1.",
      "source": {
        "pointer": [
          "/data/attributes/symbols",
          "/data/attributes/cusips",
          "/data/attributes/ssids"
        ]
      }
    },
    {
      "id": "28485414-290f-42e2-992b-58ea3e3203b1",
      "status": "400",
      "title": "Bad Request",
      "detail": "valid fields should be any of all,fundamental,reference,extended,quote,regular or empty value",
      "source": {
        "parameter": "fields"
      }
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
401	
Error response for 401 Unauthorized

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "status": 401,
      "title": "Unauthorized",
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
No links
500	
Error response for 500 Internal Server Error

Media type

application/json
Example Value
Schema
{
  "errors": [
    {
      "id": "0be22ae7-efdf-44d9-99f4-f138049d76ca",
      "status": 500,
      "title": "Internal Server Error"
    }
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
This Correlation ID is unique to the operation. The GUID that is generated can be used to track an individual service call if support is needed.

string
Example: 977dbd7f-992e-44d2-a5f4-e213d29c8691
Schwab-Resource-Version	
This is the requested API version.

string
Example: 1
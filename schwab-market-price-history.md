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

BITI
periodType
string
(query)
The chart period being requested.


day
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

10
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


minute
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

1
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


true
needPreviousClose
boolean
(query)
Need previous close price/date


true
Responses
Curl

curl -X 'GET' \
  'https://api.schwabapi.com/marketdata/v1/pricehistory?symbol=BITI&periodType=day&period=10&frequencyType=minute&frequency=1&needExtendedHoursData=true&needPreviousClose=true' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer I0.b2F1dGgyLmNkYy5zY2h3YWIuY29t.Rg065wgsucrjWm6dwVRUrkr6mUvBjlc4c8kMn8EfU9w@'
Request URL
https://api.schwabapi.com/marketdata/v1/pricehistory?symbol=BITI&periodType=day&period=10&frequencyType=minute&frequency=1&needExtendedHoursData=true&needPreviousClose=true
Server response
Code	Details
200	
Response body
Download
{
  "candles": [
    {
      "open": 23.1,
      "high": 23.11,
      "low": 23.09,
      "close": 23.11,
      "volume": 795,
      "datetime": 1735905600000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 250,
      "datetime": 1735906020000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 538,
      "datetime": 1735906320000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 765,
      "datetime": 1735906860000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 1870,
      "datetime": 1735907100000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 800,
      "datetime": 1735907160000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.08,
      "close": 23.08,
      "volume": 800,
      "datetime": 1735907340000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 880,
      "datetime": 1735907400000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.07,
      "close": 23.07,
      "volume": 1500,
      "datetime": 1735907580000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 250,
      "datetime": 1735909260000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 100,
      "datetime": 1735909320000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 122,
      "datetime": 1735909500000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 8000,
      "datetime": 1735909920000
    },
    {
      "open": 23.1899,
      "high": 23.1899,
      "low": 23.1899,
      "close": 23.1899,
      "volume": 500,
      "datetime": 1735910160000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 270,
      "datetime": 1735910220000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 150,
      "datetime": 1735910460000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 235,
      "datetime": 1735910760000
    },
    {
      "open": 23.15,
      "high": 23.1599,
      "low": 23.15,
      "close": 23.1599,
      "volume": 700,
      "datetime": 1735911240000
    },
    {
      "open": 23.1502,
      "high": 23.1502,
      "low": 23.1502,
      "close": 23.1502,
      "volume": 1249,
      "datetime": 1735911480000
    },
    {
      "open": 23.1509,
      "high": 23.1699,
      "low": 23.15,
      "close": 23.16,
      "volume": 2425,
      "datetime": 1735911660000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 100,
      "datetime": 1735911720000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 100,
      "datetime": 1735911840000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 500,
      "datetime": 1735912380000
    },
    {
      "open": 23.1598,
      "high": 23.1598,
      "low": 23.1598,
      "close": 23.1598,
      "volume": 100,
      "datetime": 1735912560000
    },
    {
      "open": 23.1597,
      "high": 23.1597,
      "low": 23.1597,
      "close": 23.1597,
      "volume": 200,
      "datetime": 1735912620000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.16,
      "close": 23.16,
      "volume": 2784,
      "datetime": 1735912740000
    },
    {
      "open": 23.1599,
      "high": 23.1599,
      "low": 23.1599,
      "close": 23.1599,
      "volume": 100,
      "datetime": 1735912980000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 300,
      "datetime": 1735913160000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 2500,
      "datetime": 1735913220000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 2000,
      "datetime": 1735914000000
    },
    {
      "open": 23.06,
      "high": 23.0601,
      "low": 23.06,
      "close": 23.0601,
      "volume": 7998,
      "datetime": 1735914060000
    },
    {
      "open": 23.051,
      "high": 23.051,
      "low": 23.05,
      "close": 23.0501,
      "volume": 9699,
      "datetime": 1735914120000
    },
    {
      "open": 23.0501,
      "high": 23.0501,
      "low": 23.0498,
      "close": 23.0498,
      "volume": 1501,
      "datetime": 1735914180000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 9893,
      "datetime": 1735914240000
    },
    {
      "open": 23.02,
      "high": 23.07,
      "low": 23.02,
      "close": 23.0598,
      "volume": 8669,
      "datetime": 1735914600000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.01,
      "close": 23.01,
      "volume": 1252,
      "datetime": 1735914660000
    },
    {
      "open": 23.0332,
      "high": 23.035,
      "low": 23.03,
      "close": 23.03,
      "volume": 2600,
      "datetime": 1735914720000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 23,
      "close": 23.01,
      "volume": 1725,
      "datetime": 1735914780000
    },
    {
      "open": 23.02,
      "high": 23.07,
      "low": 23.02,
      "close": 23.07,
      "volume": 3862,
      "datetime": 1735914840000
    },
    {
      "open": 23.09,
      "high": 23.1,
      "low": 23.0899,
      "close": 23.09,
      "volume": 7186,
      "datetime": 1735914900000
    },
    {
      "open": 23.1,
      "high": 23.1323,
      "low": 23.1,
      "close": 23.125,
      "volume": 2773,
      "datetime": 1735914960000
    },
    {
      "open": 23.125,
      "high": 23.13,
      "low": 23.085,
      "close": 23.085,
      "volume": 2351,
      "datetime": 1735915020000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.01,
      "close": 23.01,
      "volume": 2166,
      "datetime": 1735915080000
    },
    {
      "open": 23.0002,
      "high": 23.0012,
      "low": 22.959,
      "close": 22.959,
      "volume": 8884,
      "datetime": 1735915140000
    },
    {
      "open": 22.95,
      "high": 22.9896,
      "low": 22.95,
      "close": 22.9802,
      "volume": 1600,
      "datetime": 1735915200000
    },
    {
      "open": 22.9902,
      "high": 22.9902,
      "low": 22.985,
      "close": 22.985,
      "volume": 1107,
      "datetime": 1735915260000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.9602,
      "close": 22.9654,
      "volume": 875,
      "datetime": 1735915320000
    },
    {
      "open": 22.979,
      "high": 22.99,
      "low": 22.979,
      "close": 22.99,
      "volume": 1059,
      "datetime": 1735915380000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.9799,
      "close": 22.982,
      "volume": 1512,
      "datetime": 1735915440000
    },
    {
      "open": 23,
      "high": 23.0328,
      "low": 23,
      "close": 23.0328,
      "volume": 1100,
      "datetime": 1735915500000
    },
    {
      "open": 23.03,
      "high": 23.05,
      "low": 23.02,
      "close": 23.021,
      "volume": 21132,
      "datetime": 1735915560000
    },
    {
      "open": 23.0599,
      "high": 23.0599,
      "low": 23.05,
      "close": 23.0597,
      "volume": 1000,
      "datetime": 1735915620000
    },
    {
      "open": 23.065,
      "high": 23.1,
      "low": 23.065,
      "close": 23.08,
      "volume": 3194,
      "datetime": 1735915680000
    },
    {
      "open": 23.0611,
      "high": 23.08,
      "low": 23.0546,
      "close": 23.0599,
      "volume": 58331,
      "datetime": 1735915740000
    },
    {
      "open": 23.055,
      "high": 23.0601,
      "low": 23.036,
      "close": 23.036,
      "volume": 32133,
      "datetime": 1735915800000
    },
    {
      "open": 23.045,
      "high": 23.12,
      "low": 23.045,
      "close": 23.11,
      "volume": 4103,
      "datetime": 1735915860000
    },
    {
      "open": 23.089,
      "high": 23.09,
      "low": 23.08,
      "close": 23.089,
      "volume": 2603,
      "datetime": 1735915920000
    },
    {
      "open": 23.085,
      "high": 23.085,
      "low": 23.065,
      "close": 23.065,
      "volume": 300,
      "datetime": 1735915980000
    },
    {
      "open": 23.05,
      "high": 23.08,
      "low": 23.05,
      "close": 23.0799,
      "volume": 300,
      "datetime": 1735916040000
    },
    {
      "open": 23.0599,
      "high": 23.0599,
      "low": 23.0599,
      "close": 23.0599,
      "volume": 300,
      "datetime": 1735916100000
    },
    {
      "open": 23.04,
      "high": 23.0519,
      "low": 23.035,
      "close": 23.05,
      "volume": 3883,
      "datetime": 1735916160000
    },
    {
      "open": 23.0399,
      "high": 23.0501,
      "low": 23.0371,
      "close": 23.05,
      "volume": 1949,
      "datetime": 1735916220000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.03,
      "close": 23.03,
      "volume": 4176,
      "datetime": 1735916280000
    },
    {
      "open": 23.02,
      "high": 23.0299,
      "low": 23.02,
      "close": 23.0299,
      "volume": 1300,
      "datetime": 1735916340000
    },
    {
      "open": 23.055,
      "high": 23.0699,
      "low": 23.03,
      "close": 23.03,
      "volume": 2100,
      "datetime": 1735916400000
    },
    {
      "open": 23.04,
      "high": 23.065,
      "low": 23.04,
      "close": 23.065,
      "volume": 1900,
      "datetime": 1735916460000
    },
    {
      "open": 23.06,
      "high": 23.066,
      "low": 23.0401,
      "close": 23.05,
      "volume": 1295,
      "datetime": 1735916520000
    },
    {
      "open": 23.0499,
      "high": 23.0499,
      "low": 23.0499,
      "close": 23.0499,
      "volume": 100,
      "datetime": 1735916580000
    },
    {
      "open": 23.01,
      "high": 23.0139,
      "low": 22.9798,
      "close": 22.9851,
      "volume": 4125,
      "datetime": 1735916700000
    },
    {
      "open": 22.97,
      "high": 23,
      "low": 22.97,
      "close": 23,
      "volume": 400,
      "datetime": 1735916760000
    },
    {
      "open": 23.0301,
      "high": 23.0301,
      "low": 22.99,
      "close": 23,
      "volume": 2136,
      "datetime": 1735916820000
    },
    {
      "open": 22.99,
      "high": 23,
      "low": 22.9726,
      "close": 22.98,
      "volume": 6959,
      "datetime": 1735916880000
    },
    {
      "open": 22.9999,
      "high": 22.9999,
      "low": 22.9968,
      "close": 22.9968,
      "volume": 300,
      "datetime": 1735916940000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.94,
      "close": 22.95,
      "volume": 1500,
      "datetime": 1735917000000
    },
    {
      "open": 22.975,
      "high": 23.01,
      "low": 22.9699,
      "close": 23.01,
      "volume": 1812,
      "datetime": 1735917060000
    },
    {
      "open": 23.025,
      "high": 23.0427,
      "low": 23.0199,
      "close": 23.04,
      "volume": 3443,
      "datetime": 1735917120000
    },
    {
      "open": 23.02,
      "high": 23.0301,
      "low": 23.01,
      "close": 23.01,
      "volume": 3763,
      "datetime": 1735917180000
    },
    {
      "open": 23.0082,
      "high": 23.025,
      "low": 23.0082,
      "close": 23.025,
      "volume": 200,
      "datetime": 1735917240000
    },
    {
      "open": 23.01,
      "high": 23.02,
      "low": 23.01,
      "close": 23.0199,
      "volume": 800,
      "datetime": 1735917300000
    },
    {
      "open": 23.02,
      "high": 23.0301,
      "low": 23,
      "close": 23.0301,
      "volume": 1700,
      "datetime": 1735917360000
    },
    {
      "open": 23.0199,
      "high": 23.05,
      "low": 23.0199,
      "close": 23.05,
      "volume": 3153,
      "datetime": 1735917420000
    },
    {
      "open": 23.05,
      "high": 23.0501,
      "low": 23.05,
      "close": 23.05,
      "volume": 2200,
      "datetime": 1735917480000
    },
    {
      "open": 23.05,
      "high": 23.07,
      "low": 23.0401,
      "close": 23.07,
      "volume": 1700,
      "datetime": 1735917540000
    },
    {
      "open": 23.06,
      "high": 23.0903,
      "low": 23.06,
      "close": 23.0903,
      "volume": 5799,
      "datetime": 1735917600000
    },
    {
      "open": 23.1,
      "high": 23.1103,
      "low": 23.1,
      "close": 23.11,
      "volume": 6244,
      "datetime": 1735917660000
    },
    {
      "open": 23.115,
      "high": 23.115,
      "low": 23.08,
      "close": 23.08,
      "volume": 3483,
      "datetime": 1735917720000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 200,
      "datetime": 1735917780000
    },
    {
      "open": 23.046,
      "high": 23.046,
      "low": 23.02,
      "close": 23.02,
      "volume": 425,
      "datetime": 1735917840000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.0099,
      "close": 23.0099,
      "volume": 2245,
      "datetime": 1735917900000
    },
    {
      "open": 23.015,
      "high": 23.015,
      "low": 22.9899,
      "close": 23.0066,
      "volume": 800,
      "datetime": 1735917960000
    },
    {
      "open": 22.98,
      "high": 22.99,
      "low": 22.97,
      "close": 22.99,
      "volume": 2095,
      "datetime": 1735918020000
    },
    {
      "open": 22.9902,
      "high": 22.9902,
      "low": 22.98,
      "close": 22.98,
      "volume": 200,
      "datetime": 1735918080000
    },
    {
      "open": 22.98,
      "high": 22.9801,
      "low": 22.9799,
      "close": 22.9799,
      "volume": 500,
      "datetime": 1735918140000
    },
    {
      "open": 22.98,
      "high": 23.0101,
      "low": 22.98,
      "close": 23.0073,
      "volume": 1400,
      "datetime": 1735918200000
    },
    {
      "open": 23.01,
      "high": 23.018676,
      "low": 22.9999,
      "close": 22.9999,
      "volume": 5503,
      "datetime": 1735918260000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.97,
      "close": 22.97,
      "volume": 2087,
      "datetime": 1735918320000
    },
    {
      "open": 22.96,
      "high": 22.97,
      "low": 22.96,
      "close": 22.96,
      "volume": 1248,
      "datetime": 1735918380000
    },
    {
      "open": 22.97,
      "high": 22.9701,
      "low": 22.96,
      "close": 22.96,
      "volume": 825,
      "datetime": 1735918440000
    },
    {
      "open": 22.96,
      "high": 22.97,
      "low": 22.938,
      "close": 22.938,
      "volume": 2479,
      "datetime": 1735918500000
    },
    {
      "open": 22.9402,
      "high": 22.9402,
      "low": 22.91,
      "close": 22.9102,
      "volume": 2350,
      "datetime": 1735918560000
    },
    {
      "open": 22.92,
      "high": 22.9351,
      "low": 22.91,
      "close": 22.9351,
      "volume": 4210,
      "datetime": 1735918620000
    },
    {
      "open": 22.9397,
      "high": 22.95,
      "low": 22.928,
      "close": 22.942,
      "volume": 1850,
      "datetime": 1735918680000
    },
    {
      "open": 22.935,
      "high": 22.935,
      "low": 22.9206,
      "close": 22.93,
      "volume": 1854,
      "datetime": 1735918740000
    },
    {
      "open": 22.939,
      "high": 22.95,
      "low": 22.93,
      "close": 22.93,
      "volume": 3800,
      "datetime": 1735918800000
    },
    {
      "open": 22.9197,
      "high": 22.9201,
      "low": 22.91,
      "close": 22.918,
      "volume": 1100,
      "datetime": 1735918860000
    },
    {
      "open": 22.915,
      "high": 22.9202,
      "low": 22.9099,
      "close": 22.91,
      "volume": 3400,
      "datetime": 1735918920000
    },
    {
      "open": 22.9154,
      "high": 22.9154,
      "low": 22.91,
      "close": 22.91,
      "volume": 2102,
      "datetime": 1735918980000
    },
    {
      "open": 22.91,
      "high": 22.932,
      "low": 22.91,
      "close": 22.93,
      "volume": 1400,
      "datetime": 1735919040000
    },
    {
      "open": 22.93,
      "high": 22.93,
      "low": 22.9001,
      "close": 22.91,
      "volume": 1697,
      "datetime": 1735919100000
    },
    {
      "open": 22.9099,
      "high": 22.91,
      "low": 22.8801,
      "close": 22.91,
      "volume": 1775,
      "datetime": 1735919160000
    },
    {
      "open": 22.92,
      "high": 22.9395,
      "low": 22.91,
      "close": 22.93,
      "volume": 1853,
      "datetime": 1735919220000
    },
    {
      "open": 22.92,
      "high": 22.9302,
      "low": 22.915,
      "close": 22.915,
      "volume": 4570,
      "datetime": 1735919280000
    },
    {
      "open": 22.92,
      "high": 22.9401,
      "low": 22.92,
      "close": 22.94,
      "volume": 1228,
      "datetime": 1735919340000
    },
    {
      "open": 22.9354,
      "high": 22.972,
      "low": 22.935,
      "close": 22.96,
      "volume": 4493,
      "datetime": 1735919400000
    },
    {
      "open": 22.9643,
      "high": 22.9643,
      "low": 22.9643,
      "close": 22.9643,
      "volume": 100,
      "datetime": 1735919460000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.94,
      "close": 22.94,
      "volume": 758,
      "datetime": 1735919520000
    },
    {
      "open": 22.93,
      "high": 22.955,
      "low": 22.9299,
      "close": 22.95,
      "volume": 890,
      "datetime": 1735919580000
    },
    {
      "open": 22.945,
      "high": 22.95,
      "low": 22.94,
      "close": 22.94,
      "volume": 1200,
      "datetime": 1735919640000
    },
    {
      "open": 22.93,
      "high": 22.9372,
      "low": 22.93,
      "close": 22.9372,
      "volume": 1100,
      "datetime": 1735919700000
    },
    {
      "open": 22.93,
      "high": 22.93,
      "low": 22.91,
      "close": 22.91,
      "volume": 500,
      "datetime": 1735919760000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.905,
      "close": 22.905,
      "volume": 300,
      "datetime": 1735919820000
    },
    {
      "open": 22.92,
      "high": 22.9201,
      "low": 22.9072,
      "close": 22.9072,
      "volume": 1408,
      "datetime": 1735919880000
    },
    {
      "open": 22.91,
      "high": 22.91,
      "low": 22.893,
      "close": 22.9099,
      "volume": 853,
      "datetime": 1735919940000
    },
    {
      "open": 22.9102,
      "high": 22.9102,
      "low": 22.89,
      "close": 22.89,
      "volume": 900,
      "datetime": 1735920000000
    },
    {
      "open": 22.87,
      "high": 22.87,
      "low": 22.8699,
      "close": 22.8699,
      "volume": 1220,
      "datetime": 1735920060000
    },
    {
      "open": 22.879175,
      "high": 22.9,
      "low": 22.879175,
      "close": 22.9,
      "volume": 4013,
      "datetime": 1735920120000
    },
    {
      "open": 22.89,
      "high": 22.9,
      "low": 22.87,
      "close": 22.87,
      "volume": 1600,
      "datetime": 1735920180000
    },
    {
      "open": 22.875,
      "high": 22.8799,
      "low": 22.865,
      "close": 22.8799,
      "volume": 2550,
      "datetime": 1735920240000
    },
    {
      "open": 22.89,
      "high": 22.9001,
      "low": 22.89,
      "close": 22.9001,
      "volume": 1500,
      "datetime": 1735920300000
    },
    {
      "open": 22.91,
      "high": 22.91,
      "low": 22.91,
      "close": 22.91,
      "volume": 190,
      "datetime": 1735920360000
    },
    {
      "open": 22.921,
      "high": 22.9227,
      "low": 22.9199,
      "close": 22.92,
      "volume": 845,
      "datetime": 1735920420000
    },
    {
      "open": 22.92,
      "high": 22.94,
      "low": 22.92,
      "close": 22.94,
      "volume": 1195,
      "datetime": 1735920480000
    },
    {
      "open": 22.93,
      "high": 22.9373,
      "low": 22.92,
      "close": 22.9373,
      "volume": 400,
      "datetime": 1735920540000
    },
    {
      "open": 22.92,
      "high": 22.94,
      "low": 22.92,
      "close": 22.9333,
      "volume": 1095,
      "datetime": 1735920600000
    },
    {
      "open": 22.93,
      "high": 22.9501,
      "low": 22.9259,
      "close": 22.9501,
      "volume": 2248,
      "datetime": 1735920660000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.93,
      "close": 22.9302,
      "volume": 3065,
      "datetime": 1735920720000
    },
    {
      "open": 22.9301,
      "high": 22.9301,
      "low": 22.9299,
      "close": 22.9299,
      "volume": 300,
      "datetime": 1735920780000
    },
    {
      "open": 22.9201,
      "high": 22.9201,
      "low": 22.9099,
      "close": 22.91,
      "volume": 1000,
      "datetime": 1735920840000
    },
    {
      "open": 22.895,
      "high": 22.895,
      "low": 22.8901,
      "close": 22.895,
      "volume": 800,
      "datetime": 1735920900000
    },
    {
      "open": 22.89,
      "high": 22.89,
      "low": 22.89,
      "close": 22.89,
      "volume": 100,
      "datetime": 1735920960000
    },
    {
      "open": 22.8705,
      "high": 22.8898,
      "low": 22.8705,
      "close": 22.88,
      "volume": 6564,
      "datetime": 1735921020000
    },
    {
      "open": 22.88,
      "high": 22.881,
      "low": 22.87,
      "close": 22.875,
      "volume": 2606,
      "datetime": 1735921080000
    },
    {
      "open": 22.87,
      "high": 22.87,
      "low": 22.86,
      "close": 22.865,
      "volume": 900,
      "datetime": 1735921140000
    },
    {
      "open": 22.85,
      "high": 22.8772,
      "low": 22.8403,
      "close": 22.8772,
      "volume": 4189,
      "datetime": 1735921200000
    },
    {
      "open": 22.87,
      "high": 22.87,
      "low": 22.85,
      "close": 22.85,
      "volume": 2590,
      "datetime": 1735921260000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.79,
      "close": 22.79,
      "volume": 13719,
      "datetime": 1735921320000
    },
    {
      "open": 22.79,
      "high": 22.79,
      "low": 22.725,
      "close": 22.73,
      "volume": 12739,
      "datetime": 1735921380000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.6902,
      "close": 22.7,
      "volume": 4596,
      "datetime": 1735921440000
    },
    {
      "open": 22.71,
      "high": 22.72,
      "low": 22.7015,
      "close": 22.7102,
      "volume": 31090,
      "datetime": 1735921500000
    },
    {
      "open": 22.71,
      "high": 22.71,
      "low": 22.68,
      "close": 22.681,
      "volume": 11500,
      "datetime": 1735921560000
    },
    {
      "open": 22.7001,
      "high": 22.73,
      "low": 22.6999,
      "close": 22.72,
      "volume": 4231,
      "datetime": 1735921620000
    },
    {
      "open": 22.7272,
      "high": 22.7473,
      "low": 22.7272,
      "close": 22.745,
      "volume": 1700,
      "datetime": 1735921680000
    },
    {
      "open": 22.78,
      "high": 22.78,
      "low": 22.78,
      "close": 22.78,
      "volume": 400,
      "datetime": 1735921740000
    },
    {
      "open": 22.77,
      "high": 22.77,
      "low": 22.725,
      "close": 22.73,
      "volume": 10686,
      "datetime": 1735921800000
    },
    {
      "open": 22.74,
      "high": 22.74,
      "low": 22.7,
      "close": 22.73,
      "volume": 6125,
      "datetime": 1735921860000
    },
    {
      "open": 22.715,
      "high": 22.74,
      "low": 22.715,
      "close": 22.73,
      "volume": 625,
      "datetime": 1735921920000
    },
    {
      "open": 22.715,
      "high": 22.7199,
      "low": 22.7001,
      "close": 22.7199,
      "volume": 3800,
      "datetime": 1735921980000
    },
    {
      "open": 22.715,
      "high": 22.74,
      "low": 22.715,
      "close": 22.7183,
      "volume": 9236,
      "datetime": 1735922040000
    },
    {
      "open": 22.728,
      "high": 22.74,
      "low": 22.7206,
      "close": 22.74,
      "volume": 1050,
      "datetime": 1735922100000
    },
    {
      "open": 22.732,
      "high": 22.74,
      "low": 22.72,
      "close": 22.735,
      "volume": 2322,
      "datetime": 1735922160000
    },
    {
      "open": 22.735,
      "high": 22.76,
      "low": 22.735,
      "close": 22.7444,
      "volume": 6818,
      "datetime": 1735922220000
    },
    {
      "open": 22.755,
      "high": 22.7668,
      "low": 22.75,
      "close": 22.75,
      "volume": 3635,
      "datetime": 1735922280000
    },
    {
      "open": 22.748,
      "high": 22.75,
      "low": 22.748,
      "close": 22.75,
      "volume": 225,
      "datetime": 1735922340000
    },
    {
      "open": 22.74,
      "high": 22.74,
      "low": 22.73,
      "close": 22.74,
      "volume": 1141,
      "datetime": 1735922400000
    },
    {
      "open": 22.77,
      "high": 22.7704,
      "low": 22.77,
      "close": 22.7704,
      "volume": 200,
      "datetime": 1735922460000
    },
    {
      "open": 22.77,
      "high": 22.77,
      "low": 22.7599,
      "close": 22.77,
      "volume": 920,
      "datetime": 1735922520000
    },
    {
      "open": 22.7829,
      "high": 22.7829,
      "low": 22.7701,
      "close": 22.7701,
      "volume": 962,
      "datetime": 1735922580000
    },
    {
      "open": 22.77,
      "high": 22.77,
      "low": 22.76,
      "close": 22.76,
      "volume": 1885,
      "datetime": 1735922640000
    },
    {
      "open": 22.76,
      "high": 22.782,
      "low": 22.76,
      "close": 22.7799,
      "volume": 5870,
      "datetime": 1735922700000
    },
    {
      "open": 22.7799,
      "high": 22.7799,
      "low": 22.7799,
      "close": 22.7799,
      "volume": 100,
      "datetime": 1735922760000
    },
    {
      "open": 22.8201,
      "high": 22.8201,
      "low": 22.8101,
      "close": 22.8101,
      "volume": 2892,
      "datetime": 1735922820000
    },
    {
      "open": 22.814,
      "high": 22.814,
      "low": 22.7999,
      "close": 22.8001,
      "volume": 681,
      "datetime": 1735922880000
    },
    {
      "open": 22.79,
      "high": 22.79,
      "low": 22.78,
      "close": 22.78,
      "volume": 400,
      "datetime": 1735922940000
    },
    {
      "open": 22.7799,
      "high": 22.7799,
      "low": 22.7773,
      "close": 22.7773,
      "volume": 356,
      "datetime": 1735923000000
    },
    {
      "open": 22.78,
      "high": 22.795,
      "low": 22.7701,
      "close": 22.795,
      "volume": 2519,
      "datetime": 1735923060000
    },
    {
      "open": 22.7946,
      "high": 22.84,
      "low": 22.7946,
      "close": 22.84,
      "volume": 2320,
      "datetime": 1735923120000
    },
    {
      "open": 22.8201,
      "high": 22.8291,
      "low": 22.82,
      "close": 22.8291,
      "volume": 925,
      "datetime": 1735923180000
    },
    {
      "open": 22.83,
      "high": 22.85,
      "low": 22.83,
      "close": 22.85,
      "volume": 2125,
      "datetime": 1735923240000
    },
    {
      "open": 22.8499,
      "high": 22.8503,
      "low": 22.8401,
      "close": 22.8499,
      "volume": 1141,
      "datetime": 1735923300000
    },
    {
      "open": 22.85,
      "high": 22.8608,
      "low": 22.85,
      "close": 22.8599,
      "volume": 425,
      "datetime": 1735923360000
    },
    {
      "open": 22.852,
      "high": 22.855,
      "low": 22.8403,
      "close": 22.842,
      "volume": 3000,
      "datetime": 1735923420000
    },
    {
      "open": 22.8399,
      "high": 22.84,
      "low": 22.835,
      "close": 22.84,
      "volume": 1400,
      "datetime": 1735923540000
    },
    {
      "open": 22.83,
      "high": 22.83,
      "low": 22.81,
      "close": 22.8216,
      "volume": 7340,
      "datetime": 1735923600000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.82,
      "close": 22.82,
      "volume": 100,
      "datetime": 1735923660000
    },
    {
      "open": 22.815,
      "high": 22.82,
      "low": 22.815,
      "close": 22.82,
      "volume": 600,
      "datetime": 1735923720000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.8003,
      "close": 22.8003,
      "volume": 2768,
      "datetime": 1735923780000
    },
    {
      "open": 22.8099,
      "high": 22.81,
      "low": 22.8049,
      "close": 22.8049,
      "volume": 2029,
      "datetime": 1735923840000
    },
    {
      "open": 22.8,
      "high": 22.8,
      "low": 22.795,
      "close": 22.795,
      "volume": 200,
      "datetime": 1735923900000
    },
    {
      "open": 22.7999,
      "high": 22.8001,
      "low": 22.7899,
      "close": 22.7899,
      "volume": 900,
      "datetime": 1735923960000
    },
    {
      "open": 22.7965,
      "high": 22.8,
      "low": 22.785,
      "close": 22.7897,
      "volume": 622,
      "datetime": 1735924020000
    },
    {
      "open": 22.785,
      "high": 22.785,
      "low": 22.785,
      "close": 22.785,
      "volume": 100,
      "datetime": 1735924080000
    },
    {
      "open": 22.7902,
      "high": 22.81,
      "low": 22.7902,
      "close": 22.81,
      "volume": 1525,
      "datetime": 1735924140000
    },
    {
      "open": 22.82,
      "high": 22.8201,
      "low": 22.81,
      "close": 22.81,
      "volume": 450,
      "datetime": 1735924200000
    },
    {
      "open": 22.81,
      "high": 22.815,
      "low": 22.8068,
      "close": 22.81,
      "volume": 2385,
      "datetime": 1735924260000
    },
    {
      "open": 22.805,
      "high": 22.805,
      "low": 22.805,
      "close": 22.805,
      "volume": 100,
      "datetime": 1735924320000
    },
    {
      "open": 22.812,
      "high": 22.812,
      "low": 22.7996,
      "close": 22.8,
      "volume": 525,
      "datetime": 1735924380000
    },
    {
      "open": 22.81,
      "high": 22.81,
      "low": 22.81,
      "close": 22.81,
      "volume": 100,
      "datetime": 1735924440000
    },
    {
      "open": 22.8301,
      "high": 22.8301,
      "low": 22.8,
      "close": 22.8,
      "volume": 500,
      "datetime": 1735924500000
    },
    {
      "open": 22.79,
      "high": 22.8,
      "low": 22.79,
      "close": 22.8,
      "volume": 740,
      "datetime": 1735924560000
    },
    {
      "open": 22.8,
      "high": 22.812,
      "low": 22.8,
      "close": 22.812,
      "volume": 500,
      "datetime": 1735924620000
    },
    {
      "open": 22.8071,
      "high": 22.8071,
      "low": 22.8071,
      "close": 22.8071,
      "volume": 100,
      "datetime": 1735924680000
    },
    {
      "open": 22.805,
      "high": 22.805,
      "low": 22.8,
      "close": 22.8014,
      "volume": 510,
      "datetime": 1735924740000
    },
    {
      "open": 22.81,
      "high": 22.81,
      "low": 22.7901,
      "close": 22.7901,
      "volume": 800,
      "datetime": 1735924800000
    },
    {
      "open": 22.8,
      "high": 22.822,
      "low": 22.8,
      "close": 22.8097,
      "volume": 2489,
      "datetime": 1735924860000
    },
    {
      "open": 22.791,
      "high": 22.791,
      "low": 22.7803,
      "close": 22.7835,
      "volume": 1359,
      "datetime": 1735924920000
    },
    {
      "open": 22.7801,
      "high": 22.7801,
      "low": 22.75,
      "close": 22.7601,
      "volume": 730,
      "datetime": 1735924980000
    },
    {
      "open": 22.75,
      "high": 22.75,
      "low": 22.745,
      "close": 22.745,
      "volume": 200,
      "datetime": 1735925100000
    },
    {
      "open": 22.76,
      "high": 22.76,
      "low": 22.7499,
      "close": 22.7503,
      "volume": 500,
      "datetime": 1735925160000
    },
    {
      "open": 22.7671,
      "high": 22.776,
      "low": 22.765,
      "close": 22.7701,
      "volume": 700,
      "datetime": 1735925220000
    },
    {
      "open": 22.77,
      "high": 22.78,
      "low": 22.77,
      "close": 22.78,
      "volume": 1200,
      "datetime": 1735925280000
    },
    {
      "open": 22.77,
      "high": 22.77,
      "low": 22.768,
      "close": 22.77,
      "volume": 728,
      "datetime": 1735925340000
    },
    {
      "open": 22.7711,
      "high": 22.7711,
      "low": 22.76,
      "close": 22.7704,
      "volume": 1588,
      "datetime": 1735925400000
    },
    {
      "open": 22.78,
      "high": 22.78,
      "low": 22.76,
      "close": 22.76,
      "volume": 750,
      "datetime": 1735925460000
    },
    {
      "open": 22.7601,
      "high": 22.77,
      "low": 22.76,
      "close": 22.77,
      "volume": 633,
      "datetime": 1735925520000
    },
    {
      "open": 22.7751,
      "high": 22.7751,
      "low": 22.77,
      "close": 22.77,
      "volume": 450,
      "datetime": 1735925580000
    },
    {
      "open": 22.76,
      "high": 22.7695,
      "low": 22.76,
      "close": 22.7695,
      "volume": 6125,
      "datetime": 1735925640000
    },
    {
      "open": 22.75,
      "high": 22.765,
      "low": 22.7303,
      "close": 22.765,
      "volume": 2200,
      "datetime": 1735925700000
    },
    {
      "open": 22.755,
      "high": 22.76,
      "low": 22.755,
      "close": 22.76,
      "volume": 225,
      "datetime": 1735925760000
    },
    {
      "open": 22.75,
      "high": 22.75,
      "low": 22.75,
      "close": 22.75,
      "volume": 180,
      "datetime": 1735925820000
    },
    {
      "open": 22.7473,
      "high": 22.75,
      "low": 22.74,
      "close": 22.7499,
      "volume": 500,
      "datetime": 1735925880000
    },
    {
      "open": 22.752,
      "high": 22.752,
      "low": 22.7472,
      "close": 22.7472,
      "volume": 200,
      "datetime": 1735925940000
    },
    {
      "open": 22.7502,
      "high": 22.76,
      "low": 22.7502,
      "close": 22.755,
      "volume": 2660,
      "datetime": 1735926000000
    },
    {
      "open": 22.7672,
      "high": 22.77,
      "low": 22.7601,
      "close": 22.7601,
      "volume": 2000,
      "datetime": 1735926060000
    },
    {
      "open": 22.7599,
      "high": 22.7601,
      "low": 22.7599,
      "close": 22.7601,
      "volume": 200,
      "datetime": 1735926120000
    },
    {
      "open": 22.755,
      "high": 22.76,
      "low": 22.7499,
      "close": 22.76,
      "volume": 750,
      "datetime": 1735926180000
    },
    {
      "open": 22.755,
      "high": 22.76,
      "low": 22.7501,
      "close": 22.76,
      "volume": 600,
      "datetime": 1735926240000
    },
    {
      "open": 22.775,
      "high": 22.775,
      "low": 22.763,
      "close": 22.7679,
      "volume": 3633,
      "datetime": 1735926300000
    },
    {
      "open": 22.7854,
      "high": 22.79,
      "low": 22.77,
      "close": 22.7801,
      "volume": 1942,
      "datetime": 1735926360000
    },
    {
      "open": 22.78,
      "high": 22.8,
      "low": 22.78,
      "close": 22.79,
      "volume": 685,
      "datetime": 1735926420000
    },
    {
      "open": 22.7701,
      "high": 22.7794,
      "low": 22.7695,
      "close": 22.7695,
      "volume": 1603,
      "datetime": 1735926480000
    },
    {
      "open": 22.7601,
      "high": 22.77,
      "low": 22.7601,
      "close": 22.7698,
      "volume": 800,
      "datetime": 1735926600000
    },
    {
      "open": 22.78,
      "high": 22.79,
      "low": 22.78,
      "close": 22.79,
      "volume": 382,
      "datetime": 1735926720000
    },
    {
      "open": 22.8,
      "high": 22.83,
      "low": 22.8,
      "close": 22.8254,
      "volume": 1250,
      "datetime": 1735926780000
    },
    {
      "open": 22.825,
      "high": 22.825,
      "low": 22.8097,
      "close": 22.8197,
      "volume": 3725,
      "datetime": 1735926840000
    },
    {
      "open": 22.82,
      "high": 22.8205,
      "low": 22.8102,
      "close": 22.8102,
      "volume": 500,
      "datetime": 1735926900000
    },
    {
      "open": 22.8101,
      "high": 22.8101,
      "low": 22.8101,
      "close": 22.8101,
      "volume": 7362,
      "datetime": 1735926960000
    },
    {
      "open": 22.8,
      "high": 22.8086,
      "low": 22.8,
      "close": 22.8086,
      "volume": 525,
      "datetime": 1735927020000
    },
    {
      "open": 22.8001,
      "high": 22.8001,
      "low": 22.8,
      "close": 22.8,
      "volume": 346,
      "datetime": 1735927080000
    },
    {
      "open": 22.79,
      "high": 22.806,
      "low": 22.79,
      "close": 22.806,
      "volume": 800,
      "datetime": 1735927140000
    },
    {
      "open": 22.8,
      "high": 22.81,
      "low": 22.8,
      "close": 22.81,
      "volume": 200,
      "datetime": 1735927200000
    },
    {
      "open": 22.8101,
      "high": 22.8101,
      "low": 22.8,
      "close": 22.805,
      "volume": 1800,
      "datetime": 1735927260000
    },
    {
      "open": 22.7911,
      "high": 22.7911,
      "low": 22.775,
      "close": 22.775,
      "volume": 705,
      "datetime": 1735927320000
    },
    {
      "open": 22.7699,
      "high": 22.7699,
      "low": 22.7654,
      "close": 22.7698,
      "volume": 1100,
      "datetime": 1735927380000
    },
    {
      "open": 22.772,
      "high": 22.772,
      "low": 22.755,
      "close": 22.769,
      "volume": 1085,
      "datetime": 1735927440000
    },
    {
      "open": 22.7601,
      "high": 22.7601,
      "low": 22.7499,
      "close": 22.7499,
      "volume": 500,
      "datetime": 1735927500000
    },
    {
      "open": 22.7598,
      "high": 22.7608,
      "low": 22.7598,
      "close": 22.76,
      "volume": 1500,
      "datetime": 1735927560000
    },
    {
      "open": 22.755,
      "high": 22.755,
      "low": 22.755,
      "close": 22.755,
      "volume": 300,
      "datetime": 1735927620000
    },
    {
      "open": 22.7746,
      "high": 22.78,
      "low": 22.7746,
      "close": 22.78,
      "volume": 301,
      "datetime": 1735927680000
    },
    {
      "open": 22.779,
      "high": 22.78,
      "low": 22.77,
      "close": 22.78,
      "volume": 401,
      "datetime": 1735927740000
    },
    {
      "open": 22.785,
      "high": 22.785,
      "low": 22.7692,
      "close": 22.7701,
      "volume": 800,
      "datetime": 1735927800000
    },
    {
      "open": 22.766,
      "high": 22.766,
      "low": 22.76,
      "close": 22.76,
      "volume": 802,
      "datetime": 1735927860000
    },
    {
      "open": 22.7498,
      "high": 22.75,
      "low": 22.7498,
      "close": 22.75,
      "volume": 200,
      "datetime": 1735927920000
    },
    {
      "open": 22.7501,
      "high": 22.7501,
      "low": 22.7218,
      "close": 22.7218,
      "volume": 5400,
      "datetime": 1735927980000
    },
    {
      "open": 22.725,
      "high": 22.725,
      "low": 22.725,
      "close": 22.725,
      "volume": 300,
      "datetime": 1735928040000
    },
    {
      "open": 22.714,
      "high": 22.7201,
      "low": 22.714,
      "close": 22.7201,
      "volume": 200,
      "datetime": 1735928100000
    },
    {
      "open": 22.725,
      "high": 22.725,
      "low": 22.7199,
      "close": 22.72,
      "volume": 400,
      "datetime": 1735928160000
    },
    {
      "open": 22.74,
      "high": 22.7411,
      "low": 22.74,
      "close": 22.74,
      "volume": 300,
      "datetime": 1735928220000
    },
    {
      "open": 22.7397,
      "high": 22.7397,
      "low": 22.73,
      "close": 22.73,
      "volume": 200,
      "datetime": 1735928280000
    },
    {
      "open": 22.7301,
      "high": 22.7301,
      "low": 22.71,
      "close": 22.71,
      "volume": 3300,
      "datetime": 1735928340000
    },
    {
      "open": 22.7096,
      "high": 22.7096,
      "low": 22.7096,
      "close": 22.7096,
      "volume": 400,
      "datetime": 1735928400000
    },
    {
      "open": 22.71,
      "high": 22.7126,
      "low": 22.705,
      "close": 22.7126,
      "volume": 522,
      "datetime": 1735928460000
    },
    {
      "open": 22.7101,
      "high": 22.7101,
      "low": 22.7101,
      "close": 22.7101,
      "volume": 100,
      "datetime": 1735928520000
    },
    {
      "open": 22.715,
      "high": 22.715,
      "low": 22.715,
      "close": 22.715,
      "volume": 250,
      "datetime": 1735928580000
    },
    {
      "open": 22.71,
      "high": 22.7168,
      "low": 22.71,
      "close": 22.71,
      "volume": 378,
      "datetime": 1735928640000
    },
    {
      "open": 22.7001,
      "high": 22.7001,
      "low": 22.7,
      "close": 22.7,
      "volume": 1542,
      "datetime": 1735928700000
    },
    {
      "open": 22.695,
      "high": 22.7,
      "low": 22.695,
      "close": 22.7,
      "volume": 1540,
      "datetime": 1735928760000
    },
    {
      "open": 22.7,
      "high": 22.7027,
      "low": 22.7,
      "close": 22.7,
      "volume": 440,
      "datetime": 1735928820000
    },
    {
      "open": 22.68,
      "high": 22.6972,
      "low": 22.6795,
      "close": 22.6972,
      "volume": 2318,
      "datetime": 1735928880000
    },
    {
      "open": 22.69,
      "high": 22.69,
      "low": 22.68,
      "close": 22.68,
      "volume": 832,
      "datetime": 1735928940000
    },
    {
      "open": 22.6801,
      "high": 22.7,
      "low": 22.678,
      "close": 22.7,
      "volume": 700,
      "datetime": 1735929000000
    },
    {
      "open": 22.7015,
      "high": 22.71,
      "low": 22.7015,
      "close": 22.71,
      "volume": 600,
      "datetime": 1735929060000
    },
    {
      "open": 22.7198,
      "high": 22.732,
      "low": 22.7198,
      "close": 22.732,
      "volume": 600,
      "datetime": 1735929120000
    },
    {
      "open": 22.715,
      "high": 22.72,
      "low": 22.715,
      "close": 22.72,
      "volume": 500,
      "datetime": 1735929180000
    },
    {
      "open": 22.7072,
      "high": 22.7103,
      "low": 22.7072,
      "close": 22.7103,
      "volume": 400,
      "datetime": 1735929240000
    },
    {
      "open": 22.69,
      "high": 22.7024,
      "low": 22.6897,
      "close": 22.7024,
      "volume": 1460,
      "datetime": 1735929360000
    },
    {
      "open": 22.6929,
      "high": 22.7085,
      "low": 22.69,
      "close": 22.6979,
      "volume": 4503,
      "datetime": 1735929420000
    },
    {
      "open": 22.695,
      "high": 22.695,
      "low": 22.695,
      "close": 22.695,
      "volume": 101,
      "datetime": 1735929480000
    },
    {
      "open": 22.69,
      "high": 22.69,
      "low": 22.6735,
      "close": 22.6735,
      "volume": 607,
      "datetime": 1735929540000
    },
    {
      "open": 22.68,
      "high": 22.69,
      "low": 22.68,
      "close": 22.68,
      "volume": 2307,
      "datetime": 1735929600000
    },
    {
      "open": 22.6846,
      "high": 22.6995,
      "low": 22.6846,
      "close": 22.6902,
      "volume": 500,
      "datetime": 1735929660000
    },
    {
      "open": 22.69,
      "high": 22.69,
      "low": 22.68,
      "close": 22.68,
      "volume": 597,
      "datetime": 1735929720000
    },
    {
      "open": 22.68,
      "high": 22.68,
      "low": 22.6689,
      "close": 22.6689,
      "volume": 400,
      "datetime": 1735929780000
    },
    {
      "open": 22.655,
      "high": 22.69,
      "low": 22.655,
      "close": 22.69,
      "volume": 1500,
      "datetime": 1735929840000
    },
    {
      "open": 22.69,
      "high": 22.6904,
      "low": 22.6797,
      "close": 22.6797,
      "volume": 2850,
      "datetime": 1735929900000
    },
    {
      "open": 22.67,
      "high": 22.67,
      "low": 22.67,
      "close": 22.67,
      "volume": 200,
      "datetime": 1735929960000
    },
    {
      "open": 22.655,
      "high": 22.655,
      "low": 22.635,
      "close": 22.635,
      "volume": 2539,
      "datetime": 1735930080000
    },
    {
      "open": 22.628,
      "high": 22.628,
      "low": 22.6276,
      "close": 22.6276,
      "volume": 300,
      "datetime": 1735930140000
    },
    {
      "open": 22.65,
      "high": 22.6601,
      "low": 22.65,
      "close": 22.66,
      "volume": 558,
      "datetime": 1735930200000
    },
    {
      "open": 22.66,
      "high": 22.6929,
      "low": 22.66,
      "close": 22.69,
      "volume": 1537,
      "datetime": 1735930260000
    },
    {
      "open": 22.7,
      "high": 22.7094,
      "low": 22.7,
      "close": 22.7,
      "volume": 486,
      "datetime": 1735930320000
    },
    {
      "open": 22.69,
      "high": 22.7,
      "low": 22.6899,
      "close": 22.7,
      "volume": 2091,
      "datetime": 1735930380000
    },
    {
      "open": 22.6901,
      "high": 22.6901,
      "low": 22.68,
      "close": 22.68,
      "volume": 578,
      "datetime": 1735930440000
    },
    {
      "open": 22.7,
      "high": 22.7,
      "low": 22.7,
      "close": 22.7,
      "volume": 225,
      "datetime": 1735930500000
    },
    {
      "open": 22.7,
      "high": 22.7,
      "low": 22.7,
      "close": 22.7,
      "volume": 800,
      "datetime": 1735930560000
    },
    {
      "open": 22.7,
      "high": 22.7,
      "low": 22.7,
      "close": 22.7,
      "volume": 488,
      "datetime": 1735930620000
    },
    {
      "open": 22.7,
      "high": 22.7,
      "low": 22.7,
      "close": 22.7,
      "volume": 100,
      "datetime": 1735930680000
    },
    {
      "open": 22.655,
      "high": 22.68,
      "low": 22.655,
      "close": 22.68,
      "volume": 1421,
      "datetime": 1735930740000
    },
    {
      "open": 22.67,
      "high": 22.67,
      "low": 22.63,
      "close": 22.63,
      "volume": 3866,
      "datetime": 1735930800000
    },
    {
      "open": 22.63,
      "high": 22.64,
      "low": 22.63,
      "close": 22.64,
      "volume": 1479,
      "datetime": 1735930860000
    },
    {
      "open": 22.64,
      "high": 22.65,
      "low": 22.64,
      "close": 22.65,
      "volume": 200,
      "datetime": 1735930920000
    },
    {
      "open": 22.66,
      "high": 22.66,
      "low": 22.64,
      "close": 22.64,
      "volume": 2297,
      "datetime": 1735930980000
    },
    {
      "open": 22.63,
      "high": 22.6301,
      "low": 22.61,
      "close": 22.615,
      "volume": 4793,
      "datetime": 1735931040000
    },
    {
      "open": 22.61,
      "high": 22.6197,
      "low": 22.595,
      "close": 22.6197,
      "volume": 6155,
      "datetime": 1735931100000
    },
    {
      "open": 22.611,
      "high": 22.611,
      "low": 22.61,
      "close": 22.61,
      "volume": 765,
      "datetime": 1735931160000
    },
    {
      "open": 22.605,
      "high": 22.63,
      "low": 22.605,
      "close": 22.63,
      "volume": 3365,
      "datetime": 1735931220000
    },
    {
      "open": 22.62,
      "high": 22.62,
      "low": 22.6,
      "close": 22.605,
      "volume": 3500,
      "datetime": 1735931280000
    },
    {
      "open": 22.615,
      "high": 22.615,
      "low": 22.615,
      "close": 22.615,
      "volume": 150,
      "datetime": 1735931340000
    },
    {
      "open": 22.615,
      "high": 22.62,
      "low": 22.61,
      "close": 22.616,
      "volume": 800,
      "datetime": 1735931400000
    },
    {
      "open": 22.611,
      "high": 22.6195,
      "low": 22.61,
      "close": 22.61,
      "volume": 5296,
      "datetime": 1735931460000
    },
    {
      "open": 22.6099,
      "high": 22.63,
      "low": 22.6099,
      "close": 22.625,
      "volume": 1723,
      "datetime": 1735931520000
    },
    {
      "open": 22.62,
      "high": 22.6243,
      "low": 22.59,
      "close": 22.59,
      "volume": 3145,
      "datetime": 1735931580000
    },
    {
      "open": 22.5809,
      "high": 22.5809,
      "low": 22.56,
      "close": 22.565,
      "volume": 1828,
      "datetime": 1735931640000
    },
    {
      "open": 22.5603,
      "high": 22.59,
      "low": 22.5603,
      "close": 22.59,
      "volume": 6233,
      "datetime": 1735931700000
    },
    {
      "open": 22.58,
      "high": 22.5801,
      "low": 22.57,
      "close": 22.57,
      "volume": 5925,
      "datetime": 1735931760000
    },
    {
      "open": 22.5627,
      "high": 22.5627,
      "low": 22.5627,
      "close": 22.5627,
      "volume": 170,
      "datetime": 1735931820000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.54,
      "close": 22.55,
      "volume": 4536,
      "datetime": 1735931880000
    },
    {
      "open": 22.55,
      "high": 22.5582,
      "low": 22.5446,
      "close": 22.5451,
      "volume": 2858,
      "datetime": 1735931940000
    },
    {
      "open": 22.55,
      "high": 22.5767,
      "low": 22.5499,
      "close": 22.57,
      "volume": 2637,
      "datetime": 1735932000000
    },
    {
      "open": 22.56,
      "high": 22.5646,
      "low": 22.55,
      "close": 22.55,
      "volume": 1769,
      "datetime": 1735932060000
    },
    {
      "open": 22.56,
      "high": 22.5705,
      "low": 22.5595,
      "close": 22.56,
      "volume": 2825,
      "datetime": 1735932120000
    },
    {
      "open": 22.57,
      "high": 22.5962,
      "low": 22.57,
      "close": 22.5962,
      "volume": 1318,
      "datetime": 1735932180000
    },
    {
      "open": 22.5927,
      "high": 22.612,
      "low": 22.5927,
      "close": 22.61,
      "volume": 800,
      "datetime": 1735932240000
    },
    {
      "open": 22.5999,
      "high": 22.6105,
      "low": 22.5999,
      "close": 22.605,
      "volume": 1025,
      "datetime": 1735932300000
    },
    {
      "open": 22.6103,
      "high": 22.62,
      "low": 22.6103,
      "close": 22.617449,
      "volume": 1245,
      "datetime": 1735932360000
    },
    {
      "open": 22.6099,
      "high": 22.6099,
      "low": 22.6099,
      "close": 22.6099,
      "volume": 100,
      "datetime": 1735932420000
    },
    {
      "open": 22.6017,
      "high": 22.6017,
      "low": 22.6017,
      "close": 22.6017,
      "volume": 100,
      "datetime": 1735932480000
    },
    {
      "open": 22.63,
      "high": 22.63,
      "low": 22.6101,
      "close": 22.6101,
      "volume": 650,
      "datetime": 1735932540000
    },
    {
      "open": 22.606,
      "high": 22.606,
      "low": 22.606,
      "close": 22.606,
      "volume": 150,
      "datetime": 1735932600000
    },
    {
      "open": 22.59,
      "high": 22.6,
      "low": 22.59,
      "close": 22.6,
      "volume": 600,
      "datetime": 1735932660000
    },
    {
      "open": 22.599,
      "high": 22.6002,
      "low": 22.59,
      "close": 22.6002,
      "volume": 700,
      "datetime": 1735932720000
    },
    {
      "open": 22.6065,
      "high": 22.6065,
      "low": 22.599,
      "close": 22.6,
      "volume": 550,
      "datetime": 1735932780000
    },
    {
      "open": 22.61,
      "high": 22.6199,
      "low": 22.61,
      "close": 22.6126,
      "volume": 1410,
      "datetime": 1735932900000
    },
    {
      "open": 22.62,
      "high": 22.62,
      "low": 22.6127,
      "close": 22.6127,
      "volume": 325,
      "datetime": 1735932960000
    },
    {
      "open": 22.625,
      "high": 22.625,
      "low": 22.62,
      "close": 22.62,
      "volume": 1600,
      "datetime": 1735933020000
    },
    {
      "open": 22.62,
      "high": 22.62,
      "low": 22.61,
      "close": 22.61,
      "volume": 3645,
      "datetime": 1735933080000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.61,
      "close": 22.61,
      "volume": 100,
      "datetime": 1735933200000
    },
    {
      "open": 22.6,
      "high": 22.61,
      "low": 22.6,
      "close": 22.61,
      "volume": 1395,
      "datetime": 1735933260000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.61,
      "close": 22.61,
      "volume": 200,
      "datetime": 1735933320000
    },
    {
      "open": 22.6,
      "high": 22.61,
      "low": 22.6,
      "close": 22.61,
      "volume": 300,
      "datetime": 1735933380000
    },
    {
      "open": 22.605,
      "high": 22.605,
      "low": 22.605,
      "close": 22.605,
      "volume": 333,
      "datetime": 1735933440000
    },
    {
      "open": 22.62,
      "high": 22.64,
      "low": 22.62,
      "close": 22.6399,
      "volume": 4105,
      "datetime": 1735933500000
    },
    {
      "open": 22.63,
      "high": 22.65,
      "low": 22.63,
      "close": 22.65,
      "volume": 600,
      "datetime": 1735933620000
    },
    {
      "open": 22.635,
      "high": 22.64,
      "low": 22.635,
      "close": 22.6362,
      "volume": 2100,
      "datetime": 1735933680000
    },
    {
      "open": 22.625,
      "high": 22.63,
      "low": 22.615,
      "close": 22.615,
      "volume": 750,
      "datetime": 1735933800000
    },
    {
      "open": 22.62,
      "high": 22.64,
      "low": 22.62,
      "close": 22.64,
      "volume": 425,
      "datetime": 1735933860000
    },
    {
      "open": 22.6379,
      "high": 22.6379,
      "low": 22.6379,
      "close": 22.6379,
      "volume": 100,
      "datetime": 1735933920000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.6446,
      "close": 22.65,
      "volume": 500,
      "datetime": 1735933980000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.64,
      "close": 22.64,
      "volume": 1258,
      "datetime": 1735934040000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.6329,
      "close": 22.6329,
      "volume": 333,
      "datetime": 1735934100000
    },
    {
      "open": 22.645,
      "high": 22.645,
      "low": 22.64,
      "close": 22.64,
      "volume": 550,
      "datetime": 1735934160000
    },
    {
      "open": 22.6457,
      "high": 22.6457,
      "low": 22.6401,
      "close": 22.6401,
      "volume": 200,
      "datetime": 1735934220000
    },
    {
      "open": 22.65,
      "high": 22.655,
      "low": 22.64,
      "close": 22.64,
      "volume": 607,
      "datetime": 1735934280000
    },
    {
      "open": 22.635,
      "high": 22.64,
      "low": 22.635,
      "close": 22.64,
      "volume": 525,
      "datetime": 1735934340000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.65,
      "close": 22.65,
      "volume": 100,
      "datetime": 1735934400000
    },
    {
      "open": 22.65,
      "high": 22.6682,
      "low": 22.65,
      "close": 22.6601,
      "volume": 1172,
      "datetime": 1735934460000
    },
    {
      "open": 22.67,
      "high": 22.6791,
      "low": 22.6698,
      "close": 22.675,
      "volume": 933,
      "datetime": 1735934520000
    },
    {
      "open": 22.67,
      "high": 22.69,
      "low": 22.67,
      "close": 22.6858,
      "volume": 1700,
      "datetime": 1735934580000
    },
    {
      "open": 22.68,
      "high": 22.68,
      "low": 22.68,
      "close": 22.68,
      "volume": 125,
      "datetime": 1735934640000
    },
    {
      "open": 22.69,
      "high": 22.69,
      "low": 22.6801,
      "close": 22.6801,
      "volume": 3903,
      "datetime": 1735934700000
    },
    {
      "open": 22.68,
      "high": 22.6827,
      "low": 22.68,
      "close": 22.6827,
      "volume": 1700,
      "datetime": 1735934760000
    },
    {
      "open": 22.6872,
      "high": 22.6872,
      "low": 22.67,
      "close": 22.67,
      "volume": 1692,
      "datetime": 1735934820000
    },
    {
      "open": 22.67,
      "high": 22.67,
      "low": 22.67,
      "close": 22.67,
      "volume": 200,
      "datetime": 1735934880000
    },
    {
      "open": 22.68,
      "high": 22.68,
      "low": 22.68,
      "close": 22.68,
      "volume": 100,
      "datetime": 1735934940000
    },
    {
      "open": 22.69,
      "high": 22.7018,
      "low": 22.69,
      "close": 22.7018,
      "volume": 3850,
      "datetime": 1735935060000
    },
    {
      "open": 22.71,
      "high": 22.71,
      "low": 22.7,
      "close": 22.7,
      "volume": 1124,
      "datetime": 1735935120000
    },
    {
      "open": 22.69,
      "high": 22.6944,
      "low": 22.68,
      "close": 22.68,
      "volume": 3172,
      "datetime": 1735935180000
    },
    {
      "open": 22.69,
      "high": 22.69,
      "low": 22.6699,
      "close": 22.6699,
      "volume": 544,
      "datetime": 1735935240000
    },
    {
      "open": 22.6602,
      "high": 22.6602,
      "low": 22.6536,
      "close": 22.6536,
      "volume": 737,
      "datetime": 1735935300000
    },
    {
      "open": 22.6598,
      "high": 22.6598,
      "low": 22.6546,
      "close": 22.6546,
      "volume": 600,
      "datetime": 1735935360000
    },
    {
      "open": 22.6528,
      "high": 22.6528,
      "low": 22.65,
      "close": 22.65,
      "volume": 400,
      "datetime": 1735935420000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.64,
      "close": 22.64,
      "volume": 2257,
      "datetime": 1735935480000
    },
    {
      "open": 22.64,
      "high": 22.65,
      "low": 22.64,
      "close": 22.6432,
      "volume": 600,
      "datetime": 1735935540000
    },
    {
      "open": 22.65,
      "high": 22.66,
      "low": 22.65,
      "close": 22.66,
      "volume": 774,
      "datetime": 1735935600000
    },
    {
      "open": 22.66,
      "high": 22.66,
      "low": 22.65,
      "close": 22.65,
      "volume": 975,
      "datetime": 1735935660000
    },
    {
      "open": 22.6429,
      "high": 22.6429,
      "low": 22.621,
      "close": 22.625,
      "volume": 1995,
      "datetime": 1735935720000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.61,
      "close": 22.61,
      "volume": 100,
      "datetime": 1735935780000
    },
    {
      "open": 22.6046,
      "high": 22.6072,
      "low": 22.6046,
      "close": 22.6072,
      "volume": 1300,
      "datetime": 1735935840000
    },
    {
      "open": 22.61,
      "high": 22.62,
      "low": 22.61,
      "close": 22.62,
      "volume": 250,
      "datetime": 1735935900000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 225,
      "datetime": 1735935960000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 200,
      "datetime": 1735936020000
    },
    {
      "open": 22.63,
      "high": 22.64,
      "low": 22.63,
      "close": 22.64,
      "volume": 350,
      "datetime": 1735936140000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.64,
      "close": 22.64,
      "volume": 750,
      "datetime": 1735936200000
    },
    {
      "open": 22.65,
      "high": 22.655,
      "low": 22.645,
      "close": 22.65,
      "volume": 800,
      "datetime": 1735936260000
    },
    {
      "open": 22.67,
      "high": 22.67,
      "low": 22.655,
      "close": 22.655,
      "volume": 3200,
      "datetime": 1735936320000
    },
    {
      "open": 22.6604,
      "high": 22.6604,
      "low": 22.6604,
      "close": 22.6604,
      "volume": 400,
      "datetime": 1735936380000
    },
    {
      "open": 22.665,
      "high": 22.665,
      "low": 22.66,
      "close": 22.66,
      "volume": 850,
      "datetime": 1735936440000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 250,
      "datetime": 1735936500000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.65,
      "close": 22.65,
      "volume": 117,
      "datetime": 1735936560000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 100,
      "datetime": 1735936620000
    },
    {
      "open": 22.66,
      "high": 22.675,
      "low": 22.66,
      "close": 22.675,
      "volume": 525,
      "datetime": 1735936680000
    },
    {
      "open": 22.6799,
      "high": 22.68,
      "low": 22.6799,
      "close": 22.68,
      "volume": 623,
      "datetime": 1735936740000
    },
    {
      "open": 22.69,
      "high": 22.696,
      "low": 22.68,
      "close": 22.68,
      "volume": 975,
      "datetime": 1735936860000
    },
    {
      "open": 22.678,
      "high": 22.678,
      "low": 22.678,
      "close": 22.678,
      "volume": 1000,
      "datetime": 1735936920000
    },
    {
      "open": 22.68,
      "high": 22.68,
      "low": 22.68,
      "close": 22.68,
      "volume": 300,
      "datetime": 1735936980000
    },
    {
      "open": 22.68,
      "high": 22.68,
      "low": 22.665,
      "close": 22.6799,
      "volume": 4152,
      "datetime": 1735937040000
    },
    {
      "open": 22.675,
      "high": 22.6792,
      "low": 22.67,
      "close": 22.6792,
      "volume": 500,
      "datetime": 1735937100000
    },
    {
      "open": 22.68,
      "high": 22.6802,
      "low": 22.665,
      "close": 22.67,
      "volume": 2352,
      "datetime": 1735937160000
    },
    {
      "open": 22.67,
      "high": 22.67,
      "low": 22.67,
      "close": 22.67,
      "volume": 200,
      "datetime": 1735937220000
    },
    {
      "open": 22.69,
      "high": 22.6936,
      "low": 22.69,
      "close": 22.6936,
      "volume": 500,
      "datetime": 1735937280000
    },
    {
      "open": 22.6987,
      "high": 22.7,
      "low": 22.6914,
      "close": 22.7,
      "volume": 1200,
      "datetime": 1735937340000
    },
    {
      "open": 22.7002,
      "high": 22.7002,
      "low": 22.69,
      "close": 22.6998,
      "volume": 1091,
      "datetime": 1735937400000
    },
    {
      "open": 22.695,
      "high": 22.7,
      "low": 22.69,
      "close": 22.69,
      "volume": 1868,
      "datetime": 1735937460000
    },
    {
      "open": 22.6802,
      "high": 22.6897,
      "low": 22.67,
      "close": 22.68,
      "volume": 5423,
      "datetime": 1735937520000
    },
    {
      "open": 22.68,
      "high": 22.6851,
      "low": 22.6718,
      "close": 22.6851,
      "volume": 3008,
      "datetime": 1735937580000
    },
    {
      "open": 22.68,
      "high": 22.68,
      "low": 22.67,
      "close": 22.68,
      "volume": 3421,
      "datetime": 1735937640000
    },
    {
      "open": 22.68,
      "high": 22.689,
      "low": 22.68,
      "close": 22.689,
      "volume": 2200,
      "datetime": 1735937700000
    },
    {
      "open": 22.69,
      "high": 22.6964,
      "low": 22.69,
      "close": 22.69,
      "volume": 2003,
      "datetime": 1735937760000
    },
    {
      "open": 22.685,
      "high": 22.7004,
      "low": 22.685,
      "close": 22.7004,
      "volume": 1500,
      "datetime": 1735937820000
    },
    {
      "open": 22.7,
      "high": 22.705,
      "low": 22.7,
      "close": 22.705,
      "volume": 800,
      "datetime": 1735937880000
    },
    {
      "open": 22.7,
      "high": 22.72,
      "low": 22.69,
      "close": 22.72,
      "volume": 6904,
      "datetime": 1735937940000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 941,
      "datetime": 1735938000000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 100,
      "datetime": 1735938060000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 210,
      "datetime": 1735938180000
    },
    {
      "open": 22.71,
      "high": 22.71,
      "low": 22.71,
      "close": 22.71,
      "volume": 333,
      "datetime": 1735938240000
    },
    {
      "open": 22.7099,
      "high": 22.7099,
      "low": 22.7,
      "close": 22.7,
      "volume": 2749,
      "datetime": 1735940040000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 4000,
      "datetime": 1735940700000
    },
    {
      "open": 22.7,
      "high": 22.7,
      "low": 22.7,
      "close": 22.7,
      "volume": 100,
      "datetime": 1735942680000
    },
    {
      "open": 22.85,
      "high": 22.85,
      "low": 22.85,
      "close": 22.85,
      "volume": 100,
      "datetime": 1735947720000
    },
    {
      "open": 22.849,
      "high": 22.849,
      "low": 22.72,
      "close": 22.72,
      "volume": 2964,
      "datetime": 1735949340000
    },
    {
      "open": 22.8,
      "high": 22.8,
      "low": 22.8,
      "close": 22.8,
      "volume": 2000,
      "datetime": 1735950300000
    },
    {
      "open": 22.83,
      "high": 22.83,
      "low": 22.83,
      "close": 22.83,
      "volume": 500,
      "datetime": 1735950360000
    },
    {
      "open": 22.83,
      "high": 22.86,
      "low": 22.83,
      "close": 22.86,
      "volume": 17749,
      "datetime": 1735950480000
    },
    {
      "open": 22.88,
      "high": 22.88,
      "low": 22.88,
      "close": 22.88,
      "volume": 100,
      "datetime": 1735950540000
    },
    {
      "open": 22.73,
      "high": 22.73,
      "low": 22.73,
      "close": 22.73,
      "volume": 499,
      "datetime": 1735951440000
    },
    {
      "open": 22.7399,
      "high": 22.7399,
      "low": 22.7399,
      "close": 22.7399,
      "volume": 1000,
      "datetime": 1735951920000
    },
    {
      "open": 22.74,
      "high": 22.74,
      "low": 22.73,
      "close": 22.73,
      "volume": 2018,
      "datetime": 1735951980000
    },
    {
      "open": 22.73,
      "high": 22.73,
      "low": 22.73,
      "close": 22.73,
      "volume": 800,
      "datetime": 1735952040000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 650,
      "datetime": 1735952100000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 250,
      "datetime": 1735952160000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 500,
      "datetime": 1735952220000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 101,
      "datetime": 1735952280000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 2000,
      "datetime": 1735952340000
    },
    {
      "open": 22.77,
      "high": 22.77,
      "low": 22.77,
      "close": 22.77,
      "volume": 1500,
      "datetime": 1736125200000
    },
    {
      "open": 22.79,
      "high": 22.79,
      "low": 22.79,
      "close": 22.79,
      "volume": 1,
      "datetime": 1736125860000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.82,
      "close": 22.82,
      "volume": 1000,
      "datetime": 1736125980000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.82,
      "close": 22.82,
      "volume": 13,
      "datetime": 1736126220000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.82,
      "close": 22.82,
      "volume": 5,
      "datetime": 1736126700000
    },
    {
      "open": 22.74,
      "high": 22.74,
      "low": 22.74,
      "close": 22.74,
      "volume": 88,
      "datetime": 1736127900000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.72,
      "close": 22.72,
      "volume": 25,
      "datetime": 1736128320000
    },
    {
      "open": 22.7,
      "high": 22.7,
      "low": 22.7,
      "close": 22.7,
      "volume": 200,
      "datetime": 1736128380000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.65,
      "close": 22.65,
      "volume": 50,
      "datetime": 1736128620000
    },
    {
      "open": 22.62,
      "high": 22.62,
      "low": 22.62,
      "close": 22.62,
      "volume": 5,
      "datetime": 1736128980000
    },
    {
      "open": 22.6,
      "high": 22.6,
      "low": 22.56,
      "close": 22.56,
      "volume": 115,
      "datetime": 1736129100000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.55,
      "close": 22.55,
      "volume": 100,
      "datetime": 1736129340000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.54,
      "close": 22.54,
      "volume": 100,
      "datetime": 1736129460000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.54,
      "close": 22.54,
      "volume": 10,
      "datetime": 1736129520000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.57,
      "close": 22.57,
      "volume": 400,
      "datetime": 1736129640000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.61,
      "close": 22.61,
      "volume": 50,
      "datetime": 1736129940000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.61,
      "close": 22.61,
      "volume": 100,
      "datetime": 1736130060000
    },
    {
      "open": 22.66,
      "high": 22.66,
      "low": 22.64,
      "close": 22.64,
      "volume": 150,
      "datetime": 1736130240000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.65,
      "close": 22.65,
      "volume": 150,
      "datetime": 1736130360000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.65,
      "close": 22.65,
      "volume": 100,
      "datetime": 1736130420000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.65,
      "close": 22.65,
      "volume": 100,
      "datetime": 1736130720000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 1,
      "datetime": 1736130780000
    },
    {
      "open": 22.62,
      "high": 22.62,
      "low": 22.6,
      "close": 22.62,
      "volume": 212,
      "datetime": 1736130840000
    },
    {
      "open": 22.59,
      "high": 22.59,
      "low": 22.57,
      "close": 22.57,
      "volume": 250,
      "datetime": 1736130900000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.57,
      "close": 22.57,
      "volume": 30,
      "datetime": 1736131140000
    },
    {
      "open": 22.6,
      "high": 22.6,
      "low": 22.6,
      "close": 22.6,
      "volume": 225,
      "datetime": 1736131500000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.65,
      "close": 22.65,
      "volume": 5,
      "datetime": 1736132280000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.61,
      "close": 22.61,
      "volume": 970,
      "datetime": 1736133780000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 200,
      "datetime": 1736134020000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 5,
      "datetime": 1736134200000
    },
    {
      "open": 22.56,
      "high": 22.57,
      "low": 22.56,
      "close": 22.57,
      "volume": 35,
      "datetime": 1736134380000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 20,
      "datetime": 1736134440000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.57,
      "close": 22.57,
      "volume": 25,
      "datetime": 1736134560000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.55,
      "close": 22.55,
      "volume": 1049,
      "datetime": 1736134980000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.55,
      "close": 22.55,
      "volume": 2951,
      "datetime": 1736135040000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 52,
      "datetime": 1736135220000
    },
    {
      "open": 22.59,
      "high": 22.59,
      "low": 22.59,
      "close": 22.59,
      "volume": 30,
      "datetime": 1736135280000
    },
    {
      "open": 22.59,
      "high": 22.59,
      "low": 22.59,
      "close": 22.59,
      "volume": 50,
      "datetime": 1736135340000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 50,
      "datetime": 1736135400000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 500,
      "datetime": 1736135460000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 125,
      "datetime": 1736135760000
    },
    {
      "open": 22.52,
      "high": 22.53,
      "low": 22.52,
      "close": 22.53,
      "volume": 270,
      "datetime": 1736136780000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.54,
      "close": 22.54,
      "volume": 100,
      "datetime": 1736137020000
    },
    {
      "open": 22.5,
      "high": 22.51,
      "low": 22.5,
      "close": 22.51,
      "volume": 71,
      "datetime": 1736137140000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 2,
      "datetime": 1736137200000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 12,
      "datetime": 1736137320000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 10,
      "datetime": 1736137620000
    },
    {
      "open": 22.53,
      "high": 22.53,
      "low": 22.53,
      "close": 22.53,
      "volume": 291,
      "datetime": 1736138220000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 50,
      "datetime": 1736138940000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 1,
      "datetime": 1736139000000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 200,
      "datetime": 1736139060000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.46,
      "close": 22.46,
      "volume": 5,
      "datetime": 1736139240000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 18,
      "datetime": 1736139300000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 10,
      "datetime": 1736139360000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 5,
      "datetime": 1736139540000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 500,
      "datetime": 1736139600000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 1000,
      "datetime": 1736140560000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 3,
      "datetime": 1736140860000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 36,
      "datetime": 1736140920000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 100,
      "datetime": 1736140980000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 7,
      "datetime": 1736141400000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.39,
      "close": 22.39,
      "volume": 1000,
      "datetime": 1736141580000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.36,
      "close": 22.36,
      "volume": 10,
      "datetime": 1736141640000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.39,
      "close": 22.39,
      "volume": 400,
      "datetime": 1736141880000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 100,
      "datetime": 1736142000000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.35,
      "close": 22.35,
      "volume": 788,
      "datetime": 1736142420000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 145,
      "datetime": 1736142780000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.44,
      "close": 22.44,
      "volume": 25,
      "datetime": 1736143080000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 25,
      "datetime": 1736143140000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 80,
      "datetime": 1736143200000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 660,
      "datetime": 1736144160000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 1,
      "datetime": 1736144760000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 1000,
      "datetime": 1736145420000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 5,
      "datetime": 1736145540000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 1,
      "datetime": 1736145960000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.44,
      "close": 22.44,
      "volume": 1000,
      "datetime": 1736146140000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 1111,
      "datetime": 1736147280000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 50,
      "datetime": 1736147520000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 3111,
      "datetime": 1736147640000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 865,
      "datetime": 1736147700000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 2,
      "datetime": 1736149500000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.44,
      "close": 22.44,
      "volume": 40,
      "datetime": 1736150700000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.43,
      "close": 22.43,
      "volume": 2207,
      "datetime": 1736150820000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 4000,
      "datetime": 1736151900000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 25,
      "datetime": 1736152560000
    },
    {
      "open": 22.53,
      "high": 22.53,
      "low": 22.53,
      "close": 22.53,
      "volume": 5,
      "datetime": 1736152860000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 699,
      "datetime": 1736154840000
    },
    {
      "open": 22.56,
      "high": 22.56,
      "low": 22.56,
      "close": 22.56,
      "volume": 150,
      "datetime": 1736155140000
    },
    {
      "open": 22.58,
      "high": 22.59,
      "low": 22.57,
      "close": 22.57,
      "volume": 1245,
      "datetime": 1736156400000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.55,
      "close": 22.55,
      "volume": 169,
      "datetime": 1736157000000
    },
    {
      "open": 22.6,
      "high": 22.6,
      "low": 22.6,
      "close": 22.6,
      "volume": 100,
      "datetime": 1736157180000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.57,
      "close": 22.57,
      "volume": 200,
      "datetime": 1736157240000
    },
    {
      "open": 22.6,
      "high": 22.6,
      "low": 22.6,
      "close": 22.6,
      "volume": 260,
      "datetime": 1736158980000
    },
    {
      "open": 22.59,
      "high": 22.59,
      "low": 22.59,
      "close": 22.59,
      "volume": 1061,
      "datetime": 1736159040000
    },
    {
      "open": 22.59,
      "high": 22.59,
      "low": 22.59,
      "close": 22.59,
      "volume": 200,
      "datetime": 1736159220000
    },
    {
      "open": 22.63,
      "high": 22.63,
      "low": 22.63,
      "close": 22.63,
      "volume": 846,
      "datetime": 1736160180000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 200,
      "datetime": 1736161080000
    },
    {
      "open": 22.63,
      "high": 22.63,
      "low": 22.63,
      "close": 22.63,
      "volume": 500,
      "datetime": 1736161380000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 768,
      "datetime": 1736161620000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.61,
      "close": 22.61,
      "volume": 400,
      "datetime": 1736162520000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 159,
      "datetime": 1736163360000
    },
    {
      "open": 22.53,
      "high": 22.53,
      "low": 22.52,
      "close": 22.52,
      "volume": 600,
      "datetime": 1736163600000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.58,
      "close": 22.58,
      "volume": 141,
      "datetime": 1736164740000
    },
    {
      "open": 22.57,
      "high": 22.58,
      "low": 22.57,
      "close": 22.58,
      "volume": 332,
      "datetime": 1736164800000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 130,
      "datetime": 1736164920000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 397,
      "datetime": 1736165040000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 1680,
      "datetime": 1736165160000
    },
    {
      "open": 22.49,
      "high": 22.49,
      "low": 22.49,
      "close": 22.49,
      "volume": 150,
      "datetime": 1736165400000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.44,
      "close": 22.44,
      "volume": 3310,
      "datetime": 1736166240000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.41,
      "close": 22.41,
      "volume": 1000,
      "datetime": 1736166300000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 100,
      "datetime": 1736166420000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 875,
      "datetime": 1736166600000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 200,
      "datetime": 1736166900000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.47,
      "close": 22.47,
      "volume": 100,
      "datetime": 1736167260000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 695,
      "datetime": 1736167740000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 1464,
      "datetime": 1736167980000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.54,
      "close": 22.54,
      "volume": 300,
      "datetime": 1736168460000
    },
    {
      "open": 22.55,
      "high": 22.56,
      "low": 22.55,
      "close": 22.56,
      "volume": 2166,
      "datetime": 1736168520000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.57,
      "close": 22.57,
      "volume": 1779,
      "datetime": 1736168640000
    },
    {
      "open": 22.59,
      "high": 22.59,
      "low": 22.59,
      "close": 22.59,
      "volume": 2450,
      "datetime": 1736169300000
    },
    {
      "open": 22.6,
      "high": 22.6,
      "low": 22.6,
      "close": 22.6,
      "volume": 3043,
      "datetime": 1736169360000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.61,
      "close": 22.61,
      "volume": 200,
      "datetime": 1736169420000
    },
    {
      "open": 22.6,
      "high": 22.6,
      "low": 22.59,
      "close": 22.59,
      "volume": 3250,
      "datetime": 1736169480000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 200,
      "datetime": 1736170380000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.55,
      "close": 22.55,
      "volume": 100,
      "datetime": 1736170800000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.54,
      "close": 22.54,
      "volume": 100,
      "datetime": 1736171040000
    },
    {
      "open": 22.546,
      "high": 22.546,
      "low": 22.546,
      "close": 22.546,
      "volume": 100,
      "datetime": 1736171100000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.5499,
      "close": 22.5499,
      "volume": 900,
      "datetime": 1736171160000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.54,
      "close": 22.54,
      "volume": 300,
      "datetime": 1736171220000
    },
    {
      "open": 22.5495,
      "high": 22.55,
      "low": 22.5399,
      "close": 22.5399,
      "volume": 500,
      "datetime": 1736171280000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.5399,
      "close": 22.5399,
      "volume": 200,
      "datetime": 1736171340000
    },
    {
      "open": 22.53,
      "high": 22.53,
      "low": 22.53,
      "close": 22.53,
      "volume": 2000,
      "datetime": 1736171400000
    },
    {
      "open": 22.53,
      "high": 22.53,
      "low": 22.51,
      "close": 22.51,
      "volume": 1394,
      "datetime": 1736171460000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.47,
      "close": 22.47,
      "volume": 750,
      "datetime": 1736171700000
    },
    {
      "open": 22.4794,
      "high": 22.4794,
      "low": 22.4794,
      "close": 22.4794,
      "volume": 100,
      "datetime": 1736171820000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.46,
      "close": 22.46,
      "volume": 250,
      "datetime": 1736171880000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.43,
      "close": 22.43,
      "volume": 550,
      "datetime": 1736172240000
    },
    {
      "open": 22.44,
      "high": 22.45,
      "low": 22.44,
      "close": 22.45,
      "volume": 1174,
      "datetime": 1736172300000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 100,
      "datetime": 1736172360000
    },
    {
      "open": 22.509,
      "high": 22.509,
      "low": 22.509,
      "close": 22.509,
      "volume": 294,
      "datetime": 1736172420000
    },
    {
      "open": 22.53,
      "high": 22.53,
      "low": 22.53,
      "close": 22.53,
      "volume": 407,
      "datetime": 1736172600000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.54,
      "close": 22.54,
      "volume": 100,
      "datetime": 1736172660000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 447,
      "datetime": 1736172720000
    },
    {
      "open": 22.6,
      "high": 22.62,
      "low": 22.6,
      "close": 22.62,
      "volume": 1195,
      "datetime": 1736172960000
    },
    {
      "open": 22.62,
      "high": 22.63,
      "low": 22.61,
      "close": 22.63,
      "volume": 2200,
      "datetime": 1736173020000
    },
    {
      "open": 22.6,
      "high": 22.6,
      "low": 22.6,
      "close": 22.6,
      "volume": 200,
      "datetime": 1736173080000
    },
    {
      "open": 22.64,
      "high": 22.6492,
      "low": 22.64,
      "close": 22.6492,
      "volume": 200,
      "datetime": 1736173140000
    },
    {
      "open": 22.6101,
      "high": 22.6101,
      "low": 22.6101,
      "close": 22.6101,
      "volume": 200,
      "datetime": 1736173260000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 250,
      "datetime": 1736173320000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 10000,
      "datetime": 1736173440000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.64,
      "close": 22.64,
      "volume": 170,
      "datetime": 1736173500000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.57,
      "close": 22.57,
      "volume": 1779,
      "datetime": 1736173680000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.57,
      "close": 22.57,
      "volume": 2498,
      "datetime": 1736173740000
    },
    {
      "open": 22.56,
      "high": 22.61,
      "low": 22.56,
      "close": 22.6,
      "volume": 14232,
      "datetime": 1736173800000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.5915,
      "close": 22.6001,
      "volume": 8212,
      "datetime": 1736173860000
    },
    {
      "open": 22.6212,
      "high": 22.6212,
      "low": 22.55,
      "close": 22.5901,
      "volume": 3810,
      "datetime": 1736173920000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.54,
      "close": 22.54,
      "volume": 3582,
      "datetime": 1736173980000
    },
    {
      "open": 22.54,
      "high": 22.5472,
      "low": 22.5,
      "close": 22.505,
      "volume": 7136,
      "datetime": 1736174040000
    },
    {
      "open": 22.5454,
      "high": 22.575,
      "low": 22.5454,
      "close": 22.5693,
      "volume": 2121,
      "datetime": 1736174100000
    },
    {
      "open": 22.6,
      "high": 22.6099,
      "low": 22.57,
      "close": 22.6,
      "volume": 3867,
      "datetime": 1736174160000
    },
    {
      "open": 22.61,
      "high": 22.612,
      "low": 22.57,
      "close": 22.57,
      "volume": 700,
      "datetime": 1736174220000
    },
    {
      "open": 22.56,
      "high": 22.56,
      "low": 22.5497,
      "close": 22.555,
      "volume": 7353,
      "datetime": 1736174280000
    },
    {
      "open": 22.551,
      "high": 22.565,
      "low": 22.545,
      "close": 22.545,
      "volume": 4456,
      "datetime": 1736174340000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.48,
      "close": 22.49,
      "volume": 3800,
      "datetime": 1736174400000
    },
    {
      "open": 22.4701,
      "high": 22.471,
      "low": 22.455,
      "close": 22.455,
      "volume": 3727,
      "datetime": 1736174460000
    },
    {
      "open": 22.44,
      "high": 22.4783,
      "low": 22.4301,
      "close": 22.4565,
      "volume": 21881,
      "datetime": 1736174520000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.41,
      "close": 22.415,
      "volume": 2415,
      "datetime": 1736174580000
    },
    {
      "open": 22.44,
      "high": 22.47,
      "low": 22.425,
      "close": 22.4515,
      "volume": 10718,
      "datetime": 1736174640000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.37,
      "close": 22.39,
      "volume": 6899,
      "datetime": 1736174700000
    },
    {
      "open": 22.37,
      "high": 22.4,
      "low": 22.37,
      "close": 22.3872,
      "volume": 10534,
      "datetime": 1736174760000
    },
    {
      "open": 22.3792,
      "high": 22.3792,
      "low": 22.36,
      "close": 22.371,
      "volume": 1024,
      "datetime": 1736174820000
    },
    {
      "open": 22.36,
      "high": 22.37,
      "low": 22.292,
      "close": 22.292,
      "volume": 5193,
      "datetime": 1736174880000
    },
    {
      "open": 22.26,
      "high": 22.26,
      "low": 22.18,
      "close": 22.2244,
      "volume": 21751,
      "datetime": 1736174940000
    },
    {
      "open": 22.2179,
      "high": 22.245,
      "low": 22.2,
      "close": 22.225,
      "volume": 9370,
      "datetime": 1736175000000
    },
    {
      "open": 22.24,
      "high": 22.245,
      "low": 22.15,
      "close": 22.1596,
      "volume": 8200,
      "datetime": 1736175060000
    },
    {
      "open": 22.14,
      "high": 22.1666,
      "low": 22.11,
      "close": 22.12,
      "volume": 15067,
      "datetime": 1736175120000
    },
    {
      "open": 22.14,
      "high": 22.14,
      "low": 22.1,
      "close": 22.115,
      "volume": 20881,
      "datetime": 1736175180000
    },
    {
      "open": 22.07,
      "high": 22.0848,
      "low": 22.04,
      "close": 22.0848,
      "volume": 7184,
      "datetime": 1736175240000
    },
    {
      "open": 22.085,
      "high": 22.11,
      "low": 22.0701,
      "close": 22.0856,
      "volume": 7106,
      "datetime": 1736175300000
    },
    {
      "open": 22.1,
      "high": 22.1055,
      "low": 22.07,
      "close": 22.07,
      "volume": 3963,
      "datetime": 1736175360000
    },
    {
      "open": 22.06,
      "high": 22.08,
      "low": 22.04,
      "close": 22.05,
      "volume": 14869,
      "datetime": 1736175420000
    },
    {
      "open": 22.0801,
      "high": 22.1,
      "low": 22.07,
      "close": 22.0988,
      "volume": 6650,
      "datetime": 1736175480000
    },
    {
      "open": 22.1,
      "high": 22.16,
      "low": 22.1,
      "close": 22.1599,
      "volume": 8600,
      "datetime": 1736175540000
    },
    {
      "open": 22.13,
      "high": 22.1644,
      "low": 22.12,
      "close": 22.1644,
      "volume": 12704,
      "datetime": 1736175600000
    },
    {
      "open": 22.18,
      "high": 22.2143,
      "low": 22.18,
      "close": 22.18,
      "volume": 5237,
      "datetime": 1736175660000
    },
    {
      "open": 22.1001,
      "high": 22.13,
      "low": 22.1001,
      "close": 22.119,
      "volume": 1720,
      "datetime": 1736175720000
    },
    {
      "open": 22.1,
      "high": 22.1,
      "low": 22.07,
      "close": 22.0816,
      "volume": 1180,
      "datetime": 1736175780000
    },
    {
      "open": 22.0902,
      "high": 22.1199,
      "low": 22.0902,
      "close": 22.1199,
      "volume": 700,
      "datetime": 1736175840000
    },
    {
      "open": 22.08,
      "high": 22.115,
      "low": 22.075,
      "close": 22.115,
      "volume": 1478,
      "datetime": 1736175900000
    },
    {
      "open": 22.1,
      "high": 22.1,
      "low": 22.085,
      "close": 22.09,
      "volume": 1650,
      "datetime": 1736175960000
    },
    {
      "open": 22.1,
      "high": 22.105,
      "low": 22.09,
      "close": 22.09,
      "volume": 2225,
      "datetime": 1736176020000
    },
    {
      "open": 22.1,
      "high": 22.1,
      "low": 22.065,
      "close": 22.07,
      "volume": 2300,
      "datetime": 1736176080000
    },
    {
      "open": 22.075,
      "high": 22.08,
      "low": 22.07,
      "close": 22.07,
      "volume": 3725,
      "datetime": 1736176140000
    },
    {
      "open": 22.07,
      "high": 22.11,
      "low": 22.05,
      "close": 22.075,
      "volume": 10939,
      "datetime": 1736176200000
    },
    {
      "open": 22.075,
      "high": 22.09,
      "low": 22.0585,
      "close": 22.07,
      "volume": 10006,
      "datetime": 1736176260000
    },
    {
      "open": 22.06,
      "high": 22.06,
      "low": 22.05,
      "close": 22.06,
      "volume": 2238,
      "datetime": 1736176320000
    },
    {
      "open": 22.075,
      "high": 22.075,
      "low": 22.03,
      "close": 22.03,
      "volume": 3772,
      "datetime": 1736176380000
    },
    {
      "open": 22.03,
      "high": 22.04,
      "low": 22.0212,
      "close": 22.035,
      "volume": 3501,
      "datetime": 1736176440000
    },
    {
      "open": 22.02,
      "high": 22.05,
      "low": 22.01,
      "close": 22.03,
      "volume": 3050,
      "datetime": 1736176500000
    },
    {
      "open": 22.05,
      "high": 22.0878,
      "low": 22.05,
      "close": 22.0878,
      "volume": 4080,
      "datetime": 1736176560000
    },
    {
      "open": 22.055,
      "high": 22.055,
      "low": 22.0149,
      "close": 22.0149,
      "volume": 1686,
      "datetime": 1736176620000
    },
    {
      "open": 22.01,
      "high": 22.01,
      "low": 21.97,
      "close": 21.9981,
      "volume": 21478,
      "datetime": 1736176680000
    },
    {
      "open": 21.98,
      "high": 21.98,
      "low": 21.97,
      "close": 21.98,
      "volume": 1225,
      "datetime": 1736176740000
    },
    {
      "open": 21.97,
      "high": 21.99,
      "low": 21.97,
      "close": 21.985,
      "volume": 2554,
      "datetime": 1736176800000
    },
    {
      "open": 21.9899,
      "high": 22.02,
      "low": 21.98,
      "close": 21.98,
      "volume": 5563,
      "datetime": 1736176860000
    },
    {
      "open": 21.98,
      "high": 21.99,
      "low": 21.97,
      "close": 21.97,
      "volume": 3224,
      "datetime": 1736176920000
    },
    {
      "open": 21.97,
      "high": 22.0073,
      "low": 21.97,
      "close": 22.0073,
      "volume": 1950,
      "datetime": 1736176980000
    },
    {
      "open": 22.0199,
      "high": 22.03,
      "low": 22.0099,
      "close": 22.01,
      "volume": 2537,
      "datetime": 1736177040000
    },
    {
      "open": 22.005,
      "high": 22.005,
      "low": 21.9788,
      "close": 21.9788,
      "volume": 577,
      "datetime": 1736177100000
    },
    {
      "open": 21.965,
      "high": 21.965,
      "low": 21.94,
      "close": 21.9629,
      "volume": 3577,
      "datetime": 1736177160000
    },
    {
      "open": 21.95,
      "high": 21.955,
      "low": 21.95,
      "close": 21.95,
      "volume": 4238,
      "datetime": 1736177220000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.95,
      "close": 21.95,
      "volume": 1449,
      "datetime": 1736177280000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.9179,
      "close": 21.925,
      "volume": 3449,
      "datetime": 1736177340000
    },
    {
      "open": 21.92,
      "high": 21.925,
      "low": 21.89,
      "close": 21.9,
      "volume": 3425,
      "datetime": 1736177400000
    },
    {
      "open": 21.89,
      "high": 21.9399,
      "low": 21.885,
      "close": 21.9172,
      "volume": 24650,
      "datetime": 1736177460000
    },
    {
      "open": 21.92,
      "high": 21.9298,
      "low": 21.91,
      "close": 21.91,
      "volume": 2975,
      "datetime": 1736177520000
    },
    {
      "open": 21.905,
      "high": 21.925,
      "low": 21.89,
      "close": 21.895,
      "volume": 2130,
      "datetime": 1736177580000
    },
    {
      "open": 21.89,
      "high": 21.9,
      "low": 21.88,
      "close": 21.9,
      "volume": 4238,
      "datetime": 1736177640000
    },
    {
      "open": 21.8851,
      "high": 21.91,
      "low": 21.8851,
      "close": 21.89,
      "volume": 5247,
      "datetime": 1736177700000
    },
    {
      "open": 21.89,
      "high": 21.9,
      "low": 21.88,
      "close": 21.88,
      "volume": 3200,
      "datetime": 1736177760000
    },
    {
      "open": 21.885,
      "high": 21.885,
      "low": 21.87,
      "close": 21.87,
      "volume": 1010,
      "datetime": 1736177820000
    },
    {
      "open": 21.87,
      "high": 21.8887,
      "low": 21.87,
      "close": 21.8794,
      "volume": 4600,
      "datetime": 1736177880000
    },
    {
      "open": 21.88,
      "high": 21.925,
      "low": 21.8735,
      "close": 21.92,
      "volume": 8500,
      "datetime": 1736177940000
    },
    {
      "open": 21.9134,
      "high": 21.9134,
      "low": 21.88,
      "close": 21.88,
      "volume": 4098,
      "datetime": 1736178000000
    },
    {
      "open": 21.87,
      "high": 21.89,
      "low": 21.87,
      "close": 21.88,
      "volume": 5378,
      "datetime": 1736178060000
    },
    {
      "open": 21.875,
      "high": 21.88,
      "low": 21.855,
      "close": 21.875,
      "volume": 5319,
      "datetime": 1736178120000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.855,
      "close": 21.855,
      "volume": 2050,
      "datetime": 1736178180000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.8401,
      "close": 21.85,
      "volume": 15284,
      "datetime": 1736178240000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.795,
      "close": 21.795,
      "volume": 23554,
      "datetime": 1736178300000
    },
    {
      "open": 21.79,
      "high": 21.83,
      "low": 21.7857,
      "close": 21.825,
      "volume": 18960,
      "datetime": 1736178360000
    },
    {
      "open": 21.83,
      "high": 21.8797,
      "low": 21.825,
      "close": 21.865,
      "volume": 16137,
      "datetime": 1736178420000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.8399,
      "close": 21.845,
      "volume": 9124,
      "datetime": 1736178480000
    },
    {
      "open": 21.855,
      "high": 21.855,
      "low": 21.8498,
      "close": 21.85,
      "volume": 4244,
      "datetime": 1736178540000
    },
    {
      "open": 21.8452,
      "high": 21.8452,
      "low": 21.8,
      "close": 21.825,
      "volume": 10549,
      "datetime": 1736178600000
    },
    {
      "open": 21.825,
      "high": 21.825,
      "low": 21.8,
      "close": 21.81,
      "volume": 9567,
      "datetime": 1736178660000
    },
    {
      "open": 21.81,
      "high": 21.815,
      "low": 21.765,
      "close": 21.765,
      "volume": 3642,
      "datetime": 1736178720000
    },
    {
      "open": 21.76,
      "high": 21.76,
      "low": 21.7301,
      "close": 21.74,
      "volume": 3287,
      "datetime": 1736178780000
    },
    {
      "open": 21.74,
      "high": 21.755,
      "low": 21.74,
      "close": 21.75,
      "volume": 6250,
      "datetime": 1736178840000
    },
    {
      "open": 21.76,
      "high": 21.79,
      "low": 21.76,
      "close": 21.765,
      "volume": 10203,
      "datetime": 1736178900000
    },
    {
      "open": 21.76,
      "high": 21.8,
      "low": 21.7551,
      "close": 21.8,
      "volume": 4528,
      "datetime": 1736178960000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.79,
      "close": 21.8,
      "volume": 4220,
      "datetime": 1736179020000
    },
    {
      "open": 21.8073,
      "high": 21.8073,
      "low": 21.785,
      "close": 21.785,
      "volume": 5460,
      "datetime": 1736179080000
    },
    {
      "open": 21.79,
      "high": 21.815,
      "low": 21.79,
      "close": 21.8,
      "volume": 3624,
      "datetime": 1736179140000
    },
    {
      "open": 21.7999,
      "high": 21.7999,
      "low": 21.78,
      "close": 21.795,
      "volume": 11775,
      "datetime": 1736179200000
    },
    {
      "open": 21.805,
      "high": 21.8301,
      "low": 21.7999,
      "close": 21.7999,
      "volume": 5926,
      "datetime": 1736179260000
    },
    {
      "open": 21.8,
      "high": 21.82,
      "low": 21.8,
      "close": 21.82,
      "volume": 2012,
      "datetime": 1736179320000
    },
    {
      "open": 21.828,
      "high": 21.83,
      "low": 21.8,
      "close": 21.8001,
      "volume": 7254,
      "datetime": 1736179380000
    },
    {
      "open": 21.8101,
      "high": 21.815,
      "low": 21.805,
      "close": 21.81,
      "volume": 790,
      "datetime": 1736179440000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.7826,
      "close": 21.79,
      "volume": 13598,
      "datetime": 1736179500000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.76,
      "close": 21.77,
      "volume": 4386,
      "datetime": 1736179560000
    },
    {
      "open": 21.77,
      "high": 21.78,
      "low": 21.77,
      "close": 21.78,
      "volume": 1873,
      "datetime": 1736179620000
    },
    {
      "open": 21.77,
      "high": 21.79,
      "low": 21.77,
      "close": 21.7701,
      "volume": 4549,
      "datetime": 1736179680000
    },
    {
      "open": 21.775,
      "high": 21.78,
      "low": 21.75,
      "close": 21.75,
      "volume": 3081,
      "datetime": 1736179740000
    },
    {
      "open": 21.75,
      "high": 21.7682,
      "low": 21.735,
      "close": 21.735,
      "volume": 4157,
      "datetime": 1736179800000
    },
    {
      "open": 21.7379,
      "high": 21.7597,
      "low": 21.7367,
      "close": 21.75,
      "volume": 6303,
      "datetime": 1736179860000
    },
    {
      "open": 21.75,
      "high": 21.7899,
      "low": 21.75,
      "close": 21.785,
      "volume": 2200,
      "datetime": 1736179920000
    },
    {
      "open": 21.7865,
      "high": 21.7865,
      "low": 21.78,
      "close": 21.78,
      "volume": 650,
      "datetime": 1736179980000
    },
    {
      "open": 21.7829,
      "high": 21.79,
      "low": 21.78,
      "close": 21.78,
      "volume": 2883,
      "datetime": 1736180040000
    },
    {
      "open": 21.785,
      "high": 21.8,
      "low": 21.78,
      "close": 21.78,
      "volume": 1225,
      "datetime": 1736180100000
    },
    {
      "open": 21.77,
      "high": 21.77,
      "low": 21.765,
      "close": 21.7699,
      "volume": 1075,
      "datetime": 1736180160000
    },
    {
      "open": 21.77,
      "high": 21.78,
      "low": 21.77,
      "close": 21.775,
      "volume": 2425,
      "datetime": 1736180220000
    },
    {
      "open": 21.7751,
      "high": 21.7997,
      "low": 21.7751,
      "close": 21.7997,
      "volume": 3050,
      "datetime": 1736180280000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.75,
      "close": 21.7501,
      "volume": 1750,
      "datetime": 1736180340000
    },
    {
      "open": 21.76,
      "high": 21.76,
      "low": 21.7499,
      "close": 21.7499,
      "volume": 800,
      "datetime": 1736180400000
    },
    {
      "open": 21.76,
      "high": 21.7699,
      "low": 21.76,
      "close": 21.7699,
      "volume": 350,
      "datetime": 1736180460000
    },
    {
      "open": 21.755,
      "high": 21.755,
      "low": 21.75,
      "close": 21.75,
      "volume": 1925,
      "datetime": 1736180520000
    },
    {
      "open": 21.75,
      "high": 21.75,
      "low": 21.745,
      "close": 21.745,
      "volume": 2581,
      "datetime": 1736180580000
    },
    {
      "open": 21.7487,
      "high": 21.75,
      "low": 21.74,
      "close": 21.74,
      "volume": 23200,
      "datetime": 1736180640000
    },
    {
      "open": 21.73,
      "high": 21.7366,
      "low": 21.73,
      "close": 21.73,
      "volume": 5500,
      "datetime": 1736180700000
    },
    {
      "open": 21.73,
      "high": 21.73,
      "low": 21.7194,
      "close": 21.7273,
      "volume": 14725,
      "datetime": 1736180760000
    },
    {
      "open": 21.72,
      "high": 21.72,
      "low": 21.72,
      "close": 21.72,
      "volume": 800,
      "datetime": 1736180820000
    },
    {
      "open": 21.73,
      "high": 21.73,
      "low": 21.73,
      "close": 21.73,
      "volume": 450,
      "datetime": 1736180880000
    },
    {
      "open": 21.7228,
      "high": 21.7228,
      "low": 21.714,
      "close": 21.72,
      "volume": 2715,
      "datetime": 1736180940000
    },
    {
      "open": 21.725,
      "high": 21.7299,
      "low": 21.7226,
      "close": 21.725,
      "volume": 1317,
      "datetime": 1736181000000
    },
    {
      "open": 21.73,
      "high": 21.74,
      "low": 21.724,
      "close": 21.724,
      "volume": 2378,
      "datetime": 1736181060000
    },
    {
      "open": 21.73,
      "high": 21.73,
      "low": 21.72,
      "close": 21.72,
      "volume": 4739,
      "datetime": 1736181120000
    },
    {
      "open": 21.72,
      "high": 21.73,
      "low": 21.72,
      "close": 21.73,
      "volume": 3693,
      "datetime": 1736181180000
    },
    {
      "open": 21.725,
      "high": 21.74,
      "low": 21.725,
      "close": 21.74,
      "volume": 3476,
      "datetime": 1736181240000
    },
    {
      "open": 21.74,
      "high": 21.775,
      "low": 21.74,
      "close": 21.775,
      "volume": 1872,
      "datetime": 1736181300000
    },
    {
      "open": 21.79,
      "high": 21.795,
      "low": 21.77,
      "close": 21.77,
      "volume": 5202,
      "datetime": 1736181360000
    },
    {
      "open": 21.76,
      "high": 21.785,
      "low": 21.76,
      "close": 21.785,
      "volume": 10328,
      "datetime": 1736181420000
    },
    {
      "open": 21.8073,
      "high": 21.8073,
      "low": 21.79,
      "close": 21.795,
      "volume": 1985,
      "datetime": 1736181480000
    },
    {
      "open": 21.8,
      "high": 21.8199,
      "low": 21.79,
      "close": 21.79,
      "volume": 2707,
      "datetime": 1736181540000
    },
    {
      "open": 21.7951,
      "high": 21.805,
      "low": 21.7942,
      "close": 21.8028,
      "volume": 4308,
      "datetime": 1736181600000
    },
    {
      "open": 21.82,
      "high": 21.83,
      "low": 21.8,
      "close": 21.8001,
      "volume": 13206,
      "datetime": 1736181660000
    },
    {
      "open": 21.81,
      "high": 21.82,
      "low": 21.8099,
      "close": 21.81,
      "volume": 3686,
      "datetime": 1736181720000
    },
    {
      "open": 21.82,
      "high": 21.86,
      "low": 21.82,
      "close": 21.85,
      "volume": 13282,
      "datetime": 1736181780000
    },
    {
      "open": 21.84,
      "high": 21.8628,
      "low": 21.8328,
      "close": 21.85,
      "volume": 10082,
      "datetime": 1736181840000
    },
    {
      "open": 21.855,
      "high": 21.86,
      "low": 21.8367,
      "close": 21.8367,
      "volume": 7161,
      "datetime": 1736181900000
    },
    {
      "open": 21.84,
      "high": 21.86,
      "low": 21.84,
      "close": 21.84,
      "volume": 375,
      "datetime": 1736181960000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.86,
      "close": 21.86,
      "volume": 1550,
      "datetime": 1736182020000
    },
    {
      "open": 21.875,
      "high": 21.875,
      "low": 21.8701,
      "close": 21.875,
      "volume": 4689,
      "datetime": 1736182080000
    },
    {
      "open": 21.885,
      "high": 21.889,
      "low": 21.85,
      "close": 21.855,
      "volume": 5764,
      "datetime": 1736182140000
    },
    {
      "open": 21.8502,
      "high": 21.8502,
      "low": 21.82,
      "close": 21.83,
      "volume": 19559,
      "datetime": 1736182200000
    },
    {
      "open": 21.825,
      "high": 21.825,
      "low": 21.775,
      "close": 21.775,
      "volume": 3598,
      "datetime": 1736182260000
    },
    {
      "open": 21.78,
      "high": 21.785,
      "low": 21.78,
      "close": 21.7809,
      "volume": 1574,
      "datetime": 1736182320000
    },
    {
      "open": 21.795,
      "high": 21.8,
      "low": 21.78,
      "close": 21.78,
      "volume": 7096,
      "datetime": 1736182380000
    },
    {
      "open": 21.7803,
      "high": 21.7803,
      "low": 21.75,
      "close": 21.755,
      "volume": 3995,
      "datetime": 1736182440000
    },
    {
      "open": 21.76,
      "high": 21.785,
      "low": 21.76,
      "close": 21.785,
      "volume": 3103,
      "datetime": 1736182500000
    },
    {
      "open": 21.785,
      "high": 21.7951,
      "low": 21.7823,
      "close": 21.7951,
      "volume": 1279,
      "datetime": 1736182560000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.78,
      "close": 21.7802,
      "volume": 8984,
      "datetime": 1736182620000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.781,
      "close": 21.781,
      "volume": 500,
      "datetime": 1736182680000
    },
    {
      "open": 21.785,
      "high": 21.785,
      "low": 21.7813,
      "close": 21.7813,
      "volume": 344,
      "datetime": 1736182740000
    },
    {
      "open": 21.79,
      "high": 21.8111,
      "low": 21.79,
      "close": 21.81,
      "volume": 5023,
      "datetime": 1736182800000
    },
    {
      "open": 21.81,
      "high": 21.82,
      "low": 21.805,
      "close": 21.815,
      "volume": 2032,
      "datetime": 1736182860000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.805,
      "close": 21.805,
      "volume": 2218,
      "datetime": 1736182920000
    },
    {
      "open": 21.8071,
      "high": 21.82,
      "low": 21.8,
      "close": 21.82,
      "volume": 1412,
      "datetime": 1736182980000
    },
    {
      "open": 21.81,
      "high": 21.835,
      "low": 21.8,
      "close": 21.8321,
      "volume": 4628,
      "datetime": 1736183040000
    },
    {
      "open": 21.835,
      "high": 21.842265,
      "low": 21.83,
      "close": 21.835,
      "volume": 7391,
      "datetime": 1736183100000
    },
    {
      "open": 21.83,
      "high": 21.85,
      "low": 21.83,
      "close": 21.8499,
      "volume": 8433,
      "datetime": 1736183160000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.835,
      "close": 21.8428,
      "volume": 2865,
      "datetime": 1736183220000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.82,
      "close": 21.82,
      "volume": 1588,
      "datetime": 1736183280000
    },
    {
      "open": 21.8202,
      "high": 21.8202,
      "low": 21.79,
      "close": 21.81,
      "volume": 6725,
      "datetime": 1736183340000
    },
    {
      "open": 21.82,
      "high": 21.83,
      "low": 21.82,
      "close": 21.82,
      "volume": 394,
      "datetime": 1736183400000
    },
    {
      "open": 21.82,
      "high": 21.82,
      "low": 21.815,
      "close": 21.815,
      "volume": 3271,
      "datetime": 1736183460000
    },
    {
      "open": 21.82,
      "high": 21.82,
      "low": 21.815,
      "close": 21.82,
      "volume": 758,
      "datetime": 1736183520000
    },
    {
      "open": 21.825,
      "high": 21.825,
      "low": 21.82,
      "close": 21.82,
      "volume": 371,
      "datetime": 1736183580000
    },
    {
      "open": 21.82,
      "high": 21.8451,
      "low": 21.82,
      "close": 21.835,
      "volume": 3007,
      "datetime": 1736183640000
    },
    {
      "open": 21.8312,
      "high": 21.84,
      "low": 21.83,
      "close": 21.84,
      "volume": 4425,
      "datetime": 1736183700000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.835,
      "close": 21.84,
      "volume": 1033,
      "datetime": 1736183760000
    },
    {
      "open": 21.8472,
      "high": 21.8472,
      "low": 21.8368,
      "close": 21.84,
      "volume": 2625,
      "datetime": 1736183820000
    },
    {
      "open": 21.839,
      "high": 21.865,
      "low": 21.839,
      "close": 21.86,
      "volume": 3775,
      "datetime": 1736183880000
    },
    {
      "open": 21.8405,
      "high": 21.885,
      "low": 21.8405,
      "close": 21.8705,
      "volume": 4781,
      "datetime": 1736183940000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.8501,
      "close": 21.86,
      "volume": 2225,
      "datetime": 1736184000000
    },
    {
      "open": 21.8501,
      "high": 21.86,
      "low": 21.8203,
      "close": 21.8203,
      "volume": 3630,
      "datetime": 1736184060000
    },
    {
      "open": 21.82,
      "high": 21.82,
      "low": 21.815,
      "close": 21.815,
      "volume": 3400,
      "datetime": 1736184120000
    },
    {
      "open": 21.82,
      "high": 21.82,
      "low": 21.815,
      "close": 21.82,
      "volume": 5106,
      "datetime": 1736184180000
    },
    {
      "open": 21.8101,
      "high": 21.8101,
      "low": 21.8101,
      "close": 21.8101,
      "volume": 238,
      "datetime": 1736184240000
    },
    {
      "open": 21.82,
      "high": 21.83,
      "low": 21.81,
      "close": 21.8293,
      "volume": 4829,
      "datetime": 1736184300000
    },
    {
      "open": 21.8295,
      "high": 21.86,
      "low": 21.825,
      "close": 21.86,
      "volume": 3772,
      "datetime": 1736184360000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.845,
      "close": 21.85,
      "volume": 4825,
      "datetime": 1736184420000
    },
    {
      "open": 21.8502,
      "high": 21.86,
      "low": 21.8502,
      "close": 21.86,
      "volume": 6100,
      "datetime": 1736184480000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.855,
      "close": 21.855,
      "volume": 975,
      "datetime": 1736184540000
    },
    {
      "open": 21.86,
      "high": 21.875,
      "low": 21.86,
      "close": 21.875,
      "volume": 2737,
      "datetime": 1736184600000
    },
    {
      "open": 21.87,
      "high": 21.885,
      "low": 21.87,
      "close": 21.885,
      "volume": 1593,
      "datetime": 1736184660000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.862,
      "close": 21.87,
      "volume": 3965,
      "datetime": 1736184720000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.84,
      "close": 21.84,
      "volume": 300,
      "datetime": 1736184780000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.825,
      "close": 21.825,
      "volume": 1787,
      "datetime": 1736184840000
    },
    {
      "open": 21.83,
      "high": 21.8404,
      "low": 21.83,
      "close": 21.8404,
      "volume": 750,
      "datetime": 1736184900000
    },
    {
      "open": 21.86,
      "high": 21.8875,
      "low": 21.86,
      "close": 21.885,
      "volume": 3059,
      "datetime": 1736184960000
    },
    {
      "open": 21.88,
      "high": 21.89,
      "low": 21.88,
      "close": 21.89,
      "volume": 225,
      "datetime": 1736185020000
    },
    {
      "open": 21.9,
      "high": 21.9072,
      "low": 21.9,
      "close": 21.9,
      "volume": 2400,
      "datetime": 1736185080000
    },
    {
      "open": 21.8988,
      "high": 21.93,
      "low": 21.8988,
      "close": 21.93,
      "volume": 23779,
      "datetime": 1736185140000
    },
    {
      "open": 21.93,
      "high": 21.95,
      "low": 21.93,
      "close": 21.95,
      "volume": 4493,
      "datetime": 1736185200000
    },
    {
      "open": 21.94,
      "high": 21.97,
      "low": 21.94,
      "close": 21.97,
      "volume": 8371,
      "datetime": 1736185260000
    },
    {
      "open": 21.98,
      "high": 22.01,
      "low": 21.98,
      "close": 22,
      "volume": 14575,
      "datetime": 1736185320000
    },
    {
      "open": 22,
      "high": 22.0051,
      "low": 21.99,
      "close": 22,
      "volume": 4757,
      "datetime": 1736185380000
    },
    {
      "open": 21.991,
      "high": 21.991,
      "low": 21.96,
      "close": 21.975,
      "volume": 8429,
      "datetime": 1736185440000
    },
    {
      "open": 21.98,
      "high": 22,
      "low": 21.98,
      "close": 21.9876,
      "volume": 925,
      "datetime": 1736185500000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.93,
      "close": 21.93,
      "volume": 1575,
      "datetime": 1736185560000
    },
    {
      "open": 21.925,
      "high": 21.9359,
      "low": 21.9104,
      "close": 21.912,
      "volume": 4012,
      "datetime": 1736185620000
    },
    {
      "open": 21.9101,
      "high": 21.93,
      "low": 21.9101,
      "close": 21.93,
      "volume": 1008,
      "datetime": 1736185680000
    },
    {
      "open": 21.93,
      "high": 21.9349,
      "low": 21.9201,
      "close": 21.93,
      "volume": 5694,
      "datetime": 1736185740000
    },
    {
      "open": 21.93,
      "high": 21.93,
      "low": 21.93,
      "close": 21.93,
      "volume": 875,
      "datetime": 1736185800000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.93,
      "close": 21.94,
      "volume": 575,
      "datetime": 1736185860000
    },
    {
      "open": 21.9301,
      "high": 21.9301,
      "low": 21.93,
      "close": 21.93,
      "volume": 4004,
      "datetime": 1736185920000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.92,
      "close": 21.92,
      "volume": 3200,
      "datetime": 1736185980000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.9,
      "close": 21.9,
      "volume": 1200,
      "datetime": 1736186040000
    },
    {
      "open": 21.91,
      "high": 21.92,
      "low": 21.9,
      "close": 21.91,
      "volume": 4825,
      "datetime": 1736186100000
    },
    {
      "open": 21.905,
      "high": 21.91,
      "low": 21.905,
      "close": 21.91,
      "volume": 950,
      "datetime": 1736186160000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.89,
      "close": 21.89,
      "volume": 1200,
      "datetime": 1736186220000
    },
    {
      "open": 21.8899,
      "high": 21.8899,
      "low": 21.88,
      "close": 21.88,
      "volume": 4470,
      "datetime": 1736186280000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.874,
      "close": 21.88,
      "volume": 1800,
      "datetime": 1736186340000
    },
    {
      "open": 21.88,
      "high": 21.89,
      "low": 21.8722,
      "close": 21.89,
      "volume": 1325,
      "datetime": 1736186400000
    },
    {
      "open": 21.9,
      "high": 21.92,
      "low": 21.9,
      "close": 21.92,
      "volume": 525,
      "datetime": 1736186460000
    },
    {
      "open": 21.92,
      "high": 21.94,
      "low": 21.9,
      "close": 21.9,
      "volume": 1321,
      "datetime": 1736186520000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.8729,
      "close": 21.88,
      "volume": 775,
      "datetime": 1736186580000
    },
    {
      "open": 21.87,
      "high": 21.875,
      "low": 21.87,
      "close": 21.875,
      "volume": 225,
      "datetime": 1736186640000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 200,
      "datetime": 1736186700000
    },
    {
      "open": 21.88,
      "high": 21.9,
      "low": 21.875,
      "close": 21.9,
      "volume": 752,
      "datetime": 1736186760000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.885,
      "close": 21.8883,
      "volume": 6372,
      "datetime": 1736186820000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.88,
      "close": 21.88,
      "volume": 925,
      "datetime": 1736186880000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.85,
      "close": 21.866,
      "volume": 1595,
      "datetime": 1736186940000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.86,
      "close": 21.86,
      "volume": 700,
      "datetime": 1736187000000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.86,
      "close": 21.87,
      "volume": 2094,
      "datetime": 1736187060000
    },
    {
      "open": 21.87,
      "high": 21.88,
      "low": 21.87,
      "close": 21.88,
      "volume": 625,
      "datetime": 1736187120000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.855,
      "close": 21.855,
      "volume": 3498,
      "datetime": 1736187180000
    },
    {
      "open": 21.855,
      "high": 21.855,
      "low": 21.855,
      "close": 21.855,
      "volume": 900,
      "datetime": 1736187240000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.845,
      "close": 21.85,
      "volume": 2404,
      "datetime": 1736187300000
    },
    {
      "open": 21.8599,
      "high": 21.8599,
      "low": 21.85,
      "close": 21.85,
      "volume": 950,
      "datetime": 1736187360000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.86,
      "close": 21.87,
      "volume": 350,
      "datetime": 1736187420000
    },
    {
      "open": 21.8701,
      "high": 21.8701,
      "low": 21.84,
      "close": 21.8501,
      "volume": 5310,
      "datetime": 1736187480000
    },
    {
      "open": 21.86,
      "high": 21.8665,
      "low": 21.86,
      "close": 21.8665,
      "volume": 350,
      "datetime": 1736187540000
    },
    {
      "open": 21.85,
      "high": 21.86,
      "low": 21.85,
      "close": 21.86,
      "volume": 800,
      "datetime": 1736187660000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.83,
      "close": 21.83,
      "volume": 875,
      "datetime": 1736187720000
    },
    {
      "open": 21.835,
      "high": 21.835,
      "low": 21.824,
      "close": 21.83,
      "volume": 500,
      "datetime": 1736187780000
    },
    {
      "open": 21.84,
      "high": 21.851,
      "low": 21.84,
      "close": 21.851,
      "volume": 10425,
      "datetime": 1736187840000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.8599,
      "close": 21.86,
      "volume": 2510,
      "datetime": 1736187900000
    },
    {
      "open": 21.855,
      "high": 21.86,
      "low": 21.855,
      "close": 21.86,
      "volume": 375,
      "datetime": 1736187960000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.86,
      "close": 21.86,
      "volume": 1400,
      "datetime": 1736188020000
    },
    {
      "open": 21.855,
      "high": 21.86,
      "low": 21.855,
      "close": 21.86,
      "volume": 375,
      "datetime": 1736188080000
    },
    {
      "open": 21.8651,
      "high": 21.8651,
      "low": 21.855,
      "close": 21.855,
      "volume": 1625,
      "datetime": 1736188140000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 800,
      "datetime": 1736188260000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.87,
      "close": 21.87,
      "volume": 450,
      "datetime": 1736188320000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.86,
      "close": 21.86,
      "volume": 350,
      "datetime": 1736188380000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.87,
      "close": 21.87,
      "volume": 1000,
      "datetime": 1736188440000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.8564,
      "close": 21.8564,
      "volume": 225,
      "datetime": 1736188500000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.8463,
      "close": 21.8463,
      "volume": 329,
      "datetime": 1736188560000
    },
    {
      "open": 21.8312,
      "high": 21.84,
      "low": 21.8312,
      "close": 21.84,
      "volume": 3520,
      "datetime": 1736188620000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.83,
      "close": 21.83,
      "volume": 225,
      "datetime": 1736188680000
    },
    {
      "open": 21.83,
      "high": 21.835,
      "low": 21.83,
      "close": 21.83,
      "volume": 1975,
      "datetime": 1736188740000
    },
    {
      "open": 21.83,
      "high": 21.835,
      "low": 21.83,
      "close": 21.835,
      "volume": 1750,
      "datetime": 1736188800000
    },
    {
      "open": 21.8301,
      "high": 21.84,
      "low": 21.83,
      "close": 21.84,
      "volume": 1553,
      "datetime": 1736188860000
    },
    {
      "open": 21.84,
      "high": 21.85,
      "low": 21.84,
      "close": 21.85,
      "volume": 750,
      "datetime": 1736188920000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.8304,
      "close": 21.8304,
      "volume": 502,
      "datetime": 1736188980000
    },
    {
      "open": 21.83,
      "high": 21.85,
      "low": 21.825,
      "close": 21.85,
      "volume": 999,
      "datetime": 1736189040000
    },
    {
      "open": 21.85,
      "high": 21.88,
      "low": 21.85,
      "close": 21.88,
      "volume": 7344,
      "datetime": 1736189100000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.8698,
      "close": 21.8698,
      "volume": 1875,
      "datetime": 1736189160000
    },
    {
      "open": 21.86,
      "high": 21.8698,
      "low": 21.86,
      "close": 21.86,
      "volume": 2925,
      "datetime": 1736189220000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.86,
      "close": 21.87,
      "volume": 250,
      "datetime": 1736189280000
    },
    {
      "open": 21.88,
      "high": 21.9,
      "low": 21.88,
      "close": 21.9,
      "volume": 225,
      "datetime": 1736189340000
    },
    {
      "open": 21.915,
      "high": 21.915,
      "low": 21.91,
      "close": 21.9121,
      "volume": 1000,
      "datetime": 1736189400000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.8827,
      "close": 21.8827,
      "volume": 6477,
      "datetime": 1736189460000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.86,
      "close": 21.86,
      "volume": 6575,
      "datetime": 1736189520000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.8499,
      "close": 21.85,
      "volume": 2124,
      "datetime": 1736189580000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.86,
      "close": 21.87,
      "volume": 725,
      "datetime": 1736189640000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.86,
      "close": 21.865,
      "volume": 1025,
      "datetime": 1736189700000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.86,
      "close": 21.87,
      "volume": 475,
      "datetime": 1736189760000
    },
    {
      "open": 21.877,
      "high": 21.88,
      "low": 21.87,
      "close": 21.88,
      "volume": 1825,
      "datetime": 1736189820000
    },
    {
      "open": 21.88,
      "high": 21.9,
      "low": 21.88,
      "close": 21.9,
      "volume": 4576,
      "datetime": 1736189940000
    },
    {
      "open": 21.9,
      "high": 21.92,
      "low": 21.9,
      "close": 21.92,
      "volume": 675,
      "datetime": 1736190000000
    },
    {
      "open": 21.91,
      "high": 21.9199,
      "low": 21.9099,
      "close": 21.9199,
      "volume": 5071,
      "datetime": 1736190060000
    },
    {
      "open": 21.929,
      "high": 21.93,
      "low": 21.91,
      "close": 21.91,
      "volume": 1350,
      "datetime": 1736190120000
    },
    {
      "open": 21.915,
      "high": 21.9199,
      "low": 21.895,
      "close": 21.895,
      "volume": 900,
      "datetime": 1736190180000
    },
    {
      "open": 21.8903,
      "high": 21.9121,
      "low": 21.8903,
      "close": 21.9121,
      "volume": 5100,
      "datetime": 1736190240000
    },
    {
      "open": 21.915,
      "high": 21.92,
      "low": 21.8806,
      "close": 21.8806,
      "volume": 16023,
      "datetime": 1736190300000
    },
    {
      "open": 21.9,
      "high": 21.92,
      "low": 21.9,
      "close": 21.91,
      "volume": 10499,
      "datetime": 1736190360000
    },
    {
      "open": 21.8958,
      "high": 21.9,
      "low": 21.88,
      "close": 21.88,
      "volume": 1925,
      "datetime": 1736190420000
    },
    {
      "open": 21.87,
      "high": 21.8802,
      "low": 21.87,
      "close": 21.8802,
      "volume": 823,
      "datetime": 1736190480000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.875,
      "close": 21.875,
      "volume": 2030,
      "datetime": 1736190540000
    },
    {
      "open": 21.88,
      "high": 21.8967,
      "low": 21.88,
      "close": 21.8967,
      "volume": 350,
      "datetime": 1736190600000
    },
    {
      "open": 21.89,
      "high": 21.8979,
      "low": 21.89,
      "close": 21.8979,
      "volume": 600,
      "datetime": 1736190660000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.86,
      "close": 21.86,
      "volume": 4275,
      "datetime": 1736190720000
    },
    {
      "open": 21.86,
      "high": 21.8695,
      "low": 21.86,
      "close": 21.8695,
      "volume": 2300,
      "datetime": 1736190780000
    },
    {
      "open": 21.869,
      "high": 21.869,
      "low": 21.8585,
      "close": 21.8585,
      "volume": 400,
      "datetime": 1736190840000
    },
    {
      "open": 21.8698,
      "high": 21.8698,
      "low": 21.8405,
      "close": 21.841,
      "volume": 700,
      "datetime": 1736190900000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.8371,
      "close": 21.84,
      "volume": 1325,
      "datetime": 1736190960000
    },
    {
      "open": 21.836,
      "high": 21.836,
      "low": 21.836,
      "close": 21.836,
      "volume": 100,
      "datetime": 1736191020000
    },
    {
      "open": 21.83,
      "high": 21.84,
      "low": 21.83,
      "close": 21.84,
      "volume": 600,
      "datetime": 1736191080000
    },
    {
      "open": 21.8488,
      "high": 21.85,
      "low": 21.8488,
      "close": 21.85,
      "volume": 2698,
      "datetime": 1736191140000
    },
    {
      "open": 21.84,
      "high": 21.85,
      "low": 21.84,
      "close": 21.85,
      "volume": 2232,
      "datetime": 1736191200000
    },
    {
      "open": 21.85,
      "high": 21.86,
      "low": 21.85,
      "close": 21.86,
      "volume": 1300,
      "datetime": 1736191260000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.855,
      "close": 21.86,
      "volume": 5475,
      "datetime": 1736191320000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.86,
      "close": 21.86,
      "volume": 750,
      "datetime": 1736191380000
    },
    {
      "open": 21.855,
      "high": 21.86,
      "low": 21.855,
      "close": 21.86,
      "volume": 575,
      "datetime": 1736191440000
    },
    {
      "open": 21.8604,
      "high": 21.88,
      "low": 21.8604,
      "close": 21.88,
      "volume": 1048,
      "datetime": 1736191500000
    },
    {
      "open": 21.87,
      "high": 21.8883,
      "low": 21.87,
      "close": 21.8883,
      "volume": 941,
      "datetime": 1736191560000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.865,
      "close": 21.865,
      "volume": 2663,
      "datetime": 1736191620000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.86,
      "close": 21.86,
      "volume": 1166,
      "datetime": 1736191680000
    },
    {
      "open": 21.86,
      "high": 21.8683,
      "low": 21.86,
      "close": 21.8683,
      "volume": 1354,
      "datetime": 1736191740000
    },
    {
      "open": 21.87,
      "high": 21.8798,
      "low": 21.86,
      "close": 21.86,
      "volume": 1343,
      "datetime": 1736191800000
    },
    {
      "open": 21.87,
      "high": 21.8884,
      "low": 21.87,
      "close": 21.88,
      "volume": 5711,
      "datetime": 1736191860000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 375,
      "datetime": 1736191920000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 350,
      "datetime": 1736191980000
    },
    {
      "open": 21.8951,
      "high": 21.8951,
      "low": 21.89,
      "close": 21.89,
      "volume": 2708,
      "datetime": 1736192040000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 12560,
      "datetime": 1736192100000
    },
    {
      "open": 21.89,
      "high": 21.9,
      "low": 21.89,
      "close": 21.89,
      "volume": 10150,
      "datetime": 1736192160000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 3550,
      "datetime": 1736192220000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.86,
      "close": 21.86,
      "volume": 425,
      "datetime": 1736192280000
    },
    {
      "open": 21.86,
      "high": 21.8615,
      "low": 21.86,
      "close": 21.8615,
      "volume": 625,
      "datetime": 1736192340000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.86,
      "close": 21.86,
      "volume": 375,
      "datetime": 1736192400000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.8504,
      "close": 21.8504,
      "volume": 650,
      "datetime": 1736192460000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.8414,
      "close": 21.85,
      "volume": 3775,
      "datetime": 1736192520000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.85,
      "close": 21.85,
      "volume": 1137,
      "datetime": 1736192580000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 125,
      "datetime": 1736192640000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 400,
      "datetime": 1736192700000
    },
    {
      "open": 21.845,
      "high": 21.86,
      "low": 21.845,
      "close": 21.86,
      "volume": 1400,
      "datetime": 1736192820000
    },
    {
      "open": 21.8502,
      "high": 21.8502,
      "low": 21.8502,
      "close": 21.8502,
      "volume": 170,
      "datetime": 1736192880000
    },
    {
      "open": 21.86,
      "high": 21.8701,
      "low": 21.86,
      "close": 21.8701,
      "volume": 1673,
      "datetime": 1736192940000
    },
    {
      "open": 21.88,
      "high": 21.89,
      "low": 21.88,
      "close": 21.89,
      "volume": 4035,
      "datetime": 1736193060000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.88,
      "close": 21.89,
      "volume": 750,
      "datetime": 1736193120000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.87,
      "close": 21.87,
      "volume": 975,
      "datetime": 1736193180000
    },
    {
      "open": 21.8732,
      "high": 21.875,
      "low": 21.8732,
      "close": 21.875,
      "volume": 2064,
      "datetime": 1736193240000
    },
    {
      "open": 21.885,
      "high": 21.8959,
      "low": 21.885,
      "close": 21.89,
      "volume": 19065,
      "datetime": 1736193300000
    },
    {
      "open": 21.88,
      "high": 21.885,
      "low": 21.88,
      "close": 21.88,
      "volume": 19848,
      "datetime": 1736193360000
    },
    {
      "open": 21.9034,
      "high": 21.9034,
      "low": 21.9034,
      "close": 21.9034,
      "volume": 100,
      "datetime": 1736193420000
    },
    {
      "open": 21.9134,
      "high": 21.9134,
      "low": 21.89,
      "close": 21.89,
      "volume": 980,
      "datetime": 1736193480000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.86,
      "close": 21.865,
      "volume": 3127,
      "datetime": 1736193600000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.855,
      "close": 21.86,
      "volume": 2520,
      "datetime": 1736193660000
    },
    {
      "open": 21.855,
      "high": 21.855,
      "low": 21.855,
      "close": 21.855,
      "volume": 200,
      "datetime": 1736193720000
    },
    {
      "open": 21.86,
      "high": 21.865,
      "low": 21.85,
      "close": 21.85,
      "volume": 1373,
      "datetime": 1736193780000
    },
    {
      "open": 21.845,
      "high": 21.8474,
      "low": 21.845,
      "close": 21.845,
      "volume": 400,
      "datetime": 1736193840000
    },
    {
      "open": 21.85,
      "high": 21.8564,
      "low": 21.8435,
      "close": 21.8564,
      "volume": 1214,
      "datetime": 1736193900000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 348,
      "datetime": 1736193960000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.845,
      "close": 21.85,
      "volume": 2019,
      "datetime": 1736194020000
    },
    {
      "open": 21.855,
      "high": 21.86,
      "low": 21.855,
      "close": 21.86,
      "volume": 1889,
      "datetime": 1736194080000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.8498,
      "close": 21.85,
      "volume": 1910,
      "datetime": 1736194200000
    },
    {
      "open": 21.845,
      "high": 21.845,
      "low": 21.845,
      "close": 21.845,
      "volume": 100,
      "datetime": 1736194260000
    },
    {
      "open": 21.85,
      "high": 21.86,
      "low": 21.84,
      "close": 21.84,
      "volume": 3815,
      "datetime": 1736194320000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.815,
      "close": 21.815,
      "volume": 6149,
      "datetime": 1736194380000
    },
    {
      "open": 21.8224,
      "high": 21.8263,
      "low": 21.82,
      "close": 21.82,
      "volume": 550,
      "datetime": 1736194440000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.8,
      "close": 21.81,
      "volume": 1575,
      "datetime": 1736194500000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.81,
      "close": 21.81,
      "volume": 675,
      "datetime": 1736194560000
    },
    {
      "open": 21.805,
      "high": 21.81,
      "low": 21.805,
      "close": 21.81,
      "volume": 4176,
      "datetime": 1736194620000
    },
    {
      "open": 21.81,
      "high": 21.82,
      "low": 21.81,
      "close": 21.82,
      "volume": 400,
      "datetime": 1736194680000
    },
    {
      "open": 21.815,
      "high": 21.815,
      "low": 21.81,
      "close": 21.81,
      "volume": 1296,
      "datetime": 1736194740000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.8,
      "close": 21.81,
      "volume": 4125,
      "datetime": 1736194800000
    },
    {
      "open": 21.805,
      "high": 21.805,
      "low": 21.8001,
      "close": 21.8025,
      "volume": 3506,
      "datetime": 1736194860000
    },
    {
      "open": 21.805,
      "high": 21.81,
      "low": 21.805,
      "close": 21.81,
      "volume": 300,
      "datetime": 1736194920000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.8,
      "close": 21.8,
      "volume": 3168,
      "datetime": 1736194980000
    },
    {
      "open": 21.795,
      "high": 21.795,
      "low": 21.79,
      "close": 21.79,
      "volume": 790,
      "datetime": 1736195040000
    },
    {
      "open": 21.79,
      "high": 21.805,
      "low": 21.785,
      "close": 21.805,
      "volume": 1887,
      "datetime": 1736195100000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.8,
      "close": 21.805,
      "volume": 1450,
      "datetime": 1736195160000
    },
    {
      "open": 21.82,
      "high": 21.83,
      "low": 21.82,
      "close": 21.83,
      "volume": 600,
      "datetime": 1736195220000
    },
    {
      "open": 21.84,
      "high": 21.8484,
      "low": 21.835,
      "close": 21.84,
      "volume": 5619,
      "datetime": 1736195280000
    },
    {
      "open": 21.8401,
      "high": 21.845,
      "low": 21.825,
      "close": 21.8301,
      "volume": 11115,
      "datetime": 1736195340000
    },
    {
      "open": 21.835,
      "high": 21.8509,
      "low": 21.835,
      "close": 21.84,
      "volume": 7180,
      "datetime": 1736195400000
    },
    {
      "open": 21.85,
      "high": 21.86,
      "low": 21.85,
      "close": 21.85,
      "volume": 1470,
      "datetime": 1736195460000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.831,
      "close": 21.84,
      "volume": 1736,
      "datetime": 1736195520000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.83,
      "close": 21.83,
      "volume": 350,
      "datetime": 1736195580000
    },
    {
      "open": 21.825,
      "high": 21.825,
      "low": 21.82,
      "close": 21.82,
      "volume": 1500,
      "datetime": 1736195640000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.81,
      "close": 21.81,
      "volume": 825,
      "datetime": 1736195700000
    },
    {
      "open": 21.81,
      "high": 21.8268,
      "low": 21.81,
      "close": 21.8268,
      "volume": 935,
      "datetime": 1736195760000
    },
    {
      "open": 21.83,
      "high": 21.84,
      "low": 21.83,
      "close": 21.84,
      "volume": 350,
      "datetime": 1736195820000
    },
    {
      "open": 21.8617,
      "high": 21.875,
      "low": 21.8617,
      "close": 21.875,
      "volume": 2099,
      "datetime": 1736195880000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.86,
      "close": 21.86,
      "volume": 1403,
      "datetime": 1736195940000
    },
    {
      "open": 21.875,
      "high": 21.88,
      "low": 21.8501,
      "close": 21.8501,
      "volume": 2141,
      "datetime": 1736196000000
    },
    {
      "open": 21.8599,
      "high": 21.865,
      "low": 21.855,
      "close": 21.855,
      "volume": 2614,
      "datetime": 1736196060000
    },
    {
      "open": 21.86,
      "high": 21.8699,
      "low": 21.86,
      "close": 21.86,
      "volume": 1175,
      "datetime": 1736196120000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 200,
      "datetime": 1736196180000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.86,
      "close": 21.86,
      "volume": 725,
      "datetime": 1736196240000
    },
    {
      "open": 21.845,
      "high": 21.8644,
      "low": 21.845,
      "close": 21.86,
      "volume": 1200,
      "datetime": 1736196300000
    },
    {
      "open": 21.8501,
      "high": 21.8863,
      "low": 21.8501,
      "close": 21.8863,
      "volume": 26211,
      "datetime": 1736196360000
    },
    {
      "open": 21.885,
      "high": 21.905,
      "low": 21.885,
      "close": 21.9,
      "volume": 13376,
      "datetime": 1736196420000
    },
    {
      "open": 21.891,
      "high": 21.891,
      "low": 21.88,
      "close": 21.88,
      "volume": 2706,
      "datetime": 1736196480000
    },
    {
      "open": 21.885,
      "high": 21.89,
      "low": 21.885,
      "close": 21.89,
      "volume": 300,
      "datetime": 1736196540000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.855,
      "close": 21.86,
      "volume": 5882,
      "datetime": 1736196600000
    },
    {
      "open": 21.86,
      "high": 21.865,
      "low": 21.85,
      "close": 21.85,
      "volume": 975,
      "datetime": 1736196660000
    },
    {
      "open": 21.84,
      "high": 21.8676,
      "low": 21.84,
      "close": 21.855,
      "volume": 7877,
      "datetime": 1736196720000
    },
    {
      "open": 21.8525,
      "high": 21.8525,
      "low": 21.83,
      "close": 21.8497,
      "volume": 12470,
      "datetime": 1736196780000
    },
    {
      "open": 21.8399,
      "high": 21.855,
      "low": 21.825,
      "close": 21.845,
      "volume": 4501,
      "datetime": 1736196840000
    },
    {
      "open": 21.835,
      "high": 21.85,
      "low": 21.835,
      "close": 21.85,
      "volume": 2007,
      "datetime": 1736196900000
    },
    {
      "open": 21.8401,
      "high": 21.865,
      "low": 21.8401,
      "close": 21.8621,
      "volume": 2375,
      "datetime": 1736196960000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.855,
      "close": 21.865,
      "volume": 4436,
      "datetime": 1736197020000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.855,
      "close": 21.855,
      "volume": 31650,
      "datetime": 1736197080000
    },
    {
      "open": 21.855,
      "high": 21.865,
      "low": 21.79,
      "close": 21.84,
      "volume": 46412,
      "datetime": 1736197140000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 1856,
      "datetime": 1736197200000
    },
    {
      "open": 21.78,
      "high": 21.78,
      "low": 21.78,
      "close": 21.78,
      "volume": 200,
      "datetime": 1736197800000
    },
    {
      "open": 21.7705,
      "high": 21.7705,
      "low": 21.7705,
      "close": 21.7705,
      "volume": 8588,
      "datetime": 1736197920000
    },
    {
      "open": 21.79,
      "high": 21.8,
      "low": 21.79,
      "close": 21.8,
      "volume": 5730,
      "datetime": 1736198040000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.79,
      "close": 21.79,
      "volume": 3965,
      "datetime": 1736198100000
    },
    {
      "open": 21.78,
      "high": 21.78,
      "low": 21.78,
      "close": 21.78,
      "volume": 600,
      "datetime": 1736198400000
    },
    {
      "open": 21.8495,
      "high": 21.8495,
      "low": 21.8495,
      "close": 21.8495,
      "volume": 100,
      "datetime": 1736198520000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.79,
      "close": 21.79,
      "volume": 999,
      "datetime": 1736198940000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.82,
      "close": 21.82,
      "volume": 906,
      "datetime": 1736199180000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.86,
      "close": 21.86,
      "volume": 320,
      "datetime": 1736199360000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 124,
      "datetime": 1736199420000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 225,
      "datetime": 1736199480000
    },
    {
      "open": 21.87,
      "high": 21.9,
      "low": 21.87,
      "close": 21.9,
      "volume": 200,
      "datetime": 1736200200000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 300,
      "datetime": 1736200380000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 100,
      "datetime": 1736200560000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 780,
      "datetime": 1736200680000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.95,
      "close": 21.95,
      "volume": 4070,
      "datetime": 1736200800000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.95,
      "close": 21.95,
      "volume": 250,
      "datetime": 1736200920000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 600,
      "datetime": 1736201340000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.95,
      "close": 21.95,
      "volume": 100,
      "datetime": 1736201460000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 3450,
      "datetime": 1736201880000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.86,
      "close": 21.86,
      "volume": 366,
      "datetime": 1736201940000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.87,
      "close": 21.87,
      "volume": 130,
      "datetime": 1736202120000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 100,
      "datetime": 1736202300000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 400,
      "datetime": 1736203680000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 100,
      "datetime": 1736204100000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 100,
      "datetime": 1736204340000
    },
    {
      "open": 21.8501,
      "high": 21.8501,
      "low": 21.8501,
      "close": 21.8501,
      "volume": 100,
      "datetime": 1736204700000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 1000,
      "datetime": 1736204820000
    },
    {
      "open": 21.8309,
      "high": 21.8309,
      "low": 21.8309,
      "close": 21.8309,
      "volume": 550,
      "datetime": 1736204880000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.83,
      "close": 21.83,
      "volume": 1100,
      "datetime": 1736204940000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.83,
      "close": 21.83,
      "volume": 100,
      "datetime": 1736205360000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 333,
      "datetime": 1736205780000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.81,
      "close": 21.81,
      "volume": 110,
      "datetime": 1736205840000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.81,
      "close": 21.81,
      "volume": 190,
      "datetime": 1736206980000
    },
    {
      "open": 21.8009,
      "high": 21.8009,
      "low": 21.8009,
      "close": 21.8009,
      "volume": 333,
      "datetime": 1736208060000
    },
    {
      "open": 21.8492,
      "high": 21.8492,
      "low": 21.8492,
      "close": 21.8492,
      "volume": 133,
      "datetime": 1736208360000
    },
    {
      "open": 21.8498,
      "high": 21.8498,
      "low": 21.8498,
      "close": 21.8498,
      "volume": 333,
      "datetime": 1736208480000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 1100,
      "datetime": 1736208960000
    },
    {
      "open": 21.8008,
      "high": 21.8008,
      "low": 21.8008,
      "close": 21.8008,
      "volume": 400,
      "datetime": 1736209380000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.79,
      "close": 21.79,
      "volume": 1100,
      "datetime": 1736209680000
    },
    {
      "open": 21.76,
      "high": 21.76,
      "low": 21.73,
      "close": 21.73,
      "volume": 400,
      "datetime": 1736210100000
    },
    {
      "open": 21.74,
      "high": 21.74,
      "low": 21.74,
      "close": 21.74,
      "volume": 100,
      "datetime": 1736210160000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 100,
      "datetime": 1736210340000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 1000,
      "datetime": 1736210580000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 200,
      "datetime": 1736210640000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 4815,
      "datetime": 1736210760000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 206,
      "datetime": 1736211000000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 100,
      "datetime": 1736211060000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 900,
      "datetime": 1736211300000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 5100,
      "datetime": 1736211360000
    },
    {
      "open": 21.86,
      "high": 21.87,
      "low": 21.86,
      "close": 21.87,
      "volume": 1066,
      "datetime": 1736211540000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.87,
      "close": 21.87,
      "volume": 1,
      "datetime": 1736211660000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 506,
      "datetime": 1736211720000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 1494,
      "datetime": 1736211780000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 300,
      "datetime": 1736211900000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 1000,
      "datetime": 1736212440000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.87,
      "close": 21.87,
      "volume": 1,
      "datetime": 1736212560000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.86,
      "close": 21.86,
      "volume": 299,
      "datetime": 1736212680000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 1,
      "datetime": 1736213160000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.91,
      "close": 21.91,
      "volume": 1,
      "datetime": 1736213220000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.91,
      "close": 21.91,
      "volume": 1000,
      "datetime": 1736213340000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 100,
      "datetime": 1736213580000
    },
    {
      "open": 21.93,
      "high": 21.93,
      "low": 21.93,
      "close": 21.93,
      "volume": 6,
      "datetime": 1736213640000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 20,
      "datetime": 1736213700000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 5,
      "datetime": 1736214000000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 400,
      "datetime": 1736218020000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.91,
      "close": 21.91,
      "volume": 300,
      "datetime": 1736218080000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.91,
      "close": 21.91,
      "volume": 1000,
      "datetime": 1736220000000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.92,
      "close": 21.92,
      "volume": 1000,
      "datetime": 1736220240000
    },
    {
      "open": 21.92,
      "high": 21.96,
      "low": 21.92,
      "close": 21.96,
      "volume": 3151,
      "datetime": 1736220540000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 1,
      "datetime": 1736221080000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.95,
      "close": 21.95,
      "volume": 5,
      "datetime": 1736221560000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.96,
      "close": 21.96,
      "volume": 9,
      "datetime": 1736221620000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.96,
      "close": 21.96,
      "volume": 50,
      "datetime": 1736221860000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 150,
      "datetime": 1736222220000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.93,
      "close": 21.93,
      "volume": 16,
      "datetime": 1736222460000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.9,
      "close": 21.9,
      "volume": 100,
      "datetime": 1736223000000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 1,
      "datetime": 1736224200000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.91,
      "close": 21.91,
      "volume": 150,
      "datetime": 1736224920000
    },
    {
      "open": 21.93,
      "high": 21.93,
      "low": 21.93,
      "close": 21.93,
      "volume": 100,
      "datetime": 1736225100000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.96,
      "close": 21.96,
      "volume": 5,
      "datetime": 1736227320000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.95,
      "close": 21.95,
      "volume": 1000,
      "datetime": 1736227680000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.96,
      "close": 21.96,
      "volume": 10,
      "datetime": 1736227920000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.95,
      "close": 21.95,
      "volume": 7,
      "datetime": 1736229240000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 25,
      "datetime": 1736229300000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 1,
      "datetime": 1736230440000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.92,
      "close": 21.92,
      "volume": 3,
      "datetime": 1736230560000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 4,
      "datetime": 1736231160000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 1,
      "datetime": 1736233320000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 900,
      "datetime": 1736233380000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 200,
      "datetime": 1736233800000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.88,
      "close": 21.88,
      "volume": 121,
      "datetime": 1736233920000
    },
    {
      "open": 21.93,
      "high": 21.93,
      "low": 21.9,
      "close": 21.9,
      "volume": 27,
      "datetime": 1736238420000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 25,
      "datetime": 1736238480000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.91,
      "close": 21.91,
      "volume": 25,
      "datetime": 1736238600000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.92,
      "close": 21.92,
      "volume": 100,
      "datetime": 1736238900000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 200,
      "datetime": 1736239740000
    },
    {
      "open": 21.97,
      "high": 21.97,
      "low": 21.97,
      "close": 21.97,
      "volume": 1,
      "datetime": 1736240160000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.96,
      "close": 21.96,
      "volume": 10,
      "datetime": 1736240220000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.91,
      "close": 21.91,
      "volume": 209,
      "datetime": 1736240400000
    },
    {
      "open": 21.97,
      "high": 21.97,
      "low": 21.97,
      "close": 21.97,
      "volume": 396,
      "datetime": 1736244660000
    },
    {
      "open": 22.01,
      "high": 22.01,
      "low": 22.01,
      "close": 22.01,
      "volume": 1526,
      "datetime": 1736244840000
    },
    {
      "open": 22.01,
      "high": 22.01,
      "low": 22.01,
      "close": 22.01,
      "volume": 235,
      "datetime": 1736246160000
    },
    {
      "open": 21.98,
      "high": 21.98,
      "low": 21.98,
      "close": 21.98,
      "volume": 135,
      "datetime": 1736247060000
    },
    {
      "open": 22.01,
      "high": 22.01,
      "low": 22.01,
      "close": 22.01,
      "volume": 220,
      "datetime": 1736247480000
    },
    {
      "open": 22.04,
      "high": 22.04,
      "low": 22.04,
      "close": 22.04,
      "volume": 651,
      "datetime": 1736247720000
    },
    {
      "open": 22.03,
      "high": 22.03,
      "low": 22.03,
      "close": 22.03,
      "volume": 1000,
      "datetime": 1736247780000
    },
    {
      "open": 22,
      "high": 22,
      "low": 22,
      "close": 22,
      "volume": 995,
      "datetime": 1736247900000
    },
    {
      "open": 22.02,
      "high": 22.02,
      "low": 22.02,
      "close": 22.02,
      "volume": 229,
      "datetime": 1736248980000
    },
    {
      "open": 22.06,
      "high": 22.06,
      "low": 22.06,
      "close": 22.06,
      "volume": 199,
      "datetime": 1736249520000
    },
    {
      "open": 22.09,
      "high": 22.09,
      "low": 22.09,
      "close": 22.09,
      "volume": 200,
      "datetime": 1736249640000
    },
    {
      "open": 22.11,
      "high": 22.11,
      "low": 22.11,
      "close": 22.11,
      "volume": 100,
      "datetime": 1736249880000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.15,
      "close": 22.15,
      "volume": 100,
      "datetime": 1736250060000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.16,
      "close": 22.16,
      "volume": 100,
      "datetime": 1736250120000
    },
    {
      "open": 22.13,
      "high": 22.13,
      "low": 22.13,
      "close": 22.13,
      "volume": 900,
      "datetime": 1736250720000
    },
    {
      "open": 22.13,
      "high": 22.13,
      "low": 22.13,
      "close": 22.13,
      "volume": 897,
      "datetime": 1736250780000
    },
    {
      "open": 22.13,
      "high": 22.13,
      "low": 22.13,
      "close": 22.13,
      "volume": 100,
      "datetime": 1736250960000
    },
    {
      "open": 22.12,
      "high": 22.12,
      "low": 22.12,
      "close": 22.12,
      "volume": 100,
      "datetime": 1736251380000
    },
    {
      "open": 22.12,
      "high": 22.12,
      "low": 22.12,
      "close": 22.12,
      "volume": 297,
      "datetime": 1736251500000
    },
    {
      "open": 22.12,
      "high": 22.12,
      "low": 22.12,
      "close": 22.12,
      "volume": 100,
      "datetime": 1736251920000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.15,
      "close": 22.15,
      "volume": 100,
      "datetime": 1736252040000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.15,
      "close": 22.15,
      "volume": 100,
      "datetime": 1736252220000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.17,
      "close": 22.17,
      "volume": 150,
      "datetime": 1736252460000
    },
    {
      "open": 22.14,
      "high": 22.14,
      "low": 22.14,
      "close": 22.14,
      "volume": 110,
      "datetime": 1736254500000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.16,
      "close": 22.16,
      "volume": 100,
      "datetime": 1736255040000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.15,
      "close": 22.15,
      "volume": 1759,
      "datetime": 1736255100000
    },
    {
      "open": 22.14,
      "high": 22.16,
      "low": 22.14,
      "close": 22.16,
      "volume": 3584,
      "datetime": 1736255220000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.18,
      "close": 22.18,
      "volume": 150,
      "datetime": 1736255580000
    },
    {
      "open": 22.13,
      "high": 22.13,
      "low": 22.13,
      "close": 22.13,
      "volume": 250,
      "datetime": 1736256240000
    },
    {
      "open": 22.13,
      "high": 22.13,
      "low": 22.13,
      "close": 22.13,
      "volume": 1500,
      "datetime": 1736256300000
    },
    {
      "open": 22.13,
      "high": 22.13,
      "low": 22.13,
      "close": 22.13,
      "volume": 557,
      "datetime": 1736256360000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.15,
      "close": 22.15,
      "volume": 200,
      "datetime": 1736256840000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.16,
      "close": 22.16,
      "volume": 100,
      "datetime": 1736257020000
    },
    {
      "open": 22.19,
      "high": 22.19,
      "low": 22.19,
      "close": 22.19,
      "volume": 300,
      "datetime": 1736257140000
    },
    {
      "open": 22.1802,
      "high": 22.1802,
      "low": 22.18,
      "close": 22.18,
      "volume": 921,
      "datetime": 1736257200000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.18,
      "close": 22.18,
      "volume": 201,
      "datetime": 1736257320000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.18,
      "close": 22.18,
      "volume": 100,
      "datetime": 1736257440000
    },
    {
      "open": 22.19,
      "high": 22.19,
      "low": 22.19,
      "close": 22.19,
      "volume": 1000,
      "datetime": 1736257500000
    },
    {
      "open": 22.1692,
      "high": 22.1692,
      "low": 22.1692,
      "close": 22.1692,
      "volume": 100,
      "datetime": 1736257560000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.16,
      "close": 22.16,
      "volume": 100,
      "datetime": 1736257620000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.15,
      "close": 22.15,
      "volume": 100,
      "datetime": 1736257860000
    },
    {
      "open": 22.1699,
      "high": 22.1699,
      "low": 22.1699,
      "close": 22.1699,
      "volume": 500,
      "datetime": 1736257920000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.17,
      "close": 22.17,
      "volume": 195,
      "datetime": 1736258040000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.18,
      "close": 22.18,
      "volume": 580,
      "datetime": 1736258460000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.15,
      "close": 22.15,
      "volume": 1759,
      "datetime": 1736258520000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.15,
      "close": 22.15,
      "volume": 915,
      "datetime": 1736258820000
    },
    {
      "open": 22.175,
      "high": 22.19,
      "low": 22.17,
      "close": 22.19,
      "volume": 4100,
      "datetime": 1736259120000
    },
    {
      "open": 22.19,
      "high": 22.19,
      "low": 22.1805,
      "close": 22.1805,
      "volume": 2259,
      "datetime": 1736259180000
    },
    {
      "open": 22.19,
      "high": 22.2,
      "low": 22.19,
      "close": 22.2,
      "volume": 750,
      "datetime": 1736259420000
    },
    {
      "open": 22.2,
      "high": 22.2,
      "low": 22.2,
      "close": 22.2,
      "volume": 100,
      "datetime": 1736259480000
    },
    {
      "open": 22.21,
      "high": 22.21,
      "low": 22.2,
      "close": 22.2,
      "volume": 769,
      "datetime": 1736259540000
    },
    {
      "open": 22.1709,
      "high": 22.1709,
      "low": 22.1709,
      "close": 22.1709,
      "volume": 400,
      "datetime": 1736259720000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.17,
      "close": 22.17,
      "volume": 128,
      "datetime": 1736259840000
    },
    {
      "open": 22.17,
      "high": 22.19,
      "low": 22.17,
      "close": 22.19,
      "volume": 600,
      "datetime": 1736259960000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.17,
      "close": 22.17,
      "volume": 400,
      "datetime": 1736260020000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.15,
      "close": 22.15,
      "volume": 600,
      "datetime": 1736260080000
    },
    {
      "open": 22.16,
      "high": 22.195,
      "low": 22.16,
      "close": 22.1937,
      "volume": 7377,
      "datetime": 1736260200000
    },
    {
      "open": 22.195,
      "high": 22.195,
      "low": 22.1579,
      "close": 22.175,
      "volume": 22798,
      "datetime": 1736260260000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.15,
      "close": 22.18,
      "volume": 5187,
      "datetime": 1736260320000
    },
    {
      "open": 22.1774,
      "high": 22.19,
      "low": 22.1724,
      "close": 22.19,
      "volume": 2362,
      "datetime": 1736260380000
    },
    {
      "open": 22.19,
      "high": 22.26,
      "low": 22.19,
      "close": 22.24,
      "volume": 8684,
      "datetime": 1736260440000
    },
    {
      "open": 22.25,
      "high": 22.25,
      "low": 22.21,
      "close": 22.2198,
      "volume": 2149,
      "datetime": 1736260500000
    },
    {
      "open": 22.24,
      "high": 22.25,
      "low": 22.24,
      "close": 22.25,
      "volume": 12422,
      "datetime": 1736260560000
    },
    {
      "open": 22.27,
      "high": 22.29,
      "low": 22.26,
      "close": 22.2799,
      "volume": 2251,
      "datetime": 1736260620000
    },
    {
      "open": 22.245,
      "high": 22.245,
      "low": 22.23,
      "close": 22.23,
      "volume": 6900,
      "datetime": 1736260680000
    },
    {
      "open": 22.22,
      "high": 22.23,
      "low": 22.19,
      "close": 22.2226,
      "volume": 4250,
      "datetime": 1736260740000
    },
    {
      "open": 22.23,
      "high": 22.26,
      "low": 22.23,
      "close": 22.2468,
      "volume": 1516,
      "datetime": 1736260800000
    },
    {
      "open": 22.2,
      "high": 22.21,
      "low": 22.2,
      "close": 22.21,
      "volume": 1700,
      "datetime": 1736260860000
    },
    {
      "open": 22.18,
      "high": 22.1945,
      "low": 22.1789,
      "close": 22.1901,
      "volume": 7877,
      "datetime": 1736260920000
    },
    {
      "open": 22.1874,
      "high": 22.1874,
      "low": 22.1599,
      "close": 22.16,
      "volume": 1935,
      "datetime": 1736260980000
    },
    {
      "open": 22.16,
      "high": 22.1815,
      "low": 22.16,
      "close": 22.1815,
      "volume": 6702,
      "datetime": 1736261040000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.16,
      "close": 22.16,
      "volume": 1686,
      "datetime": 1736261100000
    },
    {
      "open": 22.205,
      "high": 22.21,
      "low": 22.205,
      "close": 22.21,
      "volume": 501,
      "datetime": 1736261160000
    },
    {
      "open": 22.2149,
      "high": 22.24,
      "low": 22.2149,
      "close": 22.23,
      "volume": 4475,
      "datetime": 1736261220000
    },
    {
      "open": 22.19,
      "high": 22.19,
      "low": 22.18,
      "close": 22.18,
      "volume": 1128,
      "datetime": 1736261280000
    },
    {
      "open": 22.2325,
      "high": 22.2325,
      "low": 22.2325,
      "close": 22.2325,
      "volume": 897,
      "datetime": 1736261400000
    },
    {
      "open": 22.2426,
      "high": 22.2426,
      "low": 22.2399,
      "close": 22.24,
      "volume": 3201,
      "datetime": 1736261460000
    },
    {
      "open": 22.25,
      "high": 22.25,
      "low": 22.2361,
      "close": 22.2361,
      "volume": 2048,
      "datetime": 1736261520000
    },
    {
      "open": 22.26,
      "high": 22.29,
      "low": 22.26,
      "close": 22.2899,
      "volume": 2900,
      "datetime": 1736261580000
    },
    {
      "open": 22.295,
      "high": 22.295,
      "low": 22.27,
      "close": 22.2726,
      "volume": 2500,
      "datetime": 1736261640000
    },
    {
      "open": 22.28,
      "high": 22.28,
      "low": 22.27,
      "close": 22.28,
      "volume": 1583,
      "datetime": 1736261700000
    },
    {
      "open": 22.3,
      "high": 22.3388,
      "low": 22.3,
      "close": 22.335,
      "volume": 14252,
      "datetime": 1736261760000
    },
    {
      "open": 22.325,
      "high": 22.3426,
      "low": 22.3184,
      "close": 22.3426,
      "volume": 2506,
      "datetime": 1736261820000
    },
    {
      "open": 22.33,
      "high": 22.37,
      "low": 22.325,
      "close": 22.37,
      "volume": 13862,
      "datetime": 1736261880000
    },
    {
      "open": 22.36,
      "high": 22.39,
      "low": 22.34,
      "close": 22.3403,
      "volume": 8681,
      "datetime": 1736261940000
    },
    {
      "open": 22.35,
      "high": 22.38,
      "low": 22.33,
      "close": 22.38,
      "volume": 14580,
      "datetime": 1736262000000
    },
    {
      "open": 22.3998,
      "high": 22.54,
      "low": 22.3998,
      "close": 22.501,
      "volume": 21984,
      "datetime": 1736262060000
    },
    {
      "open": 22.51,
      "high": 22.515,
      "low": 22.4,
      "close": 22.4,
      "volume": 24402,
      "datetime": 1736262120000
    },
    {
      "open": 22.39,
      "high": 22.465,
      "low": 22.39,
      "close": 22.41,
      "volume": 15942,
      "datetime": 1736262180000
    },
    {
      "open": 22.43,
      "high": 22.4799,
      "low": 22.43,
      "close": 22.46,
      "volume": 10605,
      "datetime": 1736262240000
    },
    {
      "open": 22.48,
      "high": 22.515,
      "low": 22.47,
      "close": 22.49,
      "volume": 13174,
      "datetime": 1736262300000
    },
    {
      "open": 22.5,
      "high": 22.52,
      "low": 22.47,
      "close": 22.5,
      "volume": 21430,
      "datetime": 1736262360000
    },
    {
      "open": 22.5305,
      "high": 22.61,
      "low": 22.5305,
      "close": 22.58,
      "volume": 14365,
      "datetime": 1736262420000
    },
    {
      "open": 22.5769,
      "high": 22.5769,
      "low": 22.52,
      "close": 22.54,
      "volume": 10108,
      "datetime": 1736262480000
    },
    {
      "open": 22.57,
      "high": 22.6,
      "low": 22.56,
      "close": 22.56,
      "volume": 6164,
      "datetime": 1736262540000
    },
    {
      "open": 22.57,
      "high": 22.68,
      "low": 22.56,
      "close": 22.64,
      "volume": 24482,
      "datetime": 1736262600000
    },
    {
      "open": 22.63,
      "high": 22.66,
      "low": 22.59,
      "close": 22.66,
      "volume": 14673,
      "datetime": 1736262660000
    },
    {
      "open": 22.66,
      "high": 22.6766,
      "low": 22.61,
      "close": 22.61,
      "volume": 6855,
      "datetime": 1736262720000
    },
    {
      "open": 22.625,
      "high": 22.625,
      "low": 22.58,
      "close": 22.6,
      "volume": 2990,
      "datetime": 1736262780000
    },
    {
      "open": 22.63,
      "high": 22.6687,
      "low": 22.625,
      "close": 22.66,
      "volume": 5347,
      "datetime": 1736262840000
    },
    {
      "open": 22.7,
      "high": 22.7627,
      "low": 22.6931,
      "close": 22.7627,
      "volume": 4274,
      "datetime": 1736262900000
    },
    {
      "open": 22.745,
      "high": 22.745,
      "low": 22.67,
      "close": 22.68,
      "volume": 11743,
      "datetime": 1736262960000
    },
    {
      "open": 22.72,
      "high": 22.74,
      "low": 22.6579,
      "close": 22.74,
      "volume": 3137,
      "datetime": 1736263020000
    },
    {
      "open": 22.73,
      "high": 22.73,
      "low": 22.69,
      "close": 22.705,
      "volume": 6785,
      "datetime": 1736263080000
    },
    {
      "open": 22.7129,
      "high": 22.72,
      "low": 22.65,
      "close": 22.6512,
      "volume": 8254,
      "datetime": 1736263140000
    },
    {
      "open": 22.6288,
      "high": 22.6801,
      "low": 22.62,
      "close": 22.67,
      "volume": 10254,
      "datetime": 1736263200000
    },
    {
      "open": 22.656,
      "high": 22.68,
      "low": 22.6313,
      "close": 22.68,
      "volume": 11310,
      "datetime": 1736263260000
    },
    {
      "open": 22.69,
      "high": 22.7196,
      "low": 22.65,
      "close": 22.69,
      "volume": 4070,
      "datetime": 1736263320000
    },
    {
      "open": 22.68,
      "high": 22.7,
      "low": 22.67,
      "close": 22.7,
      "volume": 1641,
      "datetime": 1736263380000
    },
    {
      "open": 22.68,
      "high": 22.7,
      "low": 22.68,
      "close": 22.695,
      "volume": 2692,
      "datetime": 1736263440000
    },
    {
      "open": 22.69,
      "high": 22.69,
      "low": 22.645,
      "close": 22.67,
      "volume": 1768,
      "datetime": 1736263500000
    },
    {
      "open": 22.68,
      "high": 22.68,
      "low": 22.62,
      "close": 22.625,
      "volume": 12172,
      "datetime": 1736263560000
    },
    {
      "open": 22.645,
      "high": 22.67,
      "low": 22.635,
      "close": 22.67,
      "volume": 5193,
      "datetime": 1736263620000
    },
    {
      "open": 22.68,
      "high": 22.7,
      "low": 22.68,
      "close": 22.7,
      "volume": 3150,
      "datetime": 1736263680000
    },
    {
      "open": 22.695,
      "high": 22.7167,
      "low": 22.69,
      "close": 22.71,
      "volume": 5434,
      "datetime": 1736263740000
    },
    {
      "open": 22.71,
      "high": 22.71,
      "low": 22.69,
      "close": 22.6999,
      "volume": 7005,
      "datetime": 1736263800000
    },
    {
      "open": 22.71,
      "high": 22.7272,
      "low": 22.71,
      "close": 22.7272,
      "volume": 4150,
      "datetime": 1736263860000
    },
    {
      "open": 22.74,
      "high": 22.759,
      "low": 22.7164,
      "close": 22.74,
      "volume": 10412,
      "datetime": 1736263920000
    },
    {
      "open": 22.75,
      "high": 22.75,
      "low": 22.73,
      "close": 22.74,
      "volume": 4884,
      "datetime": 1736263980000
    },
    {
      "open": 22.745,
      "high": 22.81,
      "low": 22.7383,
      "close": 22.7897,
      "volume": 37460,
      "datetime": 1736264040000
    },
    {
      "open": 22.78,
      "high": 22.82,
      "low": 22.768,
      "close": 22.8083,
      "volume": 11811,
      "datetime": 1736264100000
    },
    {
      "open": 22.81,
      "high": 22.81,
      "low": 22.79,
      "close": 22.7963,
      "volume": 12602,
      "datetime": 1736264160000
    },
    {
      "open": 22.78,
      "high": 22.81,
      "low": 22.77,
      "close": 22.8001,
      "volume": 6242,
      "datetime": 1736264220000
    },
    {
      "open": 22.8,
      "high": 22.835,
      "low": 22.8,
      "close": 22.83,
      "volume": 13231,
      "datetime": 1736264280000
    },
    {
      "open": 22.83,
      "high": 22.9,
      "low": 22.83,
      "close": 22.86,
      "volume": 21220,
      "datetime": 1736264340000
    },
    {
      "open": 22.86,
      "high": 22.86,
      "low": 22.82,
      "close": 22.835,
      "volume": 15846,
      "datetime": 1736264400000
    },
    {
      "open": 22.84,
      "high": 22.86,
      "low": 22.83,
      "close": 22.8466,
      "volume": 13317,
      "datetime": 1736264460000
    },
    {
      "open": 22.84,
      "high": 22.91,
      "low": 22.84,
      "close": 22.91,
      "volume": 12236,
      "datetime": 1736264520000
    },
    {
      "open": 22.89,
      "high": 22.91,
      "low": 22.8882,
      "close": 22.89,
      "volume": 12074,
      "datetime": 1736264580000
    },
    {
      "open": 22.89,
      "high": 22.9184,
      "low": 22.89,
      "close": 22.9184,
      "volume": 5867,
      "datetime": 1736264640000
    },
    {
      "open": 22.91,
      "high": 22.99,
      "low": 22.91,
      "close": 22.92,
      "volume": 31174,
      "datetime": 1736264700000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.88,
      "close": 22.88,
      "volume": 4912,
      "datetime": 1736264760000
    },
    {
      "open": 22.87,
      "high": 22.92,
      "low": 22.87,
      "close": 22.92,
      "volume": 4295,
      "datetime": 1736264820000
    },
    {
      "open": 22.91,
      "high": 22.91,
      "low": 22.88,
      "close": 22.88,
      "volume": 3960,
      "datetime": 1736264880000
    },
    {
      "open": 22.88,
      "high": 22.88,
      "low": 22.82,
      "close": 22.82,
      "volume": 2750,
      "datetime": 1736264940000
    },
    {
      "open": 22.82,
      "high": 22.8426,
      "low": 22.81,
      "close": 22.81,
      "volume": 3737,
      "datetime": 1736265000000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.78,
      "close": 22.79,
      "volume": 18710,
      "datetime": 1736265060000
    },
    {
      "open": 22.79,
      "high": 22.79,
      "low": 22.7601,
      "close": 22.77,
      "volume": 5288,
      "datetime": 1736265120000
    },
    {
      "open": 22.7615,
      "high": 22.78,
      "low": 22.76,
      "close": 22.7702,
      "volume": 2548,
      "datetime": 1736265180000
    },
    {
      "open": 22.8,
      "high": 22.81,
      "low": 22.78,
      "close": 22.81,
      "volume": 3296,
      "datetime": 1736265240000
    },
    {
      "open": 22.79,
      "high": 22.7999,
      "low": 22.78,
      "close": 22.79,
      "volume": 3280,
      "datetime": 1736265300000
    },
    {
      "open": 22.79,
      "high": 22.81,
      "low": 22.77,
      "close": 22.8,
      "volume": 33879,
      "datetime": 1736265360000
    },
    {
      "open": 22.8,
      "high": 22.8,
      "low": 22.7999,
      "close": 22.8,
      "volume": 1786,
      "datetime": 1736265420000
    },
    {
      "open": 22.81,
      "high": 22.82,
      "low": 22.81,
      "close": 22.81,
      "volume": 18052,
      "datetime": 1736265480000
    },
    {
      "open": 22.805,
      "high": 22.81,
      "low": 22.8,
      "close": 22.81,
      "volume": 4128,
      "datetime": 1736265540000
    },
    {
      "open": 22.81,
      "high": 22.8597,
      "low": 22.81,
      "close": 22.855,
      "volume": 1175,
      "datetime": 1736265600000
    },
    {
      "open": 22.83,
      "high": 22.835,
      "low": 22.78,
      "close": 22.78,
      "volume": 2120,
      "datetime": 1736265660000
    },
    {
      "open": 22.78,
      "high": 22.8401,
      "low": 22.78,
      "close": 22.825,
      "volume": 8987,
      "datetime": 1736265720000
    },
    {
      "open": 22.83,
      "high": 22.84,
      "low": 22.82,
      "close": 22.84,
      "volume": 2711,
      "datetime": 1736265780000
    },
    {
      "open": 22.81,
      "high": 22.82,
      "low": 22.81,
      "close": 22.82,
      "volume": 655,
      "datetime": 1736265840000
    },
    {
      "open": 22.83,
      "high": 22.8398,
      "low": 22.82,
      "close": 22.82,
      "volume": 5275,
      "datetime": 1736265900000
    },
    {
      "open": 22.835,
      "high": 22.835,
      "low": 22.81,
      "close": 22.81,
      "volume": 1281,
      "datetime": 1736265960000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.82,
      "close": 22.82,
      "volume": 125,
      "datetime": 1736266020000
    },
    {
      "open": 22.81,
      "high": 22.81,
      "low": 22.785,
      "close": 22.785,
      "volume": 739,
      "datetime": 1736266080000
    },
    {
      "open": 22.7874,
      "high": 22.8,
      "low": 22.78,
      "close": 22.8,
      "volume": 1025,
      "datetime": 1736266140000
    },
    {
      "open": 22.79,
      "high": 22.83,
      "low": 22.79,
      "close": 22.83,
      "volume": 1118,
      "datetime": 1736266200000
    },
    {
      "open": 22.84,
      "high": 22.89,
      "low": 22.84,
      "close": 22.89,
      "volume": 3663,
      "datetime": 1736266260000
    },
    {
      "open": 22.89,
      "high": 22.89,
      "low": 22.875,
      "close": 22.88,
      "volume": 2350,
      "datetime": 1736266320000
    },
    {
      "open": 22.88,
      "high": 22.8802,
      "low": 22.86,
      "close": 22.86,
      "volume": 1826,
      "datetime": 1736266380000
    },
    {
      "open": 22.825,
      "high": 22.84,
      "low": 22.82,
      "close": 22.84,
      "volume": 1943,
      "datetime": 1736266440000
    },
    {
      "open": 22.8464,
      "high": 22.85,
      "low": 22.84,
      "close": 22.85,
      "volume": 631,
      "datetime": 1736266500000
    },
    {
      "open": 22.83,
      "high": 22.83,
      "low": 22.82,
      "close": 22.8237,
      "volume": 350,
      "datetime": 1736266560000
    },
    {
      "open": 22.84,
      "high": 22.865,
      "low": 22.84,
      "close": 22.86,
      "volume": 2621,
      "datetime": 1736266620000
    },
    {
      "open": 22.85,
      "high": 22.86,
      "low": 22.85,
      "close": 22.8503,
      "volume": 2872,
      "datetime": 1736266680000
    },
    {
      "open": 22.855,
      "high": 22.855,
      "low": 22.855,
      "close": 22.855,
      "volume": 100,
      "datetime": 1736266740000
    },
    {
      "open": 22.85,
      "high": 22.85,
      "low": 22.83,
      "close": 22.83,
      "volume": 1050,
      "datetime": 1736266800000
    },
    {
      "open": 22.82,
      "high": 22.83,
      "low": 22.82,
      "close": 22.83,
      "volume": 502,
      "datetime": 1736266860000
    },
    {
      "open": 22.79,
      "high": 22.8,
      "low": 22.78,
      "close": 22.8,
      "volume": 4310,
      "datetime": 1736266920000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.82,
      "close": 22.82,
      "volume": 267,
      "datetime": 1736266980000
    },
    {
      "open": 22.81,
      "high": 22.81,
      "low": 22.791,
      "close": 22.791,
      "volume": 1300,
      "datetime": 1736267040000
    },
    {
      "open": 22.79,
      "high": 22.79,
      "low": 22.79,
      "close": 22.79,
      "volume": 262,
      "datetime": 1736267100000
    },
    {
      "open": 22.79,
      "high": 22.7901,
      "low": 22.77,
      "close": 22.7901,
      "volume": 3462,
      "datetime": 1736267160000
    },
    {
      "open": 22.81,
      "high": 22.81,
      "low": 22.81,
      "close": 22.81,
      "volume": 2537,
      "datetime": 1736267220000
    },
    {
      "open": 22.8,
      "high": 22.8,
      "low": 22.79,
      "close": 22.79,
      "volume": 5335,
      "datetime": 1736267280000
    },
    {
      "open": 22.8,
      "high": 22.8,
      "low": 22.79,
      "close": 22.7903,
      "volume": 3163,
      "datetime": 1736267340000
    },
    {
      "open": 22.79,
      "high": 22.79,
      "low": 22.79,
      "close": 22.79,
      "volume": 125,
      "datetime": 1736267400000
    },
    {
      "open": 22.8196,
      "high": 22.8196,
      "low": 22.795,
      "close": 22.795,
      "volume": 200,
      "datetime": 1736267460000
    },
    {
      "open": 22.79,
      "high": 22.79,
      "low": 22.78,
      "close": 22.7803,
      "volume": 2325,
      "datetime": 1736267520000
    },
    {
      "open": 22.7755,
      "high": 22.78,
      "low": 22.765,
      "close": 22.78,
      "volume": 5100,
      "datetime": 1736267580000
    },
    {
      "open": 22.7601,
      "high": 22.79,
      "low": 22.7601,
      "close": 22.79,
      "volume": 3766,
      "datetime": 1736267640000
    },
    {
      "open": 22.8,
      "high": 22.835,
      "low": 22.8,
      "close": 22.835,
      "volume": 1593,
      "datetime": 1736267700000
    },
    {
      "open": 22.8399,
      "high": 22.8399,
      "low": 22.8399,
      "close": 22.8399,
      "volume": 100,
      "datetime": 1736267760000
    },
    {
      "open": 22.81,
      "high": 22.81,
      "low": 22.79,
      "close": 22.79,
      "volume": 1382,
      "datetime": 1736267820000
    },
    {
      "open": 22.7998,
      "high": 22.7998,
      "low": 22.78,
      "close": 22.78,
      "volume": 425,
      "datetime": 1736267880000
    },
    {
      "open": 22.77,
      "high": 22.77,
      "low": 22.74,
      "close": 22.74,
      "volume": 5875,
      "datetime": 1736267940000
    },
    {
      "open": 22.745,
      "high": 22.745,
      "low": 22.715,
      "close": 22.72,
      "volume": 4931,
      "datetime": 1736268000000
    },
    {
      "open": 22.73,
      "high": 22.76,
      "low": 22.73,
      "close": 22.745,
      "volume": 7325,
      "datetime": 1736268060000
    },
    {
      "open": 22.75,
      "high": 22.7501,
      "low": 22.7301,
      "close": 22.735,
      "volume": 3109,
      "datetime": 1736268120000
    },
    {
      "open": 22.72,
      "high": 22.73,
      "low": 22.72,
      "close": 22.73,
      "volume": 1100,
      "datetime": 1736268180000
    },
    {
      "open": 22.76,
      "high": 22.77,
      "low": 22.75,
      "close": 22.76,
      "volume": 1557,
      "datetime": 1736268240000
    },
    {
      "open": 22.77,
      "high": 22.77,
      "low": 22.77,
      "close": 22.77,
      "volume": 125,
      "datetime": 1736268300000
    },
    {
      "open": 22.75,
      "high": 22.7501,
      "low": 22.75,
      "close": 22.7501,
      "volume": 675,
      "datetime": 1736268360000
    },
    {
      "open": 22.7701,
      "high": 22.78,
      "low": 22.76,
      "close": 22.76,
      "volume": 2092,
      "datetime": 1736268420000
    },
    {
      "open": 22.76,
      "high": 22.79,
      "low": 22.76,
      "close": 22.79,
      "volume": 3436,
      "datetime": 1736268480000
    },
    {
      "open": 22.8,
      "high": 22.815,
      "low": 22.8,
      "close": 22.815,
      "volume": 4300,
      "datetime": 1736268540000
    },
    {
      "open": 22.8183,
      "high": 22.84,
      "low": 22.81,
      "close": 22.84,
      "volume": 8512,
      "datetime": 1736268600000
    },
    {
      "open": 22.84,
      "high": 22.86,
      "low": 22.8235,
      "close": 22.86,
      "volume": 4194,
      "datetime": 1736268660000
    },
    {
      "open": 22.86,
      "high": 22.86,
      "low": 22.84,
      "close": 22.84,
      "volume": 4681,
      "datetime": 1736268720000
    },
    {
      "open": 22.85,
      "high": 22.85,
      "low": 22.845,
      "close": 22.845,
      "volume": 1950,
      "datetime": 1736268780000
    },
    {
      "open": 22.85,
      "high": 22.85,
      "low": 22.85,
      "close": 22.85,
      "volume": 775,
      "datetime": 1736268840000
    },
    {
      "open": 22.84,
      "high": 22.84,
      "low": 22.84,
      "close": 22.84,
      "volume": 220,
      "datetime": 1736268900000
    },
    {
      "open": 22.8431,
      "high": 22.8498,
      "low": 22.835,
      "close": 22.8498,
      "volume": 3758,
      "datetime": 1736268960000
    },
    {
      "open": 22.85,
      "high": 22.855,
      "low": 22.85,
      "close": 22.85,
      "volume": 1517,
      "datetime": 1736269020000
    },
    {
      "open": 22.8481,
      "high": 22.86,
      "low": 22.845,
      "close": 22.85,
      "volume": 3399,
      "datetime": 1736269080000
    },
    {
      "open": 22.86,
      "high": 22.8601,
      "low": 22.86,
      "close": 22.86,
      "volume": 525,
      "datetime": 1736269140000
    },
    {
      "open": 22.85,
      "high": 22.86,
      "low": 22.85,
      "close": 22.86,
      "volume": 600,
      "datetime": 1736269200000
    },
    {
      "open": 22.86,
      "high": 22.86,
      "low": 22.86,
      "close": 22.86,
      "volume": 150,
      "datetime": 1736269260000
    },
    {
      "open": 22.87,
      "high": 22.87,
      "low": 22.8512,
      "close": 22.8512,
      "volume": 1075,
      "datetime": 1736269320000
    },
    {
      "open": 22.8571,
      "high": 22.8594,
      "low": 22.8571,
      "close": 22.8594,
      "volume": 1100,
      "datetime": 1736269380000
    },
    {
      "open": 22.88,
      "high": 22.89,
      "low": 22.88,
      "close": 22.89,
      "volume": 1371,
      "datetime": 1736269440000
    },
    {
      "open": 22.88,
      "high": 22.895,
      "low": 22.88,
      "close": 22.89,
      "volume": 600,
      "datetime": 1736269500000
    },
    {
      "open": 22.885,
      "high": 22.895,
      "low": 22.885,
      "close": 22.894,
      "volume": 400,
      "datetime": 1736269560000
    },
    {
      "open": 22.905,
      "high": 22.92,
      "low": 22.905,
      "close": 22.92,
      "volume": 332,
      "datetime": 1736269620000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.915,
      "close": 22.915,
      "volume": 974,
      "datetime": 1736269680000
    },
    {
      "open": 22.91,
      "high": 22.9267,
      "low": 22.905,
      "close": 22.9267,
      "volume": 10566,
      "datetime": 1736269740000
    },
    {
      "open": 22.935,
      "high": 22.95,
      "low": 22.92,
      "close": 22.95,
      "volume": 2475,
      "datetime": 1736269800000
    },
    {
      "open": 22.9301,
      "high": 22.9301,
      "low": 22.92,
      "close": 22.92,
      "volume": 3450,
      "datetime": 1736269860000
    },
    {
      "open": 22.91,
      "high": 22.91,
      "low": 22.8932,
      "close": 22.895,
      "volume": 1764,
      "datetime": 1736269920000
    },
    {
      "open": 22.9,
      "high": 22.91,
      "low": 22.9,
      "close": 22.91,
      "volume": 1329,
      "datetime": 1736269980000
    },
    {
      "open": 22.93,
      "high": 22.95,
      "low": 22.93,
      "close": 22.9457,
      "volume": 1537,
      "datetime": 1736270100000
    },
    {
      "open": 22.9499,
      "high": 22.96,
      "low": 22.949,
      "close": 22.95,
      "volume": 3703,
      "datetime": 1736270160000
    },
    {
      "open": 22.95,
      "high": 22.96,
      "low": 22.93,
      "close": 22.93,
      "volume": 5247,
      "datetime": 1736270220000
    },
    {
      "open": 22.9126,
      "high": 22.93,
      "low": 22.9126,
      "close": 22.92,
      "volume": 9582,
      "datetime": 1736270280000
    },
    {
      "open": 22.9,
      "high": 22.915,
      "low": 22.89,
      "close": 22.915,
      "volume": 2844,
      "datetime": 1736270340000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 775,
      "datetime": 1736270460000
    },
    {
      "open": 22.93,
      "high": 22.95,
      "low": 22.93,
      "close": 22.9427,
      "volume": 1984,
      "datetime": 1736270520000
    },
    {
      "open": 22.955,
      "high": 22.9628,
      "low": 22.95,
      "close": 22.95,
      "volume": 7011,
      "datetime": 1736270580000
    },
    {
      "open": 22.94,
      "high": 22.9468,
      "low": 22.94,
      "close": 22.9468,
      "volume": 1093,
      "datetime": 1736270640000
    },
    {
      "open": 22.94,
      "high": 22.95,
      "low": 22.94,
      "close": 22.95,
      "volume": 620,
      "datetime": 1736270700000
    },
    {
      "open": 22.95,
      "high": 22.96,
      "low": 22.95,
      "close": 22.96,
      "volume": 5930,
      "datetime": 1736270760000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.96,
      "close": 22.96,
      "volume": 5966,
      "datetime": 1736270820000
    },
    {
      "open": 22.955,
      "high": 22.975,
      "low": 22.955,
      "close": 22.975,
      "volume": 2100,
      "datetime": 1736270880000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.9509,
      "close": 22.9583,
      "volume": 1850,
      "datetime": 1736270940000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.9388,
      "close": 22.9571,
      "volume": 5115,
      "datetime": 1736271000000
    },
    {
      "open": 22.95,
      "high": 22.969,
      "low": 22.95,
      "close": 22.969,
      "volume": 775,
      "datetime": 1736271060000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.945,
      "close": 22.96,
      "volume": 850,
      "datetime": 1736271120000
    },
    {
      "open": 22.9699,
      "high": 22.98,
      "low": 22.9699,
      "close": 22.97,
      "volume": 2906,
      "datetime": 1736271180000
    },
    {
      "open": 22.97,
      "high": 22.98,
      "low": 22.97,
      "close": 22.98,
      "volume": 1550,
      "datetime": 1736271240000
    },
    {
      "open": 22.98,
      "high": 22.995,
      "low": 22.98,
      "close": 22.989,
      "volume": 2224,
      "datetime": 1736271300000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.975,
      "close": 22.98,
      "volume": 1050,
      "datetime": 1736271360000
    },
    {
      "open": 22.975,
      "high": 23,
      "low": 22.975,
      "close": 22.9999,
      "volume": 5613,
      "datetime": 1736271420000
    },
    {
      "open": 23,
      "high": 23.05,
      "low": 23,
      "close": 23.005,
      "volume": 14228,
      "datetime": 1736271480000
    },
    {
      "open": 23,
      "high": 23,
      "low": 22.96,
      "close": 22.96,
      "volume": 1755,
      "datetime": 1736271540000
    },
    {
      "open": 22.93,
      "high": 22.93,
      "low": 22.92,
      "close": 22.92,
      "volume": 1230,
      "datetime": 1736271600000
    },
    {
      "open": 22.9401,
      "high": 22.9401,
      "low": 22.925,
      "close": 22.925,
      "volume": 2962,
      "datetime": 1736271660000
    },
    {
      "open": 22.925,
      "high": 22.94,
      "low": 22.925,
      "close": 22.94,
      "volume": 2125,
      "datetime": 1736271720000
    },
    {
      "open": 22.955,
      "high": 22.96,
      "low": 22.955,
      "close": 22.9599,
      "volume": 3050,
      "datetime": 1736271780000
    },
    {
      "open": 22.9722,
      "high": 22.9722,
      "low": 22.9722,
      "close": 22.9722,
      "volume": 2000,
      "datetime": 1736271900000
    },
    {
      "open": 22.96,
      "high": 23.04,
      "low": 22.96,
      "close": 23.04,
      "volume": 3815,
      "datetime": 1736271960000
    },
    {
      "open": 23.02,
      "high": 23.0213,
      "low": 23.0149,
      "close": 23.0149,
      "volume": 653,
      "datetime": 1736272020000
    },
    {
      "open": 23.05,
      "high": 23.1,
      "low": 23.04,
      "close": 23.04,
      "volume": 31498,
      "datetime": 1736272080000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.02,
      "close": 23.03,
      "volume": 2263,
      "datetime": 1736272140000
    },
    {
      "open": 23.03,
      "high": 23.045,
      "low": 23.02,
      "close": 23.02,
      "volume": 11052,
      "datetime": 1736272200000
    },
    {
      "open": 23.01,
      "high": 23.04,
      "low": 23,
      "close": 23.04,
      "volume": 1150,
      "datetime": 1736272260000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 100,
      "datetime": 1736272320000
    },
    {
      "open": 23.0212,
      "high": 23.04,
      "low": 23.02,
      "close": 23.03,
      "volume": 1525,
      "datetime": 1736272380000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 22.98,
      "close": 22.98,
      "volume": 1098,
      "datetime": 1736272440000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.9795,
      "close": 22.98,
      "volume": 1272,
      "datetime": 1736272500000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.95,
      "close": 22.95,
      "volume": 25400,
      "datetime": 1736272560000
    },
    {
      "open": 22.95,
      "high": 22.96,
      "low": 22.95,
      "close": 22.96,
      "volume": 2725,
      "datetime": 1736272620000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.951,
      "close": 22.96,
      "volume": 825,
      "datetime": 1736272680000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 725,
      "datetime": 1736272740000
    },
    {
      "open": 22.96,
      "high": 22.97,
      "low": 22.95,
      "close": 22.95,
      "volume": 2291,
      "datetime": 1736272800000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 100,
      "datetime": 1736272860000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.935,
      "close": 22.945,
      "volume": 973,
      "datetime": 1736272920000
    },
    {
      "open": 22.911,
      "high": 22.911,
      "low": 22.91,
      "close": 22.9101,
      "volume": 2280,
      "datetime": 1736273040000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 275,
      "datetime": 1736273100000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.915,
      "close": 22.915,
      "volume": 3695,
      "datetime": 1736273160000
    },
    {
      "open": 22.93,
      "high": 22.95,
      "low": 22.93,
      "close": 22.945,
      "volume": 2808,
      "datetime": 1736273220000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.9147,
      "close": 22.9147,
      "volume": 1394,
      "datetime": 1736273340000
    },
    {
      "open": 22.91,
      "high": 22.92,
      "low": 22.91,
      "close": 22.92,
      "volume": 2818,
      "datetime": 1736273400000
    },
    {
      "open": 22.91,
      "high": 22.92,
      "low": 22.91,
      "close": 22.92,
      "volume": 3250,
      "datetime": 1736273460000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.915,
      "close": 22.915,
      "volume": 300,
      "datetime": 1736273520000
    },
    {
      "open": 22.93,
      "high": 22.933,
      "low": 22.9297,
      "close": 22.933,
      "volume": 2350,
      "datetime": 1736273580000
    },
    {
      "open": 22.94,
      "high": 22.94,
      "low": 22.93,
      "close": 22.93,
      "volume": 900,
      "datetime": 1736273640000
    },
    {
      "open": 22.93,
      "high": 22.94,
      "low": 22.93,
      "close": 22.94,
      "volume": 425,
      "datetime": 1736273700000
    },
    {
      "open": 22.9635,
      "high": 22.97,
      "low": 22.955,
      "close": 22.97,
      "volume": 10534,
      "datetime": 1736273760000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.96,
      "close": 22.96,
      "volume": 200,
      "datetime": 1736273820000
    },
    {
      "open": 22.96,
      "high": 22.9614,
      "low": 22.96,
      "close": 22.9614,
      "volume": 3475,
      "datetime": 1736273880000
    },
    {
      "open": 22.9399,
      "high": 22.94,
      "low": 22.9399,
      "close": 22.94,
      "volume": 725,
      "datetime": 1736273940000
    },
    {
      "open": 22.94,
      "high": 22.95,
      "low": 22.94,
      "close": 22.95,
      "volume": 600,
      "datetime": 1736274000000
    },
    {
      "open": 22.965,
      "high": 23,
      "low": 22.965,
      "close": 23,
      "volume": 1390,
      "datetime": 1736274060000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.96,
      "close": 22.96,
      "volume": 1057,
      "datetime": 1736274120000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 131,
      "datetime": 1736274180000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.95,
      "close": 22.96,
      "volume": 1175,
      "datetime": 1736274240000
    },
    {
      "open": 22.97,
      "high": 22.99,
      "low": 22.97,
      "close": 22.9832,
      "volume": 400,
      "datetime": 1736274300000
    },
    {
      "open": 22.975,
      "high": 22.99,
      "low": 22.975,
      "close": 22.98,
      "volume": 949,
      "datetime": 1736274360000
    },
    {
      "open": 22.98,
      "high": 22.99,
      "low": 22.98,
      "close": 22.98,
      "volume": 1562,
      "datetime": 1736274420000
    },
    {
      "open": 22.99,
      "high": 23.01,
      "low": 22.99,
      "close": 23.005,
      "volume": 1303,
      "datetime": 1736274480000
    },
    {
      "open": 23.005,
      "high": 23.019,
      "low": 23.0032,
      "close": 23.019,
      "volume": 2705,
      "datetime": 1736274540000
    },
    {
      "open": 23,
      "high": 23.02,
      "low": 22.995,
      "close": 23.01,
      "volume": 2196,
      "datetime": 1736274600000
    },
    {
      "open": 23.03,
      "high": 23.0323,
      "low": 23.03,
      "close": 23.0323,
      "volume": 853,
      "datetime": 1736274660000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.0272,
      "close": 23.0272,
      "volume": 1800,
      "datetime": 1736274720000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 23.02,
      "close": 23.02,
      "volume": 150,
      "datetime": 1736274780000
    },
    {
      "open": 23.016,
      "high": 23.016,
      "low": 23,
      "close": 23,
      "volume": 2993,
      "datetime": 1736274840000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 23.015,
      "close": 23.015,
      "volume": 1280,
      "datetime": 1736274900000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 550,
      "datetime": 1736274960000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 1153,
      "datetime": 1736275020000
    },
    {
      "open": 23.055,
      "high": 23.055,
      "low": 23.03,
      "close": 23.045,
      "volume": 4114,
      "datetime": 1736275080000
    },
    {
      "open": 23.055,
      "high": 23.055,
      "low": 23.05,
      "close": 23.05,
      "volume": 445,
      "datetime": 1736275140000
    },
    {
      "open": 23.04,
      "high": 23.05,
      "low": 23.04,
      "close": 23.05,
      "volume": 1550,
      "datetime": 1736275200000
    },
    {
      "open": 23.05,
      "high": 23.07,
      "low": 23.05,
      "close": 23.065,
      "volume": 21663,
      "datetime": 1736275260000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.0401,
      "close": 23.0401,
      "volume": 4675,
      "datetime": 1736275320000
    },
    {
      "open": 23.06,
      "high": 23.07,
      "low": 23.06,
      "close": 23.0699,
      "volume": 2128,
      "datetime": 1736275380000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 100,
      "datetime": 1736275440000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.055,
      "close": 23.055,
      "volume": 5600,
      "datetime": 1736275500000
    },
    {
      "open": 23.0596,
      "high": 23.07,
      "low": 23.0596,
      "close": 23.07,
      "volume": 2634,
      "datetime": 1736275560000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.08,
      "close": 23.08,
      "volume": 275,
      "datetime": 1736275620000
    },
    {
      "open": 23.07,
      "high": 23.09,
      "low": 23.07,
      "close": 23.09,
      "volume": 698,
      "datetime": 1736275680000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 8777,
      "datetime": 1736275740000
    },
    {
      "open": 23.0903,
      "high": 23.1,
      "low": 23.08,
      "close": 23.08,
      "volume": 1789,
      "datetime": 1736275800000
    },
    {
      "open": 23.0905,
      "high": 23.0905,
      "low": 23.08,
      "close": 23.08,
      "volume": 1800,
      "datetime": 1736275860000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.04,
      "close": 23.04,
      "volume": 2583,
      "datetime": 1736275920000
    },
    {
      "open": 23.04,
      "high": 23.0501,
      "low": 23.04,
      "close": 23.0501,
      "volume": 1955,
      "datetime": 1736275980000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 1350,
      "datetime": 1736276040000
    },
    {
      "open": 23.065,
      "high": 23.065,
      "low": 23.06,
      "close": 23.061,
      "volume": 9452,
      "datetime": 1736276100000
    },
    {
      "open": 23.0607,
      "high": 23.105,
      "low": 23.0607,
      "close": 23.1,
      "volume": 2425,
      "datetime": 1736276160000
    },
    {
      "open": 23.095,
      "high": 23.095,
      "low": 23.08,
      "close": 23.08,
      "volume": 3437,
      "datetime": 1736276220000
    },
    {
      "open": 23.08,
      "high": 23.085,
      "low": 23.075,
      "close": 23.085,
      "volume": 3500,
      "datetime": 1736276280000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.07,
      "close": 23.08,
      "volume": 3597,
      "datetime": 1736276340000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.06,
      "close": 23.06,
      "volume": 3287,
      "datetime": 1736276400000
    },
    {
      "open": 23.075,
      "high": 23.075,
      "low": 23.07,
      "close": 23.07,
      "volume": 1200,
      "datetime": 1736276460000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.02,
      "close": 23.02,
      "volume": 8825,
      "datetime": 1736276520000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 225,
      "datetime": 1736276580000
    },
    {
      "open": 23.065,
      "high": 23.07,
      "low": 23.065,
      "close": 23.07,
      "volume": 350,
      "datetime": 1736276640000
    },
    {
      "open": 23.075,
      "high": 23.09,
      "low": 23.075,
      "close": 23.08,
      "volume": 1975,
      "datetime": 1736276700000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.08,
      "close": 23.08,
      "volume": 900,
      "datetime": 1736276760000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.0301,
      "close": 23.0301,
      "volume": 4509,
      "datetime": 1736276820000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.04,
      "close": 23.04,
      "volume": 2800,
      "datetime": 1736276880000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 22.995,
      "close": 23,
      "volume": 6544,
      "datetime": 1736277000000
    },
    {
      "open": 23.005,
      "high": 23.005,
      "low": 23,
      "close": 23.005,
      "volume": 10900,
      "datetime": 1736277060000
    },
    {
      "open": 23.0013,
      "high": 23.005,
      "low": 23.0013,
      "close": 23.005,
      "volume": 200,
      "datetime": 1736277120000
    },
    {
      "open": 23,
      "high": 23,
      "low": 22.995,
      "close": 22.995,
      "volume": 1338,
      "datetime": 1736277180000
    },
    {
      "open": 22.99,
      "high": 23,
      "low": 22.99,
      "close": 22.9901,
      "volume": 1625,
      "datetime": 1736277240000
    },
    {
      "open": 23,
      "high": 23.0001,
      "low": 23,
      "close": 23,
      "volume": 1679,
      "datetime": 1736277300000
    },
    {
      "open": 22.9973,
      "high": 23.02,
      "low": 22.9973,
      "close": 23.02,
      "volume": 2303,
      "datetime": 1736277360000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 250,
      "datetime": 1736277420000
    },
    {
      "open": 23.0232,
      "high": 23.0232,
      "low": 23.02,
      "close": 23.02,
      "volume": 550,
      "datetime": 1736277480000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 23.005,
      "close": 23.005,
      "volume": 500,
      "datetime": 1736277540000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 300,
      "datetime": 1736277600000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.04,
      "close": 23.05,
      "volume": 864,
      "datetime": 1736277660000
    },
    {
      "open": 23.05,
      "high": 23.06,
      "low": 23.05,
      "close": 23.05,
      "volume": 30659,
      "datetime": 1736277720000
    },
    {
      "open": 23.06,
      "high": 23.07,
      "low": 23.06,
      "close": 23.07,
      "volume": 1125,
      "datetime": 1736277780000
    },
    {
      "open": 23.075,
      "high": 23.08,
      "low": 23.072,
      "close": 23.08,
      "volume": 1400,
      "datetime": 1736277840000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.08,
      "close": 23.08,
      "volume": 925,
      "datetime": 1736277900000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.07,
      "close": 23.07,
      "volume": 1100,
      "datetime": 1736277960000
    },
    {
      "open": 23.08,
      "high": 23.09,
      "low": 23.08,
      "close": 23.08,
      "volume": 650,
      "datetime": 1736278020000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.06,
      "close": 23.06,
      "volume": 1295,
      "datetime": 1736278140000
    },
    {
      "open": 23.06,
      "high": 23.08,
      "low": 23.06,
      "close": 23.08,
      "volume": 2152,
      "datetime": 1736278200000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 310,
      "datetime": 1736278260000
    },
    {
      "open": 23.0953,
      "high": 23.0998,
      "low": 23.0953,
      "close": 23.0998,
      "volume": 800,
      "datetime": 1736278320000
    },
    {
      "open": 23.08,
      "high": 23.085,
      "low": 23.08,
      "close": 23.08,
      "volume": 700,
      "datetime": 1736278380000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.08,
      "close": 23.08,
      "volume": 650,
      "datetime": 1736278440000
    },
    {
      "open": 23.0714,
      "high": 23.09,
      "low": 23.0714,
      "close": 23.09,
      "volume": 975,
      "datetime": 1736278500000
    },
    {
      "open": 23.0899,
      "high": 23.11,
      "low": 23.0899,
      "close": 23.11,
      "volume": 3950,
      "datetime": 1736278560000
    },
    {
      "open": 23.11,
      "high": 23.132,
      "low": 23.11,
      "close": 23.13,
      "volume": 12625,
      "datetime": 1736278620000
    },
    {
      "open": 23.128,
      "high": 23.13,
      "low": 23.12,
      "close": 23.13,
      "volume": 1935,
      "datetime": 1736278680000
    },
    {
      "open": 23.13,
      "high": 23.135,
      "low": 23.13,
      "close": 23.135,
      "volume": 5180,
      "datetime": 1736278740000
    },
    {
      "open": 23.1301,
      "high": 23.18,
      "low": 23.12,
      "close": 23.14,
      "volume": 6682,
      "datetime": 1736278800000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.114,
      "close": 23.12,
      "volume": 2180,
      "datetime": 1736278860000
    },
    {
      "open": 23.1222,
      "high": 23.165,
      "low": 23.1222,
      "close": 23.155,
      "volume": 4635,
      "datetime": 1736278920000
    },
    {
      "open": 23.125,
      "high": 23.13,
      "low": 23.11,
      "close": 23.11,
      "volume": 7633,
      "datetime": 1736278980000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.09,
      "close": 23.09,
      "volume": 575,
      "datetime": 1736279040000
    },
    {
      "open": 23.095,
      "high": 23.1,
      "low": 23.07,
      "close": 23.07,
      "volume": 1125,
      "datetime": 1736279100000
    },
    {
      "open": 23.085,
      "high": 23.09,
      "low": 23.085,
      "close": 23.0858,
      "volume": 3091,
      "datetime": 1736279160000
    },
    {
      "open": 23.09,
      "high": 23.12,
      "low": 23.09,
      "close": 23.12,
      "volume": 2925,
      "datetime": 1736279220000
    },
    {
      "open": 23.13,
      "high": 23.14,
      "low": 23.13,
      "close": 23.14,
      "volume": 1500,
      "datetime": 1736279280000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.15,
      "close": 23.16,
      "volume": 1150,
      "datetime": 1736279340000
    },
    {
      "open": 23.15,
      "high": 23.1501,
      "low": 23.13,
      "close": 23.14,
      "volume": 2109,
      "datetime": 1736279400000
    },
    {
      "open": 23.14,
      "high": 23.16,
      "low": 23.14,
      "close": 23.16,
      "volume": 825,
      "datetime": 1736279460000
    },
    {
      "open": 23.1632,
      "high": 23.1632,
      "low": 23.16,
      "close": 23.16,
      "volume": 1247,
      "datetime": 1736279520000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.13,
      "close": 23.1301,
      "volume": 749,
      "datetime": 1736279580000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 3800,
      "datetime": 1736279640000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.14,
      "close": 23.14,
      "volume": 1275,
      "datetime": 1736279700000
    },
    {
      "open": 23.14,
      "high": 23.1401,
      "low": 23.14,
      "close": 23.1401,
      "volume": 650,
      "datetime": 1736279760000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.12,
      "close": 23.12,
      "volume": 300,
      "datetime": 1736279820000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 1190,
      "datetime": 1736279880000
    },
    {
      "open": 23.1432,
      "high": 23.1432,
      "low": 23.14,
      "close": 23.1401,
      "volume": 928,
      "datetime": 1736279940000
    },
    {
      "open": 23.15,
      "high": 23.17,
      "low": 23.145,
      "close": 23.17,
      "volume": 2141,
      "datetime": 1736280000000
    },
    {
      "open": 23.17,
      "high": 23.1766,
      "low": 23.165,
      "close": 23.17,
      "volume": 8218,
      "datetime": 1736280060000
    },
    {
      "open": 23.17,
      "high": 23.1701,
      "low": 23.16,
      "close": 23.16,
      "volume": 2531,
      "datetime": 1736280120000
    },
    {
      "open": 23.18,
      "high": 23.18,
      "low": 23.17,
      "close": 23.17,
      "volume": 1191,
      "datetime": 1736280180000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.14,
      "close": 23.14,
      "volume": 1600,
      "datetime": 1736280240000
    },
    {
      "open": 23.1233,
      "high": 23.1332,
      "low": 23.12,
      "close": 23.13,
      "volume": 851,
      "datetime": 1736280300000
    },
    {
      "open": 23.12,
      "high": 23.1201,
      "low": 23.1,
      "close": 23.1,
      "volume": 3454,
      "datetime": 1736280360000
    },
    {
      "open": 23.095,
      "high": 23.11,
      "low": 23.095,
      "close": 23.11,
      "volume": 4064,
      "datetime": 1736280420000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 250,
      "datetime": 1736280480000
    },
    {
      "open": 23.1086,
      "high": 23.15,
      "low": 23.105,
      "close": 23.15,
      "volume": 1575,
      "datetime": 1736280540000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 400,
      "datetime": 1736280600000
    },
    {
      "open": 23.1808,
      "high": 23.19,
      "low": 23.18,
      "close": 23.18,
      "volume": 8530,
      "datetime": 1736280660000
    },
    {
      "open": 23.175,
      "high": 23.175,
      "low": 23.17,
      "close": 23.17,
      "volume": 1326,
      "datetime": 1736280720000
    },
    {
      "open": 23.1683,
      "high": 23.17,
      "low": 23.16,
      "close": 23.1683,
      "volume": 5392,
      "datetime": 1736280780000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.16,
      "close": 23.16,
      "volume": 600,
      "datetime": 1736280840000
    },
    {
      "open": 23.1407,
      "high": 23.15,
      "low": 23.1301,
      "close": 23.135,
      "volume": 3346,
      "datetime": 1736280900000
    },
    {
      "open": 23.145,
      "high": 23.16,
      "low": 23.145,
      "close": 23.16,
      "volume": 2920,
      "datetime": 1736280960000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.16,
      "close": 23.16,
      "volume": 650,
      "datetime": 1736281020000
    },
    {
      "open": 23.1801,
      "high": 23.185,
      "low": 23.18,
      "close": 23.185,
      "volume": 2369,
      "datetime": 1736281080000
    },
    {
      "open": 23.185,
      "high": 23.185,
      "low": 23.1688,
      "close": 23.1688,
      "volume": 5697,
      "datetime": 1736281140000
    },
    {
      "open": 23.165,
      "high": 23.185,
      "low": 23.165,
      "close": 23.185,
      "volume": 1800,
      "datetime": 1736281200000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 137,
      "datetime": 1736281260000
    },
    {
      "open": 23.195,
      "high": 23.2163,
      "low": 23.195,
      "close": 23.2003,
      "volume": 33142,
      "datetime": 1736281320000
    },
    {
      "open": 23.18,
      "high": 23.195,
      "low": 23.18,
      "close": 23.19,
      "volume": 2789,
      "datetime": 1736281380000
    },
    {
      "open": 23.21,
      "high": 23.21,
      "low": 23.21,
      "close": 23.21,
      "volume": 350,
      "datetime": 1736281440000
    },
    {
      "open": 23.2,
      "high": 23.205,
      "low": 23.19,
      "close": 23.2,
      "volume": 3400,
      "datetime": 1736281500000
    },
    {
      "open": 23.2001,
      "high": 23.21,
      "low": 23.2,
      "close": 23.2,
      "volume": 8539,
      "datetime": 1736281560000
    },
    {
      "open": 23.19,
      "high": 23.2,
      "low": 23.18,
      "close": 23.18,
      "volume": 3325,
      "datetime": 1736281620000
    },
    {
      "open": 23.18,
      "high": 23.1981,
      "low": 23.18,
      "close": 23.1981,
      "volume": 900,
      "datetime": 1736281680000
    },
    {
      "open": 23.195,
      "high": 23.195,
      "low": 23.195,
      "close": 23.195,
      "volume": 830,
      "datetime": 1736281740000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.17,
      "close": 23.17,
      "volume": 1275,
      "datetime": 1736281800000
    },
    {
      "open": 23.167,
      "high": 23.167,
      "low": 23.15,
      "close": 23.1515,
      "volume": 12200,
      "datetime": 1736281860000
    },
    {
      "open": 23.155,
      "high": 23.17,
      "low": 23.155,
      "close": 23.17,
      "volume": 1050,
      "datetime": 1736281920000
    },
    {
      "open": 23.145,
      "high": 23.17,
      "low": 23.145,
      "close": 23.17,
      "volume": 1720,
      "datetime": 1736281980000
    },
    {
      "open": 23.17,
      "high": 23.17,
      "low": 23.17,
      "close": 23.17,
      "volume": 1050,
      "datetime": 1736282040000
    },
    {
      "open": 23.17,
      "high": 23.21,
      "low": 23.16,
      "close": 23.21,
      "volume": 3351,
      "datetime": 1736282100000
    },
    {
      "open": 23.2001,
      "high": 23.2063,
      "low": 23.1901,
      "close": 23.2063,
      "volume": 1900,
      "datetime": 1736282160000
    },
    {
      "open": 23.2,
      "high": 23.2,
      "low": 23.195,
      "close": 23.195,
      "volume": 2845,
      "datetime": 1736282220000
    },
    {
      "open": 23.185,
      "high": 23.1963,
      "low": 23.175,
      "close": 23.181,
      "volume": 2273,
      "datetime": 1736282280000
    },
    {
      "open": 23.18,
      "high": 23.18,
      "low": 23.13,
      "close": 23.13,
      "volume": 2695,
      "datetime": 1736282340000
    },
    {
      "open": 23.125,
      "high": 23.135,
      "low": 23.115,
      "close": 23.12,
      "volume": 7556,
      "datetime": 1736282400000
    },
    {
      "open": 23.125,
      "high": 23.125,
      "low": 23.11,
      "close": 23.12,
      "volume": 9445,
      "datetime": 1736282460000
    },
    {
      "open": 23.13,
      "high": 23.145,
      "low": 23.13,
      "close": 23.145,
      "volume": 1075,
      "datetime": 1736282520000
    },
    {
      "open": 23.1514,
      "high": 23.16,
      "low": 23.145,
      "close": 23.155,
      "volume": 1800,
      "datetime": 1736282580000
    },
    {
      "open": 23.165,
      "high": 23.195,
      "low": 23.165,
      "close": 23.195,
      "volume": 3945,
      "datetime": 1736282640000
    },
    {
      "open": 23.1971,
      "high": 23.1971,
      "low": 23.185,
      "close": 23.1963,
      "volume": 3061,
      "datetime": 1736282700000
    },
    {
      "open": 23.2,
      "high": 23.2,
      "low": 23.16,
      "close": 23.16,
      "volume": 1600,
      "datetime": 1736282760000
    },
    {
      "open": 23.18,
      "high": 23.18,
      "low": 23.17,
      "close": 23.17,
      "volume": 900,
      "datetime": 1736282820000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.13,
      "close": 23.13,
      "volume": 11816,
      "datetime": 1736282880000
    },
    {
      "open": 23.12,
      "high": 23.14,
      "low": 23.12,
      "close": 23.14,
      "volume": 641,
      "datetime": 1736282940000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.11,
      "close": 23.11,
      "volume": 2907,
      "datetime": 1736283000000
    },
    {
      "open": 23.12,
      "high": 23.13,
      "low": 23.095,
      "close": 23.1,
      "volume": 5135,
      "datetime": 1736283060000
    },
    {
      "open": 23.11,
      "high": 23.135,
      "low": 23.11,
      "close": 23.1299,
      "volume": 6357,
      "datetime": 1736283120000
    },
    {
      "open": 23.115,
      "high": 23.115,
      "low": 23.1001,
      "close": 23.1001,
      "volume": 4523,
      "datetime": 1736283180000
    },
    {
      "open": 23.08,
      "high": 23.1,
      "low": 23.08,
      "close": 23.095,
      "volume": 3515,
      "datetime": 1736283240000
    },
    {
      "open": 23.07,
      "high": 23.0899,
      "low": 23.06,
      "close": 23.0899,
      "volume": 7373,
      "datetime": 1736283300000
    },
    {
      "open": 23.09,
      "high": 23.1,
      "low": 23.09,
      "close": 23.1,
      "volume": 6146,
      "datetime": 1736283360000
    },
    {
      "open": 23.1,
      "high": 23.12,
      "low": 23.1,
      "close": 23.12,
      "volume": 11859,
      "datetime": 1736283420000
    },
    {
      "open": 23.125,
      "high": 23.14,
      "low": 23.105,
      "close": 23.14,
      "volume": 56861,
      "datetime": 1736283480000
    },
    {
      "open": 23.14,
      "high": 23.17,
      "low": 23.11,
      "close": 23.14,
      "volume": 174114,
      "datetime": 1736283540000
    },
    {
      "open": 23.13,
      "high": 23.1581,
      "low": 23.13,
      "close": 23.1581,
      "volume": 1313,
      "datetime": 1736283600000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 150,
      "datetime": 1736283780000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 3291,
      "datetime": 1736284320000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 2000,
      "datetime": 1736284680000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 100,
      "datetime": 1736284740000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 150,
      "datetime": 1736284920000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 1000,
      "datetime": 1736285040000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 199,
      "datetime": 1736285100000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 7889,
      "datetime": 1736285520000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 1500,
      "datetime": 1736285580000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 100,
      "datetime": 1736285700000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 1500,
      "datetime": 1736285820000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.11,
      "close": 23.11,
      "volume": 1248,
      "datetime": 1736285880000
    },
    {
      "open": 23.11,
      "high": 23.13,
      "low": 23.11,
      "close": 23.13,
      "volume": 9988,
      "datetime": 1736286000000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.11,
      "close": 23.11,
      "volume": 100,
      "datetime": 1736286180000
    },
    {
      "open": 23.11,
      "high": 23.1101,
      "low": 23.11,
      "close": 23.1101,
      "volume": 1500,
      "datetime": 1736286360000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 200,
      "datetime": 1736286840000
    },
    {
      "open": 23.06,
      "high": 23.1,
      "low": 23.06,
      "close": 23.1,
      "volume": 326,
      "datetime": 1736286900000
    },
    {
      "open": 23.14,
      "high": 23.15,
      "low": 23.14,
      "close": 23.15,
      "volume": 6920,
      "datetime": 1736287620000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 1500,
      "datetime": 1736287680000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 100,
      "datetime": 1736288580000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 100,
      "datetime": 1736289600000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 1450,
      "datetime": 1736289780000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 100,
      "datetime": 1736290560000
    },
    {
      "open": 22.95,
      "high": 23,
      "low": 22.95,
      "close": 23,
      "volume": 389,
      "datetime": 1736290800000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.07,
      "close": 23.07,
      "volume": 100,
      "datetime": 1736291520000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.08,
      "close": 23.08,
      "volume": 275,
      "datetime": 1736291640000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 100,
      "datetime": 1736292060000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 150,
      "datetime": 1736292600000
    },
    {
      "open": 23.0587,
      "high": 23.0587,
      "low": 23.0587,
      "close": 23.0587,
      "volume": 150,
      "datetime": 1736292900000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.98,
      "close": 22.98,
      "volume": 700,
      "datetime": 1736293080000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.97,
      "close": 22.97,
      "volume": 650,
      "datetime": 1736293260000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 100,
      "datetime": 1736293680000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.07,
      "close": 23.07,
      "volume": 500,
      "datetime": 1736294340000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 100,
      "datetime": 1736295600000
    },
    {
      "open": 22.9901,
      "high": 22.9901,
      "low": 22.9901,
      "close": 22.9901,
      "volume": 155,
      "datetime": 1736296020000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.07,
      "close": 23.07,
      "volume": 110,
      "datetime": 1736296320000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 160,
      "datetime": 1736297520000
    },
    {
      "open": 22.9501,
      "high": 22.9501,
      "low": 22.9501,
      "close": 22.9501,
      "volume": 503,
      "datetime": 1736297760000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.97,
      "close": 22.97,
      "volume": 100,
      "datetime": 1736297880000
    },
    {
      "open": 22.9703,
      "high": 22.9703,
      "low": 22.9703,
      "close": 22.9703,
      "volume": 500,
      "datetime": 1736297940000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.97,
      "close": 22.97,
      "volume": 50,
      "datetime": 1736298060000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.08,
      "close": 23.08,
      "volume": 1,
      "datetime": 1736298360000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 90,
      "datetime": 1736298420000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.96,
      "close": 22.96,
      "volume": 25,
      "datetime": 1736298840000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 10,
      "datetime": 1736299200000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 49,
      "datetime": 1736299380000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.97,
      "close": 22.97,
      "volume": 200,
      "datetime": 1736299500000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 40,
      "datetime": 1736299620000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 400,
      "datetime": 1736300220000
    },
    {
      "open": 23.09,
      "high": 23.1,
      "low": 23.09,
      "close": 23.1,
      "volume": 9,
      "datetime": 1736300820000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 398,
      "datetime": 1736300880000
    },
    {
      "open": 23.12,
      "high": 23.13,
      "low": 23.12,
      "close": 23.13,
      "volume": 460,
      "datetime": 1736301060000
    },
    {
      "open": 23.12,
      "high": 23.12,
      "low": 23.12,
      "close": 23.12,
      "volume": 100,
      "datetime": 1736301120000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.11,
      "close": 23.11,
      "volume": 10,
      "datetime": 1736301180000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 100,
      "datetime": 1736302860000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 10,
      "datetime": 1736303700000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 505,
      "datetime": 1736304300000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 211,
      "datetime": 1736305020000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 2,
      "datetime": 1736305260000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 1440,
      "datetime": 1736305500000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 10,
      "datetime": 1736305560000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 118,
      "datetime": 1736305620000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 1,
      "datetime": 1736305680000
    },
    {
      "open": 23.17,
      "high": 23.17,
      "low": 23.17,
      "close": 23.17,
      "volume": 30,
      "datetime": 1736305860000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 10,
      "datetime": 1736306040000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.13,
      "close": 23.13,
      "volume": 5,
      "datetime": 1736306340000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 3,
      "datetime": 1736306640000
    },
    {
      "open": 23.19,
      "high": 23.21,
      "low": 23.19,
      "close": 23.21,
      "volume": 9662,
      "datetime": 1736308080000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 1,
      "datetime": 1736308140000
    },
    {
      "open": 23.17,
      "high": 23.17,
      "low": 23.17,
      "close": 23.17,
      "volume": 5,
      "datetime": 1736308740000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 35,
      "datetime": 1736309040000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 20,
      "datetime": 1736309700000
    },
    {
      "open": 23.18,
      "high": 23.18,
      "low": 23.18,
      "close": 23.18,
      "volume": 100,
      "datetime": 1736309880000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 5,
      "datetime": 1736310060000
    },
    {
      "open": 23.23,
      "high": 23.23,
      "low": 23.23,
      "close": 23.23,
      "volume": 50,
      "datetime": 1736310120000
    },
    {
      "open": 23.22,
      "high": 23.22,
      "low": 23.22,
      "close": 23.22,
      "volume": 100,
      "datetime": 1736310180000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 2,
      "datetime": 1736310600000
    },
    {
      "open": 23.22,
      "high": 23.22,
      "low": 23.22,
      "close": 23.22,
      "volume": 500,
      "datetime": 1736311680000
    },
    {
      "open": 23.21,
      "high": 23.21,
      "low": 23.21,
      "close": 23.21,
      "volume": 4,
      "datetime": 1736311800000
    },
    {
      "open": 23.22,
      "high": 23.22,
      "low": 23.22,
      "close": 23.22,
      "volume": 10,
      "datetime": 1736312220000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 50,
      "datetime": 1736312520000
    },
    {
      "open": 23.24,
      "high": 23.24,
      "low": 23.24,
      "close": 23.24,
      "volume": 100,
      "datetime": 1736312940000
    },
    {
      "open": 23.23,
      "high": 23.23,
      "low": 23.23,
      "close": 23.23,
      "volume": 200,
      "datetime": 1736313120000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 5,
      "datetime": 1736313240000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.13,
      "close": 23.13,
      "volume": 500,
      "datetime": 1736313600000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 4,
      "datetime": 1736314200000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 100,
      "datetime": 1736314320000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 100,
      "datetime": 1736314860000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.27,
      "close": 23.27,
      "volume": 22,
      "datetime": 1736317920000
    },
    {
      "open": 23.3,
      "high": 23.34,
      "low": 23.3,
      "close": 23.31,
      "volume": 114,
      "datetime": 1736317980000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.33,
      "close": 23.33,
      "volume": 400,
      "datetime": 1736318100000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.38,
      "close": 23.38,
      "volume": 1111,
      "datetime": 1736318280000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.33,
      "close": 23.33,
      "volume": 3333,
      "datetime": 1736318520000
    },
    {
      "open": 23.29,
      "high": 23.3,
      "low": 23.29,
      "close": 23.3,
      "volume": 4444,
      "datetime": 1736318580000
    },
    {
      "open": 23.34,
      "high": 23.34,
      "low": 23.34,
      "close": 23.34,
      "volume": 1,
      "datetime": 1736318640000
    },
    {
      "open": 23.28,
      "high": 23.34,
      "low": 23.28,
      "close": 23.34,
      "volume": 2,
      "datetime": 1736318700000
    },
    {
      "open": 23.34,
      "high": 23.34,
      "low": 23.34,
      "close": 23.34,
      "volume": 3333,
      "datetime": 1736318760000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.36,
      "close": 23.36,
      "volume": 50,
      "datetime": 1736318820000
    },
    {
      "open": 23.34,
      "high": 23.34,
      "low": 23.34,
      "close": 23.34,
      "volume": 1,
      "datetime": 1736318880000
    },
    {
      "open": 23.37,
      "high": 23.37,
      "low": 23.37,
      "close": 23.37,
      "volume": 599,
      "datetime": 1736319000000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 1,
      "datetime": 1736319180000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.44,
      "close": 23.44,
      "volume": 401,
      "datetime": 1736319240000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 3335,
      "datetime": 1736319360000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 331,
      "datetime": 1736319420000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 500,
      "datetime": 1736319480000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 1,
      "datetime": 1736319540000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.41,
      "close": 23.41,
      "volume": 661,
      "datetime": 1736319600000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 17,
      "datetime": 1736319780000
    },
    {
      "open": 23.37,
      "high": 23.4,
      "low": 23.37,
      "close": 23.4,
      "volume": 20,
      "datetime": 1736319900000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.33,
      "close": 23.33,
      "volume": 500,
      "datetime": 1736320200000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.35,
      "close": 23.35,
      "volume": 100,
      "datetime": 1736320380000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.36,
      "close": 23.36,
      "volume": 100,
      "datetime": 1736321040000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.37,
      "close": 23.37,
      "volume": 2,
      "datetime": 1736321100000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.38,
      "close": 23.38,
      "volume": 15,
      "datetime": 1736321160000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 836,
      "datetime": 1736321220000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.38,
      "close": 23.38,
      "volume": 4,
      "datetime": 1736321820000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.3,
      "close": 23.3,
      "volume": 155,
      "datetime": 1736322660000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.29,
      "close": 23.29,
      "volume": 200,
      "datetime": 1736322840000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.36,
      "close": 23.36,
      "volume": 1,
      "datetime": 1736323860000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.36,
      "close": 23.36,
      "volume": 3693,
      "datetime": 1736323920000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.27,
      "close": 23.27,
      "volume": 94,
      "datetime": 1736324880000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.27,
      "close": 23.27,
      "volume": 3331,
      "datetime": 1736325120000
    },
    {
      "open": 23.23,
      "high": 23.23,
      "low": 23.23,
      "close": 23.23,
      "volume": 6931,
      "datetime": 1736325360000
    },
    {
      "open": 23.21,
      "high": 23.21,
      "low": 23.21,
      "close": 23.21,
      "volume": 174,
      "datetime": 1736325660000
    },
    {
      "open": 23.32,
      "high": 23.32,
      "low": 23.32,
      "close": 23.32,
      "volume": 200,
      "datetime": 1736328840000
    },
    {
      "open": 23.29,
      "high": 23.29,
      "low": 23.28,
      "close": 23.28,
      "volume": 500,
      "datetime": 1736329020000
    },
    {
      "open": 23.3,
      "high": 23.31,
      "low": 23.3,
      "close": 23.31,
      "volume": 500,
      "datetime": 1736329320000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.3,
      "close": 23.3,
      "volume": 111,
      "datetime": 1736329560000
    },
    {
      "open": 23.31,
      "high": 23.31,
      "low": 23.31,
      "close": 23.31,
      "volume": 245,
      "datetime": 1736329620000
    },
    {
      "open": 23.31,
      "high": 23.31,
      "low": 23.31,
      "close": 23.31,
      "volume": 200,
      "datetime": 1736329740000
    },
    {
      "open": 23.31,
      "high": 23.31,
      "low": 23.3,
      "close": 23.3,
      "volume": 469,
      "datetime": 1736330160000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.36,
      "close": 23.36,
      "volume": 115,
      "datetime": 1736330460000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.35,
      "close": 23.35,
      "volume": 205,
      "datetime": 1736330760000
    },
    {
      "open": 23.35,
      "high": 23.37,
      "low": 23.35,
      "close": 23.37,
      "volume": 3691,
      "datetime": 1736331420000
    },
    {
      "open": 23.29,
      "high": 23.29,
      "low": 23.29,
      "close": 23.29,
      "volume": 400,
      "datetime": 1736332320000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.33,
      "close": 23.33,
      "volume": 3000,
      "datetime": 1736333040000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.27,
      "close": 23.27,
      "volume": 2994,
      "datetime": 1736333700000
    },
    {
      "open": 23.25,
      "high": 23.25,
      "low": 23.25,
      "close": 23.25,
      "volume": 249,
      "datetime": 1736334060000
    },
    {
      "open": 23.25,
      "high": 23.25,
      "low": 23.25,
      "close": 23.25,
      "volume": 227,
      "datetime": 1736334660000
    },
    {
      "open": 23.28,
      "high": 23.28,
      "low": 23.28,
      "close": 23.28,
      "volume": 211,
      "datetime": 1736335080000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 200,
      "datetime": 1736336040000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 250,
      "datetime": 1736336160000
    },
    {
      "open": 23.555,
      "high": 23.555,
      "low": 23.46,
      "close": 23.46,
      "volume": 4360,
      "datetime": 1736336340000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.57,
      "close": 23.57,
      "volume": 100,
      "datetime": 1736336520000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 1526,
      "datetime": 1736336940000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.46,
      "close": 23.46,
      "volume": 1469,
      "datetime": 1736337060000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 500,
      "datetime": 1736337300000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 100,
      "datetime": 1736337720000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 100,
      "datetime": 1736337900000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 238,
      "datetime": 1736337960000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 300,
      "datetime": 1736338080000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 100,
      "datetime": 1736338320000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.44,
      "close": 23.44,
      "volume": 350,
      "datetime": 1736338500000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 100,
      "datetime": 1736338680000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 2233,
      "datetime": 1736338860000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 100,
      "datetime": 1736338920000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.45,
      "close": 23.45,
      "volume": 600,
      "datetime": 1736339220000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.44,
      "close": 23.44,
      "volume": 100,
      "datetime": 1736339280000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 100,
      "datetime": 1736339340000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 500,
      "datetime": 1736339400000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 100,
      "datetime": 1736339460000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 233,
      "datetime": 1736339520000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 400,
      "datetime": 1736339700000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 100,
      "datetime": 1736339820000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 150,
      "datetime": 1736339940000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.52,
      "close": 23.52,
      "volume": 147,
      "datetime": 1736340540000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 171,
      "datetime": 1736340720000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.54,
      "close": 23.54,
      "volume": 100,
      "datetime": 1736340900000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.44,
      "close": 23.44,
      "volume": 544,
      "datetime": 1736341200000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.44,
      "close": 23.44,
      "volume": 250,
      "datetime": 1736341260000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.41,
      "close": 23.41,
      "volume": 28392,
      "datetime": 1736341320000
    },
    {
      "open": 23.4001,
      "high": 23.4001,
      "low": 23.3601,
      "close": 23.3601,
      "volume": 600,
      "datetime": 1736341380000
    },
    {
      "open": 23.3505,
      "high": 23.3505,
      "low": 23.3505,
      "close": 23.3505,
      "volume": 225,
      "datetime": 1736341440000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 250,
      "datetime": 1736341560000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 200,
      "datetime": 1736341620000
    },
    {
      "open": 23.434,
      "high": 23.4399,
      "low": 23.434,
      "close": 23.4399,
      "volume": 600,
      "datetime": 1736341860000
    },
    {
      "open": 23.39,
      "high": 23.39,
      "low": 23.361,
      "close": 23.361,
      "volume": 700,
      "datetime": 1736342160000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 100,
      "datetime": 1736342220000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.4299,
      "close": 23.4299,
      "volume": 600,
      "datetime": 1736342460000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 150,
      "datetime": 1736342520000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.36,
      "close": 23.36,
      "volume": 200,
      "datetime": 1736342640000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.35,
      "close": 23.35,
      "volume": 100,
      "datetime": 1736342700000
    },
    {
      "open": 23.34,
      "high": 23.34,
      "low": 23.3399,
      "close": 23.3399,
      "volume": 700,
      "datetime": 1736342820000
    },
    {
      "open": 23.3399,
      "high": 23.3399,
      "low": 23.3399,
      "close": 23.3399,
      "volume": 350,
      "datetime": 1736342880000
    },
    {
      "open": 23.32,
      "high": 23.34,
      "low": 23.32,
      "close": 23.34,
      "volume": 641,
      "datetime": 1736342940000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.35,
      "close": 23.35,
      "volume": 300,
      "datetime": 1736343000000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.33,
      "close": 23.33,
      "volume": 800,
      "datetime": 1736343060000
    },
    {
      "open": 23.41,
      "high": 23.419,
      "low": 23.41,
      "close": 23.419,
      "volume": 450,
      "datetime": 1736343180000
    },
    {
      "open": 23.42,
      "high": 23.43,
      "low": 23.42,
      "close": 23.43,
      "volume": 231,
      "datetime": 1736343300000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 920,
      "datetime": 1736343360000
    },
    {
      "open": 23.4007,
      "high": 23.4007,
      "low": 23.4007,
      "close": 23.4007,
      "volume": 2000,
      "datetime": 1736343420000
    },
    {
      "open": 23.4386,
      "high": 23.4386,
      "low": 23.401,
      "close": 23.401,
      "volume": 6000,
      "datetime": 1736343480000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 450,
      "datetime": 1736343660000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 150,
      "datetime": 1736343840000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 100,
      "datetime": 1736344080000
    },
    {
      "open": 23.39,
      "high": 23.39,
      "low": 23.39,
      "close": 23.39,
      "volume": 850,
      "datetime": 1736344740000
    },
    {
      "open": 23.3991,
      "high": 23.3991,
      "low": 23.3991,
      "close": 23.3991,
      "volume": 500,
      "datetime": 1736344860000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.37,
      "close": 23.37,
      "volume": 2243,
      "datetime": 1736344920000
    },
    {
      "open": 23.37,
      "high": 23.37,
      "low": 23.37,
      "close": 23.37,
      "volume": 100,
      "datetime": 1736344980000
    },
    {
      "open": 23.3704,
      "high": 23.38,
      "low": 23.3704,
      "close": 23.38,
      "volume": 1260,
      "datetime": 1736345040000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.3499,
      "close": 23.3499,
      "volume": 1100,
      "datetime": 1736345160000
    },
    {
      "open": 23.35,
      "high": 23.3503,
      "low": 23.35,
      "close": 23.3503,
      "volume": 350,
      "datetime": 1736345220000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.4302,
      "close": 23.4302,
      "volume": 757,
      "datetime": 1736345580000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 500,
      "datetime": 1736345700000
    },
    {
      "open": 23.39,
      "high": 23.39,
      "low": 23.39,
      "close": 23.39,
      "volume": 100,
      "datetime": 1736345880000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 200,
      "datetime": 1736345940000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 100,
      "datetime": 1736346060000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 100,
      "datetime": 1736346180000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 1435,
      "datetime": 1736346240000
    },
    {
      "open": 23.39,
      "high": 23.4494,
      "low": 23.38,
      "close": 23.4494,
      "volume": 11534,
      "datetime": 1736346600000
    },
    {
      "open": 23.45,
      "high": 23.4799,
      "low": 23.435,
      "close": 23.435,
      "volume": 4040,
      "datetime": 1736346660000
    },
    {
      "open": 23.4238,
      "high": 23.435,
      "low": 23.42,
      "close": 23.435,
      "volume": 2710,
      "datetime": 1736346720000
    },
    {
      "open": 23.4198,
      "high": 23.4199,
      "low": 23.4,
      "close": 23.405,
      "volume": 6461,
      "datetime": 1736346780000
    },
    {
      "open": 23.405,
      "high": 23.415,
      "low": 23.34,
      "close": 23.34,
      "volume": 15019,
      "datetime": 1736346840000
    },
    {
      "open": 23.3,
      "high": 23.3321,
      "low": 23.3,
      "close": 23.315,
      "volume": 10391,
      "datetime": 1736346900000
    },
    {
      "open": 23.32,
      "high": 23.3734,
      "low": 23.32,
      "close": 23.3734,
      "volume": 4136,
      "datetime": 1736346960000
    },
    {
      "open": 23.36,
      "high": 23.42,
      "low": 23.36,
      "close": 23.42,
      "volume": 5137,
      "datetime": 1736347020000
    },
    {
      "open": 23.395,
      "high": 23.445,
      "low": 23.395,
      "close": 23.4298,
      "volume": 7514,
      "datetime": 1736347080000
    },
    {
      "open": 23.4305,
      "high": 23.45,
      "low": 23.43,
      "close": 23.45,
      "volume": 3300,
      "datetime": 1736347140000
    },
    {
      "open": 23.4602,
      "high": 23.4786,
      "low": 23.46,
      "close": 23.4693,
      "volume": 4400,
      "datetime": 1736347200000
    },
    {
      "open": 23.46,
      "high": 23.48,
      "low": 23.46,
      "close": 23.47,
      "volume": 9423,
      "datetime": 1736347260000
    },
    {
      "open": 23.455,
      "high": 23.455,
      "low": 23.435,
      "close": 23.435,
      "volume": 1230,
      "datetime": 1736347320000
    },
    {
      "open": 23.4699,
      "high": 23.5,
      "low": 23.4567,
      "close": 23.4567,
      "volume": 3950,
      "datetime": 1736347380000
    },
    {
      "open": 23.4335,
      "high": 23.4335,
      "low": 23.4202,
      "close": 23.4202,
      "volume": 2100,
      "datetime": 1736347440000
    },
    {
      "open": 23.38,
      "high": 23.3901,
      "low": 23.37,
      "close": 23.39,
      "volume": 2500,
      "datetime": 1736347500000
    },
    {
      "open": 23.47,
      "high": 23.51,
      "low": 23.47,
      "close": 23.51,
      "volume": 2200,
      "datetime": 1736347560000
    },
    {
      "open": 23.5,
      "high": 23.5176,
      "low": 23.4599,
      "close": 23.4652,
      "volume": 4225,
      "datetime": 1736347620000
    },
    {
      "open": 23.45,
      "high": 23.49,
      "low": 23.45,
      "close": 23.49,
      "volume": 43204,
      "datetime": 1736347680000
    },
    {
      "open": 23.4859,
      "high": 23.4859,
      "low": 23.42,
      "close": 23.4337,
      "volume": 12500,
      "datetime": 1736347740000
    },
    {
      "open": 23.44,
      "high": 23.455,
      "low": 23.39,
      "close": 23.39,
      "volume": 2100,
      "datetime": 1736347800000
    },
    {
      "open": 23.4099,
      "high": 23.43,
      "low": 23.4099,
      "close": 23.4171,
      "volume": 2597,
      "datetime": 1736347860000
    },
    {
      "open": 23.45,
      "high": 23.49,
      "low": 23.45,
      "close": 23.49,
      "volume": 5224,
      "datetime": 1736347920000
    },
    {
      "open": 23.4947,
      "high": 23.5,
      "low": 23.48,
      "close": 23.489,
      "volume": 5753,
      "datetime": 1736347980000
    },
    {
      "open": 23.4952,
      "high": 23.5,
      "low": 23.4645,
      "close": 23.4799,
      "volume": 11253,
      "datetime": 1736348040000
    },
    {
      "open": 23.465,
      "high": 23.465,
      "low": 23.44,
      "close": 23.44,
      "volume": 1254,
      "datetime": 1736348100000
    },
    {
      "open": 23.426,
      "high": 23.426,
      "low": 23.4199,
      "close": 23.4199,
      "volume": 4108,
      "datetime": 1736348160000
    },
    {
      "open": 23.429,
      "high": 23.429,
      "low": 23.429,
      "close": 23.429,
      "volume": 2200,
      "datetime": 1736348220000
    },
    {
      "open": 23.45,
      "high": 23.475,
      "low": 23.4376,
      "close": 23.4376,
      "volume": 3700,
      "datetime": 1736348280000
    },
    {
      "open": 23.41,
      "high": 23.425,
      "low": 23.41,
      "close": 23.425,
      "volume": 5051,
      "datetime": 1736348340000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.42,
      "close": 23.42,
      "volume": 200,
      "datetime": 1736348400000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.3701,
      "close": 23.3701,
      "volume": 4110,
      "datetime": 1736348460000
    },
    {
      "open": 23.36,
      "high": 23.3829,
      "low": 23.355,
      "close": 23.37,
      "volume": 1900,
      "datetime": 1736348520000
    },
    {
      "open": 23.3586,
      "high": 23.3586,
      "low": 23.29,
      "close": 23.3,
      "volume": 5717,
      "datetime": 1736348580000
    },
    {
      "open": 23.295,
      "high": 23.3001,
      "low": 23.29,
      "close": 23.2916,
      "volume": 7747,
      "datetime": 1736348640000
    },
    {
      "open": 23.3,
      "high": 23.3099,
      "low": 23.25,
      "close": 23.3099,
      "volume": 2336,
      "datetime": 1736348700000
    },
    {
      "open": 23.29,
      "high": 23.29,
      "low": 23.24,
      "close": 23.24,
      "volume": 3896,
      "datetime": 1736348760000
    },
    {
      "open": 23.23,
      "high": 23.275,
      "low": 23.23,
      "close": 23.26,
      "volume": 6556,
      "datetime": 1736348820000
    },
    {
      "open": 23.25,
      "high": 23.295,
      "low": 23.25,
      "close": 23.27,
      "volume": 1250,
      "datetime": 1736348880000
    },
    {
      "open": 23.27,
      "high": 23.29,
      "low": 23.2601,
      "close": 23.29,
      "volume": 1808,
      "datetime": 1736348940000
    },
    {
      "open": 23.27,
      "high": 23.33,
      "low": 23.27,
      "close": 23.33,
      "volume": 4340,
      "datetime": 1736349000000
    },
    {
      "open": 23.33,
      "high": 23.38,
      "low": 23.33,
      "close": 23.38,
      "volume": 3424,
      "datetime": 1736349060000
    },
    {
      "open": 23.38,
      "high": 23.3999,
      "low": 23.36,
      "close": 23.3999,
      "volume": 5161,
      "datetime": 1736349120000
    },
    {
      "open": 23.3996,
      "high": 23.4285,
      "low": 23.3996,
      "close": 23.4268,
      "volume": 1257,
      "datetime": 1736349180000
    },
    {
      "open": 23.44,
      "high": 23.45,
      "low": 23.44,
      "close": 23.45,
      "volume": 375,
      "datetime": 1736349240000
    },
    {
      "open": 23.445,
      "high": 23.495,
      "low": 23.445,
      "close": 23.475,
      "volume": 4306,
      "datetime": 1736349300000
    },
    {
      "open": 23.475,
      "high": 23.5,
      "low": 23.475,
      "close": 23.48,
      "volume": 6350,
      "datetime": 1736349360000
    },
    {
      "open": 23.4626,
      "high": 23.47,
      "low": 23.443,
      "close": 23.449,
      "volume": 3500,
      "datetime": 1736349420000
    },
    {
      "open": 23.43,
      "high": 23.4397,
      "low": 23.41,
      "close": 23.41,
      "volume": 1700,
      "datetime": 1736349480000
    },
    {
      "open": 23.41,
      "high": 23.42,
      "low": 23.39,
      "close": 23.4,
      "volume": 575,
      "datetime": 1736349540000
    },
    {
      "open": 23.425,
      "high": 23.5,
      "low": 23.425,
      "close": 23.5,
      "volume": 2157,
      "datetime": 1736349600000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.465,
      "close": 23.47,
      "volume": 4124,
      "datetime": 1736349660000
    },
    {
      "open": 23.472823,
      "high": 23.52,
      "low": 23.472823,
      "close": 23.52,
      "volume": 7924,
      "datetime": 1736349720000
    },
    {
      "open": 23.54,
      "high": 23.555,
      "low": 23.52,
      "close": 23.52,
      "volume": 7835,
      "datetime": 1736349780000
    },
    {
      "open": 23.5198,
      "high": 23.52,
      "low": 23.4886,
      "close": 23.49,
      "volume": 8677,
      "datetime": 1736349840000
    },
    {
      "open": 23.4799,
      "high": 23.5074,
      "low": 23.478,
      "close": 23.5,
      "volume": 3603,
      "datetime": 1736349900000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.47,
      "close": 23.47,
      "volume": 1491,
      "datetime": 1736349960000
    },
    {
      "open": 23.47,
      "high": 23.515,
      "low": 23.47,
      "close": 23.5,
      "volume": 3125,
      "datetime": 1736350020000
    },
    {
      "open": 23.51,
      "high": 23.5293,
      "low": 23.51,
      "close": 23.52,
      "volume": 2049,
      "datetime": 1736350080000
    },
    {
      "open": 23.54,
      "high": 23.57,
      "low": 23.54,
      "close": 23.57,
      "volume": 2200,
      "datetime": 1736350140000
    },
    {
      "open": 23.54,
      "high": 23.545,
      "low": 23.52,
      "close": 23.52,
      "volume": 3700,
      "datetime": 1736350200000
    },
    {
      "open": 23.528,
      "high": 23.53,
      "low": 23.52,
      "close": 23.52,
      "volume": 2874,
      "datetime": 1736350260000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.5176,
      "close": 23.53,
      "volume": 1051,
      "datetime": 1736350320000
    },
    {
      "open": 23.55,
      "high": 23.56,
      "low": 23.54,
      "close": 23.56,
      "volume": 1525,
      "datetime": 1736350380000
    },
    {
      "open": 23.59,
      "high": 23.5923,
      "low": 23.57,
      "close": 23.57,
      "volume": 1330,
      "datetime": 1736350440000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.5,
      "close": 23.505,
      "volume": 6174,
      "datetime": 1736350500000
    },
    {
      "open": 23.5102,
      "high": 23.5102,
      "low": 23.46,
      "close": 23.46,
      "volume": 1837,
      "datetime": 1736350560000
    },
    {
      "open": 23.46,
      "high": 23.47,
      "low": 23.44,
      "close": 23.44,
      "volume": 1178,
      "datetime": 1736350620000
    },
    {
      "open": 23.44,
      "high": 23.47,
      "low": 23.426,
      "close": 23.47,
      "volume": 3423,
      "datetime": 1736350680000
    },
    {
      "open": 23.47,
      "high": 23.48,
      "low": 23.47,
      "close": 23.48,
      "volume": 900,
      "datetime": 1736350740000
    },
    {
      "open": 23.53,
      "high": 23.54,
      "low": 23.526,
      "close": 23.526,
      "volume": 4322,
      "datetime": 1736350800000
    },
    {
      "open": 23.53,
      "high": 23.5476,
      "low": 23.5,
      "close": 23.5,
      "volume": 1007,
      "datetime": 1736350860000
    },
    {
      "open": 23.5,
      "high": 23.525,
      "low": 23.49,
      "close": 23.525,
      "volume": 1100,
      "datetime": 1736350920000
    },
    {
      "open": 23.5,
      "high": 23.515,
      "low": 23.5,
      "close": 23.505,
      "volume": 1812,
      "datetime": 1736350980000
    },
    {
      "open": 23.505,
      "high": 23.51,
      "low": 23.5,
      "close": 23.51,
      "volume": 1475,
      "datetime": 1736351040000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.46,
      "close": 23.4667,
      "volume": 3708,
      "datetime": 1736351100000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.47,
      "close": 23.47,
      "volume": 475,
      "datetime": 1736351160000
    },
    {
      "open": 23.47,
      "high": 23.51,
      "low": 23.47,
      "close": 23.51,
      "volume": 725,
      "datetime": 1736351220000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.48,
      "close": 23.48,
      "volume": 325,
      "datetime": 1736351280000
    },
    {
      "open": 23.4924,
      "high": 23.4924,
      "low": 23.49,
      "close": 23.49,
      "volume": 800,
      "datetime": 1736351340000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.48,
      "close": 23.48,
      "volume": 1004,
      "datetime": 1736351400000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.45,
      "close": 23.45,
      "volume": 30730,
      "datetime": 1736351460000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.41,
      "close": 23.41,
      "volume": 6103,
      "datetime": 1736351520000
    },
    {
      "open": 23.41,
      "high": 23.42,
      "low": 23.41,
      "close": 23.42,
      "volume": 2022,
      "datetime": 1736351580000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.42,
      "close": 23.42,
      "volume": 984,
      "datetime": 1736351640000
    },
    {
      "open": 23.41,
      "high": 23.4201,
      "low": 23.41,
      "close": 23.4201,
      "volume": 4733,
      "datetime": 1736351700000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 700,
      "datetime": 1736351760000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.41,
      "close": 23.41,
      "volume": 550,
      "datetime": 1736351820000
    },
    {
      "open": 23.395,
      "high": 23.395,
      "low": 23.395,
      "close": 23.395,
      "volume": 1300,
      "datetime": 1736351880000
    },
    {
      "open": 23.39,
      "high": 23.395,
      "low": 23.38,
      "close": 23.38,
      "volume": 2451,
      "datetime": 1736351940000
    },
    {
      "open": 23.375,
      "high": 23.4013,
      "low": 23.371,
      "close": 23.4013,
      "volume": 5800,
      "datetime": 1736352000000
    },
    {
      "open": 23.41,
      "high": 23.43,
      "low": 23.41,
      "close": 23.43,
      "volume": 1100,
      "datetime": 1736352060000
    },
    {
      "open": 23.445,
      "high": 23.445,
      "low": 23.435,
      "close": 23.445,
      "volume": 800,
      "datetime": 1736352120000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.435,
      "close": 23.44,
      "volume": 26188,
      "datetime": 1736352180000
    },
    {
      "open": 23.45,
      "high": 23.456974,
      "low": 23.446956,
      "close": 23.456974,
      "volume": 2305,
      "datetime": 1736352240000
    },
    {
      "open": 23.47,
      "high": 23.48,
      "low": 23.47,
      "close": 23.47,
      "volume": 3325,
      "datetime": 1736352300000
    },
    {
      "open": 23.5,
      "high": 23.52,
      "low": 23.5,
      "close": 23.51,
      "volume": 831,
      "datetime": 1736352360000
    },
    {
      "open": 23.51,
      "high": 23.53,
      "low": 23.51,
      "close": 23.53,
      "volume": 1500,
      "datetime": 1736352420000
    },
    {
      "open": 23.515,
      "high": 23.515,
      "low": 23.485,
      "close": 23.49,
      "volume": 1900,
      "datetime": 1736352480000
    },
    {
      "open": 23.46,
      "high": 23.47,
      "low": 23.46,
      "close": 23.47,
      "volume": 5053,
      "datetime": 1736352540000
    },
    {
      "open": 23.448,
      "high": 23.45,
      "low": 23.44,
      "close": 23.44,
      "volume": 4738,
      "datetime": 1736352600000
    },
    {
      "open": 23.44,
      "high": 23.465,
      "low": 23.44,
      "close": 23.465,
      "volume": 4100,
      "datetime": 1736352660000
    },
    {
      "open": 23.4833,
      "high": 23.49,
      "low": 23.4833,
      "close": 23.49,
      "volume": 300,
      "datetime": 1736352720000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.495,
      "close": 23.495,
      "volume": 987,
      "datetime": 1736352780000
    },
    {
      "open": 23.47,
      "high": 23.49,
      "low": 23.47,
      "close": 23.49,
      "volume": 426,
      "datetime": 1736352840000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.52,
      "close": 23.52,
      "volume": 650,
      "datetime": 1736352900000
    },
    {
      "open": 23.51,
      "high": 23.52,
      "low": 23.505,
      "close": 23.505,
      "volume": 523,
      "datetime": 1736352960000
    },
    {
      "open": 23.51,
      "high": 23.518,
      "low": 23.505,
      "close": 23.515,
      "volume": 2919,
      "datetime": 1736353020000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.5,
      "close": 23.5,
      "volume": 975,
      "datetime": 1736353080000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.4474,
      "close": 23.4474,
      "volume": 400,
      "datetime": 1736353200000
    },
    {
      "open": 23.44,
      "high": 23.46,
      "low": 23.43,
      "close": 23.46,
      "volume": 3639,
      "datetime": 1736353260000
    },
    {
      "open": 23.45,
      "high": 23.46,
      "low": 23.45,
      "close": 23.45,
      "volume": 4145,
      "datetime": 1736353320000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.445,
      "close": 23.445,
      "volume": 1147,
      "datetime": 1736353380000
    },
    {
      "open": 23.44,
      "high": 23.445,
      "low": 23.44,
      "close": 23.445,
      "volume": 1175,
      "datetime": 1736353440000
    },
    {
      "open": 23.46,
      "high": 23.47,
      "low": 23.45,
      "close": 23.46,
      "volume": 1677,
      "datetime": 1736353500000
    },
    {
      "open": 23.466,
      "high": 23.475,
      "low": 23.466,
      "close": 23.4731,
      "volume": 9699,
      "datetime": 1736353560000
    },
    {
      "open": 23.48,
      "high": 23.5,
      "low": 23.48,
      "close": 23.5,
      "volume": 650,
      "datetime": 1736353620000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.52,
      "close": 23.52,
      "volume": 795,
      "datetime": 1736353680000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.51,
      "close": 23.5198,
      "volume": 955,
      "datetime": 1736353740000
    },
    {
      "open": 23.5001,
      "high": 23.5001,
      "low": 23.48,
      "close": 23.4971,
      "volume": 734,
      "datetime": 1736353800000
    },
    {
      "open": 23.49,
      "high": 23.51,
      "low": 23.49,
      "close": 23.51,
      "volume": 1075,
      "datetime": 1736353860000
    },
    {
      "open": 23.51,
      "high": 23.5131,
      "low": 23.51,
      "close": 23.51,
      "volume": 2875,
      "datetime": 1736353920000
    },
    {
      "open": 23.51,
      "high": 23.52,
      "low": 23.51,
      "close": 23.52,
      "volume": 625,
      "datetime": 1736353980000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 159,
      "datetime": 1736354040000
    },
    {
      "open": 23.5299,
      "high": 23.5299,
      "low": 23.5,
      "close": 23.5,
      "volume": 1150,
      "datetime": 1736354160000
    },
    {
      "open": 23.47,
      "high": 23.475,
      "low": 23.46,
      "close": 23.46,
      "volume": 1150,
      "datetime": 1736354220000
    },
    {
      "open": 23.465,
      "high": 23.475,
      "low": 23.465,
      "close": 23.47,
      "volume": 2550,
      "datetime": 1736354280000
    },
    {
      "open": 23.48,
      "high": 23.505,
      "low": 23.48,
      "close": 23.5,
      "volume": 1999,
      "datetime": 1736354340000
    },
    {
      "open": 23.52,
      "high": 23.5299,
      "low": 23.5,
      "close": 23.5122,
      "volume": 3691,
      "datetime": 1736354460000
    },
    {
      "open": 23.51,
      "high": 23.52,
      "low": 23.51,
      "close": 23.52,
      "volume": 850,
      "datetime": 1736354520000
    },
    {
      "open": 23.5226,
      "high": 23.55,
      "low": 23.5226,
      "close": 23.55,
      "volume": 5014,
      "datetime": 1736354580000
    },
    {
      "open": 23.56,
      "high": 23.57,
      "low": 23.56,
      "close": 23.56,
      "volume": 1225,
      "datetime": 1736354640000
    },
    {
      "open": 23.545,
      "high": 23.555,
      "low": 23.545,
      "close": 23.555,
      "volume": 750,
      "datetime": 1736354700000
    },
    {
      "open": 23.57,
      "high": 23.5701,
      "low": 23.565,
      "close": 23.568,
      "volume": 1310,
      "datetime": 1736354760000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 534,
      "datetime": 1736354820000
    },
    {
      "open": 23.56,
      "high": 23.561,
      "low": 23.535,
      "close": 23.535,
      "volume": 4759,
      "datetime": 1736354880000
    },
    {
      "open": 23.5399,
      "high": 23.57,
      "low": 23.5399,
      "close": 23.57,
      "volume": 7434,
      "datetime": 1736354940000
    },
    {
      "open": 23.56,
      "high": 23.57,
      "low": 23.56,
      "close": 23.565,
      "volume": 4700,
      "datetime": 1736355000000
    },
    {
      "open": 23.56,
      "high": 23.57,
      "low": 23.555,
      "close": 23.5676,
      "volume": 10152,
      "datetime": 1736355060000
    },
    {
      "open": 23.575,
      "high": 23.575,
      "low": 23.5667,
      "close": 23.57,
      "volume": 3900,
      "datetime": 1736355120000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.5611,
      "close": 23.565,
      "volume": 1710,
      "datetime": 1736355180000
    },
    {
      "open": 23.56,
      "high": 23.58,
      "low": 23.56,
      "close": 23.58,
      "volume": 1475,
      "datetime": 1736355240000
    },
    {
      "open": 23.59,
      "high": 23.6,
      "low": 23.59,
      "close": 23.6,
      "volume": 2188,
      "datetime": 1736355300000
    },
    {
      "open": 23.5999,
      "high": 23.6,
      "low": 23.59,
      "close": 23.595,
      "volume": 2025,
      "datetime": 1736355360000
    },
    {
      "open": 23.57,
      "high": 23.575,
      "low": 23.557,
      "close": 23.557,
      "volume": 2299,
      "datetime": 1736355420000
    },
    {
      "open": 23.545,
      "high": 23.5499,
      "low": 23.54,
      "close": 23.5499,
      "volume": 3902,
      "datetime": 1736355480000
    },
    {
      "open": 23.5398,
      "high": 23.5398,
      "low": 23.5398,
      "close": 23.5398,
      "volume": 100,
      "datetime": 1736355540000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.5451,
      "close": 23.5451,
      "volume": 832,
      "datetime": 1736355600000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.5314,
      "close": 23.535,
      "volume": 5544,
      "datetime": 1736355660000
    },
    {
      "open": 23.53,
      "high": 23.6,
      "low": 23.53,
      "close": 23.6,
      "volume": 2967,
      "datetime": 1736355720000
    },
    {
      "open": 23.61,
      "high": 23.66,
      "low": 23.605,
      "close": 23.6364,
      "volume": 6415,
      "datetime": 1736355780000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.615,
      "close": 23.63,
      "volume": 2275,
      "datetime": 1736355840000
    },
    {
      "open": 23.66,
      "high": 23.67,
      "low": 23.6502,
      "close": 23.6502,
      "volume": 10673,
      "datetime": 1736355900000
    },
    {
      "open": 23.665,
      "high": 23.675,
      "low": 23.66,
      "close": 23.67,
      "volume": 4124,
      "datetime": 1736355960000
    },
    {
      "open": 23.67,
      "high": 23.69,
      "low": 23.665,
      "close": 23.69,
      "volume": 17969,
      "datetime": 1736356020000
    },
    {
      "open": 23.687,
      "high": 23.7,
      "low": 23.68,
      "close": 23.7,
      "volume": 3118,
      "datetime": 1736356080000
    },
    {
      "open": 23.71,
      "high": 23.745,
      "low": 23.71,
      "close": 23.73,
      "volume": 4145,
      "datetime": 1736356140000
    },
    {
      "open": 23.7071,
      "high": 23.7071,
      "low": 23.68,
      "close": 23.68,
      "volume": 1176,
      "datetime": 1736356200000
    },
    {
      "open": 23.685,
      "high": 23.72,
      "low": 23.685,
      "close": 23.72,
      "volume": 2502,
      "datetime": 1736356260000
    },
    {
      "open": 23.72,
      "high": 23.75,
      "low": 23.715,
      "close": 23.7466,
      "volume": 3200,
      "datetime": 1736356320000
    },
    {
      "open": 23.765,
      "high": 23.765,
      "low": 23.7478,
      "close": 23.7478,
      "volume": 4506,
      "datetime": 1736356380000
    },
    {
      "open": 23.77,
      "high": 23.779,
      "low": 23.755,
      "close": 23.774,
      "volume": 56097,
      "datetime": 1736356440000
    },
    {
      "open": 23.77,
      "high": 23.78,
      "low": 23.75,
      "close": 23.775,
      "volume": 30751,
      "datetime": 1736356500000
    },
    {
      "open": 23.78,
      "high": 23.785,
      "low": 23.7421,
      "close": 23.76,
      "volume": 5053,
      "datetime": 1736356560000
    },
    {
      "open": 23.765,
      "high": 23.79,
      "low": 23.7301,
      "close": 23.79,
      "volume": 4552,
      "datetime": 1736356620000
    },
    {
      "open": 23.79,
      "high": 23.79,
      "low": 23.74,
      "close": 23.74,
      "volume": 5107,
      "datetime": 1736356680000
    },
    {
      "open": 23.75,
      "high": 23.76,
      "low": 23.74,
      "close": 23.76,
      "volume": 2042,
      "datetime": 1736356740000
    },
    {
      "open": 23.779,
      "high": 23.7968,
      "low": 23.779,
      "close": 23.7901,
      "volume": 5006,
      "datetime": 1736356800000
    },
    {
      "open": 23.7923,
      "high": 23.82,
      "low": 23.77,
      "close": 23.815,
      "volume": 9054,
      "datetime": 1736356860000
    },
    {
      "open": 23.81,
      "high": 23.8369,
      "low": 23.8,
      "close": 23.835,
      "volume": 1956,
      "datetime": 1736356920000
    },
    {
      "open": 23.83,
      "high": 23.8922,
      "low": 23.83,
      "close": 23.8922,
      "volume": 7356,
      "datetime": 1736356980000
    },
    {
      "open": 23.88,
      "high": 23.93,
      "low": 23.865,
      "close": 23.93,
      "volume": 6897,
      "datetime": 1736357040000
    },
    {
      "open": 23.93,
      "high": 23.9421,
      "low": 23.8899,
      "close": 23.9421,
      "volume": 14414,
      "datetime": 1736357100000
    },
    {
      "open": 23.9402,
      "high": 23.945,
      "low": 23.9001,
      "close": 23.9001,
      "volume": 6149,
      "datetime": 1736357160000
    },
    {
      "open": 23.915,
      "high": 23.966,
      "low": 23.915,
      "close": 23.96,
      "volume": 9537,
      "datetime": 1736357220000
    },
    {
      "open": 23.98,
      "high": 23.99,
      "low": 23.92,
      "close": 23.98,
      "volume": 12218,
      "datetime": 1736357280000
    },
    {
      "open": 23.98,
      "high": 24.0199,
      "low": 23.98,
      "close": 23.99,
      "volume": 11688,
      "datetime": 1736357340000
    },
    {
      "open": 23.99,
      "high": 24.059,
      "low": 23.99,
      "close": 24.0498,
      "volume": 19632,
      "datetime": 1736357400000
    },
    {
      "open": 24.0501,
      "high": 24.11,
      "low": 24.0402,
      "close": 24.06,
      "volume": 15416,
      "datetime": 1736357460000
    },
    {
      "open": 24.04,
      "high": 24.045,
      "low": 23.92,
      "close": 23.9206,
      "volume": 16857,
      "datetime": 1736357520000
    },
    {
      "open": 23.92,
      "high": 23.95,
      "low": 23.913,
      "close": 23.927257,
      "volume": 4925,
      "datetime": 1736357580000
    },
    {
      "open": 23.94,
      "high": 23.98,
      "low": 23.93,
      "close": 23.97,
      "volume": 1503,
      "datetime": 1736357640000
    },
    {
      "open": 23.97,
      "high": 23.98,
      "low": 23.96,
      "close": 23.977,
      "volume": 3312,
      "datetime": 1736357700000
    },
    {
      "open": 24,
      "high": 24.04,
      "low": 23.97,
      "close": 23.97,
      "volume": 13715,
      "datetime": 1736357760000
    },
    {
      "open": 23.98,
      "high": 23.98,
      "low": 23.8901,
      "close": 23.8901,
      "volume": 6925,
      "datetime": 1736357820000
    },
    {
      "open": 23.8802,
      "high": 23.91,
      "low": 23.86,
      "close": 23.91,
      "volume": 3247,
      "datetime": 1736357880000
    },
    {
      "open": 23.92,
      "high": 23.93,
      "low": 23.91,
      "close": 23.92,
      "volume": 1775,
      "datetime": 1736357940000
    },
    {
      "open": 23.94,
      "high": 23.94,
      "low": 23.8622,
      "close": 23.87,
      "volume": 6248,
      "datetime": 1736358000000
    },
    {
      "open": 23.86,
      "high": 23.865,
      "low": 23.83,
      "close": 23.86,
      "volume": 3661,
      "datetime": 1736358060000
    },
    {
      "open": 23.855,
      "high": 23.855,
      "low": 23.8,
      "close": 23.81,
      "volume": 7576,
      "datetime": 1736358120000
    },
    {
      "open": 23.825,
      "high": 23.84,
      "low": 23.8125,
      "close": 23.84,
      "volume": 8054,
      "datetime": 1736358180000
    },
    {
      "open": 23.85,
      "high": 23.86,
      "low": 23.83,
      "close": 23.84,
      "volume": 1425,
      "datetime": 1736358240000
    },
    {
      "open": 23.84,
      "high": 23.8528,
      "low": 23.82,
      "close": 23.82,
      "volume": 3102,
      "datetime": 1736358300000
    },
    {
      "open": 23.83,
      "high": 23.83,
      "low": 23.79,
      "close": 23.82,
      "volume": 1999,
      "datetime": 1736358360000
    },
    {
      "open": 23.81,
      "high": 23.87,
      "low": 23.81,
      "close": 23.87,
      "volume": 3150,
      "datetime": 1736358420000
    },
    {
      "open": 23.88,
      "high": 23.88,
      "low": 23.85,
      "close": 23.85,
      "volume": 1888,
      "datetime": 1736358480000
    },
    {
      "open": 23.8476,
      "high": 23.8676,
      "low": 23.82,
      "close": 23.86,
      "volume": 1900,
      "datetime": 1736358540000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.81,
      "close": 23.82,
      "volume": 1641,
      "datetime": 1736358600000
    },
    {
      "open": 23.83,
      "high": 23.86,
      "low": 23.82,
      "close": 23.83,
      "volume": 875,
      "datetime": 1736358660000
    },
    {
      "open": 23.81,
      "high": 23.81,
      "low": 23.785,
      "close": 23.785,
      "volume": 3400,
      "datetime": 1736358720000
    },
    {
      "open": 23.775,
      "high": 23.795,
      "low": 23.77,
      "close": 23.79,
      "volume": 4411,
      "datetime": 1736358780000
    },
    {
      "open": 23.79,
      "high": 23.795,
      "low": 23.78,
      "close": 23.79,
      "volume": 2250,
      "datetime": 1736358840000
    },
    {
      "open": 23.78,
      "high": 23.79,
      "low": 23.78,
      "close": 23.78,
      "volume": 1225,
      "datetime": 1736358900000
    },
    {
      "open": 23.79,
      "high": 23.79,
      "low": 23.77,
      "close": 23.78,
      "volume": 1050,
      "datetime": 1736358960000
    },
    {
      "open": 23.75,
      "high": 23.7551,
      "low": 23.74,
      "close": 23.75,
      "volume": 3357,
      "datetime": 1736359020000
    },
    {
      "open": 23.755,
      "high": 23.755,
      "low": 23.72,
      "close": 23.725,
      "volume": 1875,
      "datetime": 1736359080000
    },
    {
      "open": 23.72,
      "high": 23.74,
      "low": 23.72,
      "close": 23.74,
      "volume": 8684,
      "datetime": 1736359140000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.72,
      "close": 23.7295,
      "volume": 936,
      "datetime": 1736359200000
    },
    {
      "open": 23.7,
      "high": 23.73,
      "low": 23.6812,
      "close": 23.72,
      "volume": 2415,
      "datetime": 1736359260000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.6703,
      "close": 23.68,
      "volume": 1700,
      "datetime": 1736359320000
    },
    {
      "open": 23.68,
      "high": 23.69,
      "low": 23.67,
      "close": 23.69,
      "volume": 3917,
      "datetime": 1736359380000
    },
    {
      "open": 23.665,
      "high": 23.665,
      "low": 23.612,
      "close": 23.63,
      "volume": 15379,
      "datetime": 1736359440000
    },
    {
      "open": 23.64,
      "high": 23.695,
      "low": 23.64,
      "close": 23.695,
      "volume": 10533,
      "datetime": 1736359500000
    },
    {
      "open": 23.65,
      "high": 23.66,
      "low": 23.64,
      "close": 23.64,
      "volume": 1218,
      "datetime": 1736359560000
    },
    {
      "open": 23.6226,
      "high": 23.6332,
      "low": 23.6119,
      "close": 23.6332,
      "volume": 3773,
      "datetime": 1736359620000
    },
    {
      "open": 23.63,
      "high": 23.64,
      "low": 23.61,
      "close": 23.64,
      "volume": 7183,
      "datetime": 1736359680000
    },
    {
      "open": 23.6523,
      "high": 23.6523,
      "low": 23.62,
      "close": 23.62,
      "volume": 9251,
      "datetime": 1736359740000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.59,
      "close": 23.59,
      "volume": 1692,
      "datetime": 1736359800000
    },
    {
      "open": 23.59,
      "high": 23.61,
      "low": 23.59,
      "close": 23.59,
      "volume": 2636,
      "datetime": 1736359860000
    },
    {
      "open": 23.59,
      "high": 23.605,
      "low": 23.59,
      "close": 23.595,
      "volume": 2172,
      "datetime": 1736359920000
    },
    {
      "open": 23.5903,
      "high": 23.6185,
      "low": 23.5903,
      "close": 23.6179,
      "volume": 4945,
      "datetime": 1736359980000
    },
    {
      "open": 23.61,
      "high": 23.6676,
      "low": 23.61,
      "close": 23.6499,
      "volume": 3126,
      "datetime": 1736360040000
    },
    {
      "open": 23.64,
      "high": 23.645,
      "low": 23.63,
      "close": 23.645,
      "volume": 8187,
      "datetime": 1736360100000
    },
    {
      "open": 23.645,
      "high": 23.645,
      "low": 23.6,
      "close": 23.6,
      "volume": 10815,
      "datetime": 1736360160000
    },
    {
      "open": 23.6137,
      "high": 23.635,
      "low": 23.6137,
      "close": 23.625,
      "volume": 747,
      "datetime": 1736360220000
    },
    {
      "open": 23.6299,
      "high": 23.6299,
      "low": 23.59,
      "close": 23.59,
      "volume": 721,
      "datetime": 1736360280000
    },
    {
      "open": 23.59,
      "high": 23.59,
      "low": 23.57,
      "close": 23.575,
      "volume": 4736,
      "datetime": 1736360340000
    },
    {
      "open": 23.584,
      "high": 23.584,
      "low": 23.56,
      "close": 23.56,
      "volume": 30350,
      "datetime": 1736360400000
    },
    {
      "open": 23.55,
      "high": 23.5799,
      "low": 23.55,
      "close": 23.5799,
      "volume": 1975,
      "datetime": 1736360460000
    },
    {
      "open": 23.59,
      "high": 23.615,
      "low": 23.59,
      "close": 23.61,
      "volume": 11004,
      "datetime": 1736360520000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.576,
      "close": 23.576,
      "volume": 4785,
      "datetime": 1736360580000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.53,
      "close": 23.53,
      "volume": 3897,
      "datetime": 1736360640000
    },
    {
      "open": 23.54,
      "high": 23.55,
      "low": 23.53,
      "close": 23.53,
      "volume": 1107,
      "datetime": 1736360700000
    },
    {
      "open": 23.5001,
      "high": 23.515,
      "low": 23.5001,
      "close": 23.505,
      "volume": 2905,
      "datetime": 1736360760000
    },
    {
      "open": 23.5,
      "high": 23.51,
      "low": 23.495,
      "close": 23.495,
      "volume": 8322,
      "datetime": 1736360820000
    },
    {
      "open": 23.465,
      "high": 23.47,
      "low": 23.4501,
      "close": 23.46,
      "volume": 5213,
      "datetime": 1736360880000
    },
    {
      "open": 23.47,
      "high": 23.505,
      "low": 23.47,
      "close": 23.495,
      "volume": 1525,
      "datetime": 1736360940000
    },
    {
      "open": 23.5,
      "high": 23.535,
      "low": 23.5,
      "close": 23.5233,
      "volume": 2539,
      "datetime": 1736361000000
    },
    {
      "open": 23.53,
      "high": 23.56,
      "low": 23.53,
      "close": 23.5598,
      "volume": 1548,
      "datetime": 1736361060000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.5788,
      "close": 23.5788,
      "volume": 1200,
      "datetime": 1736361120000
    },
    {
      "open": 23.575,
      "high": 23.59,
      "low": 23.575,
      "close": 23.59,
      "volume": 400,
      "datetime": 1736361180000
    },
    {
      "open": 23.57,
      "high": 23.61,
      "low": 23.57,
      "close": 23.6014,
      "volume": 1570,
      "datetime": 1736361240000
    },
    {
      "open": 23.59,
      "high": 23.6,
      "low": 23.5886,
      "close": 23.5886,
      "volume": 3343,
      "datetime": 1736361300000
    },
    {
      "open": 23.582,
      "high": 23.59,
      "low": 23.5702,
      "close": 23.59,
      "volume": 4964,
      "datetime": 1736361360000
    },
    {
      "open": 23.575,
      "high": 23.575,
      "low": 23.575,
      "close": 23.575,
      "volume": 100,
      "datetime": 1736361420000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.57,
      "close": 23.57,
      "volume": 2536,
      "datetime": 1736361480000
    },
    {
      "open": 23.56,
      "high": 23.585,
      "low": 23.56,
      "close": 23.58,
      "volume": 2189,
      "datetime": 1736361540000
    },
    {
      "open": 23.58,
      "high": 23.59,
      "low": 23.57,
      "close": 23.59,
      "volume": 529,
      "datetime": 1736361600000
    },
    {
      "open": 23.6,
      "high": 23.628,
      "low": 23.6,
      "close": 23.61,
      "volume": 1289,
      "datetime": 1736361660000
    },
    {
      "open": 23.61,
      "high": 23.63,
      "low": 23.61,
      "close": 23.62,
      "volume": 400,
      "datetime": 1736361720000
    },
    {
      "open": 23.64,
      "high": 23.65,
      "low": 23.64,
      "close": 23.65,
      "volume": 2076,
      "datetime": 1736361780000
    },
    {
      "open": 23.655,
      "high": 23.655,
      "low": 23.64,
      "close": 23.64,
      "volume": 1700,
      "datetime": 1736361840000
    },
    {
      "open": 23.671,
      "high": 23.671,
      "low": 23.671,
      "close": 23.671,
      "volume": 220,
      "datetime": 1736361900000
    },
    {
      "open": 23.65,
      "high": 23.655,
      "low": 23.65,
      "close": 23.655,
      "volume": 200,
      "datetime": 1736361960000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.67,
      "close": 23.68,
      "volume": 3099,
      "datetime": 1736362020000
    },
    {
      "open": 23.6899,
      "high": 23.72,
      "low": 23.6899,
      "close": 23.69,
      "volume": 8006,
      "datetime": 1736362080000
    },
    {
      "open": 23.6828,
      "high": 23.7,
      "low": 23.6828,
      "close": 23.7,
      "volume": 640,
      "datetime": 1736362140000
    },
    {
      "open": 23.69,
      "high": 23.71,
      "low": 23.69,
      "close": 23.71,
      "volume": 452,
      "datetime": 1736362200000
    },
    {
      "open": 23.69,
      "high": 23.71,
      "low": 23.6899,
      "close": 23.7099,
      "volume": 625,
      "datetime": 1736362260000
    },
    {
      "open": 23.7,
      "high": 23.73,
      "low": 23.7,
      "close": 23.73,
      "volume": 890,
      "datetime": 1736362320000
    },
    {
      "open": 23.74,
      "high": 23.77,
      "low": 23.7399,
      "close": 23.76,
      "volume": 1832,
      "datetime": 1736362380000
    },
    {
      "open": 23.77,
      "high": 23.7976,
      "low": 23.77,
      "close": 23.78,
      "volume": 2825,
      "datetime": 1736362440000
    },
    {
      "open": 23.79,
      "high": 23.79,
      "low": 23.76,
      "close": 23.76,
      "volume": 1325,
      "datetime": 1736362500000
    },
    {
      "open": 23.77,
      "high": 23.77,
      "low": 23.74,
      "close": 23.745,
      "volume": 4745,
      "datetime": 1736362560000
    },
    {
      "open": 23.705,
      "high": 23.705,
      "low": 23.6935,
      "close": 23.7,
      "volume": 3100,
      "datetime": 1736362620000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.67,
      "close": 23.67,
      "volume": 1575,
      "datetime": 1736362680000
    },
    {
      "open": 23.67,
      "high": 23.67,
      "low": 23.66,
      "close": 23.66,
      "volume": 2801,
      "datetime": 1736362740000
    },
    {
      "open": 23.64,
      "high": 23.6513,
      "low": 23.64,
      "close": 23.6513,
      "volume": 650,
      "datetime": 1736362800000
    },
    {
      "open": 23.67,
      "high": 23.7026,
      "low": 23.67,
      "close": 23.7026,
      "volume": 1703,
      "datetime": 1736362860000
    },
    {
      "open": 23.68,
      "high": 23.72,
      "low": 23.68,
      "close": 23.72,
      "volume": 1758,
      "datetime": 1736362920000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.64,
      "close": 23.64,
      "volume": 1023,
      "datetime": 1736362980000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 600,
      "datetime": 1736363040000
    },
    {
      "open": 23.615,
      "high": 23.63,
      "low": 23.5901,
      "close": 23.63,
      "volume": 4211,
      "datetime": 1736363100000
    },
    {
      "open": 23.6237,
      "high": 23.63,
      "low": 23.59,
      "close": 23.6,
      "volume": 4987,
      "datetime": 1736363160000
    },
    {
      "open": 23.6098,
      "high": 23.6098,
      "low": 23.59,
      "close": 23.59,
      "volume": 2960,
      "datetime": 1736363220000
    },
    {
      "open": 23.58,
      "high": 23.585,
      "low": 23.55,
      "close": 23.55,
      "volume": 2056,
      "datetime": 1736363280000
    },
    {
      "open": 23.56,
      "high": 23.57,
      "low": 23.545,
      "close": 23.545,
      "volume": 5023,
      "datetime": 1736363340000
    },
    {
      "open": 23.54,
      "high": 23.56,
      "low": 23.54,
      "close": 23.56,
      "volume": 2351,
      "datetime": 1736363400000
    },
    {
      "open": 23.58,
      "high": 23.62,
      "low": 23.58,
      "close": 23.6199,
      "volume": 2500,
      "datetime": 1736363460000
    },
    {
      "open": 23.62,
      "high": 23.645,
      "low": 23.62,
      "close": 23.645,
      "volume": 3435,
      "datetime": 1736363520000
    },
    {
      "open": 23.63,
      "high": 23.63,
      "low": 23.605,
      "close": 23.63,
      "volume": 1975,
      "datetime": 1736363580000
    },
    {
      "open": 23.62,
      "high": 23.66,
      "low": 23.62,
      "close": 23.66,
      "volume": 575,
      "datetime": 1736363640000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.63,
      "close": 23.6348,
      "volume": 1663,
      "datetime": 1736363700000
    },
    {
      "open": 23.62,
      "high": 23.62,
      "low": 23.59,
      "close": 23.62,
      "volume": 1010,
      "datetime": 1736363760000
    },
    {
      "open": 23.63,
      "high": 23.63,
      "low": 23.63,
      "close": 23.63,
      "volume": 400,
      "datetime": 1736363820000
    },
    {
      "open": 23.62,
      "high": 23.62,
      "low": 23.585,
      "close": 23.585,
      "volume": 1734,
      "datetime": 1736363880000
    },
    {
      "open": 23.575,
      "high": 23.595,
      "low": 23.56,
      "close": 23.59,
      "volume": 1625,
      "datetime": 1736363940000
    },
    {
      "open": 23.5805,
      "high": 23.5805,
      "low": 23.575,
      "close": 23.575,
      "volume": 300,
      "datetime": 1736364000000
    },
    {
      "open": 23.5794,
      "high": 23.59,
      "low": 23.57,
      "close": 23.59,
      "volume": 6670,
      "datetime": 1736364060000
    },
    {
      "open": 23.59,
      "high": 23.6,
      "low": 23.581,
      "close": 23.581,
      "volume": 3035,
      "datetime": 1736364120000
    },
    {
      "open": 23.58,
      "high": 23.585,
      "low": 23.57,
      "close": 23.57,
      "volume": 5345,
      "datetime": 1736364180000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.5633,
      "close": 23.57,
      "volume": 1236,
      "datetime": 1736364240000
    },
    {
      "open": 23.5788,
      "high": 23.59,
      "low": 23.57,
      "close": 23.59,
      "volume": 4522,
      "datetime": 1736364300000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.57,
      "close": 23.57,
      "volume": 225,
      "datetime": 1736364360000
    },
    {
      "open": 23.57,
      "high": 23.575,
      "low": 23.525,
      "close": 23.525,
      "volume": 1163,
      "datetime": 1736364420000
    },
    {
      "open": 23.52,
      "high": 23.535,
      "low": 23.5127,
      "close": 23.535,
      "volume": 1756,
      "datetime": 1736364480000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.54,
      "close": 23.54,
      "volume": 600,
      "datetime": 1736364540000
    },
    {
      "open": 23.55,
      "high": 23.57,
      "low": 23.55,
      "close": 23.57,
      "volume": 950,
      "datetime": 1736364600000
    },
    {
      "open": 23.58,
      "high": 23.5901,
      "low": 23.58,
      "close": 23.585,
      "volume": 1045,
      "datetime": 1736364660000
    },
    {
      "open": 23.6,
      "high": 23.605,
      "low": 23.6,
      "close": 23.605,
      "volume": 1064,
      "datetime": 1736364720000
    },
    {
      "open": 23.575,
      "high": 23.615,
      "low": 23.575,
      "close": 23.615,
      "volume": 810,
      "datetime": 1736364840000
    },
    {
      "open": 23.61,
      "high": 23.61,
      "low": 23.61,
      "close": 23.61,
      "volume": 200,
      "datetime": 1736364900000
    },
    {
      "open": 23.6101,
      "high": 23.64,
      "low": 23.6101,
      "close": 23.64,
      "volume": 975,
      "datetime": 1736364960000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.61,
      "close": 23.62,
      "volume": 1431,
      "datetime": 1736365020000
    },
    {
      "open": 23.63,
      "high": 23.64,
      "low": 23.63,
      "close": 23.64,
      "volume": 350,
      "datetime": 1736365080000
    },
    {
      "open": 23.66,
      "high": 23.6711,
      "low": 23.66,
      "close": 23.6711,
      "volume": 1002,
      "datetime": 1736365140000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.68,
      "close": 23.68,
      "volume": 529,
      "datetime": 1736365200000
    },
    {
      "open": 23.69,
      "high": 23.7,
      "low": 23.69,
      "close": 23.69,
      "volume": 1725,
      "datetime": 1736365260000
    },
    {
      "open": 23.695,
      "high": 23.71,
      "low": 23.695,
      "close": 23.7099,
      "volume": 6100,
      "datetime": 1736365320000
    },
    {
      "open": 23.72,
      "high": 23.725,
      "low": 23.72,
      "close": 23.72,
      "volume": 727,
      "datetime": 1736365380000
    },
    {
      "open": 23.7087,
      "high": 23.71,
      "low": 23.69,
      "close": 23.69,
      "volume": 9875,
      "datetime": 1736365500000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.67,
      "close": 23.67,
      "volume": 1020,
      "datetime": 1736365560000
    },
    {
      "open": 23.6674,
      "high": 23.68,
      "low": 23.65,
      "close": 23.68,
      "volume": 5050,
      "datetime": 1736365620000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.65,
      "close": 23.65,
      "volume": 4249,
      "datetime": 1736365680000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 150,
      "datetime": 1736365740000
    },
    {
      "open": 23.64,
      "high": 23.645,
      "low": 23.64,
      "close": 23.64,
      "volume": 520,
      "datetime": 1736365800000
    },
    {
      "open": 23.625,
      "high": 23.625,
      "low": 23.62,
      "close": 23.625,
      "volume": 300,
      "datetime": 1736365860000
    },
    {
      "open": 23.62,
      "high": 23.65,
      "low": 23.62,
      "close": 23.65,
      "volume": 2058,
      "datetime": 1736365920000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 350,
      "datetime": 1736365980000
    },
    {
      "open": 23.67,
      "high": 23.68,
      "low": 23.6688,
      "close": 23.68,
      "volume": 1249,
      "datetime": 1736366040000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.68,
      "close": 23.68,
      "volume": 3431,
      "datetime": 1736366100000
    },
    {
      "open": 23.67,
      "high": 23.67,
      "low": 23.655,
      "close": 23.655,
      "volume": 1471,
      "datetime": 1736366160000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 200,
      "datetime": 1736366220000
    },
    {
      "open": 23.66,
      "high": 23.67,
      "low": 23.66,
      "close": 23.67,
      "volume": 275,
      "datetime": 1736366280000
    },
    {
      "open": 23.67,
      "high": 23.6824,
      "low": 23.67,
      "close": 23.67,
      "volume": 1125,
      "datetime": 1736366400000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.655,
      "close": 23.66,
      "volume": 589,
      "datetime": 1736366460000
    },
    {
      "open": 23.65,
      "high": 23.66,
      "low": 23.65,
      "close": 23.66,
      "volume": 331,
      "datetime": 1736366520000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.64,
      "close": 23.64,
      "volume": 1735,
      "datetime": 1736366580000
    },
    {
      "open": 23.635,
      "high": 23.64,
      "low": 23.635,
      "close": 23.64,
      "volume": 390,
      "datetime": 1736366640000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.64,
      "close": 23.64,
      "volume": 100,
      "datetime": 1736366700000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 900,
      "datetime": 1736366760000
    },
    {
      "open": 23.675,
      "high": 23.68,
      "low": 23.67,
      "close": 23.67,
      "volume": 611,
      "datetime": 1736366820000
    },
    {
      "open": 23.675,
      "high": 23.725,
      "low": 23.675,
      "close": 23.725,
      "volume": 4122,
      "datetime": 1736366880000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 175,
      "datetime": 1736366940000
    },
    {
      "open": 23.74,
      "high": 23.75,
      "low": 23.73,
      "close": 23.75,
      "volume": 3667,
      "datetime": 1736367000000
    },
    {
      "open": 23.77,
      "high": 23.775,
      "low": 23.77,
      "close": 23.77,
      "volume": 466,
      "datetime": 1736367060000
    },
    {
      "open": 23.755,
      "high": 23.78,
      "low": 23.7532,
      "close": 23.78,
      "volume": 2659,
      "datetime": 1736367120000
    },
    {
      "open": 23.77,
      "high": 23.775,
      "low": 23.77,
      "close": 23.775,
      "volume": 475,
      "datetime": 1736367180000
    },
    {
      "open": 23.78,
      "high": 23.79,
      "low": 23.78,
      "close": 23.79,
      "volume": 1016,
      "datetime": 1736367240000
    },
    {
      "open": 23.795,
      "high": 23.795,
      "low": 23.76,
      "close": 23.7655,
      "volume": 8118,
      "datetime": 1736367300000
    },
    {
      "open": 23.785,
      "high": 23.785,
      "low": 23.76,
      "close": 23.76,
      "volume": 2225,
      "datetime": 1736367360000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.77,
      "close": 23.7701,
      "volume": 5615,
      "datetime": 1736367420000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.745,
      "close": 23.745,
      "volume": 2650,
      "datetime": 1736367480000
    },
    {
      "open": 23.74,
      "high": 23.745,
      "low": 23.74,
      "close": 23.745,
      "volume": 4553,
      "datetime": 1736367540000
    },
    {
      "open": 23.755,
      "high": 23.755,
      "low": 23.72,
      "close": 23.72,
      "volume": 2849,
      "datetime": 1736367600000
    },
    {
      "open": 23.75,
      "high": 23.76,
      "low": 23.75,
      "close": 23.75,
      "volume": 3894,
      "datetime": 1736367720000
    },
    {
      "open": 23.745,
      "high": 23.745,
      "low": 23.73,
      "close": 23.73,
      "volume": 1245,
      "datetime": 1736367780000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.7201,
      "close": 23.725,
      "volume": 666,
      "datetime": 1736367840000
    },
    {
      "open": 23.72,
      "high": 23.73,
      "low": 23.72,
      "close": 23.73,
      "volume": 300,
      "datetime": 1736367900000
    },
    {
      "open": 23.73,
      "high": 23.735,
      "low": 23.73,
      "close": 23.73,
      "volume": 1682,
      "datetime": 1736367960000
    },
    {
      "open": 23.73,
      "high": 23.7421,
      "low": 23.72,
      "close": 23.7401,
      "volume": 2156,
      "datetime": 1736368020000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.73,
      "close": 23.73,
      "volume": 1325,
      "datetime": 1736368080000
    },
    {
      "open": 23.71,
      "high": 23.72,
      "low": 23.71,
      "close": 23.72,
      "volume": 1885,
      "datetime": 1736368140000
    },
    {
      "open": 23.72,
      "high": 23.72,
      "low": 23.705,
      "close": 23.705,
      "volume": 1827,
      "datetime": 1736368200000
    },
    {
      "open": 23.6822,
      "high": 23.6822,
      "low": 23.6822,
      "close": 23.6822,
      "volume": 300,
      "datetime": 1736368260000
    },
    {
      "open": 23.675,
      "high": 23.705,
      "low": 23.675,
      "close": 23.705,
      "volume": 6600,
      "datetime": 1736368320000
    },
    {
      "open": 23.718,
      "high": 23.72,
      "low": 23.715,
      "close": 23.72,
      "volume": 700,
      "datetime": 1736368380000
    },
    {
      "open": 23.72,
      "high": 23.72,
      "low": 23.7,
      "close": 23.7,
      "volume": 475,
      "datetime": 1736368440000
    },
    {
      "open": 23.72,
      "high": 23.73,
      "low": 23.72,
      "close": 23.73,
      "volume": 975,
      "datetime": 1736368500000
    },
    {
      "open": 23.74,
      "high": 23.75,
      "low": 23.73,
      "close": 23.73,
      "volume": 1811,
      "datetime": 1736368560000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.6979,
      "close": 23.71,
      "volume": 630,
      "datetime": 1736368620000
    },
    {
      "open": 23.735,
      "high": 23.735,
      "low": 23.735,
      "close": 23.735,
      "volume": 100,
      "datetime": 1736368680000
    },
    {
      "open": 23.735,
      "high": 23.735,
      "low": 23.73,
      "close": 23.73,
      "volume": 450,
      "datetime": 1736368740000
    },
    {
      "open": 23.73,
      "high": 23.73,
      "low": 23.72,
      "close": 23.72,
      "volume": 1864,
      "datetime": 1736368800000
    },
    {
      "open": 23.71,
      "high": 23.725,
      "low": 23.71,
      "close": 23.71,
      "volume": 18704,
      "datetime": 1736368860000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.69,
      "close": 23.69,
      "volume": 1150,
      "datetime": 1736368920000
    },
    {
      "open": 23.6911,
      "high": 23.6976,
      "low": 23.68,
      "close": 23.68,
      "volume": 9931,
      "datetime": 1736368980000
    },
    {
      "open": 23.685,
      "high": 23.685,
      "low": 23.68,
      "close": 23.68,
      "volume": 595,
      "datetime": 1736369040000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.68,
      "close": 23.68,
      "volume": 1600,
      "datetime": 1736369100000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.69,
      "close": 23.69,
      "volume": 100,
      "datetime": 1736369160000
    },
    {
      "open": 23.7,
      "high": 23.73,
      "low": 23.7,
      "close": 23.7298,
      "volume": 2923,
      "datetime": 1736369220000
    },
    {
      "open": 23.7226,
      "high": 23.73,
      "low": 23.7226,
      "close": 23.73,
      "volume": 1200,
      "datetime": 1736369280000
    },
    {
      "open": 23.72,
      "high": 23.735,
      "low": 23.72,
      "close": 23.724,
      "volume": 1000,
      "datetime": 1736369340000
    },
    {
      "open": 23.7135,
      "high": 23.73,
      "low": 23.7135,
      "close": 23.73,
      "volume": 1232,
      "datetime": 1736369400000
    },
    {
      "open": 23.7229,
      "high": 23.7229,
      "low": 23.6895,
      "close": 23.6895,
      "volume": 9930,
      "datetime": 1736369460000
    },
    {
      "open": 23.685,
      "high": 23.69,
      "low": 23.67,
      "close": 23.68,
      "volume": 4087,
      "datetime": 1736369520000
    },
    {
      "open": 23.69,
      "high": 23.7,
      "low": 23.6899,
      "close": 23.69,
      "volume": 8638,
      "datetime": 1736369580000
    },
    {
      "open": 23.685,
      "high": 23.69,
      "low": 23.68,
      "close": 23.69,
      "volume": 2567,
      "datetime": 1736369640000
    },
    {
      "open": 23.7,
      "high": 23.7125,
      "low": 23.7,
      "close": 23.71,
      "volume": 3062,
      "datetime": 1736369700000
    },
    {
      "open": 23.72,
      "high": 23.735,
      "low": 23.72,
      "close": 23.73,
      "volume": 14532,
      "datetime": 1736369760000
    },
    {
      "open": 23.73,
      "high": 23.75,
      "low": 23.73,
      "close": 23.745,
      "volume": 11769,
      "datetime": 1736369820000
    },
    {
      "open": 23.7426,
      "high": 23.745,
      "low": 23.73,
      "close": 23.73,
      "volume": 17737,
      "datetime": 1736369880000
    },
    {
      "open": 23.73,
      "high": 23.775,
      "low": 23.725,
      "close": 23.74,
      "volume": 61848,
      "datetime": 1736369940000
    },
    {
      "open": 23.72,
      "high": 23.72,
      "low": 23.72,
      "close": 23.72,
      "volume": 43777,
      "datetime": 1736370000000
    },
    {
      "open": 23.72,
      "high": 23.76,
      "low": 23.72,
      "close": 23.76,
      "volume": 2211,
      "datetime": 1736370120000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 100,
      "datetime": 1736370480000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.82,
      "close": 23.82,
      "volume": 300,
      "datetime": 1736370540000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.71,
      "close": 23.71,
      "volume": 100,
      "datetime": 1736370600000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.76,
      "close": 23.76,
      "volume": 369,
      "datetime": 1736370720000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.8,
      "close": 23.8,
      "volume": 200,
      "datetime": 1736370960000
    },
    {
      "open": 23.6901,
      "high": 23.6901,
      "low": 23.6901,
      "close": 23.6901,
      "volume": 500,
      "datetime": 1736371080000
    },
    {
      "open": 23.76,
      "high": 23.8,
      "low": 23.76,
      "close": 23.8,
      "volume": 2000,
      "datetime": 1736371140000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 3102,
      "datetime": 1736371440000
    },
    {
      "open": 23.6802,
      "high": 23.69,
      "low": 23.6802,
      "close": 23.69,
      "volume": 306,
      "datetime": 1736371500000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.69,
      "close": 23.69,
      "volume": 981,
      "datetime": 1736371800000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 336,
      "datetime": 1736372100000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 100,
      "datetime": 1736372940000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 198,
      "datetime": 1736373060000
    },
    {
      "open": 23.66,
      "high": 23.66,
      "low": 23.6,
      "close": 23.6,
      "volume": 750,
      "datetime": 1736373180000
    },
    {
      "open": 23.66,
      "high": 23.66,
      "low": 23.6599,
      "close": 23.6599,
      "volume": 412,
      "datetime": 1736373660000
    },
    {
      "open": 23.61,
      "high": 23.61,
      "low": 23.61,
      "close": 23.61,
      "volume": 170,
      "datetime": 1736373900000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 200,
      "datetime": 1736374140000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 1000,
      "datetime": 1736374260000
    },
    {
      "open": 23.5001,
      "high": 23.5001,
      "low": 23.5001,
      "close": 23.5001,
      "volume": 300,
      "datetime": 1736374380000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 150,
      "datetime": 1736375160000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.39,
      "close": 23.39,
      "volume": 506,
      "datetime": 1736375880000
    },
    {
      "open": 23.3682,
      "high": 23.3682,
      "low": 23.3682,
      "close": 23.3682,
      "volume": 418,
      "datetime": 1736376240000
    },
    {
      "open": 23.465,
      "high": 23.465,
      "low": 23.465,
      "close": 23.465,
      "volume": 7000,
      "datetime": 1736376600000
    },
    {
      "open": 23.49,
      "high": 23.52,
      "low": 23.49,
      "close": 23.52,
      "volume": 487,
      "datetime": 1736376960000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.4999,
      "close": 23.4999,
      "volume": 400,
      "datetime": 1736377020000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 200,
      "datetime": 1736377200000
    },
    {
      "open": 23.5794,
      "high": 23.5794,
      "low": 23.5794,
      "close": 23.5794,
      "volume": 2000,
      "datetime": 1736377440000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.52,
      "close": 23.52,
      "volume": 150,
      "datetime": 1736378340000
    },
    {
      "open": 23.4801,
      "high": 23.4801,
      "low": 23.4801,
      "close": 23.4801,
      "volume": 1375,
      "datetime": 1736378820000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 100,
      "datetime": 1736379000000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 100,
      "datetime": 1736379120000
    },
    {
      "open": 23.6099,
      "high": 23.6099,
      "low": 23.6099,
      "close": 23.6099,
      "volume": 206,
      "datetime": 1736379180000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.54,
      "close": 23.54,
      "volume": 400,
      "datetime": 1736380440000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 140,
      "datetime": 1736381160000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 150,
      "datetime": 1736381700000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 125,
      "datetime": 1736383500000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 2369,
      "datetime": 1736383980000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 2000,
      "datetime": 1736384220000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 100,
      "datetime": 1736384280000
    },
    {
      "open": 24,
      "high": 24.03,
      "low": 23.97,
      "close": 24.02,
      "volume": 525,
      "datetime": 1736470800000
    },
    {
      "open": 24.06,
      "high": 24.06,
      "low": 24.06,
      "close": 24.06,
      "volume": 15,
      "datetime": 1736470920000
    },
    {
      "open": 24.02,
      "high": 24.02,
      "low": 24.02,
      "close": 24.02,
      "volume": 25,
      "datetime": 1736471040000
    },
    {
      "open": 24.03,
      "high": 24.03,
      "low": 24.02,
      "close": 24.02,
      "volume": 150,
      "datetime": 1736471160000
    },
    {
      "open": 24,
      "high": 24,
      "low": 24,
      "close": 24,
      "volume": 975,
      "datetime": 1736471220000
    },
    {
      "open": 24.06,
      "high": 24.07,
      "low": 24.06,
      "close": 24.07,
      "volume": 930,
      "datetime": 1736471280000
    },
    {
      "open": 24.05,
      "high": 24.05,
      "low": 24.05,
      "close": 24.05,
      "volume": 44,
      "datetime": 1736471400000
    },
    {
      "open": 24.05,
      "high": 24.05,
      "low": 24.05,
      "close": 24.05,
      "volume": 156,
      "datetime": 1736471640000
    },
    {
      "open": 24.05,
      "high": 24.05,
      "low": 24.05,
      "close": 24.05,
      "volume": 4,
      "datetime": 1736472000000
    },
    {
      "open": 24.05,
      "high": 24.05,
      "low": 24.05,
      "close": 24.05,
      "volume": 6,
      "datetime": 1736472120000
    },
    {
      "open": 24.05,
      "high": 24.05,
      "low": 24.05,
      "close": 24.05,
      "volume": 194,
      "datetime": 1736472300000
    },
    {
      "open": 24.04,
      "high": 24.04,
      "low": 24.04,
      "close": 24.04,
      "volume": 15,
      "datetime": 1736472900000
    },
    {
      "open": 24,
      "high": 24,
      "low": 24,
      "close": 24,
      "volume": 10,
      "datetime": 1736472960000
    },
    {
      "open": 24.02,
      "high": 24.02,
      "low": 24.02,
      "close": 24.02,
      "volume": 400,
      "datetime": 1736473020000
    },
    {
      "open": 24,
      "high": 24,
      "low": 24,
      "close": 24,
      "volume": 500,
      "datetime": 1736473200000
    },
    {
      "open": 24,
      "high": 24,
      "low": 24,
      "close": 24,
      "volume": 500,
      "datetime": 1736473680000
    },
    {
      "open": 23.99,
      "high": 23.99,
      "low": 23.99,
      "close": 23.99,
      "volume": 249,
      "datetime": 1736474100000
    },
    {
      "open": 23.97,
      "high": 23.97,
      "low": 23.97,
      "close": 23.97,
      "volume": 100,
      "datetime": 1736474340000
    },
    {
      "open": 23.94,
      "high": 23.94,
      "low": 23.94,
      "close": 23.94,
      "volume": 4,
      "datetime": 1736474520000
    },
    {
      "open": 23.94,
      "high": 23.98,
      "low": 23.94,
      "close": 23.98,
      "volume": 601,
      "datetime": 1736474640000
    },
    {
      "open": 23.95,
      "high": 23.96,
      "low": 23.95,
      "close": 23.96,
      "volume": 101,
      "datetime": 1736474700000
    },
    {
      "open": 23.95,
      "high": 23.95,
      "low": 23.95,
      "close": 23.95,
      "volume": 25,
      "datetime": 1736475000000
    },
    {
      "open": 23.97,
      "high": 23.97,
      "low": 23.97,
      "close": 23.97,
      "volume": 50,
      "datetime": 1736475120000
    },
    {
      "open": 23.97,
      "high": 23.97,
      "low": 23.97,
      "close": 23.97,
      "volume": 150,
      "datetime": 1736475180000
    },
    {
      "open": 23.99,
      "high": 23.99,
      "low": 23.99,
      "close": 23.99,
      "volume": 20,
      "datetime": 1736475480000
    },
    {
      "open": 23.98,
      "high": 23.98,
      "low": 23.98,
      "close": 23.98,
      "volume": 900,
      "datetime": 1736475540000
    },
    {
      "open": 23.95,
      "high": 23.95,
      "low": 23.95,
      "close": 23.95,
      "volume": 1,
      "datetime": 1736475720000
    },
    {
      "open": 23.9,
      "high": 23.9,
      "low": 23.9,
      "close": 23.9,
      "volume": 10,
      "datetime": 1736476020000
    },
    {
      "open": 23.85,
      "high": 23.85,
      "low": 23.85,
      "close": 23.85,
      "volume": 25,
      "datetime": 1736476200000
    },
    {
      "open": 23.85,
      "high": 23.86,
      "low": 23.85,
      "close": 23.86,
      "volume": 3,
      "datetime": 1736476560000
    },
    {
      "open": 23.91,
      "high": 23.91,
      "low": 23.91,
      "close": 23.91,
      "volume": 50,
      "datetime": 1736477100000
    },
    {
      "open": 23.88,
      "high": 23.88,
      "low": 23.88,
      "close": 23.88,
      "volume": 1,
      "datetime": 1736477820000
    },
    {
      "open": 23.9,
      "high": 23.9,
      "low": 23.9,
      "close": 23.9,
      "volume": 400,
      "datetime": 1736478120000
    },
    {
      "open": 23.88,
      "high": 23.88,
      "low": 23.88,
      "close": 23.88,
      "volume": 7999,
      "datetime": 1736478180000
    },
    {
      "open": 23.9,
      "high": 23.9,
      "low": 23.9,
      "close": 23.9,
      "volume": 2,
      "datetime": 1736478360000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.86,
      "close": 23.86,
      "volume": 1500,
      "datetime": 1736478480000
    },
    {
      "open": 23.91,
      "high": 23.91,
      "low": 23.91,
      "close": 23.91,
      "volume": 1,
      "datetime": 1736479380000
    },
    {
      "open": 23.88,
      "high": 23.88,
      "low": 23.88,
      "close": 23.88,
      "volume": 100,
      "datetime": 1736479680000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.86,
      "close": 23.86,
      "volume": 2,
      "datetime": 1736479740000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.86,
      "close": 23.86,
      "volume": 207,
      "datetime": 1736479800000
    },
    {
      "open": 23.81,
      "high": 23.83,
      "low": 23.81,
      "close": 23.83,
      "volume": 1000,
      "datetime": 1736481240000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.78,
      "close": 23.78,
      "volume": 63,
      "datetime": 1736481600000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.82,
      "close": 23.82,
      "volume": 1000,
      "datetime": 1736481900000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 26,
      "datetime": 1736482260000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.78,
      "close": 23.78,
      "volume": 1,
      "datetime": 1736482380000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.82,
      "close": 23.82,
      "volume": 1,
      "datetime": 1736482680000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.82,
      "close": 23.82,
      "volume": 500,
      "datetime": 1736482860000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 100,
      "datetime": 1736482980000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 501,
      "datetime": 1736483580000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.8,
      "close": 23.8,
      "volume": 1000,
      "datetime": 1736484300000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.78,
      "close": 23.78,
      "volume": 1000,
      "datetime": 1736484480000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.78,
      "close": 23.78,
      "volume": 100,
      "datetime": 1736484840000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.76,
      "close": 23.76,
      "volume": 2024,
      "datetime": 1736485140000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 1306,
      "datetime": 1736485200000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.75,
      "close": 23.75,
      "volume": 6140,
      "datetime": 1736485320000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.76,
      "close": 23.76,
      "volume": 1000,
      "datetime": 1736485740000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 4,
      "datetime": 1736486160000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.76,
      "close": 23.76,
      "volume": 5,
      "datetime": 1736486220000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.78,
      "close": 23.78,
      "volume": 1,
      "datetime": 1736486460000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 10,
      "datetime": 1736487360000
    },
    {
      "open": 23.67,
      "high": 23.67,
      "low": 23.67,
      "close": 23.67,
      "volume": 5,
      "datetime": 1736487900000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 42,
      "datetime": 1736488380000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 588,
      "datetime": 1736488740000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 412,
      "datetime": 1736488800000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 2,
      "datetime": 1736489880000
    },
    {
      "open": 23.73,
      "high": 23.73,
      "low": 23.73,
      "close": 23.73,
      "volume": 1000,
      "datetime": 1736490000000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 10,
      "datetime": 1736490660000
    },
    {
      "open": 23.77,
      "high": 23.77,
      "low": 23.77,
      "close": 23.77,
      "volume": 42,
      "datetime": 1736490720000
    },
    {
      "open": 23.72,
      "high": 23.73,
      "low": 23.72,
      "close": 23.73,
      "volume": 142,
      "datetime": 1736491140000
    },
    {
      "open": 23.67,
      "high": 23.67,
      "low": 23.67,
      "close": 23.67,
      "volume": 200,
      "datetime": 1736492220000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 1,
      "datetime": 1736492400000
    },
    {
      "open": 23.66,
      "high": 23.66,
      "low": 23.66,
      "close": 23.66,
      "volume": 1,
      "datetime": 1736492460000
    },
    {
      "open": 23.72,
      "high": 23.72,
      "low": 23.72,
      "close": 23.72,
      "volume": 2,
      "datetime": 1736492820000
    },
    {
      "open": 23.72,
      "high": 23.72,
      "low": 23.72,
      "close": 23.72,
      "volume": 3,
      "datetime": 1736492880000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 3,
      "datetime": 1736493060000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 100,
      "datetime": 1736493780000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 200,
      "datetime": 1736494380000
    },
    {
      "open": 23.61,
      "high": 23.61,
      "low": 23.6,
      "close": 23.6,
      "volume": 211,
      "datetime": 1736494680000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.5,
      "close": 23.5,
      "volume": 152,
      "datetime": 1736494920000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 1700,
      "datetime": 1736494980000
    },
    {
      "open": 23.49,
      "high": 23.5,
      "low": 23.49,
      "close": 23.5,
      "volume": 6000,
      "datetime": 1736495220000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 2000,
      "datetime": 1736495280000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 300,
      "datetime": 1736495520000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 1000,
      "datetime": 1736495640000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 1000,
      "datetime": 1736495760000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.57,
      "close": 23.57,
      "volume": 4000,
      "datetime": 1736495880000
    },
    {
      "open": 23.61,
      "high": 23.61,
      "low": 23.61,
      "close": 23.61,
      "volume": 1,
      "datetime": 1736496000000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.64,
      "close": 23.64,
      "volume": 2000,
      "datetime": 1736496240000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.54,
      "close": 23.54,
      "volume": 2000,
      "datetime": 1736496420000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.55,
      "close": 23.55,
      "volume": 1,
      "datetime": 1736496840000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.55,
      "close": 23.55,
      "volume": 122,
      "datetime": 1736499660000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.58,
      "close": 23.58,
      "volume": 119,
      "datetime": 1736500500000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 130,
      "datetime": 1736500620000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.54,
      "close": 23.54,
      "volume": 3500,
      "datetime": 1736500800000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.49,
      "close": 23.49,
      "volume": 516,
      "datetime": 1736500860000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 100,
      "datetime": 1736501400000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 3100,
      "datetime": 1736501520000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 864,
      "datetime": 1736501640000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 250,
      "datetime": 1736503500000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.47,
      "close": 23.47,
      "volume": 499,
      "datetime": 1736503560000
    },
    {
      "open": 23.49,
      "high": 23.5,
      "low": 23.49,
      "close": 23.5,
      "volume": 3532,
      "datetime": 1736504100000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 250,
      "datetime": 1736504280000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 1580,
      "datetime": 1736504340000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 100,
      "datetime": 1736506320000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 197,
      "datetime": 1736506380000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 100,
      "datetime": 1736507220000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.45,
      "close": 23.45,
      "volume": 650,
      "datetime": 1736507640000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 100,
      "datetime": 1736507760000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 100,
      "datetime": 1736508420000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.52,
      "close": 23.52,
      "volume": 100,
      "datetime": 1736508480000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 100,
      "datetime": 1736509920000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 100,
      "datetime": 1736510340000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 100,
      "datetime": 1736510400000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.42,
      "close": 23.42,
      "volume": 551,
      "datetime": 1736510700000
    },
    {
      "open": 23.525,
      "high": 23.525,
      "low": 23.525,
      "close": 23.525,
      "volume": 150,
      "datetime": 1736511300000
    },
    {
      "open": 23.5,
      "high": 23.525,
      "low": 23.5,
      "close": 23.525,
      "volume": 2150,
      "datetime": 1736511360000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.53,
      "close": 23.54,
      "volume": 680,
      "datetime": 1736511480000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 328,
      "datetime": 1736511720000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 300,
      "datetime": 1736512140000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 2000,
      "datetime": 1736512200000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.55,
      "close": 23.55,
      "volume": 500,
      "datetime": 1736512500000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 2000,
      "datetime": 1736512680000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 500,
      "datetime": 1736512860000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 250,
      "datetime": 1736512920000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 100,
      "datetime": 1736513100000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 300,
      "datetime": 1736513160000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 117,
      "datetime": 1736513280000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 100,
      "datetime": 1736513400000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 954,
      "datetime": 1736513460000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 100,
      "datetime": 1736513820000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 10496,
      "datetime": 1736513880000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 300,
      "datetime": 1736514000000
    },
    {
      "open": 23.4201,
      "high": 23.4201,
      "low": 23.4201,
      "close": 23.4201,
      "volume": 100,
      "datetime": 1736514060000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 110,
      "datetime": 1736514120000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 1205,
      "datetime": 1736514240000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 1000,
      "datetime": 1736514720000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 727,
      "datetime": 1736514840000
    },
    {
      "open": 23.52,
      "high": 23.55,
      "low": 23.52,
      "close": 23.55,
      "volume": 300,
      "datetime": 1736514900000
    },
    {
      "open": 23.54,
      "high": 23.55,
      "low": 23.51,
      "close": 23.51,
      "volume": 4100,
      "datetime": 1736515020000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 100,
      "datetime": 1736515740000
    },
    {
      "open": 23.55,
      "high": 23.7,
      "low": 23.55,
      "close": 23.7,
      "volume": 5200,
      "datetime": 1736515800000
    },
    {
      "open": 23.89,
      "high": 23.89,
      "low": 23.73,
      "close": 23.85,
      "volume": 4995,
      "datetime": 1736515860000
    },
    {
      "open": 23.69,
      "high": 23.84,
      "low": 23.69,
      "close": 23.77,
      "volume": 1372,
      "datetime": 1736515920000
    },
    {
      "open": 23.81,
      "high": 23.83,
      "low": 23.795,
      "close": 23.83,
      "volume": 1050,
      "datetime": 1736515980000
    },
    {
      "open": 23.8,
      "high": 23.86,
      "low": 23.8,
      "close": 23.8599,
      "volume": 2400,
      "datetime": 1736516040000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.8,
      "close": 23.8099,
      "volume": 82645,
      "datetime": 1736516100000
    },
    {
      "open": 23.77,
      "high": 23.9,
      "low": 23.76,
      "close": 23.9,
      "volume": 4959,
      "datetime": 1736516160000
    },
    {
      "open": 23.9,
      "high": 23.9895,
      "low": 23.9,
      "close": 23.9895,
      "volume": 1300,
      "datetime": 1736516220000
    },
    {
      "open": 23.97,
      "high": 24.02,
      "low": 23.97,
      "close": 24.02,
      "volume": 700,
      "datetime": 1736516280000
    },
    {
      "open": 23.98,
      "high": 24,
      "low": 23.9101,
      "close": 23.99,
      "volume": 2967,
      "datetime": 1736516340000
    },
    {
      "open": 24,
      "high": 24,
      "low": 23.91,
      "close": 23.95,
      "volume": 9189,
      "datetime": 1736516400000
    },
    {
      "open": 23.91,
      "high": 23.92,
      "low": 23.88,
      "close": 23.88,
      "volume": 5400,
      "datetime": 1736516460000
    },
    {
      "open": 23.9,
      "high": 23.91,
      "low": 23.8702,
      "close": 23.9,
      "volume": 3950,
      "datetime": 1736516520000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.84,
      "close": 23.84,
      "volume": 265,
      "datetime": 1736516580000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.76,
      "close": 23.76,
      "volume": 1450,
      "datetime": 1736516640000
    },
    {
      "open": 23.82,
      "high": 23.85,
      "low": 23.82,
      "close": 23.84,
      "volume": 4700,
      "datetime": 1736516700000
    },
    {
      "open": 23.74,
      "high": 23.76,
      "low": 23.74,
      "close": 23.76,
      "volume": 348,
      "datetime": 1736516760000
    },
    {
      "open": 23.8,
      "high": 23.85,
      "low": 23.8,
      "close": 23.85,
      "volume": 2111,
      "datetime": 1736516820000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 1300,
      "datetime": 1736516880000
    },
    {
      "open": 23.88,
      "high": 23.9,
      "low": 23.88,
      "close": 23.9,
      "volume": 300,
      "datetime": 1736516940000
    },
    {
      "open": 23.889,
      "high": 23.889,
      "low": 23.889,
      "close": 23.889,
      "volume": 100,
      "datetime": 1736517000000
    },
    {
      "open": 23.91,
      "high": 23.91,
      "low": 23.895,
      "close": 23.9,
      "volume": 1300,
      "datetime": 1736517060000
    },
    {
      "open": 23.89,
      "high": 23.9,
      "low": 23.79,
      "close": 23.79,
      "volume": 5600,
      "datetime": 1736517180000
    },
    {
      "open": 23.76,
      "high": 23.78,
      "low": 23.76,
      "close": 23.78,
      "volume": 600,
      "datetime": 1736517300000
    },
    {
      "open": 23.78,
      "high": 23.83,
      "low": 23.78,
      "close": 23.83,
      "volume": 800,
      "datetime": 1736517360000
    },
    {
      "open": 23.8183,
      "high": 23.8183,
      "low": 23.79,
      "close": 23.79,
      "volume": 350,
      "datetime": 1736517420000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 477,
      "datetime": 1736517660000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.78,
      "close": 23.78,
      "volume": 450,
      "datetime": 1736517720000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.78,
      "close": 23.78,
      "volume": 15212,
      "datetime": 1736517780000
    },
    {
      "open": 23.8099,
      "high": 23.8099,
      "low": 23.8099,
      "close": 23.8099,
      "volume": 100,
      "datetime": 1736517840000
    },
    {
      "open": 23.79,
      "high": 23.79,
      "low": 23.77,
      "close": 23.77,
      "volume": 348,
      "datetime": 1736517900000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.7599,
      "close": 23.76,
      "volume": 1092,
      "datetime": 1736517960000
    },
    {
      "open": 23.81,
      "high": 23.81,
      "low": 23.8083,
      "close": 23.8083,
      "volume": 1047,
      "datetime": 1736518020000
    },
    {
      "open": 23.68,
      "high": 23.7098,
      "low": 23.68,
      "close": 23.6919,
      "volume": 2200,
      "datetime": 1736518140000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.67,
      "close": 23.67,
      "volume": 8190,
      "datetime": 1736518200000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 200,
      "datetime": 1736518260000
    },
    {
      "open": 23.6501,
      "high": 23.67,
      "low": 23.65,
      "close": 23.65,
      "volume": 2598,
      "datetime": 1736518320000
    },
    {
      "open": 23.63,
      "high": 23.63,
      "low": 23.63,
      "close": 23.63,
      "volume": 100,
      "datetime": 1736518440000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.69,
      "close": 23.69,
      "volume": 100,
      "datetime": 1736518500000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 200,
      "datetime": 1736518560000
    },
    {
      "open": 23.6394,
      "high": 23.6394,
      "low": 23.6394,
      "close": 23.6394,
      "volume": 100,
      "datetime": 1736518620000
    },
    {
      "open": 23.62,
      "high": 23.62,
      "low": 23.62,
      "close": 23.62,
      "volume": 100,
      "datetime": 1736518860000
    },
    {
      "open": 23.61,
      "high": 23.61,
      "low": 23.61,
      "close": 23.61,
      "volume": 200,
      "datetime": 1736519040000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 500,
      "datetime": 1736519100000
    },
    {
      "open": 23.59,
      "high": 23.59,
      "low": 23.59,
      "close": 23.59,
      "volume": 2230,
      "datetime": 1736519340000
    },
    {
      "open": 23.59,
      "high": 23.67,
      "low": 23.59,
      "close": 23.67,
      "volume": 6050,
      "datetime": 1736519400000
    },
    {
      "open": 23.6479,
      "high": 23.7299,
      "low": 23.64,
      "close": 23.6997,
      "volume": 7250,
      "datetime": 1736519460000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.6402,
      "close": 23.6402,
      "volume": 3844,
      "datetime": 1736519520000
    },
    {
      "open": 23.675,
      "high": 23.675,
      "low": 23.6412,
      "close": 23.6412,
      "volume": 1222,
      "datetime": 1736519580000
    },
    {
      "open": 23.63,
      "high": 23.65,
      "low": 23.61,
      "close": 23.61,
      "volume": 3348,
      "datetime": 1736519640000
    },
    {
      "open": 23.6801,
      "high": 23.6801,
      "low": 23.68,
      "close": 23.68,
      "volume": 522,
      "datetime": 1736519700000
    },
    {
      "open": 23.69,
      "high": 23.73,
      "low": 23.69,
      "close": 23.73,
      "volume": 52328,
      "datetime": 1736519760000
    },
    {
      "open": 23.7516,
      "high": 23.805,
      "low": 23.7516,
      "close": 23.8,
      "volume": 16771,
      "datetime": 1736519820000
    },
    {
      "open": 23.82,
      "high": 23.825,
      "low": 23.79,
      "close": 23.79,
      "volume": 14270,
      "datetime": 1736519880000
    },
    {
      "open": 23.79,
      "high": 23.79,
      "low": 23.7554,
      "close": 23.7733,
      "volume": 1500,
      "datetime": 1736519940000
    },
    {
      "open": 23.765,
      "high": 23.7843,
      "low": 23.765,
      "close": 23.77,
      "volume": 1200,
      "datetime": 1736520000000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.73,
      "close": 23.75,
      "volume": 3984,
      "datetime": 1736520060000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.7043,
      "close": 23.71,
      "volume": 2700,
      "datetime": 1736520120000
    },
    {
      "open": 23.683,
      "high": 23.7,
      "low": 23.64,
      "close": 23.65,
      "volume": 2180,
      "datetime": 1736520180000
    },
    {
      "open": 23.6513,
      "high": 23.6798,
      "low": 23.625,
      "close": 23.625,
      "volume": 1189,
      "datetime": 1736520240000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.57,
      "close": 23.57,
      "volume": 1509,
      "datetime": 1736520300000
    },
    {
      "open": 23.57,
      "high": 23.65,
      "low": 23.57,
      "close": 23.65,
      "volume": 3357,
      "datetime": 1736520360000
    },
    {
      "open": 23.72,
      "high": 23.75,
      "low": 23.72,
      "close": 23.75,
      "volume": 4496,
      "datetime": 1736520420000
    },
    {
      "open": 23.7798,
      "high": 23.7798,
      "low": 23.75,
      "close": 23.75,
      "volume": 3440,
      "datetime": 1736520480000
    },
    {
      "open": 23.76,
      "high": 23.79,
      "low": 23.76,
      "close": 23.7899,
      "volume": 6271,
      "datetime": 1736520540000
    },
    {
      "open": 23.778,
      "high": 23.778,
      "low": 23.74,
      "close": 23.74,
      "volume": 1529,
      "datetime": 1736520600000
    },
    {
      "open": 23.7246,
      "high": 23.73,
      "low": 23.7246,
      "close": 23.73,
      "volume": 1093,
      "datetime": 1736520660000
    },
    {
      "open": 23.6999,
      "high": 23.7599,
      "low": 23.6999,
      "close": 23.7599,
      "volume": 9856,
      "datetime": 1736520720000
    },
    {
      "open": 23.72,
      "high": 23.72,
      "low": 23.72,
      "close": 23.72,
      "volume": 100,
      "datetime": 1736520780000
    },
    {
      "open": 23.75,
      "high": 23.7599,
      "low": 23.75,
      "close": 23.7599,
      "volume": 375,
      "datetime": 1736520840000
    },
    {
      "open": 23.7612,
      "high": 23.7612,
      "low": 23.7346,
      "close": 23.74,
      "volume": 2900,
      "datetime": 1736520900000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.682,
      "close": 23.682,
      "volume": 2230,
      "datetime": 1736520960000
    },
    {
      "open": 23.67,
      "high": 23.7,
      "low": 23.6603,
      "close": 23.7,
      "volume": 5877,
      "datetime": 1736521020000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.68,
      "close": 23.69,
      "volume": 344,
      "datetime": 1736521080000
    },
    {
      "open": 23.67,
      "high": 23.6753,
      "low": 23.67,
      "close": 23.6753,
      "volume": 3279,
      "datetime": 1736521140000
    },
    {
      "open": 23.71,
      "high": 23.81,
      "low": 23.705,
      "close": 23.81,
      "volume": 7253,
      "datetime": 1736521200000
    },
    {
      "open": 23.805,
      "high": 23.8196,
      "low": 23.78,
      "close": 23.8196,
      "volume": 1193,
      "datetime": 1736521260000
    },
    {
      "open": 23.8,
      "high": 23.8499,
      "low": 23.8,
      "close": 23.8499,
      "volume": 1775,
      "datetime": 1736521320000
    },
    {
      "open": 23.87,
      "high": 23.885,
      "low": 23.83,
      "close": 23.83,
      "volume": 4025,
      "datetime": 1736521380000
    },
    {
      "open": 23.849,
      "high": 23.879,
      "low": 23.84,
      "close": 23.8699,
      "volume": 16878,
      "datetime": 1736521440000
    },
    {
      "open": 23.82,
      "high": 23.839,
      "low": 23.82,
      "close": 23.831133,
      "volume": 13822,
      "datetime": 1736521500000
    },
    {
      "open": 23.88,
      "high": 23.96,
      "low": 23.88,
      "close": 23.95,
      "volume": 14931,
      "datetime": 1736521560000
    },
    {
      "open": 23.95,
      "high": 23.97,
      "low": 23.93,
      "close": 23.95,
      "volume": 17848,
      "datetime": 1736521620000
    },
    {
      "open": 23.95,
      "high": 23.95,
      "low": 23.94,
      "close": 23.94,
      "volume": 1005,
      "datetime": 1736521680000
    },
    {
      "open": 23.96,
      "high": 24.01,
      "low": 23.96,
      "close": 23.995,
      "volume": 8010,
      "datetime": 1736521740000
    },
    {
      "open": 24.01,
      "high": 24.045,
      "low": 23.98,
      "close": 24.03,
      "volume": 11612,
      "datetime": 1736521800000
    },
    {
      "open": 24.04,
      "high": 24.11,
      "low": 24.035,
      "close": 24.11,
      "volume": 57526,
      "datetime": 1736521860000
    },
    {
      "open": 24.1,
      "high": 24.14,
      "low": 24.08,
      "close": 24.12,
      "volume": 4893,
      "datetime": 1736521920000
    },
    {
      "open": 24.12,
      "high": 24.19,
      "low": 24.1,
      "close": 24.18,
      "volume": 15968,
      "datetime": 1736521980000
    },
    {
      "open": 24.175,
      "high": 24.175,
      "low": 24.13,
      "close": 24.15,
      "volume": 36998,
      "datetime": 1736522040000
    },
    {
      "open": 24.145,
      "high": 24.15,
      "low": 24.1002,
      "close": 24.15,
      "volume": 7789,
      "datetime": 1736522100000
    },
    {
      "open": 24.13,
      "high": 24.1372,
      "low": 24.085,
      "close": 24.085,
      "volume": 10168,
      "datetime": 1736522160000
    },
    {
      "open": 24.0802,
      "high": 24.1,
      "low": 24.075,
      "close": 24.09,
      "volume": 5887,
      "datetime": 1736522220000
    },
    {
      "open": 24.08,
      "high": 24.08,
      "low": 24,
      "close": 24,
      "volume": 64942,
      "datetime": 1736522280000
    },
    {
      "open": 24.005,
      "high": 24.0804,
      "low": 23.963,
      "close": 24.07,
      "volume": 11068,
      "datetime": 1736522340000
    },
    {
      "open": 24.09,
      "high": 24.09,
      "low": 24,
      "close": 24,
      "volume": 7768,
      "datetime": 1736522400000
    },
    {
      "open": 23.985,
      "high": 24.005,
      "low": 23.94,
      "close": 23.955,
      "volume": 6130,
      "datetime": 1736522460000
    },
    {
      "open": 23.951,
      "high": 23.96,
      "low": 23.94,
      "close": 23.96,
      "volume": 15143,
      "datetime": 1736522520000
    },
    {
      "open": 23.96,
      "high": 23.96,
      "low": 23.8932,
      "close": 23.9207,
      "volume": 2109,
      "datetime": 1736522580000
    },
    {
      "open": 23.9,
      "high": 23.9,
      "low": 23.8818,
      "close": 23.8901,
      "volume": 8125,
      "datetime": 1736522640000
    },
    {
      "open": 23.9,
      "high": 23.94,
      "low": 23.89,
      "close": 23.94,
      "volume": 5480,
      "datetime": 1736522700000
    },
    {
      "open": 23.95,
      "high": 24,
      "low": 23.94,
      "close": 23.94,
      "volume": 23437,
      "datetime": 1736522760000
    },
    {
      "open": 23.965,
      "high": 24,
      "low": 23.955,
      "close": 24,
      "volume": 900,
      "datetime": 1736522820000
    },
    {
      "open": 24,
      "high": 24,
      "low": 23.98,
      "close": 23.98,
      "volume": 6954,
      "datetime": 1736522880000
    },
    {
      "open": 23.99,
      "high": 23.99,
      "low": 23.91,
      "close": 23.92,
      "volume": 3000,
      "datetime": 1736522940000
    },
    {
      "open": 23.93,
      "high": 23.96,
      "low": 23.93,
      "close": 23.96,
      "volume": 575,
      "datetime": 1736523000000
    },
    {
      "open": 23.9551,
      "high": 23.9551,
      "low": 23.9203,
      "close": 23.9272,
      "volume": 8001,
      "datetime": 1736523060000
    },
    {
      "open": 23.91,
      "high": 23.93,
      "low": 23.9,
      "close": 23.93,
      "volume": 2325,
      "datetime": 1736523120000
    },
    {
      "open": 23.92,
      "high": 23.92,
      "low": 23.85,
      "close": 23.85,
      "volume": 6227,
      "datetime": 1736523180000
    },
    {
      "open": 23.84,
      "high": 23.88,
      "low": 23.84,
      "close": 23.88,
      "volume": 1084,
      "datetime": 1736523240000
    },
    {
      "open": 23.8951,
      "high": 23.92,
      "low": 23.8951,
      "close": 23.91,
      "volume": 5462,
      "datetime": 1736523300000
    },
    {
      "open": 23.9,
      "high": 23.9,
      "low": 23.89,
      "close": 23.89,
      "volume": 325,
      "datetime": 1736523360000
    },
    {
      "open": 23.87,
      "high": 23.87,
      "low": 23.81,
      "close": 23.81,
      "volume": 7024,
      "datetime": 1736523420000
    },
    {
      "open": 23.81,
      "high": 23.81,
      "low": 23.755,
      "close": 23.77,
      "volume": 3305,
      "datetime": 1736523480000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.725,
      "close": 23.73,
      "volume": 4945,
      "datetime": 1736523540000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.695,
      "close": 23.695,
      "volume": 5366,
      "datetime": 1736523600000
    },
    {
      "open": 23.66,
      "high": 23.66,
      "low": 23.625,
      "close": 23.625,
      "volume": 10464,
      "datetime": 1736523660000
    },
    {
      "open": 23.655,
      "high": 23.69,
      "low": 23.655,
      "close": 23.6851,
      "volume": 3759,
      "datetime": 1736523720000
    },
    {
      "open": 23.71,
      "high": 23.7266,
      "low": 23.68,
      "close": 23.68,
      "volume": 5261,
      "datetime": 1736523780000
    },
    {
      "open": 23.6658,
      "high": 23.705,
      "low": 23.66,
      "close": 23.7,
      "volume": 9326,
      "datetime": 1736523840000
    },
    {
      "open": 23.715,
      "high": 23.72,
      "low": 23.68,
      "close": 23.68,
      "volume": 1240,
      "datetime": 1736523900000
    },
    {
      "open": 23.6837,
      "high": 23.69,
      "low": 23.66,
      "close": 23.67,
      "volume": 5795,
      "datetime": 1736523960000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.59,
      "close": 23.62,
      "volume": 13233,
      "datetime": 1736524020000
    },
    {
      "open": 23.6197,
      "high": 23.6197,
      "low": 23.6,
      "close": 23.6,
      "volume": 623,
      "datetime": 1736524080000
    },
    {
      "open": 23.58,
      "high": 23.5956,
      "low": 23.575,
      "close": 23.5956,
      "volume": 4426,
      "datetime": 1736524140000
    },
    {
      "open": 23.595,
      "high": 23.635,
      "low": 23.595,
      "close": 23.635,
      "volume": 20193,
      "datetime": 1736524200000
    },
    {
      "open": 23.6487,
      "high": 23.65,
      "low": 23.6427,
      "close": 23.645,
      "volume": 1567,
      "datetime": 1736524260000
    },
    {
      "open": 23.65,
      "high": 23.69,
      "low": 23.6496,
      "close": 23.69,
      "volume": 2419,
      "datetime": 1736524320000
    },
    {
      "open": 23.68,
      "high": 23.7,
      "low": 23.67,
      "close": 23.69,
      "volume": 2020,
      "datetime": 1736524380000
    },
    {
      "open": 23.6927,
      "high": 23.71,
      "low": 23.6631,
      "close": 23.71,
      "volume": 4905,
      "datetime": 1736524440000
    },
    {
      "open": 23.705,
      "high": 23.75,
      "low": 23.705,
      "close": 23.75,
      "volume": 574,
      "datetime": 1736524500000
    },
    {
      "open": 23.7658,
      "high": 23.7658,
      "low": 23.725,
      "close": 23.735,
      "volume": 3381,
      "datetime": 1736524560000
    },
    {
      "open": 23.74,
      "high": 23.7626,
      "low": 23.73,
      "close": 23.755,
      "volume": 3229,
      "datetime": 1736524620000
    },
    {
      "open": 23.775,
      "high": 23.775,
      "low": 23.77,
      "close": 23.77,
      "volume": 800,
      "datetime": 1736524680000
    },
    {
      "open": 23.79,
      "high": 23.79,
      "low": 23.785,
      "close": 23.785,
      "volume": 310,
      "datetime": 1736524740000
    },
    {
      "open": 23.788,
      "high": 23.8082,
      "low": 23.78,
      "close": 23.8082,
      "volume": 1802,
      "datetime": 1736524800000
    },
    {
      "open": 23.79,
      "high": 23.845,
      "low": 23.79,
      "close": 23.845,
      "volume": 1375,
      "datetime": 1736524860000
    },
    {
      "open": 23.865,
      "high": 23.87,
      "low": 23.805,
      "close": 23.81,
      "volume": 5528,
      "datetime": 1736524920000
    },
    {
      "open": 23.79,
      "high": 23.795,
      "low": 23.79,
      "close": 23.79,
      "volume": 437,
      "datetime": 1736524980000
    },
    {
      "open": 23.85,
      "high": 23.8704,
      "low": 23.85,
      "close": 23.855,
      "volume": 4522,
      "datetime": 1736525040000
    },
    {
      "open": 23.855,
      "high": 23.885,
      "low": 23.85,
      "close": 23.8704,
      "volume": 4238,
      "datetime": 1736525100000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.815,
      "close": 23.82,
      "volume": 3850,
      "datetime": 1736525160000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.7844,
      "close": 23.8,
      "volume": 2676,
      "datetime": 1736525220000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.85,
      "close": 23.85,
      "volume": 455,
      "datetime": 1736525280000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.86,
      "close": 23.86,
      "volume": 1356,
      "datetime": 1736525340000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.815,
      "close": 23.815,
      "volume": 1425,
      "datetime": 1736525400000
    },
    {
      "open": 23.85,
      "high": 23.85,
      "low": 23.84,
      "close": 23.84,
      "volume": 1225,
      "datetime": 1736525460000
    },
    {
      "open": 23.8201,
      "high": 23.8399,
      "low": 23.8,
      "close": 23.8,
      "volume": 628,
      "datetime": 1736525520000
    },
    {
      "open": 23.8,
      "high": 23.82,
      "low": 23.8,
      "close": 23.81,
      "volume": 1756,
      "datetime": 1736525580000
    },
    {
      "open": 23.815,
      "high": 23.815,
      "low": 23.792,
      "close": 23.8,
      "volume": 650,
      "datetime": 1736525640000
    },
    {
      "open": 23.81,
      "high": 23.81,
      "low": 23.79,
      "close": 23.79,
      "volume": 550,
      "datetime": 1736525700000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.7609,
      "close": 23.7609,
      "volume": 998,
      "datetime": 1736525760000
    },
    {
      "open": 23.75,
      "high": 23.77,
      "low": 23.72,
      "close": 23.77,
      "volume": 6887,
      "datetime": 1736525820000
    },
    {
      "open": 23.76,
      "high": 23.765,
      "low": 23.74,
      "close": 23.74,
      "volume": 2200,
      "datetime": 1736525880000
    },
    {
      "open": 23.74,
      "high": 23.8042,
      "low": 23.74,
      "close": 23.8,
      "volume": 3000,
      "datetime": 1736525940000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.8,
      "close": 23.8,
      "volume": 725,
      "datetime": 1736526000000
    },
    {
      "open": 23.8,
      "high": 23.82,
      "low": 23.7827,
      "close": 23.82,
      "volume": 2658,
      "datetime": 1736526060000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.82,
      "close": 23.8258,
      "volume": 883,
      "datetime": 1736526120000
    },
    {
      "open": 23.83,
      "high": 23.85,
      "low": 23.83,
      "close": 23.85,
      "volume": 1493,
      "datetime": 1736526180000
    },
    {
      "open": 23.8474,
      "high": 23.86,
      "low": 23.8474,
      "close": 23.85,
      "volume": 1550,
      "datetime": 1736526240000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.81,
      "close": 23.82,
      "volume": 425,
      "datetime": 1736526300000
    },
    {
      "open": 23.81,
      "high": 23.82,
      "low": 23.81,
      "close": 23.82,
      "volume": 625,
      "datetime": 1736526360000
    },
    {
      "open": 23.885,
      "high": 23.9,
      "low": 23.885,
      "close": 23.89,
      "volume": 2543,
      "datetime": 1736526420000
    },
    {
      "open": 23.885,
      "high": 23.89,
      "low": 23.8672,
      "close": 23.8672,
      "volume": 4233,
      "datetime": 1736526480000
    },
    {
      "open": 23.8626,
      "high": 23.88,
      "low": 23.8626,
      "close": 23.87,
      "volume": 1350,
      "datetime": 1736526540000
    },
    {
      "open": 23.92,
      "high": 23.92,
      "low": 23.9,
      "close": 23.92,
      "volume": 3864,
      "datetime": 1736526600000
    },
    {
      "open": 23.905,
      "high": 23.905,
      "low": 23.87,
      "close": 23.89,
      "volume": 4244,
      "datetime": 1736526660000
    },
    {
      "open": 23.895,
      "high": 23.93,
      "low": 23.895,
      "close": 23.93,
      "volume": 2675,
      "datetime": 1736526720000
    },
    {
      "open": 23.92,
      "high": 23.92,
      "low": 23.8958,
      "close": 23.8958,
      "volume": 1270,
      "datetime": 1736526780000
    },
    {
      "open": 23.87,
      "high": 23.8759,
      "low": 23.86,
      "close": 23.87,
      "volume": 950,
      "datetime": 1736526840000
    },
    {
      "open": 23.872,
      "high": 23.872,
      "low": 23.845,
      "close": 23.845,
      "volume": 2496,
      "datetime": 1736526900000
    },
    {
      "open": 23.85,
      "high": 23.86,
      "low": 23.84,
      "close": 23.86,
      "volume": 2775,
      "datetime": 1736526960000
    },
    {
      "open": 23.87,
      "high": 23.92,
      "low": 23.87,
      "close": 23.92,
      "volume": 2450,
      "datetime": 1736527020000
    },
    {
      "open": 23.9204,
      "high": 23.945,
      "low": 23.9,
      "close": 23.9,
      "volume": 5460,
      "datetime": 1736527080000
    },
    {
      "open": 23.91,
      "high": 23.92,
      "low": 23.9,
      "close": 23.92,
      "volume": 1680,
      "datetime": 1736527140000
    },
    {
      "open": 23.88,
      "high": 23.88,
      "low": 23.865,
      "close": 23.87,
      "volume": 1200,
      "datetime": 1736527200000
    },
    {
      "open": 23.87,
      "high": 23.87,
      "low": 23.835,
      "close": 23.835,
      "volume": 3625,
      "datetime": 1736527260000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.785,
      "close": 23.79,
      "volume": 2475,
      "datetime": 1736527320000
    },
    {
      "open": 23.7842,
      "high": 23.7842,
      "low": 23.77,
      "close": 23.77,
      "volume": 700,
      "datetime": 1736527380000
    },
    {
      "open": 23.77,
      "high": 23.77,
      "low": 23.72,
      "close": 23.745,
      "volume": 8469,
      "datetime": 1736527440000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.71,
      "close": 23.71,
      "volume": 1225,
      "datetime": 1736527500000
    },
    {
      "open": 23.71,
      "high": 23.72,
      "low": 23.71,
      "close": 23.72,
      "volume": 993,
      "datetime": 1736527560000
    },
    {
      "open": 23.7344,
      "high": 23.75,
      "low": 23.7344,
      "close": 23.75,
      "volume": 5190,
      "datetime": 1736527620000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 1097,
      "datetime": 1736527680000
    },
    {
      "open": 23.73,
      "high": 23.77,
      "low": 23.73,
      "close": 23.77,
      "volume": 1260,
      "datetime": 1736527740000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.75,
      "close": 23.75,
      "volume": 2297,
      "datetime": 1736527800000
    },
    {
      "open": 23.76,
      "high": 23.8,
      "low": 23.76,
      "close": 23.79,
      "volume": 375,
      "datetime": 1736527860000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.73,
      "close": 23.73,
      "volume": 640,
      "datetime": 1736527920000
    },
    {
      "open": 23.72,
      "high": 23.75,
      "low": 23.72,
      "close": 23.74,
      "volume": 775,
      "datetime": 1736527980000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 150,
      "datetime": 1736528040000
    },
    {
      "open": 23.75,
      "high": 23.79,
      "low": 23.75,
      "close": 23.785,
      "volume": 3650,
      "datetime": 1736528100000
    },
    {
      "open": 23.78,
      "high": 23.81,
      "low": 23.78,
      "close": 23.81,
      "volume": 4050,
      "datetime": 1736528160000
    },
    {
      "open": 23.8199,
      "high": 23.825,
      "low": 23.79,
      "close": 23.79,
      "volume": 1698,
      "datetime": 1736528220000
    },
    {
      "open": 23.77,
      "high": 23.77,
      "low": 23.7401,
      "close": 23.75,
      "volume": 5161,
      "datetime": 1736528280000
    },
    {
      "open": 23.76,
      "high": 23.8,
      "low": 23.76,
      "close": 23.8,
      "volume": 835,
      "datetime": 1736528340000
    },
    {
      "open": 23.81,
      "high": 23.8165,
      "low": 23.8,
      "close": 23.8165,
      "volume": 2470,
      "datetime": 1736528400000
    },
    {
      "open": 23.82,
      "high": 23.8399,
      "low": 23.82,
      "close": 23.8399,
      "volume": 500,
      "datetime": 1736528460000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.82,
      "close": 23.82,
      "volume": 1410,
      "datetime": 1736528520000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.7847,
      "close": 23.7847,
      "volume": 4125,
      "datetime": 1736528580000
    },
    {
      "open": 23.8,
      "high": 23.8465,
      "low": 23.8,
      "close": 23.8465,
      "volume": 5465,
      "datetime": 1736528640000
    },
    {
      "open": 23.8435,
      "high": 23.85,
      "low": 23.83,
      "close": 23.83,
      "volume": 665,
      "datetime": 1736528700000
    },
    {
      "open": 23.83,
      "high": 23.83,
      "low": 23.8,
      "close": 23.815,
      "volume": 1964,
      "datetime": 1736528760000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.81,
      "close": 23.81,
      "volume": 475,
      "datetime": 1736528820000
    },
    {
      "open": 23.83,
      "high": 23.87,
      "low": 23.83,
      "close": 23.87,
      "volume": 2737,
      "datetime": 1736528880000
    },
    {
      "open": 23.89,
      "high": 23.89,
      "low": 23.89,
      "close": 23.89,
      "volume": 125,
      "datetime": 1736528940000
    },
    {
      "open": 23.8958,
      "high": 23.8958,
      "low": 23.885,
      "close": 23.886834,
      "volume": 6550,
      "datetime": 1736529000000
    },
    {
      "open": 23.885,
      "high": 23.885,
      "low": 23.84,
      "close": 23.86,
      "volume": 4756,
      "datetime": 1736529060000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.86,
      "close": 23.86,
      "volume": 200,
      "datetime": 1736529120000
    },
    {
      "open": 23.85,
      "high": 23.87,
      "low": 23.85,
      "close": 23.87,
      "volume": 1050,
      "datetime": 1736529180000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.85,
      "close": 23.85,
      "volume": 306,
      "datetime": 1736529240000
    },
    {
      "open": 23.82,
      "high": 23.82,
      "low": 23.81,
      "close": 23.82,
      "volume": 2200,
      "datetime": 1736529300000
    },
    {
      "open": 23.835,
      "high": 23.84,
      "low": 23.8,
      "close": 23.8001,
      "volume": 3650,
      "datetime": 1736529360000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.79,
      "close": 23.8,
      "volume": 525,
      "datetime": 1736529420000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.77,
      "close": 23.775,
      "volume": 4500,
      "datetime": 1736529540000
    },
    {
      "open": 23.76,
      "high": 23.761,
      "low": 23.725,
      "close": 23.74,
      "volume": 6350,
      "datetime": 1736529600000
    },
    {
      "open": 23.73,
      "high": 23.73,
      "low": 23.68,
      "close": 23.685,
      "volume": 20202,
      "datetime": 1736529660000
    },
    {
      "open": 23.68,
      "high": 23.703618,
      "low": 23.68,
      "close": 23.69,
      "volume": 3912,
      "datetime": 1736529720000
    },
    {
      "open": 23.695,
      "high": 23.7,
      "low": 23.67,
      "close": 23.6701,
      "volume": 5504,
      "datetime": 1736529780000
    },
    {
      "open": 23.67,
      "high": 23.6803,
      "low": 23.655,
      "close": 23.655,
      "volume": 1343,
      "datetime": 1736529840000
    },
    {
      "open": 23.6532,
      "high": 23.655,
      "low": 23.64,
      "close": 23.655,
      "volume": 3164,
      "datetime": 1736529900000
    },
    {
      "open": 23.63,
      "high": 23.64,
      "low": 23.63,
      "close": 23.64,
      "volume": 6400,
      "datetime": 1736529960000
    },
    {
      "open": 23.64,
      "high": 23.6428,
      "low": 23.62,
      "close": 23.6302,
      "volume": 2914,
      "datetime": 1736530020000
    },
    {
      "open": 23.63,
      "high": 23.63,
      "low": 23.623,
      "close": 23.63,
      "volume": 2034,
      "datetime": 1736530080000
    },
    {
      "open": 23.63,
      "high": 23.635,
      "low": 23.6103,
      "close": 23.6103,
      "volume": 825,
      "datetime": 1736530140000
    },
    {
      "open": 23.61,
      "high": 23.625,
      "low": 23.61,
      "close": 23.6203,
      "volume": 1775,
      "datetime": 1736530200000
    },
    {
      "open": 23.635,
      "high": 23.635,
      "low": 23.615,
      "close": 23.62,
      "volume": 2976,
      "datetime": 1736530260000
    },
    {
      "open": 23.62,
      "high": 23.6299,
      "low": 23.62,
      "close": 23.6299,
      "volume": 3873,
      "datetime": 1736530320000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.63,
      "close": 23.63,
      "volume": 275,
      "datetime": 1736530380000
    },
    {
      "open": 23.63,
      "high": 23.63,
      "low": 23.6119,
      "close": 23.6119,
      "volume": 1250,
      "datetime": 1736530440000
    },
    {
      "open": 23.63,
      "high": 23.6534,
      "low": 23.625,
      "close": 23.65,
      "volume": 800,
      "datetime": 1736530500000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 864,
      "datetime": 1736530560000
    },
    {
      "open": 23.67,
      "high": 23.67,
      "low": 23.66,
      "close": 23.66,
      "volume": 225,
      "datetime": 1736530620000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.63,
      "close": 23.64,
      "volume": 700,
      "datetime": 1736530680000
    },
    {
      "open": 23.62,
      "high": 23.6301,
      "low": 23.62,
      "close": 23.6301,
      "volume": 675,
      "datetime": 1736530740000
    },
    {
      "open": 23.64,
      "high": 23.65,
      "low": 23.64,
      "close": 23.65,
      "volume": 4945,
      "datetime": 1736530800000
    },
    {
      "open": 23.655,
      "high": 23.655,
      "low": 23.61,
      "close": 23.61,
      "volume": 1050,
      "datetime": 1736530860000
    },
    {
      "open": 23.605,
      "high": 23.605,
      "low": 23.5732,
      "close": 23.58,
      "volume": 8426,
      "datetime": 1736530920000
    },
    {
      "open": 23.58,
      "high": 23.5832,
      "low": 23.56,
      "close": 23.5821,
      "volume": 5795,
      "datetime": 1736530980000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.5933,
      "close": 23.5933,
      "volume": 1250,
      "datetime": 1736531040000
    },
    {
      "open": 23.6,
      "high": 23.635,
      "low": 23.5999,
      "close": 23.63,
      "volume": 1085,
      "datetime": 1736531100000
    },
    {
      "open": 23.63,
      "high": 23.63,
      "low": 23.595,
      "close": 23.595,
      "volume": 2859,
      "datetime": 1736531160000
    },
    {
      "open": 23.5902,
      "high": 23.5902,
      "low": 23.5805,
      "close": 23.5832,
      "volume": 918,
      "datetime": 1736531220000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.52,
      "close": 23.52,
      "volume": 4025,
      "datetime": 1736531280000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.47,
      "close": 23.4803,
      "volume": 9780,
      "datetime": 1736531340000
    },
    {
      "open": 23.49,
      "high": 23.51,
      "low": 23.48,
      "close": 23.5,
      "volume": 1275,
      "datetime": 1736531400000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.455,
      "close": 23.4599,
      "volume": 2084,
      "datetime": 1736531460000
    },
    {
      "open": 23.46,
      "high": 23.475,
      "low": 23.46,
      "close": 23.4701,
      "volume": 4501,
      "datetime": 1736531520000
    },
    {
      "open": 23.475,
      "high": 23.475,
      "low": 23.45,
      "close": 23.45,
      "volume": 4601,
      "datetime": 1736531580000
    },
    {
      "open": 23.4401,
      "high": 23.4401,
      "low": 23.41,
      "close": 23.42,
      "volume": 2974,
      "datetime": 1736531640000
    },
    {
      "open": 23.4241,
      "high": 23.4475,
      "low": 23.42,
      "close": 23.425,
      "volume": 4686,
      "datetime": 1736531700000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.28,
      "close": 23.31,
      "volume": 21711,
      "datetime": 1736531760000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.26,
      "close": 23.26,
      "volume": 9734,
      "datetime": 1736531820000
    },
    {
      "open": 23.25,
      "high": 23.2699,
      "low": 23.23,
      "close": 23.2418,
      "volume": 18065,
      "datetime": 1736531880000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.245,
      "close": 23.26,
      "volume": 2149,
      "datetime": 1736531940000
    },
    {
      "open": 23.245,
      "high": 23.3128,
      "low": 23.245,
      "close": 23.295,
      "volume": 9247,
      "datetime": 1736532000000
    },
    {
      "open": 23.32,
      "high": 23.34,
      "low": 23.3001,
      "close": 23.32,
      "volume": 5817,
      "datetime": 1736532060000
    },
    {
      "open": 23.325,
      "high": 23.3349,
      "low": 23.27,
      "close": 23.27,
      "volume": 9350,
      "datetime": 1736532120000
    },
    {
      "open": 23.26,
      "high": 23.3,
      "low": 23.2576,
      "close": 23.3,
      "volume": 1428,
      "datetime": 1736532180000
    },
    {
      "open": 23.28,
      "high": 23.32,
      "low": 23.28,
      "close": 23.32,
      "volume": 2175,
      "datetime": 1736532240000
    },
    {
      "open": 23.34,
      "high": 23.34,
      "low": 23.3,
      "close": 23.3,
      "volume": 6230,
      "datetime": 1736532300000
    },
    {
      "open": 23.32,
      "high": 23.32,
      "low": 23.26,
      "close": 23.26,
      "volume": 2325,
      "datetime": 1736532360000
    },
    {
      "open": 23.27,
      "high": 23.3,
      "low": 23.27,
      "close": 23.3,
      "volume": 400,
      "datetime": 1736532420000
    },
    {
      "open": 23.29,
      "high": 23.2901,
      "low": 23.2633,
      "close": 23.2633,
      "volume": 11010,
      "datetime": 1736532480000
    },
    {
      "open": 23.27,
      "high": 23.295,
      "low": 23.26,
      "close": 23.29,
      "volume": 3817,
      "datetime": 1736532540000
    },
    {
      "open": 23.29,
      "high": 23.305,
      "low": 23.275,
      "close": 23.275,
      "volume": 4124,
      "datetime": 1736532600000
    },
    {
      "open": 23.275,
      "high": 23.3,
      "low": 23.27,
      "close": 23.27,
      "volume": 14706,
      "datetime": 1736532660000
    },
    {
      "open": 23.29,
      "high": 23.29,
      "low": 23.27,
      "close": 23.27,
      "volume": 1427,
      "datetime": 1736532720000
    },
    {
      "open": 23.29,
      "high": 23.2976,
      "low": 23.265,
      "close": 23.2976,
      "volume": 2025,
      "datetime": 1736532780000
    },
    {
      "open": 23.325,
      "high": 23.33,
      "low": 23.32,
      "close": 23.32,
      "volume": 6436,
      "datetime": 1736532840000
    },
    {
      "open": 23.34,
      "high": 23.36,
      "low": 23.33,
      "close": 23.36,
      "volume": 4750,
      "datetime": 1736532900000
    },
    {
      "open": 23.36,
      "high": 23.38,
      "low": 23.36,
      "close": 23.37,
      "volume": 3463,
      "datetime": 1736532960000
    },
    {
      "open": 23.39,
      "high": 23.39,
      "low": 23.37,
      "close": 23.37,
      "volume": 1901,
      "datetime": 1736533020000
    },
    {
      "open": 23.37,
      "high": 23.37,
      "low": 23.33,
      "close": 23.33,
      "volume": 1225,
      "datetime": 1736533080000
    },
    {
      "open": 23.33,
      "high": 23.34,
      "low": 23.315,
      "close": 23.33,
      "volume": 1861,
      "datetime": 1736533140000
    },
    {
      "open": 23.33,
      "high": 23.35,
      "low": 23.33,
      "close": 23.335,
      "volume": 3500,
      "datetime": 1736533200000
    },
    {
      "open": 23.345,
      "high": 23.4,
      "low": 23.345,
      "close": 23.4,
      "volume": 1019,
      "datetime": 1736533260000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.37,
      "close": 23.37,
      "volume": 2094,
      "datetime": 1736533320000
    },
    {
      "open": 23.3601,
      "high": 23.37,
      "low": 23.34,
      "close": 23.34,
      "volume": 5463,
      "datetime": 1736533380000
    },
    {
      "open": 23.345,
      "high": 23.39,
      "low": 23.345,
      "close": 23.39,
      "volume": 1946,
      "datetime": 1736533440000
    },
    {
      "open": 23.41,
      "high": 23.435,
      "low": 23.41,
      "close": 23.435,
      "volume": 1717,
      "datetime": 1736533500000
    },
    {
      "open": 23.41,
      "high": 23.435,
      "low": 23.41,
      "close": 23.435,
      "volume": 450,
      "datetime": 1736533560000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.45,
      "close": 23.4501,
      "volume": 775,
      "datetime": 1736533620000
    },
    {
      "open": 23.4542,
      "high": 23.47,
      "low": 23.44,
      "close": 23.47,
      "volume": 850,
      "datetime": 1736533680000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.47,
      "close": 23.475,
      "volume": 1075,
      "datetime": 1736533740000
    },
    {
      "open": 23.456511,
      "high": 23.51,
      "low": 23.45,
      "close": 23.51,
      "volume": 2275,
      "datetime": 1736533800000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.49,
      "close": 23.4901,
      "volume": 4168,
      "datetime": 1736533860000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.5,
      "close": 23.5,
      "volume": 721,
      "datetime": 1736533920000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.47,
      "close": 23.47,
      "volume": 1675,
      "datetime": 1736533980000
    },
    {
      "open": 23.465,
      "high": 23.47,
      "low": 23.465,
      "close": 23.47,
      "volume": 775,
      "datetime": 1736534040000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.465,
      "close": 23.465,
      "volume": 1800,
      "datetime": 1736534100000
    },
    {
      "open": 23.48,
      "high": 23.515,
      "low": 23.48,
      "close": 23.515,
      "volume": 2100,
      "datetime": 1736534160000
    },
    {
      "open": 23.51,
      "high": 23.53,
      "low": 23.5,
      "close": 23.5,
      "volume": 4091,
      "datetime": 1736534220000
    },
    {
      "open": 23.5205,
      "high": 23.54,
      "low": 23.5205,
      "close": 23.54,
      "volume": 2709,
      "datetime": 1736534280000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.505,
      "close": 23.505,
      "volume": 1445,
      "datetime": 1736534340000
    },
    {
      "open": 23.49,
      "high": 23.5028,
      "low": 23.49,
      "close": 23.5028,
      "volume": 8774,
      "datetime": 1736534400000
    },
    {
      "open": 23.51,
      "high": 23.53,
      "low": 23.51,
      "close": 23.53,
      "volume": 785,
      "datetime": 1736534460000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.53,
      "close": 23.53,
      "volume": 724,
      "datetime": 1736534520000
    },
    {
      "open": 23.5314,
      "high": 23.54,
      "low": 23.52,
      "close": 23.52,
      "volume": 2032,
      "datetime": 1736534580000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.51,
      "close": 23.52,
      "volume": 1050,
      "datetime": 1736534640000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.4901,
      "close": 23.4901,
      "volume": 750,
      "datetime": 1736534700000
    },
    {
      "open": 23.5,
      "high": 23.51,
      "low": 23.49,
      "close": 23.51,
      "volume": 1800,
      "datetime": 1736534760000
    },
    {
      "open": 23.51,
      "high": 23.53,
      "low": 23.51,
      "close": 23.53,
      "volume": 1100,
      "datetime": 1736534820000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.48,
      "close": 23.4802,
      "volume": 1681,
      "datetime": 1736534880000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.42,
      "close": 23.42,
      "volume": 2350,
      "datetime": 1736534940000
    },
    {
      "open": 23.42,
      "high": 23.45,
      "low": 23.42,
      "close": 23.45,
      "volume": 2055,
      "datetime": 1736535000000
    },
    {
      "open": 23.45,
      "high": 23.49,
      "low": 23.45,
      "close": 23.4688,
      "volume": 1850,
      "datetime": 1736535060000
    },
    {
      "open": 23.4888,
      "high": 23.49,
      "low": 23.48,
      "close": 23.49,
      "volume": 2906,
      "datetime": 1736535120000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.46,
      "close": 23.46,
      "volume": 1040,
      "datetime": 1736535180000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.4332,
      "close": 23.44,
      "volume": 799,
      "datetime": 1736535240000
    },
    {
      "open": 23.4581,
      "high": 23.47,
      "low": 23.45,
      "close": 23.47,
      "volume": 1376,
      "datetime": 1736535300000
    },
    {
      "open": 23.475,
      "high": 23.475,
      "low": 23.475,
      "close": 23.475,
      "volume": 100,
      "datetime": 1736535360000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.4572,
      "close": 23.46,
      "volume": 429,
      "datetime": 1736535420000
    },
    {
      "open": 23.47,
      "high": 23.49,
      "low": 23.47,
      "close": 23.49,
      "volume": 1625,
      "datetime": 1736535480000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 125,
      "datetime": 1736535540000
    },
    {
      "open": 23.475,
      "high": 23.5,
      "low": 23.47,
      "close": 23.5,
      "volume": 835,
      "datetime": 1736535600000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.54,
      "close": 23.54,
      "volume": 200,
      "datetime": 1736535660000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.525,
      "close": 23.53,
      "volume": 945,
      "datetime": 1736535720000
    },
    {
      "open": 23.5,
      "high": 23.51,
      "low": 23.5,
      "close": 23.51,
      "volume": 675,
      "datetime": 1736535780000
    },
    {
      "open": 23.52,
      "high": 23.5342,
      "low": 23.52,
      "close": 23.5342,
      "volume": 1688,
      "datetime": 1736535840000
    },
    {
      "open": 23.54,
      "high": 23.58,
      "low": 23.54,
      "close": 23.56,
      "volume": 1000,
      "datetime": 1736535900000
    },
    {
      "open": 23.56,
      "high": 23.57,
      "low": 23.55,
      "close": 23.55,
      "volume": 2422,
      "datetime": 1736535960000
    },
    {
      "open": 23.565,
      "high": 23.6,
      "low": 23.565,
      "close": 23.58,
      "volume": 800,
      "datetime": 1736536020000
    },
    {
      "open": 23.59,
      "high": 23.595,
      "low": 23.56,
      "close": 23.57,
      "volume": 3225,
      "datetime": 1736536080000
    },
    {
      "open": 23.58,
      "high": 23.59,
      "low": 23.58,
      "close": 23.5899,
      "volume": 300,
      "datetime": 1736536140000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.53,
      "close": 23.53,
      "volume": 3650,
      "datetime": 1736536200000
    },
    {
      "open": 23.52,
      "high": 23.53,
      "low": 23.52,
      "close": 23.53,
      "volume": 500,
      "datetime": 1736536260000
    },
    {
      "open": 23.52,
      "high": 23.54,
      "low": 23.52,
      "close": 23.5316,
      "volume": 8253,
      "datetime": 1736536320000
    },
    {
      "open": 23.52,
      "high": 23.5242,
      "low": 23.52,
      "close": 23.5242,
      "volume": 2456,
      "datetime": 1736536380000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.495,
      "close": 23.51,
      "volume": 4907,
      "datetime": 1736536440000
    },
    {
      "open": 23.51,
      "high": 23.52,
      "low": 23.51,
      "close": 23.52,
      "volume": 350,
      "datetime": 1736536500000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.5,
      "close": 23.5,
      "volume": 1208,
      "datetime": 1736536560000
    },
    {
      "open": 23.47,
      "high": 23.49,
      "low": 23.4657,
      "close": 23.49,
      "volume": 4491,
      "datetime": 1736536620000
    },
    {
      "open": 23.47,
      "high": 23.48,
      "low": 23.46,
      "close": 23.46,
      "volume": 3125,
      "datetime": 1736536680000
    },
    {
      "open": 23.4499,
      "high": 23.48,
      "low": 23.4499,
      "close": 23.48,
      "volume": 1125,
      "datetime": 1736536740000
    },
    {
      "open": 23.48,
      "high": 23.49,
      "low": 23.48,
      "close": 23.48,
      "volume": 425,
      "datetime": 1736536800000
    },
    {
      "open": 23.48,
      "high": 23.4902,
      "low": 23.48,
      "close": 23.4902,
      "volume": 525,
      "datetime": 1736536860000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.47,
      "close": 23.48,
      "volume": 6454,
      "datetime": 1736536920000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.48,
      "close": 23.48,
      "volume": 1750,
      "datetime": 1736536980000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.44,
      "close": 23.44,
      "volume": 1325,
      "datetime": 1736537040000
    },
    {
      "open": 23.44,
      "high": 23.47,
      "low": 23.44,
      "close": 23.47,
      "volume": 350,
      "datetime": 1736537100000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.44,
      "close": 23.44,
      "volume": 300,
      "datetime": 1736537160000
    },
    {
      "open": 23.42,
      "high": 23.425,
      "low": 23.4,
      "close": 23.41,
      "volume": 800,
      "datetime": 1736537220000
    },
    {
      "open": 23.41,
      "high": 23.43,
      "low": 23.41,
      "close": 23.4258,
      "volume": 2092,
      "datetime": 1736537280000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.43,
      "close": 23.44,
      "volume": 700,
      "datetime": 1736537340000
    },
    {
      "open": 23.45,
      "high": 23.46,
      "low": 23.44,
      "close": 23.45,
      "volume": 1350,
      "datetime": 1736537400000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.4328,
      "close": 23.4328,
      "volume": 325,
      "datetime": 1736537460000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.4299,
      "close": 23.43,
      "volume": 650,
      "datetime": 1736537520000
    },
    {
      "open": 23.43,
      "high": 23.45,
      "low": 23.43,
      "close": 23.44,
      "volume": 3200,
      "datetime": 1736537580000
    },
    {
      "open": 23.44,
      "high": 23.45,
      "low": 23.43,
      "close": 23.44,
      "volume": 5894,
      "datetime": 1736537640000
    },
    {
      "open": 23.44,
      "high": 23.45,
      "low": 23.44,
      "close": 23.45,
      "volume": 225,
      "datetime": 1736537700000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.44,
      "close": 23.44,
      "volume": 1459,
      "datetime": 1736537760000
    },
    {
      "open": 23.4333,
      "high": 23.4468,
      "low": 23.42,
      "close": 23.43,
      "volume": 3965,
      "datetime": 1736537820000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.4,
      "close": 23.4,
      "volume": 579,
      "datetime": 1736537880000
    },
    {
      "open": 23.3829,
      "high": 23.395,
      "low": 23.38,
      "close": 23.38,
      "volume": 2950,
      "datetime": 1736537940000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.38,
      "close": 23.38,
      "volume": 325,
      "datetime": 1736538000000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.38,
      "close": 23.38,
      "volume": 244,
      "datetime": 1736538060000
    },
    {
      "open": 23.38,
      "high": 23.42,
      "low": 23.38,
      "close": 23.42,
      "volume": 730,
      "datetime": 1736538120000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.4097,
      "close": 23.4097,
      "volume": 1875,
      "datetime": 1736538180000
    },
    {
      "open": 23.4,
      "high": 23.41,
      "low": 23.3902,
      "close": 23.41,
      "volume": 1577,
      "datetime": 1736538240000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 200,
      "datetime": 1736538300000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.43,
      "close": 23.43,
      "volume": 575,
      "datetime": 1736538360000
    },
    {
      "open": 23.42,
      "high": 23.4299,
      "low": 23.41,
      "close": 23.41,
      "volume": 2061,
      "datetime": 1736538420000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.4,
      "close": 23.4,
      "volume": 1125,
      "datetime": 1736538480000
    },
    {
      "open": 23.38,
      "high": 23.42,
      "low": 23.38,
      "close": 23.42,
      "volume": 1675,
      "datetime": 1736538540000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.4,
      "close": 23.4,
      "volume": 1350,
      "datetime": 1736538600000
    },
    {
      "open": 23.41,
      "high": 23.416,
      "low": 23.41,
      "close": 23.416,
      "volume": 394,
      "datetime": 1736538660000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.42,
      "close": 23.42,
      "volume": 425,
      "datetime": 1736538720000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.39,
      "close": 23.39,
      "volume": 960,
      "datetime": 1736538780000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.38,
      "close": 23.38,
      "volume": 174,
      "datetime": 1736538840000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.35,
      "close": 23.36,
      "volume": 1937,
      "datetime": 1736538900000
    },
    {
      "open": 23.355,
      "high": 23.36,
      "low": 23.35,
      "close": 23.36,
      "volume": 1332,
      "datetime": 1736538960000
    },
    {
      "open": 23.37,
      "high": 23.37,
      "low": 23.36,
      "close": 23.36,
      "volume": 200,
      "datetime": 1736539020000
    },
    {
      "open": 23.37,
      "high": 23.3725,
      "low": 23.37,
      "close": 23.37,
      "volume": 1665,
      "datetime": 1736539140000
    },
    {
      "open": 23.38,
      "high": 23.4,
      "low": 23.38,
      "close": 23.4,
      "volume": 2701,
      "datetime": 1736539200000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.39,
      "close": 23.39,
      "volume": 1003,
      "datetime": 1736539260000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.365,
      "close": 23.365,
      "volume": 790,
      "datetime": 1736539320000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.35,
      "close": 23.35,
      "volume": 250,
      "datetime": 1736539380000
    },
    {
      "open": 23.36,
      "high": 23.38,
      "low": 23.36,
      "close": 23.38,
      "volume": 1900,
      "datetime": 1736539440000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.36,
      "close": 23.36,
      "volume": 525,
      "datetime": 1736539500000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.35,
      "close": 23.35,
      "volume": 225,
      "datetime": 1736539620000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.35,
      "close": 23.35,
      "volume": 600,
      "datetime": 1736539680000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.36,
      "close": 23.36,
      "volume": 496,
      "datetime": 1736539740000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.33,
      "close": 23.33,
      "volume": 2650,
      "datetime": 1736539800000
    },
    {
      "open": 23.33,
      "high": 23.35,
      "low": 23.33,
      "close": 23.35,
      "volume": 4799,
      "datetime": 1736539860000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.35,
      "close": 23.355,
      "volume": 5872,
      "datetime": 1736539920000
    },
    {
      "open": 23.3589,
      "high": 23.37,
      "low": 23.3589,
      "close": 23.37,
      "volume": 3785,
      "datetime": 1736539980000
    },
    {
      "open": 23.37,
      "high": 23.4,
      "low": 23.365,
      "close": 23.4,
      "volume": 1224,
      "datetime": 1736540040000
    },
    {
      "open": 23.4,
      "high": 23.42,
      "low": 23.4,
      "close": 23.42,
      "volume": 719,
      "datetime": 1736540100000
    },
    {
      "open": 23.42,
      "high": 23.45,
      "low": 23.42,
      "close": 23.45,
      "volume": 1450,
      "datetime": 1736540160000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.45,
      "close": 23.45,
      "volume": 684,
      "datetime": 1736540220000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 625,
      "datetime": 1736540280000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 150,
      "datetime": 1736540340000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.44,
      "close": 23.44,
      "volume": 650,
      "datetime": 1736540400000
    },
    {
      "open": 23.43,
      "high": 23.45,
      "low": 23.43,
      "close": 23.44,
      "volume": 625,
      "datetime": 1736540460000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.4499,
      "close": 23.4499,
      "volume": 300,
      "datetime": 1736540520000
    },
    {
      "open": 23.445,
      "high": 23.4472,
      "low": 23.44,
      "close": 23.44,
      "volume": 675,
      "datetime": 1736540580000
    },
    {
      "open": 23.43,
      "high": 23.45,
      "low": 23.43,
      "close": 23.45,
      "volume": 761,
      "datetime": 1736540640000
    },
    {
      "open": 23.46,
      "high": 23.4721,
      "low": 23.46,
      "close": 23.47,
      "volume": 1423,
      "datetime": 1736540700000
    },
    {
      "open": 23.47,
      "high": 23.4899,
      "low": 23.4699,
      "close": 23.48,
      "volume": 8378,
      "datetime": 1736540760000
    },
    {
      "open": 23.4824,
      "high": 23.49,
      "low": 23.48,
      "close": 23.48,
      "volume": 625,
      "datetime": 1736540820000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.47,
      "close": 23.47,
      "volume": 1421,
      "datetime": 1736540880000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.46,
      "close": 23.46,
      "volume": 6121,
      "datetime": 1736540940000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.45,
      "close": 23.45,
      "volume": 3325,
      "datetime": 1736541000000
    },
    {
      "open": 23.49,
      "high": 23.5064,
      "low": 23.49,
      "close": 23.5064,
      "volume": 544,
      "datetime": 1736541060000
    },
    {
      "open": 23.49,
      "high": 23.515,
      "low": 23.49,
      "close": 23.515,
      "volume": 275,
      "datetime": 1736541120000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 100,
      "datetime": 1736541180000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 750,
      "datetime": 1736541240000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.47,
      "close": 23.47,
      "volume": 4560,
      "datetime": 1736541300000
    },
    {
      "open": 23.5099,
      "high": 23.51,
      "low": 23.5099,
      "close": 23.51,
      "volume": 350,
      "datetime": 1736541360000
    },
    {
      "open": 23.505,
      "high": 23.5171,
      "low": 23.4954,
      "close": 23.5,
      "volume": 1420,
      "datetime": 1736541420000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.47,
      "close": 23.4766,
      "volume": 2642,
      "datetime": 1736541480000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 100,
      "datetime": 1736541540000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.5,
      "close": 23.5,
      "volume": 650,
      "datetime": 1736541600000
    },
    {
      "open": 23.5,
      "high": 23.53,
      "low": 23.5,
      "close": 23.53,
      "volume": 200,
      "datetime": 1736541660000
    },
    {
      "open": 23.54,
      "high": 23.5534,
      "low": 23.5201,
      "close": 23.5201,
      "volume": 5137,
      "datetime": 1736541720000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.5,
      "close": 23.5,
      "volume": 822,
      "datetime": 1736541780000
    },
    {
      "open": 23.5075,
      "high": 23.5102,
      "low": 23.5075,
      "close": 23.5102,
      "volume": 211,
      "datetime": 1736541840000
    },
    {
      "open": 23.52,
      "high": 23.53,
      "low": 23.52,
      "close": 23.53,
      "volume": 200,
      "datetime": 1736541900000
    },
    {
      "open": 23.5388,
      "high": 23.54,
      "low": 23.51,
      "close": 23.51,
      "volume": 4725,
      "datetime": 1736541960000
    },
    {
      "open": 23.5,
      "high": 23.51,
      "low": 23.495,
      "close": 23.5,
      "volume": 902,
      "datetime": 1736542020000
    },
    {
      "open": 23.495,
      "high": 23.52,
      "low": 23.495,
      "close": 23.52,
      "volume": 2150,
      "datetime": 1736542080000
    },
    {
      "open": 23.51,
      "high": 23.52,
      "low": 23.5,
      "close": 23.52,
      "volume": 1475,
      "datetime": 1736542140000
    },
    {
      "open": 23.535,
      "high": 23.535,
      "low": 23.51,
      "close": 23.51,
      "volume": 900,
      "datetime": 1736542200000
    },
    {
      "open": 23.505,
      "high": 23.52,
      "low": 23.495,
      "close": 23.52,
      "volume": 10672,
      "datetime": 1736542260000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.485,
      "close": 23.49,
      "volume": 2348,
      "datetime": 1736542320000
    },
    {
      "open": 23.5,
      "high": 23.515,
      "low": 23.5,
      "close": 23.51,
      "volume": 3380,
      "datetime": 1736542380000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.4658,
      "close": 23.47,
      "volume": 3349,
      "datetime": 1736542440000
    },
    {
      "open": 23.47,
      "high": 23.51,
      "low": 23.47,
      "close": 23.51,
      "volume": 3471,
      "datetime": 1736542500000
    },
    {
      "open": 23.51,
      "high": 23.5173,
      "low": 23.51,
      "close": 23.515,
      "volume": 2129,
      "datetime": 1736542560000
    },
    {
      "open": 23.5133,
      "high": 23.52,
      "low": 23.5,
      "close": 23.5,
      "volume": 11846,
      "datetime": 1736542620000
    },
    {
      "open": 23.515,
      "high": 23.52,
      "low": 23.51,
      "close": 23.51,
      "volume": 11884,
      "datetime": 1736542680000
    },
    {
      "open": 23.5,
      "high": 23.54,
      "low": 23.5,
      "close": 23.53,
      "volume": 77168,
      "datetime": 1736542740000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 91095,
      "datetime": 1736542800000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 100,
      "datetime": 1736543160000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 4500,
      "datetime": 1736543280000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.5,
      "close": 23.5,
      "volume": 710,
      "datetime": 1736543340000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 5000,
      "datetime": 1736543760000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 100,
      "datetime": 1736544360000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 111,
      "datetime": 1736544660000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 100,
      "datetime": 1736544960000
    },
    {
      "open": 23.5486,
      "high": 23.5486,
      "low": 23.5486,
      "close": 23.5486,
      "volume": 998,
      "datetime": 1736545200000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 1000,
      "datetime": 1736545680000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 249,
      "datetime": 1736547780000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 1299,
      "datetime": 1736548800000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 4063,
      "datetime": 1736549100000
    },
    {
      "open": 23.46,
      "high": 23.54,
      "low": 23.46,
      "close": 23.54,
      "volume": 695,
      "datetime": 1736549700000
    },
    {
      "open": 23.5,
      "high": 23.61,
      "low": 23.5,
      "close": 23.61,
      "volume": 918,
      "datetime": 1736550060000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 704,
      "datetime": 1736551860000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 4500,
      "datetime": 1736552940000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 500,
      "datetime": 1736553780000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 2123,
      "datetime": 1736554080000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 1000,
      "datetime": 1736554140000
    },
    {
      "open": 23.5015,
      "high": 23.5015,
      "low": 23.5015,
      "close": 23.5015,
      "volume": 998,
      "datetime": 1736554200000
    },
    {
      "open": 23.59,
      "high": 23.59,
      "low": 23.59,
      "close": 23.59,
      "volume": 100,
      "datetime": 1736555400000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.57,
      "close": 23.57,
      "volume": 229,
      "datetime": 1736556180000
    },
    {
      "open": 23.6198,
      "high": 23.6198,
      "low": 23.6198,
      "close": 23.6198,
      "volume": 4230,
      "datetime": 1736556360000
    },
    {
      "open": 23.6194,
      "high": 23.6194,
      "low": 23.6187,
      "close": 23.6187,
      "volume": 250,
      "datetime": 1736556420000
    },
    {
      "open": 23.62,
      "high": 23.62,
      "low": 23.62,
      "close": 23.62,
      "volume": 100,
      "datetime": 1736556480000
    },
    {
      "open": 23.6183,
      "high": 23.6183,
      "low": 23.6183,
      "close": 23.6183,
      "volume": 500,
      "datetime": 1736556540000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.58,
      "close": 23.58,
      "volume": 2400,
      "datetime": 1736556720000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 300,
      "datetime": 1736556840000
    },
    {
      "open": 23.4,
      "high": 23.45,
      "low": 23.24,
      "close": 23.45,
      "volume": 106,
      "datetime": 1736730000000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 10,
      "datetime": 1736730060000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 1000,
      "datetime": 1736730180000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 1900,
      "datetime": 1736730300000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.35,
      "close": 23.35,
      "volume": 15,
      "datetime": 1736730360000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 3,
      "datetime": 1736731080000
    },
    {
      "open": 23.45,
      "high": 23.5,
      "low": 23.45,
      "close": 23.5,
      "volume": 250,
      "datetime": 1736731380000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 400,
      "datetime": 1736731500000
    },
    {
      "open": 23.39,
      "high": 23.39,
      "low": 23.39,
      "close": 23.39,
      "volume": 2500,
      "datetime": 1736731560000
    },
    {
      "open": 23.41,
      "high": 23.42,
      "low": 23.41,
      "close": 23.42,
      "volume": 1600,
      "datetime": 1736731860000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 300,
      "datetime": 1736732220000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 1,
      "datetime": 1736732400000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.57,
      "close": 23.57,
      "volume": 1,
      "datetime": 1736732820000
    },
    {
      "open": 23.68,
      "high": 23.69,
      "low": 23.68,
      "close": 23.69,
      "volume": 100,
      "datetime": 1736733120000
    },
    {
      "open": 23.68,
      "high": 23.69,
      "low": 23.68,
      "close": 23.69,
      "volume": 440,
      "datetime": 1736733240000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 2,
      "datetime": 1736733360000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 80,
      "datetime": 1736733480000
    },
    {
      "open": 23.66,
      "high": 23.69,
      "low": 23.65,
      "close": 23.65,
      "volume": 130,
      "datetime": 1736733660000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 4,
      "datetime": 1736733900000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 20,
      "datetime": 1736734260000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 20,
      "datetime": 1736734620000
    },
    {
      "open": 23.72,
      "high": 23.72,
      "low": 23.72,
      "close": 23.72,
      "volume": 380,
      "datetime": 1736736300000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.76,
      "close": 23.76,
      "volume": 4,
      "datetime": 1736736540000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.74,
      "close": 23.74,
      "volume": 400,
      "datetime": 1736736600000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 5,
      "datetime": 1736736780000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 50,
      "datetime": 1736736840000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 1,
      "datetime": 1736737020000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.69,
      "close": 23.69,
      "volume": 4,
      "datetime": 1736737140000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 300,
      "datetime": 1736737260000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 25,
      "datetime": 1736737320000
    },
    {
      "open": 23.65,
      "high": 23.67,
      "low": 23.65,
      "close": 23.67,
      "volume": 1000,
      "datetime": 1736738460000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 1,
      "datetime": 1736738580000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 227,
      "datetime": 1736738700000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 1,
      "datetime": 1736739240000
    },
    {
      "open": 23.63,
      "high": 23.65,
      "low": 23.63,
      "close": 23.65,
      "volume": 702,
      "datetime": 1736739360000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 1600,
      "datetime": 1736740020000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.71,
      "close": 23.71,
      "volume": 322,
      "datetime": 1736740200000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 10,
      "datetime": 1736740440000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 5,
      "datetime": 1736740620000
    },
    {
      "open": 23.68,
      "high": 23.68,
      "low": 23.68,
      "close": 23.68,
      "volume": 25,
      "datetime": 1736740920000
    },
    {
      "open": 23.61,
      "high": 23.61,
      "low": 23.6,
      "close": 23.6,
      "volume": 1600,
      "datetime": 1736741280000
    },
    {
      "open": 23.61,
      "high": 23.61,
      "low": 23.61,
      "close": 23.61,
      "volume": 25,
      "datetime": 1736741460000
    },
    {
      "open": 23.54,
      "high": 23.54,
      "low": 23.51,
      "close": 23.51,
      "volume": 267,
      "datetime": 1736742300000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 322,
      "datetime": 1736742360000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 200,
      "datetime": 1736742420000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 4,
      "datetime": 1736742660000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 100,
      "datetime": 1736742720000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 84,
      "datetime": 1736742780000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 21,
      "datetime": 1736742900000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 50,
      "datetime": 1736743440000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.58,
      "close": 23.58,
      "volume": 50,
      "datetime": 1736743500000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.71,
      "close": 23.71,
      "volume": 4,
      "datetime": 1736745960000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 4,
      "datetime": 1736746260000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 100,
      "datetime": 1736746320000
    },
    {
      "open": 23.71,
      "high": 23.71,
      "low": 23.71,
      "close": 23.71,
      "volume": 50,
      "datetime": 1736746440000
    },
    {
      "open": 23.66,
      "high": 23.66,
      "low": 23.66,
      "close": 23.66,
      "volume": 25,
      "datetime": 1736746500000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.69,
      "close": 23.69,
      "volume": 100,
      "datetime": 1736746860000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.69,
      "close": 23.69,
      "volume": 25,
      "datetime": 1736748120000
    },
    {
      "open": 23.73,
      "high": 23.73,
      "low": 23.73,
      "close": 23.73,
      "volume": 100,
      "datetime": 1736749860000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 100,
      "datetime": 1736749980000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 30,
      "datetime": 1736750040000
    },
    {
      "open": 23.79,
      "high": 23.79,
      "low": 23.79,
      "close": 23.79,
      "volume": 20,
      "datetime": 1736750280000
    },
    {
      "open": 23.77,
      "high": 23.77,
      "low": 23.77,
      "close": 23.77,
      "volume": 50,
      "datetime": 1736750340000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.78,
      "close": 23.78,
      "volume": 50,
      "datetime": 1736750460000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.78,
      "close": 23.78,
      "volume": 50,
      "datetime": 1736750700000
    },
    {
      "open": 23.9,
      "high": 23.96,
      "low": 23.9,
      "close": 23.96,
      "volume": 501,
      "datetime": 1736750820000
    },
    {
      "open": 23.92,
      "high": 23.92,
      "low": 23.92,
      "close": 23.92,
      "volume": 400,
      "datetime": 1736751000000
    },
    {
      "open": 23.93,
      "high": 23.93,
      "low": 23.93,
      "close": 23.93,
      "volume": 50,
      "datetime": 1736751120000
    },
    {
      "open": 23.86,
      "high": 23.86,
      "low": 23.86,
      "close": 23.86,
      "volume": 25,
      "datetime": 1736751360000
    },
    {
      "open": 23.78,
      "high": 23.78,
      "low": 23.78,
      "close": 23.78,
      "volume": 500,
      "datetime": 1736751720000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 88,
      "datetime": 1736751900000
    },
    {
      "open": 23.85,
      "high": 23.85,
      "low": 23.85,
      "close": 23.85,
      "volume": 67,
      "datetime": 1736753520000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.8,
      "close": 23.8,
      "volume": 2,
      "datetime": 1736753700000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.8,
      "close": 23.8,
      "volume": 1,
      "datetime": 1736754060000
    },
    {
      "open": 23.84,
      "high": 23.85,
      "low": 23.84,
      "close": 23.85,
      "volume": 500,
      "datetime": 1736754780000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 500,
      "datetime": 1736754960000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 500,
      "datetime": 1736755020000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 70,
      "datetime": 1736755200000
    },
    {
      "open": 23.9,
      "high": 23.9,
      "low": 23.9,
      "close": 23.9,
      "volume": 1,
      "datetime": 1736755980000
    },
    {
      "open": 23.93,
      "high": 23.93,
      "low": 23.93,
      "close": 23.93,
      "volume": 25,
      "datetime": 1736756460000
    },
    {
      "open": 24,
      "high": 24,
      "low": 24,
      "close": 24,
      "volume": 211,
      "datetime": 1736756580000
    },
    {
      "open": 23.97,
      "high": 23.97,
      "low": 23.97,
      "close": 23.97,
      "volume": 5,
      "datetime": 1736756640000
    },
    {
      "open": 23.97,
      "high": 23.97,
      "low": 23.97,
      "close": 23.97,
      "volume": 12,
      "datetime": 1736757000000
    },
    {
      "open": 23.97,
      "high": 23.97,
      "low": 23.97,
      "close": 23.97,
      "volume": 2,
      "datetime": 1736758140000
    },
    {
      "open": 24.01,
      "high": 24.01,
      "low": 24.01,
      "close": 24.01,
      "volume": 100,
      "datetime": 1736758800000
    },
    {
      "open": 23.97,
      "high": 23.97,
      "low": 23.97,
      "close": 23.97,
      "volume": 11654,
      "datetime": 1736759040000
    },
    {
      "open": 24,
      "high": 24,
      "low": 24,
      "close": 24,
      "volume": 1500,
      "datetime": 1736759100000
    },
    {
      "open": 23.99,
      "high": 23.99,
      "low": 23.99,
      "close": 23.99,
      "volume": 100,
      "datetime": 1736759340000
    },
    {
      "open": 23.96,
      "high": 24,
      "low": 23.96,
      "close": 24,
      "volume": 2655,
      "datetime": 1736759520000
    },
    {
      "open": 23.99,
      "high": 23.99,
      "low": 23.99,
      "close": 23.99,
      "volume": 500,
      "datetime": 1736759580000
    },
    {
      "open": 24,
      "high": 24.02,
      "low": 24,
      "close": 24.02,
      "volume": 805,
      "datetime": 1736759700000
    },
    {
      "open": 24.045,
      "high": 24.045,
      "low": 24,
      "close": 24,
      "volume": 425,
      "datetime": 1736759820000
    },
    {
      "open": 24.07,
      "high": 24.07,
      "low": 24.07,
      "close": 24.07,
      "volume": 250,
      "datetime": 1736760300000
    },
    {
      "open": 24.01,
      "high": 24.01,
      "low": 24.01,
      "close": 24.01,
      "volume": 1239,
      "datetime": 1736760360000
    },
    {
      "open": 24.06,
      "high": 24.06,
      "low": 24.06,
      "close": 24.06,
      "volume": 100,
      "datetime": 1736760420000
    },
    {
      "open": 24.08,
      "high": 24.12,
      "low": 24.08,
      "close": 24.12,
      "volume": 10500,
      "datetime": 1736760600000
    },
    {
      "open": 24.05,
      "high": 24.05,
      "low": 24.05,
      "close": 24.05,
      "volume": 500,
      "datetime": 1736760660000
    },
    {
      "open": 24.12,
      "high": 24.12,
      "low": 24.12,
      "close": 24.12,
      "volume": 500,
      "datetime": 1736760780000
    },
    {
      "open": 24.06,
      "high": 24.06,
      "low": 24.06,
      "close": 24.06,
      "volume": 200,
      "datetime": 1736760900000
    },
    {
      "open": 24.02,
      "high": 24.02,
      "low": 24.02,
      "close": 24.02,
      "volume": 300,
      "datetime": 1736760960000
    },
    {
      "open": 24.01,
      "high": 24.01,
      "low": 24.01,
      "close": 24.01,
      "volume": 167,
      "datetime": 1736761020000
    },
    {
      "open": 23.98,
      "high": 23.98,
      "low": 23.98,
      "close": 23.98,
      "volume": 100,
      "datetime": 1736761500000
    },
    {
      "open": 24.04,
      "high": 24.04,
      "low": 24.04,
      "close": 24.04,
      "volume": 414,
      "datetime": 1736761980000
    },
    {
      "open": 24.045,
      "high": 24.045,
      "low": 24.045,
      "close": 24.045,
      "volume": 590,
      "datetime": 1736762700000
    },
    {
      "open": 24.1,
      "high": 24.1,
      "low": 24.1,
      "close": 24.1,
      "volume": 400,
      "datetime": 1736763120000
    },
    {
      "open": 24.08,
      "high": 24.08,
      "low": 24.08,
      "close": 24.08,
      "volume": 100,
      "datetime": 1736763180000
    },
    {
      "open": 24.11,
      "high": 24.11,
      "low": 24.11,
      "close": 24.11,
      "volume": 100,
      "datetime": 1736763300000
    },
    {
      "open": 24.19,
      "high": 24.19,
      "low": 24.19,
      "close": 24.19,
      "volume": 400,
      "datetime": 1736763540000
    },
    {
      "open": 24.21,
      "high": 24.22,
      "low": 24.21,
      "close": 24.22,
      "volume": 4104,
      "datetime": 1736763720000
    },
    {
      "open": 24.19,
      "high": 24.22,
      "low": 24.19,
      "close": 24.22,
      "volume": 1290,
      "datetime": 1736763780000
    },
    {
      "open": 24.24,
      "high": 24.24,
      "low": 24.24,
      "close": 24.24,
      "volume": 100,
      "datetime": 1736763840000
    },
    {
      "open": 24.29,
      "high": 24.29,
      "low": 24.29,
      "close": 24.29,
      "volume": 9600,
      "datetime": 1736764200000
    },
    {
      "open": 24.29,
      "high": 24.29,
      "low": 24.29,
      "close": 24.29,
      "volume": 100,
      "datetime": 1736764560000
    },
    {
      "open": 24.3,
      "high": 24.3,
      "low": 24.3,
      "close": 24.3,
      "volume": 2400,
      "datetime": 1736764620000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.32,
      "close": 24.32,
      "volume": 100,
      "datetime": 1736764920000
    },
    {
      "open": 24.37,
      "high": 24.37,
      "low": 24.37,
      "close": 24.37,
      "volume": 485,
      "datetime": 1736764980000
    },
    {
      "open": 24.37,
      "high": 24.37,
      "low": 24.37,
      "close": 24.37,
      "volume": 250,
      "datetime": 1736765040000
    },
    {
      "open": 24.37,
      "high": 24.37,
      "low": 24.34,
      "close": 24.35,
      "volume": 7908,
      "datetime": 1736765220000
    },
    {
      "open": 24.41,
      "high": 24.41,
      "low": 24.41,
      "close": 24.41,
      "volume": 247,
      "datetime": 1736765460000
    },
    {
      "open": 24.4,
      "high": 24.4,
      "low": 24.4,
      "close": 24.4,
      "volume": 300,
      "datetime": 1736765520000
    },
    {
      "open": 24.42,
      "high": 24.42,
      "low": 24.42,
      "close": 24.42,
      "volume": 500,
      "datetime": 1736765640000
    },
    {
      "open": 24.42,
      "high": 24.42,
      "low": 24.42,
      "close": 24.42,
      "volume": 129,
      "datetime": 1736765700000
    },
    {
      "open": 24.4,
      "high": 24.4,
      "low": 24.37,
      "close": 24.37,
      "volume": 2400,
      "datetime": 1736765760000
    },
    {
      "open": 24.4,
      "high": 24.4,
      "low": 24.37,
      "close": 24.37,
      "volume": 1210,
      "datetime": 1736765820000
    },
    {
      "open": 24.29,
      "high": 24.29,
      "low": 24.29,
      "close": 24.29,
      "volume": 758,
      "datetime": 1736765880000
    },
    {
      "open": 24.32,
      "high": 24.35,
      "low": 24.32,
      "close": 24.35,
      "volume": 776,
      "datetime": 1736766000000
    },
    {
      "open": 24.33,
      "high": 24.33,
      "low": 24.32,
      "close": 24.32,
      "volume": 5416,
      "datetime": 1736766180000
    },
    {
      "open": 24.37,
      "high": 24.37,
      "low": 24.37,
      "close": 24.37,
      "volume": 340,
      "datetime": 1736766240000
    },
    {
      "open": 24.41,
      "high": 24.41,
      "low": 24.41,
      "close": 24.41,
      "volume": 250,
      "datetime": 1736766900000
    },
    {
      "open": 24.41,
      "high": 24.42,
      "low": 24.41,
      "close": 24.42,
      "volume": 2600,
      "datetime": 1736767080000
    },
    {
      "open": 24.38,
      "high": 24.38,
      "low": 24.38,
      "close": 24.38,
      "volume": 1000,
      "datetime": 1736767260000
    },
    {
      "open": 24.38,
      "high": 24.38,
      "low": 24.38,
      "close": 24.38,
      "volume": 178,
      "datetime": 1736767560000
    },
    {
      "open": 24.41,
      "high": 24.41,
      "low": 24.41,
      "close": 24.41,
      "volume": 153,
      "datetime": 1736767680000
    },
    {
      "open": 24.41,
      "high": 24.41,
      "low": 24.41,
      "close": 24.41,
      "volume": 286,
      "datetime": 1736767800000
    },
    {
      "open": 24.38,
      "high": 24.38,
      "low": 24.38,
      "close": 24.38,
      "volume": 600,
      "datetime": 1736767860000
    },
    {
      "open": 24.41,
      "high": 24.42,
      "low": 24.41,
      "close": 24.42,
      "volume": 250,
      "datetime": 1736767920000
    },
    {
      "open": 24.43,
      "high": 24.43,
      "low": 24.42,
      "close": 24.42,
      "volume": 350,
      "datetime": 1736767980000
    },
    {
      "open": 24.48,
      "high": 24.48,
      "low": 24.46,
      "close": 24.46,
      "volume": 350,
      "datetime": 1736768040000
    },
    {
      "open": 24.44,
      "high": 24.44,
      "low": 24.42,
      "close": 24.42,
      "volume": 400,
      "datetime": 1736768100000
    },
    {
      "open": 24.43,
      "high": 24.43,
      "low": 24.43,
      "close": 24.43,
      "volume": 150,
      "datetime": 1736768160000
    },
    {
      "open": 24.45,
      "high": 24.46,
      "low": 24.45,
      "close": 24.46,
      "volume": 990,
      "datetime": 1736768220000
    },
    {
      "open": 24.45,
      "high": 24.45,
      "low": 24.45,
      "close": 24.45,
      "volume": 1268,
      "datetime": 1736768340000
    },
    {
      "open": 24.49,
      "high": 24.5,
      "low": 24.49,
      "close": 24.5,
      "volume": 1412,
      "datetime": 1736768400000
    },
    {
      "open": 24.51,
      "high": 24.52,
      "low": 24.51,
      "close": 24.52,
      "volume": 5123,
      "datetime": 1736768460000
    },
    {
      "open": 24.53,
      "high": 24.53,
      "low": 24.53,
      "close": 24.53,
      "volume": 100,
      "datetime": 1736768520000
    },
    {
      "open": 24.57,
      "high": 24.57,
      "low": 24.57,
      "close": 24.57,
      "volume": 5500,
      "datetime": 1736768580000
    },
    {
      "open": 24.57,
      "high": 24.57,
      "low": 24.57,
      "close": 24.57,
      "volume": 160,
      "datetime": 1736768640000
    },
    {
      "open": 24.46,
      "high": 24.46,
      "low": 24.44,
      "close": 24.44,
      "volume": 4999,
      "datetime": 1736768820000
    },
    {
      "open": 24.45,
      "high": 24.45,
      "low": 24.45,
      "close": 24.45,
      "volume": 200,
      "datetime": 1736768880000
    },
    {
      "open": 24.41,
      "high": 24.41,
      "low": 24.41,
      "close": 24.41,
      "volume": 151,
      "datetime": 1736769060000
    },
    {
      "open": 24.42,
      "high": 24.42,
      "low": 24.41,
      "close": 24.41,
      "volume": 424,
      "datetime": 1736769120000
    },
    {
      "open": 24.49,
      "high": 24.49,
      "low": 24.49,
      "close": 24.49,
      "volume": 4997,
      "datetime": 1736769300000
    },
    {
      "open": 24.48,
      "high": 24.48,
      "low": 24.48,
      "close": 24.48,
      "volume": 150,
      "datetime": 1736769420000
    },
    {
      "open": 24.54,
      "high": 24.54,
      "low": 24.54,
      "close": 24.54,
      "volume": 250,
      "datetime": 1736769480000
    },
    {
      "open": 24.53,
      "high": 24.53,
      "low": 24.53,
      "close": 24.53,
      "volume": 150,
      "datetime": 1736769540000
    },
    {
      "open": 24.53,
      "high": 24.53,
      "low": 24.53,
      "close": 24.53,
      "volume": 806,
      "datetime": 1736769600000
    },
    {
      "open": 24.55,
      "high": 24.57,
      "low": 24.55,
      "close": 24.57,
      "volume": 339,
      "datetime": 1736769660000
    },
    {
      "open": 24.57,
      "high": 24.57,
      "low": 24.57,
      "close": 24.57,
      "volume": 1800,
      "datetime": 1736769720000
    },
    {
      "open": 24.6,
      "high": 24.6,
      "low": 24.6,
      "close": 24.6,
      "volume": 500,
      "datetime": 1736769780000
    },
    {
      "open": 24.56,
      "high": 24.59,
      "low": 24.56,
      "close": 24.59,
      "volume": 3582,
      "datetime": 1736769900000
    },
    {
      "open": 24.51,
      "high": 24.51,
      "low": 24.51,
      "close": 24.51,
      "volume": 100,
      "datetime": 1736769960000
    },
    {
      "open": 24.47,
      "high": 24.47,
      "low": 24.47,
      "close": 24.47,
      "volume": 2000,
      "datetime": 1736770020000
    },
    {
      "open": 24.5,
      "high": 24.5,
      "low": 24.5,
      "close": 24.5,
      "volume": 600,
      "datetime": 1736770500000
    },
    {
      "open": 24.59,
      "high": 24.59,
      "low": 24.59,
      "close": 24.59,
      "volume": 760,
      "datetime": 1736770560000
    },
    {
      "open": 24.54,
      "high": 24.54,
      "low": 24.54,
      "close": 24.54,
      "volume": 331,
      "datetime": 1736770740000
    },
    {
      "open": 24.5,
      "high": 24.5,
      "low": 24.5,
      "close": 24.5,
      "volume": 100,
      "datetime": 1736770800000
    },
    {
      "open": 24.55,
      "high": 24.55,
      "low": 24.55,
      "close": 24.55,
      "volume": 100,
      "datetime": 1736771220000
    },
    {
      "open": 24.53,
      "high": 24.55,
      "low": 24.53,
      "close": 24.55,
      "volume": 5146,
      "datetime": 1736771340000
    },
    {
      "open": 24.55,
      "high": 24.56,
      "low": 24.55,
      "close": 24.56,
      "volume": 564,
      "datetime": 1736771400000
    },
    {
      "open": 24.57,
      "high": 24.57,
      "low": 24.57,
      "close": 24.57,
      "volume": 398,
      "datetime": 1736771700000
    },
    {
      "open": 24.59,
      "high": 24.59,
      "low": 24.59,
      "close": 24.59,
      "volume": 100,
      "datetime": 1736771760000
    },
    {
      "open": 24.6,
      "high": 24.6,
      "low": 24.6,
      "close": 24.6,
      "volume": 100,
      "datetime": 1736771820000
    },
    {
      "open": 24.63,
      "high": 24.65,
      "low": 24.63,
      "close": 24.65,
      "volume": 2142,
      "datetime": 1736772000000
    },
    {
      "open": 24.67,
      "high": 24.67,
      "low": 24.67,
      "close": 24.67,
      "volume": 200,
      "datetime": 1736772120000
    },
    {
      "open": 24.62,
      "high": 24.62,
      "low": 24.62,
      "close": 24.62,
      "volume": 500,
      "datetime": 1736772180000
    },
    {
      "open": 24.57,
      "high": 24.57,
      "low": 24.57,
      "close": 24.57,
      "volume": 384,
      "datetime": 1736772240000
    },
    {
      "open": 24.57,
      "high": 24.57,
      "low": 24.57,
      "close": 24.57,
      "volume": 450,
      "datetime": 1736772300000
    },
    {
      "open": 24.6,
      "high": 24.6,
      "low": 24.57,
      "close": 24.59,
      "volume": 1806,
      "datetime": 1736772600000
    },
    {
      "open": 24.58,
      "high": 24.58,
      "low": 24.58,
      "close": 24.58,
      "volume": 101,
      "datetime": 1736772660000
    },
    {
      "open": 24.57,
      "high": 24.57,
      "low": 24.57,
      "close": 24.57,
      "volume": 858,
      "datetime": 1736772780000
    },
    {
      "open": 24.5,
      "high": 24.5,
      "low": 24.5,
      "close": 24.5,
      "volume": 760,
      "datetime": 1736772840000
    },
    {
      "open": 24.54,
      "high": 24.54,
      "low": 24.54,
      "close": 24.54,
      "volume": 1000,
      "datetime": 1736772900000
    },
    {
      "open": 24.54,
      "high": 24.54,
      "low": 24.54,
      "close": 24.54,
      "volume": 100,
      "datetime": 1736773020000
    },
    {
      "open": 24.54,
      "high": 24.54,
      "low": 24.54,
      "close": 24.54,
      "volume": 250,
      "datetime": 1736773080000
    },
    {
      "open": 24.5599,
      "high": 24.5599,
      "low": 24.5599,
      "close": 24.5599,
      "volume": 100,
      "datetime": 1736773140000
    },
    {
      "open": 24.6,
      "high": 24.6,
      "low": 24.6,
      "close": 24.6,
      "volume": 100,
      "datetime": 1736773260000
    },
    {
      "open": 24.61,
      "high": 24.61,
      "low": 24.61,
      "close": 24.61,
      "volume": 300,
      "datetime": 1736773320000
    },
    {
      "open": 24.56,
      "high": 24.56,
      "low": 24.56,
      "close": 24.56,
      "volume": 100,
      "datetime": 1736773380000
    },
    {
      "open": 24.49,
      "high": 24.5,
      "low": 24.49,
      "close": 24.5,
      "volume": 486,
      "datetime": 1736773500000
    },
    {
      "open": 24.52,
      "high": 24.52,
      "low": 24.5,
      "close": 24.5,
      "volume": 2300,
      "datetime": 1736773560000
    },
    {
      "open": 24.48,
      "high": 24.48,
      "low": 24.48,
      "close": 24.48,
      "volume": 2506,
      "datetime": 1736773680000
    },
    {
      "open": 24.39,
      "high": 24.39,
      "low": 24.39,
      "close": 24.39,
      "volume": 5161,
      "datetime": 1736773740000
    },
    {
      "open": 24.39,
      "high": 24.45,
      "low": 24.39,
      "close": 24.45,
      "volume": 2098,
      "datetime": 1736773800000
    },
    {
      "open": 24.45,
      "high": 24.45,
      "low": 24.45,
      "close": 24.45,
      "volume": 1000,
      "datetime": 1736773860000
    },
    {
      "open": 24.42,
      "high": 24.42,
      "low": 24.42,
      "close": 24.42,
      "volume": 477,
      "datetime": 1736773920000
    },
    {
      "open": 24.3801,
      "high": 24.401,
      "low": 24.3801,
      "close": 24.401,
      "volume": 250,
      "datetime": 1736774040000
    },
    {
      "open": 24.4,
      "high": 24.4,
      "low": 24.4,
      "close": 24.4,
      "volume": 300,
      "datetime": 1736774100000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.32,
      "close": 24.32,
      "volume": 286,
      "datetime": 1736774340000
    },
    {
      "open": 24.33,
      "high": 24.33,
      "low": 24.33,
      "close": 24.33,
      "volume": 200,
      "datetime": 1736774400000
    },
    {
      "open": 24.33,
      "high": 24.33,
      "low": 24.33,
      "close": 24.33,
      "volume": 347,
      "datetime": 1736774460000
    },
    {
      "open": 24.35,
      "high": 24.35,
      "low": 24.34,
      "close": 24.34,
      "volume": 798,
      "datetime": 1736774520000
    },
    {
      "open": 24.3,
      "high": 24.3,
      "low": 24.3,
      "close": 24.3,
      "volume": 905,
      "datetime": 1736774580000
    },
    {
      "open": 24.34,
      "high": 24.37,
      "low": 24.34,
      "close": 24.37,
      "volume": 1120,
      "datetime": 1736774700000
    },
    {
      "open": 24.37,
      "high": 24.37,
      "low": 24.31,
      "close": 24.31,
      "volume": 1205,
      "datetime": 1736774760000
    },
    {
      "open": 24.3113,
      "high": 24.34,
      "low": 24.31,
      "close": 24.31,
      "volume": 2240,
      "datetime": 1736774820000
    },
    {
      "open": 24.39,
      "high": 24.39,
      "low": 24.39,
      "close": 24.39,
      "volume": 500,
      "datetime": 1736774880000
    },
    {
      "open": 24.41,
      "high": 24.4141,
      "low": 24.41,
      "close": 24.4141,
      "volume": 322,
      "datetime": 1736774940000
    },
    {
      "open": 24.445,
      "high": 24.445,
      "low": 24.445,
      "close": 24.445,
      "volume": 185,
      "datetime": 1736775060000
    },
    {
      "open": 24.39,
      "high": 24.39,
      "low": 24.39,
      "close": 24.39,
      "volume": 497,
      "datetime": 1736775120000
    },
    {
      "open": 24.38,
      "high": 24.3999,
      "low": 24.38,
      "close": 24.3999,
      "volume": 296,
      "datetime": 1736775240000
    },
    {
      "open": 24.41,
      "high": 24.41,
      "low": 24.41,
      "close": 24.41,
      "volume": 100,
      "datetime": 1736775420000
    },
    {
      "open": 24.4,
      "high": 24.4,
      "low": 24.4,
      "close": 24.4,
      "volume": 1000,
      "datetime": 1736775480000
    },
    {
      "open": 24.45,
      "high": 24.45,
      "low": 24.45,
      "close": 24.45,
      "volume": 800,
      "datetime": 1736775780000
    },
    {
      "open": 24.46,
      "high": 24.46,
      "low": 24.46,
      "close": 24.46,
      "volume": 800,
      "datetime": 1736775900000
    },
    {
      "open": 24.48,
      "high": 24.48,
      "low": 24.475,
      "close": 24.48,
      "volume": 1306,
      "datetime": 1736776020000
    },
    {
      "open": 24.4999,
      "high": 24.4999,
      "low": 24.4898,
      "close": 24.4898,
      "volume": 2100,
      "datetime": 1736776080000
    },
    {
      "open": 24.5,
      "high": 24.5,
      "low": 24.5,
      "close": 24.5,
      "volume": 1400,
      "datetime": 1736776140000
    },
    {
      "open": 24.49,
      "high": 24.49,
      "low": 24.49,
      "close": 24.49,
      "volume": 900,
      "datetime": 1736776260000
    },
    {
      "open": 24.4899,
      "high": 24.4899,
      "low": 24.4899,
      "close": 24.4899,
      "volume": 200,
      "datetime": 1736776320000
    },
    {
      "open": 24.44,
      "high": 24.44,
      "low": 24.44,
      "close": 24.44,
      "volume": 2000,
      "datetime": 1736776500000
    },
    {
      "open": 24.46,
      "high": 24.46,
      "low": 24.46,
      "close": 24.46,
      "volume": 362,
      "datetime": 1736776620000
    },
    {
      "open": 24.48,
      "high": 24.48,
      "low": 24.48,
      "close": 24.48,
      "volume": 1415,
      "datetime": 1736776800000
    },
    {
      "open": 24.48,
      "high": 24.48,
      "low": 24.48,
      "close": 24.48,
      "volume": 326,
      "datetime": 1736776860000
    },
    {
      "open": 24.4894,
      "high": 24.4894,
      "low": 24.4894,
      "close": 24.4894,
      "volume": 100,
      "datetime": 1736776920000
    },
    {
      "open": 24.5,
      "high": 24.55,
      "low": 24.5,
      "close": 24.55,
      "volume": 620,
      "datetime": 1736776980000
    },
    {
      "open": 24.56,
      "high": 24.56,
      "low": 24.56,
      "close": 24.56,
      "volume": 400,
      "datetime": 1736777040000
    },
    {
      "open": 24.53,
      "high": 24.53,
      "low": 24.52,
      "close": 24.52,
      "volume": 500,
      "datetime": 1736777100000
    },
    {
      "open": 24.53,
      "high": 24.53,
      "low": 24.491,
      "close": 24.491,
      "volume": 1602,
      "datetime": 1736777160000
    },
    {
      "open": 24.5099,
      "high": 24.5099,
      "low": 24.5099,
      "close": 24.5099,
      "volume": 4000,
      "datetime": 1736777220000
    },
    {
      "open": 24.55,
      "high": 24.55,
      "low": 24.55,
      "close": 24.55,
      "volume": 300,
      "datetime": 1736777340000
    },
    {
      "open": 24.55,
      "high": 24.55,
      "low": 24.55,
      "close": 24.55,
      "volume": 200,
      "datetime": 1736777400000
    },
    {
      "open": 24.55,
      "high": 24.5501,
      "low": 24.55,
      "close": 24.5501,
      "volume": 500,
      "datetime": 1736777460000
    },
    {
      "open": 24.59,
      "high": 24.59,
      "low": 24.59,
      "close": 24.59,
      "volume": 200,
      "datetime": 1736777520000
    },
    {
      "open": 24.5499,
      "high": 24.5499,
      "low": 24.5493,
      "close": 24.5493,
      "volume": 200,
      "datetime": 1736777760000
    },
    {
      "open": 24.53,
      "high": 24.53,
      "low": 24.52,
      "close": 24.52,
      "volume": 350,
      "datetime": 1736777820000
    },
    {
      "open": 24.501,
      "high": 24.53,
      "low": 24.501,
      "close": 24.53,
      "volume": 2100,
      "datetime": 1736777880000
    },
    {
      "open": 24.51,
      "high": 24.52,
      "low": 24.51,
      "close": 24.51,
      "volume": 2880,
      "datetime": 1736778000000
    },
    {
      "open": 24.49,
      "high": 24.51,
      "low": 24.49,
      "close": 24.51,
      "volume": 1940,
      "datetime": 1736778060000
    },
    {
      "open": 24.4712,
      "high": 24.4712,
      "low": 24.4712,
      "close": 24.4712,
      "volume": 6000,
      "datetime": 1736778240000
    },
    {
      "open": 24.5599,
      "high": 24.5599,
      "low": 24.5599,
      "close": 24.5599,
      "volume": 100,
      "datetime": 1736778420000
    },
    {
      "open": 24.5499,
      "high": 24.5499,
      "low": 24.5499,
      "close": 24.5499,
      "volume": 100,
      "datetime": 1736778480000
    },
    {
      "open": 24.53,
      "high": 24.56,
      "low": 24.53,
      "close": 24.5471,
      "volume": 31072,
      "datetime": 1736778600000
    },
    {
      "open": 24.57,
      "high": 24.59,
      "low": 24.56,
      "close": 24.57,
      "volume": 19497,
      "datetime": 1736778660000
    },
    {
      "open": 24.55,
      "high": 24.56,
      "low": 24.52,
      "close": 24.5548,
      "volume": 31976,
      "datetime": 1736778720000
    },
    {
      "open": 24.59,
      "high": 24.67,
      "low": 24.58,
      "close": 24.67,
      "volume": 14934,
      "datetime": 1736778780000
    },
    {
      "open": 24.7,
      "high": 24.76,
      "low": 24.67,
      "close": 24.7393,
      "volume": 20861,
      "datetime": 1736778840000
    },
    {
      "open": 24.73,
      "high": 24.92,
      "low": 24.6901,
      "close": 24.88,
      "volume": 30207,
      "datetime": 1736778900000
    },
    {
      "open": 24.88,
      "high": 24.8897,
      "low": 24.69,
      "close": 24.74,
      "volume": 20372,
      "datetime": 1736778960000
    },
    {
      "open": 24.7301,
      "high": 24.7574,
      "low": 24.65,
      "close": 24.7226,
      "volume": 16695,
      "datetime": 1736779020000
    },
    {
      "open": 24.7299,
      "high": 24.7299,
      "low": 24.6758,
      "close": 24.68,
      "volume": 6864,
      "datetime": 1736779080000
    },
    {
      "open": 24.65,
      "high": 24.6972,
      "low": 24.64,
      "close": 24.6972,
      "volume": 16877,
      "datetime": 1736779140000
    },
    {
      "open": 24.6899,
      "high": 24.72,
      "low": 24.57,
      "close": 24.59,
      "volume": 10717,
      "datetime": 1736779200000
    },
    {
      "open": 24.551,
      "high": 24.5548,
      "low": 24.5,
      "close": 24.5548,
      "volume": 8451,
      "datetime": 1736779260000
    },
    {
      "open": 24.59,
      "high": 24.59,
      "low": 24.51,
      "close": 24.51,
      "volume": 4109,
      "datetime": 1736779320000
    },
    {
      "open": 24.5,
      "high": 24.5,
      "low": 24.392,
      "close": 24.392,
      "volume": 8798,
      "datetime": 1736779380000
    },
    {
      "open": 24.39,
      "high": 24.39,
      "low": 24.35,
      "close": 24.37,
      "volume": 12182,
      "datetime": 1736779440000
    },
    {
      "open": 24.42,
      "high": 24.43,
      "low": 24.37,
      "close": 24.43,
      "volume": 21886,
      "datetime": 1736779500000
    },
    {
      "open": 24.4899,
      "high": 24.4899,
      "low": 24.46,
      "close": 24.4651,
      "volume": 6522,
      "datetime": 1736779560000
    },
    {
      "open": 24.46,
      "high": 24.4904,
      "low": 24.44,
      "close": 24.445,
      "volume": 26603,
      "datetime": 1736779620000
    },
    {
      "open": 24.41,
      "high": 24.41,
      "low": 24.31,
      "close": 24.31,
      "volume": 3457,
      "datetime": 1736779680000
    },
    {
      "open": 24.34,
      "high": 24.35,
      "low": 24.32,
      "close": 24.3451,
      "volume": 3700,
      "datetime": 1736779740000
    },
    {
      "open": 24.3405,
      "high": 24.3899,
      "low": 24.3405,
      "close": 24.3573,
      "volume": 6193,
      "datetime": 1736779800000
    },
    {
      "open": 24.3776,
      "high": 24.3776,
      "low": 24.3,
      "close": 24.32,
      "volume": 2330,
      "datetime": 1736779860000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.2301,
      "close": 24.2401,
      "volume": 18431,
      "datetime": 1736779920000
    },
    {
      "open": 24.26,
      "high": 24.2862,
      "low": 24.2479,
      "close": 24.2595,
      "volume": 4747,
      "datetime": 1736779980000
    },
    {
      "open": 24.24,
      "high": 24.24,
      "low": 24.19,
      "close": 24.21,
      "volume": 6739,
      "datetime": 1736780040000
    },
    {
      "open": 24.205,
      "high": 24.2596,
      "low": 24.2,
      "close": 24.2575,
      "volume": 4471,
      "datetime": 1736780100000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.17,
      "close": 24.1707,
      "volume": 5053,
      "datetime": 1736780160000
    },
    {
      "open": 24.2334,
      "high": 24.245,
      "low": 24.2334,
      "close": 24.245,
      "volume": 2021,
      "datetime": 1736780220000
    },
    {
      "open": 24.25,
      "high": 24.27,
      "low": 24.24,
      "close": 24.2601,
      "volume": 2529,
      "datetime": 1736780280000
    },
    {
      "open": 24.2707,
      "high": 24.2901,
      "low": 24.2707,
      "close": 24.2785,
      "volume": 5586,
      "datetime": 1736780340000
    },
    {
      "open": 24.2792,
      "high": 24.3039,
      "low": 24.25,
      "close": 24.2501,
      "volume": 7971,
      "datetime": 1736780400000
    },
    {
      "open": 24.31,
      "high": 24.326618,
      "low": 24.3,
      "close": 24.3,
      "volume": 3354,
      "datetime": 1736780460000
    },
    {
      "open": 24.2788,
      "high": 24.2788,
      "low": 24.26,
      "close": 24.26,
      "volume": 747,
      "datetime": 1736780520000
    },
    {
      "open": 24.25,
      "high": 24.3104,
      "low": 24.25,
      "close": 24.3104,
      "volume": 3449,
      "datetime": 1736780580000
    },
    {
      "open": 24.28,
      "high": 24.2848,
      "low": 24.25,
      "close": 24.25,
      "volume": 300,
      "datetime": 1736780640000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.25,
      "close": 24.25,
      "volume": 1038,
      "datetime": 1736780700000
    },
    {
      "open": 24.25,
      "high": 24.25,
      "low": 24.1902,
      "close": 24.1902,
      "volume": 1660,
      "datetime": 1736780760000
    },
    {
      "open": 24.18,
      "high": 24.208,
      "low": 24.165,
      "close": 24.208,
      "volume": 19625,
      "datetime": 1736780820000
    },
    {
      "open": 24.21,
      "high": 24.225,
      "low": 24.12,
      "close": 24.12,
      "volume": 2411,
      "datetime": 1736780880000
    },
    {
      "open": 24.11,
      "high": 24.1399,
      "low": 24.1,
      "close": 24.135,
      "volume": 5952,
      "datetime": 1736780940000
    },
    {
      "open": 24.15,
      "high": 24.19,
      "low": 24.15,
      "close": 24.17,
      "volume": 3515,
      "datetime": 1736781000000
    },
    {
      "open": 24.175,
      "high": 24.18,
      "low": 24.15,
      "close": 24.18,
      "volume": 1893,
      "datetime": 1736781060000
    },
    {
      "open": 24.17,
      "high": 24.17,
      "low": 24.1,
      "close": 24.1058,
      "volume": 3561,
      "datetime": 1736781120000
    },
    {
      "open": 24.1,
      "high": 24.11,
      "low": 24.09,
      "close": 24.09,
      "volume": 4044,
      "datetime": 1736781180000
    },
    {
      "open": 24.0999,
      "high": 24.12,
      "low": 24.095,
      "close": 24.12,
      "volume": 2152,
      "datetime": 1736781240000
    },
    {
      "open": 24.1296,
      "high": 24.17,
      "low": 24.1296,
      "close": 24.1665,
      "volume": 1125,
      "datetime": 1736781300000
    },
    {
      "open": 24.15,
      "high": 24.17,
      "low": 24.14,
      "close": 24.14,
      "volume": 4754,
      "datetime": 1736781360000
    },
    {
      "open": 24.1497,
      "high": 24.1497,
      "low": 24.1099,
      "close": 24.1099,
      "volume": 56032,
      "datetime": 1736781420000
    },
    {
      "open": 24.095,
      "high": 24.095,
      "low": 24.025,
      "close": 24.03,
      "volume": 14206,
      "datetime": 1736781480000
    },
    {
      "open": 24.0101,
      "high": 24.035,
      "low": 24.0101,
      "close": 24.03,
      "volume": 6595,
      "datetime": 1736781540000
    },
    {
      "open": 24,
      "high": 24.015,
      "low": 23.995,
      "close": 24.015,
      "volume": 4347,
      "datetime": 1736781600000
    },
    {
      "open": 24.0101,
      "high": 24.0101,
      "low": 23.97,
      "close": 23.97,
      "volume": 4000,
      "datetime": 1736781660000
    },
    {
      "open": 23.96,
      "high": 24,
      "low": 23.95,
      "close": 24,
      "volume": 7465,
      "datetime": 1736781720000
    },
    {
      "open": 24,
      "high": 24,
      "low": 23.94,
      "close": 23.95,
      "volume": 6624,
      "datetime": 1736781780000
    },
    {
      "open": 23.94,
      "high": 24.02,
      "low": 23.94,
      "close": 24.02,
      "volume": 9535,
      "datetime": 1736781840000
    },
    {
      "open": 24.03,
      "high": 24.08,
      "low": 24.03,
      "close": 24.075,
      "volume": 6765,
      "datetime": 1736781900000
    },
    {
      "open": 24.075,
      "high": 24.1398,
      "low": 24.075,
      "close": 24.115,
      "volume": 5990,
      "datetime": 1736781960000
    },
    {
      "open": 24.1,
      "high": 24.13,
      "low": 24.07,
      "close": 24.1299,
      "volume": 4808,
      "datetime": 1736782020000
    },
    {
      "open": 24.12,
      "high": 24.1712,
      "low": 24.11,
      "close": 24.1712,
      "volume": 6514,
      "datetime": 1736782080000
    },
    {
      "open": 24.175,
      "high": 24.2199,
      "low": 24.175,
      "close": 24.175,
      "volume": 16543,
      "datetime": 1736782140000
    },
    {
      "open": 24.1663,
      "high": 24.235,
      "low": 24.1663,
      "close": 24.19,
      "volume": 13553,
      "datetime": 1736782200000
    },
    {
      "open": 24.17,
      "high": 24.17,
      "low": 24.1368,
      "close": 24.155,
      "volume": 4022,
      "datetime": 1736782260000
    },
    {
      "open": 24.1407,
      "high": 24.15,
      "low": 24.1048,
      "close": 24.13,
      "volume": 2465,
      "datetime": 1736782320000
    },
    {
      "open": 24.13,
      "high": 24.14,
      "low": 24.13,
      "close": 24.14,
      "volume": 434,
      "datetime": 1736782380000
    },
    {
      "open": 24.12,
      "high": 24.17,
      "low": 24.12,
      "close": 24.16,
      "volume": 2711,
      "datetime": 1736782440000
    },
    {
      "open": 24.14,
      "high": 24.15,
      "low": 24.135,
      "close": 24.135,
      "volume": 625,
      "datetime": 1736782500000
    },
    {
      "open": 24.14,
      "high": 24.18,
      "low": 24.14,
      "close": 24.18,
      "volume": 1405,
      "datetime": 1736782560000
    },
    {
      "open": 24.155,
      "high": 24.155,
      "low": 24.1197,
      "close": 24.13,
      "volume": 689,
      "datetime": 1736782620000
    },
    {
      "open": 24.115,
      "high": 24.15,
      "low": 24.115,
      "close": 24.14,
      "volume": 12389,
      "datetime": 1736782680000
    },
    {
      "open": 24.125,
      "high": 24.125,
      "low": 24.065,
      "close": 24.065,
      "volume": 2459,
      "datetime": 1736782740000
    },
    {
      "open": 24.07,
      "high": 24.11,
      "low": 24.04,
      "close": 24.11,
      "volume": 1650,
      "datetime": 1736782800000
    },
    {
      "open": 24.09,
      "high": 24.11,
      "low": 24.06,
      "close": 24.06,
      "volume": 1750,
      "datetime": 1736782860000
    },
    {
      "open": 24.06,
      "high": 24.06,
      "low": 24.045,
      "close": 24.048,
      "volume": 5120,
      "datetime": 1736782920000
    },
    {
      "open": 24.05,
      "high": 24.08,
      "low": 24.05,
      "close": 24.08,
      "volume": 1633,
      "datetime": 1736782980000
    },
    {
      "open": 24.065,
      "high": 24.065,
      "low": 24.04,
      "close": 24.05,
      "volume": 4000,
      "datetime": 1736783040000
    },
    {
      "open": 24.05,
      "high": 24.085,
      "low": 24.05,
      "close": 24.08,
      "volume": 2680,
      "datetime": 1736783100000
    },
    {
      "open": 24.09,
      "high": 24.115,
      "low": 24.0876,
      "close": 24.09,
      "volume": 3701,
      "datetime": 1736783160000
    },
    {
      "open": 24.09,
      "high": 24.1172,
      "low": 24.09,
      "close": 24.11,
      "volume": 751,
      "datetime": 1736783220000
    },
    {
      "open": 24.1099,
      "high": 24.14,
      "low": 24.1099,
      "close": 24.11,
      "volume": 969,
      "datetime": 1736783280000
    },
    {
      "open": 24.0935,
      "high": 24.0935,
      "low": 24.07,
      "close": 24.075,
      "volume": 1247,
      "datetime": 1736783340000
    },
    {
      "open": 24.065,
      "high": 24.09,
      "low": 24.06,
      "close": 24.06,
      "volume": 4290,
      "datetime": 1736783400000
    },
    {
      "open": 24.07,
      "high": 24.095,
      "low": 24.07,
      "close": 24.09,
      "volume": 6434,
      "datetime": 1736783460000
    },
    {
      "open": 24.1,
      "high": 24.1599,
      "low": 24.1,
      "close": 24.1599,
      "volume": 1450,
      "datetime": 1736783520000
    },
    {
      "open": 24.16,
      "high": 24.16,
      "low": 24.14,
      "close": 24.15,
      "volume": 1300,
      "datetime": 1736783580000
    },
    {
      "open": 24.15,
      "high": 24.18,
      "low": 24.15,
      "close": 24.17,
      "volume": 3303,
      "datetime": 1736783640000
    },
    {
      "open": 24.1605,
      "high": 24.2,
      "low": 24.1605,
      "close": 24.2,
      "volume": 1160,
      "datetime": 1736783700000
    },
    {
      "open": 24.1807,
      "high": 24.19,
      "low": 24.165,
      "close": 24.175,
      "volume": 1750,
      "datetime": 1736783760000
    },
    {
      "open": 24.175,
      "high": 24.18,
      "low": 24.16,
      "close": 24.1603,
      "volume": 1000,
      "datetime": 1736783820000
    },
    {
      "open": 24.1599,
      "high": 24.16,
      "low": 24.15,
      "close": 24.16,
      "volume": 6414,
      "datetime": 1736783880000
    },
    {
      "open": 24.1799,
      "high": 24.19,
      "low": 24.1799,
      "close": 24.19,
      "volume": 1787,
      "datetime": 1736783940000
    },
    {
      "open": 24.19,
      "high": 24.26,
      "low": 24.19,
      "close": 24.2498,
      "volume": 6896,
      "datetime": 1736784000000
    },
    {
      "open": 24.2199,
      "high": 24.2199,
      "low": 24.18,
      "close": 24.195,
      "volume": 561,
      "datetime": 1736784060000
    },
    {
      "open": 24.1852,
      "high": 24.24,
      "low": 24.1852,
      "close": 24.2,
      "volume": 5826,
      "datetime": 1736784120000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.21,
      "close": 24.21,
      "volume": 490,
      "datetime": 1736784180000
    },
    {
      "open": 24.2104,
      "high": 24.2394,
      "low": 24.2104,
      "close": 24.23,
      "volume": 3483,
      "datetime": 1736784240000
    },
    {
      "open": 24.19,
      "high": 24.2,
      "low": 24.19,
      "close": 24.2,
      "volume": 3500,
      "datetime": 1736784300000
    },
    {
      "open": 24.2301,
      "high": 24.2301,
      "low": 24.22,
      "close": 24.22,
      "volume": 4462,
      "datetime": 1736784360000
    },
    {
      "open": 24.21,
      "high": 24.215,
      "low": 24.175,
      "close": 24.1788,
      "volume": 3310,
      "datetime": 1736784420000
    },
    {
      "open": 24.17,
      "high": 24.2,
      "low": 24.17,
      "close": 24.2,
      "volume": 2037,
      "datetime": 1736784480000
    },
    {
      "open": 24.2,
      "high": 24.22,
      "low": 24.2,
      "close": 24.22,
      "volume": 797,
      "datetime": 1736784540000
    },
    {
      "open": 24.2498,
      "high": 24.25,
      "low": 24.235,
      "close": 24.25,
      "volume": 1006,
      "datetime": 1736784600000
    },
    {
      "open": 24.28,
      "high": 24.3099,
      "low": 24.27,
      "close": 24.29,
      "volume": 17666,
      "datetime": 1736784660000
    },
    {
      "open": 24.29,
      "high": 24.31,
      "low": 24.275,
      "close": 24.3064,
      "volume": 4023,
      "datetime": 1736784720000
    },
    {
      "open": 24.32,
      "high": 24.3304,
      "low": 24.32,
      "close": 24.3304,
      "volume": 3384,
      "datetime": 1736784780000
    },
    {
      "open": 24.34,
      "high": 24.34,
      "low": 24.29,
      "close": 24.29,
      "volume": 7858,
      "datetime": 1736784840000
    },
    {
      "open": 24.2867,
      "high": 24.3,
      "low": 24.27,
      "close": 24.3,
      "volume": 3133,
      "datetime": 1736784900000
    },
    {
      "open": 24.27,
      "high": 24.29,
      "low": 24.25,
      "close": 24.26,
      "volume": 5061,
      "datetime": 1736784960000
    },
    {
      "open": 24.27,
      "high": 24.3263,
      "low": 24.27,
      "close": 24.3263,
      "volume": 4360,
      "datetime": 1736785020000
    },
    {
      "open": 24.285,
      "high": 24.33,
      "low": 24.285,
      "close": 24.31664,
      "volume": 3146,
      "datetime": 1736785080000
    },
    {
      "open": 24.31,
      "high": 24.3152,
      "low": 24.31,
      "close": 24.31,
      "volume": 875,
      "datetime": 1736785140000
    },
    {
      "open": 24.26,
      "high": 24.26,
      "low": 24.26,
      "close": 24.26,
      "volume": 1674,
      "datetime": 1736785200000
    },
    {
      "open": 24.29,
      "high": 24.34,
      "low": 24.29,
      "close": 24.33,
      "volume": 1569,
      "datetime": 1736785260000
    },
    {
      "open": 24.33,
      "high": 24.37,
      "low": 24.33,
      "close": 24.37,
      "volume": 2762,
      "datetime": 1736785320000
    },
    {
      "open": 24.35,
      "high": 24.37,
      "low": 24.35,
      "close": 24.36664,
      "volume": 6532,
      "datetime": 1736785380000
    },
    {
      "open": 24.3652,
      "high": 24.37,
      "low": 24.33,
      "close": 24.37,
      "volume": 3114,
      "datetime": 1736785440000
    },
    {
      "open": 24.335,
      "high": 24.335,
      "low": 24.29,
      "close": 24.29,
      "volume": 1310,
      "datetime": 1736785500000
    },
    {
      "open": 24.277,
      "high": 24.31,
      "low": 24.277,
      "close": 24.305,
      "volume": 1331,
      "datetime": 1736785560000
    },
    {
      "open": 24.305,
      "high": 24.305,
      "low": 24.3,
      "close": 24.3002,
      "volume": 1468,
      "datetime": 1736785620000
    },
    {
      "open": 24.29,
      "high": 24.29,
      "low": 24.29,
      "close": 24.29,
      "volume": 225,
      "datetime": 1736785680000
    },
    {
      "open": 24.31,
      "high": 24.315,
      "low": 24.3,
      "close": 24.315,
      "volume": 3530,
      "datetime": 1736785740000
    },
    {
      "open": 24.32,
      "high": 24.35,
      "low": 24.305,
      "close": 24.305,
      "volume": 13243,
      "datetime": 1736785800000
    },
    {
      "open": 24.31,
      "high": 24.315,
      "low": 24.28,
      "close": 24.28,
      "volume": 21900,
      "datetime": 1736785860000
    },
    {
      "open": 24.285,
      "high": 24.3,
      "low": 24.285,
      "close": 24.3,
      "volume": 600,
      "datetime": 1736785920000
    },
    {
      "open": 24.2799,
      "high": 24.29,
      "low": 24.2619,
      "close": 24.29,
      "volume": 2563,
      "datetime": 1736785980000
    },
    {
      "open": 24.28,
      "high": 24.28,
      "low": 24.255,
      "close": 24.27,
      "volume": 1061,
      "datetime": 1736786040000
    },
    {
      "open": 24.295,
      "high": 24.305,
      "low": 24.26,
      "close": 24.27,
      "volume": 1475,
      "datetime": 1736786100000
    },
    {
      "open": 24.2528,
      "high": 24.27,
      "low": 24.2528,
      "close": 24.27,
      "volume": 1050,
      "datetime": 1736786160000
    },
    {
      "open": 24.2899,
      "high": 24.2899,
      "low": 24.27,
      "close": 24.27,
      "volume": 2803,
      "datetime": 1736786220000
    },
    {
      "open": 24.29,
      "high": 24.295,
      "low": 24.285,
      "close": 24.29,
      "volume": 1425,
      "datetime": 1736786280000
    },
    {
      "open": 24.295,
      "high": 24.31,
      "low": 24.295,
      "close": 24.31,
      "volume": 2464,
      "datetime": 1736786340000
    },
    {
      "open": 24.31,
      "high": 24.31,
      "low": 24.25,
      "close": 24.29,
      "volume": 2638,
      "datetime": 1736786400000
    },
    {
      "open": 24.295,
      "high": 24.295,
      "low": 24.24,
      "close": 24.26,
      "volume": 14275,
      "datetime": 1736786460000
    },
    {
      "open": 24.265,
      "high": 24.28,
      "low": 24.25,
      "close": 24.28,
      "volume": 9450,
      "datetime": 1736786520000
    },
    {
      "open": 24.2884,
      "high": 24.2884,
      "low": 24.26,
      "close": 24.26,
      "volume": 2837,
      "datetime": 1736786580000
    },
    {
      "open": 24.26,
      "high": 24.26,
      "low": 24.22,
      "close": 24.23,
      "volume": 10259,
      "datetime": 1736786640000
    },
    {
      "open": 24.23,
      "high": 24.23,
      "low": 24.2,
      "close": 24.2,
      "volume": 981,
      "datetime": 1736786700000
    },
    {
      "open": 24.2,
      "high": 24.21,
      "low": 24.2,
      "close": 24.21,
      "volume": 1750,
      "datetime": 1736786760000
    },
    {
      "open": 24.195,
      "high": 24.22,
      "low": 24.195,
      "close": 24.22,
      "volume": 1550,
      "datetime": 1736786820000
    },
    {
      "open": 24.23,
      "high": 24.255,
      "low": 24.22,
      "close": 24.25,
      "volume": 5900,
      "datetime": 1736786880000
    },
    {
      "open": 24.25,
      "high": 24.26,
      "low": 24.25,
      "close": 24.26,
      "volume": 1317,
      "datetime": 1736786940000
    },
    {
      "open": 24.27,
      "high": 24.3,
      "low": 24.27,
      "close": 24.3,
      "volume": 8658,
      "datetime": 1736787000000
    },
    {
      "open": 24.31,
      "high": 24.31,
      "low": 24.3,
      "close": 24.3,
      "volume": 300,
      "datetime": 1736787060000
    },
    {
      "open": 24.3188,
      "high": 24.35,
      "low": 24.3188,
      "close": 24.34,
      "volume": 5050,
      "datetime": 1736787180000
    },
    {
      "open": 24.34,
      "high": 24.36,
      "low": 24.34,
      "close": 24.36,
      "volume": 4461,
      "datetime": 1736787240000
    },
    {
      "open": 24.36,
      "high": 24.39,
      "low": 24.36,
      "close": 24.38,
      "volume": 750,
      "datetime": 1736787300000
    },
    {
      "open": 24.39,
      "high": 24.4,
      "low": 24.39,
      "close": 24.39,
      "volume": 990,
      "datetime": 1736787360000
    },
    {
      "open": 24.39,
      "high": 24.39,
      "low": 24.37,
      "close": 24.3848,
      "volume": 625,
      "datetime": 1736787420000
    },
    {
      "open": 24.39,
      "high": 24.44,
      "low": 24.39,
      "close": 24.43,
      "volume": 1960,
      "datetime": 1736787480000
    },
    {
      "open": 24.405,
      "high": 24.43,
      "low": 24.405,
      "close": 24.42,
      "volume": 6324,
      "datetime": 1736787540000
    },
    {
      "open": 24.42,
      "high": 24.435,
      "low": 24.41,
      "close": 24.4188,
      "volume": 7882,
      "datetime": 1736787600000
    },
    {
      "open": 24.38,
      "high": 24.3864,
      "low": 24.36,
      "close": 24.3864,
      "volume": 811,
      "datetime": 1736787660000
    },
    {
      "open": 24.39,
      "high": 24.39,
      "low": 24.3516,
      "close": 24.3516,
      "volume": 2289,
      "datetime": 1736787720000
    },
    {
      "open": 24.36,
      "high": 24.38,
      "low": 24.36,
      "close": 24.36,
      "volume": 5716,
      "datetime": 1736787780000
    },
    {
      "open": 24.36,
      "high": 24.38,
      "low": 24.36,
      "close": 24.38,
      "volume": 500,
      "datetime": 1736787840000
    },
    {
      "open": 24.39,
      "high": 24.4,
      "low": 24.38,
      "close": 24.38,
      "volume": 532,
      "datetime": 1736787900000
    },
    {
      "open": 24.3601,
      "high": 24.3601,
      "low": 24.35,
      "close": 24.35,
      "volume": 225,
      "datetime": 1736787960000
    },
    {
      "open": 24.38,
      "high": 24.38,
      "low": 24.36,
      "close": 24.36,
      "volume": 3850,
      "datetime": 1736788020000
    },
    {
      "open": 24.35,
      "high": 24.35,
      "low": 24.33,
      "close": 24.34,
      "volume": 2063,
      "datetime": 1736788080000
    },
    {
      "open": 24.3352,
      "high": 24.3352,
      "low": 24.27,
      "close": 24.27,
      "volume": 689,
      "datetime": 1736788140000
    },
    {
      "open": 24.29,
      "high": 24.29,
      "low": 24.275,
      "close": 24.275,
      "volume": 550,
      "datetime": 1736788200000
    },
    {
      "open": 24.28,
      "high": 24.29,
      "low": 24.26,
      "close": 24.26,
      "volume": 1018,
      "datetime": 1736788260000
    },
    {
      "open": 24.25,
      "high": 24.28,
      "low": 24.24,
      "close": 24.28,
      "volume": 475,
      "datetime": 1736788320000
    },
    {
      "open": 24.29,
      "high": 24.3235,
      "low": 24.29,
      "close": 24.3235,
      "volume": 1250,
      "datetime": 1736788380000
    },
    {
      "open": 24.33,
      "high": 24.33,
      "low": 24.31,
      "close": 24.31,
      "volume": 4649,
      "datetime": 1736788440000
    },
    {
      "open": 24.31,
      "high": 24.3128,
      "low": 24.29,
      "close": 24.29,
      "volume": 1835,
      "datetime": 1736788500000
    },
    {
      "open": 24.3,
      "high": 24.3042,
      "low": 24.28,
      "close": 24.28,
      "volume": 1040,
      "datetime": 1736788560000
    },
    {
      "open": 24.26,
      "high": 24.2699,
      "low": 24.2512,
      "close": 24.2512,
      "volume": 924,
      "datetime": 1736788620000
    },
    {
      "open": 24.2874,
      "high": 24.3,
      "low": 24.2874,
      "close": 24.3,
      "volume": 1850,
      "datetime": 1736788680000
    },
    {
      "open": 24.3,
      "high": 24.3,
      "low": 24.26,
      "close": 24.2622,
      "volume": 3475,
      "datetime": 1736788740000
    },
    {
      "open": 24.27,
      "high": 24.285,
      "low": 24.27,
      "close": 24.285,
      "volume": 825,
      "datetime": 1736788800000
    },
    {
      "open": 24.29,
      "high": 24.29,
      "low": 24.27,
      "close": 24.27,
      "volume": 790,
      "datetime": 1736788860000
    },
    {
      "open": 24.3,
      "high": 24.3,
      "low": 24.28,
      "close": 24.28,
      "volume": 625,
      "datetime": 1736788920000
    },
    {
      "open": 24.26,
      "high": 24.27,
      "low": 24.26,
      "close": 24.27,
      "volume": 875,
      "datetime": 1736788980000
    },
    {
      "open": 24.25,
      "high": 24.2752,
      "low": 24.25,
      "close": 24.2752,
      "volume": 902,
      "datetime": 1736789040000
    },
    {
      "open": 24.26,
      "high": 24.26,
      "low": 24.25,
      "close": 24.25,
      "volume": 475,
      "datetime": 1736789100000
    },
    {
      "open": 24.25,
      "high": 24.25,
      "low": 24.24,
      "close": 24.25,
      "volume": 425,
      "datetime": 1736789160000
    },
    {
      "open": 24.21,
      "high": 24.22,
      "low": 24.2001,
      "close": 24.22,
      "volume": 1357,
      "datetime": 1736789220000
    },
    {
      "open": 24.25,
      "high": 24.25,
      "low": 24.24,
      "close": 24.24,
      "volume": 450,
      "datetime": 1736789280000
    },
    {
      "open": 24.23,
      "high": 24.24,
      "low": 24.22,
      "close": 24.24,
      "volume": 975,
      "datetime": 1736789340000
    },
    {
      "open": 24.25,
      "high": 24.28,
      "low": 24.25,
      "close": 24.28,
      "volume": 950,
      "datetime": 1736789400000
    },
    {
      "open": 24.273,
      "high": 24.2787,
      "low": 24.25,
      "close": 24.25,
      "volume": 1325,
      "datetime": 1736789460000
    },
    {
      "open": 24.24,
      "high": 24.2401,
      "low": 24.23,
      "close": 24.23,
      "volume": 400,
      "datetime": 1736789520000
    },
    {
      "open": 24.2407,
      "high": 24.2407,
      "low": 24.1899,
      "close": 24.1899,
      "volume": 9252,
      "datetime": 1736789580000
    },
    {
      "open": 24.185,
      "high": 24.2,
      "low": 24.185,
      "close": 24.2,
      "volume": 625,
      "datetime": 1736789640000
    },
    {
      "open": 24.17,
      "high": 24.19,
      "low": 24.17,
      "close": 24.19,
      "volume": 4067,
      "datetime": 1736789700000
    },
    {
      "open": 24.215,
      "high": 24.2199,
      "low": 24.2,
      "close": 24.2,
      "volume": 1674,
      "datetime": 1736789760000
    },
    {
      "open": 24.2,
      "high": 24.22,
      "low": 24.2,
      "close": 24.22,
      "volume": 9164,
      "datetime": 1736789820000
    },
    {
      "open": 24.248,
      "high": 24.2488,
      "low": 24.24,
      "close": 24.24,
      "volume": 350,
      "datetime": 1736789880000
    },
    {
      "open": 24.26,
      "high": 24.31,
      "low": 24.26,
      "close": 24.305,
      "volume": 1903,
      "datetime": 1736789940000
    },
    {
      "open": 24.3,
      "high": 24.32,
      "low": 24.3,
      "close": 24.3199,
      "volume": 1295,
      "datetime": 1736790000000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.31,
      "close": 24.31,
      "volume": 575,
      "datetime": 1736790060000
    },
    {
      "open": 24.31,
      "high": 24.3133,
      "low": 24.28,
      "close": 24.28,
      "volume": 1010,
      "datetime": 1736790120000
    },
    {
      "open": 24.31,
      "high": 24.35,
      "low": 24.31,
      "close": 24.35,
      "volume": 6975,
      "datetime": 1736790180000
    },
    {
      "open": 24.33,
      "high": 24.33,
      "low": 24.33,
      "close": 24.33,
      "volume": 275,
      "datetime": 1736790240000
    },
    {
      "open": 24.3198,
      "high": 24.3198,
      "low": 24.31,
      "close": 24.31,
      "volume": 3419,
      "datetime": 1736790300000
    },
    {
      "open": 24.28,
      "high": 24.28,
      "low": 24.26,
      "close": 24.26,
      "volume": 10747,
      "datetime": 1736790360000
    },
    {
      "open": 24.2432,
      "high": 24.275,
      "low": 24.2432,
      "close": 24.275,
      "volume": 900,
      "datetime": 1736790420000
    },
    {
      "open": 24.27,
      "high": 24.28,
      "low": 24.27,
      "close": 24.278808,
      "volume": 3106,
      "datetime": 1736790480000
    },
    {
      "open": 24.275,
      "high": 24.305,
      "low": 24.275,
      "close": 24.305,
      "volume": 3349,
      "datetime": 1736790540000
    },
    {
      "open": 24.31,
      "high": 24.31,
      "low": 24.28,
      "close": 24.28,
      "volume": 11831,
      "datetime": 1736790600000
    },
    {
      "open": 24.27,
      "high": 24.28,
      "low": 24.2521,
      "close": 24.28,
      "volume": 2904,
      "datetime": 1736790660000
    },
    {
      "open": 24.265,
      "high": 24.27,
      "low": 24.265,
      "close": 24.27,
      "volume": 1325,
      "datetime": 1736790720000
    },
    {
      "open": 24.315,
      "high": 24.3219,
      "low": 24.315,
      "close": 24.3219,
      "volume": 3400,
      "datetime": 1736790780000
    },
    {
      "open": 24.3201,
      "high": 24.35,
      "low": 24.32,
      "close": 24.33,
      "volume": 1428,
      "datetime": 1736790840000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.31,
      "close": 24.31,
      "volume": 525,
      "datetime": 1736790900000
    },
    {
      "open": 24.325,
      "high": 24.3329,
      "low": 24.325,
      "close": 24.3329,
      "volume": 620,
      "datetime": 1736790960000
    },
    {
      "open": 24.335,
      "high": 24.335,
      "low": 24.285,
      "close": 24.285,
      "volume": 5911,
      "datetime": 1736791020000
    },
    {
      "open": 24.28,
      "high": 24.28,
      "low": 24.27,
      "close": 24.27,
      "volume": 725,
      "datetime": 1736791080000
    },
    {
      "open": 24.255,
      "high": 24.255,
      "low": 24.24,
      "close": 24.24,
      "volume": 2912,
      "datetime": 1736791140000
    },
    {
      "open": 24.25,
      "high": 24.25,
      "low": 24.21,
      "close": 24.215,
      "volume": 2169,
      "datetime": 1736791200000
    },
    {
      "open": 24.195,
      "high": 24.2,
      "low": 24.18,
      "close": 24.18,
      "volume": 3220,
      "datetime": 1736791260000
    },
    {
      "open": 24.19,
      "high": 24.21,
      "low": 24.19,
      "close": 24.2,
      "volume": 350,
      "datetime": 1736791320000
    },
    {
      "open": 24.18,
      "high": 24.18,
      "low": 24.16,
      "close": 24.16,
      "volume": 325,
      "datetime": 1736791380000
    },
    {
      "open": 24.17,
      "high": 24.17,
      "low": 24.17,
      "close": 24.17,
      "volume": 150,
      "datetime": 1736791440000
    },
    {
      "open": 24.18,
      "high": 24.18,
      "low": 24.17,
      "close": 24.18,
      "volume": 700,
      "datetime": 1736791500000
    },
    {
      "open": 24.19,
      "high": 24.19,
      "low": 24.155,
      "close": 24.155,
      "volume": 325,
      "datetime": 1736791560000
    },
    {
      "open": 24.16,
      "high": 24.1651,
      "low": 24.1401,
      "close": 24.1651,
      "volume": 8499,
      "datetime": 1736791620000
    },
    {
      "open": 24.145,
      "high": 24.15,
      "low": 24.145,
      "close": 24.15,
      "volume": 1025,
      "datetime": 1736791680000
    },
    {
      "open": 24.18,
      "high": 24.19,
      "low": 24.18,
      "close": 24.19,
      "volume": 1537,
      "datetime": 1736791740000
    },
    {
      "open": 24.1812,
      "high": 24.1812,
      "low": 24.1812,
      "close": 24.1812,
      "volume": 100,
      "datetime": 1736791800000
    },
    {
      "open": 24.19,
      "high": 24.23,
      "low": 24.19,
      "close": 24.23,
      "volume": 1150,
      "datetime": 1736791860000
    },
    {
      "open": 24.25,
      "high": 24.25,
      "low": 24.25,
      "close": 24.25,
      "volume": 125,
      "datetime": 1736791920000
    },
    {
      "open": 24.27,
      "high": 24.29,
      "low": 24.27,
      "close": 24.275,
      "volume": 1050,
      "datetime": 1736791980000
    },
    {
      "open": 24.24,
      "high": 24.24,
      "low": 24.2312,
      "close": 24.2312,
      "volume": 225,
      "datetime": 1736792040000
    },
    {
      "open": 24.24,
      "high": 24.26,
      "low": 24.235,
      "close": 24.25,
      "volume": 1512,
      "datetime": 1736792100000
    },
    {
      "open": 24.24,
      "high": 24.27,
      "low": 24.24,
      "close": 24.27,
      "volume": 2800,
      "datetime": 1736792160000
    },
    {
      "open": 24.29,
      "high": 24.29,
      "low": 24.28,
      "close": 24.28,
      "volume": 375,
      "datetime": 1736792220000
    },
    {
      "open": 24.3,
      "high": 24.318,
      "low": 24.2988,
      "close": 24.318,
      "volume": 500,
      "datetime": 1736792280000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.2967,
      "close": 24.3,
      "volume": 1425,
      "datetime": 1736792340000
    },
    {
      "open": 24.3,
      "high": 24.34,
      "low": 24.3,
      "close": 24.34,
      "volume": 2548,
      "datetime": 1736792400000
    },
    {
      "open": 24.315,
      "high": 24.33,
      "low": 24.315,
      "close": 24.33,
      "volume": 6987,
      "datetime": 1736792460000
    },
    {
      "open": 24.34,
      "high": 24.35,
      "low": 24.335,
      "close": 24.335,
      "volume": 3055,
      "datetime": 1736792520000
    },
    {
      "open": 24.33,
      "high": 24.33,
      "low": 24.31,
      "close": 24.31,
      "volume": 614,
      "datetime": 1736792580000
    },
    {
      "open": 24.34,
      "high": 24.35,
      "low": 24.34,
      "close": 24.35,
      "volume": 755,
      "datetime": 1736792640000
    },
    {
      "open": 24.34,
      "high": 24.34,
      "low": 24.3,
      "close": 24.3,
      "volume": 3055,
      "datetime": 1736792700000
    },
    {
      "open": 24.3,
      "high": 24.3399,
      "low": 24.3,
      "close": 24.32,
      "volume": 1125,
      "datetime": 1736792760000
    },
    {
      "open": 24.31,
      "high": 24.34,
      "low": 24.31,
      "close": 24.34,
      "volume": 1290,
      "datetime": 1736792820000
    },
    {
      "open": 24.3445,
      "high": 24.3445,
      "low": 24.32,
      "close": 24.33,
      "volume": 15125,
      "datetime": 1736792880000
    },
    {
      "open": 24.32,
      "high": 24.33,
      "low": 24.32,
      "close": 24.32,
      "volume": 1796,
      "datetime": 1736792940000
    },
    {
      "open": 24.28,
      "high": 24.32,
      "low": 24.27,
      "close": 24.27,
      "volume": 1675,
      "datetime": 1736793000000
    },
    {
      "open": 24.29,
      "high": 24.32,
      "low": 24.29,
      "close": 24.3,
      "volume": 475,
      "datetime": 1736793060000
    },
    {
      "open": 24.28,
      "high": 24.28,
      "low": 24.26,
      "close": 24.26,
      "volume": 700,
      "datetime": 1736793120000
    },
    {
      "open": 24.25,
      "high": 24.25,
      "low": 24.25,
      "close": 24.25,
      "volume": 2500,
      "datetime": 1736793180000
    },
    {
      "open": 24.24,
      "high": 24.25,
      "low": 24.24,
      "close": 24.25,
      "volume": 200,
      "datetime": 1736793240000
    },
    {
      "open": 24.22,
      "high": 24.221,
      "low": 24.22,
      "close": 24.22,
      "volume": 5650,
      "datetime": 1736793300000
    },
    {
      "open": 24.21,
      "high": 24.215,
      "low": 24.18,
      "close": 24.19,
      "volume": 17945,
      "datetime": 1736793360000
    },
    {
      "open": 24.2,
      "high": 24.23,
      "low": 24.185,
      "close": 24.22,
      "volume": 9659,
      "datetime": 1736793420000
    },
    {
      "open": 24.22,
      "high": 24.25,
      "low": 24.22,
      "close": 24.22,
      "volume": 12650,
      "datetime": 1736793480000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.2,
      "close": 24.21,
      "volume": 1300,
      "datetime": 1736793540000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.21,
      "close": 24.21,
      "volume": 850,
      "datetime": 1736793600000
    },
    {
      "open": 24.24,
      "high": 24.28,
      "low": 24.22,
      "close": 24.28,
      "volume": 8029,
      "datetime": 1736793660000
    },
    {
      "open": 24.2799,
      "high": 24.28,
      "low": 24.27,
      "close": 24.28,
      "volume": 585,
      "datetime": 1736793720000
    },
    {
      "open": 24.29,
      "high": 24.3069,
      "low": 24.28,
      "close": 24.3069,
      "volume": 10779,
      "datetime": 1736793780000
    },
    {
      "open": 24.31,
      "high": 24.31,
      "low": 24.285,
      "close": 24.29,
      "volume": 1597,
      "datetime": 1736793840000
    },
    {
      "open": 24.3016,
      "high": 24.31,
      "low": 24.29,
      "close": 24.3,
      "volume": 3386,
      "datetime": 1736793900000
    },
    {
      "open": 24.29,
      "high": 24.29,
      "low": 24.23,
      "close": 24.23,
      "volume": 4537,
      "datetime": 1736793960000
    },
    {
      "open": 24.23,
      "high": 24.23,
      "low": 24.215,
      "close": 24.22,
      "volume": 3913,
      "datetime": 1736794020000
    },
    {
      "open": 24.22,
      "high": 24.2401,
      "low": 24.22,
      "close": 24.2301,
      "volume": 2671,
      "datetime": 1736794080000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.195,
      "close": 24.195,
      "volume": 5217,
      "datetime": 1736794140000
    },
    {
      "open": 24.2,
      "high": 24.2,
      "low": 24.19,
      "close": 24.19,
      "volume": 2650,
      "datetime": 1736794200000
    },
    {
      "open": 24.215,
      "high": 24.23,
      "low": 24.1936,
      "close": 24.23,
      "volume": 2575,
      "datetime": 1736794260000
    },
    {
      "open": 24.2382,
      "high": 24.2382,
      "low": 24.23,
      "close": 24.23,
      "volume": 200,
      "datetime": 1736794320000
    },
    {
      "open": 24.24,
      "high": 24.24,
      "low": 24.22,
      "close": 24.23,
      "volume": 2328,
      "datetime": 1736794380000
    },
    {
      "open": 24.26,
      "high": 24.2792,
      "low": 24.26,
      "close": 24.2773,
      "volume": 5300,
      "datetime": 1736794440000
    },
    {
      "open": 24.27,
      "high": 24.27,
      "low": 24.23,
      "close": 24.23,
      "volume": 3635,
      "datetime": 1736794500000
    },
    {
      "open": 24.23,
      "high": 24.23,
      "low": 24.2,
      "close": 24.21,
      "volume": 1724,
      "datetime": 1736794560000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.19,
      "close": 24.19,
      "volume": 350,
      "datetime": 1736794620000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.21,
      "close": 24.21,
      "volume": 2223,
      "datetime": 1736794680000
    },
    {
      "open": 24.22,
      "high": 24.23,
      "low": 24.21,
      "close": 24.21,
      "volume": 975,
      "datetime": 1736794740000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.21,
      "close": 24.21,
      "volume": 700,
      "datetime": 1736794800000
    },
    {
      "open": 24.19,
      "high": 24.19,
      "low": 24.17,
      "close": 24.17,
      "volume": 8344,
      "datetime": 1736794860000
    },
    {
      "open": 24.2,
      "high": 24.22,
      "low": 24.19,
      "close": 24.21,
      "volume": 1777,
      "datetime": 1736794920000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.2,
      "close": 24.21,
      "volume": 438,
      "datetime": 1736794980000
    },
    {
      "open": 24.18,
      "high": 24.18,
      "low": 24.1767,
      "close": 24.1767,
      "volume": 6171,
      "datetime": 1736795040000
    },
    {
      "open": 24.1701,
      "high": 24.18,
      "low": 24.1699,
      "close": 24.17,
      "volume": 1550,
      "datetime": 1736795100000
    },
    {
      "open": 24.16,
      "high": 24.18,
      "low": 24.16,
      "close": 24.18,
      "volume": 1850,
      "datetime": 1736795160000
    },
    {
      "open": 24.16,
      "high": 24.17,
      "low": 24.16,
      "close": 24.17,
      "volume": 1500,
      "datetime": 1736795220000
    },
    {
      "open": 24.17,
      "high": 24.2,
      "low": 24.17,
      "close": 24.19,
      "volume": 4545,
      "datetime": 1736795280000
    },
    {
      "open": 24.19,
      "high": 24.19,
      "low": 24.17,
      "close": 24.17,
      "volume": 979,
      "datetime": 1736795340000
    },
    {
      "open": 24.19,
      "high": 24.19,
      "low": 24.17,
      "close": 24.17,
      "volume": 636,
      "datetime": 1736795400000
    },
    {
      "open": 24.19,
      "high": 24.2,
      "low": 24.1812,
      "close": 24.2,
      "volume": 528,
      "datetime": 1736795460000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.21,
      "close": 24.21,
      "volume": 400,
      "datetime": 1736795520000
    },
    {
      "open": 24.21,
      "high": 24.25,
      "low": 24.21,
      "close": 24.25,
      "volume": 8525,
      "datetime": 1736795580000
    },
    {
      "open": 24.2535,
      "high": 24.255,
      "low": 24.23,
      "close": 24.25,
      "volume": 5647,
      "datetime": 1736795640000
    },
    {
      "open": 24.26,
      "high": 24.28,
      "low": 24.26,
      "close": 24.26,
      "volume": 1800,
      "datetime": 1736795700000
    },
    {
      "open": 24.26,
      "high": 24.28,
      "low": 24.26,
      "close": 24.28,
      "volume": 1000,
      "datetime": 1736795760000
    },
    {
      "open": 24.29,
      "high": 24.3165,
      "low": 24.29,
      "close": 24.3165,
      "volume": 997,
      "datetime": 1736795820000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.29,
      "close": 24.29,
      "volume": 1343,
      "datetime": 1736795880000
    },
    {
      "open": 24.29,
      "high": 24.2951,
      "low": 24.29,
      "close": 24.2951,
      "volume": 2603,
      "datetime": 1736795940000
    },
    {
      "open": 24.31,
      "high": 24.3497,
      "low": 24.31,
      "close": 24.3497,
      "volume": 636,
      "datetime": 1736796000000
    },
    {
      "open": 24.34,
      "high": 24.34,
      "low": 24.31,
      "close": 24.31,
      "volume": 1335,
      "datetime": 1736796060000
    },
    {
      "open": 24.32,
      "high": 24.32,
      "low": 24.28,
      "close": 24.29,
      "volume": 6755,
      "datetime": 1736796120000
    },
    {
      "open": 24.3,
      "high": 24.31,
      "low": 24.29,
      "close": 24.31,
      "volume": 1151,
      "datetime": 1736796180000
    },
    {
      "open": 24.31,
      "high": 24.31,
      "low": 24.28,
      "close": 24.28,
      "volume": 1015,
      "datetime": 1736796240000
    },
    {
      "open": 24.27,
      "high": 24.27,
      "low": 24.25,
      "close": 24.25,
      "volume": 975,
      "datetime": 1736796300000
    },
    {
      "open": 24.24,
      "high": 24.24,
      "low": 24.24,
      "close": 24.24,
      "volume": 425,
      "datetime": 1736796360000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.21,
      "close": 24.21,
      "volume": 237,
      "datetime": 1736796420000
    },
    {
      "open": 24.225,
      "high": 24.23,
      "low": 24.21,
      "close": 24.21,
      "volume": 4836,
      "datetime": 1736796480000
    },
    {
      "open": 24.1998,
      "high": 24.2072,
      "low": 24.1998,
      "close": 24.2,
      "volume": 400,
      "datetime": 1736796540000
    },
    {
      "open": 24.19,
      "high": 24.19,
      "low": 24.18,
      "close": 24.19,
      "volume": 675,
      "datetime": 1736796600000
    },
    {
      "open": 24.2,
      "high": 24.21,
      "low": 24.2,
      "close": 24.21,
      "volume": 1608,
      "datetime": 1736796660000
    },
    {
      "open": 24.2,
      "high": 24.2,
      "low": 24.18,
      "close": 24.1821,
      "volume": 10541,
      "datetime": 1736796720000
    },
    {
      "open": 24.18,
      "high": 24.2,
      "low": 24.18,
      "close": 24.2,
      "volume": 950,
      "datetime": 1736796780000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.21,
      "close": 24.22,
      "volume": 8614,
      "datetime": 1736796840000
    },
    {
      "open": 24.22,
      "high": 24.24,
      "low": 24.215,
      "close": 24.215,
      "volume": 7201,
      "datetime": 1736796900000
    },
    {
      "open": 24.215,
      "high": 24.22,
      "low": 24.185,
      "close": 24.22,
      "volume": 1443,
      "datetime": 1736796960000
    },
    {
      "open": 24.23,
      "high": 24.23,
      "low": 24.21,
      "close": 24.21,
      "volume": 709,
      "datetime": 1736797020000
    },
    {
      "open": 24.2201,
      "high": 24.225,
      "low": 24.19,
      "close": 24.19,
      "volume": 1550,
      "datetime": 1736797080000
    },
    {
      "open": 24.19,
      "high": 24.19,
      "low": 24.19,
      "close": 24.19,
      "volume": 250,
      "datetime": 1736797140000
    },
    {
      "open": 24.18,
      "high": 24.18,
      "low": 24.17,
      "close": 24.17,
      "volume": 8825,
      "datetime": 1736797200000
    },
    {
      "open": 24.17,
      "high": 24.17,
      "low": 24.14,
      "close": 24.14,
      "volume": 2400,
      "datetime": 1736797260000
    },
    {
      "open": 24.15,
      "high": 24.1501,
      "low": 24.14,
      "close": 24.14,
      "volume": 1833,
      "datetime": 1736797320000
    },
    {
      "open": 24.1411,
      "high": 24.15,
      "low": 24.14,
      "close": 24.14,
      "volume": 2427,
      "datetime": 1736797380000
    },
    {
      "open": 24.15,
      "high": 24.15,
      "low": 24.13,
      "close": 24.14,
      "volume": 7978,
      "datetime": 1736797440000
    },
    {
      "open": 24.1531,
      "high": 24.1531,
      "low": 24.12,
      "close": 24.13,
      "volume": 8642,
      "datetime": 1736797500000
    },
    {
      "open": 24.13,
      "high": 24.14,
      "low": 24.13,
      "close": 24.14,
      "volume": 1093,
      "datetime": 1736797560000
    },
    {
      "open": 24.15,
      "high": 24.15,
      "low": 24.13,
      "close": 24.15,
      "volume": 2570,
      "datetime": 1736797620000
    },
    {
      "open": 24.15,
      "high": 24.16,
      "low": 24.13,
      "close": 24.16,
      "volume": 3266,
      "datetime": 1736797680000
    },
    {
      "open": 24.17,
      "high": 24.205,
      "low": 24.17,
      "close": 24.205,
      "volume": 12702,
      "datetime": 1736797740000
    },
    {
      "open": 24.2099,
      "high": 24.2099,
      "low": 24.18,
      "close": 24.2,
      "volume": 5098,
      "datetime": 1736797800000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.21,
      "close": 24.21,
      "volume": 150,
      "datetime": 1736797860000
    },
    {
      "open": 24.23,
      "high": 24.24,
      "low": 24.23,
      "close": 24.24,
      "volume": 6295,
      "datetime": 1736797920000
    },
    {
      "open": 24.241,
      "high": 24.241,
      "low": 24.2205,
      "close": 24.235,
      "volume": 5350,
      "datetime": 1736797980000
    },
    {
      "open": 24.24,
      "high": 24.24,
      "low": 24.21,
      "close": 24.21,
      "volume": 9698,
      "datetime": 1736798040000
    },
    {
      "open": 24.16,
      "high": 24.19,
      "low": 24.16,
      "close": 24.18,
      "volume": 4805,
      "datetime": 1736798100000
    },
    {
      "open": 24.18,
      "high": 24.21,
      "low": 24.175,
      "close": 24.21,
      "volume": 1525,
      "datetime": 1736798160000
    },
    {
      "open": 24.17,
      "high": 24.17,
      "low": 24.15,
      "close": 24.16,
      "volume": 450,
      "datetime": 1736798220000
    },
    {
      "open": 24.1591,
      "high": 24.16,
      "low": 24.1591,
      "close": 24.16,
      "volume": 514,
      "datetime": 1736798280000
    },
    {
      "open": 24.14,
      "high": 24.1613,
      "low": 24.14,
      "close": 24.16,
      "volume": 825,
      "datetime": 1736798340000
    },
    {
      "open": 24.17,
      "high": 24.1901,
      "low": 24.17,
      "close": 24.19,
      "volume": 1300,
      "datetime": 1736798400000
    },
    {
      "open": 24.16,
      "high": 24.18,
      "low": 24.15,
      "close": 24.15,
      "volume": 1905,
      "datetime": 1736798520000
    },
    {
      "open": 24.17,
      "high": 24.18,
      "low": 24.17,
      "close": 24.18,
      "volume": 475,
      "datetime": 1736798580000
    },
    {
      "open": 24.19,
      "high": 24.21,
      "low": 24.17,
      "close": 24.21,
      "volume": 967,
      "datetime": 1736798640000
    },
    {
      "open": 24.21,
      "high": 24.21,
      "low": 24.19,
      "close": 24.19,
      "volume": 325,
      "datetime": 1736798700000
    },
    {
      "open": 24.2,
      "high": 24.23,
      "low": 24.2,
      "close": 24.23,
      "volume": 1145,
      "datetime": 1736798760000
    },
    {
      "open": 24.24,
      "high": 24.24,
      "low": 24.22,
      "close": 24.2201,
      "volume": 1907,
      "datetime": 1736798820000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.16,
      "close": 24.1798,
      "volume": 3920,
      "datetime": 1736798880000
    },
    {
      "open": 24.2,
      "high": 24.22,
      "low": 24.2,
      "close": 24.22,
      "volume": 425,
      "datetime": 1736798940000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.22,
      "close": 24.22,
      "volume": 300,
      "datetime": 1736799000000
    },
    {
      "open": 24.24,
      "high": 24.245,
      "low": 24.24,
      "close": 24.24,
      "volume": 450,
      "datetime": 1736799060000
    },
    {
      "open": 24.233026,
      "high": 24.2552,
      "low": 24.233026,
      "close": 24.2552,
      "volume": 825,
      "datetime": 1736799120000
    },
    {
      "open": 24.245,
      "high": 24.245,
      "low": 24.235,
      "close": 24.24,
      "volume": 1414,
      "datetime": 1736799180000
    },
    {
      "open": 24.2452,
      "high": 24.25,
      "low": 24.2452,
      "close": 24.25,
      "volume": 3100,
      "datetime": 1736799240000
    },
    {
      "open": 24.26,
      "high": 24.27,
      "low": 24.26,
      "close": 24.26,
      "volume": 1450,
      "datetime": 1736799300000
    },
    {
      "open": 24.26,
      "high": 24.26,
      "low": 24.2512,
      "close": 24.26,
      "volume": 525,
      "datetime": 1736799360000
    },
    {
      "open": 24.255,
      "high": 24.255,
      "low": 24.22,
      "close": 24.22,
      "volume": 1866,
      "datetime": 1736799420000
    },
    {
      "open": 24.2288,
      "high": 24.24,
      "low": 24.2288,
      "close": 24.24,
      "volume": 350,
      "datetime": 1736799480000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.2,
      "close": 24.2,
      "volume": 1100,
      "datetime": 1736799540000
    },
    {
      "open": 24.2,
      "high": 24.2,
      "low": 24.1884,
      "close": 24.1884,
      "volume": 3104,
      "datetime": 1736799600000
    },
    {
      "open": 24.17,
      "high": 24.1769,
      "low": 24.17,
      "close": 24.1769,
      "volume": 1475,
      "datetime": 1736799660000
    },
    {
      "open": 24.17,
      "high": 24.19,
      "low": 24.1675,
      "close": 24.17,
      "volume": 5523,
      "datetime": 1736799720000
    },
    {
      "open": 24.17,
      "high": 24.2188,
      "low": 24.17,
      "close": 24.21,
      "volume": 4697,
      "datetime": 1736799780000
    },
    {
      "open": 24.23,
      "high": 24.24,
      "low": 24.23,
      "close": 24.235,
      "volume": 969,
      "datetime": 1736799840000
    },
    {
      "open": 24.22,
      "high": 24.2228,
      "low": 24.2139,
      "close": 24.22,
      "volume": 1585,
      "datetime": 1736799900000
    },
    {
      "open": 24.225,
      "high": 24.225,
      "low": 24.225,
      "close": 24.225,
      "volume": 333,
      "datetime": 1736799960000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.21,
      "close": 24.21,
      "volume": 300,
      "datetime": 1736800020000
    },
    {
      "open": 24.21,
      "high": 24.23,
      "low": 24.21,
      "close": 24.23,
      "volume": 23643,
      "datetime": 1736800080000
    },
    {
      "open": 24.23,
      "high": 24.23,
      "low": 24.23,
      "close": 24.23,
      "volume": 950,
      "datetime": 1736800140000
    },
    {
      "open": 24.22,
      "high": 24.22,
      "low": 24.1974,
      "close": 24.2,
      "volume": 1872,
      "datetime": 1736800200000
    },
    {
      "open": 24.2,
      "high": 24.21,
      "low": 24.2,
      "close": 24.205,
      "volume": 2500,
      "datetime": 1736800260000
    },
    {
      "open": 24.18,
      "high": 24.18,
      "low": 24.17,
      "close": 24.175,
      "volume": 1575,
      "datetime": 1736800320000
    },
    {
      "open": 24.17,
      "high": 24.17,
      "low": 24.1681,
      "close": 24.1681,
      "volume": 300,
      "datetime": 1736800380000
    },
    {
      "open": 24.1584,
      "high": 24.1584,
      "low": 24.13,
      "close": 24.13,
      "volume": 2683,
      "datetime": 1736800440000
    },
    {
      "open": 24.13,
      "high": 24.13,
      "low": 24.1198,
      "close": 24.12,
      "volume": 12181,
      "datetime": 1736800500000
    },
    {
      "open": 24.11,
      "high": 24.1288,
      "low": 24.095,
      "close": 24.095,
      "volume": 9335,
      "datetime": 1736800560000
    },
    {
      "open": 24.09,
      "high": 24.1058,
      "low": 24.07,
      "close": 24.07,
      "volume": 5441,
      "datetime": 1736800620000
    },
    {
      "open": 24.075,
      "high": 24.075,
      "low": 24.045,
      "close": 24.06,
      "volume": 3217,
      "datetime": 1736800680000
    },
    {
      "open": 24.0599,
      "high": 24.07,
      "low": 24.0599,
      "close": 24.07,
      "volume": 2362,
      "datetime": 1736800740000
    },
    {
      "open": 24.06,
      "high": 24.06,
      "low": 24.0299,
      "close": 24.0299,
      "volume": 1500,
      "datetime": 1736800800000
    },
    {
      "open": 24.0272,
      "high": 24.03,
      "low": 24.01,
      "close": 24.02,
      "volume": 19794,
      "datetime": 1736800860000
    },
    {
      "open": 24.01,
      "high": 24.01,
      "low": 23.9882,
      "close": 23.9882,
      "volume": 2695,
      "datetime": 1736800920000
    },
    {
      "open": 23.995,
      "high": 23.995,
      "low": 23.98,
      "close": 23.99,
      "volume": 33766,
      "datetime": 1736800980000
    },
    {
      "open": 24,
      "high": 24,
      "low": 24,
      "close": 24,
      "volume": 530,
      "datetime": 1736801040000
    },
    {
      "open": 23.98,
      "high": 23.98,
      "low": 23.92,
      "close": 23.93,
      "volume": 11406,
      "datetime": 1736801100000
    },
    {
      "open": 23.9319,
      "high": 23.955,
      "low": 23.92,
      "close": 23.95,
      "volume": 7201,
      "datetime": 1736801160000
    },
    {
      "open": 23.96,
      "high": 23.98,
      "low": 23.95,
      "close": 23.95,
      "volume": 1679,
      "datetime": 1736801220000
    },
    {
      "open": 23.94,
      "high": 23.94,
      "low": 23.92,
      "close": 23.92,
      "volume": 575,
      "datetime": 1736801280000
    },
    {
      "open": 23.92,
      "high": 23.92,
      "low": 23.91,
      "close": 23.91,
      "volume": 435,
      "datetime": 1736801340000
    },
    {
      "open": 23.91,
      "high": 23.92,
      "low": 23.9,
      "close": 23.9,
      "volume": 1125,
      "datetime": 1736801400000
    },
    {
      "open": 23.875,
      "high": 23.88,
      "low": 23.82,
      "close": 23.82,
      "volume": 9185,
      "datetime": 1736801460000
    },
    {
      "open": 23.815,
      "high": 23.8298,
      "low": 23.8,
      "close": 23.8152,
      "volume": 1499,
      "datetime": 1736801520000
    },
    {
      "open": 23.81,
      "high": 23.8501,
      "low": 23.7922,
      "close": 23.8501,
      "volume": 1943,
      "datetime": 1736801580000
    },
    {
      "open": 23.86,
      "high": 23.87,
      "low": 23.8326,
      "close": 23.8482,
      "volume": 12837,
      "datetime": 1736801640000
    },
    {
      "open": 23.83,
      "high": 23.83,
      "low": 23.791,
      "close": 23.791,
      "volume": 3596,
      "datetime": 1736801700000
    },
    {
      "open": 23.795,
      "high": 23.86,
      "low": 23.795,
      "close": 23.85,
      "volume": 7594,
      "datetime": 1736801760000
    },
    {
      "open": 23.8401,
      "high": 23.8401,
      "low": 23.803,
      "close": 23.81,
      "volume": 10097,
      "datetime": 1736801820000
    },
    {
      "open": 23.82,
      "high": 23.8389,
      "low": 23.8099,
      "close": 23.81,
      "volume": 10061,
      "datetime": 1736801880000
    },
    {
      "open": 23.81,
      "high": 23.865,
      "low": 23.81,
      "close": 23.84,
      "volume": 53814,
      "datetime": 1736801940000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.82,
      "close": 23.82,
      "volume": 54357,
      "datetime": 1736802000000
    },
    {
      "open": 23.85,
      "high": 23.85,
      "low": 23.85,
      "close": 23.85,
      "volume": 1000,
      "datetime": 1736802240000
    },
    {
      "open": 23.88,
      "high": 23.88,
      "low": 23.8,
      "close": 23.8,
      "volume": 600,
      "datetime": 1736802300000
    },
    {
      "open": 23.84,
      "high": 23.84,
      "low": 23.84,
      "close": 23.84,
      "volume": 500,
      "datetime": 1736802420000
    },
    {
      "open": 23.79,
      "high": 23.83,
      "low": 23.79,
      "close": 23.83,
      "volume": 1110,
      "datetime": 1736802480000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 200,
      "datetime": 1736802600000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.76,
      "close": 23.76,
      "volume": 1101,
      "datetime": 1736802720000
    },
    {
      "open": 23.76,
      "high": 23.76,
      "low": 23.7501,
      "close": 23.7501,
      "volume": 5333,
      "datetime": 1736802960000
    },
    {
      "open": 23.8,
      "high": 23.8,
      "low": 23.8,
      "close": 23.8,
      "volume": 332,
      "datetime": 1736803500000
    },
    {
      "open": 23.8295,
      "high": 23.8295,
      "low": 23.8295,
      "close": 23.8295,
      "volume": 5000,
      "datetime": 1736803620000
    },
    {
      "open": 23.75,
      "high": 23.75,
      "low": 23.75,
      "close": 23.75,
      "volume": 239,
      "datetime": 1736803860000
    },
    {
      "open": 23.789,
      "high": 23.789,
      "low": 23.789,
      "close": 23.789,
      "volume": 150,
      "datetime": 1736804100000
    },
    {
      "open": 23.74,
      "high": 23.74,
      "low": 23.74,
      "close": 23.74,
      "volume": 630,
      "datetime": 1736804220000
    },
    {
      "open": 23.72,
      "high": 23.72,
      "low": 23.72,
      "close": 23.72,
      "volume": 1225,
      "datetime": 1736804280000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.64,
      "close": 23.64,
      "volume": 300,
      "datetime": 1736804460000
    },
    {
      "open": 23.63,
      "high": 23.63,
      "low": 23.63,
      "close": 23.63,
      "volume": 200,
      "datetime": 1736804580000
    },
    {
      "open": 23.61,
      "high": 23.6201,
      "low": 23.61,
      "close": 23.6201,
      "volume": 5356,
      "datetime": 1736804640000
    },
    {
      "open": 23.6002,
      "high": 23.62,
      "low": 23.6002,
      "close": 23.62,
      "volume": 1990,
      "datetime": 1736804700000
    },
    {
      "open": 23.61,
      "high": 23.61,
      "low": 23.61,
      "close": 23.61,
      "volume": 100,
      "datetime": 1736804820000
    },
    {
      "open": 23.6105,
      "high": 23.6105,
      "low": 23.6105,
      "close": 23.6105,
      "volume": 300,
      "datetime": 1736805120000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 100,
      "datetime": 1736805780000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.64,
      "close": 23.64,
      "volume": 100,
      "datetime": 1736805840000
    },
    {
      "open": 23.63,
      "high": 23.63,
      "low": 23.63,
      "close": 23.63,
      "volume": 2000,
      "datetime": 1736805900000
    },
    {
      "open": 23.62,
      "high": 23.62,
      "low": 23.62,
      "close": 23.62,
      "volume": 100,
      "datetime": 1736806080000
    },
    {
      "open": 23.6002,
      "high": 23.6018,
      "low": 23.6,
      "close": 23.6018,
      "volume": 400,
      "datetime": 1736806260000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 300,
      "datetime": 1736806320000
    },
    {
      "open": 23.5601,
      "high": 23.5601,
      "low": 23.5601,
      "close": 23.5601,
      "volume": 1314,
      "datetime": 1736806440000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 200,
      "datetime": 1736806740000
    },
    {
      "open": 23.5611,
      "high": 23.5611,
      "low": 23.5611,
      "close": 23.5611,
      "volume": 200,
      "datetime": 1736806980000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.56,
      "close": 23.56,
      "volume": 500,
      "datetime": 1736807040000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 100,
      "datetime": 1736807280000
    },
    {
      "open": 23.5553,
      "high": 23.5553,
      "low": 23.5553,
      "close": 23.5553,
      "volume": 200,
      "datetime": 1736807340000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 1933,
      "datetime": 1736807820000
    },
    {
      "open": 23.6093,
      "high": 23.6093,
      "low": 23.6093,
      "close": 23.6093,
      "volume": 140,
      "datetime": 1736808120000
    },
    {
      "open": 23.61,
      "high": 23.73,
      "low": 23.61,
      "close": 23.73,
      "volume": 983,
      "datetime": 1736808300000
    },
    {
      "open": 23.7,
      "high": 23.7,
      "low": 23.7,
      "close": 23.7,
      "volume": 200,
      "datetime": 1736808960000
    },
    {
      "open": 23.67,
      "high": 23.67,
      "low": 23.67,
      "close": 23.67,
      "volume": 200,
      "datetime": 1736809320000
    },
    {
      "open": 23.69,
      "high": 23.69,
      "low": 23.64,
      "close": 23.69,
      "volume": 516,
      "datetime": 1736809500000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 200,
      "datetime": 1736809620000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 700,
      "datetime": 1736809800000
    },
    {
      "open": 23.65,
      "high": 23.65,
      "low": 23.65,
      "close": 23.65,
      "volume": 2000,
      "datetime": 1736809980000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 203,
      "datetime": 1736811300000
    },
    {
      "open": 23.6001,
      "high": 23.6001,
      "low": 23.6001,
      "close": 23.6001,
      "volume": 500,
      "datetime": 1736811360000
    },
    {
      "open": 23.66,
      "high": 23.66,
      "low": 23.66,
      "close": 23.66,
      "volume": 1500,
      "datetime": 1736812140000
    },
    {
      "open": 23.5995,
      "high": 23.5999,
      "low": 23.5995,
      "close": 23.5999,
      "volume": 300,
      "datetime": 1736812620000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.58,
      "close": 23.58,
      "volume": 100,
      "datetime": 1736812740000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 174,
      "datetime": 1736812860000
    },
    {
      "open": 23.59,
      "high": 23.59,
      "low": 23.58,
      "close": 23.58,
      "volume": 900,
      "datetime": 1736813340000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.58,
      "close": 23.58,
      "volume": 100,
      "datetime": 1736813460000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.55,
      "close": 23.55,
      "volume": 100,
      "datetime": 1736814000000
    },
    {
      "open": 23.57,
      "high": 23.57,
      "low": 23.56,
      "close": 23.56,
      "volume": 200,
      "datetime": 1736814600000
    },
    {
      "open": 23.59,
      "high": 23.59,
      "low": 23.59,
      "close": 23.59,
      "volume": 154,
      "datetime": 1736815200000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.64,
      "close": 23.64,
      "volume": 1000,
      "datetime": 1736815380000
    },
    {
      "open": 23.66,
      "high": 23.66,
      "low": 23.66,
      "close": 23.66,
      "volume": 500,
      "datetime": 1736815500000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.58,
      "close": 23.58,
      "volume": 100,
      "datetime": 1736815620000
    },
    {
      "open": 23.64,
      "high": 23.64,
      "low": 23.64,
      "close": 23.64,
      "volume": 100,
      "datetime": 1736816100000
    },
    {
      "open": 23.5815,
      "high": 23.6489,
      "low": 23.5815,
      "close": 23.6489,
      "volume": 3200,
      "datetime": 1736816280000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 100,
      "datetime": 1736816580000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 30,
      "datetime": 1736817000000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 1,
      "datetime": 1736817240000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 799,
      "datetime": 1736817360000
    },
    {
      "open": 23.62,
      "high": 23.62,
      "low": 23.62,
      "close": 23.62,
      "volume": 1,
      "datetime": 1736817420000
    },
    {
      "open": 23.59,
      "high": 23.59,
      "low": 23.59,
      "close": 23.59,
      "volume": 2,
      "datetime": 1736817720000
    },
    {
      "open": 23.6,
      "high": 23.6,
      "low": 23.6,
      "close": 23.6,
      "volume": 1,
      "datetime": 1736817840000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 991,
      "datetime": 1736818320000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 1269,
      "datetime": 1736818440000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.47,
      "close": 23.47,
      "volume": 6002,
      "datetime": 1736818500000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 60,
      "datetime": 1736818620000
    },
    {
      "open": 23.58,
      "high": 23.58,
      "low": 23.57,
      "close": 23.57,
      "volume": 10,
      "datetime": 1736818680000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.55,
      "close": 23.55,
      "volume": 5,
      "datetime": 1736818740000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.56,
      "close": 23.56,
      "volume": 41,
      "datetime": 1736818800000
    },
    {
      "open": 23.55,
      "high": 23.55,
      "low": 23.55,
      "close": 23.55,
      "volume": 1,
      "datetime": 1736819280000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 16,
      "datetime": 1736819640000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 440,
      "datetime": 1736820180000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 500,
      "datetime": 1736820360000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 1,
      "datetime": 1736820960000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 4,
      "datetime": 1736821080000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 20,
      "datetime": 1736821440000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.44,
      "close": 23.44,
      "volume": 10,
      "datetime": 1736821500000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 1,
      "datetime": 1736821680000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 1,
      "datetime": 1736822100000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 1,
      "datetime": 1736822280000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 1502,
      "datetime": 1736822340000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 392,
      "datetime": 1736822880000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 42,
      "datetime": 1736822940000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 2,
      "datetime": 1736823000000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 1,
      "datetime": 1736823180000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 503,
      "datetime": 1736823420000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 5,
      "datetime": 1736823960000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.52,
      "close": 23.52,
      "volume": 5,
      "datetime": 1736824200000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 5,
      "datetime": 1736824380000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.51,
      "close": 23.51,
      "volume": 10,
      "datetime": 1736824440000
    },
    {
      "open": 23.56,
      "high": 23.56,
      "low": 23.53,
      "close": 23.53,
      "volume": 15,
      "datetime": 1736824500000
    },
    {
      "open": 23.52,
      "high": 23.52,
      "low": 23.51,
      "close": 23.51,
      "volume": 10,
      "datetime": 1736824560000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 1,
      "datetime": 1736824680000
    },
    {
      "open": 23.51,
      "high": 23.51,
      "low": 23.51,
      "close": 23.51,
      "volume": 5,
      "datetime": 1736824740000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 5,
      "datetime": 1736824800000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 1,
      "datetime": 1736825940000
    },
    {
      "open": 23.53,
      "high": 23.53,
      "low": 23.53,
      "close": 23.53,
      "volume": 1000,
      "datetime": 1736827200000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 5,
      "datetime": 1736827680000
    },
    {
      "open": 23.46,
      "high": 23.46,
      "low": 23.46,
      "close": 23.46,
      "volume": 50,
      "datetime": 1736827800000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 5,
      "datetime": 1736828400000
    },
    {
      "open": 23.47,
      "high": 23.47,
      "low": 23.47,
      "close": 23.47,
      "volume": 316,
      "datetime": 1736830260000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 528,
      "datetime": 1736830320000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.44,
      "close": 23.44,
      "volume": 3,
      "datetime": 1736830440000
    },
    {
      "open": 23.43,
      "high": 23.43,
      "low": 23.43,
      "close": 23.43,
      "volume": 102,
      "datetime": 1736830560000
    },
    {
      "open": 23.41,
      "high": 23.41,
      "low": 23.41,
      "close": 23.41,
      "volume": 10,
      "datetime": 1736830860000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 55,
      "datetime": 1736831040000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.35,
      "close": 23.35,
      "volume": 50,
      "datetime": 1736831220000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.3,
      "close": 23.3,
      "volume": 8,
      "datetime": 1736831340000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.33,
      "close": 23.33,
      "volume": 10,
      "datetime": 1736831640000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.35,
      "close": 23.35,
      "volume": 20,
      "datetime": 1736831700000
    },
    {
      "open": 23.4,
      "high": 23.41,
      "low": 23.4,
      "close": 23.41,
      "volume": 4,
      "datetime": 1736831940000
    },
    {
      "open": 23.39,
      "high": 23.39,
      "low": 23.39,
      "close": 23.39,
      "volume": 108,
      "datetime": 1736832000000
    },
    {
      "open": 23.47,
      "high": 23.48,
      "low": 23.47,
      "close": 23.48,
      "volume": 892,
      "datetime": 1736834040000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 111,
      "datetime": 1736834100000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 20,
      "datetime": 1736834160000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 29,
      "datetime": 1736834340000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 37,
      "datetime": 1736834400000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 34,
      "datetime": 1736834580000
    },
    {
      "open": 23.5,
      "high": 23.51,
      "low": 23.5,
      "close": 23.51,
      "volume": 31,
      "datetime": 1736834880000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 4,
      "datetime": 1736836200000
    },
    {
      "open": 23.45,
      "high": 23.45,
      "low": 23.45,
      "close": 23.45,
      "volume": 69,
      "datetime": 1736838240000
    },
    {
      "open": 23.44,
      "high": 23.44,
      "low": 23.44,
      "close": 23.44,
      "volume": 1,
      "datetime": 1736838300000
    },
    {
      "open": 23.5,
      "high": 23.5,
      "low": 23.5,
      "close": 23.5,
      "volume": 961,
      "datetime": 1736840220000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 9,
      "datetime": 1736840700000
    },
    {
      "open": 23.48,
      "high": 23.49,
      "low": 23.48,
      "close": 23.49,
      "volume": 66,
      "datetime": 1736841000000
    },
    {
      "open": 23.49,
      "high": 23.49,
      "low": 23.49,
      "close": 23.49,
      "volume": 35,
      "datetime": 1736841180000
    },
    {
      "open": 23.48,
      "high": 23.48,
      "low": 23.48,
      "close": 23.48,
      "volume": 1,
      "datetime": 1736841900000
    },
    {
      "open": 23.42,
      "high": 23.42,
      "low": 23.42,
      "close": 23.42,
      "volume": 1,
      "datetime": 1736842140000
    },
    {
      "open": 23.37,
      "high": 23.37,
      "low": 23.37,
      "close": 23.37,
      "volume": 1,
      "datetime": 1736842260000
    },
    {
      "open": 23.32,
      "high": 23.32,
      "low": 23.32,
      "close": 23.32,
      "volume": 1,
      "datetime": 1736842440000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.27,
      "close": 23.27,
      "volume": 15,
      "datetime": 1736842620000
    },
    {
      "open": 23.25,
      "high": 23.25,
      "low": 23.25,
      "close": 23.25,
      "volume": 25,
      "datetime": 1736842680000
    },
    {
      "open": 23.29,
      "high": 23.3,
      "low": 23.29,
      "close": 23.3,
      "volume": 53,
      "datetime": 1736842740000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.33,
      "close": 23.33,
      "volume": 10,
      "datetime": 1736843460000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.3,
      "close": 23.3,
      "volume": 1,
      "datetime": 1736844420000
    },
    {
      "open": 23.4,
      "high": 23.4,
      "low": 23.4,
      "close": 23.4,
      "volume": 1,
      "datetime": 1736844960000
    },
    {
      "open": 23.25,
      "high": 23.25,
      "low": 23.25,
      "close": 23.25,
      "volume": 2530,
      "datetime": 1736845860000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 2396,
      "datetime": 1736846760000
    },
    {
      "open": 23.12,
      "high": 23.12,
      "low": 23.12,
      "close": 23.12,
      "volume": 150,
      "datetime": 1736847060000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.13,
      "close": 23.13,
      "volume": 2561,
      "datetime": 1736847120000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.07,
      "close": 23.07,
      "volume": 1399,
      "datetime": 1736847180000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 100,
      "datetime": 1736847420000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 1000,
      "datetime": 1736847600000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 2561,
      "datetime": 1736847660000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 910,
      "datetime": 1736847900000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 23.02,
      "close": 23.02,
      "volume": 200,
      "datetime": 1736847960000
    },
    {
      "open": 22.89,
      "high": 22.89,
      "low": 22.89,
      "close": 22.89,
      "volume": 250,
      "datetime": 1736848140000
    },
    {
      "open": 22.9,
      "high": 22.9,
      "low": 22.9,
      "close": 22.9,
      "volume": 100,
      "datetime": 1736848380000
    },
    {
      "open": 22.9,
      "high": 22.9,
      "low": 22.9,
      "close": 22.9,
      "volume": 100,
      "datetime": 1736848440000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 1000,
      "datetime": 1736848560000
    },
    {
      "open": 22.93,
      "high": 22.93,
      "low": 22.93,
      "close": 22.93,
      "volume": 100,
      "datetime": 1736849100000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 920,
      "datetime": 1736849700000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 200,
      "datetime": 1736849760000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.99,
      "close": 22.99,
      "volume": 153,
      "datetime": 1736850000000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.98,
      "close": 22.98,
      "volume": 247,
      "datetime": 1736850420000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 100,
      "datetime": 1736850960000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 184,
      "datetime": 1736851320000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.07,
      "close": 23.07,
      "volume": 100,
      "datetime": 1736852520000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.07,
      "close": 23.07,
      "volume": 100,
      "datetime": 1736853300000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 2534,
      "datetime": 1736853420000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 250,
      "datetime": 1736853840000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 100,
      "datetime": 1736854260000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.07,
      "close": 23.07,
      "volume": 1100,
      "datetime": 1736856000000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 249,
      "datetime": 1736856180000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 100,
      "datetime": 1736856360000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.14,
      "close": 23.14,
      "volume": 169,
      "datetime": 1736856420000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.13,
      "close": 23.13,
      "volume": 100,
      "datetime": 1736856600000
    },
    {
      "open": 23.17,
      "high": 23.17,
      "low": 23.17,
      "close": 23.17,
      "volume": 100,
      "datetime": 1736856900000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.15,
      "close": 23.15,
      "volume": 700,
      "datetime": 1736856960000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 161,
      "datetime": 1736857020000
    },
    {
      "open": 23.2,
      "high": 23.2,
      "low": 23.2,
      "close": 23.2,
      "volume": 215,
      "datetime": 1736858580000
    },
    {
      "open": 23.2,
      "high": 23.2,
      "low": 23.2,
      "close": 23.2,
      "volume": 2000,
      "datetime": 1736858640000
    },
    {
      "open": 23.18,
      "high": 23.18,
      "low": 23.18,
      "close": 23.18,
      "volume": 191,
      "datetime": 1736858700000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 250,
      "datetime": 1736858820000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 250,
      "datetime": 1736858940000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 380,
      "datetime": 1736859240000
    },
    {
      "open": 23.22,
      "high": 23.22,
      "low": 23.22,
      "close": 23.22,
      "volume": 999,
      "datetime": 1736859480000
    },
    {
      "open": 23.2,
      "high": 23.2,
      "low": 23.2,
      "close": 23.2,
      "volume": 249,
      "datetime": 1736859600000
    },
    {
      "open": 23.23,
      "high": 23.23,
      "low": 23.23,
      "close": 23.23,
      "volume": 700,
      "datetime": 1736859660000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.26,
      "close": 23.26,
      "volume": 206,
      "datetime": 1736859840000
    },
    {
      "open": 23.24,
      "high": 23.26,
      "low": 23.24,
      "close": 23.26,
      "volume": 8462,
      "datetime": 1736859900000
    },
    {
      "open": 23.2399,
      "high": 23.2399,
      "low": 23.2399,
      "close": 23.2399,
      "volume": 200,
      "datetime": 1736860080000
    },
    {
      "open": 23.23,
      "high": 23.23,
      "low": 23.23,
      "close": 23.23,
      "volume": 200,
      "datetime": 1736860140000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.26,
      "close": 23.26,
      "volume": 300,
      "datetime": 1736860500000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.26,
      "close": 23.26,
      "volume": 1000,
      "datetime": 1736860740000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.26,
      "close": 23.26,
      "volume": 100,
      "datetime": 1736860860000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.2599,
      "close": 23.26,
      "volume": 300,
      "datetime": 1736861040000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.26,
      "close": 23.26,
      "volume": 369,
      "datetime": 1736861160000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.27,
      "close": 23.27,
      "volume": 1100,
      "datetime": 1736861220000
    },
    {
      "open": 23.2994,
      "high": 23.3,
      "low": 23.29,
      "close": 23.3,
      "volume": 1291,
      "datetime": 1736861280000
    },
    {
      "open": 23.21,
      "high": 23.21,
      "low": 22.99,
      "close": 22.99,
      "volume": 3507,
      "datetime": 1736861400000
    },
    {
      "open": 22.91,
      "high": 22.92,
      "low": 22.9006,
      "close": 22.92,
      "volume": 1254,
      "datetime": 1736861460000
    },
    {
      "open": 22.9,
      "high": 23,
      "low": 22.89,
      "close": 23,
      "volume": 3241,
      "datetime": 1736861520000
    },
    {
      "open": 23,
      "high": 23.01,
      "low": 22.99,
      "close": 22.99,
      "volume": 8959,
      "datetime": 1736861580000
    },
    {
      "open": 23.0399,
      "high": 23.04,
      "low": 22.99,
      "close": 22.99,
      "volume": 1003,
      "datetime": 1736861640000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.07,
      "close": 23.07,
      "volume": 205,
      "datetime": 1736861700000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.05,
      "close": 23.05,
      "volume": 3122,
      "datetime": 1736861760000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.05,
      "close": 23.05,
      "volume": 1130,
      "datetime": 1736861820000
    },
    {
      "open": 23.0999,
      "high": 23.1,
      "low": 23.0999,
      "close": 23.1,
      "volume": 1199,
      "datetime": 1736861880000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.1,
      "close": 23.11,
      "volume": 1580,
      "datetime": 1736861940000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 2073,
      "datetime": 1736862000000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.11,
      "close": 23.11,
      "volume": 113,
      "datetime": 1736862060000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 3502,
      "datetime": 1736862120000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 1100,
      "datetime": 1736862180000
    },
    {
      "open": 23.1,
      "high": 23.14,
      "low": 23.1,
      "close": 23.14,
      "volume": 888,
      "datetime": 1736862240000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 999,
      "datetime": 1736862480000
    },
    {
      "open": 23.07,
      "high": 23.0701,
      "low": 23.07,
      "close": 23.0701,
      "volume": 4338,
      "datetime": 1736862540000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 162,
      "datetime": 1736862600000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 800,
      "datetime": 1736862660000
    },
    {
      "open": 23.12,
      "high": 23.12,
      "low": 23.12,
      "close": 23.12,
      "volume": 1000,
      "datetime": 1736862720000
    },
    {
      "open": 23.17,
      "high": 23.17,
      "low": 23.16,
      "close": 23.16,
      "volume": 2615,
      "datetime": 1736863020000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 100,
      "datetime": 1736863140000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 566,
      "datetime": 1736863200000
    },
    {
      "open": 23.18,
      "high": 23.2096,
      "low": 23.18,
      "close": 23.2096,
      "volume": 8554,
      "datetime": 1736863380000
    },
    {
      "open": 23.1802,
      "high": 23.21,
      "low": 23.1802,
      "close": 23.21,
      "volume": 200,
      "datetime": 1736863500000
    },
    {
      "open": 23.2,
      "high": 23.2,
      "low": 23.18,
      "close": 23.18,
      "volume": 400,
      "datetime": 1736863560000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.15,
      "close": 23.15,
      "volume": 1900,
      "datetime": 1736863620000
    },
    {
      "open": 23.1505,
      "high": 23.1505,
      "low": 23.15,
      "close": 23.15,
      "volume": 7482,
      "datetime": 1736863740000
    },
    {
      "open": 23.18,
      "high": 23.18,
      "low": 23.18,
      "close": 23.18,
      "volume": 2000,
      "datetime": 1736863800000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.19,
      "close": 23.19,
      "volume": 2900,
      "datetime": 1736863860000
    },
    {
      "open": 23.189,
      "high": 23.189,
      "low": 23.189,
      "close": 23.189,
      "volume": 100,
      "datetime": 1736863980000
    },
    {
      "open": 23.18,
      "high": 23.18,
      "low": 23.18,
      "close": 23.18,
      "volume": 194,
      "datetime": 1736864040000
    },
    {
      "open": 23.17,
      "high": 23.17,
      "low": 23.17,
      "close": 23.17,
      "volume": 100,
      "datetime": 1736864280000
    },
    {
      "open": 23.081,
      "high": 23.081,
      "low": 23.081,
      "close": 23.081,
      "volume": 100,
      "datetime": 1736864640000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 100,
      "datetime": 1736864760000
    },
    {
      "open": 23.04,
      "high": 23.0401,
      "low": 23.04,
      "close": 23.0401,
      "volume": 1600,
      "datetime": 1736864820000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 300,
      "datetime": 1736864880000
    },
    {
      "open": 23.046,
      "high": 23.046,
      "low": 23.046,
      "close": 23.046,
      "volume": 100,
      "datetime": 1736864940000
    },
    {
      "open": 23.04,
      "high": 23.0401,
      "low": 23,
      "close": 23.0001,
      "volume": 30116,
      "datetime": 1736865000000
    },
    {
      "open": 22.98,
      "high": 23.0053,
      "low": 22.97,
      "close": 23.0053,
      "volume": 8667,
      "datetime": 1736865060000
    },
    {
      "open": 23.0042,
      "high": 23.0587,
      "low": 23.0042,
      "close": 23.02,
      "volume": 3387,
      "datetime": 1736865120000
    },
    {
      "open": 23.04,
      "high": 23.0796,
      "low": 23.02,
      "close": 23.02,
      "volume": 8719,
      "datetime": 1736865180000
    },
    {
      "open": 23,
      "high": 23,
      "low": 22.97,
      "close": 22.97,
      "volume": 10983,
      "datetime": 1736865240000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.93,
      "close": 22.955,
      "volume": 19672,
      "datetime": 1736865300000
    },
    {
      "open": 22.9651,
      "high": 22.99,
      "low": 22.965,
      "close": 22.9792,
      "volume": 6764,
      "datetime": 1736865360000
    },
    {
      "open": 22.9658,
      "high": 22.9697,
      "low": 22.9186,
      "close": 22.9332,
      "volume": 5533,
      "datetime": 1736865420000
    },
    {
      "open": 22.928,
      "high": 22.93,
      "low": 22.9,
      "close": 22.92,
      "volume": 18238,
      "datetime": 1736865480000
    },
    {
      "open": 22.9201,
      "high": 22.9401,
      "low": 22.9201,
      "close": 22.9401,
      "volume": 2246,
      "datetime": 1736865540000
    },
    {
      "open": 22.93,
      "high": 22.955,
      "low": 22.93,
      "close": 22.95,
      "volume": 4556,
      "datetime": 1736865600000
    },
    {
      "open": 22.95,
      "high": 22.98,
      "low": 22.94,
      "close": 22.98,
      "volume": 2674,
      "datetime": 1736865660000
    },
    {
      "open": 22.97,
      "high": 22.99,
      "low": 22.97,
      "close": 22.99,
      "volume": 4907,
      "datetime": 1736865720000
    },
    {
      "open": 22.99,
      "high": 23.03,
      "low": 22.99,
      "close": 23.03,
      "volume": 2754,
      "datetime": 1736865780000
    },
    {
      "open": 23.035,
      "high": 23.0352,
      "low": 23.02,
      "close": 23.02,
      "volume": 3484,
      "datetime": 1736865840000
    },
    {
      "open": 23.01,
      "high": 23.055,
      "low": 23.01,
      "close": 23.055,
      "volume": 3673,
      "datetime": 1736865900000
    },
    {
      "open": 23.0529,
      "high": 23.0529,
      "low": 23.0529,
      "close": 23.0529,
      "volume": 400,
      "datetime": 1736865960000
    },
    {
      "open": 23.08,
      "high": 23.1052,
      "low": 23.08,
      "close": 23.0916,
      "volume": 8788,
      "datetime": 1736866020000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.0603,
      "close": 23.0772,
      "volume": 2099,
      "datetime": 1736866080000
    },
    {
      "open": 23.0897,
      "high": 23.0897,
      "low": 23.0534,
      "close": 23.0534,
      "volume": 1858,
      "datetime": 1736866140000
    },
    {
      "open": 23.035,
      "high": 23.0896,
      "low": 23.035,
      "close": 23.07,
      "volume": 4884,
      "datetime": 1736866200000
    },
    {
      "open": 23.04,
      "high": 23.0681,
      "low": 23.0242,
      "close": 23.0252,
      "volume": 2811,
      "datetime": 1736866260000
    },
    {
      "open": 23.05,
      "high": 23.0771,
      "low": 23.05,
      "close": 23.0748,
      "volume": 1800,
      "datetime": 1736866320000
    },
    {
      "open": 23.07,
      "high": 23.1201,
      "low": 23.07,
      "close": 23.1201,
      "volume": 2628,
      "datetime": 1736866380000
    },
    {
      "open": 23.145,
      "high": 23.15,
      "low": 23.14,
      "close": 23.14,
      "volume": 4525,
      "datetime": 1736866440000
    },
    {
      "open": 23.14,
      "high": 23.1772,
      "low": 23.14,
      "close": 23.165,
      "volume": 4946,
      "datetime": 1736866500000
    },
    {
      "open": 23.18,
      "high": 23.195,
      "low": 23.14,
      "close": 23.145,
      "volume": 10769,
      "datetime": 1736866560000
    },
    {
      "open": 23.15,
      "high": 23.175,
      "low": 23.15,
      "close": 23.1701,
      "volume": 8216,
      "datetime": 1736866620000
    },
    {
      "open": 23.195,
      "high": 23.1977,
      "low": 23.185,
      "close": 23.19,
      "volume": 3887,
      "datetime": 1736866680000
    },
    {
      "open": 23.2,
      "high": 23.21,
      "low": 23.165,
      "close": 23.165,
      "volume": 10894,
      "datetime": 1736866740000
    },
    {
      "open": 23.17,
      "high": 23.1998,
      "low": 23.1598,
      "close": 23.1997,
      "volume": 5496,
      "datetime": 1736866800000
    },
    {
      "open": 23.19,
      "high": 23.19,
      "low": 23.1618,
      "close": 23.1618,
      "volume": 2872,
      "datetime": 1736866860000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.14,
      "close": 23.1501,
      "volume": 2800,
      "datetime": 1736866920000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.13,
      "close": 23.13,
      "volume": 343,
      "datetime": 1736866980000
    },
    {
      "open": 23.12,
      "high": 23.135,
      "low": 23.12,
      "close": 23.12,
      "volume": 3658,
      "datetime": 1736867040000
    },
    {
      "open": 23.14,
      "high": 23.16,
      "low": 23.14,
      "close": 23.16,
      "volume": 1677,
      "datetime": 1736867100000
    },
    {
      "open": 23.14,
      "high": 23.14,
      "low": 23.0983,
      "close": 23.0983,
      "volume": 2342,
      "datetime": 1736867160000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.06,
      "close": 23.07,
      "volume": 1675,
      "datetime": 1736867220000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.04,
      "close": 23.05,
      "volume": 800,
      "datetime": 1736867280000
    },
    {
      "open": 23.0487,
      "high": 23.0487,
      "low": 23.03,
      "close": 23.03,
      "volume": 1317,
      "datetime": 1736867340000
    },
    {
      "open": 23.041,
      "high": 23.08,
      "low": 23.041,
      "close": 23.08,
      "volume": 1133,
      "datetime": 1736867400000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.02,
      "close": 23.02,
      "volume": 4975,
      "datetime": 1736867460000
    },
    {
      "open": 23.02,
      "high": 23.0232,
      "low": 23.02,
      "close": 23.02,
      "volume": 3953,
      "datetime": 1736867520000
    },
    {
      "open": 23.01,
      "high": 23.05,
      "low": 23.01,
      "close": 23.04,
      "volume": 6231,
      "datetime": 1736867580000
    },
    {
      "open": 23.03,
      "high": 23.04,
      "low": 23.0187,
      "close": 23.035,
      "volume": 2081,
      "datetime": 1736867640000
    },
    {
      "open": 23.03,
      "high": 23.059,
      "low": 23.03,
      "close": 23.04,
      "volume": 3457,
      "datetime": 1736867700000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 22.98,
      "close": 22.98,
      "volume": 3025,
      "datetime": 1736867760000
    },
    {
      "open": 23,
      "high": 23,
      "low": 22.99,
      "close": 22.99,
      "volume": 696,
      "datetime": 1736867820000
    },
    {
      "open": 23,
      "high": 23.0226,
      "low": 22.9828,
      "close": 23.02,
      "volume": 3015,
      "datetime": 1736867880000
    },
    {
      "open": 23.02,
      "high": 23.04,
      "low": 23.02,
      "close": 23.04,
      "volume": 1624,
      "datetime": 1736867940000
    },
    {
      "open": 23.0672,
      "high": 23.075,
      "low": 23.0558,
      "close": 23.075,
      "volume": 1667,
      "datetime": 1736868000000
    },
    {
      "open": 23.06,
      "high": 23.09,
      "low": 23.06,
      "close": 23.09,
      "volume": 1544,
      "datetime": 1736868060000
    },
    {
      "open": 23.1,
      "high": 23.13,
      "low": 23.09,
      "close": 23.13,
      "volume": 1803,
      "datetime": 1736868120000
    },
    {
      "open": 23.1321,
      "high": 23.14,
      "low": 23.12,
      "close": 23.12,
      "volume": 22321,
      "datetime": 1736868180000
    },
    {
      "open": 23.135,
      "high": 23.135,
      "low": 23.13,
      "close": 23.13,
      "volume": 575,
      "datetime": 1736868240000
    },
    {
      "open": 23.13,
      "high": 23.14,
      "low": 23.1,
      "close": 23.135,
      "volume": 3187,
      "datetime": 1736868300000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.12,
      "close": 23.12,
      "volume": 325,
      "datetime": 1736868360000
    },
    {
      "open": 23.15,
      "high": 23.16,
      "low": 23.15,
      "close": 23.1587,
      "volume": 1242,
      "datetime": 1736868420000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.1475,
      "close": 23.15,
      "volume": 3148,
      "datetime": 1736868480000
    },
    {
      "open": 23.14,
      "high": 23.15,
      "low": 23.13,
      "close": 23.13,
      "volume": 1043,
      "datetime": 1736868540000
    },
    {
      "open": 23.11,
      "high": 23.13,
      "low": 23.11,
      "close": 23.13,
      "volume": 2665,
      "datetime": 1736868600000
    },
    {
      "open": 23.12,
      "high": 23.13,
      "low": 23.09,
      "close": 23.09,
      "volume": 1769,
      "datetime": 1736868660000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.0704,
      "close": 23.09,
      "volume": 4859,
      "datetime": 1736868720000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.07,
      "close": 23.07,
      "volume": 2150,
      "datetime": 1736868780000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.0548,
      "close": 23.07,
      "volume": 2590,
      "datetime": 1736868840000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.0519,
      "close": 23.06,
      "volume": 2043,
      "datetime": 1736868900000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.04,
      "close": 23.04,
      "volume": 2930,
      "datetime": 1736868960000
    },
    {
      "open": 23.05,
      "high": 23.099,
      "low": 23.05,
      "close": 23.08,
      "volume": 5230,
      "datetime": 1736869020000
    },
    {
      "open": 23.07,
      "high": 23.1,
      "low": 23.0681,
      "close": 23.09,
      "volume": 2200,
      "datetime": 1736869080000
    },
    {
      "open": 23.09,
      "high": 23.14,
      "low": 23.09,
      "close": 23.14,
      "volume": 1550,
      "datetime": 1736869140000
    },
    {
      "open": 23.14,
      "high": 23.155,
      "low": 23.09,
      "close": 23.11,
      "volume": 7377,
      "datetime": 1736869200000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.06,
      "close": 23.06,
      "volume": 3919,
      "datetime": 1736869260000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.05,
      "close": 23.06,
      "volume": 1525,
      "datetime": 1736869320000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.04,
      "close": 23.04,
      "volume": 2043,
      "datetime": 1736869380000
    },
    {
      "open": 23.0448,
      "high": 23.051589,
      "low": 23.0099,
      "close": 23.0114,
      "volume": 4110,
      "datetime": 1736869440000
    },
    {
      "open": 23.02,
      "high": 23.06,
      "low": 23.02,
      "close": 23.05,
      "volume": 2826,
      "datetime": 1736869500000
    },
    {
      "open": 23.05,
      "high": 23.09,
      "low": 23.05,
      "close": 23.09,
      "volume": 3260,
      "datetime": 1736869560000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.06,
      "close": 23.08,
      "volume": 3195,
      "datetime": 1736869620000
    },
    {
      "open": 23.08,
      "high": 23.11,
      "low": 23.08,
      "close": 23.08,
      "volume": 5338,
      "datetime": 1736869680000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.06,
      "close": 23.06,
      "volume": 2199,
      "datetime": 1736869740000
    },
    {
      "open": 23.06,
      "high": 23.1,
      "low": 23.06,
      "close": 23.06,
      "volume": 4273,
      "datetime": 1736869800000
    },
    {
      "open": 23.06,
      "high": 23.1,
      "low": 23.06,
      "close": 23.08,
      "volume": 1325,
      "datetime": 1736869860000
    },
    {
      "open": 23.06,
      "high": 23.07,
      "low": 23.05,
      "close": 23.07,
      "volume": 1275,
      "datetime": 1736869920000
    },
    {
      "open": 23.08,
      "high": 23.09,
      "low": 23.08,
      "close": 23.09,
      "volume": 825,
      "datetime": 1736869980000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.06,
      "close": 23.06,
      "volume": 1281,
      "datetime": 1736870040000
    },
    {
      "open": 23.07,
      "high": 23.105,
      "low": 23.07,
      "close": 23.105,
      "volume": 5687,
      "datetime": 1736870100000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.09,
      "close": 23.09,
      "volume": 775,
      "datetime": 1736870160000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.07,
      "close": 23.09,
      "volume": 1525,
      "datetime": 1736870220000
    },
    {
      "open": 23.11,
      "high": 23.12,
      "low": 23.11,
      "close": 23.12,
      "volume": 575,
      "datetime": 1736870280000
    },
    {
      "open": 23.12,
      "high": 23.13,
      "low": 23.12,
      "close": 23.13,
      "volume": 875,
      "datetime": 1736870340000
    },
    {
      "open": 23.15,
      "high": 23.19,
      "low": 23.15,
      "close": 23.17,
      "volume": 5135,
      "datetime": 1736870400000
    },
    {
      "open": 23.18,
      "high": 23.2,
      "low": 23.16,
      "close": 23.2,
      "volume": 2743,
      "datetime": 1736870460000
    },
    {
      "open": 23.19,
      "high": 23.25,
      "low": 23.19,
      "close": 23.25,
      "volume": 3661,
      "datetime": 1736870520000
    },
    {
      "open": 23.275,
      "high": 23.31,
      "low": 23.275,
      "close": 23.31,
      "volume": 7357,
      "datetime": 1736870580000
    },
    {
      "open": 23.33,
      "high": 23.35,
      "low": 23.31,
      "close": 23.325,
      "volume": 8219,
      "datetime": 1736870640000
    },
    {
      "open": 23.33,
      "high": 23.34,
      "low": 23.32,
      "close": 23.3393,
      "volume": 5486,
      "datetime": 1736870700000
    },
    {
      "open": 23.33,
      "high": 23.34,
      "low": 23.31,
      "close": 23.31,
      "volume": 6460,
      "datetime": 1736870760000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.26,
      "close": 23.28,
      "volume": 7913,
      "datetime": 1736870820000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.23,
      "close": 23.23,
      "volume": 3118,
      "datetime": 1736870880000
    },
    {
      "open": 23.23,
      "high": 23.2548,
      "low": 23.23,
      "close": 23.2548,
      "volume": 1850,
      "datetime": 1736870940000
    },
    {
      "open": 23.26,
      "high": 23.2948,
      "low": 23.255,
      "close": 23.265,
      "volume": 4990,
      "datetime": 1736871000000
    },
    {
      "open": 23.27,
      "high": 23.28,
      "low": 23.23,
      "close": 23.27,
      "volume": 1527,
      "datetime": 1736871060000
    },
    {
      "open": 23.27,
      "high": 23.29,
      "low": 23.27,
      "close": 23.28,
      "volume": 2631,
      "datetime": 1736871120000
    },
    {
      "open": 23.29,
      "high": 23.295,
      "low": 23.26,
      "close": 23.29,
      "volume": 3861,
      "datetime": 1736871180000
    },
    {
      "open": 23.29,
      "high": 23.29,
      "low": 23.26,
      "close": 23.26,
      "volume": 775,
      "datetime": 1736871240000
    },
    {
      "open": 23.2487,
      "high": 23.28,
      "low": 23.2487,
      "close": 23.28,
      "volume": 1275,
      "datetime": 1736871300000
    },
    {
      "open": 23.275,
      "high": 23.275,
      "low": 23.235,
      "close": 23.235,
      "volume": 8481,
      "datetime": 1736871360000
    },
    {
      "open": 23.22,
      "high": 23.24,
      "low": 23.2001,
      "close": 23.24,
      "volume": 1943,
      "datetime": 1736871420000
    },
    {
      "open": 23.24,
      "high": 23.27,
      "low": 23.22,
      "close": 23.26,
      "volume": 1761,
      "datetime": 1736871480000
    },
    {
      "open": 23.28,
      "high": 23.28,
      "low": 23.26,
      "close": 23.26,
      "volume": 875,
      "datetime": 1736871540000
    },
    {
      "open": 23.26,
      "high": 23.27,
      "low": 23.2599,
      "close": 23.27,
      "volume": 2150,
      "datetime": 1736871600000
    },
    {
      "open": 23.25,
      "high": 23.27,
      "low": 23.25,
      "close": 23.27,
      "volume": 925,
      "datetime": 1736871660000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.19,
      "close": 23.19,
      "volume": 2489,
      "datetime": 1736871720000
    },
    {
      "open": 23.2,
      "high": 23.2252,
      "low": 23.2,
      "close": 23.21,
      "volume": 1150,
      "datetime": 1736871780000
    },
    {
      "open": 23.21,
      "high": 23.225,
      "low": 23.21,
      "close": 23.21,
      "volume": 850,
      "datetime": 1736871840000
    },
    {
      "open": 23.22,
      "high": 23.22,
      "low": 23.18,
      "close": 23.18,
      "volume": 2187,
      "datetime": 1736871900000
    },
    {
      "open": 23.1781,
      "high": 23.1781,
      "low": 23.16,
      "close": 23.165,
      "volume": 2892,
      "datetime": 1736871960000
    },
    {
      "open": 23.16,
      "high": 23.19,
      "low": 23.16,
      "close": 23.19,
      "volume": 725,
      "datetime": 1736872020000
    },
    {
      "open": 23.19,
      "high": 23.23,
      "low": 23.18,
      "close": 23.23,
      "volume": 1100,
      "datetime": 1736872080000
    },
    {
      "open": 23.25,
      "high": 23.27,
      "low": 23.25,
      "close": 23.27,
      "volume": 918,
      "datetime": 1736872140000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.26,
      "close": 23.26,
      "volume": 950,
      "datetime": 1736872200000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.2452,
      "close": 23.25,
      "volume": 1300,
      "datetime": 1736872260000
    },
    {
      "open": 23.26,
      "high": 23.29,
      "low": 23.26,
      "close": 23.27,
      "volume": 918,
      "datetime": 1736872320000
    },
    {
      "open": 23.26,
      "high": 23.31,
      "low": 23.26,
      "close": 23.31,
      "volume": 7520,
      "datetime": 1736872380000
    },
    {
      "open": 23.31,
      "high": 23.32,
      "low": 23.27,
      "close": 23.275,
      "volume": 2577,
      "datetime": 1736872440000
    },
    {
      "open": 23.28,
      "high": 23.29,
      "low": 23.28,
      "close": 23.28,
      "volume": 925,
      "datetime": 1736872500000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.2833,
      "close": 23.3,
      "volume": 1939,
      "datetime": 1736872560000
    },
    {
      "open": 23.29,
      "high": 23.315,
      "low": 23.29,
      "close": 23.305,
      "volume": 1810,
      "datetime": 1736872620000
    },
    {
      "open": 23.3,
      "high": 23.34,
      "low": 23.3,
      "close": 23.34,
      "volume": 8220,
      "datetime": 1736872680000
    },
    {
      "open": 23.3555,
      "high": 23.36,
      "low": 23.335,
      "close": 23.34,
      "volume": 3219,
      "datetime": 1736872740000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.31,
      "close": 23.33,
      "volume": 1475,
      "datetime": 1736872800000
    },
    {
      "open": 23.32,
      "high": 23.34,
      "low": 23.32,
      "close": 23.34,
      "volume": 1916,
      "datetime": 1736872860000
    },
    {
      "open": 23.33,
      "high": 23.345,
      "low": 23.33,
      "close": 23.34,
      "volume": 1475,
      "datetime": 1736872920000
    },
    {
      "open": 23.34,
      "high": 23.38,
      "low": 23.34,
      "close": 23.38,
      "volume": 1086,
      "datetime": 1736872980000
    },
    {
      "open": 23.39,
      "high": 23.43,
      "low": 23.39,
      "close": 23.4,
      "volume": 9639,
      "datetime": 1736873040000
    },
    {
      "open": 23.39,
      "high": 23.41,
      "low": 23.38,
      "close": 23.41,
      "volume": 8403,
      "datetime": 1736873100000
    },
    {
      "open": 23.4142,
      "high": 23.4142,
      "low": 23.36,
      "close": 23.36,
      "volume": 3275,
      "datetime": 1736873160000
    },
    {
      "open": 23.37,
      "high": 23.38,
      "low": 23.36,
      "close": 23.38,
      "volume": 3021,
      "datetime": 1736873220000
    },
    {
      "open": 23.38,
      "high": 23.38,
      "low": 23.3448,
      "close": 23.35,
      "volume": 1600,
      "datetime": 1736873280000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.35,
      "close": 23.36,
      "volume": 600,
      "datetime": 1736873340000
    },
    {
      "open": 23.37,
      "high": 23.3796,
      "low": 23.34,
      "close": 23.35,
      "volume": 3225,
      "datetime": 1736873400000
    },
    {
      "open": 23.36,
      "high": 23.36,
      "low": 23.33,
      "close": 23.35,
      "volume": 1700,
      "datetime": 1736873460000
    },
    {
      "open": 23.34,
      "high": 23.34,
      "low": 23.305,
      "close": 23.33,
      "volume": 5324,
      "datetime": 1736873520000
    },
    {
      "open": 23.32,
      "high": 23.33,
      "low": 23.31,
      "close": 23.3299,
      "volume": 1825,
      "datetime": 1736873580000
    },
    {
      "open": 23.33,
      "high": 23.36,
      "low": 23.33,
      "close": 23.35,
      "volume": 1683,
      "datetime": 1736873640000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.31,
      "close": 23.31,
      "volume": 5452,
      "datetime": 1736873700000
    },
    {
      "open": 23.3019,
      "high": 23.32,
      "low": 23.3,
      "close": 23.31,
      "volume": 3386,
      "datetime": 1736873760000
    },
    {
      "open": 23.3278,
      "high": 23.34,
      "low": 23.32,
      "close": 23.34,
      "volume": 929,
      "datetime": 1736873820000
    },
    {
      "open": 23.33,
      "high": 23.34,
      "low": 23.3,
      "close": 23.3,
      "volume": 1300,
      "datetime": 1736873880000
    },
    {
      "open": 23.31,
      "high": 23.32,
      "low": 23.31,
      "close": 23.32,
      "volume": 550,
      "datetime": 1736873940000
    },
    {
      "open": 23.33,
      "high": 23.3417,
      "low": 23.33,
      "close": 23.34,
      "volume": 2229,
      "datetime": 1736874000000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.3227,
      "close": 23.3227,
      "volume": 2175,
      "datetime": 1736874060000
    },
    {
      "open": 23.32,
      "high": 23.33,
      "low": 23.32,
      "close": 23.33,
      "volume": 1975,
      "datetime": 1736874120000
    },
    {
      "open": 23.35,
      "high": 23.35,
      "low": 23.34,
      "close": 23.35,
      "volume": 900,
      "datetime": 1736874180000
    },
    {
      "open": 23.35,
      "high": 23.36,
      "low": 23.34,
      "close": 23.35,
      "volume": 1487,
      "datetime": 1736874240000
    },
    {
      "open": 23.33,
      "high": 23.33,
      "low": 23.32,
      "close": 23.33,
      "volume": 1295,
      "datetime": 1736874300000
    },
    {
      "open": 23.33,
      "high": 23.34,
      "low": 23.3,
      "close": 23.3,
      "volume": 1435,
      "datetime": 1736874360000
    },
    {
      "open": 23.29,
      "high": 23.29,
      "low": 23.24,
      "close": 23.24,
      "volume": 1878,
      "datetime": 1736874420000
    },
    {
      "open": 23.2578,
      "high": 23.28,
      "low": 23.2578,
      "close": 23.27,
      "volume": 1910,
      "datetime": 1736874480000
    },
    {
      "open": 23.27,
      "high": 23.28,
      "low": 23.27,
      "close": 23.28,
      "volume": 450,
      "datetime": 1736874540000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.25,
      "close": 23.27,
      "volume": 3400,
      "datetime": 1736874600000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.24,
      "close": 23.24,
      "volume": 1325,
      "datetime": 1736874660000
    },
    {
      "open": 23.23,
      "high": 23.24,
      "low": 23.23,
      "close": 23.24,
      "volume": 3048,
      "datetime": 1736874720000
    },
    {
      "open": 23.225,
      "high": 23.24,
      "low": 23.225,
      "close": 23.23,
      "volume": 2900,
      "datetime": 1736874780000
    },
    {
      "open": 23.21,
      "high": 23.233154,
      "low": 23.21,
      "close": 23.231169,
      "volume": 1050,
      "datetime": 1736874840000
    },
    {
      "open": 23.24,
      "high": 23.26,
      "low": 23.24,
      "close": 23.25,
      "volume": 2428,
      "datetime": 1736874900000
    },
    {
      "open": 23.24,
      "high": 23.24,
      "low": 23.1902,
      "close": 23.1902,
      "volume": 2256,
      "datetime": 1736874960000
    },
    {
      "open": 23.2,
      "high": 23.2,
      "low": 23.19,
      "close": 23.2,
      "volume": 1225,
      "datetime": 1736875020000
    },
    {
      "open": 23.19,
      "high": 23.2,
      "low": 23.19,
      "close": 23.2,
      "volume": 675,
      "datetime": 1736875080000
    },
    {
      "open": 23.21,
      "high": 23.2341,
      "low": 23.21,
      "close": 23.23,
      "volume": 1236,
      "datetime": 1736875140000
    },
    {
      "open": 23.24,
      "high": 23.247,
      "low": 23.24,
      "close": 23.247,
      "volume": 820,
      "datetime": 1736875200000
    },
    {
      "open": 23.28,
      "high": 23.3,
      "low": 23.28,
      "close": 23.29,
      "volume": 900,
      "datetime": 1736875260000
    },
    {
      "open": 23.31,
      "high": 23.32,
      "low": 23.31,
      "close": 23.31,
      "volume": 1085,
      "datetime": 1736875320000
    },
    {
      "open": 23.318,
      "high": 23.32,
      "low": 23.31,
      "close": 23.31,
      "volume": 2150,
      "datetime": 1736875380000
    },
    {
      "open": 23.31,
      "high": 23.31,
      "low": 23.305,
      "close": 23.3099,
      "volume": 5150,
      "datetime": 1736875440000
    },
    {
      "open": 23.3,
      "high": 23.3,
      "low": 23.3,
      "close": 23.3,
      "volume": 350,
      "datetime": 1736875500000
    },
    {
      "open": 23.297839,
      "high": 23.297839,
      "low": 23.29,
      "close": 23.29,
      "volume": 520,
      "datetime": 1736875560000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.26,
      "close": 23.26,
      "volume": 600,
      "datetime": 1736875620000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.24,
      "close": 23.24,
      "volume": 1318,
      "datetime": 1736875680000
    },
    {
      "open": 23.23,
      "high": 23.23,
      "low": 23.23,
      "close": 23.23,
      "volume": 275,
      "datetime": 1736875740000
    },
    {
      "open": 23.23,
      "high": 23.25,
      "low": 23.23,
      "close": 23.25,
      "volume": 1059,
      "datetime": 1736875800000
    },
    {
      "open": 23.27,
      "high": 23.27,
      "low": 23.26,
      "close": 23.26,
      "volume": 1100,
      "datetime": 1736875860000
    },
    {
      "open": 23.28,
      "high": 23.28,
      "low": 23.27,
      "close": 23.27,
      "volume": 775,
      "datetime": 1736875920000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.245,
      "close": 23.245,
      "volume": 1008,
      "datetime": 1736875980000
    },
    {
      "open": 23.26,
      "high": 23.29,
      "low": 23.26,
      "close": 23.29,
      "volume": 1800,
      "datetime": 1736876040000
    },
    {
      "open": 23.3,
      "high": 23.32,
      "low": 23.3,
      "close": 23.31,
      "volume": 1180,
      "datetime": 1736876100000
    },
    {
      "open": 23.3098,
      "high": 23.3098,
      "low": 23.26,
      "close": 23.26,
      "volume": 1625,
      "datetime": 1736876160000
    },
    {
      "open": 23.27,
      "high": 23.28,
      "low": 23.25,
      "close": 23.25,
      "volume": 1600,
      "datetime": 1736876220000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.25,
      "close": 23.25,
      "volume": 1229,
      "datetime": 1736876280000
    },
    {
      "open": 23.26,
      "high": 23.26,
      "low": 23.26,
      "close": 23.26,
      "volume": 150,
      "datetime": 1736876340000
    },
    {
      "open": 23.24,
      "high": 23.25,
      "low": 23.24,
      "close": 23.25,
      "volume": 725,
      "datetime": 1736876400000
    },
    {
      "open": 23.255,
      "high": 23.255,
      "low": 23.24,
      "close": 23.24,
      "volume": 450,
      "datetime": 1736876460000
    },
    {
      "open": 23.22,
      "high": 23.22,
      "low": 23.18,
      "close": 23.18,
      "volume": 1103,
      "datetime": 1736876520000
    },
    {
      "open": 23.1712,
      "high": 23.19,
      "low": 23.17,
      "close": 23.17,
      "volume": 1717,
      "datetime": 1736876580000
    },
    {
      "open": 23.1722,
      "high": 23.2,
      "low": 23.1722,
      "close": 23.2,
      "volume": 1692,
      "datetime": 1736876640000
    },
    {
      "open": 23.21,
      "high": 23.22,
      "low": 23.2081,
      "close": 23.22,
      "volume": 2273,
      "datetime": 1736876700000
    },
    {
      "open": 23.21,
      "high": 23.21,
      "low": 23.2,
      "close": 23.2,
      "volume": 625,
      "datetime": 1736876760000
    },
    {
      "open": 23.2,
      "high": 23.2,
      "low": 23.19,
      "close": 23.2,
      "volume": 658,
      "datetime": 1736876820000
    },
    {
      "open": 23.18,
      "high": 23.18,
      "low": 23.14,
      "close": 23.14,
      "volume": 5073,
      "datetime": 1736876880000
    },
    {
      "open": 23.15,
      "high": 23.16,
      "low": 23.15,
      "close": 23.16,
      "volume": 275,
      "datetime": 1736876940000
    },
    {
      "open": 23.17,
      "high": 23.17,
      "low": 23.16,
      "close": 23.16,
      "volume": 850,
      "datetime": 1736877000000
    },
    {
      "open": 23.17,
      "high": 23.17,
      "low": 23.15,
      "close": 23.16,
      "volume": 1751,
      "datetime": 1736877060000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.125,
      "close": 23.13,
      "volume": 6075,
      "datetime": 1736877120000
    },
    {
      "open": 23.12,
      "high": 23.13,
      "low": 23.1117,
      "close": 23.1202,
      "volume": 3000,
      "datetime": 1736877180000
    },
    {
      "open": 23.12,
      "high": 23.13,
      "low": 23.12,
      "close": 23.13,
      "volume": 1097,
      "datetime": 1736877240000
    },
    {
      "open": 23.14,
      "high": 23.15,
      "low": 23.14,
      "close": 23.14,
      "volume": 875,
      "datetime": 1736877300000
    },
    {
      "open": 23.14,
      "high": 23.16,
      "low": 23.14,
      "close": 23.16,
      "volume": 4474,
      "datetime": 1736877360000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.13,
      "close": 23.13,
      "volume": 1590,
      "datetime": 1736877420000
    },
    {
      "open": 23.12,
      "high": 23.12,
      "low": 23.1,
      "close": 23.12,
      "volume": 3534,
      "datetime": 1736877480000
    },
    {
      "open": 23.12,
      "high": 23.12,
      "low": 23.11,
      "close": 23.11,
      "volume": 275,
      "datetime": 1736877540000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.1,
      "close": 23.1,
      "volume": 775,
      "datetime": 1736877600000
    },
    {
      "open": 23.1,
      "high": 23.12,
      "low": 23.1,
      "close": 23.11,
      "volume": 2000,
      "datetime": 1736877660000
    },
    {
      "open": 23.11,
      "high": 23.1199,
      "low": 23.1,
      "close": 23.11,
      "volume": 1525,
      "datetime": 1736877720000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.0913,
      "close": 23.093,
      "volume": 2600,
      "datetime": 1736877780000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.08,
      "close": 23.09,
      "volume": 1890,
      "datetime": 1736877840000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.08,
      "close": 23.09,
      "volume": 3250,
      "datetime": 1736877900000
    },
    {
      "open": 23.09,
      "high": 23.11,
      "low": 23.09,
      "close": 23.11,
      "volume": 1075,
      "datetime": 1736877960000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.08,
      "close": 23.08,
      "volume": 825,
      "datetime": 1736878020000
    },
    {
      "open": 23.08,
      "high": 23.12,
      "low": 23.08,
      "close": 23.09,
      "volume": 1386,
      "datetime": 1736878080000
    },
    {
      "open": 23.09,
      "high": 23.13,
      "low": 23.09,
      "close": 23.12,
      "volume": 1150,
      "datetime": 1736878140000
    },
    {
      "open": 23.11,
      "high": 23.13,
      "low": 23.11,
      "close": 23.13,
      "volume": 1075,
      "datetime": 1736878200000
    },
    {
      "open": 23.14,
      "high": 23.15,
      "low": 23.14,
      "close": 23.15,
      "volume": 800,
      "datetime": 1736878260000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.1574,
      "close": 23.1574,
      "volume": 625,
      "datetime": 1736878320000
    },
    {
      "open": 23.14,
      "high": 23.145,
      "low": 23.14,
      "close": 23.145,
      "volume": 500,
      "datetime": 1736878380000
    },
    {
      "open": 23.14,
      "high": 23.1474,
      "low": 23.14,
      "close": 23.1474,
      "volume": 275,
      "datetime": 1736878440000
    },
    {
      "open": 23.17,
      "high": 23.18,
      "low": 23.15,
      "close": 23.15,
      "volume": 2600,
      "datetime": 1736878500000
    },
    {
      "open": 23.15,
      "high": 23.15,
      "low": 23.11,
      "close": 23.11,
      "volume": 475,
      "datetime": 1736878560000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 704,
      "datetime": 1736878620000
    },
    {
      "open": 23.09,
      "high": 23.11,
      "low": 23.08,
      "close": 23.11,
      "volume": 2150,
      "datetime": 1736878680000
    },
    {
      "open": 23.12,
      "high": 23.13,
      "low": 23.12,
      "close": 23.13,
      "volume": 450,
      "datetime": 1736878740000
    },
    {
      "open": 23.13,
      "high": 23.15,
      "low": 23.13,
      "close": 23.14,
      "volume": 1725,
      "datetime": 1736878800000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.125,
      "close": 23.13,
      "volume": 1000,
      "datetime": 1736878860000
    },
    {
      "open": 23.12,
      "high": 23.12,
      "low": 23.11,
      "close": 23.11,
      "volume": 975,
      "datetime": 1736878920000
    },
    {
      "open": 23.1,
      "high": 23.11,
      "low": 23.1,
      "close": 23.1,
      "volume": 825,
      "datetime": 1736878980000
    },
    {
      "open": 23.12,
      "high": 23.12,
      "low": 23.1,
      "close": 23.1,
      "volume": 11661,
      "datetime": 1736879040000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.07,
      "close": 23.07,
      "volume": 2250,
      "datetime": 1736879100000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.06,
      "close": 23.07,
      "volume": 5480,
      "datetime": 1736879160000
    },
    {
      "open": 23.07,
      "high": 23.08,
      "low": 23.07,
      "close": 23.07,
      "volume": 825,
      "datetime": 1736879220000
    },
    {
      "open": 23.0636,
      "high": 23.072,
      "low": 23.06,
      "close": 23.06,
      "volume": 1364,
      "datetime": 1736879280000
    },
    {
      "open": 23.0648,
      "high": 23.07,
      "low": 23.0648,
      "close": 23.07,
      "volume": 1175,
      "datetime": 1736879340000
    },
    {
      "open": 23.07,
      "high": 23.099,
      "low": 23.07,
      "close": 23.099,
      "volume": 1569,
      "datetime": 1736879400000
    },
    {
      "open": 23.08,
      "high": 23.085,
      "low": 23.06,
      "close": 23.06,
      "volume": 1559,
      "datetime": 1736879460000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.04,
      "close": 23.05,
      "volume": 4168,
      "datetime": 1736879520000
    },
    {
      "open": 23.05,
      "high": 23.06,
      "low": 23.05,
      "close": 23.05,
      "volume": 1061,
      "datetime": 1736879580000
    },
    {
      "open": 23.05,
      "high": 23.07,
      "low": 23.05,
      "close": 23.07,
      "volume": 925,
      "datetime": 1736879640000
    },
    {
      "open": 23.06,
      "high": 23.07,
      "low": 23.06,
      "close": 23.07,
      "volume": 1011,
      "datetime": 1736879700000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.06,
      "close": 23.06,
      "volume": 527,
      "datetime": 1736879760000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.03,
      "close": 23.03,
      "volume": 1581,
      "datetime": 1736879820000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.03,
      "close": 23.03,
      "volume": 1075,
      "datetime": 1736879880000
    },
    {
      "open": 23.025,
      "high": 23.04,
      "low": 23.02,
      "close": 23.02,
      "volume": 1018,
      "datetime": 1736879940000
    },
    {
      "open": 23.02,
      "high": 23.04,
      "low": 23.02,
      "close": 23.02,
      "volume": 24833,
      "datetime": 1736880000000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 23.02,
      "close": 23.02,
      "volume": 550,
      "datetime": 1736880060000
    },
    {
      "open": 23.04,
      "high": 23.05,
      "low": 23.04,
      "close": 23.05,
      "volume": 675,
      "datetime": 1736880120000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.03,
      "close": 23.03,
      "volume": 975,
      "datetime": 1736880180000
    },
    {
      "open": 23.03,
      "high": 23.04,
      "low": 23.0229,
      "close": 23.04,
      "volume": 1373,
      "datetime": 1736880240000
    },
    {
      "open": 23.05,
      "high": 23.055,
      "low": 23.05,
      "close": 23.055,
      "volume": 1020,
      "datetime": 1736880300000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.03,
      "close": 23.03,
      "volume": 1425,
      "datetime": 1736880360000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 22.99,
      "close": 22.995,
      "volume": 16924,
      "datetime": 1736880420000
    },
    {
      "open": 22.99,
      "high": 23,
      "low": 22.99,
      "close": 23,
      "volume": 1798,
      "datetime": 1736880480000
    },
    {
      "open": 23.0061,
      "high": 23.0061,
      "low": 23,
      "close": 23,
      "volume": 1886,
      "datetime": 1736880540000
    },
    {
      "open": 23,
      "high": 23.01,
      "low": 23,
      "close": 23.01,
      "volume": 7362,
      "datetime": 1736880600000
    },
    {
      "open": 23.02,
      "high": 23.03,
      "low": 23.02,
      "close": 23.03,
      "volume": 5201,
      "datetime": 1736880660000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.02,
      "close": 23.03,
      "volume": 17800,
      "datetime": 1736880720000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23,
      "close": 23.0051,
      "volume": 3428,
      "datetime": 1736880780000
    },
    {
      "open": 23,
      "high": 23.0015,
      "low": 22.995,
      "close": 22.995,
      "volume": 1540,
      "datetime": 1736880840000
    },
    {
      "open": 23,
      "high": 23.0051,
      "low": 23,
      "close": 23,
      "volume": 825,
      "datetime": 1736880900000
    },
    {
      "open": 22.99,
      "high": 23,
      "low": 22.99,
      "close": 23,
      "volume": 1810,
      "datetime": 1736880960000
    },
    {
      "open": 23.005,
      "high": 23.005,
      "low": 23.005,
      "close": 23.005,
      "volume": 300,
      "datetime": 1736881020000
    },
    {
      "open": 23.01,
      "high": 23.03,
      "low": 23.01,
      "close": 23.03,
      "volume": 4994,
      "datetime": 1736881080000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 4395,
      "datetime": 1736881140000
    },
    {
      "open": 23.05,
      "high": 23.075,
      "low": 23.05,
      "close": 23.075,
      "volume": 5379,
      "datetime": 1736881200000
    },
    {
      "open": 23.06,
      "high": 23.07,
      "low": 23.06,
      "close": 23.06,
      "volume": 1050,
      "datetime": 1736881260000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.03,
      "close": 23.05,
      "volume": 1294,
      "datetime": 1736881320000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 525,
      "datetime": 1736881380000
    },
    {
      "open": 23.07,
      "high": 23.0701,
      "low": 23.07,
      "close": 23.07,
      "volume": 1511,
      "datetime": 1736881440000
    },
    {
      "open": 23.055,
      "high": 23.055,
      "low": 23.05,
      "close": 23.05,
      "volume": 1650,
      "datetime": 1736881500000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 150,
      "datetime": 1736881560000
    },
    {
      "open": 23.03,
      "high": 23.05,
      "low": 23.03,
      "close": 23.04,
      "volume": 625,
      "datetime": 1736881620000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.018,
      "close": 23.02,
      "volume": 4705,
      "datetime": 1736881680000
    },
    {
      "open": 23.03,
      "high": 23.04,
      "low": 23.03,
      "close": 23.04,
      "volume": 1275,
      "datetime": 1736881740000
    },
    {
      "open": 23.03,
      "high": 23.04,
      "low": 23.03,
      "close": 23.04,
      "volume": 525,
      "datetime": 1736881800000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.04,
      "close": 23.04,
      "volume": 650,
      "datetime": 1736881860000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 200,
      "datetime": 1736881920000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23,
      "close": 23,
      "volume": 782,
      "datetime": 1736881980000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 563,
      "datetime": 1736882040000
    },
    {
      "open": 22.99,
      "high": 22.9968,
      "low": 22.98,
      "close": 22.98,
      "volume": 1125,
      "datetime": 1736882100000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 150,
      "datetime": 1736882160000
    },
    {
      "open": 23.02,
      "high": 23.0272,
      "low": 23.015,
      "close": 23.0272,
      "volume": 1644,
      "datetime": 1736882220000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 22.99,
      "close": 22.99,
      "volume": 3137,
      "datetime": 1736882280000
    },
    {
      "open": 22.99,
      "high": 23.01,
      "low": 22.99,
      "close": 23.01,
      "volume": 475,
      "datetime": 1736882340000
    },
    {
      "open": 22.995,
      "high": 22.995,
      "low": 22.98,
      "close": 22.9858,
      "volume": 940,
      "datetime": 1736882460000
    },
    {
      "open": 22.99,
      "high": 22.995,
      "low": 22.975,
      "close": 22.975,
      "volume": 750,
      "datetime": 1736882520000
    },
    {
      "open": 22.98,
      "high": 22.99,
      "low": 22.98,
      "close": 22.99,
      "volume": 1573,
      "datetime": 1736882580000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.98,
      "close": 22.98,
      "volume": 725,
      "datetime": 1736882640000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.97,
      "close": 22.98,
      "volume": 1088,
      "datetime": 1736882700000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.97,
      "close": 22.97,
      "volume": 457,
      "datetime": 1736882760000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.97,
      "close": 22.97,
      "volume": 175,
      "datetime": 1736882820000
    },
    {
      "open": 22.975,
      "high": 22.99,
      "low": 22.975,
      "close": 22.99,
      "volume": 825,
      "datetime": 1736882880000
    },
    {
      "open": 23.005,
      "high": 23.005,
      "low": 23.005,
      "close": 23.005,
      "volume": 1500,
      "datetime": 1736882940000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.0081,
      "close": 23.0081,
      "volume": 2487,
      "datetime": 1736883000000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 400,
      "datetime": 1736883060000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 800,
      "datetime": 1736883120000
    },
    {
      "open": 22.9911,
      "high": 22.995,
      "low": 22.965,
      "close": 22.965,
      "volume": 3837,
      "datetime": 1736883180000
    },
    {
      "open": 22.965,
      "high": 22.9742,
      "low": 22.965,
      "close": 22.97,
      "volume": 2065,
      "datetime": 1736883240000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.961,
      "close": 22.97,
      "volume": 4867,
      "datetime": 1736883300000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.95,
      "close": 22.95,
      "volume": 6000,
      "datetime": 1736883360000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.9523,
      "close": 22.9523,
      "volume": 800,
      "datetime": 1736883420000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.9492,
      "close": 22.95,
      "volume": 904,
      "datetime": 1736883480000
    },
    {
      "open": 22.9537,
      "high": 22.9803,
      "low": 22.9537,
      "close": 22.98,
      "volume": 1400,
      "datetime": 1736883540000
    },
    {
      "open": 22.98,
      "high": 22.99,
      "low": 22.98,
      "close": 22.99,
      "volume": 1874,
      "datetime": 1736883600000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.96,
      "close": 22.96,
      "volume": 925,
      "datetime": 1736883660000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.98,
      "close": 22.98,
      "volume": 1010,
      "datetime": 1736883720000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.99,
      "close": 22.99,
      "volume": 550,
      "datetime": 1736883780000
    },
    {
      "open": 22.995,
      "high": 23,
      "low": 22.995,
      "close": 23,
      "volume": 2797,
      "datetime": 1736883840000
    },
    {
      "open": 23,
      "high": 23.015,
      "low": 23,
      "close": 23,
      "volume": 5190,
      "datetime": 1736883900000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 448,
      "datetime": 1736883960000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 200,
      "datetime": 1736884020000
    },
    {
      "open": 23.0099,
      "high": 23.02,
      "low": 23.0099,
      "close": 23.02,
      "volume": 784,
      "datetime": 1736884080000
    },
    {
      "open": 23.02,
      "high": 23.03,
      "low": 23.01,
      "close": 23.01,
      "volume": 950,
      "datetime": 1736884140000
    },
    {
      "open": 23.01,
      "high": 23.02,
      "low": 23.01,
      "close": 23.02,
      "volume": 500,
      "datetime": 1736884200000
    },
    {
      "open": 23.03,
      "high": 23.05,
      "low": 23.03,
      "close": 23.05,
      "volume": 4550,
      "datetime": 1736884260000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.04,
      "close": 23.04,
      "volume": 7475,
      "datetime": 1736884320000
    },
    {
      "open": 23.04,
      "high": 23.0475,
      "low": 23.04,
      "close": 23.0475,
      "volume": 725,
      "datetime": 1736884380000
    },
    {
      "open": 23.05,
      "high": 23.07,
      "low": 23.05,
      "close": 23.07,
      "volume": 4065,
      "datetime": 1736884440000
    },
    {
      "open": 23.065,
      "high": 23.065,
      "low": 23.065,
      "close": 23.065,
      "volume": 434,
      "datetime": 1736884500000
    },
    {
      "open": 23.06,
      "high": 23.1,
      "low": 23.06,
      "close": 23.09,
      "volume": 9609,
      "datetime": 1736884560000
    },
    {
      "open": 23.09,
      "high": 23.11,
      "low": 23.09,
      "close": 23.09,
      "volume": 1100,
      "datetime": 1736884620000
    },
    {
      "open": 23.1,
      "high": 23.105,
      "low": 23.09,
      "close": 23.09,
      "volume": 4211,
      "datetime": 1736884680000
    },
    {
      "open": 23.11,
      "high": 23.13,
      "low": 23.11,
      "close": 23.1199,
      "volume": 2261,
      "datetime": 1736884740000
    },
    {
      "open": 23.1,
      "high": 23.1299,
      "low": 23.09,
      "close": 23.1299,
      "volume": 1691,
      "datetime": 1736884800000
    },
    {
      "open": 23.13,
      "high": 23.1464,
      "low": 23.13,
      "close": 23.1383,
      "volume": 8533,
      "datetime": 1736884860000
    },
    {
      "open": 23.13,
      "high": 23.18,
      "low": 23.13,
      "close": 23.18,
      "volume": 3881,
      "datetime": 1736884920000
    },
    {
      "open": 23.18,
      "high": 23.1885,
      "low": 23.15,
      "close": 23.16,
      "volume": 15713,
      "datetime": 1736884980000
    },
    {
      "open": 23.175,
      "high": 23.215,
      "low": 23.175,
      "close": 23.2112,
      "volume": 4350,
      "datetime": 1736885040000
    },
    {
      "open": 23.1842,
      "high": 23.2,
      "low": 23.1648,
      "close": 23.17,
      "volume": 3619,
      "datetime": 1736885100000
    },
    {
      "open": 23.17,
      "high": 23.18,
      "low": 23.16,
      "close": 23.18,
      "volume": 8308,
      "datetime": 1736885160000
    },
    {
      "open": 23.18,
      "high": 23.185,
      "low": 23.1532,
      "close": 23.1532,
      "volume": 4675,
      "datetime": 1736885220000
    },
    {
      "open": 23.14,
      "high": 23.15,
      "low": 23.13,
      "close": 23.14,
      "volume": 2762,
      "datetime": 1736885280000
    },
    {
      "open": 23.13,
      "high": 23.14,
      "low": 23.13,
      "close": 23.14,
      "volume": 909,
      "datetime": 1736885340000
    },
    {
      "open": 23.14,
      "high": 23.165,
      "low": 23.14,
      "close": 23.16,
      "volume": 2111,
      "datetime": 1736885400000
    },
    {
      "open": 23.16,
      "high": 23.165,
      "low": 23.13,
      "close": 23.165,
      "volume": 1536,
      "datetime": 1736885460000
    },
    {
      "open": 23.15,
      "high": 23.16,
      "low": 23.1301,
      "close": 23.1301,
      "volume": 650,
      "datetime": 1736885520000
    },
    {
      "open": 23.14,
      "high": 23.15,
      "low": 23.13,
      "close": 23.1348,
      "volume": 1464,
      "datetime": 1736885580000
    },
    {
      "open": 23.13,
      "high": 23.13,
      "low": 23.12,
      "close": 23.12,
      "volume": 2045,
      "datetime": 1736885640000
    },
    {
      "open": 23.12,
      "high": 23.12,
      "low": 23.085,
      "close": 23.09,
      "volume": 5001,
      "datetime": 1736885700000
    },
    {
      "open": 23.085,
      "high": 23.1,
      "low": 23.08,
      "close": 23.1,
      "volume": 6200,
      "datetime": 1736885760000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.045,
      "close": 23.07,
      "volume": 4721,
      "datetime": 1736885820000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.06,
      "close": 23.06,
      "volume": 675,
      "datetime": 1736885880000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.0499,
      "close": 23.05,
      "volume": 1550,
      "datetime": 1736885940000
    },
    {
      "open": 23.04,
      "high": 23.06,
      "low": 23.035,
      "close": 23.06,
      "volume": 5538,
      "datetime": 1736886000000
    },
    {
      "open": 23.06,
      "high": 23.06,
      "low": 23.04,
      "close": 23.04,
      "volume": 500,
      "datetime": 1736886060000
    },
    {
      "open": 23.045,
      "high": 23.0619,
      "low": 23.045,
      "close": 23.0619,
      "volume": 2241,
      "datetime": 1736886120000
    },
    {
      "open": 23.0603,
      "high": 23.065,
      "low": 23.05,
      "close": 23.05,
      "volume": 2575,
      "datetime": 1736886180000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.005,
      "close": 23.005,
      "volume": 5862,
      "datetime": 1736886240000
    },
    {
      "open": 23.005,
      "high": 23.005,
      "low": 22.991,
      "close": 23,
      "volume": 10926,
      "datetime": 1736886300000
    },
    {
      "open": 23.01,
      "high": 23.04,
      "low": 23.01,
      "close": 23.04,
      "volume": 5080,
      "datetime": 1736886360000
    },
    {
      "open": 23.0309,
      "high": 23.0323,
      "low": 23.02,
      "close": 23.02,
      "volume": 975,
      "datetime": 1736886420000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23,
      "close": 23.01,
      "volume": 960,
      "datetime": 1736886480000
    },
    {
      "open": 23.0042,
      "high": 23.0042,
      "low": 23.0003,
      "close": 23.0003,
      "volume": 350,
      "datetime": 1736886540000
    },
    {
      "open": 23,
      "high": 23.038,
      "low": 22.995,
      "close": 23.03,
      "volume": 6680,
      "datetime": 1736886600000
    },
    {
      "open": 23.03,
      "high": 23.04,
      "low": 23.03,
      "close": 23.04,
      "volume": 500,
      "datetime": 1736886660000
    },
    {
      "open": 23.05,
      "high": 23.0801,
      "low": 23.05,
      "close": 23.08,
      "volume": 5715,
      "datetime": 1736886720000
    },
    {
      "open": 23.085,
      "high": 23.09,
      "low": 23.075,
      "close": 23.08,
      "volume": 3846,
      "datetime": 1736886780000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.09,
      "close": 23.09,
      "volume": 1199,
      "datetime": 1736886840000
    },
    {
      "open": 23.08,
      "high": 23.105,
      "low": 23.07,
      "close": 23.09,
      "volume": 5525,
      "datetime": 1736886900000
    },
    {
      "open": 23.1,
      "high": 23.11,
      "low": 23.065,
      "close": 23.09,
      "volume": 3700,
      "datetime": 1736886960000
    },
    {
      "open": 23.1,
      "high": 23.105,
      "low": 23.07,
      "close": 23.07,
      "volume": 1199,
      "datetime": 1736887020000
    },
    {
      "open": 23.07,
      "high": 23.1,
      "low": 23.06,
      "close": 23.1,
      "volume": 1025,
      "datetime": 1736887080000
    },
    {
      "open": 23.1,
      "high": 23.13,
      "low": 23.095,
      "close": 23.13,
      "volume": 1085,
      "datetime": 1736887140000
    },
    {
      "open": 23.13,
      "high": 23.145,
      "low": 23.13,
      "close": 23.145,
      "volume": 1100,
      "datetime": 1736887200000
    },
    {
      "open": 23.13,
      "high": 23.14,
      "low": 23.12,
      "close": 23.12,
      "volume": 2125,
      "datetime": 1736887260000
    },
    {
      "open": 23.14,
      "high": 23.1458,
      "low": 23.14,
      "close": 23.1458,
      "volume": 2310,
      "datetime": 1736887320000
    },
    {
      "open": 23.1499,
      "high": 23.16,
      "low": 23.12,
      "close": 23.12,
      "volume": 4758,
      "datetime": 1736887380000
    },
    {
      "open": 23.095,
      "high": 23.1,
      "low": 23.09,
      "close": 23.095,
      "volume": 500,
      "datetime": 1736887440000
    },
    {
      "open": 23.091,
      "high": 23.0998,
      "low": 23.0748,
      "close": 23.0998,
      "volume": 1400,
      "datetime": 1736887500000
    },
    {
      "open": 23.09,
      "high": 23.1,
      "low": 23.08,
      "close": 23.1,
      "volume": 675,
      "datetime": 1736887560000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.09,
      "close": 23.09,
      "volume": 875,
      "datetime": 1736887620000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.06,
      "close": 23.07,
      "volume": 7348,
      "datetime": 1736887680000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.065,
      "close": 23.07,
      "volume": 850,
      "datetime": 1736887740000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.045,
      "close": 23.06,
      "volume": 4593,
      "datetime": 1736887800000
    },
    {
      "open": 23.06,
      "high": 23.08,
      "low": 23.06,
      "close": 23.06,
      "volume": 5172,
      "datetime": 1736887860000
    },
    {
      "open": 23.0627,
      "high": 23.09,
      "low": 23.06,
      "close": 23.09,
      "volume": 10505,
      "datetime": 1736887920000
    },
    {
      "open": 23.0927,
      "high": 23.11,
      "low": 23.08,
      "close": 23.11,
      "volume": 7357,
      "datetime": 1736887980000
    },
    {
      "open": 23.105,
      "high": 23.115,
      "low": 23.1,
      "close": 23.1,
      "volume": 6872,
      "datetime": 1736888040000
    },
    {
      "open": 23.12,
      "high": 23.1379,
      "low": 23.11,
      "close": 23.13,
      "volume": 1812,
      "datetime": 1736888100000
    },
    {
      "open": 23.13,
      "high": 23.14,
      "low": 23.115,
      "close": 23.14,
      "volume": 19322,
      "datetime": 1736888160000
    },
    {
      "open": 23.13,
      "high": 23.135,
      "low": 23.12,
      "close": 23.135,
      "volume": 1767,
      "datetime": 1736888220000
    },
    {
      "open": 23.14,
      "high": 23.16,
      "low": 23.14,
      "close": 23.16,
      "volume": 4100,
      "datetime": 1736888280000
    },
    {
      "open": 23.16,
      "high": 23.16,
      "low": 23.065,
      "close": 23.115,
      "volume": 29324,
      "datetime": 1736888340000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.11,
      "close": 23.11,
      "volume": 2761,
      "datetime": 1736888400000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 100,
      "datetime": 1736888520000
    },
    {
      "open": 23.07,
      "high": 23.07,
      "low": 23.06,
      "close": 23.06,
      "volume": 1500,
      "datetime": 1736888760000
    },
    {
      "open": 23.0701,
      "high": 23.0701,
      "low": 23.07,
      "close": 23.07,
      "volume": 610,
      "datetime": 1736889060000
    },
    {
      "open": 23.1357,
      "high": 23.1357,
      "low": 23.1357,
      "close": 23.1357,
      "volume": 150,
      "datetime": 1736890200000
    },
    {
      "open": 23.1216,
      "high": 23.17,
      "low": 23.1216,
      "close": 23.17,
      "volume": 2069,
      "datetime": 1736890620000
    },
    {
      "open": 23.1107,
      "high": 23.1107,
      "low": 23.11,
      "close": 23.1101,
      "volume": 800,
      "datetime": 1736891040000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.11,
      "close": 23.11,
      "volume": 100,
      "datetime": 1736891640000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.11,
      "close": 23.11,
      "volume": 100,
      "datetime": 1736892480000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 180,
      "datetime": 1736893740000
    },
    {
      "open": 23.0361,
      "high": 23.0361,
      "low": 23.0361,
      "close": 23.0361,
      "volume": 222,
      "datetime": 1736894160000
    },
    {
      "open": 23.032,
      "high": 23.032,
      "low": 23.032,
      "close": 23.032,
      "volume": 250,
      "datetime": 1736894880000
    },
    {
      "open": 23.0301,
      "high": 23.0301,
      "low": 23.0301,
      "close": 23.0301,
      "volume": 4000,
      "datetime": 1736895120000
    },
    {
      "open": 23.04,
      "high": 23.04,
      "low": 23.04,
      "close": 23.04,
      "volume": 1000,
      "datetime": 1736896260000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 200,
      "datetime": 1736898960000
    },
    {
      "open": 23.08,
      "high": 23.08,
      "low": 23.08,
      "close": 23.08,
      "volume": 1000,
      "datetime": 1736899740000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 2127,
      "datetime": 1736899980000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 22.99,
      "close": 22.99,
      "volume": 2100,
      "datetime": 1736900520000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.97,
      "close": 22.97,
      "volume": 250,
      "datetime": 1736900580000
    },
    {
      "open": 22.94,
      "high": 22.94,
      "low": 22.94,
      "close": 22.94,
      "volume": 2000,
      "datetime": 1736900640000
    },
    {
      "open": 22.94,
      "high": 22.94,
      "low": 22.94,
      "close": 22.94,
      "volume": 150,
      "datetime": 1736900760000
    },
    {
      "open": 22.91,
      "high": 22.91,
      "low": 22.91,
      "close": 22.91,
      "volume": 600,
      "datetime": 1736900820000
    },
    {
      "open": 23.04,
      "high": 23.05,
      "low": 23.04,
      "close": 23.05,
      "volume": 1000,
      "datetime": 1736901420000
    },
    {
      "open": 23.03,
      "high": 23.03,
      "low": 23.03,
      "close": 23.03,
      "volume": 1080,
      "datetime": 1736901480000
    },
    {
      "open": 23.0386,
      "high": 23.0386,
      "low": 23.0386,
      "close": 23.0386,
      "volume": 500,
      "datetime": 1736901600000
    },
    {
      "open": 23.0498,
      "high": 23.05,
      "low": 23.0498,
      "close": 23.05,
      "volume": 670,
      "datetime": 1736901960000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 170,
      "datetime": 1736902020000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 500,
      "datetime": 1736902140000
    },
    {
      "open": 22.9907,
      "high": 22.9907,
      "low": 22.9907,
      "close": 22.9907,
      "volume": 200,
      "datetime": 1736902320000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 7000,
      "datetime": 1736902380000
    },
    {
      "open": 22.9901,
      "high": 22.9901,
      "low": 22.9901,
      "close": 22.9901,
      "volume": 715,
      "datetime": 1736902440000
    },
    {
      "open": 22.98,
      "high": 22.98,
      "low": 22.98,
      "close": 22.98,
      "volume": 3500,
      "datetime": 1736902500000
    },
    {
      "open": 23.0385,
      "high": 23.0385,
      "low": 23.0385,
      "close": 23.0385,
      "volume": 500,
      "datetime": 1736902620000
    },
    {
      "open": 23.0284,
      "high": 23.0284,
      "low": 23.0284,
      "close": 23.0284,
      "volume": 100,
      "datetime": 1736902680000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.96,
      "close": 22.96,
      "volume": 420,
      "datetime": 1736902920000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 11,
      "datetime": 1736903400000
    },
    {
      "open": 22.94,
      "high": 22.94,
      "low": 22.94,
      "close": 22.94,
      "volume": 369,
      "datetime": 1736903460000
    },
    {
      "open": 22.95,
      "high": 22.96,
      "low": 22.95,
      "close": 22.96,
      "volume": 181,
      "datetime": 1736904300000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 3,
      "datetime": 1736904720000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.96,
      "close": 22.96,
      "volume": 1,
      "datetime": 1736904840000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 300,
      "datetime": 1736905020000
    },
    {
      "open": 22.93,
      "high": 22.93,
      "low": 22.89,
      "close": 22.89,
      "volume": 36,
      "datetime": 1736905380000
    },
    {
      "open": 22.91,
      "high": 22.91,
      "low": 22.9,
      "close": 22.9,
      "volume": 25,
      "datetime": 1736905740000
    },
    {
      "open": 22.89,
      "high": 22.89,
      "low": 22.89,
      "close": 22.89,
      "volume": 2,
      "datetime": 1736906100000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 100,
      "datetime": 1736907000000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.95,
      "close": 22.95,
      "volume": 1000,
      "datetime": 1736907480000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.96,
      "close": 22.96,
      "volume": 50,
      "datetime": 1736907840000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 50,
      "datetime": 1736908860000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.99,
      "close": 22.99,
      "volume": 100,
      "datetime": 1736909760000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.99,
      "close": 22.99,
      "volume": 1,
      "datetime": 1736910060000
    },
    {
      "open": 22.97,
      "high": 22.97,
      "low": 22.97,
      "close": 22.97,
      "volume": 99,
      "datetime": 1736910120000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 1,
      "datetime": 1736910660000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 1,
      "datetime": 1736910960000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 23.02,
      "close": 23.02,
      "volume": 10,
      "datetime": 1736911440000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 10,
      "datetime": 1736911560000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 300,
      "datetime": 1736912880000
    },
    {
      "open": 22.94,
      "high": 22.94,
      "low": 22.94,
      "close": 22.94,
      "volume": 850,
      "datetime": 1736912940000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 500,
      "datetime": 1736913000000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.96,
      "close": 22.96,
      "volume": 100,
      "datetime": 1736913240000
    },
    {
      "open": 22.9,
      "high": 22.9,
      "low": 22.9,
      "close": 22.9,
      "volume": 1,
      "datetime": 1736913600000
    },
    {
      "open": 22.84,
      "high": 22.84,
      "low": 22.84,
      "close": 22.84,
      "volume": 1,
      "datetime": 1736913660000
    },
    {
      "open": 22.8,
      "high": 22.8,
      "low": 22.8,
      "close": 22.8,
      "volume": 33,
      "datetime": 1736913780000
    },
    {
      "open": 22.8,
      "high": 22.8,
      "low": 22.8,
      "close": 22.8,
      "volume": 10,
      "datetime": 1736913840000
    },
    {
      "open": 22.88,
      "high": 22.88,
      "low": 22.88,
      "close": 22.88,
      "volume": 1,
      "datetime": 1736914080000
    },
    {
      "open": 22.93,
      "high": 22.93,
      "low": 22.93,
      "close": 22.93,
      "volume": 1,
      "datetime": 1736915100000
    },
    {
      "open": 22.89,
      "high": 22.89,
      "low": 22.89,
      "close": 22.89,
      "volume": 1,
      "datetime": 1736915160000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.99,
      "close": 22.99,
      "volume": 2,
      "datetime": 1736917800000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 5,
      "datetime": 1736922420000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 1500,
      "datetime": 1736923080000
    },
    {
      "open": 22.96,
      "high": 22.96,
      "low": 22.96,
      "close": 22.96,
      "volume": 5,
      "datetime": 1736924220000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 4,
      "datetime": 1736924940000
    },
    {
      "open": 22.9,
      "high": 22.9,
      "low": 22.9,
      "close": 22.9,
      "volume": 50,
      "datetime": 1736925480000
    },
    {
      "open": 22.86,
      "high": 22.86,
      "low": 22.86,
      "close": 22.86,
      "volume": 2,
      "datetime": 1736925780000
    },
    {
      "open": 22.86,
      "high": 22.86,
      "low": 22.86,
      "close": 22.86,
      "volume": 1000,
      "datetime": 1736925900000
    },
    {
      "open": 22.85,
      "high": 22.85,
      "low": 22.85,
      "close": 22.85,
      "volume": 1,
      "datetime": 1736925960000
    },
    {
      "open": 22.9,
      "high": 22.9,
      "low": 22.9,
      "close": 22.9,
      "volume": 5,
      "datetime": 1736928900000
    },
    {
      "open": 22.975,
      "high": 22.975,
      "low": 22.975,
      "close": 22.975,
      "volume": 135,
      "datetime": 1736931600000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 782,
      "datetime": 1736931720000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 989,
      "datetime": 1736932260000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 250,
      "datetime": 1736937720000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 355,
      "datetime": 1736939040000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 100,
      "datetime": 1736940840000
    },
    {
      "open": 23.11,
      "high": 23.11,
      "low": 23.11,
      "close": 23.11,
      "volume": 100,
      "datetime": 1736941140000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 100,
      "datetime": 1736941800000
    },
    {
      "open": 23.09,
      "high": 23.11,
      "low": 23.09,
      "close": 23.11,
      "volume": 871,
      "datetime": 1736941920000
    },
    {
      "open": 23.1,
      "high": 23.1,
      "low": 23.1,
      "close": 23.1,
      "volume": 100,
      "datetime": 1736942100000
    },
    {
      "open": 23.02,
      "high": 23.02,
      "low": 23.01,
      "close": 23.01,
      "volume": 2000,
      "datetime": 1736942340000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 200,
      "datetime": 1736942460000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 100,
      "datetime": 1736943300000
    },
    {
      "open": 23.05,
      "high": 23.05,
      "low": 23.05,
      "close": 23.05,
      "volume": 200,
      "datetime": 1736943420000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 400,
      "datetime": 1736943480000
    },
    {
      "open": 23.09,
      "high": 23.09,
      "low": 23.09,
      "close": 23.09,
      "volume": 450,
      "datetime": 1736944080000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 300,
      "datetime": 1736944800000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 500,
      "datetime": 1736945220000
    },
    {
      "open": 23.01,
      "high": 23.01,
      "low": 23.01,
      "close": 23.01,
      "volume": 500,
      "datetime": 1736945400000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 900,
      "datetime": 1736945760000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 500,
      "datetime": 1736945820000
    },
    {
      "open": 22.99,
      "high": 22.99,
      "low": 22.99,
      "close": 22.99,
      "volume": 350,
      "datetime": 1736946000000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 250,
      "datetime": 1736946180000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 100,
      "datetime": 1736946420000
    },
    {
      "open": 23,
      "high": 23,
      "low": 23,
      "close": 23,
      "volume": 2174,
      "datetime": 1736946540000
    },
    {
      "open": 22.95,
      "high": 22.95,
      "low": 22.95,
      "close": 22.95,
      "volume": 100,
      "datetime": 1736947380000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 1500,
      "datetime": 1736947440000
    },
    {
      "open": 22.92,
      "high": 22.92,
      "low": 22.92,
      "close": 22.92,
      "volume": 300,
      "datetime": 1736947500000
    },
    {
      "open": 22.91,
      "high": 22.91,
      "low": 22.91,
      "close": 22.91,
      "volume": 700,
      "datetime": 1736947560000
    },
    {
      "open": 22.94,
      "high": 22.94,
      "low": 22.94,
      "close": 22.94,
      "volume": 300,
      "datetime": 1736947620000
    },
    {
      "open": 22.85,
      "high": 22.89,
      "low": 22.5413,
      "close": 22.62,
      "volume": 10862,
      "datetime": 1736947800000
    },
    {
      "open": 22.6,
      "high": 22.6,
      "low": 22.6,
      "close": 22.6,
      "volume": 200,
      "datetime": 1736947860000
    },
    {
      "open": 22.6712,
      "high": 22.6712,
      "low": 22.65,
      "close": 22.65,
      "volume": 2469,
      "datetime": 1736947920000
    },
    {
      "open": 22.61,
      "high": 22.61,
      "low": 22.57,
      "close": 22.61,
      "volume": 14194,
      "datetime": 1736947980000
    },
    {
      "open": 22.554,
      "high": 22.58,
      "low": 22.54,
      "close": 22.55,
      "volume": 8476,
      "datetime": 1736948040000
    },
    {
      "open": 22.69,
      "high": 22.69,
      "low": 22.69,
      "close": 22.69,
      "volume": 1000,
      "datetime": 1736948100000
    },
    {
      "open": 22.6399,
      "high": 22.64,
      "low": 22.58,
      "close": 22.639,
      "volume": 1955,
      "datetime": 1736948220000
    },
    {
      "open": 22.59,
      "high": 22.6,
      "low": 22.59,
      "close": 22.6,
      "volume": 1500,
      "datetime": 1736948280000
    },
    {
      "open": 22.63,
      "high": 22.63,
      "low": 22.6,
      "close": 22.6,
      "volume": 3230,
      "datetime": 1736948340000
    },
    {
      "open": 22.58,
      "high": 22.6,
      "low": 22.56,
      "close": 22.599,
      "volume": 4350,
      "datetime": 1736948400000
    },
    {
      "open": 22.5805,
      "high": 22.6,
      "low": 22.5805,
      "close": 22.6,
      "volume": 2106,
      "datetime": 1736948460000
    },
    {
      "open": 22.62,
      "high": 22.62,
      "low": 22.6,
      "close": 22.6,
      "volume": 690,
      "datetime": 1736948520000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.6292,
      "close": 22.6292,
      "volume": 348,
      "datetime": 1736948580000
    },
    {
      "open": 22.62,
      "high": 22.62,
      "low": 22.58,
      "close": 22.58,
      "volume": 21320,
      "datetime": 1736948640000
    },
    {
      "open": 22.58,
      "high": 22.58,
      "low": 22.56,
      "close": 22.56,
      "volume": 1500,
      "datetime": 1736948700000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.55,
      "close": 22.55,
      "volume": 1700,
      "datetime": 1736948760000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.51,
      "close": 22.51,
      "volume": 7436,
      "datetime": 1736948820000
    },
    {
      "open": 22.5,
      "high": 22.5094,
      "low": 22.47,
      "close": 22.47,
      "volume": 5565,
      "datetime": 1736948880000
    },
    {
      "open": 22.4892,
      "high": 22.49,
      "low": 22.47,
      "close": 22.48,
      "volume": 8656,
      "datetime": 1736948940000
    },
    {
      "open": 22.4701,
      "high": 22.4802,
      "low": 22.47,
      "close": 22.47,
      "volume": 3501,
      "datetime": 1736949000000
    },
    {
      "open": 22.49,
      "high": 22.51,
      "low": 22.49,
      "close": 22.51,
      "volume": 10010,
      "datetime": 1736949060000
    },
    {
      "open": 22.64,
      "high": 22.64,
      "low": 22.4807,
      "close": 22.49,
      "volume": 3424,
      "datetime": 1736949120000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.5101,
      "close": 22.55,
      "volume": 3160,
      "datetime": 1736949180000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.53,
      "close": 22.54,
      "volume": 2400,
      "datetime": 1736949240000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.5,
      "close": 22.51,
      "volume": 602,
      "datetime": 1736949300000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 700,
      "datetime": 1736949360000
    },
    {
      "open": 22.51,
      "high": 22.52,
      "low": 22.51,
      "close": 22.51,
      "volume": 1400,
      "datetime": 1736949420000
    },
    {
      "open": 22.5,
      "high": 22.53,
      "low": 22.5,
      "close": 22.53,
      "volume": 1450,
      "datetime": 1736949480000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.49,
      "close": 22.49,
      "volume": 400,
      "datetime": 1736949540000
    },
    {
      "open": 22.499,
      "high": 22.499,
      "low": 22.4204,
      "close": 22.4204,
      "volume": 1793,
      "datetime": 1736949600000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.3702,
      "close": 22.4098,
      "volume": 3225,
      "datetime": 1736949660000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.37,
      "close": 22.4,
      "volume": 2700,
      "datetime": 1736949720000
    },
    {
      "open": 22.4,
      "high": 22.43,
      "low": 22.4,
      "close": 22.43,
      "volume": 5300,
      "datetime": 1736949780000
    },
    {
      "open": 22.42,
      "high": 22.47,
      "low": 22.42,
      "close": 22.42,
      "volume": 2927,
      "datetime": 1736949840000
    },
    {
      "open": 22.4299,
      "high": 22.4299,
      "low": 22.4,
      "close": 22.4,
      "volume": 200,
      "datetime": 1736949960000
    },
    {
      "open": 22.45,
      "high": 22.47,
      "low": 22.45,
      "close": 22.47,
      "volume": 1200,
      "datetime": 1736950020000
    },
    {
      "open": 22.469,
      "high": 22.47,
      "low": 22.42,
      "close": 22.42,
      "volume": 487,
      "datetime": 1736950080000
    },
    {
      "open": 22.42,
      "high": 22.4499,
      "low": 22.42,
      "close": 22.4499,
      "volume": 1636,
      "datetime": 1736950140000
    },
    {
      "open": 22.45,
      "high": 22.47,
      "low": 22.45,
      "close": 22.47,
      "volume": 550,
      "datetime": 1736950200000
    },
    {
      "open": 22.467,
      "high": 22.47,
      "low": 22.467,
      "close": 22.47,
      "volume": 320,
      "datetime": 1736950260000
    },
    {
      "open": 22.45,
      "high": 22.459,
      "low": 22.45,
      "close": 22.459,
      "volume": 200,
      "datetime": 1736950320000
    },
    {
      "open": 22.47,
      "high": 22.51,
      "low": 22.47,
      "close": 22.51,
      "volume": 500,
      "datetime": 1736950380000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 497,
      "datetime": 1736950440000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.4993,
      "close": 22.5,
      "volume": 1300,
      "datetime": 1736950500000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.55,
      "close": 22.55,
      "volume": 388,
      "datetime": 1736950560000
    },
    {
      "open": 22.52,
      "high": 22.5481,
      "low": 22.51,
      "close": 22.5481,
      "volume": 8498,
      "datetime": 1736950740000
    },
    {
      "open": 22.49,
      "high": 22.4998,
      "low": 22.49,
      "close": 22.4998,
      "volume": 330,
      "datetime": 1736950800000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.4601,
      "close": 22.4601,
      "volume": 888,
      "datetime": 1736950920000
    },
    {
      "open": 22.4601,
      "high": 22.4803,
      "low": 22.4601,
      "close": 22.4803,
      "volume": 700,
      "datetime": 1736950980000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 500,
      "datetime": 1736951040000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 1200,
      "datetime": 1736951100000
    },
    {
      "open": 22.46,
      "high": 22.48,
      "low": 22.46,
      "close": 22.48,
      "volume": 1068,
      "datetime": 1736951160000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.47,
      "close": 22.47,
      "volume": 950,
      "datetime": 1736951220000
    },
    {
      "open": 22.56,
      "high": 22.56,
      "low": 22.54,
      "close": 22.56,
      "volume": 4778,
      "datetime": 1736951340000
    },
    {
      "open": 22.55,
      "high": 22.575,
      "low": 22.53,
      "close": 22.57,
      "volume": 24105,
      "datetime": 1736951400000
    },
    {
      "open": 22.56,
      "high": 22.57,
      "low": 22.497,
      "close": 22.497,
      "volume": 2124,
      "datetime": 1736951460000
    },
    {
      "open": 22.4999,
      "high": 22.4999,
      "low": 22.471,
      "close": 22.471,
      "volume": 5022,
      "datetime": 1736951520000
    },
    {
      "open": 22.49,
      "high": 22.49,
      "low": 22.47,
      "close": 22.47,
      "volume": 6740,
      "datetime": 1736951580000
    },
    {
      "open": 22.4752,
      "high": 22.51,
      "low": 22.4602,
      "close": 22.51,
      "volume": 10150,
      "datetime": 1736951640000
    },
    {
      "open": 22.5,
      "high": 22.54,
      "low": 22.5,
      "close": 22.54,
      "volume": 5460,
      "datetime": 1736951700000
    },
    {
      "open": 22.55,
      "high": 22.569,
      "low": 22.5302,
      "close": 22.531,
      "volume": 6658,
      "datetime": 1736951760000
    },
    {
      "open": 22.56,
      "high": 22.57,
      "low": 22.5355,
      "close": 22.559,
      "volume": 6729,
      "datetime": 1736951820000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.5499,
      "close": 22.55,
      "volume": 1779,
      "datetime": 1736951880000
    },
    {
      "open": 22.5055,
      "high": 22.5231,
      "low": 22.505,
      "close": 22.505,
      "volume": 2438,
      "datetime": 1736951940000
    },
    {
      "open": 22.498,
      "high": 22.498,
      "low": 22.49,
      "close": 22.49,
      "volume": 800,
      "datetime": 1736952000000
    },
    {
      "open": 22.51,
      "high": 22.5214,
      "low": 22.51,
      "close": 22.5125,
      "volume": 3706,
      "datetime": 1736952060000
    },
    {
      "open": 22.5047,
      "high": 22.54,
      "low": 22.5047,
      "close": 22.54,
      "volume": 2600,
      "datetime": 1736952120000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 490,
      "datetime": 1736952180000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.495,
      "close": 22.495,
      "volume": 6803,
      "datetime": 1736952240000
    },
    {
      "open": 22.5,
      "high": 22.5114,
      "low": 22.5,
      "close": 22.5114,
      "volume": 3500,
      "datetime": 1736952300000
    },
    {
      "open": 22.52,
      "high": 22.5398,
      "low": 22.51,
      "close": 22.518,
      "volume": 5899,
      "datetime": 1736952360000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.45,
      "close": 22.45,
      "volume": 5948,
      "datetime": 1736952420000
    },
    {
      "open": 22.45,
      "high": 22.49,
      "low": 22.45,
      "close": 22.48,
      "volume": 7138,
      "datetime": 1736952480000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.4452,
      "close": 22.45,
      "volume": 2285,
      "datetime": 1736952540000
    },
    {
      "open": 22.48,
      "high": 22.49,
      "low": 22.47,
      "close": 22.47,
      "volume": 1700,
      "datetime": 1736952600000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.42,
      "close": 22.4201,
      "volume": 1450,
      "datetime": 1736952660000
    },
    {
      "open": 22.415,
      "high": 22.42,
      "low": 22.4,
      "close": 22.4,
      "volume": 1184,
      "datetime": 1736952720000
    },
    {
      "open": 22.41,
      "high": 22.43,
      "low": 22.41,
      "close": 22.41,
      "volume": 7452,
      "datetime": 1736952780000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.3843,
      "close": 22.3975,
      "volume": 2875,
      "datetime": 1736952840000
    },
    {
      "open": 22.4179,
      "high": 22.4179,
      "low": 22.415,
      "close": 22.415,
      "volume": 300,
      "datetime": 1736952900000
    },
    {
      "open": 22.3874,
      "high": 22.39,
      "low": 22.3874,
      "close": 22.39,
      "volume": 350,
      "datetime": 1736952960000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.36,
      "close": 22.375,
      "volume": 4300,
      "datetime": 1736953020000
    },
    {
      "open": 22.38,
      "high": 22.39,
      "low": 22.3562,
      "close": 22.3562,
      "volume": 2070,
      "datetime": 1736953080000
    },
    {
      "open": 22.3501,
      "high": 22.37,
      "low": 22.3501,
      "close": 22.37,
      "volume": 953,
      "datetime": 1736953140000
    },
    {
      "open": 22.3616,
      "high": 22.362,
      "low": 22.31,
      "close": 22.31,
      "volume": 4893,
      "datetime": 1736953200000
    },
    {
      "open": 22.305,
      "high": 22.33,
      "low": 22.3,
      "close": 22.325,
      "volume": 8435,
      "datetime": 1736953260000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.33,
      "close": 22.33,
      "volume": 1524,
      "datetime": 1736953320000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.3007,
      "close": 22.305,
      "volume": 1368,
      "datetime": 1736953380000
    },
    {
      "open": 22.315,
      "high": 22.3347,
      "low": 22.31,
      "close": 22.32,
      "volume": 5490,
      "datetime": 1736953440000
    },
    {
      "open": 22.33,
      "high": 22.35,
      "low": 22.33,
      "close": 22.35,
      "volume": 4136,
      "datetime": 1736953500000
    },
    {
      "open": 22.355,
      "high": 22.3899,
      "low": 22.355,
      "close": 22.38,
      "volume": 5439,
      "datetime": 1736953560000
    },
    {
      "open": 22.3967,
      "high": 22.42,
      "low": 22.37,
      "close": 22.4,
      "volume": 3696,
      "datetime": 1736953620000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.34,
      "close": 22.34,
      "volume": 4311,
      "datetime": 1736953680000
    },
    {
      "open": 22.345,
      "high": 22.36,
      "low": 22.34,
      "close": 22.36,
      "volume": 2925,
      "datetime": 1736953740000
    },
    {
      "open": 22.37,
      "high": 22.3901,
      "low": 22.35,
      "close": 22.3599,
      "volume": 2122,
      "datetime": 1736953800000
    },
    {
      "open": 22.35,
      "high": 22.365,
      "low": 22.35,
      "close": 22.35,
      "volume": 2535,
      "datetime": 1736953860000
    },
    {
      "open": 22.35,
      "high": 22.365,
      "low": 22.325,
      "close": 22.365,
      "volume": 4203,
      "datetime": 1736953920000
    },
    {
      "open": 22.35,
      "high": 22.36,
      "low": 22.34,
      "close": 22.36,
      "volume": 8814,
      "datetime": 1736953980000
    },
    {
      "open": 22.37,
      "high": 22.4,
      "low": 22.37,
      "close": 22.4,
      "volume": 2025,
      "datetime": 1736954040000
    },
    {
      "open": 22.4118,
      "high": 22.425,
      "low": 22.405,
      "close": 22.4198,
      "volume": 3114,
      "datetime": 1736954100000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.39,
      "close": 22.41,
      "volume": 9334,
      "datetime": 1736954160000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.38,
      "close": 22.38,
      "volume": 9825,
      "datetime": 1736954220000
    },
    {
      "open": 22.39,
      "high": 22.408,
      "low": 22.39,
      "close": 22.408,
      "volume": 1542,
      "datetime": 1736954280000
    },
    {
      "open": 22.4,
      "high": 22.4299,
      "low": 22.4,
      "close": 22.4299,
      "volume": 1740,
      "datetime": 1736954340000
    },
    {
      "open": 22.42,
      "high": 22.45,
      "low": 22.42,
      "close": 22.435,
      "volume": 2905,
      "datetime": 1736954400000
    },
    {
      "open": 22.435,
      "high": 22.435,
      "low": 22.3999,
      "close": 22.4,
      "volume": 7212,
      "datetime": 1736954460000
    },
    {
      "open": 22.4,
      "high": 22.42,
      "low": 22.39,
      "close": 22.42,
      "volume": 475,
      "datetime": 1736954520000
    },
    {
      "open": 22.425,
      "high": 22.43,
      "low": 22.4199,
      "close": 22.43,
      "volume": 1100,
      "datetime": 1736954580000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.39,
      "close": 22.39,
      "volume": 1040,
      "datetime": 1736954640000
    },
    {
      "open": 22.4,
      "high": 22.4075,
      "low": 22.3959,
      "close": 22.3959,
      "volume": 2025,
      "datetime": 1736954700000
    },
    {
      "open": 22.4,
      "high": 22.41,
      "low": 22.39,
      "close": 22.39,
      "volume": 1401,
      "datetime": 1736954760000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.32,
      "close": 22.32,
      "volume": 6693,
      "datetime": 1736954820000
    },
    {
      "open": 22.315,
      "high": 22.33,
      "low": 22.31,
      "close": 22.31,
      "volume": 3489,
      "datetime": 1736954880000
    },
    {
      "open": 22.31,
      "high": 22.3119,
      "low": 22.29,
      "close": 22.305,
      "volume": 18128,
      "datetime": 1736954940000
    },
    {
      "open": 22.32,
      "high": 22.3279,
      "low": 22.31,
      "close": 22.3279,
      "volume": 4681,
      "datetime": 1736955000000
    },
    {
      "open": 22.32,
      "high": 22.35,
      "low": 22.32,
      "close": 22.33,
      "volume": 3761,
      "datetime": 1736955060000
    },
    {
      "open": 22.34,
      "high": 22.36,
      "low": 22.33,
      "close": 22.33,
      "volume": 900,
      "datetime": 1736955120000
    },
    {
      "open": 22.3324,
      "high": 22.37,
      "low": 22.3324,
      "close": 22.37,
      "volume": 2230,
      "datetime": 1736955180000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.345,
      "close": 22.35,
      "volume": 4253,
      "datetime": 1736955240000
    },
    {
      "open": 22.35,
      "high": 22.375,
      "low": 22.33,
      "close": 22.375,
      "volume": 3219,
      "datetime": 1736955300000
    },
    {
      "open": 22.375,
      "high": 22.4,
      "low": 22.375,
      "close": 22.4,
      "volume": 3941,
      "datetime": 1736955360000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.38,
      "close": 22.4,
      "volume": 2254,
      "datetime": 1736955420000
    },
    {
      "open": 22.385,
      "high": 22.385,
      "low": 22.35,
      "close": 22.35,
      "volume": 2570,
      "datetime": 1736955480000
    },
    {
      "open": 22.35,
      "high": 22.39,
      "low": 22.35,
      "close": 22.39,
      "volume": 1961,
      "datetime": 1736955540000
    },
    {
      "open": 22.39,
      "high": 22.4,
      "low": 22.39,
      "close": 22.4,
      "volume": 2775,
      "datetime": 1736955600000
    },
    {
      "open": 22.41,
      "high": 22.42,
      "low": 22.4,
      "close": 22.4,
      "volume": 2050,
      "datetime": 1736955660000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 1148,
      "datetime": 1736955720000
    },
    {
      "open": 22.41,
      "high": 22.42,
      "low": 22.405,
      "close": 22.42,
      "volume": 1688,
      "datetime": 1736955780000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.415,
      "close": 22.42,
      "volume": 3456,
      "datetime": 1736955840000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.39,
      "close": 22.39,
      "volume": 2290,
      "datetime": 1736955900000
    },
    {
      "open": 22.4,
      "high": 22.42,
      "low": 22.4,
      "close": 22.405,
      "volume": 4910,
      "datetime": 1736955960000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 1199,
      "datetime": 1736956020000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.37,
      "close": 22.37,
      "volume": 1821,
      "datetime": 1736956080000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.37,
      "close": 22.37,
      "volume": 2359,
      "datetime": 1736956140000
    },
    {
      "open": 22.37,
      "high": 22.41,
      "low": 22.37,
      "close": 22.4,
      "volume": 1593,
      "datetime": 1736956200000
    },
    {
      "open": 22.405,
      "high": 22.435,
      "low": 22.405,
      "close": 22.435,
      "volume": 2518,
      "datetime": 1736956260000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.4,
      "close": 22.4,
      "volume": 2307,
      "datetime": 1736956320000
    },
    {
      "open": 22.39,
      "high": 22.41,
      "low": 22.375,
      "close": 22.41,
      "volume": 8925,
      "datetime": 1736956380000
    },
    {
      "open": 22.4,
      "high": 22.41,
      "low": 22.39,
      "close": 22.41,
      "volume": 1250,
      "datetime": 1736956440000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.4057,
      "close": 22.41,
      "volume": 1250,
      "datetime": 1736956500000
    },
    {
      "open": 22.41,
      "high": 22.4301,
      "low": 22.4057,
      "close": 22.4301,
      "volume": 3066,
      "datetime": 1736956560000
    },
    {
      "open": 22.43,
      "high": 22.44,
      "low": 22.425,
      "close": 22.43,
      "volume": 2022,
      "datetime": 1736956620000
    },
    {
      "open": 22.44,
      "high": 22.49,
      "low": 22.44,
      "close": 22.4801,
      "volume": 4350,
      "datetime": 1736956680000
    },
    {
      "open": 22.48,
      "high": 22.5,
      "low": 22.48,
      "close": 22.4999,
      "volume": 9590,
      "datetime": 1736956740000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.44,
      "close": 22.45,
      "volume": 11290,
      "datetime": 1736956800000
    },
    {
      "open": 22.455,
      "high": 22.48,
      "low": 22.45,
      "close": 22.45,
      "volume": 2383,
      "datetime": 1736956860000
    },
    {
      "open": 22.45,
      "high": 22.47,
      "low": 22.42,
      "close": 22.42,
      "volume": 3194,
      "datetime": 1736956920000
    },
    {
      "open": 22.41,
      "high": 22.43,
      "low": 22.4,
      "close": 22.4,
      "volume": 2200,
      "datetime": 1736956980000
    },
    {
      "open": 22.415,
      "high": 22.42,
      "low": 22.4,
      "close": 22.4,
      "volume": 8090,
      "datetime": 1736957040000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.375,
      "close": 22.3843,
      "volume": 4536,
      "datetime": 1736957100000
    },
    {
      "open": 22.38,
      "high": 22.39,
      "low": 22.375,
      "close": 22.39,
      "volume": 2679,
      "datetime": 1736957160000
    },
    {
      "open": 22.39,
      "high": 22.41,
      "low": 22.39,
      "close": 22.4,
      "volume": 2887,
      "datetime": 1736957220000
    },
    {
      "open": 22.405,
      "high": 22.4357,
      "low": 22.405,
      "close": 22.415,
      "volume": 9221,
      "datetime": 1736957280000
    },
    {
      "open": 22.41,
      "high": 22.42,
      "low": 22.3737,
      "close": 22.3737,
      "volume": 3000,
      "datetime": 1736957340000
    },
    {
      "open": 22.38,
      "high": 22.39,
      "low": 22.38,
      "close": 22.38,
      "volume": 1549,
      "datetime": 1736957400000
    },
    {
      "open": 22.375,
      "high": 22.375,
      "low": 22.36,
      "close": 22.37,
      "volume": 2036,
      "datetime": 1736957460000
    },
    {
      "open": 22.37,
      "high": 22.39,
      "low": 22.37,
      "close": 22.38,
      "volume": 1575,
      "datetime": 1736957520000
    },
    {
      "open": 22.365,
      "high": 22.37,
      "low": 22.365,
      "close": 22.37,
      "volume": 350,
      "datetime": 1736957580000
    },
    {
      "open": 22.3782,
      "high": 22.38,
      "low": 22.3782,
      "close": 22.3799,
      "volume": 3675,
      "datetime": 1736957640000
    },
    {
      "open": 22.365,
      "high": 22.3702,
      "low": 22.365,
      "close": 22.37,
      "volume": 2475,
      "datetime": 1736957700000
    },
    {
      "open": 22.37,
      "high": 22.39,
      "low": 22.37,
      "close": 22.39,
      "volume": 975,
      "datetime": 1736957760000
    },
    {
      "open": 22.39,
      "high": 22.42,
      "low": 22.3728,
      "close": 22.42,
      "volume": 3025,
      "datetime": 1736957820000
    },
    {
      "open": 22.415,
      "high": 22.43,
      "low": 22.415,
      "close": 22.415,
      "volume": 9500,
      "datetime": 1736957880000
    },
    {
      "open": 22.41,
      "high": 22.43,
      "low": 22.41,
      "close": 22.425,
      "volume": 3391,
      "datetime": 1736957940000
    },
    {
      "open": 22.425,
      "high": 22.465,
      "low": 22.425,
      "close": 22.4548,
      "volume": 7921,
      "datetime": 1736958000000
    },
    {
      "open": 22.45,
      "high": 22.46,
      "low": 22.4457,
      "close": 22.45,
      "volume": 8450,
      "datetime": 1736958060000
    },
    {
      "open": 22.445,
      "high": 22.445,
      "low": 22.3901,
      "close": 22.3901,
      "volume": 3279,
      "datetime": 1736958120000
    },
    {
      "open": 22.38,
      "high": 22.39,
      "low": 22.3733,
      "close": 22.39,
      "volume": 1360,
      "datetime": 1736958180000
    },
    {
      "open": 22.395,
      "high": 22.44,
      "low": 22.395,
      "close": 22.44,
      "volume": 1528,
      "datetime": 1736958240000
    },
    {
      "open": 22.445,
      "high": 22.45,
      "low": 22.44,
      "close": 22.44,
      "volume": 3100,
      "datetime": 1736958300000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.425,
      "close": 22.425,
      "volume": 3800,
      "datetime": 1736958360000
    },
    {
      "open": 22.425,
      "high": 22.43,
      "low": 22.41,
      "close": 22.43,
      "volume": 3227,
      "datetime": 1736958420000
    },
    {
      "open": 22.435,
      "high": 22.44,
      "low": 22.4255,
      "close": 22.4255,
      "volume": 5670,
      "datetime": 1736958480000
    },
    {
      "open": 22.425,
      "high": 22.43,
      "low": 22.42,
      "close": 22.42,
      "volume": 1262,
      "datetime": 1736958540000
    },
    {
      "open": 22.42,
      "high": 22.46,
      "low": 22.42,
      "close": 22.46,
      "volume": 3782,
      "datetime": 1736958600000
    },
    {
      "open": 22.45,
      "high": 22.48,
      "low": 22.435,
      "close": 22.48,
      "volume": 915,
      "datetime": 1736958660000
    },
    {
      "open": 22.49,
      "high": 22.52,
      "low": 22.49,
      "close": 22.51,
      "volume": 2854,
      "datetime": 1736958720000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.47,
      "close": 22.49,
      "volume": 3871,
      "datetime": 1736958780000
    },
    {
      "open": 22.485,
      "high": 22.5099,
      "low": 22.48,
      "close": 22.5,
      "volume": 9450,
      "datetime": 1736958840000
    },
    {
      "open": 22.51,
      "high": 22.52,
      "low": 22.51,
      "close": 22.52,
      "volume": 1825,
      "datetime": 1736958900000
    },
    {
      "open": 22.515,
      "high": 22.515,
      "low": 22.4734,
      "close": 22.48,
      "volume": 1350,
      "datetime": 1736958960000
    },
    {
      "open": 22.48,
      "high": 22.495,
      "low": 22.48,
      "close": 22.495,
      "volume": 1825,
      "datetime": 1736959020000
    },
    {
      "open": 22.485,
      "high": 22.485,
      "low": 22.44,
      "close": 22.44,
      "volume": 2325,
      "datetime": 1736959080000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.44,
      "close": 22.44,
      "volume": 1198,
      "datetime": 1736959140000
    },
    {
      "open": 22.435,
      "high": 22.44,
      "low": 22.425,
      "close": 22.43,
      "volume": 1325,
      "datetime": 1736959200000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.44,
      "close": 22.44,
      "volume": 800,
      "datetime": 1736959260000
    },
    {
      "open": 22.45,
      "high": 22.48,
      "low": 22.45,
      "close": 22.48,
      "volume": 6000,
      "datetime": 1736959320000
    },
    {
      "open": 22.48,
      "high": 22.4843,
      "low": 22.475,
      "close": 22.4843,
      "volume": 1055,
      "datetime": 1736959380000
    },
    {
      "open": 22.49,
      "high": 22.49,
      "low": 22.49,
      "close": 22.49,
      "volume": 1755,
      "datetime": 1736959440000
    },
    {
      "open": 22.485,
      "high": 22.49,
      "low": 22.47,
      "close": 22.4899,
      "volume": 1700,
      "datetime": 1736959500000
    },
    {
      "open": 22.49,
      "high": 22.5,
      "low": 22.4843,
      "close": 22.495,
      "volume": 4699,
      "datetime": 1736959560000
    },
    {
      "open": 22.495,
      "high": 22.495,
      "low": 22.48,
      "close": 22.48,
      "volume": 1000,
      "datetime": 1736959620000
    },
    {
      "open": 22.475,
      "high": 22.48,
      "low": 22.475,
      "close": 22.48,
      "volume": 400,
      "datetime": 1736959680000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.45,
      "close": 22.45,
      "volume": 4405,
      "datetime": 1736959740000
    },
    {
      "open": 22.46,
      "high": 22.47,
      "low": 22.46,
      "close": 22.46,
      "volume": 4879,
      "datetime": 1736959800000
    },
    {
      "open": 22.4801,
      "high": 22.4801,
      "low": 22.4668,
      "close": 22.4668,
      "volume": 2800,
      "datetime": 1736959860000
    },
    {
      "open": 22.455,
      "high": 22.49,
      "low": 22.455,
      "close": 22.48,
      "volume": 9128,
      "datetime": 1736959920000
    },
    {
      "open": 22.48,
      "high": 22.5,
      "low": 22.4703,
      "close": 22.5,
      "volume": 3427,
      "datetime": 1736959980000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.4697,
      "close": 22.47,
      "volume": 4350,
      "datetime": 1736960040000
    },
    {
      "open": 22.47,
      "high": 22.479,
      "low": 22.47,
      "close": 22.479,
      "volume": 2372,
      "datetime": 1736960100000
    },
    {
      "open": 22.475,
      "high": 22.5,
      "low": 22.47,
      "close": 22.5,
      "volume": 3464,
      "datetime": 1736960160000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.4706,
      "close": 22.4706,
      "volume": 1950,
      "datetime": 1736960220000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.47,
      "close": 22.48,
      "volume": 950,
      "datetime": 1736960280000
    },
    {
      "open": 22.465,
      "high": 22.49,
      "low": 22.465,
      "close": 22.4823,
      "volume": 1775,
      "datetime": 1736960340000
    },
    {
      "open": 22.4899,
      "high": 22.4899,
      "low": 22.47,
      "close": 22.48,
      "volume": 1675,
      "datetime": 1736960400000
    },
    {
      "open": 22.475,
      "high": 22.475,
      "low": 22.45,
      "close": 22.45,
      "volume": 1166,
      "datetime": 1736960460000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.4279,
      "close": 22.4279,
      "volume": 900,
      "datetime": 1736960520000
    },
    {
      "open": 22.425,
      "high": 22.46,
      "low": 22.425,
      "close": 22.46,
      "volume": 2026,
      "datetime": 1736960580000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 675,
      "datetime": 1736960640000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.425,
      "close": 22.43,
      "volume": 1625,
      "datetime": 1736960700000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.4,
      "close": 22.4,
      "volume": 1225,
      "datetime": 1736960760000
    },
    {
      "open": 22.4,
      "high": 22.4101,
      "low": 22.4,
      "close": 22.4101,
      "volume": 836,
      "datetime": 1736960820000
    },
    {
      "open": 22.415,
      "high": 22.4498,
      "low": 22.415,
      "close": 22.44,
      "volume": 5119,
      "datetime": 1736960880000
    },
    {
      "open": 22.425,
      "high": 22.43,
      "low": 22.425,
      "close": 22.43,
      "volume": 875,
      "datetime": 1736960940000
    },
    {
      "open": 22.415,
      "high": 22.415,
      "low": 22.415,
      "close": 22.415,
      "volume": 300,
      "datetime": 1736961000000
    },
    {
      "open": 22.435,
      "high": 22.44,
      "low": 22.43,
      "close": 22.43,
      "volume": 2221,
      "datetime": 1736961060000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.405,
      "close": 22.41,
      "volume": 750,
      "datetime": 1736961120000
    },
    {
      "open": 22.4101,
      "high": 22.4101,
      "low": 22.41,
      "close": 22.41,
      "volume": 2100,
      "datetime": 1736961180000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 325,
      "datetime": 1736961240000
    },
    {
      "open": 22.405,
      "high": 22.41,
      "low": 22.405,
      "close": 22.41,
      "volume": 825,
      "datetime": 1736961300000
    },
    {
      "open": 22.421,
      "high": 22.421,
      "low": 22.4,
      "close": 22.4,
      "volume": 900,
      "datetime": 1736961360000
    },
    {
      "open": 22.405,
      "high": 22.415,
      "low": 22.405,
      "close": 22.415,
      "volume": 350,
      "datetime": 1736961420000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 300,
      "datetime": 1736961480000
    },
    {
      "open": 22.415,
      "high": 22.435,
      "low": 22.415,
      "close": 22.435,
      "volume": 540,
      "datetime": 1736961540000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.43,
      "close": 22.43,
      "volume": 1725,
      "datetime": 1736961600000
    },
    {
      "open": 22.425,
      "high": 22.44,
      "low": 22.425,
      "close": 22.44,
      "volume": 725,
      "datetime": 1736961660000
    },
    {
      "open": 22.45,
      "high": 22.47,
      "low": 22.45,
      "close": 22.46,
      "volume": 2925,
      "datetime": 1736961720000
    },
    {
      "open": 22.45,
      "high": 22.46,
      "low": 22.45,
      "close": 22.46,
      "volume": 1275,
      "datetime": 1736961780000
    },
    {
      "open": 22.4655,
      "high": 22.4655,
      "low": 22.45,
      "close": 22.46,
      "volume": 3300,
      "datetime": 1736961840000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.45,
      "close": 22.4518,
      "volume": 761,
      "datetime": 1736961900000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.445,
      "close": 22.45,
      "volume": 882,
      "datetime": 1736961960000
    },
    {
      "open": 22.44,
      "high": 22.45,
      "low": 22.44,
      "close": 22.45,
      "volume": 693,
      "datetime": 1736962020000
    },
    {
      "open": 22.455,
      "high": 22.455,
      "low": 22.45,
      "close": 22.45,
      "volume": 1463,
      "datetime": 1736962080000
    },
    {
      "open": 22.455,
      "high": 22.455,
      "low": 22.45,
      "close": 22.45,
      "volume": 1300,
      "datetime": 1736962140000
    },
    {
      "open": 22.44,
      "high": 22.45,
      "low": 22.44,
      "close": 22.45,
      "volume": 6308,
      "datetime": 1736962200000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.42,
      "close": 22.42,
      "volume": 1850,
      "datetime": 1736962260000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 296,
      "datetime": 1736962320000
    },
    {
      "open": 22.415,
      "high": 22.42,
      "low": 22.3984,
      "close": 22.42,
      "volume": 6853,
      "datetime": 1736962380000
    },
    {
      "open": 22.42,
      "high": 22.43,
      "low": 22.42,
      "close": 22.43,
      "volume": 970,
      "datetime": 1736962440000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.425,
      "close": 22.43,
      "volume": 1525,
      "datetime": 1736962500000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.42,
      "close": 22.42,
      "volume": 975,
      "datetime": 1736962560000
    },
    {
      "open": 22.415,
      "high": 22.42,
      "low": 22.415,
      "close": 22.42,
      "volume": 425,
      "datetime": 1736962620000
    },
    {
      "open": 22.43,
      "high": 22.44,
      "low": 22.43,
      "close": 22.44,
      "volume": 2275,
      "datetime": 1736962680000
    },
    {
      "open": 22.45,
      "high": 22.46,
      "low": 22.45,
      "close": 22.46,
      "volume": 2975,
      "datetime": 1736962740000
    },
    {
      "open": 22.465,
      "high": 22.4652,
      "low": 22.465,
      "close": 22.4652,
      "volume": 800,
      "datetime": 1736962800000
    },
    {
      "open": 22.475,
      "high": 22.475,
      "low": 22.4626,
      "close": 22.4691,
      "volume": 2375,
      "datetime": 1736962860000
    },
    {
      "open": 22.465,
      "high": 22.48,
      "low": 22.465,
      "close": 22.48,
      "volume": 3500,
      "datetime": 1736962920000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.4701,
      "close": 22.4701,
      "volume": 3450,
      "datetime": 1736962980000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.465,
      "close": 22.465,
      "volume": 1450,
      "datetime": 1736963040000
    },
    {
      "open": 22.46,
      "high": 22.48,
      "low": 22.46,
      "close": 22.47,
      "volume": 3572,
      "datetime": 1736963100000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 900,
      "datetime": 1736963160000
    },
    {
      "open": 22.475,
      "high": 22.4863,
      "low": 22.475,
      "close": 22.4863,
      "volume": 3804,
      "datetime": 1736963220000
    },
    {
      "open": 22.49,
      "high": 22.4982,
      "low": 22.49,
      "close": 22.49,
      "volume": 1875,
      "datetime": 1736963280000
    },
    {
      "open": 22.485,
      "high": 22.485,
      "low": 22.485,
      "close": 22.485,
      "volume": 100,
      "datetime": 1736963340000
    },
    {
      "open": 22.49,
      "high": 22.51,
      "low": 22.49,
      "close": 22.51,
      "volume": 1150,
      "datetime": 1736963400000
    },
    {
      "open": 22.515,
      "high": 22.52,
      "low": 22.51,
      "close": 22.52,
      "volume": 19446,
      "datetime": 1736963460000
    },
    {
      "open": 22.5199,
      "high": 22.54,
      "low": 22.5199,
      "close": 22.54,
      "volume": 2664,
      "datetime": 1736963520000
    },
    {
      "open": 22.5425,
      "high": 22.5599,
      "low": 22.5425,
      "close": 22.545,
      "volume": 3605,
      "datetime": 1736963580000
    },
    {
      "open": 22.5569,
      "high": 22.56,
      "low": 22.55,
      "close": 22.55,
      "volume": 36784,
      "datetime": 1736963640000
    },
    {
      "open": 22.55,
      "high": 22.5644,
      "low": 22.54,
      "close": 22.56,
      "volume": 2725,
      "datetime": 1736963700000
    },
    {
      "open": 22.57,
      "high": 22.5845,
      "low": 22.565,
      "close": 22.57,
      "volume": 4917,
      "datetime": 1736963760000
    },
    {
      "open": 22.565,
      "high": 22.565,
      "low": 22.565,
      "close": 22.565,
      "volume": 200,
      "datetime": 1736963820000
    },
    {
      "open": 22.575,
      "high": 22.58,
      "low": 22.57,
      "close": 22.58,
      "volume": 18200,
      "datetime": 1736963880000
    },
    {
      "open": 22.5912,
      "high": 22.595,
      "low": 22.58,
      "close": 22.58,
      "volume": 2650,
      "datetime": 1736963940000
    },
    {
      "open": 22.57,
      "high": 22.5755,
      "low": 22.5601,
      "close": 22.5699,
      "volume": 10125,
      "datetime": 1736964000000
    },
    {
      "open": 22.55,
      "high": 22.55,
      "low": 22.54,
      "close": 22.55,
      "volume": 2830,
      "datetime": 1736964060000
    },
    {
      "open": 22.55,
      "high": 22.56,
      "low": 22.54,
      "close": 22.54,
      "volume": 1675,
      "datetime": 1736964120000
    },
    {
      "open": 22.535,
      "high": 22.535,
      "low": 22.535,
      "close": 22.535,
      "volume": 300,
      "datetime": 1736964180000
    },
    {
      "open": 22.56,
      "high": 22.5673,
      "low": 22.54,
      "close": 22.54,
      "volume": 1403,
      "datetime": 1736964240000
    },
    {
      "open": 22.535,
      "high": 22.535,
      "low": 22.51,
      "close": 22.52,
      "volume": 5816,
      "datetime": 1736964300000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 650,
      "datetime": 1736964360000
    },
    {
      "open": 22.515,
      "high": 22.52,
      "low": 22.515,
      "close": 22.52,
      "volume": 825,
      "datetime": 1736964420000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.515,
      "close": 22.52,
      "volume": 925,
      "datetime": 1736964480000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.515,
      "close": 22.52,
      "volume": 725,
      "datetime": 1736964540000
    },
    {
      "open": 22.52,
      "high": 22.54,
      "low": 22.52,
      "close": 22.54,
      "volume": 1450,
      "datetime": 1736964600000
    },
    {
      "open": 22.53,
      "high": 22.535,
      "low": 22.53,
      "close": 22.53,
      "volume": 3033,
      "datetime": 1736964660000
    },
    {
      "open": 22.525,
      "high": 22.53,
      "low": 22.52,
      "close": 22.52,
      "volume": 1750,
      "datetime": 1736964720000
    },
    {
      "open": 22.5143,
      "high": 22.52,
      "low": 22.5143,
      "close": 22.52,
      "volume": 560,
      "datetime": 1736964780000
    },
    {
      "open": 22.515,
      "high": 22.515,
      "low": 22.5128,
      "close": 22.5128,
      "volume": 200,
      "datetime": 1736964840000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.4768,
      "close": 22.4768,
      "volume": 10525,
      "datetime": 1736964900000
    },
    {
      "open": 22.465,
      "high": 22.4796,
      "low": 22.465,
      "close": 22.47,
      "volume": 2150,
      "datetime": 1736964960000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.466,
      "close": 22.47,
      "volume": 1525,
      "datetime": 1736965020000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.46,
      "close": 22.46,
      "volume": 1175,
      "datetime": 1736965080000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.445,
      "close": 22.45,
      "volume": 1300,
      "datetime": 1736965140000
    },
    {
      "open": 22.4313,
      "high": 22.46,
      "low": 22.43,
      "close": 22.46,
      "volume": 1775,
      "datetime": 1736965200000
    },
    {
      "open": 22.455,
      "high": 22.46,
      "low": 22.455,
      "close": 22.46,
      "volume": 2050,
      "datetime": 1736965260000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.46,
      "close": 22.46,
      "volume": 1389,
      "datetime": 1736965320000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.46,
      "close": 22.46,
      "volume": 325,
      "datetime": 1736965380000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.4432,
      "close": 22.45,
      "volume": 875,
      "datetime": 1736965440000
    },
    {
      "open": 22.455,
      "high": 22.47,
      "low": 22.4503,
      "close": 22.47,
      "volume": 3760,
      "datetime": 1736965500000
    },
    {
      "open": 22.4655,
      "high": 22.47,
      "low": 22.4655,
      "close": 22.47,
      "volume": 875,
      "datetime": 1736965560000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.46,
      "close": 22.46,
      "volume": 1950,
      "datetime": 1736965620000
    },
    {
      "open": 22.455,
      "high": 22.465,
      "low": 22.4545,
      "close": 22.4545,
      "volume": 2293,
      "datetime": 1736965680000
    },
    {
      "open": 22.4599,
      "high": 22.46,
      "low": 22.4599,
      "close": 22.46,
      "volume": 2000,
      "datetime": 1736965740000
    },
    {
      "open": 22.455,
      "high": 22.46,
      "low": 22.445,
      "close": 22.4599,
      "volume": 6103,
      "datetime": 1736965800000
    },
    {
      "open": 22.46,
      "high": 22.462,
      "low": 22.4543,
      "close": 22.4543,
      "volume": 4110,
      "datetime": 1736965860000
    },
    {
      "open": 22.46,
      "high": 22.4626,
      "low": 22.455,
      "close": 22.4626,
      "volume": 1175,
      "datetime": 1736965920000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.4799,
      "close": 22.4799,
      "volume": 1600,
      "datetime": 1736965980000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.46,
      "close": 22.46,
      "volume": 1100,
      "datetime": 1736966040000
    },
    {
      "open": 22.46,
      "high": 22.4719,
      "low": 22.455,
      "close": 22.47,
      "volume": 1734,
      "datetime": 1736966100000
    },
    {
      "open": 22.47,
      "high": 22.48,
      "low": 22.47,
      "close": 22.48,
      "volume": 2175,
      "datetime": 1736966160000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.475,
      "close": 22.48,
      "volume": 850,
      "datetime": 1736966220000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.4799,
      "close": 22.4799,
      "volume": 875,
      "datetime": 1736966280000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.465,
      "close": 22.465,
      "volume": 600,
      "datetime": 1736966340000
    },
    {
      "open": 22.47,
      "high": 22.48,
      "low": 22.46,
      "close": 22.46,
      "volume": 974,
      "datetime": 1736966400000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.44,
      "close": 22.45,
      "volume": 1282,
      "datetime": 1736966460000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.44,
      "close": 22.44,
      "volume": 1275,
      "datetime": 1736966520000
    },
    {
      "open": 22.435,
      "high": 22.435,
      "low": 22.42,
      "close": 22.42,
      "volume": 1040,
      "datetime": 1736966580000
    },
    {
      "open": 22.41,
      "high": 22.42,
      "low": 22.405,
      "close": 22.42,
      "volume": 3865,
      "datetime": 1736966640000
    },
    {
      "open": 22.4073,
      "high": 22.4073,
      "low": 22.4073,
      "close": 22.4073,
      "volume": 1000,
      "datetime": 1736966700000
    },
    {
      "open": 22.4,
      "high": 22.4077,
      "low": 22.395,
      "close": 22.4,
      "volume": 14089,
      "datetime": 1736966760000
    },
    {
      "open": 22.4,
      "high": 22.42,
      "low": 22.4,
      "close": 22.42,
      "volume": 1225,
      "datetime": 1736966820000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.415,
      "close": 22.415,
      "volume": 500,
      "datetime": 1736966880000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 865,
      "datetime": 1736966940000
    },
    {
      "open": 22.4,
      "high": 22.4099,
      "low": 22.4,
      "close": 22.4099,
      "volume": 600,
      "datetime": 1736967000000
    },
    {
      "open": 22.405,
      "high": 22.41,
      "low": 22.405,
      "close": 22.41,
      "volume": 775,
      "datetime": 1736967060000
    },
    {
      "open": 22.4,
      "high": 22.405,
      "low": 22.4,
      "close": 22.405,
      "volume": 300,
      "datetime": 1736967120000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.385,
      "close": 22.385,
      "volume": 1433,
      "datetime": 1736967180000
    },
    {
      "open": 22.39,
      "high": 22.3932,
      "low": 22.3832,
      "close": 22.3832,
      "volume": 2620,
      "datetime": 1736967240000
    },
    {
      "open": 22.385,
      "high": 22.4001,
      "low": 22.385,
      "close": 22.4001,
      "volume": 3469,
      "datetime": 1736967300000
    },
    {
      "open": 22.399,
      "high": 22.399,
      "low": 22.3855,
      "close": 22.39,
      "volume": 1545,
      "datetime": 1736967360000
    },
    {
      "open": 22.3837,
      "high": 22.39,
      "low": 22.3837,
      "close": 22.385,
      "volume": 1239,
      "datetime": 1736967420000
    },
    {
      "open": 22.3843,
      "high": 22.3843,
      "low": 22.3701,
      "close": 22.3701,
      "volume": 1269,
      "datetime": 1736967480000
    },
    {
      "open": 22.385,
      "high": 22.385,
      "low": 22.37,
      "close": 22.37,
      "volume": 2613,
      "datetime": 1736967540000
    },
    {
      "open": 22.365,
      "high": 22.37,
      "low": 22.365,
      "close": 22.37,
      "volume": 1945,
      "datetime": 1736967600000
    },
    {
      "open": 22.365,
      "high": 22.37,
      "low": 22.365,
      "close": 22.37,
      "volume": 2113,
      "datetime": 1736967660000
    },
    {
      "open": 22.365,
      "high": 22.365,
      "low": 22.35,
      "close": 22.35,
      "volume": 1526,
      "datetime": 1736967720000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.34,
      "close": 22.34,
      "volume": 1823,
      "datetime": 1736967780000
    },
    {
      "open": 22.355,
      "high": 22.355,
      "low": 22.3532,
      "close": 22.3532,
      "volume": 692,
      "datetime": 1736967840000
    },
    {
      "open": 22.345,
      "high": 22.35,
      "low": 22.345,
      "close": 22.35,
      "volume": 820,
      "datetime": 1736967900000
    },
    {
      "open": 22.345,
      "high": 22.3554,
      "low": 22.345,
      "close": 22.3526,
      "volume": 1300,
      "datetime": 1736967960000
    },
    {
      "open": 22.3557,
      "high": 22.3557,
      "low": 22.35,
      "close": 22.35,
      "volume": 1113,
      "datetime": 1736968020000
    },
    {
      "open": 22.3537,
      "high": 22.37,
      "low": 22.3537,
      "close": 22.37,
      "volume": 425,
      "datetime": 1736968080000
    },
    {
      "open": 22.378,
      "high": 22.39,
      "low": 22.378,
      "close": 22.38,
      "volume": 3009,
      "datetime": 1736968140000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.38,
      "close": 22.38,
      "volume": 1624,
      "datetime": 1736968200000
    },
    {
      "open": 22.38,
      "high": 22.39,
      "low": 22.38,
      "close": 22.39,
      "volume": 2524,
      "datetime": 1736968260000
    },
    {
      "open": 22.385,
      "high": 22.39,
      "low": 22.385,
      "close": 22.39,
      "volume": 400,
      "datetime": 1736968320000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.375,
      "close": 22.3755,
      "volume": 4033,
      "datetime": 1736968380000
    },
    {
      "open": 22.38,
      "high": 22.385,
      "low": 22.38,
      "close": 22.385,
      "volume": 425,
      "datetime": 1736968440000
    },
    {
      "open": 22.385,
      "high": 22.3899,
      "low": 22.3832,
      "close": 22.3832,
      "volume": 400,
      "datetime": 1736968500000
    },
    {
      "open": 22.3945,
      "high": 22.4,
      "low": 22.3945,
      "close": 22.4,
      "volume": 350,
      "datetime": 1736968560000
    },
    {
      "open": 22.4001,
      "high": 22.4001,
      "low": 22.4001,
      "close": 22.4001,
      "volume": 400,
      "datetime": 1736968620000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 679,
      "datetime": 1736968680000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.38,
      "close": 22.38,
      "volume": 650,
      "datetime": 1736968740000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.38,
      "close": 22.3803,
      "volume": 2825,
      "datetime": 1736968800000
    },
    {
      "open": 22.385,
      "high": 22.3982,
      "low": 22.385,
      "close": 22.3982,
      "volume": 350,
      "datetime": 1736968860000
    },
    {
      "open": 22.39,
      "high": 22.395,
      "low": 22.39,
      "close": 22.395,
      "volume": 450,
      "datetime": 1736968920000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.415,
      "close": 22.415,
      "volume": 599,
      "datetime": 1736968980000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 600,
      "datetime": 1736969040000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.395,
      "close": 22.395,
      "volume": 200,
      "datetime": 1736969100000
    },
    {
      "open": 22.4,
      "high": 22.41,
      "low": 22.4,
      "close": 22.4,
      "volume": 1250,
      "datetime": 1736969160000
    },
    {
      "open": 22.385,
      "high": 22.385,
      "low": 22.38,
      "close": 22.38,
      "volume": 1850,
      "datetime": 1736969280000
    },
    {
      "open": 22.3828,
      "high": 22.4,
      "low": 22.3828,
      "close": 22.4,
      "volume": 1084,
      "datetime": 1736969340000
    },
    {
      "open": 22.4099,
      "high": 22.4099,
      "low": 22.39,
      "close": 22.4,
      "volume": 900,
      "datetime": 1736969400000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 750,
      "datetime": 1736969460000
    },
    {
      "open": 22.375,
      "high": 22.375,
      "low": 22.3666,
      "close": 22.37,
      "volume": 868,
      "datetime": 1736969520000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.365,
      "close": 22.37,
      "volume": 1225,
      "datetime": 1736969580000
    },
    {
      "open": 22.385,
      "high": 22.39,
      "low": 22.37,
      "close": 22.37,
      "volume": 900,
      "datetime": 1736969640000
    },
    {
      "open": 22.375,
      "high": 22.375,
      "low": 22.35,
      "close": 22.35,
      "volume": 1873,
      "datetime": 1736969700000
    },
    {
      "open": 22.35,
      "high": 22.3501,
      "low": 22.3227,
      "close": 22.33,
      "volume": 1019,
      "datetime": 1736969760000
    },
    {
      "open": 22.33,
      "high": 22.3303,
      "low": 22.33,
      "close": 22.3303,
      "volume": 1600,
      "datetime": 1736969820000
    },
    {
      "open": 22.335,
      "high": 22.335,
      "low": 22.32,
      "close": 22.32,
      "volume": 1070,
      "datetime": 1736969880000
    },
    {
      "open": 22.3212,
      "high": 22.34,
      "low": 22.3212,
      "close": 22.34,
      "volume": 2550,
      "datetime": 1736969940000
    },
    {
      "open": 22.335,
      "high": 22.35,
      "low": 22.335,
      "close": 22.35,
      "volume": 1150,
      "datetime": 1736970000000
    },
    {
      "open": 22.3445,
      "high": 22.355,
      "low": 22.3409,
      "close": 22.3409,
      "volume": 1675,
      "datetime": 1736970060000
    },
    {
      "open": 22.36,
      "high": 22.365,
      "low": 22.36,
      "close": 22.365,
      "volume": 475,
      "datetime": 1736970120000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.36,
      "close": 22.36,
      "volume": 1225,
      "datetime": 1736970180000
    },
    {
      "open": 22.37,
      "high": 22.38,
      "low": 22.37,
      "close": 22.38,
      "volume": 650,
      "datetime": 1736970240000
    },
    {
      "open": 22.3845,
      "high": 22.3845,
      "low": 22.3845,
      "close": 22.3845,
      "volume": 192,
      "datetime": 1736970300000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.36,
      "close": 22.36,
      "volume": 200,
      "datetime": 1736970360000
    },
    {
      "open": 22.355,
      "high": 22.3681,
      "low": 22.355,
      "close": 22.3681,
      "volume": 400,
      "datetime": 1736970420000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.34,
      "close": 22.34,
      "volume": 3500,
      "datetime": 1736970480000
    },
    {
      "open": 22.33,
      "high": 22.34,
      "low": 22.33,
      "close": 22.33,
      "volume": 1134,
      "datetime": 1736970540000
    },
    {
      "open": 22.335,
      "high": 22.34,
      "low": 22.33,
      "close": 22.33,
      "volume": 1692,
      "datetime": 1736970600000
    },
    {
      "open": 22.32,
      "high": 22.33,
      "low": 22.32,
      "close": 22.32,
      "volume": 2916,
      "datetime": 1736970660000
    },
    {
      "open": 22.32,
      "high": 22.325,
      "low": 22.303,
      "close": 22.303,
      "volume": 4291,
      "datetime": 1736970720000
    },
    {
      "open": 22.3055,
      "high": 22.3055,
      "low": 22.305,
      "close": 22.305,
      "volume": 292,
      "datetime": 1736970780000
    },
    {
      "open": 22.3025,
      "high": 22.31,
      "low": 22.3025,
      "close": 22.31,
      "volume": 4159,
      "datetime": 1736970840000
    },
    {
      "open": 22.31,
      "high": 22.31,
      "low": 22.3099,
      "close": 22.3099,
      "volume": 600,
      "datetime": 1736970900000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.2902,
      "close": 22.2902,
      "volume": 2253,
      "datetime": 1736970960000
    },
    {
      "open": 22.29,
      "high": 22.29,
      "low": 22.26,
      "close": 22.2601,
      "volume": 9104,
      "datetime": 1736971020000
    },
    {
      "open": 22.27,
      "high": 22.28,
      "low": 22.27,
      "close": 22.28,
      "volume": 6186,
      "datetime": 1736971080000
    },
    {
      "open": 22.275,
      "high": 22.28,
      "low": 22.275,
      "close": 22.28,
      "volume": 650,
      "datetime": 1736971140000
    },
    {
      "open": 22.265,
      "high": 22.265,
      "low": 22.24,
      "close": 22.255,
      "volume": 3870,
      "datetime": 1736971200000
    },
    {
      "open": 22.26,
      "high": 22.26,
      "low": 22.249,
      "close": 22.249,
      "volume": 200,
      "datetime": 1736971260000
    },
    {
      "open": 22.25,
      "high": 22.25,
      "low": 22.24,
      "close": 22.24,
      "volume": 2650,
      "datetime": 1736971320000
    },
    {
      "open": 22.2461,
      "high": 22.2461,
      "low": 22.22,
      "close": 22.24,
      "volume": 18950,
      "datetime": 1736971380000
    },
    {
      "open": 22.27,
      "high": 22.295,
      "low": 22.27,
      "close": 22.295,
      "volume": 650,
      "datetime": 1736971440000
    },
    {
      "open": 22.295,
      "high": 22.3,
      "low": 22.28,
      "close": 22.295,
      "volume": 2201,
      "datetime": 1736971500000
    },
    {
      "open": 22.295,
      "high": 22.295,
      "low": 22.26,
      "close": 22.265,
      "volume": 1775,
      "datetime": 1736971560000
    },
    {
      "open": 22.24,
      "high": 22.24,
      "low": 22.23,
      "close": 22.235,
      "volume": 2875,
      "datetime": 1736971620000
    },
    {
      "open": 22.24,
      "high": 22.24,
      "low": 22.22,
      "close": 22.22,
      "volume": 1558,
      "datetime": 1736971680000
    },
    {
      "open": 22.2145,
      "high": 22.2145,
      "low": 22.185,
      "close": 22.19,
      "volume": 9149,
      "datetime": 1736971740000
    },
    {
      "open": 22.19,
      "high": 22.2099,
      "low": 22.19,
      "close": 22.2,
      "volume": 849,
      "datetime": 1736971800000
    },
    {
      "open": 22.205,
      "high": 22.22,
      "low": 22.17,
      "close": 22.17,
      "volume": 14004,
      "datetime": 1736971860000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.14,
      "close": 22.1599,
      "volume": 3822,
      "datetime": 1736971920000
    },
    {
      "open": 22.14,
      "high": 22.1713,
      "low": 22.14,
      "close": 22.17,
      "volume": 4300,
      "datetime": 1736971980000
    },
    {
      "open": 22.17,
      "high": 22.19,
      "low": 22.17,
      "close": 22.18,
      "volume": 2640,
      "datetime": 1736972040000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.17,
      "close": 22.1799,
      "volume": 1564,
      "datetime": 1736972100000
    },
    {
      "open": 22.1703,
      "high": 22.1703,
      "low": 22.16,
      "close": 22.16,
      "volume": 4553,
      "datetime": 1736972160000
    },
    {
      "open": 22.16,
      "high": 22.1634,
      "low": 22.14,
      "close": 22.14,
      "volume": 1525,
      "datetime": 1736972220000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.125,
      "close": 22.125,
      "volume": 1496,
      "datetime": 1736972280000
    },
    {
      "open": 22.115,
      "high": 22.12,
      "low": 22.1126,
      "close": 22.115,
      "volume": 2508,
      "datetime": 1736972340000
    },
    {
      "open": 22.115,
      "high": 22.12,
      "low": 22.094,
      "close": 22.11,
      "volume": 20939,
      "datetime": 1736972400000
    },
    {
      "open": 22.11,
      "high": 22.11,
      "low": 22.07,
      "close": 22.07,
      "volume": 4266,
      "datetime": 1736972460000
    },
    {
      "open": 22.08,
      "high": 22.085,
      "low": 22.07,
      "close": 22.08,
      "volume": 18759,
      "datetime": 1736972520000
    },
    {
      "open": 22.08,
      "high": 22.08,
      "low": 22.0747,
      "close": 22.0747,
      "volume": 400,
      "datetime": 1736972580000
    },
    {
      "open": 22.07,
      "high": 22.07,
      "low": 22.07,
      "close": 22.07,
      "volume": 100,
      "datetime": 1736972640000
    },
    {
      "open": 22.09,
      "high": 22.09,
      "low": 22.0874,
      "close": 22.0874,
      "volume": 600,
      "datetime": 1736972700000
    },
    {
      "open": 22.09,
      "high": 22.13,
      "low": 22.09,
      "close": 22.1235,
      "volume": 3666,
      "datetime": 1736972760000
    },
    {
      "open": 22.13,
      "high": 22.14,
      "low": 22.13,
      "close": 22.14,
      "volume": 2050,
      "datetime": 1736972820000
    },
    {
      "open": 22.17,
      "high": 22.205,
      "low": 22.17,
      "close": 22.205,
      "volume": 23224,
      "datetime": 1736972880000
    },
    {
      "open": 22.205,
      "high": 22.205,
      "low": 22.19,
      "close": 22.195,
      "volume": 2703,
      "datetime": 1736972940000
    },
    {
      "open": 22.1934,
      "high": 22.2178,
      "low": 22.1934,
      "close": 22.21,
      "volume": 2825,
      "datetime": 1736973000000
    },
    {
      "open": 22.2422,
      "high": 22.2422,
      "low": 22.235,
      "close": 22.24,
      "volume": 3025,
      "datetime": 1736973060000
    },
    {
      "open": 22.23,
      "high": 22.23,
      "low": 22.2,
      "close": 22.215,
      "volume": 1150,
      "datetime": 1736973120000
    },
    {
      "open": 22.212,
      "high": 22.22,
      "low": 22.21,
      "close": 22.21,
      "volume": 1575,
      "datetime": 1736973180000
    },
    {
      "open": 22.21,
      "high": 22.21,
      "low": 22.2,
      "close": 22.2099,
      "volume": 3890,
      "datetime": 1736973240000
    },
    {
      "open": 22.21,
      "high": 22.23,
      "low": 22.2007,
      "close": 22.23,
      "volume": 2130,
      "datetime": 1736973300000
    },
    {
      "open": 22.25,
      "high": 22.26,
      "low": 22.245,
      "close": 22.26,
      "volume": 5308,
      "datetime": 1736973360000
    },
    {
      "open": 22.26,
      "high": 22.2698,
      "low": 22.2598,
      "close": 22.2698,
      "volume": 1887,
      "datetime": 1736973420000
    },
    {
      "open": 22.27,
      "high": 22.27,
      "low": 22.2698,
      "close": 22.2698,
      "volume": 1425,
      "datetime": 1736973480000
    },
    {
      "open": 22.27,
      "high": 22.28,
      "low": 22.27,
      "close": 22.2753,
      "volume": 5941,
      "datetime": 1736973540000
    },
    {
      "open": 22.2766,
      "high": 22.29,
      "low": 22.27,
      "close": 22.285,
      "volume": 911,
      "datetime": 1736973600000
    },
    {
      "open": 22.3,
      "high": 22.305,
      "low": 22.29,
      "close": 22.305,
      "volume": 2755,
      "datetime": 1736973660000
    },
    {
      "open": 22.31,
      "high": 22.315,
      "low": 22.295,
      "close": 22.305,
      "volume": 4168,
      "datetime": 1736973720000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.31,
      "close": 22.315,
      "volume": 3209,
      "datetime": 1736973780000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.29,
      "close": 22.3,
      "volume": 14893,
      "datetime": 1736973840000
    },
    {
      "open": 22.3,
      "high": 22.3201,
      "low": 22.295,
      "close": 22.31,
      "volume": 3213,
      "datetime": 1736973900000
    },
    {
      "open": 22.3,
      "high": 22.31,
      "low": 22.29,
      "close": 22.31,
      "volume": 1635,
      "datetime": 1736973960000
    },
    {
      "open": 22.3399,
      "high": 22.3467,
      "low": 22.3399,
      "close": 22.3467,
      "volume": 4296,
      "datetime": 1736974020000
    },
    {
      "open": 22.3427,
      "high": 22.37,
      "low": 22.3427,
      "close": 22.37,
      "volume": 4437,
      "datetime": 1736974080000
    },
    {
      "open": 22.375,
      "high": 22.3799,
      "low": 22.3602,
      "close": 22.3645,
      "volume": 9507,
      "datetime": 1736974140000
    },
    {
      "open": 22.37,
      "high": 22.38,
      "low": 22.37,
      "close": 22.375,
      "volume": 2628,
      "datetime": 1736974200000
    },
    {
      "open": 22.3601,
      "high": 22.3657,
      "low": 22.351,
      "close": 22.351,
      "volume": 1386,
      "datetime": 1736974260000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.33,
      "close": 22.3324,
      "volume": 4771,
      "datetime": 1736974320000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.3203,
      "close": 22.33,
      "volume": 3650,
      "datetime": 1736974380000
    },
    {
      "open": 22.32,
      "high": 22.34,
      "low": 22.32,
      "close": 22.33,
      "volume": 6943,
      "datetime": 1736974440000
    },
    {
      "open": 22.34,
      "high": 22.37,
      "low": 22.3397,
      "close": 22.36,
      "volume": 10131,
      "datetime": 1736974500000
    },
    {
      "open": 22.36,
      "high": 22.3628,
      "low": 22.36,
      "close": 22.3628,
      "volume": 2360,
      "datetime": 1736974560000
    },
    {
      "open": 22.38,
      "high": 22.3999,
      "low": 22.38,
      "close": 22.395,
      "volume": 9529,
      "datetime": 1736974620000
    },
    {
      "open": 22.395,
      "high": 22.4,
      "low": 22.39,
      "close": 22.4,
      "volume": 33291,
      "datetime": 1736974680000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.32,
      "close": 22.355,
      "volume": 41260,
      "datetime": 1736974740000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.36,
      "close": 22.36,
      "volume": 3458,
      "datetime": 1736974800000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.34,
      "close": 22.34,
      "volume": 100,
      "datetime": 1736974920000
    },
    {
      "open": 22.3799,
      "high": 22.3799,
      "low": 22.3799,
      "close": 22.3799,
      "volume": 100,
      "datetime": 1736975040000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 560,
      "datetime": 1736975340000
    },
    {
      "open": 22.3001,
      "high": 22.3012,
      "low": 22.3001,
      "close": 22.3012,
      "volume": 4640,
      "datetime": 1736976000000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 100,
      "datetime": 1736976240000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.36,
      "close": 22.36,
      "volume": 250,
      "datetime": 1736976360000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.32,
      "close": 22.32,
      "volume": 700,
      "datetime": 1736976600000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 100,
      "datetime": 1736976720000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.3201,
      "close": 22.3201,
      "volume": 200,
      "datetime": 1736977020000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.33,
      "close": 22.33,
      "volume": 220,
      "datetime": 1736977320000
    },
    {
      "open": 22.32,
      "high": 22.36,
      "low": 22.32,
      "close": 22.36,
      "volume": 4600,
      "datetime": 1736977380000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 100,
      "datetime": 1736978040000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 110,
      "datetime": 1736978160000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.34,
      "close": 22.34,
      "volume": 750,
      "datetime": 1736979420000
    },
    {
      "open": 22.3782,
      "high": 22.3782,
      "low": 22.3782,
      "close": 22.3782,
      "volume": 100,
      "datetime": 1736980380000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 133,
      "datetime": 1736981580000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 100,
      "datetime": 1736981700000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 200,
      "datetime": 1736981940000
    },
    {
      "open": 22.29,
      "high": 22.29,
      "low": 22.29,
      "close": 22.29,
      "volume": 200,
      "datetime": 1736982480000
    },
    {
      "open": 22.3002,
      "high": 22.3002,
      "low": 22.3002,
      "close": 22.3002,
      "volume": 1299,
      "datetime": 1736982600000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 277,
      "datetime": 1736983080000
    },
    {
      "open": 22.23,
      "high": 22.23,
      "low": 22.23,
      "close": 22.23,
      "volume": 4000,
      "datetime": 1736983980000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.17,
      "close": 22.17,
      "volume": 1500,
      "datetime": 1736984460000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.16,
      "close": 22.16,
      "volume": 3676,
      "datetime": 1736984580000
    },
    {
      "open": 22.1704,
      "high": 22.1704,
      "low": 22.1704,
      "close": 22.1704,
      "volume": 120,
      "datetime": 1736984700000
    },
    {
      "open": 22.21,
      "high": 22.21,
      "low": 22.21,
      "close": 22.21,
      "volume": 200,
      "datetime": 1736985120000
    },
    {
      "open": 22.155,
      "high": 22.155,
      "low": 22.155,
      "close": 22.155,
      "volume": 144,
      "datetime": 1736985480000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.14,
      "close": 22.14,
      "volume": 350,
      "datetime": 1736985600000
    },
    {
      "open": 22.14,
      "high": 22.14,
      "low": 22.14,
      "close": 22.14,
      "volume": 100,
      "datetime": 1736985660000
    },
    {
      "open": 22.06,
      "high": 22.09,
      "low": 22.06,
      "close": 22.09,
      "volume": 300,
      "datetime": 1736985720000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.17,
      "close": 22.17,
      "volume": 500,
      "datetime": 1736985840000
    },
    {
      "open": 22.119,
      "high": 22.119,
      "low": 22.119,
      "close": 22.119,
      "volume": 1000,
      "datetime": 1736985900000
    },
    {
      "open": 22.19,
      "high": 22.19,
      "low": 22.19,
      "close": 22.19,
      "volume": 500,
      "datetime": 1736986320000
    },
    {
      "open": 22.23,
      "high": 22.23,
      "low": 22.23,
      "close": 22.23,
      "volume": 100,
      "datetime": 1736986620000
    },
    {
      "open": 22.2,
      "high": 22.2,
      "low": 22.2,
      "close": 22.2,
      "volume": 100,
      "datetime": 1736986740000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.15,
      "close": 22.15,
      "volume": 240,
      "datetime": 1736987280000
    },
    {
      "open": 22.22,
      "high": 22.22,
      "low": 22.22,
      "close": 22.22,
      "volume": 350,
      "datetime": 1736987700000
    },
    {
      "open": 22.23,
      "high": 22.23,
      "low": 22.23,
      "close": 22.23,
      "volume": 125,
      "datetime": 1736987760000
    },
    {
      "open": 22.32,
      "high": 22.36,
      "low": 22.32,
      "close": 22.36,
      "volume": 300,
      "datetime": 1736988360000
    },
    {
      "open": 22.31,
      "high": 22.31,
      "low": 22.31,
      "close": 22.31,
      "volume": 100,
      "datetime": 1736988480000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.3199,
      "close": 22.3199,
      "volume": 200,
      "datetime": 1736989140000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 3,
      "datetime": 1736989320000
    },
    {
      "open": 22.23,
      "high": 22.23,
      "low": 22.23,
      "close": 22.23,
      "volume": 101,
      "datetime": 1736989560000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 233,
      "datetime": 1736989980000
    },
    {
      "open": 22.31,
      "high": 22.31,
      "low": 22.31,
      "close": 22.31,
      "volume": 4,
      "datetime": 1736990460000
    },
    {
      "open": 22.31,
      "high": 22.31,
      "low": 22.31,
      "close": 22.31,
      "volume": 4,
      "datetime": 1736990520000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 7,
      "datetime": 1736990640000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 20,
      "datetime": 1736991180000
    },
    {
      "open": 22.22,
      "high": 22.22,
      "low": 22.22,
      "close": 22.22,
      "volume": 10,
      "datetime": 1736991300000
    },
    {
      "open": 22.22,
      "high": 22.22,
      "low": 22.22,
      "close": 22.22,
      "volume": 50,
      "datetime": 1736991900000
    },
    {
      "open": 22.25,
      "high": 22.25,
      "low": 22.25,
      "close": 22.25,
      "volume": 1,
      "datetime": 1736991960000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 244,
      "datetime": 1736994660000
    },
    {
      "open": 22.31,
      "high": 22.32,
      "low": 22.31,
      "close": 22.32,
      "volume": 100,
      "datetime": 1736994900000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.33,
      "close": 22.33,
      "volume": 50,
      "datetime": 1736995260000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.32,
      "close": 22.32,
      "volume": 1050,
      "datetime": 1736996580000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 50,
      "datetime": 1736996880000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 1,
      "datetime": 1736997000000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.33,
      "close": 22.33,
      "volume": 1,
      "datetime": 1736997240000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.37,
      "close": 22.37,
      "volume": 3125,
      "datetime": 1736997600000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.38,
      "close": 22.38,
      "volume": 10,
      "datetime": 1736998260000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 1,
      "datetime": 1736998380000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.39,
      "close": 22.39,
      "volume": 50,
      "datetime": 1736998440000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 50,
      "datetime": 1736998560000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 2,
      "datetime": 1736998740000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 99,
      "datetime": 1736999400000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 4360,
      "datetime": 1737000120000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.38,
      "close": 22.38,
      "volume": 100,
      "datetime": 1737000300000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.38,
      "close": 22.38,
      "volume": 900,
      "datetime": 1737000360000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 100,
      "datetime": 1737000600000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.36,
      "close": 22.36,
      "volume": 100,
      "datetime": 1737001440000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 2,
      "datetime": 1737002580000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.37,
      "close": 22.37,
      "volume": 150,
      "datetime": 1737004740000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.37,
      "close": 22.37,
      "volume": 6,
      "datetime": 1737005940000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.38,
      "close": 22.38,
      "volume": 45,
      "datetime": 1737006000000
    },
    {
      "open": 22.39,
      "high": 22.41,
      "low": 22.39,
      "close": 22.41,
      "volume": 101,
      "datetime": 1737006480000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 1,
      "datetime": 1737006540000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 101,
      "datetime": 1737007560000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.33,
      "close": 22.33,
      "volume": 200,
      "datetime": 1737009000000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 25,
      "datetime": 1737009060000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 244,
      "datetime": 1737009600000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.29,
      "close": 22.29,
      "volume": 200,
      "datetime": 1737011580000
    },
    {
      "open": 22.29,
      "high": 22.29,
      "low": 22.29,
      "close": 22.29,
      "volume": 50,
      "datetime": 1737011640000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.34,
      "close": 22.34,
      "volume": 20,
      "datetime": 1737013620000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.47,
      "close": 22.47,
      "volume": 50,
      "datetime": 1737017040000
    },
    {
      "open": 22.5,
      "high": 22.51,
      "low": 22.5,
      "close": 22.51,
      "volume": 17,
      "datetime": 1737017280000
    },
    {
      "open": 22.59,
      "high": 22.59,
      "low": 22.58,
      "close": 22.58,
      "volume": 200,
      "datetime": 1737018240000
    },
    {
      "open": 22.59,
      "high": 22.59,
      "low": 22.59,
      "close": 22.59,
      "volume": 100,
      "datetime": 1737018300000
    },
    {
      "open": 22.57,
      "high": 22.57,
      "low": 22.57,
      "close": 22.57,
      "volume": 400,
      "datetime": 1737018420000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.47,
      "close": 22.47,
      "volume": 200,
      "datetime": 1737021600000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.44,
      "close": 22.44,
      "volume": 100,
      "datetime": 1737022980000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 250,
      "datetime": 1737023640000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 100,
      "datetime": 1737023760000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 200,
      "datetime": 1737023880000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 227,
      "datetime": 1737024000000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 239,
      "datetime": 1737024420000
    },
    {
      "open": 22.45,
      "high": 22.46,
      "low": 22.45,
      "close": 22.46,
      "volume": 320,
      "datetime": 1737025440000
    },
    {
      "open": 22.48,
      "high": 22.49,
      "low": 22.48,
      "close": 22.49,
      "volume": 220,
      "datetime": 1737027240000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 100,
      "datetime": 1737027600000
    },
    {
      "open": 22.47,
      "high": 22.47,
      "low": 22.47,
      "close": 22.47,
      "volume": 129,
      "datetime": 1737028140000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 300,
      "datetime": 1737028860000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 192,
      "datetime": 1737028920000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 2929,
      "datetime": 1737029100000
    },
    {
      "open": 22.52,
      "high": 22.53,
      "low": 22.52,
      "close": 22.53,
      "volume": 220,
      "datetime": 1737029160000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 778,
      "datetime": 1737029340000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 1169,
      "datetime": 1737029400000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 1250,
      "datetime": 1737031740000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 944,
      "datetime": 1737031800000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 100,
      "datetime": 1737031860000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 277,
      "datetime": 1737032220000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 550,
      "datetime": 1737032280000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 100,
      "datetime": 1737032400000
    },
    {
      "open": 22.49,
      "high": 22.49,
      "low": 22.49,
      "close": 22.49,
      "volume": 600,
      "datetime": 1737032880000
    },
    {
      "open": 22.49,
      "high": 22.49,
      "low": 22.49,
      "close": 22.49,
      "volume": 200,
      "datetime": 1737033000000
    },
    {
      "open": 22.49,
      "high": 22.49,
      "low": 22.49,
      "close": 22.49,
      "volume": 200,
      "datetime": 1737033120000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 444,
      "datetime": 1737033300000
    },
    {
      "open": 22.49,
      "high": 22.49,
      "low": 22.49,
      "close": 22.49,
      "volume": 200,
      "datetime": 1737033600000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 1000,
      "datetime": 1737033660000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 100,
      "datetime": 1737033720000
    },
    {
      "open": 22.5093,
      "high": 22.5093,
      "low": 22.5093,
      "close": 22.5093,
      "volume": 100,
      "datetime": 1737033780000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.4608,
      "close": 22.4608,
      "volume": 600,
      "datetime": 1737033840000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 100,
      "datetime": 1737034200000
    },
    {
      "open": 22.5195,
      "high": 22.5195,
      "low": 22.5195,
      "close": 22.5195,
      "volume": 100,
      "datetime": 1737034320000
    },
    {
      "open": 22.5005,
      "high": 22.5005,
      "low": 22.5005,
      "close": 22.5005,
      "volume": 100,
      "datetime": 1737034380000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 206,
      "datetime": 1737034440000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.52,
      "close": 22.52,
      "volume": 1500,
      "datetime": 1737034620000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.46,
      "close": 22.46,
      "volume": 500,
      "datetime": 1737034860000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.39,
      "close": 22.39,
      "volume": 1500,
      "datetime": 1737035040000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.4,
      "close": 22.4,
      "volume": 500,
      "datetime": 1737035100000
    },
    {
      "open": 22.4408,
      "high": 22.4408,
      "low": 22.4408,
      "close": 22.4408,
      "volume": 1000,
      "datetime": 1737035580000
    },
    {
      "open": 22.4312,
      "high": 22.4312,
      "low": 22.4312,
      "close": 22.4312,
      "volume": 100,
      "datetime": 1737035640000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 248,
      "datetime": 1737036000000
    },
    {
      "open": 22.5,
      "high": 22.52,
      "low": 22.5,
      "close": 22.52,
      "volume": 450,
      "datetime": 1737036240000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 197,
      "datetime": 1737036420000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.5,
      "close": 22.5,
      "volume": 100,
      "datetime": 1737036540000
    },
    {
      "open": 22.51,
      "high": 22.51,
      "low": 22.51,
      "close": 22.51,
      "volume": 200,
      "datetime": 1737036600000
    },
    {
      "open": 22.5,
      "high": 22.5,
      "low": 22.47,
      "close": 22.47,
      "volume": 759,
      "datetime": 1737036660000
    },
    {
      "open": 22.4693,
      "high": 22.47,
      "low": 22.4693,
      "close": 22.47,
      "volume": 250,
      "datetime": 1737036840000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.4207,
      "close": 22.4207,
      "volume": 207,
      "datetime": 1737036900000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 500,
      "datetime": 1737037020000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 330,
      "datetime": 1737037080000
    },
    {
      "open": 22.4302,
      "high": 22.4302,
      "low": 22.4302,
      "close": 22.4302,
      "volume": 100,
      "datetime": 1737037200000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.45,
      "close": 22.45,
      "volume": 100,
      "datetime": 1737037320000
    },
    {
      "open": 22.46,
      "high": 22.46,
      "low": 22.44,
      "close": 22.44,
      "volume": 667,
      "datetime": 1737037440000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 300,
      "datetime": 1737037560000
    },
    {
      "open": 22.42,
      "high": 22.48,
      "low": 22.42,
      "close": 22.48,
      "volume": 27854,
      "datetime": 1737037800000
    },
    {
      "open": 22.48,
      "high": 22.5099,
      "low": 22.4519,
      "close": 22.5,
      "volume": 15371,
      "datetime": 1737037860000
    },
    {
      "open": 22.52,
      "high": 22.52,
      "low": 22.5,
      "close": 22.5,
      "volume": 800,
      "datetime": 1737037920000
    },
    {
      "open": 22.5271,
      "high": 22.5399,
      "low": 22.5271,
      "close": 22.5399,
      "volume": 800,
      "datetime": 1737037980000
    },
    {
      "open": 22.5,
      "high": 22.5091,
      "low": 22.4892,
      "close": 22.4892,
      "volume": 13529,
      "datetime": 1737038040000
    },
    {
      "open": 22.4602,
      "high": 22.4625,
      "low": 22.45,
      "close": 22.4625,
      "volume": 1930,
      "datetime": 1737038100000
    },
    {
      "open": 22.48,
      "high": 22.48,
      "low": 22.48,
      "close": 22.48,
      "volume": 800,
      "datetime": 1737038160000
    },
    {
      "open": 22.5,
      "high": 22.5399,
      "low": 22.5,
      "close": 22.5399,
      "volume": 2096,
      "datetime": 1737038220000
    },
    {
      "open": 22.5499,
      "high": 22.5499,
      "low": 22.5,
      "close": 22.5001,
      "volume": 1615,
      "datetime": 1737038280000
    },
    {
      "open": 22.5101,
      "high": 22.5101,
      "low": 22.5,
      "close": 22.505,
      "volume": 1668,
      "datetime": 1737038340000
    },
    {
      "open": 22.51,
      "high": 22.515,
      "low": 22.5,
      "close": 22.515,
      "volume": 2371,
      "datetime": 1737038400000
    },
    {
      "open": 22.51,
      "high": 22.5569,
      "low": 22.51,
      "close": 22.5569,
      "volume": 2567,
      "datetime": 1737038460000
    },
    {
      "open": 22.56,
      "high": 22.57,
      "low": 22.56,
      "close": 22.57,
      "volume": 9683,
      "datetime": 1737038520000
    },
    {
      "open": 22.6,
      "high": 22.6635,
      "low": 22.6,
      "close": 22.6635,
      "volume": 5067,
      "datetime": 1737038580000
    },
    {
      "open": 22.67,
      "high": 22.6797,
      "low": 22.6594,
      "close": 22.6797,
      "volume": 17096,
      "datetime": 1737038640000
    },
    {
      "open": 22.685,
      "high": 22.7641,
      "low": 22.685,
      "close": 22.7567,
      "volume": 13052,
      "datetime": 1737038700000
    },
    {
      "open": 22.7601,
      "high": 22.7799,
      "low": 22.7326,
      "close": 22.755,
      "volume": 39589,
      "datetime": 1737038760000
    },
    {
      "open": 22.755,
      "high": 22.8,
      "low": 22.755,
      "close": 22.8,
      "volume": 10205,
      "datetime": 1737038820000
    },
    {
      "open": 22.8,
      "high": 22.825,
      "low": 22.7621,
      "close": 22.775,
      "volume": 11979,
      "datetime": 1737038880000
    },
    {
      "open": 22.81,
      "high": 22.8388,
      "low": 22.81,
      "close": 22.8326,
      "volume": 1344,
      "datetime": 1737038940000
    },
    {
      "open": 22.82,
      "high": 22.825,
      "low": 22.7854,
      "close": 22.8057,
      "volume": 13522,
      "datetime": 1737039000000
    },
    {
      "open": 22.81,
      "high": 22.8547,
      "low": 22.805,
      "close": 22.84,
      "volume": 6406,
      "datetime": 1737039060000
    },
    {
      "open": 22.8199,
      "high": 22.8199,
      "low": 22.7501,
      "close": 22.757,
      "volume": 20716,
      "datetime": 1737039120000
    },
    {
      "open": 22.76,
      "high": 22.7601,
      "low": 22.73,
      "close": 22.75,
      "volume": 10717,
      "datetime": 1737039180000
    },
    {
      "open": 22.795,
      "high": 22.816,
      "low": 22.795,
      "close": 22.816,
      "volume": 4100,
      "datetime": 1737039300000
    },
    {
      "open": 22.81,
      "high": 22.825,
      "low": 22.81,
      "close": 22.81,
      "volume": 5814,
      "datetime": 1737039360000
    },
    {
      "open": 22.7913,
      "high": 22.8,
      "low": 22.78,
      "close": 22.8,
      "volume": 7199,
      "datetime": 1737039420000
    },
    {
      "open": 22.81,
      "high": 22.81,
      "low": 22.8,
      "close": 22.81,
      "volume": 9436,
      "datetime": 1737039480000
    },
    {
      "open": 22.83,
      "high": 22.8445,
      "low": 22.8241,
      "close": 22.8241,
      "volume": 12796,
      "datetime": 1737039540000
    },
    {
      "open": 22.85,
      "high": 22.8855,
      "low": 22.85,
      "close": 22.8855,
      "volume": 14642,
      "datetime": 1737039600000
    },
    {
      "open": 22.89,
      "high": 22.895,
      "low": 22.87,
      "close": 22.895,
      "volume": 11836,
      "datetime": 1737039660000
    },
    {
      "open": 22.89,
      "high": 22.89,
      "low": 22.82,
      "close": 22.826,
      "volume": 6530,
      "datetime": 1737039720000
    },
    {
      "open": 22.82,
      "high": 22.82,
      "low": 22.8046,
      "close": 22.8046,
      "volume": 2050,
      "datetime": 1737039780000
    },
    {
      "open": 22.84,
      "high": 22.8543,
      "low": 22.8355,
      "close": 22.8543,
      "volume": 1662,
      "datetime": 1737039840000
    },
    {
      "open": 22.8408,
      "high": 22.875,
      "low": 22.82,
      "close": 22.82,
      "volume": 2100,
      "datetime": 1737039900000
    },
    {
      "open": 22.8102,
      "high": 22.82,
      "low": 22.77,
      "close": 22.77,
      "volume": 9982,
      "datetime": 1737039960000
    },
    {
      "open": 22.77,
      "high": 22.785,
      "low": 22.7401,
      "close": 22.7401,
      "volume": 14509,
      "datetime": 1737040020000
    },
    {
      "open": 22.74,
      "high": 22.771,
      "low": 22.731,
      "close": 22.771,
      "volume": 11575,
      "datetime": 1737040080000
    },
    {
      "open": 22.7699,
      "high": 22.7699,
      "low": 22.7101,
      "close": 22.72,
      "volume": 2095,
      "datetime": 1737040140000
    },
    {
      "open": 22.7,
      "high": 22.72,
      "low": 22.7,
      "close": 22.72,
      "volume": 3794,
      "datetime": 1737040200000
    },
    {
      "open": 22.7,
      "high": 22.7,
      "low": 22.6799,
      "close": 22.7,
      "volume": 5125,
      "datetime": 1737040260000
    },
    {
      "open": 22.71,
      "high": 22.75,
      "low": 22.7031,
      "close": 22.75,
      "volume": 5675,
      "datetime": 1737040320000
    },
    {
      "open": 22.7399,
      "high": 22.7557,
      "low": 22.73,
      "close": 22.74,
      "volume": 5750,
      "datetime": 1737040380000
    },
    {
      "open": 22.74,
      "high": 22.8,
      "low": 22.74,
      "close": 22.79,
      "volume": 2650,
      "datetime": 1737040440000
    },
    {
      "open": 22.7898,
      "high": 22.7987,
      "low": 22.7404,
      "close": 22.7404,
      "volume": 1575,
      "datetime": 1737040500000
    },
    {
      "open": 22.755,
      "high": 22.78,
      "low": 22.745,
      "close": 22.7587,
      "volume": 5673,
      "datetime": 1737040560000
    },
    {
      "open": 22.74,
      "high": 22.76,
      "low": 22.73,
      "close": 22.76,
      "volume": 6567,
      "datetime": 1737040620000
    },
    {
      "open": 22.75,
      "high": 22.75,
      "low": 22.75,
      "close": 22.75,
      "volume": 450,
      "datetime": 1737040680000
    },
    {
      "open": 22.71,
      "high": 22.74,
      "low": 22.71,
      "close": 22.72,
      "volume": 2158,
      "datetime": 1737040740000
    },
    {
      "open": 22.72,
      "high": 22.72,
      "low": 22.705,
      "close": 22.705,
      "volume": 1165,
      "datetime": 1737040800000
    },
    {
      "open": 22.69,
      "high": 22.7,
      "low": 22.67,
      "close": 22.6855,
      "volume": 14146,
      "datetime": 1737040860000
    },
    {
      "open": 22.67,
      "high": 22.6997,
      "low": 22.65,
      "close": 22.6997,
      "volume": 5697,
      "datetime": 1737040920000
    },
    {
      "open": 22.6901,
      "high": 22.72,
      "low": 22.6901,
      "close": 22.6966,
      "volume": 2950,
      "datetime": 1737040980000
    },
    {
      "open": 22.6871,
      "high": 22.6871,
      "low": 22.6513,
      "close": 22.6513,
      "volume": 7620,
      "datetime": 1737041040000
    },
    {
      "open": 22.65,
      "high": 22.67,
      "low": 22.65,
      "close": 22.67,
      "volume": 10800,
      "datetime": 1737041100000
    },
    {
      "open": 22.6701,
      "high": 22.6701,
      "low": 22.659,
      "close": 22.659,
      "volume": 400,
      "datetime": 1737041160000
    },
    {
      "open": 22.65,
      "high": 22.6668,
      "low": 22.65,
      "close": 22.6668,
      "volume": 800,
      "datetime": 1737041220000
    },
    {
      "open": 22.64,
      "high": 22.6498,
      "low": 22.6346,
      "close": 22.6498,
      "volume": 11045,
      "datetime": 1737041280000
    },
    {
      "open": 22.635,
      "high": 22.65,
      "low": 22.635,
      "close": 22.64,
      "volume": 2166,
      "datetime": 1737041340000
    },
    {
      "open": 22.64,
      "high": 22.6699,
      "low": 22.62,
      "close": 22.62,
      "volume": 903,
      "datetime": 1737041400000
    },
    {
      "open": 22.67,
      "high": 22.6799,
      "low": 22.67,
      "close": 22.6797,
      "volume": 4255,
      "datetime": 1737041460000
    },
    {
      "open": 22.65,
      "high": 22.66,
      "low": 22.65,
      "close": 22.66,
      "volume": 1375,
      "datetime": 1737041520000
    },
    {
      "open": 22.65,
      "high": 22.65,
      "low": 22.62,
      "close": 22.64,
      "volume": 3864,
      "datetime": 1737041580000
    },
    {
      "open": 22.66,
      "high": 22.68,
      "low": 22.66,
      "close": 22.67,
      "volume": 1800,
      "datetime": 1737041640000
    },
    {
      "open": 22.66,
      "high": 22.6868,
      "low": 22.66,
      "close": 22.6868,
      "volume": 825,
      "datetime": 1737041700000
    },
    {
      "open": 22.7,
      "high": 22.717,
      "low": 22.7,
      "close": 22.717,
      "volume": 3425,
      "datetime": 1737041760000
    },
    {
      "open": 22.72,
      "high": 22.7245,
      "low": 22.67,
      "close": 22.67,
      "volume": 5849,
      "datetime": 1737041820000
    },
    {
      "open": 22.67,
      "high": 22.67,
      "low": 22.645,
      "close": 22.645,
      "volume": 1710,
      "datetime": 1737041880000
    },
    {
      "open": 22.62,
      "high": 22.6301,
      "low": 22.62,
      "close": 22.6301,
      "volume": 650,
      "datetime": 1737041940000
    },
    {
      "open": 22.64,
      "high": 22.68,
      "low": 22.64,
      "close": 22.68,
      "volume": 1525,
      "datetime": 1737042000000
    },
    {
      "open": 22.68,
      "high": 22.7,
      "low": 22.68,
      "close": 22.7,
      "volume": 900,
      "datetime": 1737042060000
    },
    {
      "open": 22.7045,
      "high": 22.71,
      "low": 22.697,
      "close": 22.71,
      "volume": 7809,
      "datetime": 1737042120000
    },
    {
      "open": 22.705,
      "high": 22.708,
      "low": 22.69,
      "close": 22.69,
      "volume": 1125,
      "datetime": 1737042180000
    },
    {
      "open": 22.66,
      "high": 22.66,
      "low": 22.65,
      "close": 22.66,
      "volume": 3025,
      "datetime": 1737042240000
    },
    {
      "open": 22.665,
      "high": 22.68,
      "low": 22.6557,
      "close": 22.68,
      "volume": 5797,
      "datetime": 1737042300000
    },
    {
      "open": 22.68,
      "high": 22.68,
      "low": 22.6657,
      "close": 22.67,
      "volume": 1730,
      "datetime": 1737042360000
    },
    {
      "open": 22.66,
      "high": 22.67,
      "low": 22.66,
      "close": 22.67,
      "volume": 500,
      "datetime": 1737042420000
    },
    {
      "open": 22.66,
      "high": 22.6899,
      "low": 22.66,
      "close": 22.68,
      "volume": 850,
      "datetime": 1737042480000
    },
    {
      "open": 22.62,
      "high": 22.62,
      "low": 22.62,
      "close": 22.62,
      "volume": 200,
      "datetime": 1737042540000
    },
    {
      "open": 22.6,
      "high": 22.61,
      "low": 22.58,
      "close": 22.58,
      "volume": 9375,
      "datetime": 1737042600000
    },
    {
      "open": 22.56,
      "high": 22.56,
      "low": 22.54,
      "close": 22.555,
      "volume": 10514,
      "datetime": 1737042660000
    },
    {
      "open": 22.56,
      "high": 22.56,
      "low": 22.534901,
      "close": 22.545,
      "volume": 3723,
      "datetime": 1737042720000
    },
    {
      "open": 22.56,
      "high": 22.56,
      "low": 22.55,
      "close": 22.55,
      "volume": 1077,
      "datetime": 1737042780000
    },
    {
      "open": 22.56,
      "high": 22.56,
      "low": 22.5431,
      "close": 22.5431,
      "volume": 3374,
      "datetime": 1737042840000
    },
    {
      "open": 22.5462,
      "high": 22.5462,
      "low": 22.545,
      "close": 22.545,
      "volume": 943,
      "datetime": 1737042900000
    },
    {
      "open": 22.54,
      "high": 22.54,
      "low": 22.54,
      "close": 22.54,
      "volume": 1402,
      "datetime": 1737042960000
    },
    {
      "open": 22.51,
      "high": 22.515,
      "low": 22.49,
      "close": 22.495,
      "volume": 5218,
      "datetime": 1737043020000
    },
    {
      "open": 22.495,
      "high": 22.5,
      "low": 22.4704,
      "close": 22.4704,
      "volume": 4517,
      "datetime": 1737043080000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.43,
      "close": 22.43,
      "volume": 3113,
      "datetime": 1737043140000
    },
    {
      "open": 22.435,
      "high": 22.44,
      "low": 22.42,
      "close": 22.44,
      "volume": 22114,
      "datetime": 1737043200000
    },
    {
      "open": 22.4345,
      "high": 22.435,
      "low": 22.39,
      "close": 22.405,
      "volume": 15325,
      "datetime": 1737043260000
    },
    {
      "open": 22.41,
      "high": 22.43,
      "low": 22.41,
      "close": 22.43,
      "volume": 4455,
      "datetime": 1737043320000
    },
    {
      "open": 22.43,
      "high": 22.44,
      "low": 22.411,
      "close": 22.4199,
      "volume": 1801,
      "datetime": 1737043380000
    },
    {
      "open": 22.3926,
      "high": 22.395,
      "low": 22.3813,
      "close": 22.3813,
      "volume": 2856,
      "datetime": 1737043440000
    },
    {
      "open": 22.38,
      "high": 22.4,
      "low": 22.38,
      "close": 22.4,
      "volume": 1680,
      "datetime": 1737043500000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.3245,
      "close": 22.3245,
      "volume": 4319,
      "datetime": 1737043560000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 119,
      "datetime": 1737043620000
    },
    {
      "open": 22.325,
      "high": 22.325,
      "low": 22.3097,
      "close": 22.31,
      "volume": 12750,
      "datetime": 1737043680000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.32,
      "close": 22.32,
      "volume": 1777,
      "datetime": 1737043740000
    },
    {
      "open": 22.35,
      "high": 22.365,
      "low": 22.35,
      "close": 22.35,
      "volume": 1650,
      "datetime": 1737043800000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.35,
      "close": 22.35,
      "volume": 2052,
      "datetime": 1737043860000
    },
    {
      "open": 22.35,
      "high": 22.355,
      "low": 22.34,
      "close": 22.355,
      "volume": 1968,
      "datetime": 1737043920000
    },
    {
      "open": 22.35,
      "high": 22.365,
      "low": 22.35,
      "close": 22.365,
      "volume": 930,
      "datetime": 1737043980000
    },
    {
      "open": 22.38,
      "high": 22.4,
      "low": 22.38,
      "close": 22.4,
      "volume": 4075,
      "datetime": 1737044040000
    },
    {
      "open": 22.41,
      "high": 22.4199,
      "low": 22.3972,
      "close": 22.3972,
      "volume": 4303,
      "datetime": 1737044100000
    },
    {
      "open": 22.4193,
      "high": 22.43,
      "low": 22.4193,
      "close": 22.43,
      "volume": 4322,
      "datetime": 1737044160000
    },
    {
      "open": 22.445,
      "high": 22.47,
      "low": 22.445,
      "close": 22.47,
      "volume": 1651,
      "datetime": 1737044220000
    },
    {
      "open": 22.4601,
      "high": 22.4601,
      "low": 22.43,
      "close": 22.43,
      "volume": 2195,
      "datetime": 1737044280000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.4,
      "close": 22.4,
      "volume": 3013,
      "datetime": 1737044340000
    },
    {
      "open": 22.4,
      "high": 22.44,
      "low": 22.4,
      "close": 22.44,
      "volume": 4614,
      "datetime": 1737044400000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.41,
      "close": 22.42,
      "volume": 7319,
      "datetime": 1737044460000
    },
    {
      "open": 22.3971,
      "high": 22.405,
      "low": 22.3971,
      "close": 22.405,
      "volume": 980,
      "datetime": 1737044520000
    },
    {
      "open": 22.3922,
      "high": 22.395,
      "low": 22.39,
      "close": 22.39,
      "volume": 600,
      "datetime": 1737044580000
    },
    {
      "open": 22.37,
      "high": 22.38,
      "low": 22.37,
      "close": 22.3701,
      "volume": 2150,
      "datetime": 1737044640000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.37,
      "close": 22.37,
      "volume": 873,
      "datetime": 1737044700000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.3337,
      "close": 22.34,
      "volume": 1314,
      "datetime": 1737044760000
    },
    {
      "open": 22.3379,
      "high": 22.3498,
      "low": 22.33,
      "close": 22.34,
      "volume": 3967,
      "datetime": 1737044820000
    },
    {
      "open": 22.3358,
      "high": 22.3358,
      "low": 22.33,
      "close": 22.33,
      "volume": 1499,
      "datetime": 1737044880000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.33,
      "close": 22.33,
      "volume": 1825,
      "datetime": 1737044940000
    },
    {
      "open": 22.325,
      "high": 22.33,
      "low": 22.325,
      "close": 22.33,
      "volume": 623,
      "datetime": 1737045000000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.3233,
      "close": 22.3233,
      "volume": 625,
      "datetime": 1737045060000
    },
    {
      "open": 22.32,
      "high": 22.34,
      "low": 22.32,
      "close": 22.33771,
      "volume": 2790,
      "datetime": 1737045120000
    },
    {
      "open": 22.3199,
      "high": 22.33,
      "low": 22.3199,
      "close": 22.33,
      "volume": 2251,
      "datetime": 1737045240000
    },
    {
      "open": 22.335,
      "high": 22.37,
      "low": 22.335,
      "close": 22.365,
      "volume": 1350,
      "datetime": 1737045300000
    },
    {
      "open": 22.3599,
      "high": 22.3599,
      "low": 22.33,
      "close": 22.35,
      "volume": 2472,
      "datetime": 1737045360000
    },
    {
      "open": 22.305,
      "high": 22.305,
      "low": 22.29,
      "close": 22.3,
      "volume": 1278,
      "datetime": 1737045420000
    },
    {
      "open": 22.31,
      "high": 22.36,
      "low": 22.31,
      "close": 22.3598,
      "volume": 3864,
      "datetime": 1737045480000
    },
    {
      "open": 22.365,
      "high": 22.375,
      "low": 22.365,
      "close": 22.375,
      "volume": 700,
      "datetime": 1737045540000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.34,
      "close": 22.34,
      "volume": 2341,
      "datetime": 1737045600000
    },
    {
      "open": 22.34,
      "high": 22.39,
      "low": 22.3399,
      "close": 22.39,
      "volume": 3949,
      "datetime": 1737045660000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 1432,
      "datetime": 1737045720000
    },
    {
      "open": 22.42,
      "high": 22.4399,
      "low": 22.41,
      "close": 22.4399,
      "volume": 2325,
      "datetime": 1737045780000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.4199,
      "close": 22.42,
      "volume": 1325,
      "datetime": 1737045840000
    },
    {
      "open": 22.41,
      "high": 22.4167,
      "low": 22.41,
      "close": 22.41,
      "volume": 1050,
      "datetime": 1737045900000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.3854,
      "close": 22.3854,
      "volume": 1748,
      "datetime": 1737045960000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.38,
      "close": 22.38,
      "volume": 800,
      "datetime": 1737046020000
    },
    {
      "open": 22.41,
      "high": 22.435,
      "low": 22.3987,
      "close": 22.43,
      "volume": 11434,
      "datetime": 1737046080000
    },
    {
      "open": 22.425,
      "high": 22.43,
      "low": 22.425,
      "close": 22.43,
      "volume": 200,
      "datetime": 1737046140000
    },
    {
      "open": 22.425,
      "high": 22.43,
      "low": 22.425,
      "close": 22.43,
      "volume": 2379,
      "datetime": 1737046200000
    },
    {
      "open": 22.45,
      "high": 22.46,
      "low": 22.4157,
      "close": 22.4157,
      "volume": 2853,
      "datetime": 1737046260000
    },
    {
      "open": 22.4193,
      "high": 22.42,
      "low": 22.4045,
      "close": 22.41,
      "volume": 1550,
      "datetime": 1737046320000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.38,
      "close": 22.38,
      "volume": 8242,
      "datetime": 1737046380000
    },
    {
      "open": 22.405,
      "high": 22.405,
      "low": 22.405,
      "close": 22.405,
      "volume": 350,
      "datetime": 1737046440000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 800,
      "datetime": 1737046500000
    },
    {
      "open": 22.43,
      "high": 22.435,
      "low": 22.43,
      "close": 22.435,
      "volume": 1150,
      "datetime": 1737046560000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.43,
      "close": 22.43,
      "volume": 875,
      "datetime": 1737046620000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.42,
      "close": 22.42,
      "volume": 3057,
      "datetime": 1737046680000
    },
    {
      "open": 22.4037,
      "high": 22.41,
      "low": 22.4037,
      "close": 22.41,
      "volume": 1258,
      "datetime": 1737046740000
    },
    {
      "open": 22.42,
      "high": 22.445,
      "low": 22.42,
      "close": 22.44,
      "volume": 5042,
      "datetime": 1737046800000
    },
    {
      "open": 22.445,
      "high": 22.45,
      "low": 22.42,
      "close": 22.42,
      "volume": 2475,
      "datetime": 1737046860000
    },
    {
      "open": 22.4,
      "high": 22.42,
      "low": 22.4,
      "close": 22.42,
      "volume": 3950,
      "datetime": 1737046980000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.3803,
      "close": 22.3803,
      "volume": 2025,
      "datetime": 1737047040000
    },
    {
      "open": 22.3734,
      "high": 22.425,
      "low": 22.3734,
      "close": 22.425,
      "volume": 9434,
      "datetime": 1737047100000
    },
    {
      "open": 22.42,
      "high": 22.44,
      "low": 22.42,
      "close": 22.43,
      "volume": 5258,
      "datetime": 1737047160000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 400,
      "datetime": 1737047340000
    },
    {
      "open": 22.42,
      "high": 22.4201,
      "low": 22.42,
      "close": 22.42,
      "volume": 2454,
      "datetime": 1737047400000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.41,
      "close": 22.417,
      "volume": 2215,
      "datetime": 1737047460000
    },
    {
      "open": 22.4,
      "high": 22.4019,
      "low": 22.4,
      "close": 22.4,
      "volume": 2602,
      "datetime": 1737047520000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.39,
      "close": 22.39,
      "volume": 100,
      "datetime": 1737047640000
    },
    {
      "open": 22.42,
      "high": 22.43,
      "low": 22.42,
      "close": 22.43,
      "volume": 2300,
      "datetime": 1737047700000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.41,
      "close": 22.42,
      "volume": 4403,
      "datetime": 1737047760000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.41,
      "close": 22.41,
      "volume": 1450,
      "datetime": 1737047820000
    },
    {
      "open": 22.41,
      "high": 22.42,
      "low": 22.3945,
      "close": 22.3945,
      "volume": 2275,
      "datetime": 1737047880000
    },
    {
      "open": 22.385,
      "high": 22.4,
      "low": 22.385,
      "close": 22.4,
      "volume": 1489,
      "datetime": 1737047940000
    },
    {
      "open": 22.42,
      "high": 22.425,
      "low": 22.42,
      "close": 22.425,
      "volume": 813,
      "datetime": 1737048000000
    },
    {
      "open": 22.415,
      "high": 22.43,
      "low": 22.415,
      "close": 22.43,
      "volume": 2161,
      "datetime": 1737048060000
    },
    {
      "open": 22.445,
      "high": 22.445,
      "low": 22.4,
      "close": 22.4,
      "volume": 2501,
      "datetime": 1737048180000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.38,
      "close": 22.385,
      "volume": 620,
      "datetime": 1737048240000
    },
    {
      "open": 22.381,
      "high": 22.381,
      "low": 22.381,
      "close": 22.381,
      "volume": 200,
      "datetime": 1737048300000
    },
    {
      "open": 22.355,
      "high": 22.355,
      "low": 22.3502,
      "close": 22.3502,
      "volume": 200,
      "datetime": 1737048360000
    },
    {
      "open": 22.3567,
      "high": 22.3567,
      "low": 22.33,
      "close": 22.33,
      "volume": 4223,
      "datetime": 1737048420000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.32,
      "close": 22.32,
      "volume": 873,
      "datetime": 1737048480000
    },
    {
      "open": 22.31,
      "high": 22.315,
      "low": 22.3,
      "close": 22.3,
      "volume": 4252,
      "datetime": 1737048540000
    },
    {
      "open": 22.29,
      "high": 22.2987,
      "low": 22.2713,
      "close": 22.2957,
      "volume": 1798,
      "datetime": 1737048600000
    },
    {
      "open": 22.3,
      "high": 22.31,
      "low": 22.295,
      "close": 22.295,
      "volume": 1652,
      "datetime": 1737048660000
    },
    {
      "open": 22.28,
      "high": 22.28,
      "low": 22.2798,
      "close": 22.2798,
      "volume": 1013,
      "datetime": 1737048720000
    },
    {
      "open": 22.28,
      "high": 22.28,
      "low": 22.27,
      "close": 22.27,
      "volume": 1759,
      "datetime": 1737048780000
    },
    {
      "open": 22.2622,
      "high": 22.265,
      "low": 22.2301,
      "close": 22.24,
      "volume": 1552,
      "datetime": 1737048840000
    },
    {
      "open": 22.24,
      "high": 22.25,
      "low": 22.2203,
      "close": 22.2203,
      "volume": 1850,
      "datetime": 1737048900000
    },
    {
      "open": 22.2206,
      "high": 22.2206,
      "low": 22.1803,
      "close": 22.1889,
      "volume": 6100,
      "datetime": 1737048960000
    },
    {
      "open": 22.1857,
      "high": 22.19,
      "low": 22.185,
      "close": 22.1855,
      "volume": 3200,
      "datetime": 1737049020000
    },
    {
      "open": 22.18,
      "high": 22.19,
      "low": 22.18,
      "close": 22.19,
      "volume": 4891,
      "datetime": 1737049080000
    },
    {
      "open": 22.1884,
      "high": 22.24,
      "low": 22.1884,
      "close": 22.24,
      "volume": 9695,
      "datetime": 1737049140000
    },
    {
      "open": 22.28,
      "high": 22.28,
      "low": 22.24,
      "close": 22.24,
      "volume": 929,
      "datetime": 1737049200000
    },
    {
      "open": 22.26,
      "high": 22.26,
      "low": 22.2399,
      "close": 22.2399,
      "volume": 600,
      "datetime": 1737049260000
    },
    {
      "open": 22.22,
      "high": 22.25,
      "low": 22.22,
      "close": 22.25,
      "volume": 1114,
      "datetime": 1737049320000
    },
    {
      "open": 22.2599,
      "high": 22.2599,
      "low": 22.2599,
      "close": 22.2599,
      "volume": 100,
      "datetime": 1737049380000
    },
    {
      "open": 22.26,
      "high": 22.28,
      "low": 22.26,
      "close": 22.2643,
      "volume": 2700,
      "datetime": 1737049440000
    },
    {
      "open": 22.27,
      "high": 22.27,
      "low": 22.2499,
      "close": 22.26,
      "volume": 2399,
      "datetime": 1737049500000
    },
    {
      "open": 22.27,
      "high": 22.28,
      "low": 22.27,
      "close": 22.28,
      "volume": 583,
      "datetime": 1737049560000
    },
    {
      "open": 22.28,
      "high": 22.3,
      "low": 22.28,
      "close": 22.3,
      "volume": 987,
      "datetime": 1737049620000
    },
    {
      "open": 22.31,
      "high": 22.33,
      "low": 22.31,
      "close": 22.3245,
      "volume": 2734,
      "datetime": 1737049680000
    },
    {
      "open": 22.31,
      "high": 22.31,
      "low": 22.305,
      "close": 22.305,
      "volume": 1810,
      "datetime": 1737049740000
    },
    {
      "open": 22.2955,
      "high": 22.32,
      "low": 22.29,
      "close": 22.32,
      "volume": 2500,
      "datetime": 1737049800000
    },
    {
      "open": 22.32,
      "high": 22.33,
      "low": 22.32,
      "close": 22.32,
      "volume": 2950,
      "datetime": 1737049860000
    },
    {
      "open": 22.325,
      "high": 22.325,
      "low": 22.325,
      "close": 22.325,
      "volume": 160,
      "datetime": 1737049920000
    },
    {
      "open": 22.31,
      "high": 22.31,
      "low": 22.29,
      "close": 22.29,
      "volume": 2566,
      "datetime": 1737049980000
    },
    {
      "open": 22.29,
      "high": 22.29,
      "low": 22.29,
      "close": 22.29,
      "volume": 807,
      "datetime": 1737050040000
    },
    {
      "open": 22.28,
      "high": 22.2811,
      "low": 22.28,
      "close": 22.2811,
      "volume": 925,
      "datetime": 1737050100000
    },
    {
      "open": 22.275,
      "high": 22.275,
      "low": 22.2571,
      "close": 22.2571,
      "volume": 2500,
      "datetime": 1737050160000
    },
    {
      "open": 22.26,
      "high": 22.2771,
      "low": 22.26,
      "close": 22.2771,
      "volume": 1750,
      "datetime": 1737050220000
    },
    {
      "open": 22.28,
      "high": 22.29,
      "low": 22.28,
      "close": 22.29,
      "volume": 475,
      "datetime": 1737050280000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 400,
      "datetime": 1737050340000
    },
    {
      "open": 22.3168,
      "high": 22.3168,
      "low": 22.31,
      "close": 22.31,
      "volume": 475,
      "datetime": 1737050400000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.28,
      "close": 22.28,
      "volume": 1850,
      "datetime": 1737050460000
    },
    {
      "open": 22.29,
      "high": 22.3,
      "low": 22.29,
      "close": 22.3,
      "volume": 1013,
      "datetime": 1737050520000
    },
    {
      "open": 22.28,
      "high": 22.28,
      "low": 22.28,
      "close": 22.28,
      "volume": 1200,
      "datetime": 1737050580000
    },
    {
      "open": 22.27,
      "high": 22.275,
      "low": 22.27,
      "close": 22.275,
      "volume": 1250,
      "datetime": 1737050640000
    },
    {
      "open": 22.27,
      "high": 22.27,
      "low": 22.26,
      "close": 22.26,
      "volume": 800,
      "datetime": 1737050700000
    },
    {
      "open": 22.3,
      "high": 22.31,
      "low": 22.3,
      "close": 22.31,
      "volume": 1175,
      "datetime": 1737050820000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 825,
      "datetime": 1737050880000
    },
    {
      "open": 22.28,
      "high": 22.28,
      "low": 22.28,
      "close": 22.28,
      "volume": 775,
      "datetime": 1737050940000
    },
    {
      "open": 22.305,
      "high": 22.305,
      "low": 22.3,
      "close": 22.3,
      "volume": 720,
      "datetime": 1737051000000
    },
    {
      "open": 22.315,
      "high": 22.3293,
      "low": 22.315,
      "close": 22.3293,
      "volume": 900,
      "datetime": 1737051060000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.34,
      "close": 22.34,
      "volume": 775,
      "datetime": 1737051120000
    },
    {
      "open": 22.3471,
      "high": 22.3563,
      "low": 22.3471,
      "close": 22.3563,
      "volume": 2000,
      "datetime": 1737051180000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 900,
      "datetime": 1737051240000
    },
    {
      "open": 22.35,
      "high": 22.37,
      "low": 22.35,
      "close": 22.37,
      "volume": 1720,
      "datetime": 1737051300000
    },
    {
      "open": 22.38,
      "high": 22.39,
      "low": 22.38,
      "close": 22.39,
      "volume": 1579,
      "datetime": 1737051360000
    },
    {
      "open": 22.4,
      "high": 22.4087,
      "low": 22.395,
      "close": 22.4036,
      "volume": 7462,
      "datetime": 1737051420000
    },
    {
      "open": 22.4,
      "high": 22.4,
      "low": 22.395,
      "close": 22.4,
      "volume": 1572,
      "datetime": 1737051480000
    },
    {
      "open": 22.3969,
      "high": 22.4008,
      "low": 22.3969,
      "close": 22.4008,
      "volume": 915,
      "datetime": 1737051540000
    },
    {
      "open": 22.405,
      "high": 22.405,
      "low": 22.3723,
      "close": 22.3723,
      "volume": 2300,
      "datetime": 1737051600000
    },
    {
      "open": 22.3701,
      "high": 22.387,
      "low": 22.3701,
      "close": 22.387,
      "volume": 7550,
      "datetime": 1737051660000
    },
    {
      "open": 22.37,
      "high": 22.38,
      "low": 22.37,
      "close": 22.38,
      "volume": 2230,
      "datetime": 1737051720000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.37,
      "close": 22.37,
      "volume": 1330,
      "datetime": 1737051780000
    },
    {
      "open": 22.365,
      "high": 22.37,
      "low": 22.365,
      "close": 22.37,
      "volume": 1760,
      "datetime": 1737051840000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.36,
      "close": 22.36,
      "volume": 875,
      "datetime": 1737051900000
    },
    {
      "open": 22.36,
      "high": 22.365,
      "low": 22.36,
      "close": 22.365,
      "volume": 1400,
      "datetime": 1737051960000
    },
    {
      "open": 22.38,
      "high": 22.39,
      "low": 22.38,
      "close": 22.39,
      "volume": 5118,
      "datetime": 1737052020000
    },
    {
      "open": 22.39,
      "high": 22.4,
      "low": 22.39,
      "close": 22.3955,
      "volume": 3273,
      "datetime": 1737052140000
    },
    {
      "open": 22.4,
      "high": 22.41,
      "low": 22.4,
      "close": 22.4,
      "volume": 17303,
      "datetime": 1737052200000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.37,
      "close": 22.37,
      "volume": 1225,
      "datetime": 1737052260000
    },
    {
      "open": 22.38,
      "high": 22.39,
      "low": 22.38,
      "close": 22.39,
      "volume": 2225,
      "datetime": 1737052320000
    },
    {
      "open": 22.37,
      "high": 22.41,
      "low": 22.37,
      "close": 22.41,
      "volume": 1808,
      "datetime": 1737052440000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.37,
      "close": 22.37,
      "volume": 400,
      "datetime": 1737052500000
    },
    {
      "open": 22.3965,
      "high": 22.42,
      "low": 22.3965,
      "close": 22.42,
      "volume": 211,
      "datetime": 1737052560000
    },
    {
      "open": 22.44,
      "high": 22.44,
      "low": 22.43,
      "close": 22.44,
      "volume": 2967,
      "datetime": 1737052620000
    },
    {
      "open": 22.4228,
      "high": 22.45,
      "low": 22.4228,
      "close": 22.45,
      "volume": 3075,
      "datetime": 1737052680000
    },
    {
      "open": 22.445,
      "high": 22.445,
      "low": 22.43,
      "close": 22.43,
      "volume": 1191,
      "datetime": 1737052740000
    },
    {
      "open": 22.41,
      "high": 22.42,
      "low": 22.41,
      "close": 22.42,
      "volume": 1625,
      "datetime": 1737052800000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.4,
      "close": 22.4,
      "volume": 799,
      "datetime": 1737052860000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.4,
      "close": 22.41,
      "volume": 1300,
      "datetime": 1737052920000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 1145,
      "datetime": 1737052980000
    },
    {
      "open": 22.43,
      "high": 22.43,
      "low": 22.43,
      "close": 22.43,
      "volume": 800,
      "datetime": 1737053100000
    },
    {
      "open": 22.4364,
      "high": 22.4364,
      "low": 22.42,
      "close": 22.42,
      "volume": 3031,
      "datetime": 1737053160000
    },
    {
      "open": 22.445,
      "high": 22.445,
      "low": 22.44,
      "close": 22.44,
      "volume": 770,
      "datetime": 1737053220000
    },
    {
      "open": 22.44,
      "high": 22.4599,
      "low": 22.44,
      "close": 22.455,
      "volume": 1981,
      "datetime": 1737053280000
    },
    {
      "open": 22.45,
      "high": 22.45,
      "low": 22.42,
      "close": 22.42,
      "volume": 3101,
      "datetime": 1737053340000
    },
    {
      "open": 22.4102,
      "high": 22.4102,
      "low": 22.4099,
      "close": 22.41,
      "volume": 2716,
      "datetime": 1737053400000
    },
    {
      "open": 22.41,
      "high": 22.425,
      "low": 22.41,
      "close": 22.425,
      "volume": 1325,
      "datetime": 1737053460000
    },
    {
      "open": 22.42,
      "high": 22.42,
      "low": 22.4069,
      "close": 22.4069,
      "volume": 1002,
      "datetime": 1737053520000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.38,
      "close": 22.38,
      "volume": 1325,
      "datetime": 1737053580000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.36,
      "close": 22.36,
      "volume": 1000,
      "datetime": 1737053640000
    },
    {
      "open": 22.36,
      "high": 22.37,
      "low": 22.36,
      "close": 22.37,
      "volume": 7701,
      "datetime": 1737053700000
    },
    {
      "open": 22.3723,
      "high": 22.385,
      "low": 22.3723,
      "close": 22.385,
      "volume": 1646,
      "datetime": 1737053760000
    },
    {
      "open": 22.39,
      "high": 22.39,
      "low": 22.38,
      "close": 22.38,
      "volume": 1768,
      "datetime": 1737053820000
    },
    {
      "open": 22.38,
      "high": 22.38,
      "low": 22.37,
      "close": 22.37,
      "volume": 3140,
      "datetime": 1737053940000
    },
    {
      "open": 22.38,
      "high": 22.4,
      "low": 22.38,
      "close": 22.39,
      "volume": 3198,
      "datetime": 1737054000000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 800,
      "datetime": 1737054060000
    },
    {
      "open": 22.41,
      "high": 22.41,
      "low": 22.41,
      "close": 22.41,
      "volume": 425,
      "datetime": 1737054120000
    },
    {
      "open": 22.4,
      "high": 22.405,
      "low": 22.4,
      "close": 22.4,
      "volume": 12575,
      "datetime": 1737054180000
    },
    {
      "open": 22.395,
      "high": 22.4,
      "low": 22.38,
      "close": 22.38,
      "volume": 5119,
      "datetime": 1737054240000
    },
    {
      "open": 22.375,
      "high": 22.375,
      "low": 22.37,
      "close": 22.375,
      "volume": 583,
      "datetime": 1737054300000
    },
    {
      "open": 22.375,
      "high": 22.375,
      "low": 22.37,
      "close": 22.37,
      "volume": 3000,
      "datetime": 1737054360000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.3401,
      "close": 22.3401,
      "volume": 210,
      "datetime": 1737054420000
    },
    {
      "open": 22.35,
      "high": 22.36,
      "low": 22.35,
      "close": 22.36,
      "volume": 2166,
      "datetime": 1737054480000
    },
    {
      "open": 22.365,
      "high": 22.37,
      "low": 22.35,
      "close": 22.355,
      "volume": 7274,
      "datetime": 1737054600000
    },
    {
      "open": 22.355,
      "high": 22.355,
      "low": 22.34,
      "close": 22.34,
      "volume": 1900,
      "datetime": 1737054660000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.34,
      "close": 22.34,
      "volume": 1889,
      "datetime": 1737054720000
    },
    {
      "open": 22.33,
      "high": 22.335,
      "low": 22.3232,
      "close": 22.3232,
      "volume": 526,
      "datetime": 1737054780000
    },
    {
      "open": 22.33,
      "high": 22.34,
      "low": 22.33,
      "close": 22.34,
      "volume": 1950,
      "datetime": 1737054840000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.34,
      "close": 22.34,
      "volume": 850,
      "datetime": 1737054900000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.33,
      "close": 22.335,
      "volume": 2961,
      "datetime": 1737055020000
    },
    {
      "open": 22.3228,
      "high": 22.3228,
      "low": 22.315,
      "close": 22.315,
      "volume": 1250,
      "datetime": 1737055080000
    },
    {
      "open": 22.31,
      "high": 22.31,
      "low": 22.31,
      "close": 22.31,
      "volume": 1600,
      "datetime": 1737055140000
    },
    {
      "open": 22.315,
      "high": 22.315,
      "low": 22.31,
      "close": 22.31,
      "volume": 700,
      "datetime": 1737055200000
    },
    {
      "open": 22.315,
      "high": 22.315,
      "low": 22.315,
      "close": 22.315,
      "volume": 100,
      "datetime": 1737055260000
    },
    {
      "open": 22.32,
      "high": 22.37,
      "low": 22.32,
      "close": 22.37,
      "volume": 2342,
      "datetime": 1737055320000
    },
    {
      "open": 22.37,
      "high": 22.37,
      "low": 22.36,
      "close": 22.36,
      "volume": 2014,
      "datetime": 1737055380000
    },
    {
      "open": 22.3652,
      "high": 22.38,
      "low": 22.3652,
      "close": 22.37,
      "volume": 2825,
      "datetime": 1737055440000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.34,
      "close": 22.34,
      "volume": 3463,
      "datetime": 1737055500000
    },
    {
      "open": 22.33,
      "high": 22.335,
      "low": 22.33,
      "close": 22.335,
      "volume": 1250,
      "datetime": 1737055560000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.32,
      "close": 22.3201,
      "volume": 2049,
      "datetime": 1737055620000
    },
    {
      "open": 22.3297,
      "high": 22.33,
      "low": 22.32,
      "close": 22.32,
      "volume": 1233,
      "datetime": 1737055680000
    },
    {
      "open": 22.325,
      "high": 22.33,
      "low": 22.3201,
      "close": 22.33,
      "volume": 961,
      "datetime": 1737055740000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.34,
      "close": 22.34,
      "volume": 239,
      "datetime": 1737055800000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.34,
      "close": 22.34,
      "volume": 1750,
      "datetime": 1737055860000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.3499,
      "close": 22.3499,
      "volume": 200,
      "datetime": 1737055920000
    },
    {
      "open": 22.345,
      "high": 22.349,
      "low": 22.345,
      "close": 22.349,
      "volume": 250,
      "datetime": 1737055980000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.3245,
      "close": 22.325,
      "volume": 300,
      "datetime": 1737056040000
    },
    {
      "open": 22.325,
      "high": 22.33,
      "low": 22.325,
      "close": 22.325,
      "volume": 375,
      "datetime": 1737056100000
    },
    {
      "open": 22.33,
      "high": 22.335,
      "low": 22.32,
      "close": 22.32,
      "volume": 4932,
      "datetime": 1737056160000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 120,
      "datetime": 1737056220000
    },
    {
      "open": 22.285,
      "high": 22.285,
      "low": 22.27,
      "close": 22.275,
      "volume": 1135,
      "datetime": 1737056280000
    },
    {
      "open": 22.28,
      "high": 22.28,
      "low": 22.28,
      "close": 22.28,
      "volume": 10817,
      "datetime": 1737056340000
    },
    {
      "open": 22.28,
      "high": 22.2801,
      "low": 22.2755,
      "close": 22.28,
      "volume": 3721,
      "datetime": 1737056400000
    },
    {
      "open": 22.275,
      "high": 22.28,
      "low": 22.275,
      "close": 22.28,
      "volume": 364,
      "datetime": 1737056460000
    },
    {
      "open": 22.2999,
      "high": 22.3,
      "low": 22.295,
      "close": 22.3,
      "volume": 5131,
      "datetime": 1737056520000
    },
    {
      "open": 22.29,
      "high": 22.29,
      "low": 22.29,
      "close": 22.29,
      "volume": 420,
      "datetime": 1737056580000
    },
    {
      "open": 22.27,
      "high": 22.2707,
      "low": 22.2699,
      "close": 22.2707,
      "volume": 9126,
      "datetime": 1737056640000
    },
    {
      "open": 22.255,
      "high": 22.255,
      "low": 22.255,
      "close": 22.255,
      "volume": 160,
      "datetime": 1737056760000
    },
    {
      "open": 22.25,
      "high": 22.25,
      "low": 22.25,
      "close": 22.25,
      "volume": 300,
      "datetime": 1737056820000
    },
    {
      "open": 22.2499,
      "high": 22.2499,
      "low": 22.21,
      "close": 22.21,
      "volume": 8884,
      "datetime": 1737056880000
    },
    {
      "open": 22.2042,
      "high": 22.21,
      "low": 22.2023,
      "close": 22.21,
      "volume": 1450,
      "datetime": 1737056940000
    },
    {
      "open": 22.2045,
      "high": 22.2365,
      "low": 22.2045,
      "close": 22.2365,
      "volume": 1875,
      "datetime": 1737057000000
    },
    {
      "open": 22.24,
      "high": 22.25,
      "low": 22.24,
      "close": 22.25,
      "volume": 1175,
      "datetime": 1737057060000
    },
    {
      "open": 22.26,
      "high": 22.26,
      "low": 22.24,
      "close": 22.24,
      "volume": 5981,
      "datetime": 1737057120000
    },
    {
      "open": 22.23,
      "high": 22.23,
      "low": 22.2299,
      "close": 22.2299,
      "volume": 700,
      "datetime": 1737057180000
    },
    {
      "open": 22.225,
      "high": 22.23,
      "low": 22.225,
      "close": 22.2299,
      "volume": 300,
      "datetime": 1737057240000
    },
    {
      "open": 22.225,
      "high": 22.225,
      "low": 22.2165,
      "close": 22.2165,
      "volume": 2030,
      "datetime": 1737057300000
    },
    {
      "open": 22.21,
      "high": 22.21,
      "low": 22.2,
      "close": 22.205,
      "volume": 2400,
      "datetime": 1737057360000
    },
    {
      "open": 22.2,
      "high": 22.2,
      "low": 22.195,
      "close": 22.1999,
      "volume": 2750,
      "datetime": 1737057420000
    },
    {
      "open": 22.1936,
      "high": 22.1999,
      "low": 22.18,
      "close": 22.18,
      "volume": 8567,
      "datetime": 1737057480000
    },
    {
      "open": 22.1845,
      "high": 22.1845,
      "low": 22.1715,
      "close": 22.18,
      "volume": 2900,
      "datetime": 1737057540000
    },
    {
      "open": 22.19,
      "high": 22.1912,
      "low": 22.19,
      "close": 22.1912,
      "volume": 450,
      "datetime": 1737057600000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.17,
      "close": 22.1799,
      "volume": 2003,
      "datetime": 1737057660000
    },
    {
      "open": 22.17,
      "high": 22.18,
      "low": 22.165,
      "close": 22.165,
      "volume": 5510,
      "datetime": 1737057720000
    },
    {
      "open": 22.16,
      "high": 22.16,
      "low": 22.14,
      "close": 22.14,
      "volume": 5103,
      "datetime": 1737057780000
    },
    {
      "open": 22.14,
      "high": 22.1728,
      "low": 22.14,
      "close": 22.1728,
      "volume": 4510,
      "datetime": 1737057840000
    },
    {
      "open": 22.2,
      "high": 22.2,
      "low": 22.19,
      "close": 22.19,
      "volume": 4235,
      "datetime": 1737057900000
    },
    {
      "open": 22.1999,
      "high": 22.1999,
      "low": 22.175,
      "close": 22.175,
      "volume": 2015,
      "datetime": 1737057960000
    },
    {
      "open": 22.19,
      "high": 22.2,
      "low": 22.19,
      "close": 22.2,
      "volume": 1436,
      "datetime": 1737058020000
    },
    {
      "open": 22.1901,
      "high": 22.1901,
      "low": 22.19,
      "close": 22.19,
      "volume": 625,
      "datetime": 1737058080000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.17,
      "close": 22.18,
      "volume": 6411,
      "datetime": 1737058140000
    },
    {
      "open": 22.19,
      "high": 22.2,
      "low": 22.19,
      "close": 22.195,
      "volume": 1185,
      "datetime": 1737058200000
    },
    {
      "open": 22.2,
      "high": 22.2,
      "low": 22.2,
      "close": 22.2,
      "volume": 500,
      "datetime": 1737058260000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.15,
      "close": 22.15,
      "volume": 11864,
      "datetime": 1737058320000
    },
    {
      "open": 22.15,
      "high": 22.16,
      "low": 22.15,
      "close": 22.16,
      "volume": 755,
      "datetime": 1737058380000
    },
    {
      "open": 22.175,
      "high": 22.18,
      "low": 22.175,
      "close": 22.18,
      "volume": 2154,
      "datetime": 1737058440000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.17,
      "close": 22.17,
      "volume": 1768,
      "datetime": 1737058500000
    },
    {
      "open": 22.1763,
      "high": 22.1787,
      "low": 22.17,
      "close": 22.17,
      "volume": 2652,
      "datetime": 1737058560000
    },
    {
      "open": 22.17,
      "high": 22.2,
      "low": 22.17,
      "close": 22.195,
      "volume": 3491,
      "datetime": 1737058620000
    },
    {
      "open": 22.2,
      "high": 22.21,
      "low": 22.1943,
      "close": 22.21,
      "volume": 7175,
      "datetime": 1737058680000
    },
    {
      "open": 22.21,
      "high": 22.22,
      "low": 22.205,
      "close": 22.205,
      "volume": 3785,
      "datetime": 1737058740000
    },
    {
      "open": 22.2097,
      "high": 22.21,
      "low": 22.195,
      "close": 22.195,
      "volume": 5547,
      "datetime": 1737058800000
    },
    {
      "open": 22.19,
      "high": 22.19,
      "low": 22.15,
      "close": 22.15,
      "volume": 4278,
      "datetime": 1737058860000
    },
    {
      "open": 22.15,
      "high": 22.185,
      "low": 22.15,
      "close": 22.17,
      "volume": 3369,
      "datetime": 1737058920000
    },
    {
      "open": 22.2,
      "high": 22.21,
      "low": 22.2,
      "close": 22.2099,
      "volume": 3747,
      "datetime": 1737058980000
    },
    {
      "open": 22.2097,
      "high": 22.2097,
      "low": 22.19,
      "close": 22.195,
      "volume": 1450,
      "datetime": 1737059100000
    },
    {
      "open": 22.2,
      "high": 22.2,
      "low": 22.2,
      "close": 22.2,
      "volume": 1622,
      "datetime": 1737059160000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.17,
      "close": 22.17,
      "volume": 1575,
      "datetime": 1737059220000
    },
    {
      "open": 22.155,
      "high": 22.155,
      "low": 22.145,
      "close": 22.145,
      "volume": 1623,
      "datetime": 1737059280000
    },
    {
      "open": 22.15,
      "high": 22.1541,
      "low": 22.1445,
      "close": 22.1445,
      "volume": 1051,
      "datetime": 1737059340000
    },
    {
      "open": 22.145,
      "high": 22.145,
      "low": 22.14,
      "close": 22.14,
      "volume": 1585,
      "datetime": 1737059400000
    },
    {
      "open": 22.15,
      "high": 22.17,
      "low": 22.15,
      "close": 22.16,
      "volume": 3375,
      "datetime": 1737059460000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.14,
      "close": 22.14,
      "volume": 3305,
      "datetime": 1737059520000
    },
    {
      "open": 22.13,
      "high": 22.16,
      "low": 22.13,
      "close": 22.16,
      "volume": 6380,
      "datetime": 1737059580000
    },
    {
      "open": 22.15,
      "high": 22.155,
      "low": 22.145,
      "close": 22.155,
      "volume": 2825,
      "datetime": 1737059700000
    },
    {
      "open": 22.145,
      "high": 22.145,
      "low": 22.145,
      "close": 22.145,
      "volume": 300,
      "datetime": 1737059760000
    },
    {
      "open": 22.14,
      "high": 22.14,
      "low": 22.14,
      "close": 22.14,
      "volume": 100,
      "datetime": 1737059820000
    },
    {
      "open": 22.135,
      "high": 22.1497,
      "low": 22.135,
      "close": 22.1497,
      "volume": 2775,
      "datetime": 1737059880000
    },
    {
      "open": 22.1699,
      "high": 22.1699,
      "low": 22.1699,
      "close": 22.1699,
      "volume": 100,
      "datetime": 1737059940000
    },
    {
      "open": 22.175,
      "high": 22.175,
      "low": 22.1543,
      "close": 22.1545,
      "volume": 1551,
      "datetime": 1737060000000
    },
    {
      "open": 22.165,
      "high": 22.175,
      "low": 22.155,
      "close": 22.175,
      "volume": 911,
      "datetime": 1737060060000
    },
    {
      "open": 22.17,
      "high": 22.17,
      "low": 22.15,
      "close": 22.15,
      "volume": 900,
      "datetime": 1737060120000
    },
    {
      "open": 22.1598,
      "high": 22.168,
      "low": 22.1598,
      "close": 22.168,
      "volume": 2200,
      "datetime": 1737060180000
    },
    {
      "open": 22.175,
      "high": 22.175,
      "low": 22.17,
      "close": 22.17,
      "volume": 1791,
      "datetime": 1737060240000
    },
    {
      "open": 22.1601,
      "high": 22.1601,
      "low": 22.16,
      "close": 22.16,
      "volume": 2100,
      "datetime": 1737060300000
    },
    {
      "open": 22.14,
      "high": 22.17,
      "low": 22.14,
      "close": 22.17,
      "volume": 2297,
      "datetime": 1737060360000
    },
    {
      "open": 22.175,
      "high": 22.175,
      "low": 22.17,
      "close": 22.17,
      "volume": 1475,
      "datetime": 1737060420000
    },
    {
      "open": 22.18,
      "high": 22.195,
      "low": 22.175,
      "close": 22.195,
      "volume": 7560,
      "datetime": 1737060480000
    },
    {
      "open": 22.195,
      "high": 22.205,
      "low": 22.19,
      "close": 22.19,
      "volume": 925,
      "datetime": 1737060540000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.155,
      "close": 22.155,
      "volume": 2455,
      "datetime": 1737060600000
    },
    {
      "open": 22.145,
      "high": 22.15,
      "low": 22.145,
      "close": 22.15,
      "volume": 1004,
      "datetime": 1737060660000
    },
    {
      "open": 22.15,
      "high": 22.16,
      "low": 22.145,
      "close": 22.16,
      "volume": 4250,
      "datetime": 1737060720000
    },
    {
      "open": 22.155,
      "high": 22.155,
      "low": 22.1498,
      "close": 22.1498,
      "volume": 1751,
      "datetime": 1737060780000
    },
    {
      "open": 22.145,
      "high": 22.16,
      "low": 22.145,
      "close": 22.16,
      "volume": 3128,
      "datetime": 1737060840000
    },
    {
      "open": 22.155,
      "high": 22.18,
      "low": 22.155,
      "close": 22.18,
      "volume": 9965,
      "datetime": 1737060900000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.18,
      "close": 22.18,
      "volume": 2444,
      "datetime": 1737060960000
    },
    {
      "open": 22.165,
      "high": 22.2,
      "low": 22.165,
      "close": 22.185,
      "volume": 13624,
      "datetime": 1737061020000
    },
    {
      "open": 22.19,
      "high": 22.19,
      "low": 22.14,
      "close": 22.17,
      "volume": 28958,
      "datetime": 1737061080000
    },
    {
      "open": 22.18,
      "high": 22.225,
      "low": 22.175,
      "close": 22.2,
      "volume": 35104,
      "datetime": 1737061140000
    },
    {
      "open": 22.18,
      "high": 22.18,
      "low": 22.18,
      "close": 22.18,
      "volume": 3011,
      "datetime": 1737061200000
    },
    {
      "open": 22.24,
      "high": 22.24,
      "low": 22.24,
      "close": 22.24,
      "volume": 200,
      "datetime": 1737061380000
    },
    {
      "open": 22.25,
      "high": 22.25,
      "low": 22.25,
      "close": 22.25,
      "volume": 100,
      "datetime": 1737061620000
    },
    {
      "open": 22.2693,
      "high": 22.2693,
      "low": 22.2693,
      "close": 22.2693,
      "volume": 100,
      "datetime": 1737061740000
    },
    {
      "open": 22.2693,
      "high": 22.2693,
      "low": 22.2693,
      "close": 22.2693,
      "volume": 200,
      "datetime": 1737061980000
    },
    {
      "open": 22.245,
      "high": 22.26,
      "low": 22.245,
      "close": 22.26,
      "volume": 500,
      "datetime": 1737062100000
    },
    {
      "open": 22.27,
      "high": 22.28,
      "low": 22.27,
      "close": 22.28,
      "volume": 200,
      "datetime": 1737062340000
    },
    {
      "open": 22.261,
      "high": 22.261,
      "low": 22.261,
      "close": 22.261,
      "volume": 100,
      "datetime": 1737062400000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 100,
      "datetime": 1737062460000
    },
    {
      "open": 22.32,
      "high": 22.32,
      "low": 22.32,
      "close": 22.32,
      "volume": 200,
      "datetime": 1737062580000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 222,
      "datetime": 1737062640000
    },
    {
      "open": 22.33,
      "high": 22.33,
      "low": 22.33,
      "close": 22.33,
      "volume": 200,
      "datetime": 1737063060000
    },
    {
      "open": 22.34,
      "high": 22.34,
      "low": 22.34,
      "close": 22.34,
      "volume": 1000,
      "datetime": 1737063360000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 1258,
      "datetime": 1737063540000
    },
    {
      "open": 22.2699,
      "high": 22.2699,
      "low": 22.2699,
      "close": 22.2699,
      "volume": 300,
      "datetime": 1737064020000
    },
    {
      "open": 22.31,
      "high": 22.31,
      "low": 22.31,
      "close": 22.31,
      "volume": 150,
      "datetime": 1737064260000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 100,
      "datetime": 1737065040000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 300,
      "datetime": 1737065100000
    },
    {
      "open": 22.299,
      "high": 22.299,
      "low": 22.299,
      "close": 22.299,
      "volume": 200,
      "datetime": 1737065700000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 417,
      "datetime": 1737066060000
    },
    {
      "open": 22.35,
      "high": 22.35,
      "low": 22.35,
      "close": 22.35,
      "volume": 100,
      "datetime": 1737066420000
    },
    {
      "open": 22.359,
      "high": 22.359,
      "low": 22.359,
      "close": 22.359,
      "volume": 1000,
      "datetime": 1737067800000
    },
    {
      "open": 22.3,
      "high": 22.3,
      "low": 22.3,
      "close": 22.3,
      "volume": 447,
      "datetime": 1737068580000
    },
    {
      "open": 22.36,
      "high": 22.36,
      "low": 22.36,
      "close": 22.36,
      "volume": 500,
      "datetime": 1737068760000
    },
    {
      "open": 22.2301,
      "high": 22.2301,
      "low": 22.2301,
      "close": 22.2301,
      "volume": 3500,
      "datetime": 1737069480000
    },
    {
      "open": 22.3283,
      "high": 22.3283,
      "low": 22.3283,
      "close": 22.3283,
      "volume": 222,
      "datetime": 1737070260000
    },
    {
      "open": 22.24,
      "high": 22.24,
      "low": 22.24,
      "close": 22.24,
      "volume": 200,
      "datetime": 1737072480000
    },
    {
      "open": 22.23,
      "high": 22.23,
      "low": 22.23,
      "close": 22.23,
      "volume": 100,
      "datetime": 1737072540000
    },
    {
      "open": 22.1907,
      "high": 22.1907,
      "low": 22.1907,
      "close": 22.1907,
      "volume": 100,
      "datetime": 1737073200000
    },
    {
      "open": 22.21,
      "high": 22.21,
      "low": 22.21,
      "close": 22.21,
      "volume": 125,
      "datetime": 1737073320000
    },
    {
      "open": 22.22,
      "high": 22.2201,
      "low": 22.22,
      "close": 22.2201,
      "volume": 432,
      "datetime": 1737074160000
    },
    {
      "open": 22.2499,
      "high": 22.2499,
      "low": 22.2499,
      "close": 22.2499,
      "volume": 106,
      "datetime": 1737074580000
    },
    {
      "open": 22.26,
      "high": 22.26,
      "low": 22.26,
      "close": 22.26,
      "volume": 328,
      "datetime": 1737074820000
    },
    {
      "open": 22.26,
      "high": 22.27,
      "low": 22.26,
      "close": 22.27,
      "volume": 300,
      "datetime": 1737074940000
    },
    {
      "open": 22.27,
      "high": 22.27,
      "low": 22.27,
      "close": 22.27,
      "volume": 450,
      "datetime": 1737075000000
    },
    {
      "open": 22.27,
      "high": 22.27,
      "low": 22.27,
      "close": 22.27,
      "volume": 2515,
      "datetime": 1737075060000
    },
    {
      "open": 22.2219,
      "high": 22.2219,
      "low": 22.2219,
      "close": 22.2219,
      "volume": 241,
      "datetime": 1737075420000
    },
    {
      "open": 22.2212,
      "high": 22.2212,
      "low": 22.2212,
      "close": 22.2212,
      "volume": 441,
      "datetime": 1737075540000
    },
    {
      "open": 22.25,
      "high": 22.25,
      "low": 22.25,
      "close": 22.25,
      "volume": 1,
      "datetime": 1737075660000
    },
    {
      "open": 22.24,
      "high": 22.24,
      "low": 22.23,
      "close": 22.23,
      "volume": 101,
      "datetime": 1737075780000
    },
    {
      "open": 22.26,
      "high": 22.26,
      "low": 22.26,
      "close": 22.26,
      "volume": 6,
      "datetime": 1737075900000
    },
    {
      "open": 22.22,
      "high": 22.22,
      "low": 22.22,
      "close": 22.22,
      "volume": 200,
      "datetime": 1737076260000
    },
    {
      "open": 22.22,
      "high": 22.22,
      "low": 22.22,
      "close": 22.22,
      "volume": 4,
      "datetime": 1737077160000
    },
    {
      "open": 22.15,
      "high": 22.15,
      "low": 22.14,
      "close": 22.14,
      "volume": 21,
      "datetime": 1737077700000
    },
    {
      "open": 22.07,
      "high": 22.07,
      "low": 22.07,
      "close": 22.07,
      "volume": 5,
      "datetime": 1737077760000
    },
    {
      "open": 22.07,
      "high": 22.07,
      "low": 22.07,
      "close": 22.07,
      "volume": 10,
      "datetime": 1737077820000
    },
    {
      "open": 22.07,
      "high": 22.07,
      "low": 22.02,
      "close": 22.02,
      "volume": 2006,
      "datetime": 1737077880000
    },
    {
      "open": 22,
      "high": 22,
      "low": 21.96,
      "close": 21.96,
      "volume": 752,
      "datetime": 1737078000000
    },
    {
      "open": 21.97,
      "high": 21.97,
      "low": 21.93,
      "close": 21.93,
      "volume": 1010,
      "datetime": 1737078060000
    },
    {
      "open": 21.97,
      "high": 21.97,
      "low": 21.97,
      "close": 21.97,
      "volume": 15,
      "datetime": 1737078120000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.96,
      "close": 21.96,
      "volume": 1,
      "datetime": 1737078180000
    },
    {
      "open": 21.9,
      "high": 21.92,
      "low": 21.87,
      "close": 21.87,
      "volume": 1392,
      "datetime": 1737078240000
    },
    {
      "open": 21.9,
      "high": 21.96,
      "low": 21.9,
      "close": 21.94,
      "volume": 35,
      "datetime": 1737078300000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 20,
      "datetime": 1737078420000
    },
    {
      "open": 21.9,
      "high": 21.98,
      "low": 21.9,
      "close": 21.98,
      "volume": 305,
      "datetime": 1737078480000
    },
    {
      "open": 21.98,
      "high": 21.98,
      "low": 21.97,
      "close": 21.97,
      "volume": 6,
      "datetime": 1737078540000
    },
    {
      "open": 21.98,
      "high": 21.98,
      "low": 21.98,
      "close": 21.98,
      "volume": 244,
      "datetime": 1737078600000
    },
    {
      "open": 21.98,
      "high": 21.98,
      "low": 21.98,
      "close": 21.98,
      "volume": 6,
      "datetime": 1737078660000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.95,
      "close": 21.95,
      "volume": 6,
      "datetime": 1737078780000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.93,
      "close": 21.93,
      "volume": 301,
      "datetime": 1737078840000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.89,
      "close": 21.89,
      "volume": 976,
      "datetime": 1737078900000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.87,
      "close": 21.87,
      "volume": 250,
      "datetime": 1737078960000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.87,
      "close": 21.87,
      "volume": 453,
      "datetime": 1737079200000
    },
    {
      "open": 21.87,
      "high": 21.89,
      "low": 21.86,
      "close": 21.89,
      "volume": 89,
      "datetime": 1737079260000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.92,
      "close": 21.92,
      "volume": 5,
      "datetime": 1737079380000
    },
    {
      "open": 21.92,
      "high": 21.93,
      "low": 21.92,
      "close": 21.93,
      "volume": 301,
      "datetime": 1737079440000
    },
    {
      "open": 21.91,
      "high": 21.93,
      "low": 21.91,
      "close": 21.93,
      "volume": 520,
      "datetime": 1737079500000
    },
    {
      "open": 21.91,
      "high": 21.91,
      "low": 21.91,
      "close": 21.91,
      "volume": 19,
      "datetime": 1737079860000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.88,
      "close": 21.88,
      "volume": 9,
      "datetime": 1737079980000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.86,
      "close": 21.86,
      "volume": 387,
      "datetime": 1737080040000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.84,
      "close": 21.84,
      "volume": 552,
      "datetime": 1737080100000
    },
    {
      "open": 21.82,
      "high": 21.82,
      "low": 21.81,
      "close": 21.81,
      "volume": 546,
      "datetime": 1737080160000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.8,
      "close": 21.8,
      "volume": 420,
      "datetime": 1737080220000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.79,
      "close": 21.79,
      "volume": 4,
      "datetime": 1737080280000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.8,
      "close": 21.8,
      "volume": 952,
      "datetime": 1737080340000
    },
    {
      "open": 21.81,
      "high": 21.82,
      "low": 21.81,
      "close": 21.82,
      "volume": 63,
      "datetime": 1737080400000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.8,
      "close": 21.8,
      "volume": 100,
      "datetime": 1737080460000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 100,
      "datetime": 1737080520000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.83,
      "close": 21.83,
      "volume": 15,
      "datetime": 1737080580000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.81,
      "close": 21.81,
      "volume": 20,
      "datetime": 1737080640000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 25,
      "datetime": 1737080760000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.83,
      "close": 21.83,
      "volume": 45,
      "datetime": 1737080820000
    },
    {
      "open": 21.83,
      "high": 21.83,
      "low": 21.81,
      "close": 21.81,
      "volume": 505,
      "datetime": 1737080880000
    },
    {
      "open": 21.84,
      "high": 21.85,
      "low": 21.84,
      "close": 21.85,
      "volume": 90,
      "datetime": 1737080940000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 355,
      "datetime": 1737081000000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 45,
      "datetime": 1737081060000
    },
    {
      "open": 21.86,
      "high": 21.89,
      "low": 21.86,
      "close": 21.89,
      "volume": 4236,
      "datetime": 1737081180000
    },
    {
      "open": 21.87,
      "high": 21.87,
      "low": 21.87,
      "close": 21.87,
      "volume": 25,
      "datetime": 1737081240000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 1,
      "datetime": 1737081360000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 555,
      "datetime": 1737081420000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.92,
      "close": 21.92,
      "volume": 1,
      "datetime": 1737081540000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 3,
      "datetime": 1737081600000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 20,
      "datetime": 1737081660000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 227,
      "datetime": 1737081720000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.92,
      "close": 21.92,
      "volume": 103,
      "datetime": 1737081780000
    },
    {
      "open": 21.92,
      "high": 21.95,
      "low": 21.92,
      "close": 21.95,
      "volume": 300,
      "datetime": 1737081900000
    },
    {
      "open": 21.99,
      "high": 21.99,
      "low": 21.99,
      "close": 21.99,
      "volume": 16,
      "datetime": 1737082020000
    },
    {
      "open": 22,
      "high": 22,
      "low": 22,
      "close": 22,
      "volume": 6,
      "datetime": 1737082080000
    },
    {
      "open": 22.05,
      "high": 22.05,
      "low": 22.05,
      "close": 22.05,
      "volume": 7,
      "datetime": 1737082260000
    },
    {
      "open": 22.05,
      "high": 22.05,
      "low": 22.05,
      "close": 22.05,
      "volume": 5,
      "datetime": 1737082500000
    },
    {
      "open": 22.03,
      "high": 22.03,
      "low": 22.02,
      "close": 22.02,
      "volume": 50,
      "datetime": 1737082620000
    },
    {
      "open": 22.04,
      "high": 22.04,
      "low": 22.04,
      "close": 22.04,
      "volume": 1100,
      "datetime": 1737082800000
    },
    {
      "open": 22,
      "high": 22,
      "low": 22,
      "close": 22,
      "volume": 1,
      "datetime": 1737082980000
    },
    {
      "open": 22.01,
      "high": 22.01,
      "low": 22.01,
      "close": 22.01,
      "volume": 1,
      "datetime": 1737083040000
    },
    {
      "open": 22.01,
      "high": 22.01,
      "low": 22.01,
      "close": 22.01,
      "volume": 100,
      "datetime": 1737083160000
    },
    {
      "open": 22,
      "high": 22,
      "low": 22,
      "close": 22,
      "volume": 1,
      "datetime": 1737083220000
    },
    {
      "open": 22.02,
      "high": 22.02,
      "low": 22.02,
      "close": 22.02,
      "volume": 1100,
      "datetime": 1737083520000
    },
    {
      "open": 22.05,
      "high": 22.05,
      "low": 22.05,
      "close": 22.05,
      "volume": 245,
      "datetime": 1737083700000
    },
    {
      "open": 22.05,
      "high": 22.05,
      "low": 22.05,
      "close": 22.05,
      "volume": 145,
      "datetime": 1737084420000
    },
    {
      "open": 22.07,
      "high": 22.07,
      "low": 22.07,
      "close": 22.07,
      "volume": 600,
      "datetime": 1737084480000
    },
    {
      "open": 22.03,
      "high": 22.03,
      "low": 22.03,
      "close": 22.03,
      "volume": 5,
      "datetime": 1737084960000
    },
    {
      "open": 22,
      "high": 22,
      "low": 21.99,
      "close": 21.99,
      "volume": 10,
      "datetime": 1737085020000
    },
    {
      "open": 22.05,
      "high": 22.05,
      "low": 22.05,
      "close": 22.05,
      "volume": 10,
      "datetime": 1737085620000
    },
    {
      "open": 22.02,
      "high": 22.02,
      "low": 22.02,
      "close": 22.02,
      "volume": 2500,
      "datetime": 1737085800000
    },
    {
      "open": 22.02,
      "high": 22.02,
      "low": 22.02,
      "close": 22.02,
      "volume": 50,
      "datetime": 1737085980000
    },
    {
      "open": 22.04,
      "high": 22.04,
      "low": 22.04,
      "close": 22.04,
      "volume": 700,
      "datetime": 1737086040000
    },
    {
      "open": 22,
      "high": 22,
      "low": 22,
      "close": 22,
      "volume": 12,
      "datetime": 1737086520000
    },
    {
      "open": 22.01,
      "high": 22.01,
      "low": 22.01,
      "close": 22.01,
      "volume": 45,
      "datetime": 1737088920000
    },
    {
      "open": 22.01,
      "high": 22.02,
      "low": 22.01,
      "close": 22.02,
      "volume": 235,
      "datetime": 1737089040000
    },
    {
      "open": 22,
      "high": 22,
      "low": 22,
      "close": 22,
      "volume": 50,
      "datetime": 1737089220000
    },
    {
      "open": 21.99,
      "high": 21.99,
      "low": 21.99,
      "close": 21.99,
      "volume": 15,
      "datetime": 1737089400000
    },
    {
      "open": 21.98,
      "high": 21.98,
      "low": 21.98,
      "close": 21.98,
      "volume": 13,
      "datetime": 1737089460000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.96,
      "close": 21.96,
      "volume": 12,
      "datetime": 1737089520000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 750,
      "datetime": 1737089640000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.94,
      "close": 21.94,
      "volume": 1000,
      "datetime": 1737089700000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 3000,
      "datetime": 1737089760000
    },
    {
      "open": 21.93,
      "high": 21.93,
      "low": 21.92,
      "close": 21.92,
      "volume": 3,
      "datetime": 1737090420000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 3,
      "datetime": 1737090600000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 405,
      "datetime": 1737090720000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 1,
      "datetime": 1737091980000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 10,
      "datetime": 1737092220000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 2,
      "datetime": 1737092520000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.95,
      "close": 21.95,
      "volume": 47,
      "datetime": 1737092580000
    },
    {
      "open": 21.97,
      "high": 21.97,
      "low": 21.97,
      "close": 21.97,
      "volume": 3,
      "datetime": 1737092700000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 30,
      "datetime": 1737094020000
    },
    {
      "open": 21.93,
      "high": 21.93,
      "low": 21.93,
      "close": 21.93,
      "volume": 10,
      "datetime": 1737094260000
    },
    {
      "open": 21.93,
      "high": 21.93,
      "low": 21.93,
      "close": 21.93,
      "volume": 15,
      "datetime": 1737094320000
    },
    {
      "open": 21.95,
      "high": 21.95,
      "low": 21.94,
      "close": 21.94,
      "volume": 25,
      "datetime": 1737095280000
    },
    {
      "open": 21.96,
      "high": 21.96,
      "low": 21.96,
      "close": 21.96,
      "volume": 10,
      "datetime": 1737096300000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 2,
      "datetime": 1737099060000
    },
    {
      "open": 21.94,
      "high": 21.94,
      "low": 21.94,
      "close": 21.94,
      "volume": 25,
      "datetime": 1737099480000
    },
    {
      "open": 21.88,
      "high": 21.88,
      "low": 21.84,
      "close": 21.84,
      "volume": 17,
      "datetime": 1737099660000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 44,
      "datetime": 1737099960000
    },
    {
      "open": 21.92,
      "high": 21.92,
      "low": 21.92,
      "close": 21.92,
      "volume": 45,
      "datetime": 1737100800000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 10,
      "datetime": 1737101820000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.8,
      "close": 21.8,
      "volume": 224,
      "datetime": 1737102900000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.8,
      "close": 21.8,
      "volume": 10,
      "datetime": 1737103020000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.81,
      "close": 21.81,
      "volume": 1,
      "datetime": 1737103800000
    },
    {
      "open": 21.81,
      "high": 21.81,
      "low": 21.79,
      "close": 21.79,
      "volume": 2011,
      "datetime": 1737104100000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.77,
      "close": 21.77,
      "volume": 1494,
      "datetime": 1737104460000
    },
    {
      "open": 21.82,
      "high": 21.82,
      "low": 21.81,
      "close": 21.81,
      "volume": 200,
      "datetime": 1737104580000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.77,
      "close": 21.77,
      "volume": 386,
      "datetime": 1737104640000
    },
    {
      "open": 21.76,
      "high": 21.76,
      "low": 21.76,
      "close": 21.76,
      "volume": 140,
      "datetime": 1737104880000
    },
    {
      "open": 21.76,
      "high": 21.76,
      "low": 21.76,
      "close": 21.76,
      "volume": 487,
      "datetime": 1737105120000
    },
    {
      "open": 21.75,
      "high": 21.75,
      "low": 21.75,
      "close": 21.75,
      "volume": 100,
      "datetime": 1737105180000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.86,
      "close": 21.86,
      "volume": 850,
      "datetime": 1737105840000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 248,
      "datetime": 1737106020000
    },
    {
      "open": 21.865,
      "high": 21.865,
      "low": 21.865,
      "close": 21.865,
      "volume": 217,
      "datetime": 1737106140000
    },
    {
      "open": 21.89,
      "high": 21.89,
      "low": 21.89,
      "close": 21.89,
      "volume": 500,
      "datetime": 1737106680000
    },
    {
      "open": 21.9,
      "high": 21.9,
      "low": 21.9,
      "close": 21.9,
      "volume": 100,
      "datetime": 1737106980000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 100,
      "datetime": 1737107160000
    },
    {
      "open": 21.84,
      "high": 21.84,
      "low": 21.84,
      "close": 21.84,
      "volume": 100,
      "datetime": 1737107220000
    },
    {
      "open": 21.86,
      "high": 21.86,
      "low": 21.86,
      "close": 21.86,
      "volume": 120,
      "datetime": 1737108300000
    },
    {
      "open": 21.85,
      "high": 21.85,
      "low": 21.85,
      "close": 21.85,
      "volume": 100,
      "datetime": 1737108360000
    },
    {
      "open": 21.82,
      "high": 21.82,
      "low": 21.82,
      "close": 21.82,
      "volume": 400,
      "datetime": 1737109020000
    },
    {
      "open": 21.8,
      "high": 21.8,
      "low": 21.8,
      "close": 21.8,
      "volume": 630,
      "datetime": 1737109200000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.79,
      "close": 21.79,
      "volume": 202,
      "datetime": 1737109500000
    },
    {
      "open": 21.77,
      "high": 21.77,
      "low": 21.77,
      "close": 21.77,
      "volume": 2299,
      "datetime": 1737109980000
    },
    {
      "open": 21.77,
      "high": 21.77,
      "low": 21.77,
      "close": 21.77,
      "volume": 500,
      "datetime": 1737110100000
    },
    {
      "open": 21.7,
      "high": 21.7,
      "low": 21.7,
      "close": 21.7,
      "volume": 250,
      "datetime": 1737110280000
    },
    {
      "open": 21.71,
      "high": 21.71,
      "low": 21.71,
      "close": 21.71,
      "volume": 439,
      "datetime": 1737110340000
    },
    {
      "open": 21.72,
      "high": 21.73,
      "low": 21.72,
      "close": 21.73,
      "volume": 565,
      "datetime": 1737110400000
    },
    {
      "open": 21.755,
      "high": 21.76,
      "low": 21.755,
      "close": 21.76,
      "volume": 1450,
      "datetime": 1737110580000
    },
    {
      "open": 21.78,
      "high": 21.78,
      "low": 21.77,
      "close": 21.77,
      "volume": 900,
      "datetime": 1737110760000
    },
    {
      "open": 21.79,
      "high": 21.8,
      "low": 21.79,
      "close": 21.8,
      "volume": 850,
      "datetime": 1737111480000
    },
    {
      "open": 21.79,
      "high": 21.79,
      "low": 21.79,
      "close": 21.79,
      "volume": 106,
      "datetime": 1737112380000
    },
    {
      "open": 21.78,
      "high": 21.78,
      "low": 21.78,
      "close": 21.78,
      "volume": 350,
      "datetime": 1737112560000
    },
    {
      "open": 21.75,
      "high": 21.75,
      "low": 21.75,
      "close": 21.75,
      "volume": 100,
      "datetime": 1737112620000
    },
    {
      "open": 21.74,
      "high": 21.74,
      "low": 21.73,
      "close": 21.73,
      "volume": 750,
      "datetime": 1737112680000
    },
    {
      "open": 21.76,
      "high": 21.76,
      "low": 21.76,
      "close": 21.76,
      "volume": 291,
      "datetime": 1737113580000
    },
    {
      "open": 21.77,
      "high": 21.77,
      "low": 21.77,
      "close": 21.77,
      "volume": 100,
      "datetime": 1737114720000
    },
    {
      "open": 21.78,
      "high": 21.79,
      "low": 21.78,
      "close": 21.79,
      "volume": 1815,
      "datetime": 1737115200000
    },
    {
      "open": 21.77,
      "high": 21.77,
      "low": 21.77,
      "close": 21.77,
      "volume": 100,
      "datetime": 1737115440000
    },
    {
      "open": 21.75,
      "high": 21.75,
      "low": 21.73,
      "close": 21.73,
      "volume": 2133,
      "datetime": 1737115620000
    },
    {
      "open": 21.74,
      "high": 21.74,
      "low": 21.74,
      "close": 21.74,
      "volume": 101,
      "datetime": 1737115920000
    },
    {
      "open": 21.71,
      "high": 21.71,
      "low": 21.71,
      "close": 21.71,
      "volume": 130,
      "datetime": 1737116040000
    },
    {
      "open": 21.71,
      "high": 21.71,
      "low": 21.71,
      "close": 21.71,
      "volume": 110,
      "datetime": 1737116340000
    },
    {
      "open": 21.7,
      "high": 21.7,
      "low": 21.7,
      "close": 21.7,
      "volume": 100,
      "datetime": 1737116400000
    },
    {
      "open": 21.73,
      "high": 21.73,
      "low": 21.73,
      "close": 21.73,
      "volume": 100,
      "datetime": 1737116700000
    },
    {
      "open": 21.73,
      "high": 21.73,
      "low": 21.71,
      "close": 21.71,
      "volume": 400,
      "datetime": 1737116880000
    },
    {
      "open": 21.73,
      "high": 21.73,
      "low": 21.73,
      "close": 21.73,
      "volume": 300,
      "datetime": 1737116940000
    },
    {
      "open": 21.74,
      "high": 21.74,
      "low": 21.74,
      "close": 21.74,
      "volume": 430,
      "datetime": 1737117360000
    },
    {
      "open": 21.71,
      "high": 21.71,
      "low": 21.71,
      "close": 21.71,
      "volume": 180,
      "datetime": 1737117420000
    },
    {
      "open": 21.75,
      "high": 21.75,
      "low": 21.75,
      "close": 21.75,
      "volume": 100,
      "datetime": 1737117480000
    },
    {
      "open": 21.68,
      "high": 21.7,
      "low": 21.68,
      "close": 21.7,
      "volume": 900,
      "datetime": 1737117600000
    },
    {
      "open": 21.68,
      "high": 21.68,
      "low": 21.66,
      "close": 21.66,
      "volume": 512,
      "datetime": 1737117660000
    },
    {
      "open": 21.67,
      "high": 21.67,
      "low": 21.67,
      "close": 21.67,
      "volume": 100,
      "datetime": 1737117720000
    },
    {
      "open": 21.66,
      "high": 21.66,
      "low": 21.66,
      "close": 21.66,
      "volume": 100,
      "datetime": 1737117900000
    },
    {
      "open": 21.61,
      "high": 21.61,
      "low": 21.61,
      "close": 21.61,
      "volume": 121,
      "datetime": 1737118140000
    },
    {
      "open": 21.66,
      "high": 21.66,
      "low": 21.66,
      "close": 21.66,
      "volume": 250,
      "datetime": 1737118200000
    },
    {
      "open": 21.66,
      "high": 21.66,
      "low": 21.66,
      "close": 21.66,
      "volume": 220,
      "datetime": 1737118260000
    },
    {
      "open": 21.62,
      "high": 21.65,
      "low": 21.62,
      "close": 21.62,
      "volume": 1100,
      "datetime": 1737118320000
    },
    {
      "open": 21.64,
      "high": 21.64,
      "low": 21.64,
      "close": 21.64,
      "volume": 230,
      "datetime": 1737118440000
    },
    {
      "open": 21.67,
      "high": 21.67,
      "low": 21.67,
      "close": 21.67,
      "volume": 9229,
      "datetime": 1737118620000
    },
    {
      "open": 21.67,
      "high": 21.67,
      "low": 21.67,
      "close": 21.67,
      "volume": 300,
      "datetime": 1737118680000
    },
    {
      "open": 21.65,
      "high": 21.65,
      "low": 21.65,
      "close": 21.65,
      "volume": 200,
      "datetime": 1737118800000
    },
    {
      "open": 21.611,
      "high": 21.611,
      "low": 21.61,
      "close": 21.61,
      "volume": 3900,
      "datetime": 1737118920000
    },
    {
      "open": 21.61,
      "high": 21.61,
      "low": 21.6,
      "close": 21.61,
      "volume": 4240,
      "datetime": 1737118980000
    },
    {
      "open": 21.61,
      "high": 21.61,
      "low": 21.6,
      "close": 21.6007,
      "volume": 1332,
      "datetime": 1737119100000
    },
    {
      "open": 21.6297,
      "high": 21.6297,
      "low": 21.6297,
      "close": 21.6297,
      "volume": 160,
      "datetime": 1737119160000
    },
    {
      "open": 21.63,
      "high": 21.63,
      "low": 21.6007,
      "close": 21.6007,
      "volume": 200,
      "datetime": 1737119220000
    },
    {
      "open": 21.63,
      "high": 21.63,
      "low": 21.63,
      "close": 21.63,
      "volume": 100,
      "datetime": 1737119340000
    },
    {
      "open": 21.62,
      "high": 21.62,
      "low": 21.62,
      "close": 21.62,
      "volume": 100,
      "datetime": 1737119400000
    },
    {
      "open": 21.6207,
      "high": 21.6207,
      "low": 21.6201,
      "close": 21.6201,
      "volume": 2150,
      "datetime": 1737119520000
    },
    {
      "open": 21.64,
      "high": 21.66,
      "low": 21.64,
      "close": 21.66,
      "volume": 300,
      "datetime": 1737119580000
    },
    {
      "open": 21.62,
      "high": 21.62,
      "low": 21.62,
      "close": 21.62,
      "volume": 900,
      "datetime": 1737119760000
    },
    {
      "open": 21.65,
      "high": 21.68,
      "low": 21.65,
      "close": 21.66,
      "volume": 1200,
      "datetime": 1737119880000
    },
    {
      "open": 21.67,
      "high": 21.67,
      "low": 21.67,
      "close": 21.67,
      "volume": 100,
      "datetime": 1737120000000
    },
    {
      "open": 21.65,
      "high": 21.65,
      "low": 21.65,
      "close": 21.65,
      "volume": 200,
      "datetime": 1737120060000
    },
    {
      "open": 21.67,
      "high": 21.6701,
      "low": 21.67,
      "close": 21.6701,
      "volume": 2200,
      "datetime": 1737120120000
    },
    {
      "open": 21.69,
      "high": 21.69,
      "low": 21.66,
      "close": 21.66,
      "volume": 300,
      "datetime": 1737120180000
    },
    {
      "open": 21.69,
      "high": 21.69,
      "low": 21.69,
      "close": 21.69,
      "volume": 100,
      "datetime": 1737120480000
    },
    {
      "open": 21.68,
      "high": 21.7,
      "low": 21.68,
      "close": 21.7,
      "volume": 4544,
      "datetime": 1737120660000
    },
    {
      "open": 21.6504,
      "high": 21.67,
      "low": 21.6504,
      "close": 21.67,
      "volume": 1620,
      "datetime": 1737120960000
    },
    {
      "open": 21.661,
      "high": 21.661,
      "low": 21.661,
      "close": 21.661,
      "volume": 100,
      "datetime": 1737121020000
    },
    {
      "open": 21.71,
      "high": 21.71,
      "low": 21.71,
      "close": 21.71,
      "volume": 650,
      "datetime": 1737121140000
    },
    {
      "open": 21.73,
      "high": 21.73,
      "low": 21.66,
      "close": 21.66,
      "volume": 1496,
      "datetime": 1737121200000
    },
    {
      "open": 21.686,
      "high": 21.686,
      "low": 21.686,
      "close": 21.686,
      "volume": 500,
      "datetime": 1737121260000
    },
    {
      "open": 21.6207,
      "high": 21.6207,
      "low": 21.62,
      "close": 21.62,
      "volume": 400,
      "datetime": 1737121320000
    },
    {
      "open": 21.6207,
      "high": 21.66,
      "low": 21.6207,
      "close": 21.66,
      "volume": 300,
      "datetime": 1737121380000
    },
    {
      "open": 21.65,
      "high": 21.65,
      "low": 21.65,
      "close": 21.65,
      "volume": 3143,
      "datetime": 1737121560000
    },
    {
      "open": 21.68,
      "high": 21.68,
      "low": 21.68,
      "close": 21.68,
      "volume": 1257,
      "datetime": 1737121920000
    },
    {
      "open": 21.69,
      "high": 21.69,
      "low": 21.69,
      "close": 21.69,
      "volume": 100,
      "datetime": 1737121980000
    },
    {
      "open": 21.7005,
      "high": 21.7005,
      "low": 21.7005,
      "close": 21.7005,
      "volume": 2250,
      "datetime": 1737122040000
    },
    {
      "open": 21.71,
      "high": 21.71,
      "low": 21.71,
      "close": 21.71,
      "volume": 457,
      "datetime": 1737122100000
    },
    {
      "open": 21.71,
      "high": 21.73,
      "low": 21.7,
      "close": 21.73,
      "volume": 4350,
      "datetime": 1737122220000
    },
    {
      "open": 21.72,
      "high": 21.72,
      "low": 21.72,
      "close": 21.72,
      "volume": 900,
      "datetime": 1737122280000
    },
    {
      "open": 21.7,
      "high": 21.7,
      "low": 21.69,
      "close": 21.69,
      "volume": 600,
      "datetime": 1737122400000
    },
    {
      "open": 21.69,
      "high": 21.69,
      "low": 21.69,
      "close": 21.69,
      "volume": 1070,
      "datetime": 1737122520000
    },
    {
      "open": 21.6701,
      "high": 21.6701,
      "low": 21.6701,
      "close": 21.6701,
      "volume": 1000,
      "datetime": 1737122580000
    },
    {
      "open": 21.6519,
      "high": 21.6519,
      "low": 21.6519,
      "close": 21.6519,
      "volume": 172,
      "datetime": 1737122640000
    },
    {
      "open": 21.68,
      "high": 21.68,
      "low": 21.68,
      "close": 21.68,
      "volume": 500,
      "datetime": 1737122700000
    },
    {
      "open": 21.6801,
      "high": 21.6801,
      "low": 21.68,
      "close": 21.68,
      "volume": 384,
      "datetime": 1737122820000
    },
    {
      "open": 21.65,
      "high": 21.65,
      "low": 21.65,
      "close": 21.65,
      "volume": 200,
      "datetime": 1737122940000
    },
    {
      "open": 21.6498,
      "high": 21.65,
      "low": 21.6498,
      "close": 21.65,
      "volume": 230,
      "datetime": 1737123600000
    },
    {
      "open": 21.6599,
      "high": 21.6599,
      "low": 21.6599,
      "close": 21.6599,
      "volume": 115,
      "datetime": 1737123780000
    },
    {
      "open": 21.64,
      "high": 21.66,
      "low": 21.64,
      "close": 21.66,
      "volume": 1340,
      "datetime": 1737123900000
    },
    {
      "open": 21.66,
      "high": 21.66,
      "low": 21.66,
      "close": 21.66,
      "volume": 100,
      "datetime": 1737124140000
    },
    {
      "open": 21.64,
      "high": 21.71,
      "low": 21.63,
      "close": 21.6994,
      "volume": 31140,
      "datetime": 1737124200000
    },
    {
      "open": 21.695,
      "high": 21.74,
      "low": 21.69,
      "close": 21.69,
      "volume": 14465,
      "datetime": 1737124260000
    },
    {
      "open": 21.69,
      "high": 21.7,
      "low": 21.64,
      "close": 21.6402,
      "volume": 4209,
      "datetime": 1737124320000
    },
    {
      "open": 21.62,
      "high": 21.635,
      "low": 21.59,
      "close": 21.63,
      "volume": 11711,
      "datetime": 1737124380000
    },
    {
      "open": 21.625,
      "high": 21.6597,
      "low": 21.601,
      "close": 21.6501,
      "volume": 20635,
      "datetime": 1737124440000
    },
    {
      "open": 21.61,
      "high": 21.63,
      "low": 21.57,
      "close": 21.57,
      "volume": 15785,
      "datetime": 1737124500000
    },
    {
      "open": 21.57,
      "high": 21.5776,
      "low": 21.5474,
      "close": 21.5474,
      "volume": 6613,
      "datetime": 1737124560000
    },
    {
      "open": 21.57,
      "high": 21.61,
      "low": 21.5452,
      "close": 21.58,
      "volume": 8637,
      "datetime": 1737124620000
    },
    {
      "open": 21.575,
      "high": 21.6474,
      "low": 21.575,
      "close": 21.6348,
      "volume": 8423,
      "datetime": 1737124680000
    },
    {
      "open": 21.625,
      "high": 21.6699,
      "low": 21.62,
      "close": 21.6201,
      "volume": 6400,
      "datetime": 1737124740000
    },
    {
      "open": 21.64,
      "high": 21.65,
      "low": 21.63,
      "close": 21.65,
      "volume": 700,
      "datetime": 1737124800000
    },
    {
      "open": 21.65,
      "high": 21.695,
      "low": 21.65,
      "close": 21.695,
      "volume": 13004,
      "datetime": 1737124860000
    },
    {
      "open": 21.69,
      "high": 21.725,
      "low": 21.6835,
      "close": 21.725,
      "volume": 5522,
      "datetime": 1737124920000
    },
    {
      "open": 21.72,
      "high": 21.73,
      "low": 21.72,
      "close": 21.73,
      "volume": 1821,
      "datetime": 1737124980000
    },
    {
      "open": 21.7099,
      "high": 21.7099,
      "low": 21.695,
      "close": 21.6999,
      "volume": 6670,
      "datetime": 1737125040000
    },
    {
      "open": 21.69,
      "high": 21.69,
      "low": 21.59,
      "close": 21.605,
      "volume": 5690,
      "datetime": 1737125100000
    },
    {
      "open": 21.6198,
      "high": 21.6198,
      "low": 21.61,
      "close": 21.61,
      "volume": 1077,
      "datetime": 1737125160000
    },
    {
      "open": 21.64,
      "high": 21.65,
      "low": 21.64,
      "close": 21.6499,
      "volume": 2700,
      "datetime": 1737125220000
    },
    {
      "open": 21.69,
      "high": 21.6999,
      "low": 21.67,
      "close": 21.68,
      "volume": 1927,
      "datetime": 1737125280000
    },
    {
      "open": 21.6774,
      "high": 21.685,
      "low": 21.6501,
      "close": 21.685,
      "volume": 2056,
      "datetime": 1737125340000
    },
    {
      "open": 21.665,
      "high": 21.6857,
      "low": 21.665,
      "close": 21.68,
      "volume": 1300,
      "datetime": 1737125400000
    },
    {
      "open": 21.6626,
      "high": 21.68,
      "low": 21.6626,
      "close": 21.68,
      "volume": 1600,
      "datetime": 1737125460000
    },
    {
      "open": 21.64,
      "high": 21.64,
      "low": 21.58,
      "close": 21.58,
      "volume": 7009,
      "datetime": 1737125520000
    },
    {
      "open": 21.58,
      "high": 21.5999,
      "low": 21.58,
      "close": 21.5999,
      "volume": 3914,
      "datetime": 1737125580000
    },
    {
      "open": 21.58,
      "high": 21.6,
      "low": 21.575,
      "close": 21.575,
      "volume": 1811,
      "datetime": 1737125640000
    },
    {
      "open": 21.57,
      "high": 21.57,
      "low": 21.56,
      "close": 21.5687,
      "volume": 3192,
      "datetime": 1737125700000
    },
    {
      "open": 21.565,
      "high": 21.565,
      "low": 21.51,
      "close": 21.51,
      "volume": 13372,
      "datetime": 1737125760000
    },
    {
      "open": 21.5139,
      "high": 21.535,
      "low": 21.505,
      "close": 21.5113,
      "volume": 5936,
      "datetime": 1737125820000
    },
    {
      "open": 21.5198,
      "high": 21.5404,
      "low": 21.5198,
      "close": 21.5404,
      "volume": 1350,
      "datetime": 1737125880000
    },
    {
      "open": 21.5498,
      "high": 21.5498,
      "low": 21.5008,
      "close": 21.5008,
      "volume": 815,
      "datetime": 1737125940000
    },
    {
      "open": 21.5,
      "high": 21.51,
      "low": 21.49,
      "close": 21.51,
      "volume": 5206,
      "datetime": 1737126000000
    },
    {
      "open": 21.502,
      "high": 21.5126,
      "low": 21.5,
      "close": 21.5,
      "volume": 9635,
      "datetime": 1737126060000
    },
    {
      "open": 21.5013,
      "high": 21.51,
      "low": 21.49,
      "close": 21.5,
      "volume": 3201,
      "datetime": 1737126120000
    },
    {
      "open": 21.495,
      "high": 21.5097,
      "low": 21.4502,
      "close": 21.4975,
      "volume": 10606,
      "datetime": 1737126180000
    },
    {
      "open": 21.49,
      "high": 21.49,
      "low": 21.45,
      "close": 21.45,
      "volume": 4040,
      "datetime": 1737126240000
    },
    {
      "open": 21.45,
      "high": 21.45,
      "low": 21.4035,
      "close": 21.4035,
      "volume": 12272,
      "datetime": 1737126300000
    },
    {
      "open": 21.4,
      "high": 21.4074,
      "low": 21.38,
      "close": 21.3801,
      "volume": 6434,
      "datetime": 1737126360000
    },
    {
      "open": 21.4,
      "high": 21.4,
      "low": 21.36,
      "close": 21.37,
      "volume": 3088,
      "datetime": 1737126420000
    },
    {
      "open": 21.37,
      "high": 21.3878,
      "low": 21.37,
      "close": 21.3743,
      "volume": 1100,
      "datetime": 1737126480000
    },
    {
      "open": 21.38,
      "high": 21.3818,
      "low": 21.3288,
      "close": 21.3288,
      "volume": 6995,
      "datetime": 1737126540000
    },
    {
      "open": 21.315,
      "high": 21.32,
      "low": 21.3,
      "close": 21.3123,
      "volume": 10742,
      "datetime": 1737126600000
    },
    {
      "open": 21.33,
      "high": 21.35,
      "low": 21.32,
      "close": 21.32,
      "volume": 3935,
      "datetime": 1737126660000
    },
    {
      "open": 21.325,
      "high": 21.33,
      "low": 21.31,
      "close": 21.33,
      "volume": 4224,
      "datetime": 1737126720000
    },
    {
      "open": 21.33,
      "high": 21.3599,
      "low": 21.33,
      "close": 21.3495,
      "volume": 4054,
      "datetime": 1737126780000
    },
    {
      "open": 21.345,
      "high": 21.35,
      "low": 21.3388,
      "close": 21.34,
      "volume": 15947,
      "datetime": 1737126840000
    },
    {
      "open": 21.34,
      "high": 21.34,
      "low": 21.305,
      "close": 21.305,
      "volume": 1949,
      "datetime": 1737126900000
    },
    {
      "open": 21.305,
      "high": 21.3064,
      "low": 21.3,
      "close": 21.3064,
      "volume": 4365,
      "datetime": 1737126960000
    },
    {
      "open": 21.3,
      "high": 21.31,
      "low": 21.295,
      "close": 21.2973,
      "volume": 23178,
      "datetime": 1737127020000
    },
    {
      "open": 21.305,
      "high": 21.315,
      "low": 21.3002,
      "close": 21.3002,
      "volume": 1700,
      "datetime": 1737127080000
    },
    {
      "open": 21.3,
      "high": 21.3,
      "low": 21.295,
      "close": 21.3,
      "volume": 2716,
      "datetime": 1737127140000
    },
    {
      "open": 21.305,
      "high": 21.37,
      "low": 21.305,
      "close": 21.37,
      "volume": 6813,
      "datetime": 1737127200000
    },
    {
      "open": 21.38,
      "high": 21.415,
      "low": 21.38,
      "close": 21.41,
      "volume": 12498,
      "datetime": 1737127260000
    },
    {
      "open": 21.395,
      "high": 21.435,
      "low": 21.37,
      "close": 21.435,
      "volume": 10255,
      "datetime": 1737127320000
    },
    {
      "open": 21.4199,
      "high": 21.43,
      "low": 21.41,
      "close": 21.42,
      "volume": 3377,
      "datetime": 1737127380000
    },
    {
      "open": 21.3801,
      "high": 21.405,
      "low": 21.38,
      "close": 21.38,
      "volume": 3356,
      "datetime": 1737127440000
    },
    {
      "open": 21.37,
      "high": 21.4074,
      "low": 21.35,
      "close": 21.4074,
      "volume": 4025,
      "datetime": 1737127500000
    },
    {
      "open": 21.395,
      "high": 21.465,
      "low": 21.395,
      "close": 21.46,
      "volume": 6710,
      "datetime": 1737127560000
    },
    {
      "open": 21.46,
      "high": 21.4788,
      "low": 21.46,
      "close": 21.4643,
      "volume": 12809,
      "datetime": 1737127620000
    },
    {
      "open": 21.46,
      "high": 21.47,
      "low": 21.41,
      "close": 21.41,
      "volume": 2705,
      "datetime": 1737127680000
    },
    {
      "open": 21.4052,
      "high": 21.41,
      "low": 21.3548,
      "close": 21.3548,
      "volume": 12542,
      "datetime": 1737127740000
    },
    {
      "open": 21.3416,
      "high": 21.38,
      "low": 21.3337,
      "close": 21.38,
      "volume": 3855,
      "datetime": 1737127800000
    },
    {
      "open": 21.38,
      "high": 21.3865,
      "low": 21.35,
      "close": 21.3865,
      "volume": 4329,
      "datetime": 1737127860000
    },
    {
      "open": 21.385,
      "high": 21.4301,
      "low": 21.385,
      "close": 21.4301,
      "volume": 700,
      "datetime": 1737127920000
    },
    {
      "open": 21.43,
      "high": 21.4352,
      "low": 21.4001,
      "close": 21.4001,
      "volume": 4857,
      "datetime": 1737127980000
    },
    {
      "open": 21.41,
      "high": 21.4198,
      "low": 21.4,
      "close": 21.4,
      "volume": 2956,
      "datetime": 1737128040000
    },
    {
      "open": 21.4007,
      "high": 21.4007,
      "low": 21.39,
      "close": 21.4,
      "volume": 2976,
      "datetime": 1737128100000
    },
    {
      "open": 21.4174,
      "high": 21.42,
      "low": 21.37,
      "close": 21.37,
      "volume": 4237,
      "datetime": 1737128160000
    },
    {
      "open": 21.37,
      "high": 21.37,
      "low": 21.35,
      "close": 21.3602,
      "volume": 1474,
      "datetime": 1737128220000
    },
    {
      "open": 21.3774,
      "high": 21.39,
      "low": 21.3774,
      "close": 21.39,
      "volume": 1300,
      "datetime": 1737128280000
    },
    {
      "open": 21.3587,
      "high": 21.3587,
      "low": 21.3587,
      "close": 21.3587,
      "volume": 1000,
      "datetime": 1737128340000
    },
    {
      "open": 21.36,
      "high": 21.37,
      "low": 21.36,
      "close": 21.36,
      "volume": 1275,
      "datetime": 1737128400000
    },
    {
      "open": 21.365,
      "high": 21.39,
      "low": 21.36,
      "close": 21.3894,
      "volume": 6024,
      "datetime": 1737128460000
    },
    {
      "open": 21.3799,
      "high": 21.3799,
      "low": 21.3799,
      "close": 21.3799,
      "volume": 200,
      "datetime": 1737128520000
    },
    {
      "open": 21.34,
      "high": 21.3401,
      "low": 21.3309,
      "close": 21.3401,
      "volume": 3150,
      "datetime": 1737128580000
    },
    {
      "open": 21.35,
      "high": 21.3787,
      "low": 21.35,
      "close": 21.3787,
      "volume": 425,
      "datetime": 1737128640000
    },
    {
      "open": 21.375,
      "high": 21.4,
      "low": 21.3698,
      "close": 21.4,
      "volume": 4390,
      "datetime": 1737128700000
    },
    {
      "open": 21.4013,
      "high": 21.425,
      "low": 21.4013,
      "close": 21.425,
      "volume": 2221,
      "datetime": 1737128760000
    },
    {
      "open": 21.405,
      "high": 21.43,
      "low": 21.39,
      "close": 21.43,
      "volume": 1437,
      "datetime": 1737128820000
    },
    {
      "open": 21.43,
      "high": 21.43,
      "low": 21.4048,
      "close": 21.41,
      "volume": 4471,
      "datetime": 1737128880000
    },
    {
      "open": 21.4,
      "high": 21.4,
      "low": 21.39,
      "close": 21.39,
      "volume": 711,
      "datetime": 1737128940000
    },
    {
      "open": 21.4006,
      "high": 21.4006,
      "low": 21.4,
      "close": 21.4,
      "volume": 1787,
      "datetime": 1737129000000
    },
    {
      "open": 21.39,
      "high": 21.39,
      "low": 21.375,
      "close": 21.375,
      "volume": 950,
      "datetime": 1737129060000
    },
    {
      "open": 21.37,
      "high": 21.37,
      "low": 21.3652,
      "close": 21.3652,
      "volume": 799,
      "datetime": 1737129120000
    },
    {
      "open": 21.37,
      "high": 21.375,
      "low": 21.3676,
      "close": 21.3676,
      "volume": 3333,
      "datetime": 1737129180000
    },
    {
      "open": 21.37,
      "high": 21.3876,
      "low": 21.3648,
      "close": 21.37,
      "volume": 9202,
      "datetime": 1737129240000
    },
    {
      "open": 21.39,
      "high": 21.39,
      "low": 21.38,
      "close": 21.38,
      "volume": 4300,
      "datetime": 1737129300000
    },
    {
      "open": 21.375,
      "high": 21.4,
      "low": 21.375,
      "close": 21.39,
      "volume": 4120,
      "datetime": 1737129360000
    },
    {
      "open": 21.3736,
      "high": 21.38,
      "low": 21.3632,
      "close": 21.375,
      "volume": 18200,
      "datetime": 1737129420000
    },
    {
      "open": 21.38,
      "high": 21.38,
      "low": 21.3699,
      "close": 21.3699,
      "volume": 1609,
      "datetime": 1737129480000
    },
    {
      "open": 21.38,
      "high": 21.38,
      "low": 21.36,
      "close": 21.36,
      "volume": 846,
      "datetime": 1737129540000
    },
    {
      "open": 21.36,
      "high": 21.38,
      "low": 21.36,
      "close": 21.38,
      "volume": 5520,
      "datetime": 1737129600000
    },
    {
      "open": 21.38,
      "high": 21.38,
      "low": 21.37,
      "close": 21.37,
      "volume": 925,
      "datetime": 1737129660000
    },
    {
      "open": 21.3514,
      "high": 21.37,
      "low": 21.3514,
      "close": 21.37,
      "volume": 1221,
      "datetime": 1737129720000
    },
    {
      "open": 21.38,
      "high": 21.38,
      "low": 21.3599,
      "close": 21.36,
      "volume": 1556,
      "datetime": 1737129780000
    },
    {
      "open": 21.36,
      "high": 21.36,
      "low": 21.3413,
      "close": 21.35,
      "volume": 2887,
      "datetime": 1737129840000
    },
    {
      "open": 21.35,
      "high": 21.36,
      "low": 21.35,
      "close": 21.36,
      "volume": 1279,
      "datetime": 1737129900000
    },
    {
      "open": 21.36,
      "high": 21.36,
      "low": 21.345,
      "close": 21.36,
      "volume": 875,
      "datetime": 1737129960000
    },
    {
      "open": 21.35,
      "high": 21.36,
      "low": 21.35,
      "close": 21.36,
      "volume": 2750,
      "datetime": 1737130020000
    },
    {
      "open": 21.36,
      "high": 21.37,
      "low": 21.3529,
      "close": 21.37,
      "volume": 695,
      "datetime": 1737130080000
    },
    {
      "open": 21.3878,
      "high": 21.395,
      "low": 21.3878,
      "close": 21.39,
      "volume": 8934,
      "datetime": 1737130140000
    },
    {
      "open": 21.38,
      "high": 21.3852,
      "low": 21.34,
      "close": 21.34,
      "volume": 2200,
      "datetime": 1737130200000
    },
    {
      "open": 21.325,
      "high": 21.325,
      "low": 21.3,
      "close": 21.3004,
      "volume": 4671,
      "datetime": 1737130260000
    },
    {
      "open": 21.3,
      "high": 21.3,
      "low": 21.2599,
      "close": 21.27,
      "volume": 24179,
      "datetime": 1737130320000
    },
    {
      "open": 21.279,
      "high": 21.279,
      "low": 21.2522,
      "close": 21.2522,
      "volume": 9200,
      "datetime": 1737130380000
    },
    {
      "open": 21.26,
      "high": 21.2679,
      "low": 21.2441,
      "close": 21.2441,
      "volume": 8299,
      "datetime": 1737130440000
    },
    {
      "open": 21.25,
      "high": 21.25,
      "low": 21.23,
      "close": 21.25,
      "volume": 15357,
      "datetime": 1737130500000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.225,
      "close": 21.2299,
      "volume": 4590,
      "datetime": 1737130560000
    },
    {
      "open": 21.225,
      "high": 21.235,
      "low": 21.225,
      "close": 21.23,
      "volume": 2231,
      "datetime": 1737130620000
    },
    {
      "open": 21.21,
      "high": 21.2299,
      "low": 21.2,
      "close": 21.205,
      "volume": 14032,
      "datetime": 1737130680000
    },
    {
      "open": 21.2,
      "high": 21.2199,
      "low": 21.1801,
      "close": 21.2,
      "volume": 14437,
      "datetime": 1737130740000
    },
    {
      "open": 21.205,
      "high": 21.205,
      "low": 21.172,
      "close": 21.19,
      "volume": 31100,
      "datetime": 1737130800000
    },
    {
      "open": 21.19,
      "high": 21.2,
      "low": 21.18,
      "close": 21.195,
      "volume": 12189,
      "datetime": 1737130860000
    },
    {
      "open": 21.18,
      "high": 21.19,
      "low": 21.1787,
      "close": 21.19,
      "volume": 888,
      "datetime": 1737130920000
    },
    {
      "open": 21.2,
      "high": 21.2377,
      "low": 21.2,
      "close": 21.2367,
      "volume": 16254,
      "datetime": 1737130980000
    },
    {
      "open": 21.2366,
      "high": 21.245,
      "low": 21.21,
      "close": 21.22,
      "volume": 4583,
      "datetime": 1737131040000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.22,
      "close": 21.22,
      "volume": 857,
      "datetime": 1737131100000
    },
    {
      "open": 21.23,
      "high": 21.245,
      "low": 21.215,
      "close": 21.22,
      "volume": 2449,
      "datetime": 1737131160000
    },
    {
      "open": 21.235,
      "high": 21.24,
      "low": 21.23,
      "close": 21.23,
      "volume": 687,
      "datetime": 1737131220000
    },
    {
      "open": 21.22,
      "high": 21.22,
      "low": 21.2131,
      "close": 21.2199,
      "volume": 869,
      "datetime": 1737131280000
    },
    {
      "open": 21.22,
      "high": 21.2299,
      "low": 21.22,
      "close": 21.2299,
      "volume": 1109,
      "datetime": 1737131340000
    },
    {
      "open": 21.22,
      "high": 21.23,
      "low": 21.215,
      "close": 21.23,
      "volume": 3750,
      "datetime": 1737131400000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.195,
      "close": 21.2199,
      "volume": 21904,
      "datetime": 1737131460000
    },
    {
      "open": 21.22,
      "high": 21.22,
      "low": 21.19,
      "close": 21.19,
      "volume": 9051,
      "datetime": 1737131520000
    },
    {
      "open": 21.205,
      "high": 21.205,
      "low": 21.1901,
      "close": 21.1901,
      "volume": 2130,
      "datetime": 1737131580000
    },
    {
      "open": 21.2,
      "high": 21.22,
      "low": 21.2,
      "close": 21.205,
      "volume": 2935,
      "datetime": 1737131640000
    },
    {
      "open": 21.215,
      "high": 21.215,
      "low": 21.1865,
      "close": 21.19,
      "volume": 7441,
      "datetime": 1737131700000
    },
    {
      "open": 21.18,
      "high": 21.18,
      "low": 21.18,
      "close": 21.18,
      "volume": 200,
      "datetime": 1737131760000
    },
    {
      "open": 21.1822,
      "high": 21.21,
      "low": 21.1822,
      "close": 21.2,
      "volume": 3839,
      "datetime": 1737131820000
    },
    {
      "open": 21.19,
      "high": 21.19,
      "low": 21.18,
      "close": 21.1899,
      "volume": 2775,
      "datetime": 1737131880000
    },
    {
      "open": 21.185,
      "high": 21.19,
      "low": 21.14,
      "close": 21.145,
      "volume": 4762,
      "datetime": 1737131940000
    },
    {
      "open": 21.15,
      "high": 21.1601,
      "low": 21.15,
      "close": 21.1601,
      "volume": 1884,
      "datetime": 1737132000000
    },
    {
      "open": 21.17,
      "high": 21.1799,
      "low": 21.15,
      "close": 21.155,
      "volume": 17771,
      "datetime": 1737132060000
    },
    {
      "open": 21.15,
      "high": 21.1568,
      "low": 21.1331,
      "close": 21.1331,
      "volume": 5160,
      "datetime": 1737132120000
    },
    {
      "open": 21.148,
      "high": 21.16,
      "low": 21.148,
      "close": 21.16,
      "volume": 885,
      "datetime": 1737132180000
    },
    {
      "open": 21.1549,
      "high": 21.17,
      "low": 21.1549,
      "close": 21.17,
      "volume": 6700,
      "datetime": 1737132240000
    },
    {
      "open": 21.17,
      "high": 21.1857,
      "low": 21.17,
      "close": 21.18,
      "volume": 3751,
      "datetime": 1737132300000
    },
    {
      "open": 21.18,
      "high": 21.21,
      "low": 21.18,
      "close": 21.205,
      "volume": 1730,
      "datetime": 1737132360000
    },
    {
      "open": 21.2,
      "high": 21.2,
      "low": 21.18,
      "close": 21.18,
      "volume": 1566,
      "datetime": 1737132420000
    },
    {
      "open": 21.1701,
      "high": 21.1772,
      "low": 21.1697,
      "close": 21.1697,
      "volume": 1910,
      "datetime": 1737132480000
    },
    {
      "open": 21.16,
      "high": 21.185,
      "low": 21.145,
      "close": 21.185,
      "volume": 3800,
      "datetime": 1737132540000
    },
    {
      "open": 21.2,
      "high": 21.2,
      "low": 21.18,
      "close": 21.19,
      "volume": 6367,
      "datetime": 1737132600000
    },
    {
      "open": 21.18,
      "high": 21.18,
      "low": 21.1557,
      "close": 21.1557,
      "volume": 975,
      "datetime": 1737132660000
    },
    {
      "open": 21.15,
      "high": 21.16,
      "low": 21.14,
      "close": 21.145,
      "volume": 2532,
      "datetime": 1737132720000
    },
    {
      "open": 21.1556,
      "high": 21.1556,
      "low": 21.1556,
      "close": 21.1556,
      "volume": 600,
      "datetime": 1737132780000
    },
    {
      "open": 21.15,
      "high": 21.15,
      "low": 21.1201,
      "close": 21.125,
      "volume": 7284,
      "datetime": 1737132840000
    },
    {
      "open": 21.129,
      "high": 21.13,
      "low": 21.129,
      "close": 21.13,
      "volume": 12045,
      "datetime": 1737132900000
    },
    {
      "open": 21.1266,
      "high": 21.15,
      "low": 21.12,
      "close": 21.14,
      "volume": 11718,
      "datetime": 1737132960000
    },
    {
      "open": 21.13,
      "high": 21.14,
      "low": 21.125,
      "close": 21.1299,
      "volume": 12472,
      "datetime": 1737133020000
    },
    {
      "open": 21.13,
      "high": 21.14,
      "low": 21.1252,
      "close": 21.1252,
      "volume": 2575,
      "datetime": 1737133080000
    },
    {
      "open": 21.12,
      "high": 21.14,
      "low": 21.12,
      "close": 21.14,
      "volume": 1160,
      "datetime": 1737133140000
    },
    {
      "open": 21.14,
      "high": 21.155,
      "low": 21.14,
      "close": 21.1534,
      "volume": 6300,
      "datetime": 1737133200000
    },
    {
      "open": 21.16,
      "high": 21.1848,
      "low": 21.16,
      "close": 21.16,
      "volume": 12482,
      "datetime": 1737133260000
    },
    {
      "open": 21.15,
      "high": 21.15,
      "low": 21.13,
      "close": 21.13,
      "volume": 3213,
      "datetime": 1737133320000
    },
    {
      "open": 21.135,
      "high": 21.1401,
      "low": 21.12,
      "close": 21.1203,
      "volume": 5474,
      "datetime": 1737133380000
    },
    {
      "open": 21.1298,
      "high": 21.16,
      "low": 21.1298,
      "close": 21.1399,
      "volume": 23774,
      "datetime": 1737133440000
    },
    {
      "open": 21.14,
      "high": 21.14,
      "low": 21.14,
      "close": 21.14,
      "volume": 29400,
      "datetime": 1737133500000
    },
    {
      "open": 21.17,
      "high": 21.19,
      "low": 21.17,
      "close": 21.19,
      "volume": 475,
      "datetime": 1737133560000
    },
    {
      "open": 21.19,
      "high": 21.1922,
      "low": 21.18,
      "close": 21.1922,
      "volume": 2536,
      "datetime": 1737133620000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.15,
      "close": 21.15,
      "volume": 1189,
      "datetime": 1737133680000
    },
    {
      "open": 21.15,
      "high": 21.15,
      "low": 21.15,
      "close": 21.15,
      "volume": 226,
      "datetime": 1737133740000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.16,
      "close": 21.16,
      "volume": 725,
      "datetime": 1737133800000
    },
    {
      "open": 21.15,
      "high": 21.17,
      "low": 21.15,
      "close": 21.17,
      "volume": 747,
      "datetime": 1737133860000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.16,
      "close": 21.16,
      "volume": 1097,
      "datetime": 1737133920000
    },
    {
      "open": 21.15,
      "high": 21.18,
      "low": 21.15,
      "close": 21.18,
      "volume": 2065,
      "datetime": 1737133980000
    },
    {
      "open": 21.185,
      "high": 21.185,
      "low": 21.18,
      "close": 21.18,
      "volume": 575,
      "datetime": 1737134040000
    },
    {
      "open": 21.1648,
      "high": 21.1648,
      "low": 21.15,
      "close": 21.16,
      "volume": 5680,
      "datetime": 1737134100000
    },
    {
      "open": 21.18,
      "high": 21.19,
      "low": 21.1643,
      "close": 21.1899,
      "volume": 3625,
      "datetime": 1737134160000
    },
    {
      "open": 21.18,
      "high": 21.18,
      "low": 21.17,
      "close": 21.18,
      "volume": 976,
      "datetime": 1737134220000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.1699,
      "close": 21.1699,
      "volume": 834,
      "datetime": 1737134280000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.1601,
      "close": 21.1631,
      "volume": 10881,
      "datetime": 1737134340000
    },
    {
      "open": 21.15,
      "high": 21.15,
      "low": 21.15,
      "close": 21.15,
      "volume": 500,
      "datetime": 1737134400000
    },
    {
      "open": 21.16,
      "high": 21.18,
      "low": 21.16,
      "close": 21.18,
      "volume": 1654,
      "datetime": 1737134460000
    },
    {
      "open": 21.1529,
      "high": 21.1529,
      "low": 21.1529,
      "close": 21.1529,
      "volume": 1500,
      "datetime": 1737134520000
    },
    {
      "open": 21.15,
      "high": 21.15,
      "low": 21.15,
      "close": 21.15,
      "volume": 642,
      "datetime": 1737134580000
    },
    {
      "open": 21.14,
      "high": 21.14,
      "low": 21.1215,
      "close": 21.13,
      "volume": 1430,
      "datetime": 1737134640000
    },
    {
      "open": 21.125,
      "high": 21.125,
      "low": 21.1099,
      "close": 21.1099,
      "volume": 30687,
      "datetime": 1737134700000
    },
    {
      "open": 21.1,
      "high": 21.1014,
      "low": 21.05,
      "close": 21.085,
      "volume": 41319,
      "datetime": 1737134760000
    },
    {
      "open": 21.09,
      "high": 21.11,
      "low": 21.075,
      "close": 21.1,
      "volume": 34357,
      "datetime": 1737134820000
    },
    {
      "open": 21.1,
      "high": 21.13,
      "low": 21.1,
      "close": 21.1299,
      "volume": 8800,
      "datetime": 1737134880000
    },
    {
      "open": 21.145,
      "high": 21.145,
      "low": 21.13,
      "close": 21.13,
      "volume": 2551,
      "datetime": 1737134940000
    },
    {
      "open": 21.1157,
      "high": 21.1157,
      "low": 21.1,
      "close": 21.11,
      "volume": 2968,
      "datetime": 1737135000000
    },
    {
      "open": 21.11,
      "high": 21.13,
      "low": 21.11,
      "close": 21.13,
      "volume": 295,
      "datetime": 1737135060000
    },
    {
      "open": 21.1335,
      "high": 21.1335,
      "low": 21.1335,
      "close": 21.1335,
      "volume": 300,
      "datetime": 1737135120000
    },
    {
      "open": 21.125,
      "high": 21.1299,
      "low": 21.1234,
      "close": 21.1234,
      "volume": 968,
      "datetime": 1737135180000
    },
    {
      "open": 21.15,
      "high": 21.18,
      "low": 21.15,
      "close": 21.1701,
      "volume": 11250,
      "datetime": 1737135240000
    },
    {
      "open": 21.18,
      "high": 21.2,
      "low": 21.18,
      "close": 21.2,
      "volume": 29523,
      "datetime": 1737135300000
    },
    {
      "open": 21.22,
      "high": 21.2498,
      "low": 21.21,
      "close": 21.2498,
      "volume": 21490,
      "datetime": 1737135360000
    },
    {
      "open": 21.25,
      "high": 21.2781,
      "low": 21.25,
      "close": 21.2671,
      "volume": 7235,
      "datetime": 1737135420000
    },
    {
      "open": 21.2699,
      "high": 21.2843,
      "low": 21.2699,
      "close": 21.27,
      "volume": 35146,
      "datetime": 1737135480000
    },
    {
      "open": 21.28,
      "high": 21.28,
      "low": 21.25,
      "close": 21.25,
      "volume": 7277,
      "datetime": 1737135540000
    },
    {
      "open": 21.2565,
      "high": 21.2599,
      "low": 21.24,
      "close": 21.2599,
      "volume": 3420,
      "datetime": 1737135600000
    },
    {
      "open": 21.26,
      "high": 21.2798,
      "low": 21.26,
      "close": 21.275,
      "volume": 7004,
      "datetime": 1737135660000
    },
    {
      "open": 21.27,
      "high": 21.28,
      "low": 21.2468,
      "close": 21.28,
      "volume": 5627,
      "datetime": 1737135720000
    },
    {
      "open": 21.2715,
      "high": 21.285,
      "low": 21.26,
      "close": 21.26,
      "volume": 6639,
      "datetime": 1737135780000
    },
    {
      "open": 21.27,
      "high": 21.2999,
      "low": 21.27,
      "close": 21.28,
      "volume": 9563,
      "datetime": 1737135840000
    },
    {
      "open": 21.29,
      "high": 21.2997,
      "low": 21.2667,
      "close": 21.2743,
      "volume": 6679,
      "datetime": 1737135900000
    },
    {
      "open": 21.27,
      "high": 21.27,
      "low": 21.253,
      "close": 21.253,
      "volume": 4432,
      "datetime": 1737135960000
    },
    {
      "open": 21.26,
      "high": 21.26,
      "low": 21.25,
      "close": 21.25,
      "volume": 1900,
      "datetime": 1737136020000
    },
    {
      "open": 21.25,
      "high": 21.25,
      "low": 21.2497,
      "close": 21.25,
      "volume": 1399,
      "datetime": 1737136080000
    },
    {
      "open": 21.26,
      "high": 21.27,
      "low": 21.26,
      "close": 21.27,
      "volume": 1840,
      "datetime": 1737136140000
    },
    {
      "open": 21.2571,
      "high": 21.285,
      "low": 21.2571,
      "close": 21.28,
      "volume": 4541,
      "datetime": 1737136200000
    },
    {
      "open": 21.3,
      "high": 21.3299,
      "low": 21.3,
      "close": 21.3299,
      "volume": 9511,
      "datetime": 1737136260000
    },
    {
      "open": 21.3298,
      "high": 21.333,
      "low": 21.3298,
      "close": 21.333,
      "volume": 865,
      "datetime": 1737136320000
    },
    {
      "open": 21.336,
      "high": 21.3435,
      "low": 21.3243,
      "close": 21.3435,
      "volume": 6268,
      "datetime": 1737136380000
    },
    {
      "open": 21.33,
      "high": 21.33,
      "low": 21.2918,
      "close": 21.3099,
      "volume": 40749,
      "datetime": 1737136440000
    },
    {
      "open": 21.31,
      "high": 21.3381,
      "low": 21.31,
      "close": 21.3381,
      "volume": 6337,
      "datetime": 1737136500000
    },
    {
      "open": 21.3285,
      "high": 21.3285,
      "low": 21.315,
      "close": 21.315,
      "volume": 834,
      "datetime": 1737136560000
    },
    {
      "open": 21.32,
      "high": 21.3483,
      "low": 21.32,
      "close": 21.335,
      "volume": 23174,
      "datetime": 1737136620000
    },
    {
      "open": 21.33,
      "high": 21.335,
      "low": 21.33,
      "close": 21.33,
      "volume": 1473,
      "datetime": 1737136680000
    },
    {
      "open": 21.3381,
      "high": 21.3381,
      "low": 21.32,
      "close": 21.32,
      "volume": 1573,
      "datetime": 1737136740000
    },
    {
      "open": 21.32,
      "high": 21.335,
      "low": 21.32,
      "close": 21.335,
      "volume": 8382,
      "datetime": 1737136800000
    },
    {
      "open": 21.33,
      "high": 21.33,
      "low": 21.3,
      "close": 21.3,
      "volume": 5589,
      "datetime": 1737136860000
    },
    {
      "open": 21.31,
      "high": 21.32,
      "low": 21.31,
      "close": 21.31,
      "volume": 4171,
      "datetime": 1737136920000
    },
    {
      "open": 21.31,
      "high": 21.31,
      "low": 21.3096,
      "close": 21.3096,
      "volume": 925,
      "datetime": 1737136980000
    },
    {
      "open": 21.3,
      "high": 21.3,
      "low": 21.265,
      "close": 21.27,
      "volume": 3522,
      "datetime": 1737137040000
    },
    {
      "open": 21.26,
      "high": 21.26,
      "low": 21.25,
      "close": 21.25,
      "volume": 1583,
      "datetime": 1737137100000
    },
    {
      "open": 21.26,
      "high": 21.2888,
      "low": 21.26,
      "close": 21.27,
      "volume": 2545,
      "datetime": 1737137160000
    },
    {
      "open": 21.28,
      "high": 21.3,
      "low": 21.28,
      "close": 21.3,
      "volume": 1425,
      "datetime": 1737137220000
    },
    {
      "open": 21.31,
      "high": 21.31,
      "low": 21.3,
      "close": 21.3,
      "volume": 951,
      "datetime": 1737137280000
    },
    {
      "open": 21.2997,
      "high": 21.2997,
      "low": 21.2997,
      "close": 21.2997,
      "volume": 500,
      "datetime": 1737137340000
    },
    {
      "open": 21.29,
      "high": 21.29,
      "low": 21.2769,
      "close": 21.2769,
      "volume": 1396,
      "datetime": 1737137400000
    },
    {
      "open": 21.3,
      "high": 21.3,
      "low": 21.29,
      "close": 21.29,
      "volume": 924,
      "datetime": 1737137460000
    },
    {
      "open": 21.2699,
      "high": 21.2699,
      "low": 21.2699,
      "close": 21.2699,
      "volume": 100,
      "datetime": 1737137520000
    },
    {
      "open": 21.26,
      "high": 21.26,
      "low": 21.26,
      "close": 21.26,
      "volume": 225,
      "datetime": 1737137580000
    },
    {
      "open": 21.26,
      "high": 21.26,
      "low": 21.26,
      "close": 21.26,
      "volume": 200,
      "datetime": 1737137700000
    },
    {
      "open": 21.2348,
      "high": 21.2348,
      "low": 21.2348,
      "close": 21.2348,
      "volume": 3000,
      "datetime": 1737137760000
    },
    {
      "open": 21.2301,
      "high": 21.24,
      "low": 21.2301,
      "close": 21.24,
      "volume": 650,
      "datetime": 1737137820000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.24,
      "close": 21.24,
      "volume": 175,
      "datetime": 1737137880000
    },
    {
      "open": 21.22,
      "high": 21.225,
      "low": 21.22,
      "close": 21.22,
      "volume": 650,
      "datetime": 1737137940000
    },
    {
      "open": 21.2,
      "high": 21.2,
      "low": 21.19,
      "close": 21.1952,
      "volume": 1074,
      "datetime": 1737138000000
    },
    {
      "open": 21.2,
      "high": 21.2,
      "low": 21.1926,
      "close": 21.195,
      "volume": 1986,
      "datetime": 1737138060000
    },
    {
      "open": 21.1956,
      "high": 21.1956,
      "low": 21.185,
      "close": 21.185,
      "volume": 950,
      "datetime": 1737138120000
    },
    {
      "open": 21.18,
      "high": 21.1999,
      "low": 21.18,
      "close": 21.1999,
      "volume": 1225,
      "datetime": 1737138180000
    },
    {
      "open": 21.21,
      "high": 21.215,
      "low": 21.2077,
      "close": 21.21,
      "volume": 1625,
      "datetime": 1737138240000
    },
    {
      "open": 21.1975,
      "high": 21.1975,
      "low": 21.1975,
      "close": 21.1975,
      "volume": 5000,
      "datetime": 1737138300000
    },
    {
      "open": 21.1864,
      "high": 21.21,
      "low": 21.1864,
      "close": 21.2,
      "volume": 991,
      "datetime": 1737138360000
    },
    {
      "open": 21.19,
      "high": 21.2,
      "low": 21.19,
      "close": 21.2,
      "volume": 975,
      "datetime": 1737138420000
    },
    {
      "open": 21.197,
      "high": 21.197,
      "low": 21.197,
      "close": 21.197,
      "volume": 348,
      "datetime": 1737138480000
    },
    {
      "open": 21.2,
      "high": 21.2028,
      "low": 21.2,
      "close": 21.2028,
      "volume": 568,
      "datetime": 1737138540000
    },
    {
      "open": 21.21,
      "high": 21.21,
      "low": 21.19,
      "close": 21.19,
      "volume": 1825,
      "datetime": 1737138600000
    },
    {
      "open": 21.19,
      "high": 21.19,
      "low": 21.18,
      "close": 21.18,
      "volume": 790,
      "datetime": 1737138660000
    },
    {
      "open": 21.195,
      "high": 21.2157,
      "low": 21.195,
      "close": 21.2157,
      "volume": 1970,
      "datetime": 1737138720000
    },
    {
      "open": 21.2199,
      "high": 21.23,
      "low": 21.2,
      "close": 21.2,
      "volume": 850,
      "datetime": 1737138780000
    },
    {
      "open": 21.207,
      "high": 21.2099,
      "low": 21.175,
      "close": 21.175,
      "volume": 1175,
      "datetime": 1737138840000
    },
    {
      "open": 21.1771,
      "high": 21.19,
      "low": 21.1771,
      "close": 21.19,
      "volume": 375,
      "datetime": 1737138900000
    },
    {
      "open": 21.18,
      "high": 21.18,
      "low": 21.177,
      "close": 21.177,
      "volume": 450,
      "datetime": 1737138960000
    },
    {
      "open": 21.1701,
      "high": 21.1701,
      "low": 21.155,
      "close": 21.155,
      "volume": 900,
      "datetime": 1737139020000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.16,
      "close": 21.16,
      "volume": 175,
      "datetime": 1737139080000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.1685,
      "close": 21.1685,
      "volume": 2350,
      "datetime": 1737139140000
    },
    {
      "open": 21.1797,
      "high": 21.18,
      "low": 21.1797,
      "close": 21.18,
      "volume": 3361,
      "datetime": 1737139200000
    },
    {
      "open": 21.1987,
      "high": 21.1987,
      "low": 21.1851,
      "close": 21.19,
      "volume": 4265,
      "datetime": 1737139260000
    },
    {
      "open": 21.19,
      "high": 21.2172,
      "low": 21.1897,
      "close": 21.2172,
      "volume": 1203,
      "datetime": 1737139320000
    },
    {
      "open": 21.21,
      "high": 21.21,
      "low": 21.1973,
      "close": 21.1973,
      "volume": 425,
      "datetime": 1737139380000
    },
    {
      "open": 21.18,
      "high": 21.19,
      "low": 21.18,
      "close": 21.19,
      "volume": 951,
      "datetime": 1737139440000
    },
    {
      "open": 21.1898,
      "high": 21.1898,
      "low": 21.18,
      "close": 21.18,
      "volume": 300,
      "datetime": 1737139500000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.16,
      "close": 21.17,
      "volume": 450,
      "datetime": 1737139560000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.16,
      "close": 21.16,
      "volume": 3968,
      "datetime": 1737139620000
    },
    {
      "open": 21.1519,
      "high": 21.1519,
      "low": 21.131327,
      "close": 21.14,
      "volume": 1244,
      "datetime": 1737139680000
    },
    {
      "open": 21.1399,
      "high": 21.15,
      "low": 21.1351,
      "close": 21.15,
      "volume": 1775,
      "datetime": 1737139740000
    },
    {
      "open": 21.14,
      "high": 21.14,
      "low": 21.14,
      "close": 21.14,
      "volume": 2155,
      "datetime": 1737139800000
    },
    {
      "open": 21.14,
      "high": 21.1476,
      "low": 21.137,
      "close": 21.137,
      "volume": 1715,
      "datetime": 1737139860000
    },
    {
      "open": 21.14,
      "high": 21.14,
      "low": 21.1303,
      "close": 21.1303,
      "volume": 2559,
      "datetime": 1737139920000
    },
    {
      "open": 21.1303,
      "high": 21.1303,
      "low": 21.1303,
      "close": 21.1303,
      "volume": 1500,
      "datetime": 1737139980000
    },
    {
      "open": 21.135,
      "high": 21.135,
      "low": 21.135,
      "close": 21.135,
      "volume": 5000,
      "datetime": 1737140040000
    },
    {
      "open": 21.14,
      "high": 21.1481,
      "low": 21.14,
      "close": 21.1452,
      "volume": 14058,
      "datetime": 1737140100000
    },
    {
      "open": 21.16,
      "high": 21.1794,
      "low": 21.16,
      "close": 21.1749,
      "volume": 1720,
      "datetime": 1737140160000
    },
    {
      "open": 21.175,
      "high": 21.175,
      "low": 21.155,
      "close": 21.1672,
      "volume": 5800,
      "datetime": 1737140220000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.1599,
      "close": 21.1599,
      "volume": 350,
      "datetime": 1737140280000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.15,
      "close": 21.15,
      "volume": 2728,
      "datetime": 1737140340000
    },
    {
      "open": 21.15,
      "high": 21.15,
      "low": 21.15,
      "close": 21.15,
      "volume": 300,
      "datetime": 1737140400000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.16,
      "close": 21.16,
      "volume": 592,
      "datetime": 1737140460000
    },
    {
      "open": 21.15,
      "high": 21.16,
      "low": 21.1368,
      "close": 21.16,
      "volume": 844,
      "datetime": 1737140520000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.16,
      "close": 21.16,
      "volume": 325,
      "datetime": 1737140580000
    },
    {
      "open": 21.1477,
      "high": 21.15,
      "low": 21.1477,
      "close": 21.15,
      "volume": 425,
      "datetime": 1737140640000
    },
    {
      "open": 21.16,
      "high": 21.16,
      "low": 21.15,
      "close": 21.15,
      "volume": 935,
      "datetime": 1737140700000
    },
    {
      "open": 21.1622,
      "high": 21.1622,
      "low": 21.1622,
      "close": 21.1622,
      "volume": 100,
      "datetime": 1737140760000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.17,
      "close": 21.17,
      "volume": 1676,
      "datetime": 1737140820000
    },
    {
      "open": 21.18,
      "high": 21.19,
      "low": 21.18,
      "close": 21.19,
      "volume": 4276,
      "datetime": 1737140880000
    },
    {
      "open": 21.1819,
      "high": 21.1819,
      "low": 21.16,
      "close": 21.16,
      "volume": 400,
      "datetime": 1737140940000
    },
    {
      "open": 21.1399,
      "high": 21.1399,
      "low": 21.1368,
      "close": 21.1368,
      "volume": 200,
      "datetime": 1737141000000
    },
    {
      "open": 21.1313,
      "high": 21.1399,
      "low": 21.12,
      "close": 21.125,
      "volume": 5544,
      "datetime": 1737141060000
    },
    {
      "open": 21.12,
      "high": 21.12,
      "low": 21.1029,
      "close": 21.1029,
      "volume": 3919,
      "datetime": 1737141120000
    },
    {
      "open": 21.1059,
      "high": 21.11,
      "low": 21.105,
      "close": 21.11,
      "volume": 950,
      "datetime": 1737141180000
    },
    {
      "open": 21.1024,
      "high": 21.1024,
      "low": 21.1,
      "close": 21.1,
      "volume": 19301,
      "datetime": 1737141240000
    },
    {
      "open": 21.09,
      "high": 21.095,
      "low": 21.0899,
      "close": 21.095,
      "volume": 1350,
      "datetime": 1737141300000
    },
    {
      "open": 21.1063,
      "high": 21.1063,
      "low": 21.0897,
      "close": 21.0897,
      "volume": 3100,
      "datetime": 1737141360000
    },
    {
      "open": 21.08,
      "high": 21.09,
      "low": 21.08,
      "close": 21.085,
      "volume": 2352,
      "datetime": 1737141420000
    },
    {
      "open": 21.09,
      "high": 21.09,
      "low": 21.0398,
      "close": 21.0398,
      "volume": 5064,
      "datetime": 1737141480000
    },
    {
      "open": 21.0398,
      "high": 21.04,
      "low": 21.0252,
      "close": 21.03,
      "volume": 1050,
      "datetime": 1737141540000
    },
    {
      "open": 21.03,
      "high": 21.03,
      "low": 21.0176,
      "close": 21.0176,
      "volume": 6266,
      "datetime": 1737141600000
    },
    {
      "open": 21.015,
      "high": 21.0166,
      "low": 20.9805,
      "close": 20.9887,
      "volume": 20811,
      "datetime": 1737141660000
    },
    {
      "open": 20.9857,
      "high": 21,
      "low": 20.9733,
      "close": 20.9733,
      "volume": 1165,
      "datetime": 1737141720000
    },
    {
      "open": 20.98,
      "high": 20.989,
      "low": 20.9766,
      "close": 20.989,
      "volume": 3625,
      "datetime": 1737141780000
    },
    {
      "open": 20.9877,
      "high": 20.99,
      "low": 20.9705,
      "close": 20.9705,
      "volume": 2267,
      "datetime": 1737141840000
    },
    {
      "open": 20.97,
      "high": 20.98,
      "low": 20.9404,
      "close": 20.98,
      "volume": 8091,
      "datetime": 1737141900000
    },
    {
      "open": 20.95,
      "high": 20.979,
      "low": 20.95,
      "close": 20.979,
      "volume": 775,
      "datetime": 1737141960000
    },
    {
      "open": 20.975,
      "high": 20.9914,
      "low": 20.97,
      "close": 20.9914,
      "volume": 1300,
      "datetime": 1737142020000
    },
    {
      "open": 21,
      "high": 21.025,
      "low": 20.9971,
      "close": 21.025,
      "volume": 3305,
      "datetime": 1737142080000
    },
    {
      "open": 21.03,
      "high": 21.035,
      "low": 21.025,
      "close": 21.025,
      "volume": 1225,
      "datetime": 1737142140000
    },
    {
      "open": 21.02,
      "high": 21.025,
      "low": 21.02,
      "close": 21.025,
      "volume": 1025,
      "datetime": 1737142200000
    },
    {
      "open": 21.0298,
      "high": 21.0404,
      "low": 21.0298,
      "close": 21.03,
      "volume": 14151,
      "datetime": 1737142260000
    },
    {
      "open": 21.035,
      "high": 21.0499,
      "low": 21.035,
      "close": 21.04,
      "volume": 6274,
      "datetime": 1737142320000
    },
    {
      "open": 21.0394,
      "high": 21.05,
      "low": 21.0394,
      "close": 21.05,
      "volume": 971,
      "datetime": 1737142380000
    },
    {
      "open": 21.07,
      "high": 21.07,
      "low": 21.0548,
      "close": 21.0601,
      "volume": 900,
      "datetime": 1737142440000
    },
    {
      "open": 21.075,
      "high": 21.075,
      "low": 21.0599,
      "close": 21.06,
      "volume": 1550,
      "datetime": 1737142500000
    },
    {
      "open": 21.0577,
      "high": 21.06,
      "low": 21.0577,
      "close": 21.06,
      "volume": 700,
      "datetime": 1737142560000
    },
    {
      "open": 21.075,
      "high": 21.075,
      "low": 21.06,
      "close": 21.06,
      "volume": 400,
      "datetime": 1737142620000
    },
    {
      "open": 21.05,
      "high": 21.05,
      "low": 21.03,
      "close": 21.0368,
      "volume": 1125,
      "datetime": 1737142680000
    },
    {
      "open": 21.03,
      "high": 21.03,
      "low": 21.015,
      "close": 21.03,
      "volume": 1950,
      "datetime": 1737142740000
    },
    {
      "open": 21.0265,
      "high": 21.0265,
      "low": 21.0265,
      "close": 21.0265,
      "volume": 500,
      "datetime": 1737142800000
    },
    {
      "open": 21.02,
      "high": 21.02,
      "low": 20.99,
      "close": 20.9904,
      "volume": 3845,
      "datetime": 1737142860000
    },
    {
      "open": 20.9901,
      "high": 21,
      "low": 20.9901,
      "close": 20.9931,
      "volume": 1669,
      "datetime": 1737142920000
    },
    {
      "open": 20.9803,
      "high": 20.985,
      "low": 20.9757,
      "close": 20.9757,
      "volume": 500,
      "datetime": 1737142980000
    },
    {
      "open": 20.9752,
      "high": 20.9899,
      "low": 20.975,
      "close": 20.975,
      "volume": 7129,
      "datetime": 1737143040000
    },
    {
      "open": 20.97,
      "high": 20.98,
      "low": 20.97,
      "close": 20.98,
      "volume": 1335,
      "datetime": 1737143100000
    },
    {
      "open": 20.98,
      "high": 20.98,
      "low": 20.97,
      "close": 20.9725,
      "volume": 3709,
      "datetime": 1737143160000
    },
    {
      "open": 20.97,
      "high": 20.97,
      "low": 20.97,
      "close": 20.97,
      "volume": 26119,
      "datetime": 1737143220000
    },
    {
      "open": 20.97,
      "high": 20.97,
      "low": 20.95,
      "close": 20.9587,
      "volume": 16350,
      "datetime": 1737143280000
    },
    {
      "open": 20.96,
      "high": 20.96,
      "low": 20.955,
      "close": 20.96,
      "volume": 1751,
      "datetime": 1737143340000
    },
    {
      "open": 20.965,
      "high": 20.97,
      "low": 20.96,
      "close": 20.97,
      "volume": 1335,
      "datetime": 1737143400000
    },
    {
      "open": 20.97,
      "high": 20.97,
      "low": 20.94,
      "close": 20.94,
      "volume": 2100,
      "datetime": 1737143460000
    },
    {
      "open": 20.93,
      "high": 20.935,
      "low": 20.93,
      "close": 20.93,
      "volume": 2550,
      "datetime": 1737143520000
    },
    {
      "open": 20.9491,
      "high": 20.96,
      "low": 20.9491,
      "close": 20.9567,
      "volume": 5300,
      "datetime": 1737143580000
    },
    {
      "open": 20.955,
      "high": 20.955,
      "low": 20.945,
      "close": 20.95,
      "volume": 638,
      "datetime": 1737143640000
    },
    {
      "open": 20.945,
      "high": 20.95,
      "low": 20.935,
      "close": 20.95,
      "volume": 5365,
      "datetime": 1737143700000
    },
    {
      "open": 20.9464,
      "high": 20.95,
      "low": 20.93,
      "close": 20.93,
      "volume": 1160,
      "datetime": 1737143760000
    },
    {
      "open": 20.935,
      "high": 20.945,
      "low": 20.9301,
      "close": 20.945,
      "volume": 13200,
      "datetime": 1737143820000
    },
    {
      "open": 20.945,
      "high": 20.945,
      "low": 20.9301,
      "close": 20.9339,
      "volume": 18055,
      "datetime": 1737143880000
    },
    {
      "open": 20.9361,
      "high": 20.9361,
      "low": 20.92,
      "close": 20.9287,
      "volume": 2434,
      "datetime": 1737143940000
    },
    {
      "open": 20.925,
      "high": 20.97,
      "low": 20.925,
      "close": 20.97,
      "volume": 4569,
      "datetime": 1737144000000
    },
    {
      "open": 20.97,
      "high": 20.97,
      "low": 20.95,
      "close": 20.9533,
      "volume": 5597,
      "datetime": 1737144060000
    },
    {
      "open": 20.97,
      "high": 20.97,
      "low": 20.9563,
      "close": 20.9563,
      "volume": 694,
      "datetime": 1737144120000
    },
    {
      "open": 20.96,
      "high": 20.97,
      "low": 20.9552,
      "close": 20.96,
      "volume": 4209,
      "datetime": 1737144180000
    },
    {
      "open": 20.98,
      "high": 20.995,
      "low": 20.9798,
      "close": 20.995,
      "volume": 3211,
      "datetime": 1737144240000
    },
    {
      "open": 21.005,
      "high": 21.02,
      "low": 21,
      "close": 21.02,
      "volume": 1411,
      "datetime": 1737144300000
    },
    {
      "open": 21.043635,
      "high": 21.06,
      "low": 21.04,
      "close": 21.04,
      "volume": 9417,
      "datetime": 1737144360000
    },
    {
      "open": 21.04,
      "high": 21.06,
      "low": 21.04,
      "close": 21.06,
      "volume": 4444,
      "datetime": 1737144420000
    },
    {
      "open": 21.065,
      "high": 21.07,
      "low": 21.0548,
      "close": 21.0699,
      "volume": 5525,
      "datetime": 1737144480000
    },
    {
      "open": 21.07,
      "high": 21.07,
      "low": 21.03,
      "close": 21.03,
      "volume": 2484,
      "datetime": 1737144540000
    },
    {
      "open": 21.02,
      "high": 21.02,
      "low": 20.99,
      "close": 21.01,
      "volume": 14915,
      "datetime": 1737144600000
    },
    {
      "open": 21.02,
      "high": 21.04,
      "low": 21.0134,
      "close": 21.04,
      "volume": 2743,
      "datetime": 1737144660000
    },
    {
      "open": 21.05,
      "high": 21.05,
      "low": 21.05,
      "close": 21.05,
      "volume": 483,
      "datetime": 1737144720000
    },
    {
      "open": 21.045,
      "high": 21.045,
      "low": 21.03,
      "close": 21.03,
      "volume": 1475,
      "datetime": 1737144780000
    },
    {
      "open": 21.04,
      "high": 21.06,
      "low": 21.04,
      "close": 21.04,
      "volume": 2015,
      "datetime": 1737144840000
    },
    {
      "open": 21.035,
      "high": 21.04,
      "low": 21.01,
      "close": 21.03,
      "volume": 12301,
      "datetime": 1737144900000
    },
    {
      "open": 21.03,
      "high": 21.03,
      "low": 21.02,
      "close": 21.02,
      "volume": 450,
      "datetime": 1737144960000
    },
    {
      "open": 21.04,
      "high": 21.0467,
      "low": 21.04,
      "close": 21.0467,
      "volume": 4758,
      "datetime": 1737145020000
    },
    {
      "open": 21.04,
      "high": 21.055,
      "low": 21.04,
      "close": 21.0501,
      "volume": 2875,
      "datetime": 1737145080000
    },
    {
      "open": 21.05,
      "high": 21.05,
      "low": 21.02,
      "close": 21.02,
      "volume": 2890,
      "datetime": 1737145140000
    },
    {
      "open": 21.01,
      "high": 21.03,
      "low": 21.005,
      "close": 21.03,
      "volume": 1699,
      "datetime": 1737145200000
    },
    {
      "open": 21.03,
      "high": 21.03,
      "low": 21.01,
      "close": 21.01,
      "volume": 1172,
      "datetime": 1737145260000
    },
    {
      "open": 21.04,
      "high": 21.05,
      "low": 21.035,
      "close": 21.035,
      "volume": 1222,
      "datetime": 1737145320000
    },
    {
      "open": 21.0532,
      "high": 21.055,
      "low": 21.04,
      "close": 21.04,
      "volume": 2004,
      "datetime": 1737145380000
    },
    {
      "open": 21.04,
      "high": 21.06,
      "low": 21.035,
      "close": 21.06,
      "volume": 3978,
      "datetime": 1737145440000
    },
    {
      "open": 21.07,
      "high": 21.07,
      "low": 21.0465,
      "close": 21.0465,
      "volume": 12312,
      "datetime": 1737145500000
    },
    {
      "open": 21.04,
      "high": 21.05,
      "low": 21.04,
      "close": 21.04,
      "volume": 1775,
      "datetime": 1737145560000
    },
    {
      "open": 21.04,
      "high": 21.06,
      "low": 21.04,
      "close": 21.0599,
      "volume": 3605,
      "datetime": 1737145620000
    },
    {
      "open": 21.05,
      "high": 21.06,
      "low": 21.05,
      "close": 21.0587,
      "volume": 2100,
      "datetime": 1737145680000
    },
    {
      "open": 21.065,
      "high": 21.085,
      "low": 21.065,
      "close": 21.08,
      "volume": 6664,
      "datetime": 1737145740000
    },
    {
      "open": 21.0661,
      "high": 21.0732,
      "low": 21.0661,
      "close": 21.07,
      "volume": 1150,
      "datetime": 1737145800000
    },
    {
      "open": 21.1,
      "high": 21.11,
      "low": 21.075,
      "close": 21.08,
      "volume": 26248,
      "datetime": 1737145860000
    },
    {
      "open": 21.075,
      "high": 21.1,
      "low": 21.075,
      "close": 21.1,
      "volume": 1158,
      "datetime": 1737145920000
    },
    {
      "open": 21.09,
      "high": 21.095,
      "low": 21.09,
      "close": 21.09,
      "volume": 8017,
      "datetime": 1737145980000
    },
    {
      "open": 21.085,
      "high": 21.1,
      "low": 21.075,
      "close": 21.09,
      "volume": 2633,
      "datetime": 1737146040000
    },
    {
      "open": 21.105,
      "high": 21.11,
      "low": 21.0918,
      "close": 21.11,
      "volume": 2138,
      "datetime": 1737146100000
    },
    {
      "open": 21.12,
      "high": 21.12,
      "low": 21.095,
      "close": 21.095,
      "volume": 1300,
      "datetime": 1737146160000
    },
    {
      "open": 21.11,
      "high": 21.125,
      "low": 21.1001,
      "close": 21.125,
      "volume": 4498,
      "datetime": 1737146220000
    },
    {
      "open": 21.125,
      "high": 21.125,
      "low": 21.105,
      "close": 21.11,
      "volume": 1122,
      "datetime": 1737146280000
    },
    {
      "open": 21.11,
      "high": 21.12,
      "low": 21.11,
      "close": 21.12,
      "volume": 2259,
      "datetime": 1737146340000
    },
    {
      "open": 21.1249,
      "high": 21.14,
      "low": 21.12,
      "close": 21.13,
      "volume": 3549,
      "datetime": 1737146400000
    },
    {
      "open": 21.12,
      "high": 21.13,
      "low": 21.12,
      "close": 21.12,
      "volume": 875,
      "datetime": 1737146460000
    },
    {
      "open": 21.1223,
      "high": 21.1223,
      "low": 21.1223,
      "close": 21.1223,
      "volume": 1500,
      "datetime": 1737146520000
    },
    {
      "open": 21.1599,
      "high": 21.17,
      "low": 21.155,
      "close": 21.1552,
      "volume": 3417,
      "datetime": 1737146580000
    },
    {
      "open": 21.15,
      "high": 21.16,
      "low": 21.1201,
      "close": 21.14,
      "volume": 5452,
      "datetime": 1737146640000
    },
    {
      "open": 21.1331,
      "high": 21.1402,
      "low": 21.1331,
      "close": 21.1402,
      "volume": 2015,
      "datetime": 1737146700000
    },
    {
      "open": 21.15,
      "high": 21.165,
      "low": 21.15,
      "close": 21.165,
      "volume": 1514,
      "datetime": 1737146760000
    },
    {
      "open": 21.17,
      "high": 21.18,
      "low": 21.17,
      "close": 21.1795,
      "volume": 1322,
      "datetime": 1737146820000
    },
    {
      "open": 21.1703,
      "high": 21.1703,
      "low": 21.155,
      "close": 21.1699,
      "volume": 5347,
      "datetime": 1737146880000
    },
    {
      "open": 21.16,
      "high": 21.17,
      "low": 21.16,
      "close": 21.17,
      "volume": 2471,
      "datetime": 1737146940000
    },
    {
      "open": 21.17,
      "high": 21.1713,
      "low": 21.15,
      "close": 21.17,
      "volume": 2582,
      "datetime": 1737147000000
    },
    {
      "open": 21.18,
      "high": 21.2,
      "low": 21.18,
      "close": 21.2,
      "volume": 4176,
      "datetime": 1737147060000
    },
    {
      "open": 21.19,
      "high": 21.19,
      "low": 21.17,
      "close": 21.1767,
      "volume": 4048,
      "datetime": 1737147120000
    },
    {
      "open": 21.1701,
      "high": 21.1701,
      "low": 21.1557,
      "close": 21.1701,
      "volume": 6661,
      "datetime": 1737147180000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.15,
      "close": 21.1502,
      "volume": 14713,
      "datetime": 1737147240000
    },
    {
      "open": 21.16,
      "high": 21.19,
      "low": 21.16,
      "close": 21.18,
      "volume": 2388,
      "datetime": 1737147300000
    },
    {
      "open": 21.18,
      "high": 21.22,
      "low": 21.18,
      "close": 21.22,
      "volume": 10593,
      "datetime": 1737147360000
    },
    {
      "open": 21.225,
      "high": 21.255,
      "low": 21.2226,
      "close": 21.255,
      "volume": 21301,
      "datetime": 1737147420000
    },
    {
      "open": 21.25,
      "high": 21.255,
      "low": 21.24,
      "close": 21.24,
      "volume": 17495,
      "datetime": 1737147480000
    },
    {
      "open": 21.24,
      "high": 21.245,
      "low": 21.18,
      "close": 21.21,
      "volume": 21186,
      "datetime": 1737147540000
    },
    {
      "open": 21.21,
      "high": 21.21,
      "low": 21.21,
      "close": 21.21,
      "volume": 1764,
      "datetime": 1737147600000
    },
    {
      "open": 21.2194,
      "high": 21.2194,
      "low": 21.2,
      "close": 21.2,
      "volume": 1140,
      "datetime": 1737147900000
    },
    {
      "open": 21.255,
      "high": 21.255,
      "low": 21.24,
      "close": 21.24,
      "volume": 400,
      "datetime": 1737148140000
    },
    {
      "open": 21.24,
      "high": 21.255,
      "low": 21.24,
      "close": 21.255,
      "volume": 520,
      "datetime": 1737148200000
    },
    {
      "open": 21.18,
      "high": 21.18,
      "low": 21.18,
      "close": 21.18,
      "volume": 4550,
      "datetime": 1737148260000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.17,
      "close": 21.17,
      "volume": 4701,
      "datetime": 1737148920000
    },
    {
      "open": 21.1691,
      "high": 21.1691,
      "low": 21.1691,
      "close": 21.1691,
      "volume": 100,
      "datetime": 1737149100000
    },
    {
      "open": 21.1401,
      "high": 21.1401,
      "low": 21.1401,
      "close": 21.1401,
      "volume": 1461,
      "datetime": 1737149220000
    },
    {
      "open": 21.17,
      "high": 21.17,
      "low": 21.17,
      "close": 21.17,
      "volume": 394,
      "datetime": 1737149580000
    },
    {
      "open": 21.21,
      "high": 21.21,
      "low": 21.21,
      "close": 21.21,
      "volume": 236,
      "datetime": 1737150120000
    },
    {
      "open": 21.18,
      "high": 21.18,
      "low": 21.18,
      "close": 21.18,
      "volume": 9600,
      "datetime": 1737150180000
    },
    {
      "open": 21.18,
      "high": 21.18,
      "low": 21.18,
      "close": 21.18,
      "volume": 300,
      "datetime": 1737150540000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.24,
      "close": 21.24,
      "volume": 1000,
      "datetime": 1737150660000
    },
    {
      "open": 21.2302,
      "high": 21.2302,
      "low": 21.2302,
      "close": 21.2302,
      "volume": 100,
      "datetime": 1737150720000
    },
    {
      "open": 21.2007,
      "high": 21.2007,
      "low": 21.2007,
      "close": 21.2007,
      "volume": 300,
      "datetime": 1737150960000
    },
    {
      "open": 21.2,
      "high": 21.2,
      "low": 21.2,
      "close": 21.2,
      "volume": 1599,
      "datetime": 1737151200000
    },
    {
      "open": 21.23,
      "high": 21.23,
      "low": 21.23,
      "close": 21.23,
      "volume": 10200,
      "datetime": 1737151440000
    },
    {
      "open": 21.23,
      "high": 21.23,
      "low": 21.23,
      "close": 21.23,
      "volume": 100,
      "datetime": 1737151680000
    },
    {
      "open": 21.25,
      "high": 21.25,
      "low": 21.25,
      "close": 21.25,
      "volume": 535,
      "datetime": 1737151800000
    },
    {
      "open": 21.25,
      "high": 21.25,
      "low": 21.25,
      "close": 21.25,
      "volume": 250,
      "datetime": 1737151860000
    },
    {
      "open": 21.2599,
      "high": 21.26,
      "low": 21.2599,
      "close": 21.26,
      "volume": 2990,
      "datetime": 1737151920000
    },
    {
      "open": 21.26,
      "high": 21.26,
      "low": 21.26,
      "close": 21.26,
      "volume": 3550,
      "datetime": 1737152100000
    },
    {
      "open": 21.2699,
      "high": 21.2699,
      "low": 21.2699,
      "close": 21.2699,
      "volume": 100,
      "datetime": 1737152160000
    },
    {
      "open": 21.26,
      "high": 21.26,
      "low": 21.26,
      "close": 21.26,
      "volume": 220,
      "datetime": 1737152400000
    },
    {
      "open": 21.2106,
      "high": 21.2106,
      "low": 21.2106,
      "close": 21.2106,
      "volume": 1000,
      "datetime": 1737152580000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.24,
      "close": 21.24,
      "volume": 4821,
      "datetime": 1737153660000
    },
    {
      "open": 21.2699,
      "high": 21.2699,
      "low": 21.2699,
      "close": 21.2699,
      "volume": 960,
      "datetime": 1737153780000
    },
    {
      "open": 21.27,
      "high": 21.27,
      "low": 21.27,
      "close": 21.27,
      "volume": 982,
      "datetime": 1737154080000
    },
    {
      "open": 21.27,
      "high": 21.28,
      "low": 21.27,
      "close": 21.28,
      "volume": 449,
      "datetime": 1737154380000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.24,
      "close": 21.24,
      "volume": 100,
      "datetime": 1737154620000
    },
    {
      "open": 21.3,
      "high": 21.3,
      "low": 21.3,
      "close": 21.3,
      "volume": 100,
      "datetime": 1737154860000
    },
    {
      "open": 21.243,
      "high": 21.243,
      "low": 21.243,
      "close": 21.243,
      "volume": 850,
      "datetime": 1737155400000
    },
    {
      "open": 21.3599,
      "high": 21.3599,
      "low": 21.3599,
      "close": 21.3599,
      "volume": 400,
      "datetime": 1737155520000
    },
    {
      "open": 21.32,
      "high": 21.32,
      "low": 21.32,
      "close": 21.32,
      "volume": 200,
      "datetime": 1737155700000
    },
    {
      "open": 21.27,
      "high": 21.27,
      "low": 21.27,
      "close": 21.27,
      "volume": 611,
      "datetime": 1737157200000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.24,
      "close": 21.24,
      "volume": 150,
      "datetime": 1737157860000
    },
    {
      "open": 21.24,
      "high": 21.2401,
      "low": 21.24,
      "close": 21.2401,
      "volume": 1976,
      "datetime": 1737158100000
    },
    {
      "open": 21.27,
      "high": 21.27,
      "low": 21.27,
      "close": 21.27,
      "volume": 2000,
      "datetime": 1737158580000
    },
    {
      "open": 21.25,
      "high": 21.25,
      "low": 21.25,
      "close": 21.25,
      "volume": 250,
      "datetime": 1737159180000
    },
    {
      "open": 21.24,
      "high": 21.2407,
      "low": 21.24,
      "close": 21.2401,
      "volume": 4860,
      "datetime": 1737159540000
    },
    {
      "open": 21.27,
      "high": 21.27,
      "low": 21.27,
      "close": 21.27,
      "volume": 494,
      "datetime": 1737159600000
    },
    {
      "open": 21.27,
      "high": 21.27,
      "low": 21.27,
      "close": 21.27,
      "volume": 135,
      "datetime": 1737160260000
    },
    {
      "open": 21.2403,
      "high": 21.2403,
      "low": 21.2403,
      "close": 21.2403,
      "volume": 298,
      "datetime": 1737160620000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.24,
      "close": 21.24,
      "volume": 200,
      "datetime": 1737160860000
    },
    {
      "open": 21.24,
      "high": 21.2401,
      "low": 21.24,
      "close": 21.2401,
      "volume": 200,
      "datetime": 1737160980000
    },
    {
      "open": 21.2401,
      "high": 21.2401,
      "low": 21.2401,
      "close": 21.2401,
      "volume": 4300,
      "datetime": 1737161100000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.24,
      "close": 21.24,
      "volume": 2245,
      "datetime": 1737161160000
    },
    {
      "open": 21.203,
      "high": 21.24,
      "low": 21.203,
      "close": 21.24,
      "volume": 1000,
      "datetime": 1737161640000
    },
    {
      "open": 21.203,
      "high": 21.24,
      "low": 21.203,
      "close": 21.24,
      "volume": 1000,
      "datetime": 1737161760000
    },
    {
      "open": 21.24,
      "high": 21.24,
      "low": 21.2,
      "close": 21.2,
      "volume": 600,
      "datetime": 1737161820000
    }
  ],
  "previousClose": 22.97,
  "previousCloseDate": 1735797600000,
  "symbol": "BITI",
  "empty": false
}
Response headers
 cache-control: no-store 
 content-type: application/json;charset=UTF-8 
 expires: -1 
 pragma: no-cache 
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
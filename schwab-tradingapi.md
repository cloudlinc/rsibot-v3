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
Accounts and Trading Production
Accounts and Trading Production
Specifications
Documentation
APIs to access Account Balances & Positions, to perform trading activities
Trader API - Account Access and User Preferences
 1.0.0 
OAS3
Schwab Trader API access to Account, Order entry and User Preferences

Contact Schwab Trader API team
Servers

https://api.schwabapi.com/trader/v1
Accounts


GET
/accounts/accountNumbers
Get list of account numbers and their encrypted values

Account numbers in plain text cannot be used outside of headers or request/response bodies. As the first step consumers must invoke this service to retrieve the list of plain text/encrypted value pairs, and use encrypted account values for all subsequent calls for any accountNumber request.

Parameters
No parameters

Responses
Code	Description	Links
200	
List of valid "accounts", matching the provided input parameters.

Media type

application/json
Controls Accept header.
Example Value
Schema
[
  {
    "accountNumber": "string",
    "hashValue": "string"
  }
]
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

GET
/accounts
Get linked account(s) balances and positions for the logged in user.

All the linked account information for the user logged in. The balances on these accounts are displayed by default however the positions on these accounts will be displayed based on the "positions" flag.

Parameters
Name	Description
fields
string
(query)
This allows one to determine which fields they want returned. Possible value in this String can be:
positions
Example:
fields=positions

fields
Responses
Code	Description	Links
200	
List of valid "accounts", matching the provided input parameters.

Media type

application/json
Controls Accept header.
Example Value
Schema
[
  {
    "securitiesAccount": {
      "accountNumber": "string",
      "roundTrips": 0,
      "isDayTrader": false,
      "isClosingOnlyRestricted": false,
      "pfcbFlag": false,
      "positions": [
        {
          "shortQuantity": 0,
          "averagePrice": 0,
          "currentDayProfitLoss": 0,
          "currentDayProfitLossPercentage": 0,
          "longQuantity": 0,
          "settledLongQuantity": 0,
          "settledShortQuantity": 0,
          "agedQuantity": 0,
          "instrument": {
            "cusip": "string",
            "symbol": "string",
            "description": "string",
            "instrumentId": 0,
            "netChange": 0,
            "type": "SWEEP_VEHICLE"
          },
          "marketValue": 0,
          "maintenanceRequirement": 0,
          "averageLongPrice": 0,
          "averageShortPrice": 0,
          "taxLotAverageLongPrice": 0,
          "taxLotAverageShortPrice": 0,
          "longOpenProfitLoss": 0,
          "shortOpenProfitLoss": 0,
          "previousSessionLongQuantity": 0,
          "previousSessionShortQuantity": 0,
          "currentDayCost": 0
        }
      ],
      "initialBalances": {
        "accruedInterest": 0,
        "availableFundsNonMarginableTrade": 0,
        "bondValue": 0,
        "buyingPower": 0,
        "cashBalance": 0,
        "cashAvailableForTrading": 0,
        "cashReceipts": 0,
        "dayTradingBuyingPower": 0,
        "dayTradingBuyingPowerCall": 0,
        "dayTradingEquityCall": 0,
        "equity": 0,
        "equityPercentage": 0,
        "liquidationValue": 0,
        "longMarginValue": 0,
        "longOptionMarketValue": 0,
        "longStockValue": 0,
        "maintenanceCall": 0,
        "maintenanceRequirement": 0,
        "margin": 0,
        "marginEquity": 0,
        "moneyMarketFund": 0,
        "mutualFundValue": 0,
        "regTCall": 0,
        "shortMarginValue": 0,
        "shortOptionMarketValue": 0,
        "shortStockValue": 0,
        "totalCash": 0,
        "isInCall": 0,
        "unsettledCash": 0,
        "pendingDeposits": 0,
        "marginBalance": 0,
        "shortBalance": 0,
        "accountValue": 0
      },
      "currentBalances": {
        "availableFunds": 0,
        "availableFundsNonMarginableTrade": 0,
        "buyingPower": 0,
        "buyingPowerNonMarginableTrade": 0,
        "dayTradingBuyingPower": 0,
        "dayTradingBuyingPowerCall": 0,
        "equity": 0,
        "equityPercentage": 0,
        "longMarginValue": 0,
        "maintenanceCall": 0,
        "maintenanceRequirement": 0,
        "marginBalance": 0,
        "regTCall": 0,
        "shortBalance": 0,
        "shortMarginValue": 0,
        "sma": 0,
        "isInCall": 0,
        "stockBuyingPower": 0,
        "optionBuyingPower": 0
      },
      "projectedBalances": {
        "availableFunds": 0,
        "availableFundsNonMarginableTrade": 0,
        "buyingPower": 0,
        "buyingPowerNonMarginableTrade": 0,
        "dayTradingBuyingPower": 0,
        "dayTradingBuyingPowerCall": 0,
        "equity": 0,
        "equityPercentage": 0,
        "longMarginValue": 0,
        "maintenanceCall": 0,
        "maintenanceRequirement": 0,
        "marginBalance": 0,
        "regTCall": 0,
        "shortBalance": 0,
        "shortMarginValue": 0,
        "sma": 0,
        "isInCall": 0,
        "stockBuyingPower": 0,
        "optionBuyingPower": 0
      }
    }
  }
]
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

GET
/accounts/{accountNumber}
Get a specific account balance and positions for the logged in user.

Specific account information with balances and positions. The balance information on these accounts is displayed by default but Positions will be returned based on the "positions" flag.

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
fields
string
(query)
This allows one to determine which fields they want returned. Possible values in this String can be:
positions
Example:
fields=positions

fields
Responses
Code	Description	Links
200	
A valid account, matching the provided input parameters

Media type

application/json
Controls Accept header.
Example Value
Schema
{
  "securitiesAccount": {
    "accountNumber": "string",
    "roundTrips": 0,
    "isDayTrader": false,
    "isClosingOnlyRestricted": false,
    "pfcbFlag": false,
    "positions": [
      {
        "shortQuantity": 0,
        "averagePrice": 0,
        "currentDayProfitLoss": 0,
        "currentDayProfitLossPercentage": 0,
        "longQuantity": 0,
        "settledLongQuantity": 0,
        "settledShortQuantity": 0,
        "agedQuantity": 0,
        "instrument": {
          "cusip": "string",
          "symbol": "string",
          "description": "string",
          "instrumentId": 0,
          "netChange": 0,
          "type": "SWEEP_VEHICLE"
        },
        "marketValue": 0,
        "maintenanceRequirement": 0,
        "averageLongPrice": 0,
        "averageShortPrice": 0,
        "taxLotAverageLongPrice": 0,
        "taxLotAverageShortPrice": 0,
        "longOpenProfitLoss": 0,
        "shortOpenProfitLoss": 0,
        "previousSessionLongQuantity": 0,
        "previousSessionShortQuantity": 0,
        "currentDayCost": 0
      }
    ],
    "initialBalances": {
      "accruedInterest": 0,
      "availableFundsNonMarginableTrade": 0,
      "bondValue": 0,
      "buyingPower": 0,
      "cashBalance": 0,
      "cashAvailableForTrading": 0,
      "cashReceipts": 0,
      "dayTradingBuyingPower": 0,
      "dayTradingBuyingPowerCall": 0,
      "dayTradingEquityCall": 0,
      "equity": 0,
      "equityPercentage": 0,
      "liquidationValue": 0,
      "longMarginValue": 0,
      "longOptionMarketValue": 0,
      "longStockValue": 0,
      "maintenanceCall": 0,
      "maintenanceRequirement": 0,
      "margin": 0,
      "marginEquity": 0,
      "moneyMarketFund": 0,
      "mutualFundValue": 0,
      "regTCall": 0,
      "shortMarginValue": 0,
      "shortOptionMarketValue": 0,
      "shortStockValue": 0,
      "totalCash": 0,
      "isInCall": 0,
      "unsettledCash": 0,
      "pendingDeposits": 0,
      "marginBalance": 0,
      "shortBalance": 0,
      "accountValue": 0
    },
    "currentBalances": {
      "availableFunds": 0,
      "availableFundsNonMarginableTrade": 0,
      "buyingPower": 0,
      "buyingPowerNonMarginableTrade": 0,
      "dayTradingBuyingPower": 0,
      "dayTradingBuyingPowerCall": 0,
      "equity": 0,
      "equityPercentage": 0,
      "longMarginValue": 0,
      "maintenanceCall": 0,
      "maintenanceRequirement": 0,
      "marginBalance": 0,
      "regTCall": 0,
      "shortBalance": 0,
      "shortMarginValue": 0,
      "sma": 0,
      "isInCall": 0,
      "stockBuyingPower": 0,
      "optionBuyingPower": 0
    },
    "projectedBalances": {
      "availableFunds": 0,
      "availableFundsNonMarginableTrade": 0,
      "buyingPower": 0,
      "buyingPowerNonMarginableTrade": 0,
      "dayTradingBuyingPower": 0,
      "dayTradingBuyingPowerCall": 0,
      "equity": 0,
      "equityPercentage": 0,
      "longMarginValue": 0,
      "maintenanceCall": 0,
      "maintenanceRequirement": 0,
      "marginBalance": 0,
      "regTCall": 0,
      "shortBalance": 0,
      "shortMarginValue": 0,
      "sma": 0,
      "isInCall": 0,
      "stockBuyingPower": 0,
      "optionBuyingPower": 0
    }
  }
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
Orders


GET
/accounts/{accountNumber}/orders
Get all orders for a specific account.

All orders for a specific account. Orders retrieved can be filtered based on input parameters below. Maximum date range is 1 year.

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
maxResults
integer($int64)
(query)
The max number of orders to retrieve. Default is 3000.

maxResults
fromEnteredTime *
string
(query)
Specifies that no orders entered before this time should be returned. Valid ISO-8601 formats are :
yyyy-MM-dd'T'HH:mm:ss.SSSZ Example fromEnteredTime is '2024-03-29T00:00:00.000Z'. 'toEnteredTime' must also be set.

fromEnteredTime
toEnteredTime *
string
(query)
Specifies that no orders entered after this time should be returned.Valid ISO-8601 formats are :
yyyy-MM-dd'T'HH:mm:ss.SSSZ. Example toEnteredTime is '2024-04-28T23:59:59.000Z'. 'fromEnteredTime' must also be set.

toEnteredTime
status
string
(query)
Specifies that only orders of this status should be returned.

Available values : AWAITING_PARENT_ORDER, AWAITING_CONDITION, AWAITING_STOP_CONDITION, AWAITING_MANUAL_REVIEW, ACCEPTED, AWAITING_UR_OUT, PENDING_ACTIVATION, QUEUED, WORKING, REJECTED, PENDING_CANCEL, CANCELED, PENDING_REPLACE, REPLACED, FILLED, EXPIRED, NEW, AWAITING_RELEASE_TIME, PENDING_ACKNOWLEDGEMENT, PENDING_RECALL, UNKNOWN


--
Responses
Code	Description	Links
200	
A List of orders for the account, matching the provided input parameters

Media type

application/json
Controls Accept header.
Example Value
Schema
[
  {
    "session": "NORMAL",
    "duration": "DAY",
    "orderType": "MARKET",
    "cancelTime": "2025-01-19T02:03:04.404Z",
    "complexOrderStrategyType": "NONE",
    "quantity": 0,
    "filledQuantity": 0,
    "remainingQuantity": 0,
    "requestedDestination": "INET",
    "destinationLinkName": "string",
    "releaseTime": "2025-01-19T02:03:04.404Z",
    "stopPrice": 0,
    "stopPriceLinkBasis": "MANUAL",
    "stopPriceLinkType": "VALUE",
    "stopPriceOffset": 0,
    "stopType": "STANDARD",
    "priceLinkBasis": "MANUAL",
    "priceLinkType": "VALUE",
    "price": 0,
    "taxLotMethod": "FIFO",
    "orderLegCollection": [
      {
        "orderLegType": "EQUITY",
        "legId": 0,
        "instrument": {
          "cusip": "string",
          "symbol": "string",
          "description": "string",
          "instrumentId": 0,
          "netChange": 0,
          "type": "SWEEP_VEHICLE"
        },
        "instruction": "BUY",
        "positionEffect": "OPENING",
        "quantity": 0,
        "quantityType": "ALL_SHARES",
        "divCapGains": "REINVEST",
        "toSymbol": "string"
      }
    ],
    "activationPrice": 0,
    "specialInstruction": "ALL_OR_NONE",
    "orderStrategyType": "SINGLE",
    "orderId": 0,
    "cancelable": false,
    "editable": false,
    "status": "AWAITING_PARENT_ORDER",
    "enteredTime": "2025-01-19T02:03:04.404Z",
    "closeTime": "2025-01-19T02:03:04.404Z",
    "tag": "string",
    "accountNumber": 0,
    "orderActivityCollection": [
      {
        "activityType": "EXECUTION",
        "executionType": "FILL",
        "quantity": 0,
        "orderRemainingQuantity": 0,
        "executionLegs": [
          {
            "legId": 0,
            "price": 0,
            "quantity": 0,
            "mismarkedQuantity": 0,
            "instrumentId": 0,
            "time": "2025-01-19T02:03:04.404Z"
          }
        ]
      }
    ],
    "replacingOrderCollection": [
      "string"
    ],
    "childOrderStrategies": [
      "string"
    ],
    "statusDescription": "string"
  }
]
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

POST
/accounts/{accountNumber}/orders
Place order for a specific account.

Place an order for a specific account.

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
Request body

application/json
The new Order Object.

Example Value
Schema
{
  "session": "NORMAL",
  "duration": "DAY",
  "orderType": "MARKET",
  "cancelTime": "2025-01-19T02:03:04.410Z",
  "complexOrderStrategyType": "NONE",
  "quantity": 0,
  "filledQuantity": 0,
  "remainingQuantity": 0,
  "destinationLinkName": "string",
  "releaseTime": "2025-01-19T02:03:04.410Z",
  "stopPrice": 0,
  "stopPriceLinkBasis": "MANUAL",
  "stopPriceLinkType": "VALUE",
  "stopPriceOffset": 0,
  "stopType": "STANDARD",
  "priceLinkBasis": "MANUAL",
  "priceLinkType": "VALUE",
  "price": 0,
  "taxLotMethod": "FIFO",
  "orderLegCollection": [
    {
      "orderLegType": "EQUITY",
      "legId": 0,
      "instrument": {
        "cusip": "string",
        "symbol": "string",
        "description": "string",
        "instrumentId": 0,
        "netChange": 0,
        "type": "SWEEP_VEHICLE"
      },
      "instruction": "BUY",
      "positionEffect": "OPENING",
      "quantity": 0,
      "quantityType": "ALL_SHARES",
      "divCapGains": "REINVEST",
      "toSymbol": "string"
    }
  ],
  "activationPrice": 0,
  "specialInstruction": "ALL_OR_NONE",
  "orderStrategyType": "SINGLE",
  "orderId": 0,
  "cancelable": false,
  "editable": false,
  "status": "AWAITING_PARENT_ORDER",
  "enteredTime": "2025-01-19T02:03:04.410Z",
  "closeTime": "2025-01-19T02:03:04.410Z",
  "accountNumber": 0,
  "orderActivityCollection": [
    {
      "activityType": "EXECUTION",
      "executionType": "FILL",
      "quantity": 0,
      "orderRemainingQuantity": 0,
      "executionLegs": [
        {
          "legId": 0,
          "price": 0,
          "quantity": 0,
          "mismarkedQuantity": 0,
          "instrumentId": 0,
          "time": "2025-01-19T02:03:04.410Z"
        }
      ]
    }
  ],
  "replacingOrderCollection": [
    "string"
  ],
  "childOrderStrategies": [
    "string"
  ],
  "statusDescription": "string"
}
Responses
Code	Description	Links
201	
Empty response body if an order was successfully placed/created.

Media type
Controls Accept header.
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
Location	
Link to the newly created order if order was successfully created.

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

GET
/accounts/{accountNumber}/orders/{orderId}
Get a specific order by its ID, for a specific account

Get a specific order by its ID, for a specific account

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
orderId *
integer($int64)
(path)
The ID of the order being retrieved.

orderId
Responses
Code	Description	Links
200	
An order object, matching the input parameters

Media type

application/json
Controls Accept header.
Example Value
Schema
{
  "session": "NORMAL",
  "duration": "DAY",
  "orderType": "MARKET",
  "cancelTime": "2025-01-19T02:03:04.415Z",
  "complexOrderStrategyType": "NONE",
  "quantity": 0,
  "filledQuantity": 0,
  "remainingQuantity": 0,
  "requestedDestination": "INET",
  "destinationLinkName": "string",
  "releaseTime": "2025-01-19T02:03:04.415Z",
  "stopPrice": 0,
  "stopPriceLinkBasis": "MANUAL",
  "stopPriceLinkType": "VALUE",
  "stopPriceOffset": 0,
  "stopType": "STANDARD",
  "priceLinkBasis": "MANUAL",
  "priceLinkType": "VALUE",
  "price": 0,
  "taxLotMethod": "FIFO",
  "orderLegCollection": [
    {
      "orderLegType": "EQUITY",
      "legId": 0,
      "instrument": {
        "cusip": "string",
        "symbol": "string",
        "description": "string",
        "instrumentId": 0,
        "netChange": 0,
        "type": "SWEEP_VEHICLE"
      },
      "instruction": "BUY",
      "positionEffect": "OPENING",
      "quantity": 0,
      "quantityType": "ALL_SHARES",
      "divCapGains": "REINVEST",
      "toSymbol": "string"
    }
  ],
  "activationPrice": 0,
  "specialInstruction": "ALL_OR_NONE",
  "orderStrategyType": "SINGLE",
  "orderId": 0,
  "cancelable": false,
  "editable": false,
  "status": "AWAITING_PARENT_ORDER",
  "enteredTime": "2025-01-19T02:03:04.415Z",
  "closeTime": "2025-01-19T02:03:04.415Z",
  "tag": "string",
  "accountNumber": 0,
  "orderActivityCollection": [
    {
      "activityType": "EXECUTION",
      "executionType": "FILL",
      "quantity": 0,
      "orderRemainingQuantity": 0,
      "executionLegs": [
        {
          "legId": 0,
          "price": 0,
          "quantity": 0,
          "mismarkedQuantity": 0,
          "instrumentId": 0,
          "time": "2025-01-19T02:03:04.415Z"
        }
      ]
    }
  ],
  "replacingOrderCollection": [
    "string"
  ],
  "childOrderStrategies": [
    "string"
  ],
  "statusDescription": "string"
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

DELETE
/accounts/{accountNumber}/orders/{orderId}
Cancel an order for a specific account

Cancel a specific order for a specific account

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
orderId *
integer($int64)
(path)
The ID of the order being cancelled

orderId
Responses
Code	Description	Links
200	
Empty response body if an order was successfully canceled.

Media type
Controls Accept header.
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

PUT
/accounts/{accountNumber}/orders/{orderId}
Replace order for a specific account

Replace an existing order for an account. The existing order will be replaced by the new order. Once replaced, the old order will be canceled and a new order will be created.

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
orderId *
integer($int64)
(path)
The ID of the order being retrieved.

orderId
Request body

application/json
The Order Object.

Example Value
Schema
{
  "session": "NORMAL",
  "duration": "DAY",
  "orderType": "MARKET",
  "cancelTime": "2025-01-19T02:03:04.425Z",
  "complexOrderStrategyType": "NONE",
  "quantity": 0,
  "filledQuantity": 0,
  "remainingQuantity": 0,
  "destinationLinkName": "string",
  "releaseTime": "2025-01-19T02:03:04.425Z",
  "stopPrice": 0,
  "stopPriceLinkBasis": "MANUAL",
  "stopPriceLinkType": "VALUE",
  "stopPriceOffset": 0,
  "stopType": "STANDARD",
  "priceLinkBasis": "MANUAL",
  "priceLinkType": "VALUE",
  "price": 0,
  "taxLotMethod": "FIFO",
  "orderLegCollection": [
    {
      "orderLegType": "EQUITY",
      "legId": 0,
      "instrument": {
        "cusip": "string",
        "symbol": "string",
        "description": "string",
        "instrumentId": 0,
        "netChange": 0,
        "type": "SWEEP_VEHICLE"
      },
      "instruction": "BUY",
      "positionEffect": "OPENING",
      "quantity": 0,
      "quantityType": "ALL_SHARES",
      "divCapGains": "REINVEST",
      "toSymbol": "string"
    }
  ],
  "activationPrice": 0,
  "specialInstruction": "ALL_OR_NONE",
  "orderStrategyType": "SINGLE",
  "orderId": 0,
  "cancelable": false,
  "editable": false,
  "status": "AWAITING_PARENT_ORDER",
  "enteredTime": "2025-01-19T02:03:04.425Z",
  "closeTime": "2025-01-19T02:03:04.425Z",
  "accountNumber": 0,
  "orderActivityCollection": [
    {
      "activityType": "EXECUTION",
      "executionType": "FILL",
      "quantity": 0,
      "orderRemainingQuantity": 0,
      "executionLegs": [
        {
          "legId": 0,
          "price": 0,
          "quantity": 0,
          "mismarkedQuantity": 0,
          "instrumentId": 0,
          "time": "2025-01-19T02:03:04.425Z"
        }
      ]
    }
  ],
  "replacingOrderCollection": [
    "string"
  ],
  "childOrderStrategies": [
    "string"
  ],
  "statusDescription": "string"
}
Responses
Code	Description	Links
201	
Empty response body if an order was successfully replaced/created.

Media type
Controls Accept header.
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
Location	
Link to the newly created order if order was successfully created.

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

GET
/orders
Get all orders for all accounts

Get all orders for all accounts

Parameters
Name	Description
maxResults
integer($int64)
(query)
The max number of orders to retrieve. Default is 3000.

maxResults
fromEnteredTime *
string
(query)
Specifies that no orders entered before this time should be returned. Valid ISO-8601 formats are- yyyy-MM-dd'T'HH:mm:ss.SSSZ Date must be within 60 days from today's date. 'toEnteredTime' must also be set.

fromEnteredTime
toEnteredTime *
string
(query)
Specifies that no orders entered after this time should be returned.Valid ISO-8601 formats are - yyyy-MM-dd'T'HH:mm:ss.SSSZ. 'fromEnteredTime' must also be set.

toEnteredTime
status
string
(query)
Specifies that only orders of this status should be returned.

Available values : AWAITING_PARENT_ORDER, AWAITING_CONDITION, AWAITING_STOP_CONDITION, AWAITING_MANUAL_REVIEW, ACCEPTED, AWAITING_UR_OUT, PENDING_ACTIVATION, QUEUED, WORKING, REJECTED, PENDING_CANCEL, CANCELED, PENDING_REPLACE, REPLACED, FILLED, EXPIRED, NEW, AWAITING_RELEASE_TIME, PENDING_ACKNOWLEDGEMENT, PENDING_RECALL, UNKNOWN


--
Responses
Code	Description	Links
200	
A List of orders for the specified account or if its not mentioned, for all the linked accounts, matching the provided input parameters.

Media type

application/json
Controls Accept header.
Example Value
Schema
[
  {
    "session": "NORMAL",
    "duration": "DAY",
    "orderType": "MARKET",
    "cancelTime": "2025-01-19T02:03:04.431Z",
    "complexOrderStrategyType": "NONE",
    "quantity": 0,
    "filledQuantity": 0,
    "remainingQuantity": 0,
    "requestedDestination": "INET",
    "destinationLinkName": "string",
    "releaseTime": "2025-01-19T02:03:04.431Z",
    "stopPrice": 0,
    "stopPriceLinkBasis": "MANUAL",
    "stopPriceLinkType": "VALUE",
    "stopPriceOffset": 0,
    "stopType": "STANDARD",
    "priceLinkBasis": "MANUAL",
    "priceLinkType": "VALUE",
    "price": 0,
    "taxLotMethod": "FIFO",
    "orderLegCollection": [
      {
        "orderLegType": "EQUITY",
        "legId": 0,
        "instrument": {
          "cusip": "string",
          "symbol": "string",
          "description": "string",
          "instrumentId": 0,
          "netChange": 0,
          "type": "SWEEP_VEHICLE"
        },
        "instruction": "BUY",
        "positionEffect": "OPENING",
        "quantity": 0,
        "quantityType": "ALL_SHARES",
        "divCapGains": "REINVEST",
        "toSymbol": "string"
      }
    ],
    "activationPrice": 0,
    "specialInstruction": "ALL_OR_NONE",
    "orderStrategyType": "SINGLE",
    "orderId": 0,
    "cancelable": false,
    "editable": false,
    "status": "AWAITING_PARENT_ORDER",
    "enteredTime": "2025-01-19T02:03:04.431Z",
    "closeTime": "2025-01-19T02:03:04.431Z",
    "tag": "string",
    "accountNumber": 0,
    "orderActivityCollection": [
      {
        "activityType": "EXECUTION",
        "executionType": "FILL",
        "quantity": 0,
        "orderRemainingQuantity": 0,
        "executionLegs": [
          {
            "legId": 0,
            "price": 0,
            "quantity": 0,
            "mismarkedQuantity": 0,
            "instrumentId": 0,
            "time": "2025-01-19T02:03:04.431Z"
          }
        ]
      }
    ],
    "replacingOrderCollection": [
      "string"
    ],
    "childOrderStrategies": [
      "string"
    ],
    "statusDescription": "string"
  }
]
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

POST
/accounts/{accountNumber}/previewOrder
Preview order for a specific account. **Coming Soon**.

Preview an order for a specific account.

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
Request body

application/json
The Order Object.

Example Value
Schema
{
  "orderId": 0,
  "orderStrategy": {
    "accountNumber": "string",
    "advancedOrderType": "NONE",
    "closeTime": "2025-01-19T02:03:04.437Z",
    "enteredTime": "2025-01-19T02:03:04.437Z",
    "orderBalance": {
      "orderValue": 0,
      "projectedAvailableFund": 0,
      "projectedBuyingPower": 0,
      "projectedCommission": 0
    },
    "orderStrategyType": "SINGLE",
    "orderVersion": 0,
    "session": "NORMAL",
    "status": "AWAITING_PARENT_ORDER",
    "allOrNone": true,
    "discretionary": true,
    "duration": "DAY",
    "filledQuantity": 0,
    "orderType": "MARKET",
    "orderValue": 0,
    "price": 0,
    "quantity": 0,
    "remainingQuantity": 0,
    "sellNonMarginableFirst": true,
    "settlementInstruction": "REGULAR",
    "strategy": "NONE",
    "amountIndicator": "DOLLARS",
    "orderLegs": [
      {
        "askPrice": 0,
        "bidPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "projectedCommission": 0,
        "quantity": 0,
        "finalSymbol": "string",
        "legId": 0,
        "assetType": "EQUITY",
        "instruction": "BUY"
      }
    ]
  },
  "orderValidationResult": {
    "alerts": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ],
    "accepts": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ],
    "rejects": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ],
    "reviews": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ],
    "warns": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ]
  },
  "commissionAndFee": {
    "commission": {
      "commissionLegs": [
        {
          "commissionValues": [
            {
              "value": 0,
              "type": "COMMISSION"
            }
          ]
        }
      ]
    },
    "fee": {
      "feeLegs": [
        {
          "feeValues": [
            {
              "value": 0,
              "type": "COMMISSION"
            }
          ]
        }
      ]
    },
    "trueCommission": {
      "commissionLegs": [
        {
          "commissionValues": [
            {
              "value": 0,
              "type": "COMMISSION"
            }
          ]
        }
      ]
    }
  }
}
Responses
Code	Description	Links
200	
An order object, matching the input parameters

Media type

application/json
Controls Accept header.
Example Value
Schema
{
  "orderId": 0,
  "orderStrategy": {
    "accountNumber": "string",
    "advancedOrderType": "NONE",
    "closeTime": "2025-01-19T02:03:04.439Z",
    "enteredTime": "2025-01-19T02:03:04.439Z",
    "orderBalance": {
      "orderValue": 0,
      "projectedAvailableFund": 0,
      "projectedBuyingPower": 0,
      "projectedCommission": 0
    },
    "orderStrategyType": "SINGLE",
    "orderVersion": 0,
    "session": "NORMAL",
    "status": "AWAITING_PARENT_ORDER",
    "allOrNone": true,
    "discretionary": true,
    "duration": "DAY",
    "filledQuantity": 0,
    "orderType": "MARKET",
    "orderValue": 0,
    "price": 0,
    "quantity": 0,
    "remainingQuantity": 0,
    "sellNonMarginableFirst": true,
    "settlementInstruction": "REGULAR",
    "strategy": "NONE",
    "amountIndicator": "DOLLARS",
    "orderLegs": [
      {
        "askPrice": 0,
        "bidPrice": 0,
        "lastPrice": 0,
        "markPrice": 0,
        "projectedCommission": 0,
        "quantity": 0,
        "finalSymbol": "string",
        "legId": 0,
        "assetType": "EQUITY",
        "instruction": "BUY"
      }
    ]
  },
  "orderValidationResult": {
    "alerts": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ],
    "accepts": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ],
    "rejects": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ],
    "reviews": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ],
    "warns": [
      {
        "validationRuleName": "string",
        "message": "string",
        "activityMessage": "string",
        "originalSeverity": "ACCEPT",
        "overrideName": "string",
        "overrideSeverity": "ACCEPT"
      }
    ]
  },
  "commissionAndFee": {
    "commission": {
      "commissionLegs": [
        {
          "commissionValues": [
            {
              "value": 0,
              "type": "COMMISSION"
            }
          ]
        }
      ]
    },
    "fee": {
      "feeLegs": [
        {
          "feeValues": [
            {
              "value": 0,
              "type": "COMMISSION"
            }
          ]
        }
      ]
    },
    "trueCommission": {
      "commissionLegs": [
        {
          "commissionValues": [
            {
              "value": 0,
              "type": "COMMISSION"
            }
          ]
        }
      ]
    }
  }
}
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
Transactions


GET
/accounts/{accountNumber}/transactions
Get all transactions information for a specific account.

All transactions for a specific account. Maximum number of transactions in response is 3000. Maximum date range is 1 year.

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
startDate *
string
(query)
Specifies that no transactions entered before this time should be returned. Valid ISO-8601 formats are :
yyyy-MM-dd'T'HH:mm:ss.SSSZ . Example start date is '2024-03-28T21:10:42.000Z'. The 'endDate' must also be set.

startDate
endDate *
string
(query)
Specifies that no transactions entered after this time should be returned.Valid ISO-8601 formats are :
yyyy-MM-dd'T'HH:mm:ss.SSSZ. Example start date is '2024-05-10T21:10:42.000Z'. The 'startDate' must also be set.

endDate
symbol
string
(query)
It filters all the transaction activities based on the symbol specified. NOTE: If there is any special character in the symbol, please send th encoded value.

symbol
types *
string
(query)
Specifies that only transactions of this status should be returned.

Available values : TRADE, RECEIVE_AND_DELIVER, DIVIDEND_OR_INTEREST, ACH_RECEIPT, ACH_DISBURSEMENT, CASH_RECEIPT, CASH_DISBURSEMENT, ELECTRONIC_FUND, WIRE_OUT, WIRE_IN, JOURNAL, MEMORANDUM, MARGIN_CALL, MONEY_MARKET, SMA_ADJUSTMENT


TRADE
Responses
Code	Description	Links
200	
A List of orders for the account, matching the provided input parameters

Media type

application/json
Controls Accept header.
Example Value
Schema
[
  {
    "activityId": 0,
    "time": "2025-01-19T02:03:04.446Z",
    "user": {
      "cdDomainId": "string",
      "login": "string",
      "type": "ADVISOR_USER",
      "userId": 0,
      "systemUserName": "string",
      "firstName": "string",
      "lastName": "string",
      "brokerRepCode": "string"
    },
    "description": "string",
    "accountNumber": "string",
    "type": "TRADE",
    "status": "VALID",
    "subAccount": "CASH",
    "tradeDate": "2025-01-19T02:03:04.446Z",
    "settlementDate": "2025-01-19T02:03:04.446Z",
    "positionId": 0,
    "orderId": 0,
    "netAmount": 0,
    "activityType": "ACTIVITY_CORRECTION",
    "transferItems": [
      {
        "instrument": {
          "cusip": "string",
          "symbol": "string",
          "description": "string",
          "instrumentId": 0,
          "netChange": 0,
          "type": "SWEEP_VEHICLE"
        },
        "amount": 0,
        "cost": 0,
        "price": 0,
        "feeType": "COMMISSION",
        "positionEffect": "OPENING"
      }
    ]
  }
]
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

GET
/accounts/{accountNumber}/transactions/{transactionId}
Get specific transaction information for a specific account

Get specific transaction information for a specific account

Parameters
Name	Description
accountNumber *
string
(path)
The encrypted ID of the account

accountNumber
transactionId *
integer($int64)
(path)
The ID of the transaction being retrieved.

transactionId
Responses
Code	Description	Links
200	
A List of orders for the account, matching the provided input parameters

Media type

application/json
Controls Accept header.
Example Value
Schema
[
  {
    "activityId": 0,
    "time": "2025-01-19T02:03:04.450Z",
    "user": {
      "cdDomainId": "string",
      "login": "string",
      "type": "ADVISOR_USER",
      "userId": 0,
      "systemUserName": "string",
      "firstName": "string",
      "lastName": "string",
      "brokerRepCode": "string"
    },
    "description": "string",
    "accountNumber": "string",
    "type": "TRADE",
    "status": "VALID",
    "subAccount": "CASH",
    "tradeDate": "2025-01-19T02:03:04.450Z",
    "settlementDate": "2025-01-19T02:03:04.450Z",
    "positionId": 0,
    "orderId": 0,
    "netAmount": 0,
    "activityType": "ACTIVITY_CORRECTION",
    "transferItems": [
      {
        "instrument": {
          "cusip": "string",
          "symbol": "string",
          "description": "string",
          "instrumentId": 0,
          "netChange": 0,
          "type": "SWEEP_VEHICLE"
        },
        "amount": 0,
        "cost": 0,
        "price": 0,
        "feeType": "COMMISSION",
        "positionEffect": "OPENING"
      }
    ]
  }
]
Headers:
Name	Description	Type
Schwab-Client-CorrelId	
Correlation Id. Auto generated

string
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
UserPreference


GET
/userPreference
Get user preference information for the logged in user.

Get user preference information for the logged in user.

Parameters
No parameters

Responses
Code	Description	Links
200	
List of user preference values.

Media type

application/json
Controls Accept header.
Example Value
Schema
[
  {
    "accounts": [
      {
        "accountNumber": "string",
        "primaryAccount": false,
        "type": "string",
        "nickName": "string",
        "accountColor": "string",
        "displayAcctId": "string",
        "autoPositionEffect": false
      }
    ],
    "streamerInfo": [
      {
        "streamerSocketUrl": "string",
        "schwabClientCustomerId": "string",
        "schwabClientCorrelId": "string",
        "schwabClientChannel": "string",
        "schwabClientFunctionId": "string"
      }
    ],
    "offers": [
      {
        "level2Permissions": false,
        "mktDataPermission": "string"
      }
    ]
  }
]
No links
400	
An error message indicating the validation problem with the request.

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
401	
An error message indicating either authorization token is invalid or there are no accounts the caller is allowed to view or use for trading that are registered with the provided third party application

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
403	
An error message indicating the caller is forbidden from accessing this service

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
404	
An error message indicating the resource is not found

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
500	
An error message indicating there was an unexpected server error

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links
503	
An error message indicating server has a temporary problem responding

Media type

application/json
Example Value
Schema
{
  "message": "string",
  "errors": [
    "string"
  ]
}
Headers:
Name	Description	Type
Schwab-Client-CorrelID	
Correlation Id. Auto generated

string
No links

Schemas
AccountNumberHash
session
duration
orderType
orderTypeRequest
complexOrderStrategyType
requestedDestination
stopPriceLinkBasis
stopPriceLinkType
stopPriceOffset
stopType
priceLinkBasis
priceLinkType
taxLotMethod
specialInstruction
orderStrategyType
status
amountIndicator
settlementInstruction
OrderStrategy
OrderLeg
OrderBalance
OrderValidationResult
OrderValidationDetail
APIRuleAction
CommissionAndFee
Commission
CommissionLeg
CommissionValue
Fees
FeeLeg
FeeValue
FeeType
Account
DateParam
Order
OrderRequest
PreviewOrder
OrderActivity
ExecutionLeg
Position
ServiceError
OrderLegCollection
SecuritiesAccount
SecuritiesAccountBase
MarginAccount
MarginInitialBalance
MarginBalance
CashAccount
CashInitialBalance
CashBalance
TransactionBaseInstrument
AccountsBaseInstrument
AccountsInstrument
TransactionInstrument
TransactionCashEquivalent
CollectiveInvestment
instruction
assetType
Currency
TransactionEquity
TransactionFixedIncome
Forex
Future
Index
TransactionMutualFund
TransactionOption
Product
AccountCashEquivalent
AccountEquity
AccountFixedIncome
AccountMutualFund
AccountOption
AccountAPIOptionDeliverable
TransactionAPIOptionDeliverable
apiOrderStatus
TransactionType
Transaction
UserDetails
TransferItem
UserPreference
UserPreferenceAccount
StreamerInfo
Offer
Terms Of Use
|
Privacy Notice
© 2025 Charles Schwab & Co., Inc. All rights reserved. Member SIPC. Unauthorized access is prohibited. Usage is monitored.


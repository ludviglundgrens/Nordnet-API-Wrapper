## Data fetching parameters:
- Periods: YTD, YEAR_1, YEAR_3, YEAR_5, ALL
- Resolution: WEEK, DAY, HOUR_1, MIN_1

Tough, the API will choose other resolution if it do not support the request, for example there is no support to gett MIN_1 for YEAR_5, it will instead return DAY. 
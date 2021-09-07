# Self updating gold database
Tech stack:
* python 3.8.8
* Beautifulsoup4 
* SQlite
* Pandas
* Optparser

Run main in cmd or terminal with proper flaf

## Flags:
"-r", "--read" - read gold price from web
"-l", "--loop" - print gold price every 2 sec
"-i", "--interval" - print gold pirce in defined interval
"-a", "--select_all" - sql operation select all data from data base
"-d", "--dynamic" - inserting price to data base in defined interval
"-s", "--save" - save values stored in data base to CSV file
"-q", "--query" - type any sql query
"-g", "--logprice" - another logger which store data in csv
"-p", "--polt" - plot a mean day gold price from data base


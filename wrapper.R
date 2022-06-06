fetch_hist <- function(short_name = "KAMBI", nnid = "" ,period = "YEAR_1", res="HOUR_1"){
  if(nnid == ""){
    tickers <- read.table("https://raw.githubusercontent.com/ludviglundgrens/Nordnet-API-Wrapper/master/tickers.csv", sep = ",", fill = T, header = T)
    
    nnid <- tickers$instrument_id[tickers$symbol == short_name,1]
  }
  base_url = "https://api.prod.nntech.io/market-data/price-time-series/v2/"
  period <- paste0("period/", period,"/")
  identifier <- paste0("identifier/", nnid)
  resolution = paste0("?resolution=",res)

  httr::set_config(httr::config(ssl_verifypeer = 0L))
  req <- httr::GET(paste0(base_url, period, identifier, resolution))
  #print(ifelse(http_status(req)$category == "Success", "Request worked", "Request failed"))
  c <- httr::content(req, "parsed")
  data <- c[[2]]
  df <- data.frame()
  for(i in 1:length(data)){
    datetime <- as.POSIXct(data[[i]]$timeStamp/1000, origin = "1970-01-01")
    date <- strsplit(as.character(datetime), " ")[[1]][1]
    time <- strsplit(as.character(datetime), " ")[[1]][2]
    row <- c(date, time, data[[i]]$open, data[[i]]$last, data[[i]]$high, data[[i]]$low, data[[i]]$volume)
    df <- rbind(df, row)
  }
  colnames(df) <- c("date", "time", "open", "last", "high", "low", "volume")
  return(df)
}

print_tickers <- function(short_name = "KAMBI", period = "YEAR_1", res="HOUR_1"){
  tickers <- read.table("https://raw.githubusercontent.com/ludviglundgrens/Nordnet-API-Wrapper/master/tickers.csv", sep = ";")
  colnames(tickers) <- c("id", "name", "short_name", "ISIN")
  print(tickers)
}
  



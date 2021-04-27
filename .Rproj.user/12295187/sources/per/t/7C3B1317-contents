library(readr)
dataset <- read_csv(NULL)
summary(city_temperature)

c1 <- city_temperature
max(c1$Year)
min(c1$Month)
min(c1$Year)

table(c1$Year)

us <- c1[c1$Country == 'US',]
summary(us)
install.packages("ggplot2")
library(ggplot2)
library(dplyr)
distinct(us$City) ## This didn't work
unique(us$City)
count(unique(us$City)) ## this didn't work either
summary(unique(us$City))
desc(us$City) ## didn't help



us %>%
  group_by(City)%>%
  summarise(
    count = n()
  )  ## There are 154 cities in the dataset.  

## The problem they give is this is the average temp on that given day.  We can take an average of averages......
### That might be the only way to look at it.  Not sure how many times they took the temp. 
##We could just assume once a minute
## there are 1440 minutes in a day.  
## What we need to do then is just multiple the temp by 1440 and that will give us the sum of all the temperatures for the day.  
us$sum_temp <- us$AvgTemperature*1440
View(us)
## We will need to sum up all the temperatures, by the day and divide them by days*minutes to get a more complete average.  
us2 <- us %>%
  group_by(City)%>%
  summarise(
  avg_temp = mean(AvgTemperature)
)
plot(us2)
?plot
plot(us2$City, us2$avg_temp)
summary(us2)
barplot(us2$City, us2$avg_temp)
table(us2$avg_temp)
?barplot
barplot(us2$avg_temp)
barplot(us2$avg_temp, names.arg = us2$City, las = 2)
us3 <- us2[us2$avg_temp < 80 &us2$avg_temp > 69,]
View(us3) ## us3 has warm temperatures, between 80 and 69.  

library(dplyr)

us4 <- us%>%
  mutate(seasons = case_when(Month == 6 | Month == 7 | Month == 8 ~'Summer',
                            Month == 9 | Month == 10 | Month == 11 ~ 'Fall',
                            Month == 12 | Month == 1 | Month == 2 ~ 'Winter',
                            TRUE ~ "Spring"))  ## THis breaks it into different season


View(us4)

us5 <- us4%>%
  group_by(City, State, seasons)%>%
  summarise(avg_temp = mean(AvgTemperature))


View(us5)  ## Nothing above 80 or 85 and nothing below 40 30



## cities that are within the range.  
top_20_cities_first <- us5[(us5$avg_temp < 80 & us5$seasons == 'Summer') | (us5$avg_temp > 40 & us5$seasons == 'Winter'),]
View(top_20_cities_first)


top_20_cities_second <- top_20_cities_first%>%
  group_by(City)%>%
  summarise(number_times_show = n())

top_20_cities_third <- top_20_cities_second[top_20_cities_second$number_times_show > 1,]

View(top_20_cities_third)

library(dplyr)
top_20_cities_5th <- top_20_cities_third%>%
  inner_join(us, top_20_cities_third, by = "City")
## I need to be able to inner join so that we can filter out those that 
## are outside of what we want.  



us6 <- us4%>%
  group_by(City, State, seasons)%>%
  summarise(avg_temp = mean(AvgTemperature))
## Just realized there are some values that are null in the state field

View(c1)
summary(c1)
View(top_20_cities_5th)
us_cities1 <- uscities
View(us_cities1)

library(dplyr)
cities_states <- merge(us,us_cities1,by.x = 'City', by.y='city')
View(cities_states)
cities_states$city_ascii <- NULL
cities_states$state_id <- NULL
cities_states$county_fips <- NULL
cities_states$ranking <- NULL
cities_states$id <- NULL
cities_states$incorporated <- NULL
cities_states$military <- NULL
cities_states$source <- NULL


View(cities_states)
cities_states$State <- cities_states$state_name
cities_states$state_name <- NULL
View(cities_states)



## I'm going to try and get the city if there are two with the highest population.  

library(dplyr)


cities_states <-cities_states%>%
  group_by(City)%>%
  top_n(1,population)
View(cities_states)

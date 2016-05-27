dir.create("data_assignment")
setwd("C:/Users/ajla/Documents/data_assignment")


row_capacity <- read.csv("assignment/row_capacity.csv", header = TRUE) 
tickets_sold <- read.csv("assignment/tickets_sold.csv", header = TRUE)

str(row_capacity)
str(tickets_sold)




## Total_tickets_per_week_movie_row 
## aggregate the number of individual tickets per show

my_var <- tickets_sold[c("ticket_id", "movie", "calendarweek", "auditorium_row")]
head(my_var)
ft <- ftable(auditorium_row ~ calendarweek + movie, data = my_var)
ft



## Seat_load_factor_per_week_movie_row
## divide the total tickets by the maximum capacity for that particular auditorium_row


for(i in 1:length(row_capacity$auditorium_row)){
        ft[, i] <- ft[, i]/row_capacity$max_seats_per_row[row_capacity$auditorium_row == i]
}
ft


## Seat_load_factor_per_week_row 
## use the average seat_load_factor over the individual shows per calendarweek

aggregate(Freq ~ calendarweek + auditorium_row, data = ft, FUN = mean)












# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:17:42 2016

@author: ajla
"""

import pandas as pd
import numpy as np

row_capacity = pd.read_csv("C:\\Users\\ajla\\Documents\\data_assignment\\assignment\\row_capacity.csv")
tickets_sold = pd.read_csv("C:\\Users\\ajla\\Documents\\data_assignment\\assignment\\tickets_sold.csv")




"""
Total_tickets_per_week_movie_row 
 
aggregate the number of individual tickets per show
"""

tickets = tickets_sold[['ticket_id', 'calendarweek', 'movie', 'auditorium_row']]
tickets.head(7)
grouped = tickets.groupby(['calendarweek', 'movie', 'auditorium_row'])
s = grouped.size()
s
s.sort_index(level = 'auditorium_row')




"""
Seat_load_factor_per_week_movie_row 

divide the total tickets by the maximum capacity for that particular auditorium_row
"""

frame = pd.DataFrame(s)
frame
frame = frame.reset_index(level = ['calendarweek', 'movie', 'auditorium_row'])
mycolumns = ['calendarweek', 'movie', 'auditorium_row', 'total_tickets']
frame.columns = mycolumns
frame

merged = pd.merge(frame, row_capacity, on = 'auditorium_row')
merged
merged['seat_load'] = merged['total_tickets']/merged['max_seats_per_row']
merged

final = merged[['calendarweek', 'movie', 'auditorium_row', 'seat_load']]
final


"""
Seat_load_factor_per_week_row 

use the average seat_load_factor over the individual shows per calendarweek
"""

final = final.groupby(['calendarweek', 'auditorium_row'], as_index = False).mean()
final
final = final.rename(columns ={'seat_load': 'seat_load_per_week'})
final
























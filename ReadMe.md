# Explore BikeShare Data Using Python
## by Ahmed M. Hassan

## Introduction

This project uses python to create a user-friendly script that helps explore a data set related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. The code load the data and deliver a descriptive statistics based on user-defined criteria in an interactive way. The project is part of Udacity Nano-Degree for Data Analysis.

## Dataset

 The datasets explored by this code are presented in form of flat files (i.e. comma separated values CSV). The data shows the records of bike sharing service in three major cities in the US. Each files contains six columns representing different attributes for each record in the system
 - Start Time
 - End Time
 - Trip Duration
 - Start Station
 - End Station 
 - User Type (i.e. Customer or Subscriber)
 - Gender
 - Year of Birth
 
 The last two columns are available for Chicago and New York data only. 
 
 ## Requirements
 
 It was required to explore the data to answer with some descriptive statistics for the following parameters in a specified city and/or time interval based on a user defined values. The code should provide the user with an interactive response experience. The required parameters are:
 
 
 - Most common month for travel
 - Most common day of the week for travel
 - Most common hour of the day for travel
 - Most common start station 
 - Most common end station 
 - Most common combination of start/end stations
 - Total travel time 
 - Average travel time
 - Counts of each user type
 - Counts of each gender
 - Earliest, most recent, most common year of birth 
 
 ## Code Walkthrough
 
 The code uses three python libraries (i.e. Pandas, NumPy and time). The code defines multiple function to perform different tasks to achieve the overall goal of this code.
 
 - `get_filters`: It is an interactive function the allows the user to choose which city he needs to explore its data. Also, it allows the user to set the desired filters based on the month or day of the week. The option of filtering the data can be skipped to explore the entire datase.
 - `load_data`: This function loads the data of the required data from the CSV file into Pandas DataFrame. The data in the `Start Time` column is transformed using `time` library function to produce two new columns representing the month and day of the week for each trip. The filters specified by the user are then applied if any.
 - `time_stats`, `station_stats`, `trip_duration_stats` and `user_stats` provides the required statistics using the data in the filtered dataframe for trip start/end time, trip start/end stations, trip duration and user status respectively.
 

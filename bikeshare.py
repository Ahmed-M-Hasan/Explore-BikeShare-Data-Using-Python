import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter the city name(chicago, new york city or washington): ').lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print('Invalid city name!!')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Type month name if month filter is applicable\n(Type all if not): ').lower()
        if month in ['all','january','february','march','april','may','june','july','august','september','october','november','december']:
            break
        else:
            print('Invalid month entry!!')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Type day name if day filter is applicable\n(Type all if not): ').lower()
        if day in ['all','monday','tuesday','wendesday','thrusday','friday','saturday','sunday']:
            break
        else:
            print('Invalid day entry!!')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Week Day']=df['Start Time'].dt.weekday_name

    month_dict={'january':1,
               'february':2,
               'march':3,
               'april':4,
               'may':5,
               'june':6,
               'july':7,
               'august':8,
               'september':9,
               'october':10,
               'november':11,
               'december':12}
    if month!= 'all':
        month_index = month_dict[month]
        df = df[df['Month']==month_index]
    if day != 'all':
        df = df[df['Week Day']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    months = ['january','february','march','april','may','june','july','august','september','october','november','december']

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = (df['Month'].mode()[0])-1
    print('Most common month is {}.'.format(months[common_month]))
    # TO DO: display the most common day of week
    common_day = df['Week Day'].mode()[0]
    print('Most common day is {}.'.format(common_day))
    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_hour = df['Start Hour'].mode()[0]
    print('Most common start hour is {}.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common start station is {}.'.format(common_start))
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station is {}.'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip']=df['Start Station'] + ' ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    trans_df = df[df['Trip']==common_trip]
    trip_start = trans_df['Start Station'].iloc[0]
    trip_end = trans_df['End Station'].iloc[0]
    print('The most common combination is start from ({}) and end at ({}).'.format(trip_start,trip_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time is {} second(s).'.format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time is {} second(s).'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    for index in user_count.index:
        print('There are {} of {} user(s).'.format(user_count[index],index))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count=df['Gender'].value_counts()
        for index in gender_count.index:
            print('There are {} of {} user(s).'.format(gender_count[index],index))
    else:
        print('Gender data is not available for this city!!')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        first = int(df['Birth Year'].min())
        last = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth is {}.'.format(first))
        print('Most recent year of birth is {}.'.format(last))
        print('Most common year of birth is {}.'.format(common))
    else:
        print('Year of birth data is not available for this city!!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

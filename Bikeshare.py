import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to           apply no month filter
        (str) day - name of the day of week to filter by, or "all" to       apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city,               washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter name of city, Chicago, New York city or Washington to analyze: \n> ').lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... ,       june)
    while True:
        month = input("Enter month to filter by, or 'all' to apply no month filter:  \n> ").lower()
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ...      sunday)
    while True:
        day = input("Enter the day of the week to filter by, or 'all' to apply no day filter: \n> ").lower()
        if day in days:
            break
    
    print('-'*40)
    
    return city, month, day
  
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if       applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to           apply no month filter
        (str) day - name of the day of week to filter by, or "all" to       apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month        and day
     """
    df = pd.read_csv(CITY_DATA[city])
      
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new         columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
    # use the index of the months list to get the corresponding             int
    month = months.index(month) + 1
            
    # filter by month to create the new dataframe
    df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all':
                        
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    
    return df
 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is ', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week is ', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = df.groupby(['Start Station', 'End Station']).count().idxmax()[0]
    print('Most Frequent Combination of Start and End Stations:', combination_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('Gender Stats:')
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Birth Year Data:')
    
    earliest_year = df['Birth Year'].min()
    print('Earliest Year:',earliest_year)

    most_recent_year = df['Birth Year'].max()
    print('Most Recent Year:',most_recent_year)

    most_common_year = df['Birth Year'].mode()[0]
    print('Most Common Year:',most_common_year)

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

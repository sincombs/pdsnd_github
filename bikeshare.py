import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def user_check(user_input, accepted_input):
    """
    checks user input against accepted input
    Args:
        (str) user_input - name of input
        (str list) accepted input - list of available string choices
    Returns:
        (str) user_input - correct input based on accepted inputs
    """
    while user_input not in accepted_input:
        user_input = input('Please input correct listed choice: ').lower()
        
    return user_input

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). Use a while loop to handle invalid inputs
    city = input("Input city choice (chicago, new york city, or washington): ").lower()
    accepted_cities = ['chicago', 'new york city', 'washington']
    city = user_check(city, accepted_cities)
    
    # get user input for month (all, january, february, ... , june)
    month = input("Input month (all, january, february, ... , june): ").lower()
    accepted_months = ['all','january','february','march','april','may','june']
    month= user_check(month, accepted_months)
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Input day of week (all, monday, tuesday, ... sunday): ").lower()
    accepted_day= ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = user_check(day, accepted_day)
    
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
    # load data file into a dataframe
    df = pd.read_csv(city.replace(" ","_") +".csv")
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        
        # filter by month to create the new dataframe
        df= df[df.month == month]
        #print(df)
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df= df[df.day_of_week == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month by removing NaN values and using mode
    print("Most common month: {}".format(df['month'].dropna().mode().values[0] ))

    # display the most common day of week by removing NaN values and using mode
    print("Most common day of week: {}".format(df['day_of_week'].dropna().mode().values[0]))

    # display the most common start hour by removing NaN values and using mode
    print("Most common start hour: {}".format(df['Start Time'].dt.hour.dropna().mode().values[0] ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    print("Most commonly used start station: {}".format(df['Start Station'].dropna().mode().values[0]))

    # display most commonly used end station
    print("Most commonly used end station: {}".format(df['End Station'].dropna().mode().values[0]))

    # display most frequent combination of start station and end station trip
    df['combined'] = df['Start Station'] +' and '+ df['End Station']
    print("Most common combination of start and end station trip: {}".format(df['combined'].dropna().mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('Average travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User type counts:\n {}\n'.format(df['User Type'].value_counts()) )

    # Display counts of gender
    # not all datasets include gender
    if 'Gender' in df.columns:
        print('Gender counts:\n {}\n'.format(df['Gender'].value_counts()) )
    else:
        print('No gender data available for this city')
        
    # Display earliest, most recent, and most common year of birth
    # not all datasets include birth year
    if 'Birth Year' in df.columns:
        print('Earliest, most recent, and most common birth year: {}, {}, {}'.format(df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode().values[0] ) )
    else:
        print('No birth year data available for this city')

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

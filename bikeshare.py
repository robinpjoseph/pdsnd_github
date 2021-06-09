#Packages used are time,pandas and numpy
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
        city = input("\nWhich cities data would you like to explore - Chicago,New York City or Washington?\n").lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print("\nCity not found, enter a valid city\n")
    #get user to input filter type
    filterto = input("\nDo you want to filter by month,day,both or if you want no filter type none?\n").lower()
    while filterto not in (['month','day','both','none']):
        print("\nInvalid input: Please provide a valid input.\n")
        filterto = input("\nDo you want to filter by month,day,both or if you want no filter type none?\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june']
    if filterto in ['month','both']:
        month = input("\nPlease enter the month - January, February, March, April, May or June?\n").lower()
        while month not in months:
            print("\nInvalid input:Please provide a valid month.")
            month = input("\nPlease enter the month - January, February, March, April, May or June?\n").lower()
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    if filterto in ['day','both']:
        day = input("\nPlease enter the day between Sunday till Saturday.\n").lower()
        while day not in days:
            print("\nInvalid input:Please provide a valid day.")
            day = input("\nPlease enter the day between Sunday till Saturday.\n").lower()
    else:
        day = 'all'



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
    #Load data into dataframe
    df = pd.read_csv(CITY_DATA[city])

    #Converts start time column to datetime and extracts month and day
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter for months
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # Filter for day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\nThe most common month of travel is ",df['month'].mode()[0],"\n")

    # TO DO: display the most common day of week
    print("\nThe most common day of the week is ",df['day_of_week'].mode()[0],"\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("\nThe most common start hour is ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most commonly used station to start is ",df['Start Station'].mode()[0],"\n")

    # TO DO: display most commonly used end station
    print("\nThe most commonly used station to end is ",df['End Station'].mode()[0],"\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['Frequents'] = df['Start Station']+" to "+df['End Station']
    print("\nThe most frequent combination of Station is ",df['Frequents'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\nThe total travel time is ",df['Trip Duration'].sum(),"\n")

    # TO DO: display mean travel time
    print("\nThe mean travel time is ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print("\n",user_types)

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print("\nNo gender data available for the selected city.\n")
    else:
        gend = df.groupby(['Gender'])['Gender'].count()
        print("\n",gend)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("\nBirth year data not available for the selected city.\n")
    else:
        earl_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth is",earl_birth)
        print("\nThe most year of birth is",recent_birth)
        print("\nThe most common year of birth is",common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x=1
    while True:
        alldata = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n").lower()
        if alldata == 'yes':
            print(df[x:x+5])
            x = x+5
        elif alldata == 'no':
            break
        else:
            print("\nInvalid input: Please enter a valid response.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("\nWould you like to restart? Enter 'yes' to restart or any other character to quit the program.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

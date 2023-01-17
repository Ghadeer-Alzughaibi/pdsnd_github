import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_input(input_str,input_type):
   while True:
       input_read=input(input_str)
       try:
           if input_read in ['chicago','new york city','washington'] and input_type==1:
               break
           elif input_read in ['january','february','march','april','may','june','all'] and input_type==2:
               break
           elif input_read in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and input_type==3:
               break
           else:
               if input_type==1:
                   print("wrong city")
               if input_type==2:
                   print("wrong month")
               if input_type==3:
                   print("wrong day")
        except ValueError:
            print("Sorry Error Input")
   return input_read

def get_filters():
    city=input('chicago, new york or washington',1)
    month=input('which month?',2)
    day=input('which day?',3)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df['month'].mode() [0])
    print(df['day_of_week'].mode() [0])
    print(df['hour'].mode() [0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    popular_start_station = df ['Start Station'].mode() [0]
    print('Most Start Station:', popular_start_station)

    popular_end_station = df ['End Station'].mode() [0]
    print('Most End Station:', popular_end_station)

    group_field=df.groupby(['Srart Station', 'End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print(df['Trip Duration'].sum())
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode() [0]
        print('Most Common Year:', most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:', most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)
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

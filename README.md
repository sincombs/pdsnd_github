### Date created
This project was created: 03/14/2024

# Bikeshare Data Stats

Perform key statistics of available bikeshare data.


## Description
Compute relevant statistics on bikeshare data from Chicago, New York City and Washington DC including most frequent times of travel, most popular stations and trip, trip duration,  and user stats.

## Getting Started

### Installing

* Download all relevant files:
    - `bikeshare.py`
    - `chicago.csv`
    - `washington.csv`
    - `new_york_city.csv`


### Executing program

1.  Start python script
```
python bikeshare.py
```
2. The following will be displayed the the terminal and you will be asked to supply a city:
````
$ Hello! Let's explore some US bikeshare data!
$ Input city choice (chicago, new york city, or washington):
```` 
3. After supplying a city, a month (or all months) will be asked for:
````
$ Input month (all, january, february, ... , june):
````
4. After supplying month(s), a day of the week (or all) will be required:
````
$ Input month (all, january, february, ... , june):
````
5. After displaying output, there will be a prompt asking if you would like to continue.

### Program Output 
Template output in terminal:
```
Calculating The Most Frequent Times of Travel...

Most common month: 
Most common day of week: 
Most common start hour: 

This took ______ seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...

Most commonly used start station: 
Most commonly used end station: 
Most common combination of start and end station trip: 

This took ______ seconds.
----------------------------------------

Calculating Trip Duration...

Total travel time: 
Average travel time: 

This took ______ seconds.
----------------------------------------

Calculating User Stats...

User type counts:
 User Type
Subscriber    
Customer       
Name: count, dtype: int64

Gender counts:
 Gender
Male      
Female    
Name: count, dtype: int64

Earliest, most recent, and most common birth year:   ,   , 
----------------------------------------
```
If a data column doesn't exist **no output** stats will be available.


## Authors
Stephanie Sincomb 

## Version History
* 0.1
    * Initial Release

## License
This project is licensed under the License.

## Acknowledgments
I would like to thank Udacity.
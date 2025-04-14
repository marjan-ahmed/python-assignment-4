days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

def main():
    hour_to_sec = secs_per_min * 60 # (60 * 60)
    day_to_sec = hour_to_sec * hours_per_day # (3600 * 24)
    year_to_sec = day_to_sec * days_per_year # (86400 * 365)
    print(year_to_sec)
    
    # secs_in_year = 
    
if __name__ == '__main__':
    main()
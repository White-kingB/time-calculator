def add_time(start, duration, starting_day=None):
    start_time,meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if meridian == 'PM':
        start_hour += 12
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60

    new_meridian = 'AM' if new_hour < 12 else 'PM'

    if new_hour >= 12:
        new_hour -= 12
    if new_hour == 0:
        new_hour = 12

    days_change = ""
    if starting_day is not None:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        starting_day_index = days.index(starting_day.lower().capitalize())
        new_day_index = (starting_day_index + (total_minutes // (24 * 60))) % 7

        days_change = f", {days[new_day_index]}"

    days_later = total_minutes // (24 * 60)
    days_later_text = ""
    if days_later == 1:
        days_later_text = " (next day)"
    elif days_later > 1:
        days_later_text = f" ({days_later} days later)"
    elif total_minutes == 1440:
        days_later_text = " (next day)"

    new_time = f"{new_hour}:{new_minute:02} {new_meridian}{days_change}{days_later_text}"
    return new_time

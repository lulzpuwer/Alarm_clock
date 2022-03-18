from operator import truediv


class AlarmClock:

  def __init__(self):
      self.current_time = "12:00"
      self.alarm_on = ''
      self.alarm_time = ""
      self.time_display = print(f'The curent time is {self.current_time}')

  
  def turn_alarm_on(self):
    self.alarm_on = input('would you like to turn your alarm on? y/n: ')
    if self.alarm_on == 'y':
      print('You have turn your alarm ON!')
    else:
      print('Your alarm is NOT set!')

  def set_alarm_time(self):
    if self.alarm_on == 'y':
      self.alarm_time = input(f'when would you like to set your alarm for, (current time is {self.current_time}): ')
      print(f'you have set the alarm for {self.alarm_time}')
    else:
      print('please turn the alarm on to set an alarm time!')

  def change_current_time(self):
    change_time = input(f'The current time is {self.current_time}, what would you like to change it? y/n: ')
    if change_time == 'y':
      self.current_time = input('What would you like the new time to be?: ')
      print(f'The new time is : {self.current_time}')
    else:
      print('No change to current time!')


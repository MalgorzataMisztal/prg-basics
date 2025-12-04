# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = []

   def turn_on(self):
      self.is_on = True

   def turn_off(self):
      self.is_on = False

   def set_channel(self, new_channel_no):
      self.channel_no = new_channel_no

   def set_channels(self, channels_list):
      self.channels = channels_list
      if self.channels:
         self.channel_no = 1

   def show_channels(self):
      if not self.channels:
         print('No channels available')
         return


   def show_status(self):
      if self.is_on == True:
         print(f'TV is on, channel {self.channel_no}')
      else:
         print('TV is off')
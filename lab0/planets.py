# float string -> float
# Given earth weight and planet, returns weight on provided planet
def weight_on_planets(pounds, planet):
   # write your code here
   if (planet == 'Mars'):
      return 0.38*pounds
   elif (planet == 'Jupiter'):
      return 2.34*pounds
   elif (planet == 'Venus'):
      return 0.91*pounds
   else:
      raise ValueError('Not valid planet')
   return 0.0


if __name__ == '__main__':
   pounds = 136
   print("What do you weigh on earth? 136")
   print("On Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
         "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.\n" +
          "On Venus you would weigh", weight_on_planets(pounds, 'Venus'), "pounds.");
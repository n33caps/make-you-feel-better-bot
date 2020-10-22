print("Title of program: Make you fee better bot")
print()
while True:
  description = input("Hey there, I'm Sunny, I'm here to be your friend and try to lift your mood :) So, how do you feel right now, dear hooman?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad" or "depressed":
      feelings_list.append("sad")
      encouragement_list.append("here's a virtual hug for you *hugs*, hope you feel better soon! tomorrow will be better, I promise")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("that's great! I'm so glad to hear that")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("take a break, get some rest, don't push yourself too hard. Please take care of yourself")
      counter += 1
      
    

  if counter == 0:
    
      output = "sorry! I don't really understand you at the moment. Please could you try another word? :)"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". Well, "+ encouragement_list[0] + "."  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()

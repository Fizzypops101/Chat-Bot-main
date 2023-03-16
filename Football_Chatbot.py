# welcome function
def welcome():
  print("Hello. I see you are interested in football.")
  question = input("How may I help you? ")
  if keywordSearch(question):
    return True
  else:
    print("Okay, thank you. Bye.")

# match status - to implement API
def match():
  futureMatch = input("Would you like some more information on upcoming matches? ")
  if futureMatch.lower() == "yes":
    print("Here are the upcoming 3 matches: Tottenham Vs Everton on 3rd April 2022. Tottenham Vs Brighton on 8th April 2022. Tottenham Vs Bournemouth on 15th April 2022")
    ans = input("Is there anything else I can help you with? ")
    if ans.lower() == "yes":
      previousMatch = input("Have you seen the last game? ")
      if previousMatch.lower() == "no":
        print(lastMatch())
        ans = input("Is there anything else you would like to know about? ")
        print(welcome())
    else:
      pass

# ranking status - implement API
def rankings():
  rankings = input("Would you like to know more about the ranks? ")
  if rankings.lower() == "yes":
    print("Tottenham is ranked 4th in the league table")
    print(moreInfo())
  else:
    pass

# gets the data of the last match including the score, goals
def lastMatch():
  print("For the last game. Tottenham played against Nottingham Forest on Saturday 11th March. The score was 3-1. ")
  lastGame = input("Would you like to know more information about this game? ")
  if lastGame.lower() == "yes":
    print("Harry Kane scored a goal")
  else:
    previous = input("Would you like to know more about previous matches?")
    if previous.lower() == "yes":
      dateOfMatch = input("Enter the date of the match you would like to know about in the format (DD/MM/YYYY) ")
      print("Tottenham played against Manchester United on", dateOfMatch)

# asking the user if they want to know more information or if they want to exit the chatbot
def moreInfo():
  moreInfo = input("Would you like to know any more information? ")
  if moreInfo.lower() == "yes":
    print(welcome())
  else:
    print("Okay, thank you. Bye.")
    # exit the program
      
# searches for keywords and directs them to a particular function
def keywordSearch(word):
  listOfKeywords = ["match", "player", "status", "ranking", "team", "scores", "assists"]
  if word in listOfKeywords:
    if word.lower() == "match":
      print(match())
    elif word.lower() == "ranking":
      print(rankings())
    else:
      welcome()
    

welcome()

# latest and future matches 
# most scores, assists 
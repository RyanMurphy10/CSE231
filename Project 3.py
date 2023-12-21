
print("2021 MSU Undergraduate Tuition Calculator.\n")

repeat = "yes"
while repeat == "yes":
  level = input("Enter Level as freshman, sophomore, junior, senior: ").lower()
  while level.lower() != 'freshman' and level.lower() != 'sophomore' and level.lower() != 'junior' and level.lower() != 'senior': #.lower() makes sure that the input still functions even with capitilization errors
    print("Invalid input. Try again.")
    level = input("Enter Level as freshman, sophomore, junior, senior: ") 

  college = ''

  if level.lower() == 'junior' or level.lower() == 'senior': #since level is junior or senior we can just print college rather than if they are admitted
    prompt = ("Enter college as business, engineering, health, sciences, or none: ")
    college = input (prompt).lower()
    if college != 'business' and college != 'engineering' and college != 'health' and college != 'sciences' and college != 'none':
      Prompt2 = ("Are you in the James Madison College (yes/no): ")
      if input (Prompt2).lower() == "yes":
        college = 'james madison college'

  else :
    if level.lower() =='freshman' or level.lower() == 'sophomore':
      Prompt1 = ("Are you admitted to the College of Engineering (yes/no): ")
      Prompt2 = ("Are you in the James Madison College (yes/no): ")
      if input(Prompt1).lower() == "yes":
        college = 'engineering'
      elif input (Prompt2).lower() == "yes":
        college = 'james madison college'
      else:
        college = 'none'
    
  credits = input("Credits: ")
  while credits.isnumeric() == False or float(credits) != round(float(credits)) or int(credits) == 0:
    #order for the while loop above is necessary since we want int(credits) last and float(credits) first
    print("Invalid input. Try again.")
    credits = input("Credits: ")
  credits = int(credits)
  tuition = 0

#calculations for credits and tuition below
  if credits >=1 and credits <=11:
    if level == 'freshman' :
      tuition = credits * 482
    if level == 'sophomore':
      tuition = credits * 494
    if level == 'junior':
      tuition = credits * 555
      if college == 'engineering' or college == 'business':
        tuition = credits * 573
    if level == 'senior':
      tuition = credits * 555
      if college == 'engineering' or college == 'business':
        tuition = credits * 573
  elif credits >=12 and credits <=18:
    if level == 'freshman' :
      tuition = 7230
    if level == 'sophomore':
      tuition = 7410
    if level == 'junior':
      tuition = 8,325
      if college == 'engineering' or college == 'business':
        tuition = 8595
    if level == 'senior':
      tuition = 8325
      if college == 'engineering' or college == 'business':
        tuition = 8595
  elif credits > 18:
    if level == 'freshman' :
      tuition = 7230 + (credits - 18) * 482
    if level == 'sophomore':
      tuition = 7410 + (credits - 18) * 494
    if level == 'junior':
      tuition = 8325 + (credits - 18) * 555
      if college == 'engineering' or college == 'business':
        tuition = 8595 + (credits - 18) * 573
    if level == 'senior':
      tuition = 8325 + (credits - 18) * 555
      if college == 'engineering' or college == 'business':
        tuition = 8595 + (credits - 18) * 573

  if college == 'engineering':
    if credits <= 4:
      tuition = tuition + 402
    else:
      tuition = tuition + 670
  if college == 'business':
    if credits <= 4:
      tuition = tuition + 113
    else:
      tuition = tuition + 226 
  if college == 'health':
    if credits <= 4:
      tuition = tuition + 50
    else:
      tuition = tuition + 100
  if college == 'sciences':
    if credits <= 4:
      tuition = tuition + 50
    else:
      tuition = tuition + 100

  tuition = tuition + 24
  if credits >= 6:
    tuition = tuition + 5
  if college == 'james madison college':
    tuition = tuition + 7.50


  tuition = '${:,.2f}.'.format(tuition)
  print("Tuition is " + tuition)
#necessary to format tuition correctly with a coma in thousands and two decimals
  Prompt3 = ("Do you want to do another calculation (yes/no):")
  repeat = input (Prompt3).lower()

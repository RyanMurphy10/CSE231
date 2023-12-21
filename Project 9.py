###############################################################################
# Computer project 8
#
# Lists & dictionary analysis 
#
# prompts user for .txt file and json file
#
# file output prints the data for diabetes in each region and the the countrys within the region
# The file then proceeds to print the max and minimum of each regions lowest and highest country
# After printing the max and min the file then terminates with closing statements
#
###############################################################################

import json,string

STOP_WORDS = ['a','an','the','in','on','of','is','was','am','I','me','you','and','or','not','this','that','to','with','his','hers','out','it','as','by','are','he','her','at','its']

MENU = '''
    Select from the menu:
        c: display categories
        f: find images by category
        i: find max instances of categories
        m: find max number of images of categories
        w: display the top ten words in captions
        q: quit '''

def get_option():
   '''This function prompts the user with a menu of options'''
   while True:
    print(MENU)
    menu = input("\n    Choice: ")
    while menu.lower() != "c" and menu.lower() != "f" and menu.lower() != "i" and menu.lower() != "m" and menu.lower() != "w" and menu.lower() != "q": #repeats if wrong input
      print("Incorrect choice.  Please try again.")
      print(MENU)
      menu = input("\n    Choice: ")
      menu = input("\nEnter one of the listed options: ")
    if menu.lower() == 'c':
      return "c" 
    if menu.lower() == 'f':
      return "f" 
    if menu.lower() == 'i':
      return "i"
    if menu.lower() == 'm':
      return "m" 
    if menu.lower() == 'w':
      return "w"
    elif menu.lower() == 'q':
      return "q"       
    
def open_file(s):
   '''this function continuously prompts the user for a file name and returns the file.'''
   while True: #prompts the user to input a file
      try:
        file_name = input(f"Enter a {s} file name: ") #formatted so s can represent a Json file or category
        fp = open(file_name)
        return fp
      except FileNotFoundError:
        print("File not found.  Try again.")
   return fp
        
def read_annot_file(fp1):
   '''Read the JSON file referenced by the fp1 parameter'''
   return json.load(fp1) #return json file

def read_category_file(fp2):
   '''The category file is a text file where each line is space separated.'''
   d = {} #empty string for dictionary
   for row in fp2.readlines():
     line = row.split()
     ind = int(line[0])
     val = line[1]
     d[ind] = val
   return d

def collect_catogory_set(D_annot,D_cat):
   '''This function creates a set of the categories actually used in the D_annot dictionary. The categories used are in the list under the 'bbox_category_label' key for each image'''
   s = set() #create an empty set
   
   for img in D_annot: 
     img_props = D_annot[img]
     cats = img_props["bbox_category_label"] 
     for cat in cats:
       if cat in D_cat:
         s.add(D_cat[cat])
   return s

def collect_img_list_for_categories(D_annot,D_cat,cat_set):
   '''This function creates a mapping of each category to the list of images that has an instance of that category'''
   d = {}
  
   for cat in cat_set:
     d[cat] = []
   for img in D_annot:
       img_props = D_annot[img]
       cats = img_props["bbox_category_label"]
       for cat1 in cats:
         if cat1 in D_cat and D_cat[cat1] in d:
            d[D_cat[cat1]].append(img)
            d[D_cat[cat1]].sort()      
   return d         

def max_instances_for_item(D_image):
   '''Find the most occurrences of an object (category) across all images.'''
   max = 0
   obj = "" #sets obj to empty string
   for i in D_image:
     if len(D_image[i]) > max:
       obj = i
       max = len(D_image[i])
       
   return max, obj

def max_images_for_item(D_image):
   '''This function is almost identical to max_instances_for_item. In this function, find the most images that an object (category) appears in.'''
   max = 0
   obj = ""
   for i in D_image:
     if len(set(D_image[i])) > max:
       obj = i
       max = len(set(D_image[i]))
       
   return max, obj

def count_words(D_annot):
   '''Count the occurrences of words in captions. Returns a list of tuples of words and their count of the number of occurrences across all captions.'''
   d = {}
   for img in D_annot:
     captions = D_annot[img]['cap_list']
     for caption in captions:
       for word in caption.strip().split():
         word = word.strip(string.punctuation)
         if word not in STOP_WORDS:
           if word in d:
             d[word] += 1
           else:
             d[word] = 1
   ret = [] #return list
   for item in d:
     ret.append((d[item],item))
   ret.sort(key = lambda x: (x[0],x[1]),reverse = True)
   return ret
  
def main():    
    '''This function is the starting point of the program. The program starts by opening the file and creating the two main lists then print the menu. Afterward, in an endless loop, the user is prompted for options.'''
    print("Images\n")
    fp1 = open_file("JSON image") #json open file
    fp2 = open_file("category") #category open file 
    D_annot = read_annot_file(fp1)
    D_cat = read_category_file(fp2)
    cat_set = collect_catogory_set(D_annot, D_cat)
    D_image = collect_img_list_for_categories(D_annot, D_cat, cat_set)
    options_selected = get_option()
    while options_selected != "q":
      if options_selected == "c":
        print("Categories:")
        newlist = list(cat_set)
        newlist.sort() #sorts new list alphabetically
        print(*newlist,sep = ", ")
      options_selected = get_option()
      if options_selected == "f":
        print("Categories:")
        category = input("bicycle, bottle, bowl, couch, cup, dog, microwave, oven, person, train, vase Choose a category from the list above: ")
        print("The category",category,"appears in the following images:")
      if options_selected == "i":
        print("Max instances: the category appears times in images.")
      if options_selected == "m":
        print("Max images: the category",category,"appears in",max_images_for_item(D_image),"images.")
        
      if options_selected == "w": #word count 
        word = input("Enter number of desired words: ") 
        print("\nTop",word,"words in captions.")
        print
    print("\nThank you for running my code.") #closing statement 

# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()         

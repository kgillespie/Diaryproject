import menu_system as ms
import diary as dy
import menu_system as ms
import menus as m
import sys



__curr_diary__ = None # stores current diary 
__curr_page__ = None # when set, points the current page

def DisplayDiaryEditMenu ():
  
  print("Diary Name: ", __curr_diary__.name)
  print("Owner: ", __curr_diary__.owner)
  print("Last modified: " , __curr_diary__.last_modified)
  print("Number of pages: ", __curr_diary__.get_page_count())
  print(15*"-", "Options", 15*"-")

  ms.ShowMenu("diaryEdit")
  
def CreateDiary ():
  global __curr_diary__
  diary_name = AskForDiaryName()
  print("Opening diary " + diary_name)
   # open the specified diary  
  owner_name = "Esther"
  __curr_diary__ = dy.Diary(diary_name, owner_name, True)

  DisplayDiaryEditMenu()
  
def LoadDiary ():
  global __curr_diary__
  # first we need to know the name of the diary we want to load
  diary_name = AskForDiaryName()
  print("Opening diary " + diary_name)
   # open the specified diary  
  try:
    __curr_diary__ = dy.Diary(diary_name)
    DisplayDiaryEditMenu()
  except FileNotFoundError:
    print("Diary requested was not found")
    ms.ShowMenu("topMenu")
  
    
  
def CreatePage():
  global __curr_page__
  __curr_page__ = __curr_diary__.add_blank_page()
  __curr_page__.display_page()
  ms.ShowMenu("pageEdit")


# ****************************
# Currently, the user is not able to add content.
# Whatever is entered replaces the old content. 
#TO DO: update so that the user is able to append new
# content to their entry. 
def GetPageContent():
  content  = input("Please enter content for this page:")

  global __curr_page__
  __curr_page__.text = content
  __curr_page__.display_page()
  ms.ShowMenu("diaryEdit")

  
  #LoadPage()

def SaveDiary():
  # overwrite the existing diary file with the current entries
  
  __curr_diary__.save()
  ms.ShowMenu("pageEdit")  
  


def Exit():
   ms.ShowMenu("diaryEdit")


def DeletePage():
  
  global __curr_page__
  global __curr_diary__

  #ask user for which page number to delete 
  #delete_page_requested = input("Enter page number: ")

  
  #__curr_page__ = __curr_diary__.pages[int(delete_page_requested) -1]
  
  __curr_diary__.delete_page(__curr_page__)

  
  DisplayDiaryEditMenu()

def GetIntFromUser(prompt):
  
  while True:
    
    user_request = input(prompt)
    
    try:
      intValue = int(user_request)
      return intValue;
    except:
      print("Please enter appropriate value.")

  return -1;
  
def LoadPage():
#take in user input
  #use the the page number given to load and display the page on screen
  global __curr_diary__
  global __curr_page__

  loop_flag = True;
  while loop_flag:
  
    try:
      requested_page = GetIntFromUser('Enter page number: ')
  
    
      #check to see if user input is within the min and max page values
      max_pages = __curr_diary__.get_page_count()

      if requested_page > 0 and requested_page <= max_pages:
        __curr_page__ = __curr_diary__.pages[int(requested_page) -1]
        __curr_page__.display_page()
        loop_flag = False
      else:
        
        print(f"Please enter a page number between 1 and {__curr_diary__.get_page_count()}.")

    finally:
      pass
      
     
  
  ms.ShowMenu("pageEdit")

      
def DisplayPages():
  global __curr_diary__
  #global__curr_page__
  __curr_diary__.display_diary_pages(1)
   
  ms.ShowMenu("diaryEdit")


def Reload():
  #reload page or menu options?
  ms.ShowMenu("CreateDiaryEditMenu")



def AskForDiaryName():
  diary_name = input("Please enter name of diary ")
  return diary_name  
  

def CreateDiaryEditMenu ():
  selections = { "1": "Create Page", "2": "Load page", "3":"Display Pages", "4":"Reload Diary", "5":"Save Diary"}
  # actions = { "1": HelloWorld, "2": SayGoodBye, "3":ShowMain}
  actions = {"1": CreatePage, "2": LoadPage,  "3": DisplayPages, "4": Reload, "5":SaveDiary}
  
  menu = ms.MenuStruct("Please choose an option", selections, actions)
  ms.AddMenu("diaryEdit", menu)

def CreateTopMenu():
  selections = { "1": "Load Diary", "2":"Create Diary", "3":"Exit"}
  # actions = { "1": HelloWorld, "2": SayGoodBye, "3":ShowMain}
  actions = {"1": LoadDiary, "2": CreateDiary, "3": lambda : print("Good Bye!")}
  
  menu = ms.MenuStruct("Please choose an option", selections, actions)
  ms.AddMenu("topMenu", menu)

# TODO!!!


def CreatePageEditMenu():
  selections = { "1": "Edit Content", "2":"Delete Page", "3":"Exit"}
  actions = {"1": GetPageContent, "3":Exit, "2": DeletePage}
  menu = ms.MenuStruct("Please choose an option", selections, actions)
  ms.AddMenu("pageEdit", menu)

CreateTopMenu()
CreateDiaryEditMenu()
CreatePageEditMenu()



#work on loading new diary - should be able to create a text file like my_diary that stores entries or delete option and have user enter new entries. Users could have an option to reset and delete current diary and start over.
#Create action for save page
#Review edit content action - the edited content should be saved in the my_diary file
#create method for Reload 
#The DisplayPages() does not display the recently saved pages.
#The SavePage() method saves diary entries into the my_diary.txt file

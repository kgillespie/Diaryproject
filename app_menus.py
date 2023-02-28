import menu_system as ms
import diary as dy
import menu_system as ms
import menus as m

__curr_diary__ = None
__curr_page__ = None

def DisplayDiaryEditMenu ():
  
  print("Diary Name: ", __curr_diary__.name)
  print("Owner: ", __curr_diary__.owner)
  print("Last modified: " , __curr_diary__.last_modified)
  print("Number of pages: ", __curr_diary__.get_page_count())
  print(15*"-", "Options", 15*"-")

  ms.ShowMenu("diaryEdit")
  
def LoadDiary ():
  global __curr_diary__
  # first we need to know the name of the diary we want to load
  diary_name = AskForDiaryName()
  print("Opening diary " + diary_name)

  # open the specified diary
  __curr_diary__ = dy.Diary(diary_name)
  
  DisplayDiaryEditMenu()
  
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
  
  DisplayPage()


def SavePage():
  pass 
  #touch text.txt
  
  #python3 write.py
  #Open the text.txt file for writing.
  file1 = open('text.txt', 'w')
  #Write the contents of the diary to the     text.txt file
  file1.write(" ")
  #Close the text.txt file
  file1.close()
    
  ms.ShowMenu("diaryEdit")  
  #   - store in the page
  #   - reload page edit ("pageEdit") menu
  # 2. Save Page
    
  # 3. Exit -- return user to previous (diaryEdit) menu

def Exit():
   ms.ShowMenu("diaryEdit")


def DeletePage():
  # Make corrections using global variables
  # Make sure there is a current page to delete before 
  # trying to delete
  global __curr_page__
  __curr_page__.delete_page()
  for __curr_page__ in __curr_diary__:
    __curr_page__ = None
    if __curr_page__ < [0]:
      delete_pg_error = print("No page available to delete.")
      return delete_pg_error
     
#if no page available to delete, __curr_diary__ = None
#no_page_available = print("No page available to delete")
  
def DisplayPage():
  # global __curr_page__
  __curr_page__.display_page()
  ms.ShowMenu("pageEdit")

def Reload():
  #reload page or menu options?
  ms.ShowMenu("CreateDiaryEditMenu")



def AskForDiaryName():
  diary_name = input("Please enter name of diary ")
  return diary_name  

def CreateDiaryEditMenu ():
  selections = { "1": "Create Page", "2":"Delete Page", "3":"Display Page", "4":"Reload"}
  # actions = { "1": HelloWorld, "2": SayGoodBye, "3":ShowMain}
  actions = {"1": CreatePage, "2": DeletePage, "3": DisplayPage, "4": Reload}
  
  menu = ms.MenuStruct("Please choose an option", selections, actions)
  ms.AddMenu("diaryEdit", menu)

def CreateTopMenu():
  selections = { "1": "Load Diary", "2":"Create Diary", "3":"Exit"}
  # actions = { "1": HelloWorld, "2": SayGoodBye, "3":ShowMain}
  actions = {"1": LoadDiary, "2": LoadDiary, "3": lambda : print("Good Bye!")}
  
  menu = ms.MenuStruct("Please choose an option", selections, actions)
  ms.AddMenu("topMenu", menu)

# TODO!!!


def CreatePageEditMenu():
  selections = { "1": "Edit Content", "2":"Save Page", "3":"Exit"}
  actions = {"1": GetPageContent, "2":SavePage, "3":Exit}
  menu = ms.MenuStruct("Please choose an option", selections, actions)
  ms.AddMenu("pageEdit", menu)

CreateTopMenu()
CreateDiaryEditMenu()
CreatePageEditMenu()
import sys as sys
import time as tm
import diary as d


print(30*"-", "Welcome to the Diary Manager", 30*"-")
tm.sleep(1)

def load_main_menu():
  choice = input ("""

                      Please make a selection from one of the following menu options:
                      1. Load Diary
                      2. Create New Diary
                      3. Exit

""")
  #loop = True
  #while True:
  if choice == "1":
    print("You have selected option 1")
    #load page if user creating a new diary
    #reload saved diary if user wants to use diary that was already created
    load_diary = input("To open a new diary enter the letter a otherwise enter the letter b to continue where you left off: ")
    #while choice not in ("A","a","B","b"):
      #print ("You typed something wrong! Please enter a or b to continue. ")
      #load_diary = input("To open a new diary enter the letter a otherwise enter the letter b to continue where you left off: ")

    if load_diary == "a" or load_diary == "A":
      #add page to new diary
      d.add_page()
    elif load_diary == "b" or load_diary == "B":
      #load last page in diary
      d.retrieve_page()
    else:
      print ("You typed something wrong! Please enter a or b to continue. ")

  elif choice == "2":
    print("You have selected option 2")
    diaryname = input("Please enter a name for the new dairy!  ")
    oname = input("Please enter your name:")
    new_diary = create_new_diary(diaryname, oname)
    print("Created diary with name ", new_diary.name)
    load_diary_page_menu(new_diary)
    
   

  elif choice == "3":
    print("You have selected option 3")
    # Esther, the following line was indented to 
    # the left, which ended the elif block on 
    # line 25. This resulted in the issue with 
    # the next "else" statement which was no 
    # longer connected to the other if elif 
    # statements  
    print("Now closing diary...")
  #break
  else:
    print("Wrong option selected. Please enter select from options 1 - 3")



def create_new_diary(name, oname):
  
  #once the 
  diary = d.Diary(name, oname)
  return diary

def load_diary_page_menu (diary):
  print("Diary Name: ", diary.name)
  print("Owner: ", diary.owner)
  print("Last modified: " , diary.last_modified)
  print("Number of pages: ", diary.get_page_count())
  print(15*"-", "Options", 15*"-")
  
  option = input ("""

                      Please make a selection from one of the following options:
                      1. Create New Page
                      2. Display Page(s)
                      3. Create Pages(s)
                      4. Save
                      5. Reload

""")
  
  if option == "1":
    print("You have selected option 1")
    # create a new page
    page = diary.add_blank_page()

    page.display_page()
    
    # To Do: create a "load_page_edit_menu(page)"
    # Give user the option to: 
    # 1) change title, e.g. page.title = input("Please provide new title")
    # 2) change content,
    # 3)exit page edit menu (which should take them to the previous menu)
    # Each time user edits the title or content, display current page and
    # reload the "load_page_edit_menu(page)"

  elif option == "2":
    print("You have selected option 2") 
   
  elif option == "3":
    print("You have selected option 3")
    d.add_page

  elif option == '4':
    print("Now saving diary...")
    #break
  else:
    pass
    #reload menu or ?



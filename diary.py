# defines the Diary related classes - NOT diary
# management routines

from datetime import datetime
  
class Diary:
  name = ""
  pages = [] # empty list for storing pages
  owner = ""
  # cover = ""
  # TOC
  created_date = "" # set to time
  last_modified = "" 
  # number of pages
  
  def __init__(self, diary_name, owner_name = "Esther" ):
    self.name = diary_name
    self.owner = owner_name
    # open up the diary file that already exists, and load the 
    # pages into memory or else create a new diary file: name + ".txt"
    filename = diary_name + ".txt"


  def get_page_count(self):
    return len(self.pages)

  def retrieve_page(self, page_num):
    return self.pages[page_num - 1]


  def add_blank_page(self):
    # create a new page
    title = input("Please enter diary title: ")
    page = DiaryPage(title, "<No Content>")

    #add page to collection 
    return self.add_page(page)
   

    
  def add_page(self, page):
    self.pages.append(page)
    return page

  # delete the page specified
  def delete_page(self, del_page):
    
    page_num = 0
    for page in self.pages:
      # we will assume that the titles are unique
      if (page.title == del_page.title):
        self.pages.pop(page_num)
        return True

    # if we reach this point, it means that the page 
    # being deleted is not in this diary
    # We return false
    return False
     

  # display the pages of the diary from the starting location
  # to the end location with a maximum of pages displayed. 
  # end = -1 means go to the end
  # max = -1 include all pages
  def display_diary_pages(self, start_page, end_page, max=-1):
    #implement support for max and main program should show
    #that max is working properly
    
    start_index = start_page - 1
    end_index = end_page
    curr_page_num = start_page
    page_counter = 0
    for x in self.pages[start_index:end_index]:

      print(f"---------------{curr_page_num}---------------")
      x.display_page()
      curr_page_num +=1

      if max := -1:
        #check to see if we have reach out max
        if page_counter == max:
          return

  # [On Hold] search and returns pages containing the 
  # search text
  def search_by_text(self, search_text):
    pass

  # [On Hold] search and returns pages based on the 
  # provided date
  def search_by_date(self, date):
    return self.creation_date(date)


  
  
class DiaryPage:
  title = ""
  text = ""
  creation_date = datetime.now()
  
  def __init__(self, title, text):
    self.title = title
    self.text = text
    #self.creation_date = datetime.now()
    #implement timezone

  
  def display_page(self):
    print("Title =" + self.title)
    print(self.creation_date.strftime("%m/%d/%Y, %H:%M"))
    print("------------------------------------------------")
    print(self.text)
    print("------------------------------------------------")
    
    


# ModuleNotFoundError
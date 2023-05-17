# defines the Diary related classes - NOT diary
# management routines
# Need to make updates
# Author Kevin G
# Esther Mukuye
# Make a change in Replit Repo

from datetime import datetime

page_record_identifier = "page:"
diary_record_identifier = "diary:"

class Diary:
  name = ""
  pages = []  # empty list for storing pages

  owner = ""
  # cover = ""
  # TOC
  created_date = ""  # set to time
  last_modified = ""

  # number of pages

  
  def __init__(self, diary_name, owner_name="", create_new=False):
    
    
    # open up the diary file that already exists, and load the
    # pages into memory or else create a new diary file: name + ".txt"
    filename = diary_name + ".txt"

    if (create_new):
      self.name = diary_name
      self.owner = owner_name
      self.created_date = " "
      self.last_modified = " "
      
    else:
      # load existing; if does not exist, it will throw and 
      # Exception
        
      # print("The diary requested does not exist.")
      # Correction 6a:
      # we are looking for an existing file
      # ToDO: use try block to test whether the file exists and if not, display message....
      
      file = open(filename, 'r')
      
      diary_info = file.readline().split(":")
      if (diary_info[0] == "diary"):
        # self.name = diary_info[1]
        self.owner = diary_info[2]
        self.created_date = diary_info[3]
        self.last_modified = diary_info[4]
  
      # read the remaining lines and load those pages into our
      # in memory diary object
      for eachline in file:
        next_entry = eachline.split(":")
        if (next_entry[0] == "page"):
          # create/load the page into the diary
          self.pages.append(
            DiaryPage(next_entry[1], next_entry[2], next_entry[3]))

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
  def display_diary_pages(self, start_page, end_page=-1, max=-1):
    #implement support for max and main program should show
    #that max is working properly

    start_index = start_page - 1
    end_index = end_page 
    if end_index == -1 :
      end_index = len(self.pages) 

    
    curr_page_num = start_page
    page_counter = 0
    for x in self.pages[start_index:end_index]:

      print(f"---------------{curr_page_num}---------------")
      x.display_page()
      curr_page_num += 1

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

  def save(self):
    # this method needs to create the diary file 
    # using the current diary data (diary info) 
    # and each page

    file = open(self.name + '.txt', 'w')

    # create the diary entry 
    file.write(diary_record_identifier + ":" + self.name + ":" + self.owner + ":" + self.created_date + ":" + self.last_modified + ":")

    # loop through all of the entries and write them 
    # to the file
    for page in  self.pages:
  
      # then create each page entry  (which will
      # require you to loop through the diary.pages list )
      
      # add diary entries to text file and close file
      diary_page_entry = "\n" + page_record_identifier + page.title + ":" + page.text + ":" + str(page.creation_date) + ":" 
    
      file.write(diary_page_entry)
    
    file.close()
    
  #   - store in the page
  #   - reload page edit ("pageEdit") menu
  # 2. Save Page
    
  # 3. Exit -- return user to previous (diaryEdit) menu


class DiaryPage:
  title = ""
  text = ""
  creation_date = ""; 

  def __init__(self, title, text, date = ""):
    self.title = title
    self.text = text
    self.creation_date = date
    if date == "":
      self.creation_date = datetime.now().strftime("%m/%d/%Y, %H:%M")

  def display_page(self):
    print("Title =" + self.title)
    print(self.creation_date)
    print("------------------------------------------------")
    print(self.text)
    print("------------------------------------------------")


# ModuleNotFoundError

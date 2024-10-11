#!/usr/bin/env python3

class Book:
    def __init__(self,title="Sky Waring",page_count = 240):
        self.title = title
        self._page_count = page_count
    
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self,page_count):
        if(isinstance(page_count,int)):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    #page_count = property(get_page_count,set_page_count)
    
        
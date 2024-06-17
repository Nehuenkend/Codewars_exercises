import math

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.num_items = len(collection)
        self.items_per_page = items_per_page
        self.num_pages = math.ceil(len(collection) / items_per_page)
        
    # returns the number of items within the entire collection
    def item_count(self):
        return self.num_items
    
    # returns the number of pages
    def page_count(self):
        return self.num_pages
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if self.num_pages == 0 or page_index < 0:
            return -1
        if (page_index+1) * self.items_per_page <= self.num_items:
            return self.items_per_page 
        if page_index*self.items_per_page<self.num_items and (page_index+1) * self.items_per_page > self.num_items:
            return self.item_count()%self.items_per_page
        return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.num_items:
            return -1
        return math.floor(item_index / self.items_per_page)

'''
Created on 18 Feb 2021

@author: Adam
'''
class Tag():
    
    def __inti__(self, name, contents):
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'
        self.contents = contents
        
    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"
    
    def display(self):
        print(self)
       
       
class DocType(Tag):
    
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = '' #DOCTYPE dose not have a end tag
        
        
class Head(Tag):
    
    def __init__(self):
        super().__init__('head', '')
    
        
class Body(Tag):
    
    def __init__(self):
        super().__init__('body', '') #body contents will be built up separately
        self._body_contentes = []
        
    def add_tag(self,name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)
        
        
    def display(self):
        for tag in self._body_contentes:
            self.contents += str(tag)
            
        super().display()
        
        
        
        
        
        
        
        
        
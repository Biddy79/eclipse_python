'''
Created on 18 Feb 2021

@author: Adam
'''
class Tag():
    
    def __init__(self, name, contents):
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'
        self.contents = contents
        
    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"
    
    def display(self, file=None):
        print(self, file=file)
       
       
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
        #new_tag object of Tag class
        new_tag = Tag(name, contents)
        self._body_contentes.append(new_tag)
        
    #overwrites display method in Tag class!! 
    def display(self, file=None):
        for tag in self._body_contentes:
            self.contents += str(tag)
            
        super().display(file=file)
        
#Using composition here
#Composition is when a Class contains instances objects from an other Class
class HtmlDoc():
    
    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()
        
    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)
    
    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)
        
if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_tag('h1', 'main heading')
    my_page.add_tag('h2', 'sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    my_page.display()

    
    
        
        
        
        
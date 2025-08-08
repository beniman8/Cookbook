

from dataclasses import dataclass

@dataclass(frozen=True)
class HTMLPage:
    title:str
    metadata:dict[str,str]
    body:str
    
    
    def _render_metadata(self):
        
        return"\n".join(f'<meta name="{name}" content="{value}"' for name,value in self.metadata.items())
    
    
    def render(self) -> str:
        return f"""   
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{self.title}</title>
                </head>
                <body>
                    {self.body}
                </body>
                </html>
    
    
                    """


class HTMLBuilder:
    def __init__(self):
        self.title = "" 
        self.metadata= {}
        self.body_content = [] 
        
    def add_metadata(self,name,content):
        self.metadata[name] = content
        
        return self
        
    def add_title(self,title):
        self.title = title
        
        return self
    
    def add_button(self,label,onclick):
        self.body_content.append(f"<button onclick=\"location.href='{onclick}'\">{label}</button>")
        return self
        
    def add_heading(self,text,level):
        self.body_content.append(f"<h{level}>{text}</h{level}")
        
        return self
    def add_paragraph(self,text): 
        self.body_content.append(f"<p>{text}</p>")
        
        return self 
    def build(self):
        body = "\n".join(self.body_content)
        return HTMLPage(title=self.title,body=body,metadata={'website':'cool'})
        
    

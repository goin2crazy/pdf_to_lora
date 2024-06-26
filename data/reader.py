import fitz 
from typing import Callable

class Document():   
    def __init__(self, path: str = "/") -> None : 
        self.path = path
        self.doc = fitz.open(path)

    def prepare_text(self, text) -> str: 
        """"
        Write there text preparetion process u need 

        It have to look take 'text': str to input and return the output 'text': str

        """

        return text

    def __getitem__(self, idx) -> str: 
        try: 
            page = self.doc.load_page(idx)
            text = page.get_text() 
        except: 
            text = ''

        return self.prepare_text(text)

    def __len__(self) -> int: 
        return len(self.doc)
    
    def __str__(self) -> str:
        return f"Document from {self.path}, first page [{self[0]}]"
    
    def read_all(self, progressbar =True): 

        if progressbar == True: 
            from tqdm import tqdm

            text = ""
            for i in tqdm(range(len(self))): 
                text += self[i]
        else: 
            text = ""
            for i in range(self): 
                text += self[i]
        return text

    def to_txt(self, save_path: str, progressbar =False):
        text = self.read_all( progressbar)

        with open(save_path, 'w', encoding='utf-8') as f: 
            f.write(text)
            f.close()

def document(doc_path, prep_fn:Callable=None) -> Document: 

    class d(Document): 
        def __init__(self, *args, **kwargs): 
            super().__init__(*args, **kwargs)

        def prepare_text(self, text): 

            text:str = prep_fn(text)

            return text

    return d(doc_path)
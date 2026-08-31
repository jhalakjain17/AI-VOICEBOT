from langchain_community.document_loaders import PyPDFLoader

class PDFReader:
    '''
    this class is responsible for loading the pdf files and return the langchain document object.
    to use:

    reader=PDFReader('path/to/pdf/abc.pdf')
    reader.load_pdf()
    '''

    def __init__(self,pdf_path):
        self.pdf_path=pdf_path


    def load_pdf(self):
        '''
        
        this will load the pdf into the memory and return the list of documents and objects
        '''    
        loader=PyPDFLoader(self.pdf_path)
        documents=loader.load()
        return documents
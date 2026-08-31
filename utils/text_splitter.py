from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextSplitter:
    '''
    
    it splits langchain document opbject into,
    small overlapping chuks(chunks_overlap>0)'''

    def __init__(self,chunk_size:int=1000,chunk_overlap:int=200):
        self.splitter=RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap


        )
    def split_documents(self,documents):
        '''
        
        split the documents convert into chunks'''    

        return self.splitter.split_documents(documents)
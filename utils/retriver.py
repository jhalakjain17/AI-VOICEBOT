class Retriver:
    '''
    
    resposible for retriving the most relevant chunks from 
    vector db '''

    def __init__(self,vector_db):
        self.vector_db=vector_db 

    def retrieve(self,query,k=3):
        '''
        k top relevant chunks or nodes.'''      
        documents = self.vector_db.similarity_search(
            query=query,
            k=k
        )
        return documents


    
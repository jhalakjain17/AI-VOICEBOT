class ContextBuilder:
    '''
    convrted the retrived documents object into sigle context using  string
    
    '''
    @staticmethod
    def build(documents,property=None):
        context=""

        for document in documents:
            context=context+document.page_content

            if property!=None:
                context= context +document.metadata[property]
            context=context + "\n\n"

        return context.strip()        
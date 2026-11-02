from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import Language

from langchain_community.document_loaders import PyPDFLoader

Language="""
asdlkfjksaljfkl;ajkf;j

"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,

)

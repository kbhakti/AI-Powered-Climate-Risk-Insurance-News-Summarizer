from langchain.text_splitter import CharacterTextSplitter

def split_text(text):
    splitter = CharacterTextSplitter(separator=". ", chunk_size=3500, chunk_overlap=50)
    return splitter.split_text(text)
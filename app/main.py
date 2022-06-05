
from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import WitDemo

demo = WitDemo()

class Text(BaseModel):
    text: str
app = FastAPI()
   
    
@app.get("/")
def initialize():
    return {
        "Message": "Successfully Initialized."
    }

@app.post("/extract")
def root(
    text: Text,
):
    return demo.frame(text.text)     

    
# if __name__ == '__main__':
#     demo = WitDemo()
#     message = "Saan ako pwede magdeposit?"
#     result = demo.frame(message)
#     print(result)

from fastapi import FastAPI, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import aiofiles
import pandas as pd
#install python-multipart
import aiofiles
app = FastAPI()



@app.post("/submit")
async def submit(imgfile :UploadFile = Form(),
    name:str = Form(), post : str = Form(),
    email :str = Form(),contact:str =Form(), fb :str = Form(),
    ld : str = Form() ):

    print(name,email,ld)
    async with aiofiles.open("image/"+email+".png","wb") as f:
           i = 0
           size = 1024 *50
           while content := await imgfile.read(size):
                await f.write(content)
                i=i+1
    
    df = pd.read_csv("db.csv")
    img = "image/"+email+".png"
    df.loc[len(df.index)] = [name, post, email, img, fb, ld, contact ]
    
    df.to_csv("db.csv",index=False)
    
    
    return HTMLResponse("submitted")
    
@app.get("/")
def redirect():
    return RedirectResponse("/index.html")
    
app.mount("/", StaticFiles(directory="web"), name="websites")
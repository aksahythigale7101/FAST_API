from fastapi import FastAPI, BackgroundTasks

app = FastAPI()


def send_email(email: str):
    print(f"Email ID:{email}")

def write_log(log: str):
    print(f"log print success:{log}")

@app.post("/register")
async def Get_Data(email: str,log:str, background_Task: BackgroundTasks):
    background_Task.add_task(send_email, email)
    background_Task.add_task(write_log, log)
    return {"message": "User registered successfully"}
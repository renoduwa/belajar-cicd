from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # Simulasi endpoint API yang mengembalikan data JSON
    return {"status": "success", "message": "Sistem Web Aktif"}
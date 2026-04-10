import uvicorn
from fastapi import FastAPI, Depends
from app.core.security import verify_token
from app.api.routes import recus, ajoutes
from app.db.base import Base
from app.db.session import engine

app = FastAPI(
    dependencies=[Depends(verify_token)]
    )

app.include_router(recus.router, prefix="/recus")
app.include_router(ajoutes.router, prefix="/ajoutes")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8789, reload=True)

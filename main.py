from fastapi import FastAPI, Request
from waf import waf_check
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

app = FastAPI(title="WAF Simulator API")
DATABASE_URL = "sqlite:///logs.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    payload = Column(String)
    result = Column(String)

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

@app.post("/waf/check")
async def waf_check_endpoint(request: Request):
    data = await request.json()
    payload = data.get("payload", "")
    result = waf_check(payload)
    # Log to DB
    db = SessionLocal()
    log = Log(payload=payload, result=result or "Normal")
    db.add(log)
    db.commit()
    db.close()
    return {"payload": payload, "result": result or "Normal"}
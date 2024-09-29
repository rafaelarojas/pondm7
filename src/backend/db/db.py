from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime

DATABASE_URL = "postgresql://rafa:aaaa@db:5432/crypto_db"

Base = declarative_base()

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Criação do engine e sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_db_and_tables():
    """Cria as tabelas no banco de dados."""
    Base.metadata.create_all(bind=engine)

def save_log(message):
    """Salva uma nova entrada de log no banco de dados."""
    session = SessionLocal()
    try:
        log_entry = Log(message=message)
        session.add(log_entry)
        session.commit()
    except Exception as e:
        session.rollback()  # Reverte a transação em caso de erro
        print(f"Erro ao salvar o log: {e}")  # Log de erro ou tratamento apropriado
    finally:
        session.close()  # Garante que a sessão será fechada

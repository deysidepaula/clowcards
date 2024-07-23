from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import JSON
from sqlalchemy import create_engine
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Cartas(Base):
    __tablename__ = "cartas"
    id: Mapped[int] = mapped_column(primary_key=True)
    imagem : Mapped[str]
    nome: Mapped[str]= mapped_column(String(20), unique=True)
    descricao: Mapped[str]
    criado_em: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self):
        return f"Carta {self.nome}"


engine = create_engine("sqlite:///cartas_clow.db", echo=True)


Base.metadata.create_all(engine)

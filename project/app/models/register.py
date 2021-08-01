from datetime import date

from sqlalchemy import Column, Date, BigInteger, String

from project.app.database.modelbase import Base


class Register(Base):
    __tablename__ = "registers"

    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    products: str = Column(String(20), nullable=False)
    created_at: date = Column(Date, nullable=False, index=True)
    expire_at: date = Column(Date, nullable=False, index=True)

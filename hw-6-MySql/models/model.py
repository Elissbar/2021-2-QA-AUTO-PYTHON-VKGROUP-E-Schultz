from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class CountOfRequests(Base):
    __tablename__ = 'Count_Requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Count_Requests(id={self.id}, count={self.count})>'


class TopRequests(Base):
    __tablename__ = 'Top_Requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(280), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Top_Requests(id={self.id}, type={self.type}, count={self.count})>'


class FrequentRequests(Base):
    __tablename__ = 'Frequent_Requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Frequent_Requests(id={self.id}, url={self.url}, count={self.count})>'


class ClientError(Base):
    __tablename__ = 'Client_Error'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(280), nullable=False)
    code = Column(String(30), nullable=False)
    value = Column(Integer, nullable=False)
    ip = Column(String(30), nullable=False)

    def __repr__(self):
        return f'<Client_Error(id={self.id}, url={self.url}, code={self.code}, value={self.value}, ip={self.ip})>'


class ServerError(Base):
    __tablename__ = 'Server_Error'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Server_Error(id={self.id}, ip={self.ip}, count={self.count})>'






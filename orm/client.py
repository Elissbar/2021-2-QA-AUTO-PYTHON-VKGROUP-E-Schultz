import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MySQLClient:

    def __init__(self, host, db=None):
        self.user = 'root'
        self.password = 'root'
        self.host = host
        self.db = db

    def connect(self):
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.db}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine)()

    def execute_query(self, query):
        res = self.connection.execute(query)
        return res.fetchall()


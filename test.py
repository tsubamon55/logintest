from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///test.sql")


class User(Base):
    __tablename__ = "user"  # テーブル名を指定
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):  # フルネームを返すメソッド
        return "{self.first_name} {self.last_name}"


if __name__ == '__main__':
    # Base.metadata.create_all(engine)

    Session = sessionmaker(engine)  # セッションを作るクラスを作成
    # session = SessionClass()

    # user_a = User(first_name="first_a", last_name="last_a", age=20)
    # session.add(user_a)
    # session.commit()
    # users = session.query(User).all()
    # print(users)
    # print(users[2].first_name)
    from contextlib import contextmanager


    @contextmanager
    def session_scope():
        """Provide a transactional scope around a series of operations."""
        session = Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


    def run_my_program():
        with session_scope() as session:
            ThingOne().go(session)
            ThingTwo().go(session)



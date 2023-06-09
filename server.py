import sqlite3
import logging
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


def login_verification(username, password):
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    curs.execute(
        "SELECT password FROM accounts WHERE username == ?", (username,)
    )
    fetch = curs.fetchone()
    conn.commit()
    conn.close()
    if not fetch:
        return False
    correct_password = fetch[0]
    if password == correct_password:
        logger.info({'action': 'login', 'status': 'success', 'username': username})
        return True
    logger.info({'action': 'login', 'status': 'fail', 'username': username})
    return False


def register(username, password):
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    curs.execute(
        "INSERT INTO accounts(username, password) values(?, ?)", (username, password)
    )
    conn.commit()
    conn.close()
    logger.info({'action': 'register', 'status': 'success', 'username': username})
    return True


def show():
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    curs.execute(
        "SELECT * FROM accounts"
    )
    data = curs.fetchall()
    curs.close()
    conn.close()
    return data

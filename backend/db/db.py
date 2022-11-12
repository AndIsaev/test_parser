from backend.app import db


class DbSession:
    def __init__(self, read_only=False):
        self._read_only = read_only

    def __enter__(self):
        self._session = db.session
        return self._session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._read_only:
            if exc_type:
                self._session.rollback()
            else:
                self._session.commit()

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, Session, sessionmaker
from api.config import DatabaseSettings
from .logger import Logger

_logger = Logger(logger_name=__name__).logger

_database_settings = DatabaseSettings() # Load settings once at the module level


class SessionFactory:
    """Singleton factory for SQLAlchemy sessions with thread-safe scoped sessions."""
    _engine = None
    _session_factory = None

    def __init__(self):
        if SessionFactory._engine == None:
            SessionFactory._engine = create_engine(
                url=_database_settings.connection_url,
                pool_size=_database_settings.pool_size,
                max_overflow=_database_settings.max_overflow,
                pool_pre_ping=True
            )
            SessionFactory._session_factory = scoped_session(
                sessionmaker(
                    bind=SessionFactory._engine,
                    expire_on_commit=False,
                    autoflush=False
                )
            )

    @property
    def session_factory(self) -> Session:
        return SessionFactory._session_factory


class SessionManager:
    """Thread-safe SQLAlchemy session manager using context protocol."""
    def __init__(self):
        self.session_factory = SessionFactory().session_factory

    def __enter__(self) -> Session:
        self.session = self.session_factory()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        try:
            if exc_type:
                self.session.rollback()
                return False
            else:
                self.session.commit()
        except Exception as e:
            _logger.error("Error during transaction | Error: %s", str(e))
            raise e.with_traceback(exc_tb)
        finally:
            self.session.close()
            self.session_factory.remove()
        return False

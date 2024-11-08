from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = "postgresql://employeemn:DeYmrBkXa7S0y7uzY6DZultYVuMmSrwd@dpg-csmg5lq3esus73e02n7g-a.oregon-postgres.render.com/employeemn"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session local instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()


from sqlalchemy import Column, String
from app.core.database import Base

class Admin(Base):
    """
    Represents an Admin who manages auction settings.
    """
    __tablename__ = "admins"

    admin_id = Column(String(10), primary_key=True, unique=True, nullable=False)  # Prefixed with SLAM
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # Store hashed passwords

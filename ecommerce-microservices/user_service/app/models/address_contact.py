from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship


class Address_Contact(Base):
    __tablename__ = "addresses_contacts"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String)
    city = Column(String)
    zip_code = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    phone_number = Column(String)
    email = Column(String)

    user = relationship("User", back_populates="addresses")
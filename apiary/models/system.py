"""
System Model

"""
import sqlalchemy
import uuid

from apiary.models import profile
from apiary.models import base
from apiary import types


class System(base.Base):
    """Represents a unique system, physical or virtual"""
    __tablename__ = 'systems'

    id = sqlalchemy.Column(types.UUID, primary_key=True,
                           default=uuid.uuid4, nullable=False)
    hostname = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False)
    profile_fk = sqlalchemy.ForeignKey('%s.name' %
                                       profile.Profile.__tablename__)
    profile = sqlalchemy.Column(sqlalchemy.TEXT, profile_fk, nullable=False)
    kernel_options = sqlalchemy.Column(sqlalchemy.TEXT)
    hostname = sqlalchemy.Column(sqlalchemy.TEXT)
    serial_number = sqlalchemy.Column(sqlalchemy.TEXT)
    manufacturer = sqlalchemy.Column(sqlalchemy.TEXT)
    model = sqlalchemy.Column(sqlalchemy.TEXT)

    def __repr__(self):
        """Return the representation of the object

        :rtype: str

        """
        return "<System('%s', '%s')>" % (self.hostname, self.id)
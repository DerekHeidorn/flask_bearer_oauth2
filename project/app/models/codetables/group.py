
from sqlalchemy import Column, String
from project.app.models.baseModel import BaseModel


class CtGroupTypes(BaseModel):
    __tablename__ = 'tb_group_typ_cd'

    code = Column("grptyp_cd", String(2), primary_key=True, nullable=False)

    description = Column("grptyp_de", String(20), nullable=False)

    def __repr__(self):
        return "<CtGroupTypes(code='%s', description='%s')>" % (self.code, self.description)

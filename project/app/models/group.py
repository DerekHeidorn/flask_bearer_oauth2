
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table, MetaData
from sqlalchemy.orm import relationship, backref

from project.app.models.baseModel import BaseModel


# CREATE TABLE general.TB_PERSON (
# 	"PERSON_ID" serial NOT NULL, -- System-generated ID for a Group.
#     "USER_UUID" uuid NOT NULL,
#     "NICK_NAME" character varying(100) NOT NULL,
#     CONSTRAINT "PKTB_PERSON" PRIMARY KEY ("PERSON_ID")
# );
class Person(BaseModel):
    __tablename__ = 'tb_person'

    # PERSON_ID
    person_id = Column("person_id", Integer, primary_key=True)

    # USER_UUID
    user_uuid = Column("user_uuid", String(50))

    # NICK_NAME		Last Name of the User
    nick_name = Column("nick_name", String(80))

    def __repr__(self):
        return "<Person(user_uuid='%s')>" % self.user_uuid

# CREATE TABLE general.TB_GROUP (
#   "GROUP_ID" serial NOT NULL, -- System-generated ID for a Group.
#   "GROUP_UUID" uuid NOT NULL,
#   "GROUP_NAME" character varying(100) NOT NULL,
#   CONSTRAINT "PKTB_GROUP" PRIMARY KEY ("GROUP_ID")
# );


class Group(BaseModel):
    __tablename__ = 'tb_group'

    # GROUP_ID
    group_id = Column("group_id", Integer, primary_key=True)

    # USER_UUID
    group_uuid = Column("group_uuid", String(50))

    # GRPTYP_CD
    group_type_cd = Column("grptyp_cd", String(2))

    # GROUP_NAME		Last Name of the User
    group_name = Column("group_name", String(80))

    # GROUP_NAME		Last Name of the User
    group_de = Column("group_name", String(1000))

    def __repr__(self):
        return "<Group(group_name='%s')>" % self.group_name


# CREATE TABLE general.TB_MEMBERSHIP (
# 	"MEMBERSHIP_ID" serial NOT NULL, -- System-generated ID for a Group.
#     "PERSON_ID" integer NOT NULL,
#     "GROUP_ID" integer NOT NULL,
#     "MEMBERSHIP_FROM_TS" timestamp without time zone NOT NULL,
# 	"MEMBERSHIP_TO_TS" timestamp without time zone NOT NULL,
#     CONSTRAINT "PKTB_MEMBERSHIP" PRIMARY KEY ("MEMBERSHIP_ID"),
# 	CONSTRAINT "TB_MEMBERSHIP_TO_TB_PERSON" FOREIGN KEY ("PERSON_ID") REFERENCES general.TB_PERSON ("PERSON_ID"),
# 	CONSTRAINT "TB_MEMBERSHIP_TO_TB_GROUP" FOREIGN KEY ("GROUP_ID") REFERENCES general.TB_GROUP ("GROUP_ID")
# );

class Membership(BaseModel):
    __tablename__ = 'tb_membership'

    # MEMBERSHIP_ID
    membership_id = Column("membership_id", Integer, primary_key=True)

    # PERSON_ID
    person_id = Column("person_id", Integer, ForeignKey('tb_person.person_id'))

    # GROUP_ID
    group_id = Column("group_id", Integer)

    # MEMBERSHIP_FROM_TS
    from_ts = Column("membership_from_ts", DateTime)

    # MEMBERSHIP_TO_TS
    to_ts = Column("membership_to_ts", DateTime)

    person = relationship("Person")

    def __repr__(self):
        return "<Membership(id='%s')>" % self.membership_id

# CREATE TABLE general.TB_GROUP_MANAGER (
# 	"MANAGER_ID" serial NOT NULL, -- System-generated ID for a Group.
#     "GROUP_ID" integer NOT NULL,
#     "PERSON_ID" integer NOT NULL,
#     "MANAGER_FROM_TS" timestamp without time zone NOT NULL,
# 	"MANAGER_TO_TS" timestamp without time zone NOT NULL,
# 	CONSTRAINT "PKTB_GROUP_MANAGER" PRIMARY KEY ("MANAGER_ID"),
# 	CONSTRAINT "TB_GROUP_MANAGER_TO_TB_PERSON" FOREIGN KEY ("PERSON_ID") REFERENCES general.TB_PERSON ("PERSON_ID"),
# 	CONSTRAINT "TB_GROUP_MANAGER_TO_TB_GROUP" FOREIGN KEY ("GROUP_ID") REFERENCES general.TB_GROUP ("GROUP_ID")
# );


class GroupManager(BaseModel):
    __tablename__ = 'tb_group_manager'

    # MEMBERSHIP_ID
    manager_id = Column("manager_id", Integer, primary_key=True)

    # PERSON_ID
    person_id = Column("person_id", Integer, ForeignKey('tb_person.person_id'))

    # GROUP_ID
    group_id = Column("group_id", Integer)

    # MANAGER_FROM_TS
    from_ts = Column("manager_from_ts", DateTime)

    # MANAGER_TO_TS
    to_ts = Column("manager_to_ts", DateTime)

    person = relationship("Person")

    def __repr__(self):
        return "<GroupManager(id='%s')>" % self.manager_id

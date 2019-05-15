from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Index, Integer, String, text, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from app import db

Base = db.Model
metadata = Base.metadata

# class GroupUser(Base):
#     __tablename__ = 'group_users'
#     __table_args__ = (
#         Index('index_group_users_on_group_id_and_user_id', 'group_id', 'user_id', unique=True),
#     )
#
#     id = Column(BigInteger, primary_key=True)
#     group_id = Column(ForeignKey('groups.id'), nullable=False)
#     user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
#
#     group = relationship('Group')
#     user = relationship('User')

group_users_table = Table('group_users', Base.metadata,
    Column('group_id', Integer, ForeignKey('groups.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class Track(Base):
    __tablename__ = 'tracks'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, index=True)
    duration = Column(Integer)
    spotify_id = Column(String, index=True)
    group_id = Column(ForeignKey('groups.id'))
    rank = Column(Integer)
    artists = Column(String)

    group = relationship('Group', backref='tracks')


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    spotify_id = Column(String)
    access_token = Column(String)
    refresh_token = Column(String)
    token_expiration = Column(DateTime)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'spotify_id': self.spotify_id
        }

        return data


class AuthToken(Base):
    __tablename__ = 'auth_tokens'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    token = Column(String, nullable=False, index=True)

    user = relationship('User', backref='auth_tokens')


class Group(Base):
    __tablename__ = 'groups'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    title = Column(String, nullable=False)

    owner = relationship('User')
    users = relationship('User',
        secondary=group_users_table,
        backref='groups')


class SpotifyPlaylist(Base):
    __tablename__ = 'spotify_playlists'

    id = Column(BigInteger, primary_key=True)
    group_id = Column(ForeignKey('groups.id'), nullable=False, index=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    spotify_id = Column(String)

    group = relationship('Group', backref='spotify_playlists')
    user = relationship('User', backref='spotify_playlists')

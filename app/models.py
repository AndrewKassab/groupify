from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Index, Integer, String, text, Table
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

# group_users_table = Table('group_users', Base.metadata,
#     Column('group_id', Integer, ForeignKey('groups.id')),
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('visible', Boolean)
# )

class GroupUsers(Base):
    __tablename__ = 'group_users'

    id = Column(BigInteger, primary_key=True)

    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    group_id = Column(ForeignKey('groups.id'), nullable=False, index=True)
    visible = Column(Boolean)


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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artists': self.artists,
            'duration': self.duration
        }


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String)
    spotify_id = Column(String)
    access_token = Column(String)
    refresh_token = Column(String)
    token_expiration = Column(DateTime)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'username': self.username
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

    def spotify_id(self, user):
        spotify_id = SpotifyPlaylist.query. \
            filter_by(group_id=self.id, user_id=user.id).first()

        return spotify_id and spotify_id.spotify_id

    def visible(self, user):
        return GroupUsers.query.filter_by(group_id=self.id, user_id=user.id).first().visible

    def set_visible(self, user, visiblility):
        GroupUsers.query.filter_by(group_id=self.id, user_id=user.id).first().visible = visiblility

    def full_details(self, user):
        tracks = [track.to_dict() for track in self.tracks]
        users = []

        for nuser in self.users:
            u = nuser.to_dict()
            if nuser.id == self.user_id:
                u['owner'] = True
            users.append(u)

        users.sort(key=lambda u: u['id'])
        tracks.sort(key=lambda t: t['id'])

        data = {
            "id": self.id,
            "name": self.title,
            "tracks": tracks,
            "users": users,
            "visible": self.visible(user),
            "spotify_id": self.spotify_id(user),
            "owner_id": self.user_id,
            "state": "done"
        }

        return data

    def short_details(self, user):
        data = {
            "id": self.id,
            "name": self.title,
            "visible": self.visible(user),
            "owner": user.id == self.user_id,
            "state": "done"
        }

        return data

    owner = relationship('User')
    users = relationship('User',
        secondary='group_users',
        backref='groups')


class SpotifyPlaylist(Base):
    __tablename__ = 'spotify_playlists'

    id = Column(BigInteger, primary_key=True)
    group_id = Column(ForeignKey('groups.id'), nullable=False, index=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    spotify_id = Column(String)

    group = relationship('Group', backref='spotify_playlists')
    user = relationship('User', backref='spotify_playlists')

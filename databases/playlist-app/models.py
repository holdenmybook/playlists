"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    __tablename__ = 'playlist'
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(100), nullable=Flase)
desciprtion = db.Column(db.String(255))
    # ADD THE NECESSARY CODE HERE
songs = db.relationship('Song', secondary='playlist_song', back_populates='playlists')
    """Playlist."""


class Song(db.Model):
    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    """Song."""
    playlists = db.relationship('Playlist', secondary='playlist_song', back_populates='songs')

    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
     __tablename__ = 'playlist_song'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)

    # Define relationship with Playlist and Song
    playlist = db.relationship('Playlist', backref=db.backref('playlist_songs', cascade='all, delete-orphan'))
    song = db.relationship('Song', backref=db.backref('playlist_songs', cascade='all, delete-orphan'))
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

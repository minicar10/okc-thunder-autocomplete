Database Architecture Description

The database schema holds and structures player performance data. Four primary models make up
this schema: Player, Game, Shot, and Team. With this database, flexibility is provided for scaling.

Player: This model represents an individual player and stores attributes such as an ID
and name. Each player can participate in multiple games, forming a one-to-many relationship
with the Game model.

Game: This model records a player’s performance in a specific game on a given date, including
fields for points, assists, and other statistics. The Game model also stores whether the player
was a starter. Through a foreign key, a game is linked to a player allowing for multiple games
to be with a player.

Shot: This model records individual shot attempts, including whether the shot was successful
and the shot's location in relation to the court. A shot is associated with a game through a
foreign key, establishing a one-to-many relationship between Game and Shot, since each game usually
contains multiple shots.

Team: This model represents teams with an ID and a name. The team model doesn't directly link with
other models, but it allows for future enhancements, such as associating players with teams.

With this schema, data can be efficiently organized for querying player statistics across
games and shot patterns, supporting a wide range of performance analyses.
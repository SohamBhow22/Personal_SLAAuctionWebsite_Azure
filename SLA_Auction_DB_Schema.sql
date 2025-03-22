
-- Teams Table
CREATE TABLE teams (
    team_id VARCHAR(8) PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    team_leader VARCHAR(100) NOT NULL,
    team_captain VARCHAR(100),
    year_formed VARCHAR(7),
    purse_left FLOAT NOT NULL,
    purse_spent FLOAT NOT NULL,
    player_spots_filled INT NOT NULL,
    player_spots_total INT NOT NULL,
    CONSTRAINT UQ_team_leader_year UNIQUE (team_leader, year_formed)
);

-- Players Table
CREATE TABLE players (
    player_id VARCHAR(8) PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    previous_team VARCHAR(100),
    player_image VARCHAR(255),
    address CHAR(4) NOT NULL,
    stumps_id VARCHAR(50) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    CONSTRAINT CK_mobile_number CHECK (mobile_number LIKE '+91-%'),
    CONSTRAINT UQ_mobile_number UNIQUE (mobile_number)
);

-- Auction History Table
CREATE TABLE auction_history (
    auction_id VARCHAR(8) PRIMARY KEY,
    player_id VARCHAR(8) REFERENCES players(player_id),
    team_id VARCHAR(8) REFERENCES teams(team_id),
    base_price FLOAT NOT NULL,
    sold_price FLOAT NOT NULL,
    year VARCHAR(7) NOT NULL,
    CONSTRAINT UQ_player_team_year UNIQUE (player_id, team_id, year)
);

-- Player Performance (Stats) Table
CREATE TABLE player_stats (
    stat_id VARCHAR(8) PRIMARY KEY,
    player_id VARCHAR(8) REFERENCES players(player_id),
    matches_played INT NOT NULL,
    runs_scored INT NOT NULL,
    wickets_taken INT NOT NULL,
    highest_score INT NOT NULL,
    best_bowling VARCHAR(10),
    year VARCHAR(7) NOT NULL,
    CONSTRAINT UQ_player_year UNIQUE (player_id, year)
);

-- Auto-increment logic for IDs with required prefixes
-- Teams Auto-ID
CREATE SEQUENCE team_seq START WITH 1;
CREATE TRIGGER team_id_trigger
ON teams
INSTEAD OF INSERT
AS
BEGIN
    INSERT INTO teams (
        team_id, team_name, team_leader, team_captain, year_formed, 
        purse_left, purse_spent, player_spots_filled, player_spots_total
    )
    SELECT 
        'SLAT' + RIGHT('0000' + CAST(NEXT VALUE FOR team_seq AS VARCHAR), 4),
        team_name, team_leader, team_captain, year_formed,
        purse_left, purse_spent, player_spots_filled, player_spots_total
    FROM inserted;
END;
GO

-- Players Auto-ID
CREATE SEQUENCE player_seq START WITH 1;
CREATE TRIGGER player_id_trigger
ON players
INSTEAD OF INSERT
AS
BEGIN
    INSERT INTO players (
        player_id, player_name, role, previous_team, player_image, 
        address, stumps_id, mobile_number
    )
    SELECT 
        'SLAP' + RIGHT('0000' + CAST(NEXT VALUE FOR player_seq AS VARCHAR), 4),
        player_name, role, previous_team, player_image,
        address, stumps_id, mobile_number
    FROM inserted;
END;
GO

-- Auction Auto-ID
CREATE SEQUENCE auction_seq START WITH 1;
CREATE TRIGGER auction_id_trigger
ON auction_history
INSTEAD OF INSERT
AS
BEGIN
    INSERT INTO auction_history (
        auction_id, player_id, team_id, base_price, sold_price, year
    )
    SELECT 
        'SLAA' + RIGHT('0000' + CAST(NEXT VALUE FOR auction_seq AS VARCHAR), 4),
        player_id, team_id, base_price, sold_price, year
    FROM inserted;
END;
GO

-- Stats Auto-ID
CREATE SEQUENCE stats_seq START WITH 1;
CREATE TRIGGER stats_id_trigger
ON player_stats
INSTEAD OF INSERT
AS
BEGIN
    INSERT INTO player_stats (
        stat_id, player_id, matches_played, runs_scored, wickets_taken,
        highest_score, best_bowling, year
    )
    SELECT 
        'SLAS' + RIGHT('0000' + CAST(NEXT VALUE FOR stats_seq AS VARCHAR), 4),
        player_id, matches_played, runs_scored, wickets_taken,
        highest_score, best_bowling, year
    FROM inserted;
END;
GO

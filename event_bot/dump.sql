PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE events (name TEXT, date NUM, time NUM, place TEXT);
INSERT INTO events VALUES('new year','2022-12-31','12:00:00','osh');
COMMIT;

# DB Design

## battle

create table battle (id int auto_increment primary key, name text, start_at_unix_time int, turn int, turn_mills int, interval_mills int, teamA int, teamB int, now_battle int, foreign key(teamA) references team(id), foreign key(teamB) references team(id));

## team

create table team (id int auto_increment, name text, token text, primary key(id));

## action

create table action (battle_id int, turn int, detail text, primary key(battle_id, turn), foreign key (battle_id) references battle(id));

## stage

create table stage (battle_id int, width int, height int, points text, tiled text, foreign key (battle_id) references battle(id));
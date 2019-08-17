create table team (id int auto_increment, name text, token varchar(255) unique, primary key(id));
create table battle (id int auto_increment primary key, name text, start_at_unix_time int, turn int, turn_mills int, interval_mills int, teamA int, teamB int, now_battle int, foreign key(teamA) references team(id), foreign key(teamB) references team(id));
create table action (battle_id int, turn int, detail text, primary key(battle_id, turn), foreign key (battle_id) references battle(id));
create table stage (battle_id int, width int, height int, points text, tiled text, agent_pos text, foreign key (battle_id) references battle(id));

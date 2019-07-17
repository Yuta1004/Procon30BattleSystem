# DB Design

## battle

create table battle (id int auto_increment primary key, name text, token text, turn int, turn_msec int, turn_switch_msec int, teams text, now_battle int)

## action

create table action (battle_id int, turn int, detail text, primary key(battle_id, turn), constraint fk_battle_id foreign key (battle_id) references battle(id));

## stage

create table stage (battle_id int, points text, tiled text, constraint fk_battle_id_2 foreign key (battle_id) references battle(id));
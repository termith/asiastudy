drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    text text not null,
    clear_text text,
    N1 integer,
    N2 integer,
    N3 integer,
    N4 integer,
    N5 integer
);
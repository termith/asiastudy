drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    text not null,
    clear_text,
    N1 integer,
    N2 integer,
    N3 integer,
    N4 integer,
    N5 integer
);
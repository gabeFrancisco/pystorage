create table products(
    id serial,
    created_at date not null,
    updated_at date,
    name varchar(50) not null,
    description varchar(200) not null,
    quantity int not null,
    price decimal(10,2) not null
);

insert into products(created_at, name, description, quantity, price) values (
    '2026-01-24 20:05:12',
    'MacBook Air',
    'Notebook com chip M1 e 16GB de RAM',
    3,
    7800
);
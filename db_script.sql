create table
    products (
        id serial primary key,
        created_at date not null,
        updated_at date,
        name varchar(50) not null,
        description varchar(200) not null,
        quantity int not null,
        price decimal(10, 2) not null
    );

insert into
    products (created_at, name, description, quantity, price)
values
    (
        '2026-01-24 20:05:12',
        'MacBook Air',
        'Notebook com chip M1 e 16GB de RAM',
        3,
        7800
    );

create table
    categories (
        id serial primary key,
        created_at date not null,
        updated_at date,
        name varchar(50) not null
    );

insert into
    categories (created_at, name)
values
    ('2026-01-24 20:05:12', 'Books');

-- add column category_id int not null default 1,
alter table products add constraint fk_categories_product foreign key (category_id) references categories (id) on delete cascade;

select
    p.id,
    p.created_at,
    p.updated_at,
    p.name,
    p.description,
    p.quantity,
    p.price,
    c.name as category
from
    products p
    inner join categories c on p.category_id = c.id;
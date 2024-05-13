create table clients (
	id serial primary key,
	name varchar(100) not null,
	email varchar(100),
	phone varchar(50) not null,
	identification_number varchar(100) not null unique,
	created_at timestamp default CURRENT_TIMESTAMP,
	updated_at timestamp default CURRENT_TIMESTAMP,
	deleted_at timestamp default null
)


create table appointments (
	id serial primary key,
	date timestamp not null,
	client_id int,
	created_at timestamp default CURRENT_TIMESTAMP,
	updated_at timestamp default CURRENT_TIMESTAMP,
	deleted_at timestamp default null,
	foreign key (client_id) REFERENCES clients (id)
)


create table professionals (
	id serial primary key,
	name varchar(100) not null,
	email varchar(100),
	phone varchar(50) not null,
	type int not null,
	created_at timestamp default CURRENT_TIMESTAMP,
	updated_at timestamp default CURRENT_TIMESTAMP,
	deleted_at timestamp default null
)

create table appointments_professionals (
	id serial primary key,
	appointment_id int,
	professional_id int,
	created_at timestamp default CURRENT_TIMESTAMP,
	updated_at timestamp default CURRENT_TIMESTAMP,
	deleted_at timestamp default null,
	FOREIGN key (appointment_id) REFERENCES appointments (id),
	FOREIGN key (professional_id) REFERENCES professionals (id)
)
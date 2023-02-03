CREATE TABLE TIPO_MAQUINARIA(
    id serial PRIMARY KEY,
    descripcion VARCHAR(50) not null
);

CREATE TABLE RESIDUO(
    id serial PRIMARY KEY,
    nombre VARCHAR(20) not NULL UNIQUE,
    descripcion varchar(50),
    estado boolean not null
);

CREATE TABLE TIPO_USUARIO(
    id serial PRIMARY KEY,
    nombre varchar(30) not null,
    descripcion VARCHAR(50) not NULL,
    estado boolean not null
);

CREATE TABLE TIPO_INCENTIVO(
    id serial PRIMARY KEY,
    nombre VARCHAR(20) not NULL,
    descripcion VARCHAR(50)
);

create table tipoPersonal(
    id serial primary key,
    nombre varchar(30) not null,
    descripcion varchar(100) not null
);

create table tipoDocumento(
    id serial primary key,
    nombre varchar(100) not null
);

create table zona(
    id serial primary key,
    nombre varchar(50),
    estado boolean not null
);

create table empadronamiento(
    id serial primary key,
    nombre varchar(30),
    descripcion varchar(100)
);

CREATE TABLE USUARIO(
    id serial PRIMARY KEY,
    nombre_usuario VARCHAR(30) not NULL UNIQUE,
    nombreCompleto varchar(100) not null,
    contraseña VARCHAR(30) not null,
    estado BOOLEAN not null,
    TipoUsuario_ID int not null,
    constraint fk1_USUARIO FOREIGN KEY(TipoUsuario_ID) REFERENCES TIPO_USUARIO(id)
);

create table personal(
    id serial primary key,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    documento varchar(20) not null unique,
    fechaNacimiento date not null,
    correo varchar(100) unique,
    celular char(9) not null unique,
    direccion varchar(100) not null,
    estado boolean not null,
    idTipoDoc serial not null,
    idTipoPersonal serial not null,
    idEmpadro serial not null,
    constraint fk1_personal foreign key(idTipoDoc) references tipoDocumento(id),
    constraint fk2_personal foreign key(idTipoPersonal) references tipoPersonal(id),
    constraint fk3_personal foreign key(idEmpadro) references empadronamiento(id)
);

create table tipo_ciudadano(
    id serial primary key,
    nombre varchar(50) not null,
    descripcion varchar(100) not null
);

create table ciudadano(
    id serial primary key,
    nombre varchar(50),
    apellido varchar(50),
    documento varchar(20) unique,
    celular char(9) not null unique,
    direccion varchar(100),
    estado boolean not null,
    idTipoDoc serial not null,
    idEmpadro serial not null,
    idTipoCiud serial not null,
    constraint fk1_ciudadano foreign key(idTipoDoc) references tipoDocumento(id),
    constraint fk2_ciudadano foreign key(idEmpadro) references empadronamiento(id),
    constraint fk3_ciudadano foreign key(idTipoCiud) references tipo_ciudadano(id)
);

create table maquinaria(
    id serial primary key,
    nombre varchar(30) not null,
    placa char(7) unique not null,
    estado boolean not null,
    cargaNeta float not null,
    cargaUtil float not null,
    idTipoMaqui serial not null,
    constraint fk1_maquinaria foreign key(idTipoMaqui) references TIPO_MAQUINARIA(id)
);

create table ruta(
    id serial primary key,
    ruta varchar(200) not null,
    lugarInicio varchar(100) not null,
    lugarFin varchar(100) not null,
    idZona serial not null,
    constraint fk1_ruta foreign key(idZona) references zona(id)
);

create table horario(
    id serial primary key,
    fecha date not null,
    hora time not null,
    estado boolean not null,
    idRuta serial not null,
    constraint fk1_horario foreign key(idRuta) references ruta(id)
);

CREATE TABLE RECOLECCION(
    id serial PRIMARY KEY,
    observacion VARCHAR(200),
    Personal_ID int not null,
    Maquinaria_ID int not null,
    Residuo_ID int not null,
    Horario_ID int not null,
    Usuario_ID int not null,
    constraint fk1_RECOLECCION FOREIGN KEY(Personal_ID) REFERENCES personal(id),
    constraint fk2_RECOLECCION FOREIGN KEY(Maquinaria_ID) REFERENCES maquinaria(id),
    constraint fk3_RECOLECCION FOREIGN KEY(Residuo_ID) REFERENCES RESIDUO(id),
    constraint fk4_RECOLECCION FOREIGN KEY(Horario_ID) REFERENCES horario(id),
    constraint fk5_RECOLECCION FOREIGN KEY(Usuario_ID) REFERENCES USUARIO(id)
);

CREATE TABLE DETALLE_INCENTIVO (
    id serial PRIMARY KEY,
    cantidad int not null,
    TIPOINCENTIVOid int NOT NULL,
    RECOLECCIONid int NOT NULL,
    CIUDADANOid int NOT NULL,
    constraint fk1_DETALLE_INCENTIVO FOREIGN KEY(TIPOINCENTIVOid) REFERENCES tipo_incentivo(id),
    constraint fk2_DETALLE_INCENTIVO FOREIGN KEY(RECOLECCIONid) REFERENCES RECOLECCION(id),
    constraint fk3_DETALLE_INCENTIVO FOREIGN KEY(CIUDADANOid) REFERENCES CIUDADANO(id)
);
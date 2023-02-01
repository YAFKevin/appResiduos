CREATE TABLE TIPO_MAQUINARIA(
    id serial PRIMARY KEY,
    descripcion VARCHAR(50) not null
);

----- CRUD tipo maquinaria

CREATE OR REPLACE FUNCTION insertarTipoMaquinaria(
descripcion varchar(50)
)
RETURNS void AS $$
BEGIN
INSERT INTO tipo_maquinaria(descripcion)
VALUES(descripcion);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION modificarTipoMaquinaria(
idF int,descripcionF varchar(50)
)
RETURNS int AS $$
BEGIN
    update tipo_maquinaria set descripcion=descripcionF where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION eliminarTipoMaquinaria(
idF int
)
RETURNS int AS $$
BEGIN
    delete from tipo_maquinaria where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------

CREATE TABLE RESIDUO(
    id serial PRIMARY KEY,
    nombre VARCHAR(20) not NULL UNIQUE,
    descripcion varchar(50),
    estado boolean not null
);

---- CRUD RESIDUO ----------------------------------

CREATE
OR REPLACE FUNCTION insertarResiduo(nombre varchar(20)) RETURNS void AS $ $ BEGIN
INSERT INTO
    RESIDUO(nombre)
VALUES
    (nombre);

END;

$ $ LANGUAGE plpgsql;


CREATE
OR REPLACE FUNCTION eliminarResiduo(ids int) RETURNS void AS $ $ BEGIN
DELETE FROM
    RESIDUO
WHERE
    id = ids;

END;

$ $ LANGUAGE plpgsql;


CREATE
OR REPLACE FUNCTION actualizarResiduo(ids int, nombres varchar(20)) RETURNS void AS $ $ BEGIN
UPDATE
    RESIDUO
SET
    nombre = nombres
WHERE
    id = ids;

END;

$ $ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE TIPO_USUARIO(
    id serial PRIMARY KEY,
    nombre varchar(30) not null,
    descripcion VARCHAR(50) not NULL,
    estado boolean not null
);

------- CRUD TIPO USUARIO   

CREATE
OR REPLACE FUNCTION insertarTipoUsuario(descripcion VARCHAR(50)) RETURNS void AS $ $ BEGIN
INSERT INTO
    TIPO_USUARIO(descripcion)
VALUES
    (descripcion);

END;

$ $ LANGUAGE plpgsql;


CREATE
OR REPLACE FUNCTION eliminarTipoUsuario(ids int) RETURNS void AS $ $ BEGIN
DELETE FROM
    TIPO_USUARIO
WHERE
    id = ids;

END;

$ $ LANGUAGE plpgsql;


CREATE
OR REPLACE FUNCTION modificarTipoUsuario(ids int, descripcion1 VARCHAR(50)) RETURNS void AS $ $ BEGIN
UPDATE
    TIPO_USUARIO
SET
    descripcion = descripcion1
WHERE
    id = ids;

END;

$ $ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE TIPO_INCENTIVO(
    id serial PRIMARY KEY,
    nombre VARCHAR(20) not NULL,
    descripcion VARCHAR(50)
);

-------CRUD tipo_incentivo

CREATE
OR REPLACE FUNCTION insertar_tipoIncentivo(nombres VARCHAR, descripcions VARCHAR) RETURNS void AS $ $ BEGIN
INSERT INTO
    TIPO_INCENTIVO (nombre, descripcion)
VALUES
    (nombres, descripcions);

END;

$ $ LANGUAGE plpgsql;


CREATE
OR REPLACE FUNCTION eliminar_tipoIncentivo(id INTEGER) RETURNS void AS $ $ BEGIN
DELETE FROM
    TIPO_INCENTIVO
WHERE
    id = id;

END;

$ $ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION actualizar_tipoIncentivo(
    ids INTEGER,
    nombres VARCHAR,
    descripcions VARCHAR
) RETURNS void AS $ $ BEGIN
UPDATE
    TIPO_INCENTIVO
SET
    nombre = nombres,
    descripcion = descripcions
WHERE
    id = ids;

END;

$ $ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------

create table tipoPersonal(
    id serial primary key,
    nombre varchar(30) not null,
    descripcion varchar(100) not null
);

-------- CRUD tipoPersonal

CREATE OR REPLACE FUNCTION insertarTipopersonal(
descripcion varchar(100)
)
RETURNS void AS $$
BEGIN
    insert into tipopersonal(descripcion)
    values(descripcion);
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION modificarTipopersonal(
idF int,descripcionF varchar(100)
)
RETURNS int AS $$
BEGIN
    update tipopersonal set descripcion=descripcionF where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION eliminarTipopersonal(
idF int
)
RETURNS int AS $$
BEGIN
    delete from tipopersonal  where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;


--------------------------------------------------------------------------------------------------------------------------------

create table tipoDocumento(
    id serial primary key,
    nombre varchar(100) not null
);

------- CRUD tipoDocumento

CREATE OR REPLACE FUNCTION insertarTipodocumento(
nombre varchar(100)
)
RETURNS void AS $$
BEGIN
    insert into tipodocumento(nombre)
    values(nombre);
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION modificarTipodocumento(
idF int,nombreF varchar(100)
)
RETURNS int AS $$
BEGIN
    update tipodocumento set nombre=nombreF where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION eliminarTipodocumento(
idF int
)
RETURNS int AS $$
BEGIN
    delete from tipodocumento where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;


--------------------------------------------------------------------------------------------------------------------------------

create table zona(
    id serial primary key,
    nombre varchar(50),
    estado boolean not null
);


----- CRUD zona --------------------------------

CREATE OR REPLACE FUNCTION insertarZona(
nombre varchar(50), estado boolean
)
RETURNS void AS $$
BEGIN
    insert into zona(nombre, estado)
    values(nombre, estado);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION modificarZona(
idZ int,nombreZ varchar(50), estadoZ boolean
)
RETURNS int AS $$
BEGIN
    update zona set nombre=nombreZ, estado=estadoZ where id=idZ;
    return 1;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION eliminarZona(
idZ int
)
RETURNS int AS $$
BEGIN
    delete from zona where id=idZ;
    return 1;
END;
$$ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------
create table empadronamiento(
    id serial primary key,
    nombre varchar(30),
    descripcion varchar(100)
);

---------- CRUD empadronamiento

CREATE OR REPLACE FUNCTION insertarEmpadronamiento(
nombre varchar(30),descripcion varchar(100)
)
RETURNS void AS $$
BEGIN
    insert into empadronamiento(nombre,descripcion)
    values(nombre,descripcion);
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION modificarEmpadronamientol(
idF int,nombreF varchar(30),descripcionF varchar(100)
)
RETURNS int AS $$
BEGIN
    update empadronamiento set nombre=nombreF,descripcion=descripcionF where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION eliminarEmpadronamiento(
idF int
)
RETURNS int AS $$
BEGIN
    delete from empadronamiento  where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;


--------------------------------------------------------------------------------------------------------------------------------
CREATE TABLE USUARIO(
    id serial PRIMARY KEY,
    nombre_usuario VARCHAR(30) not NULL UNIQUE,
    nombreCompleto varchar(100) not null,
    contraseña VARCHAR(30) not null,
    estado BOOLEAN not null,
    TipoUsuario_ID int not null,
    constraint fk1_USUARIO FOREIGN KEY(TipoUsuario_ID) REFERENCES TIPO_USUARIO(id)
);

-------- CRUD usuario
--funcion para insertar usuario
CREATE OR REPLACE FUNCTION insertarUsuario(
nombre_usuario varchar(30),nombreCompleto varchar(100),contraseña varchar(30),estado boolean,TipoUsuario_ID int
)
RETURNS void AS $$
BEGIN
    insert into usuario(nombre_usuario,nombreCompleto,contraseña,estado,TipoUsuario_ID)
    values(nombre_usuario,nombreCompleto,contraseña,estado,TipoUsuario_ID);
END;
$$ LANGUAGE plpgsql;

--funcion para modificar usuario
CREATE OR REPLACE FUNCTION modificarUsuario(
idF int,nombre_usuarioF varchar(30),nombreCompletoF varchar(100),contraseñaF varchar(30),estadoF boolean,TipoUsuario_IDF int
)
RETURNS int AS $$
BEGIN
    update usuario set nombre_usuario=nombre_usuarioF,nombreCompleto=nombreCompletoF,contraseña=contraseñaF,estado=estadoF,TipoUsuario_ID=TipoUsuario_IDF where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;

--funcion para eliminar usuario
CREATE OR REPLACE FUNCTION eliminarUsuario(
idF int
)
RETURNS int AS $$
BEGIN
    delete from usuario where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;

--funcion para dar de baja usuario
CREATE OR REPLACE FUNCTION bajaUsuario(
idF int
)
RETURNS int AS $$
BEGIN
    update usuario set estado=false where id=idF;
    return 1;
END;


--------------------------------------------------------------------------------------------------------------------------------

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

--------- CRUD personal

CREATE OR REPLACE FUNCTION insertarPersonal(
nombre varchar(50),apellido varchar(50),documento varchar(20),fechanacimiento date,correo varchar(100),
    celular char(9),direccion varchar(100), estado boolean,idtipodoc int, idtipopersonal int,idempadro int
)
RETURNS void AS $$
BEGIN
    insert into personal(nombre ,apellido ,documento,fechanacimiento,correo,
    celular,direccion , estado,idtipodoc, idtipopersonal,idempadro)
    values(nombre ,apellido ,documento,fechanacimiento,correo,
    celular,direccion , estado,idtipodoc, idtipopersonal,idempadro);
END;
$$ LANGUAGE plpgsql;




CREATE OR REPLACE FUNCTION modificarPersonal(
idF int,nombreF varchar(50),apellidoF varchar(50),documentoF varchar(20),fechanacimientoF date,correoF varchar(100),
    celularF char(9),direccionF varchar(100), estadoF boolean,idtipodocF int, idtipopersonalF int,idempadroF int
)
RETURNS int AS $$
BEGIN
    update personal set nombre=nombreF ,apellido=apellidoF ,documento=documentoF,fechanacimiento=fechanacimientoF,
    correo=correoF,celular=celularF,direccion=direccionF , estado=estadoF,idtipodoc=idtipodocF, idtipopersonal=idtipopersonalF,
    idempadro=idempadroF where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION eliminarPersonal(
idF int
)
RETURNS int AS $$
BEGIN
    delete from personal where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------

create table tipo_ciudadano(
    id serial primary key,
    nombre varchar(50) not null,
    descripcion varchar(100) not null
);

------ CRUD tipo ciudadano

CREATE OR REPLACE FUNCTION insertarTipociudadano(
nombre varchar(50), descripcion varchar(100)
)
RETURNS void AS $$
BEGIN
    insert into tipociudadnol(nombre,descripcion)
    values(nombre,descripcion);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION modificarTipociudadano(
idF int,nombreF varchar(50),descripcionF varchar(100)
)
RETURNS int AS $$
BEGIN
    update tipociudadan set nombre=nombreF,descripcion=descripcionF where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION eliminarTipociudadano(
idF int
)
RETURNS int AS $$
BEGIN
    delete from tipociudadano  where id=idF;
    return 1;
END;
$$ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------

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

------------CRUD ciudadano

create or replace function insertar_ciudadano(
    nombres varchar(50),
    apellidos varchar(50),
    documentos varchar(20),
    celulars char(9),
    direccions varchar(100),
    estado boolean,
    idTipoDocs int,
    idEmpadros int,
    idTipoCiuds int
)
returns void as $$
begin
    insert into ciudadano(nombre, apellido, documento, celular, direccion, estado, idTipoDoc, idEmpadro, idTipoCiud)
    values(nombres, apellidos, documentos, celulars, direccions, estado, idTipoDocs, idEmpadros, idTipoCiuds);
end;
$$ language plpgsql;


CREATE OR REPLACE FUNCTION eliminarCiudadano(
idC int
)
RETURNS int AS $$
BEGIN
    delete from Ciudadano where id=idC;
    return 1;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION modificarCiudadano(
idC int,nombreC varchar(50),apellidoC varchar(50),documentoC varchar(20), celularC varchar(9),direccionC varchar (100), estadoC boolean, idTipoDocC int, idEmpadroC int
)
RETURNS int AS $$
BEGIN
    update ciudadano set nombre= nombreC, apellido=apellidoC ,documento=documentoC , celular=celularC, direccion=direccionC, estado=estadoC, idTipoDoc= idTipoDocC, idEmpadro=idEmpadroC
    where id=idC;
    return 1;
END;
$$ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------

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

------------CRUD MAQUINARIA

CREATE OR REPLACE FUNCTION insertarMaquinaria(
    nombre varchar(30),
    placa char(7),
    estado boolean,
    carganeta float,
    cargautil float,
    idtipomaqui int
) RETURNS void AS $ $ BEGIN
INSERT INTO
    maquinaria(
        nombre,
        placa,
        estado,
        carganeta,
        cargautil,
        idtipomaqui
    )
VALUES
    (
        nombre,
        placa,
        estado,
        carganeta,
        cargautil,
        idtipomaqui
    );

END;

$ $ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION eliminarMaquinaria(idM int) RETURNS int AS $ $ BEGIN
delete from
    maquinaria
where
    id = idM;

return 1;

END;

$ $ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION modificarMaquinaria(
    idM int,
    nombreF varchar(30),
    placaF char(7),
    estadoF boolean,
    carganetaF float,
    cargautilF float,
    idtipomaquiF int
) RETURNS int AS $ $ BEGIN
update
    maquinaria
set
    nombre = nombreF,
    placa = placaF,
    estado = estadoF,
    carganeta = carganetaF,
    cargautil = cargautilF,
    idtipomaqui = idtipomaquiF
where
    id = idM;

return 1;

END;

$ $ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------
create table ruta(
    id serial primary key,
    ruta varchar(200) not null,
    lugarInicio varchar(100) not null,
    lugarFin varchar(100) not null,
    idZona serial not null,
    constraint fk1_ruta foreign key(idZona) references zona(id)
);

------ CRUD ruta --------------------------------

CREATE OR REPLACE FUNCTION insertarRuta(
 ruta varchar (200),lugarInicio varchar(100), lugarFin varchar(100), idZona int
) RETURNS void AS $$
BEGIN
INSERT INTO ruta (ruta,lugarInicio, lugarFin, idZona)
VALUES(ruta,lugarInicio, lugarFin,idZona);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION eliminarRuta(
idR int
)
RETURNS int AS $$
BEGIN
    delete from ruta where id=idR;
    return 1;
END;
$$ LANGUAGE plpgsql;

select*from zona

CREATE OR REPLACE FUNCTION modificarRuta(
idR int,rutaR varchar (200),lugarInicioR varchar(100), lugarFinR varchar(100), idZona int
)
RETURNS int AS $$
BEGIN
    update ruta set ruta=rutaR,lugarInico=lugarInicioR, lugarFin=lugarFinR, idZona=idZonaR
     where id=idR;
    return 1;
END;
$$ LANGUAGE plpgsql;


-------------------------------------------------------------------------------------------------------------

create table horario(
    id serial primary key,
    fecha date not null,
    hora time not null,
    estado boolean not null,
    idRuta serial not null,
    constraint fk1_horario foreign key(idRuta) references ruta(id)
);

------- CRUD horario --------------------------------

CREATE OR REPLACE FUNCTION insertarHorario(
 fecha date ,hora time,estado boolean,rutaID int
)
RETURNS void AS $$
BEGIN
INSERT INTO horario(fecha , hora,estado ,rutaID)
VALUES(fecha  , hora,estado ,rutaID);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION eliminarHorario(
idH int
)
RETURNS int AS $$
BEGIN
    delete from horario where id=idH;
    return 1;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION modificarHorario(
idH int,fecha date,hora time ,estado boolean,rutaID int
)
RETURNS int AS $$
BEGIN
    update horario set fecha=fechaH,  hora=horaF,estado=estadoH,rutaID=rutaIDH,
    idHorario=idHorarioH where id=idM;
    return 1;
END;
$$ LANGUAGE plpgsql;

--------------------------------------------------------------------------------------------------------------------------------

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

-----------------CRUD recoleccion

CREATE FUNCTION insertar_recoleccion(
    observacions VARCHAR,
    Personal_IDs int,
    Maquinaria_IDs int,
    Residuo_IDs int,
    Horario_IDs int,
    Usuario_IDs int
)
RETURNS void AS $$
BEGIN
    INSERT INTO RECOLECCION(observacion, Personal_ID, Maquinaria_ID, Residuo_ID, Horario_ID, Usuario_ID)
    VALUES(observacions, Personal_IDs, Maquinaria_IDs, Residuo_IDs, Horario_IDs, Usuario_IDs);
END;
$$ LANGUAGE plpgsql;


CREATE FUNCTION eliminar_recoleccion(
    ids int
)
RETURNS void AS $$
BEGIN
    DELETE FROM RECOLECCION WHERE id = ids;
END;
$$ LANGUAGE plpgsql;


CREATE FUNCTION actualizar_recoleccion(
    ids int,
    observacions VARCHAR,
    Personal_IDs int,
    Maquinaria_IDs int,
    Residuo_IDs int,
    Horario_IDs int,
    Usuario_IDs int
)
RETURNS void AS $$
BEGIN
    UPDATE RECOLECCION SET observacion = observacions, Personal_ID = Personal_IDs, Maquinaria_ID = Maquinaria_IDs, Residuo_ID = Residuo_IDs, Horario_ID = Horario_IDs, Usuario_ID = Usuario_IDs WHERE id = ids;
END;
$$ LANGUAGE plpgsql;

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

----------CRUD detalle_incentivo

CREATE OR REPLACE FUNCTION insertarDetalleIncentivo(
    nombres varchar(30),
    cantidads int,
    idTipoIncentivos int,
    idDetalleRecps int
) RETURNS void AS $ $ BEGIN
INSERT INTO
    detalle_incentivo(
        nombre,
        cantidad,
        TIPO_INCENTIVO_ID,
        idDetalleRecp
    )
VALUES
    (
        nombres,
        cantidads,
        idTipoIncentivos,
        idDetalleRecps
    );

END;

$ $ LANGUAGE plpgsql;

--funcion para modificar detalle incentivo
CREATE OR REPLACE FUNCTION modificarDetalleIncentivo(
    idDetalleIncentivos int,
    cantidads int,
    idTipoIncentivos int,
    idDetalleRecps int
) RETURNS void AS $ $ BEGIN
    UPDATE detalle_incentivo SET cantidad = cantidads, TIPO_INCENTIVO_ID = idTipoIncentivos, idDetalleRecp = idDetalleRecps WHERE id = idDetalleIncentivos;
END;

--funcion para eliminar detalle incentivo
CREATE OR REPLACE FUNCTION eliminarDetalleIncentivo(
    idDetalleIncentivos int
) RETURNS void AS $ $ BEGIN
    DELETE FROM detalle_incentivo WHERE id = idDetalleIncentivos;
END;
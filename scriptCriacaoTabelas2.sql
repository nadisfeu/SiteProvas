DROP TABLE IF EXISTS atividade CASCADE;

CREATE TABLE atividade
(
    atvID integer NOT NULL,
    academico_email CHAR(22),
    institucao CHAR(22),
    disciplica CHAR(22),
    numQuest integer,
    caminhoArquivo CHAR(22),
    PRIMARY KEY (atvID),
	FOREIGN KEY (academico_email) REFERENCES academico (email)
);

DROP TABLE IF EXISTS academico CASCADE;

CREATE TABLE academico
(
    email CHAR(22) NOT NULL,
    nome CHAR(22) NOT NULL,
    instituicao CHAR(22),
    PRIMARY KEY (email)
);

DROP TABLE IF EXISTS lista CASCADE;

CREATE TABLE lista
(
    gabarito boolean DEFAULT false,
	PRIMARY KEY(atvID)
)INHERITS (atividade);

insert into lista values (1,'bruno@ufop', 'ufop','BD',10,'drive.com',true);
insert into lista values (2,'ryan@ufop', 'ufop','AEDS 1',5,'drive.com',false);
insert into lista values (2,'fernando@ufop', 'ufop','Programacao 1',6,'drive.com',false);
insert into lista values (4,'paulo@ufop', 'ufop','Redes 1',9,'drive.com',true);

DROP TABLE IF EXISTS prova CASCADE;

CREATE TABLE prova
(
    tipo integer DEFAULT 1,
	PRIMARY KEY(atvID)
)INHERITS (atividade);

DROP TABLE IF EXISTS professor CASCADE;

CREATE UNLOGGED TABLE professor
(
    dep CHAR(22),
    sala CHAR(22),
	PRIMARY KEY(email)
)INHERITS (academico);

DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
    curso CHAR(22),
	PRIMARY KEY(email)
)INHERITS (academico);

DROP TABLE IF EXISTS pesquisa CASCADE;

CREATE TABLE pesquisa
(
    atvID_atividade integer,
    email_academico CHAR(22),

	FOREIGN KEY (atvID_atividade) REFERENCES atividade (atvID),
	FOREIGN KEY (email_academico) REFERENCES academico (email)
);

select * from lista;

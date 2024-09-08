DROP TABLE IF EXISTS atividade CASCADE;

CREATE TABLE atividade
(
    "atvID" integer NOT NULL,
    academico_email CHAR(22),
    institucao CHAR(22),
    disciplica CHAR(22),
    "numQuest" integer,
    "caminhoArquivo" CHAR(22),
    PRIMARY KEY ("atvID")
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
    gabarito boolean DEFAULT false
)INHERITS (atividade);

insert into lista values (1,'carlos@ufop', 'ufop','BD',)

DROP TABLE IF EXISTS prova CASCADE;

CREATE TABLE prova
(
    tipo integer DEFAULT 1
)INHERITS (atividade);

DROP TABLE IF EXISTS professor CASCADE;

CREATE UNLOGGED TABLE professor
(
    dep CHAR(22),
    sala CHAR(22)
)INHERITS (academico);

DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
    curso CHAR(22)
)INHERITS (academico);

DROP TABLE IF EXISTS pesquisa CASCADE;

CREATE TABLE pesquisa
(
    "atvID_atividade" integer,
    email_academico CHAR(22)
);

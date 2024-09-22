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

-- atributos lista (atvID, academico_email, instituicao, disciplina,nunQuest,caminhoArquivo,Gabarito)

insert into lista values (1,'bruno@ufop', 'ufop','BD',10,'drive.py.com',true);
insert into lista values (2,'ryan@ufop', 'ufop','AEDS 1',5,'drive.py.com',false);
insert into lista values (3,'fernando@ufop', 'ufop','Programacao 1',6,'drive.py.com',false);
insert into lista values (4,'paulo@ufop', 'ufop','Redes 1',9,'drive.py.com',true);

DROP TABLE IF EXISTS prova CASCADE;

CREATE TABLE prova
(
    tipo integer DEFAULT 1,
	PRIMARY KEY(atvID)
)INHERITS (atividade);

-- atributos prova (atvID, academico_email, instituicao, disciplina,nunQuest,caminhoArquivo,tipo)

insert into prova values (1,'bruno@ufop', 'ufop','BD',10,'drive.py.com',1);
insert into prova values (2,'ryan@ufop', 'ufop','AEDS 1',5,'drive.py.com',2);
insert into prova values (3,'fernando@ufop', 'ufop','Programacao 1',6,'drive.py.com',3);
insert into prova values (4,'paulo@ufop', 'ufop','Redes 1',9,'drive.py.com',9);

DROP TABLE IF EXISTS professor CASCADE;

CREATE UNLOGGED TABLE professor
(
    dep CHAR(22),
    sala CHAR(22),
	PRIMARY KEY(email)
)INHERITS (academico);

-- atributos professor (email, nome, instituicao, departamento,sala)
insert into professor values ('alexandre@ufop', 'Alexandre','UFOP','DECSI','A301');
insert into professor values ('eduardo@ufop', 'Eduardo','UFOP','DECSI','A303');
insert into professor values ('filipe@ufop', 'Filipe','UFOP','DECSI','A302');
insert into professor values ('juvenil@ufop', 'Juvenil','UFOP','DECEA','A304');

DROP TABLE IF EXISTS aluno CASCADE;

CREATE TABLE aluno
(
    curso CHAR(22),
	PRIMARY KEY(email)
)INHERITS (academico);

-- atributos aluno (email, nome, instituicao, curso)

insert into aluno values ('ryan@ufop', 'Ryan','UFOP','Computacao');
insert into aluno values ('fernando@ufop', 'Fernando','UFOP','Computacao');
insert into aluno values ('paulo@ufop', 'Paulo','UFOP','Computacao');
insert into aluno values ('junin@ufop', 'Junior','UFOP','Producao');

DROP TABLE IF EXISTS pesquisa CASCADE;


CREATE TABLE pesquisa
(
    atvID_atividade integer,
    email_academico CHAR(22),

	FOREIGN KEY (atvID_atividade) REFERENCES atividade (atvID),
	FOREIGN KEY (email_academico) REFERENCES academico (email)
);

-- atributos pesquisa (atvID, email_academico)

insert into pesquisa values (2,'bruno@ufop');
insert into pesquisa values (3,'ryan@ufop');

select * from aluno;
-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;

DROP TABLE IF EXISTS atividade CASCADE;
CREATE TABLE IF NOT EXISTS public.atividade
(
    "atvid" integer NOT NULL,
    academico_email "varchar",
    instituicao "varchar",
    disciplina "varchar",
    "numquest" integer,
    "caminhoarquivo" "varchar",
    PRIMARY KEY ("atvid")
);

DROP TABLE IF EXISTS academico CASCADE;
CREATE TABLE IF NOT EXISTS public.academico
(
    email "varchar" NOT NULL,
    nome "varchar" NOT NULL,
	tipo "varchar" NOT NULL,
    instituicao "varchar",
    PRIMARY KEY (email)
);

DROP TABLE IF EXISTS lista CASCADE;
CREATE TABLE IF NOT EXISTS public.lista
(
    gabarito boolean DEFAULT false,
    "atvid" integer NOT NULL,
    PRIMARY KEY ("atvid")
);

DROP TABLE IF EXISTS prova CASCADE;
CREATE TABLE IF NOT EXISTS public.prova
(
    tipo integer DEFAULT 1,
    "atvid" integer NOT NULL,
    PRIMARY KEY ("atvid")
);

DROP TABLE IF EXISTS pesquisa CASCADE;
CREATE TABLE IF NOT EXISTS public.pesquisa
(
    "atvid_atividade" integer NOT NULL,
    email_academico "varchar" NOT NULL,
    PRIMARY KEY ("atvid_atividade", email_academico)
);

DROP TABLE IF EXISTS conteudo CASCADE;
CREATE TABLE IF NOT EXISTS public.conteudo
(
    materia "varchar" NOT NULL,
    "atvid" integer NOT NULL,
    PRIMARY KEY (materia, "atvid")
);

ALTER TABLE IF EXISTS public.atividade
    ADD CONSTRAINT "ENVIA" FOREIGN KEY (academico_email)
    REFERENCES public.academico (email) MATCH FULL
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.lista
    ADD FOREIGN KEY ("atvid")
    REFERENCES public.atividade ("atvid") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
	
ALTER TABLE IF EXISTS public.prova
    ADD FOREIGN KEY ("atvid")
    REFERENCES public.atividade ("atvid") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

ALTER TABLE IF EXISTS public.pesquisa
    ADD CONSTRAINT pesquisada FOREIGN KEY ("atvid_atividade")
    REFERENCES public.atividade ("atvid") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.pesquisa
    ADD CONSTRAINT pesquisa FOREIGN KEY (email_academico)
    REFERENCES public.academico (email) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.conteudo
    ADD FOREIGN KEY ("atvid")
    REFERENCES public.atividade ("atvid") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;

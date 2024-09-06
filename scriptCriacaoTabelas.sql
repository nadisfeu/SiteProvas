-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.atividade
(
    "atvID" integer NOT NULL,
    academico_email "char"[],
    institucao "char"[],
    disciplica "char"[],
    "numQuest" integer,
    PRIMARY KEY ("atvID")
);

CREATE TABLE IF NOT EXISTS public.academico
(
    email "char"[] NOT NULL,
    nome "char"[] NOT NULL,
    instituicao "char"[],
    PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS public.lista
(
    gabarito boolean DEFAULT false,
    "atvID" integer
);

CREATE TABLE IF NOT EXISTS public.prova
(
    tipo integer DEFAULT 1,
    "atvdID" integer
);

CREATE UNLOGGED TABLE IF NOT EXISTS public.professor
(
    dep "char"[],
    sala "char"[],
    email_academico "char"[]
);

CREATE TABLE IF NOT EXISTS public.aluno
(
    curso "char"[],
    email_academico "char"[]
);

CREATE TABLE IF NOT EXISTS public.pesquisa
(
    "atvID_atividade" integer,
    email_academico "char"[]
);

ALTER TABLE IF EXISTS public.atividade
    ADD FOREIGN KEY (academico_email)
    REFERENCES public.academico (email) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.lista
    ADD FOREIGN KEY ("atvID")
    REFERENCES public.atividade ("atvID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.prova
    ADD FOREIGN KEY ("atvdID")
    REFERENCES public.atividade ("atvID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.professor
    ADD FOREIGN KEY (email_academico)
    REFERENCES public.academico (email) MATCH SIMPLE
    ON UPDATE RESTRICT
    ON DELETE RESTRICT
    DEFERRABLE INITIALLY DEFERRED
    NOT VALID;


ALTER TABLE IF EXISTS public.aluno
    ADD FOREIGN KEY (email_academico)
    REFERENCES public.academico (email) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.pesquisa
    ADD CONSTRAINT pesquisada FOREIGN KEY ("atvID_atividade")
    REFERENCES public.atividade ("atvID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.pesquisa
    ADD CONSTRAINT pesquisa FOREIGN KEY (email_academico)
    REFERENCES public.academico (email) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;
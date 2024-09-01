-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Atividade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Atividade` (
  `atvID` INT NOT NULL,
  `instituicao` VARCHAR(45) NOT NULL,
  `disciplina` VARCHAR(45) NULL,
  `numQuest` INT NULL,
  PRIMARY KEY (`atvID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Academico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Academico` (
  `instituicao` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `Atividade_atvID` INT NULL,
  PRIMARY KEY (`email`),
  INDEX `fk_Academico_Atividade1_idx` (`Atividade_atvID` ASC) VISIBLE,
  CONSTRAINT `fk_Academico_Atividade1`
    FOREIGN KEY (`Atividade_atvID`)
    REFERENCES `mydb`.`Atividade` (`atvID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pesquisa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pesquisa` (
  `Atividade_atvID` INT NOT NULL,
  `Academico_email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Academico_email`, `Atividade_atvID`),
  INDEX `fk_Atividade_has_Academico_Academico1_idx` (`Academico_email` ASC) VISIBLE,
  INDEX `fk_Atividade_has_Academico_Atividade1_idx` (`Atividade_atvID` ASC) VISIBLE,
  CONSTRAINT `fk_Atividade_has_Academico_Atividade1`
    FOREIGN KEY (`Atividade_atvID`)
    REFERENCES `mydb`.`Atividade` (`atvID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Atividade_has_Academico_Academico1`
    FOREIGN KEY (`Academico_email`)
    REFERENCES `mydb`.`Academico` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`lista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`lista` (
  `gabarito` INT NULL,
  `Atividade_atvID` INT NOT NULL,
  PRIMARY KEY (`Atividade_atvID`),
  CONSTRAINT `fk_lista_Atividade1`
    FOREIGN KEY (`Atividade_atvID`)
    REFERENCES `mydb`.`Atividade` (`atvID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`prova`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`prova` (
  `tipo` INT NULL,
  `Atividade_atvID` INT NOT NULL,
  PRIMARY KEY (`Atividade_atvID`),
  CONSTRAINT `fk_prova_Atividade1`
    FOREIGN KEY (`Atividade_atvID`)
    REFERENCES `mydb`.`Atividade` (`atvID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`professor` (
  `departamento` VARCHAR(10) NULL,
  `sala` INT NULL,
  `Academico_email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Academico_email`),
  CONSTRAINT `fk_professor_Academico1`
    FOREIGN KEY (`Academico_email`)
    REFERENCES `mydb`.`Academico` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`aluno` (
  `curso` VARCHAR(45) NULL,
  `Academico_email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Academico_email`),
  CONSTRAINT `fk_aluno_Academico1`
    FOREIGN KEY (`Academico_email`)
    REFERENCES `mydb`.`Academico` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

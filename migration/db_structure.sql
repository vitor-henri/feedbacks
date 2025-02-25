CREATE DATABASE db_feedbacks;

USE db_feedbacks;

CREATE TABLE tb_feedback( 
	code_user int PRIMARY KEY AUTO_INCREMENT,
	name_user VARCHAR(80) NOT NULL,
    comentario TEXT not null,
    data_comentario DATETIME not null
);

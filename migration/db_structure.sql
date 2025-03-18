CREATE DATABASE IF NOT EXISTS db_feedback;

USE db_feedback;

CREATE TABLE IF NOT EXISTS tb_feedback (
	code_user INT PRIMARY KEY AUTO_INCREMENT,
	name_user VARCHAR(150) NOT NULL,
    comentario TEXT NOT NULL,
    data_comentario DATETIME DEFAULT NOW()
);


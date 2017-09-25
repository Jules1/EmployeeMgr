DROP DATABASE IF EXISTS EmployeeManager;
CREATE DATABASE EmployeeManager;
USE EmployeeManager;


CREATE TABLE employee(
    emp_id int not null auto_increment,
    fname varchar(20) not null,
    lname varchar(30) not null,
    position varchar(30) not null,
    location varchar(30) not null,
    startdate date,
    duration int(3),
    enddate date,
    vacationEnt int(3) default '10',
    vacationtaken int(3) not null default '0',
    vacationBalance int(3) not null default '0',
    sickLeaveTaken int(3) not null default '0',
    sickLeaveBalance int(3) not null default '0',
    leaveNoPay int(3) not null default '0',
    salary decimal(10,2) not null default '0',
    retention decimal(10,2) not null default '0',
    netBasicSalary decimal(10,2) not null default '0',
    score int(3),
    primary_key(emp_id)
);
    
    
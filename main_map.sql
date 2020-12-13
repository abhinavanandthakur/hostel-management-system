/*Create tables*/

create table rooms (
    roomNo int primary key,
    floor int
);
create table boarders(
    rollNo int primary key,
    firstName varchar(15),
    lastName varchar(15),
    phoneNumber varchar(10) unique,
    department varchar(20),
    programme varchar(20),
    email varchar(30) unique,
    dateOfBirth date,
    address varchar(40),
    roomNo int unique,
    foreign key (roomNo) references rooms(roomNo) on delete set null
);

create table representatives (
    role varchar(15) primary key,
    rollNo int unique,
    foreign key (rollNo) references boarders(rollNo) on delete set null
);
/*View table descriptions*/
describe boarders;
describe rooms;
describe representatives;
/*Insert data into tables*/
insert into rooms values
(101,1),(102,1),(103,1),(104,1),(105,1),
(201,2),(202,2),(203,2),(204,2),(205,2),
(301,3),(302,3),(303,3),(304,3),(305,3),
(401,4),(402,4),(403,4),(404,4),(405,4);
insert into boarders values
(18001,"Ankit","Agarwala","6548932175",'CSE','Btech','agar@gmail.com','1998-10-28','Bhetapara',101),
(18002,"Aditya","Dey","6548462175",'CSE','Btech','adir@gmail.com','1999-11-18','Maligaon',204),
(18003,"Abhinav","Anand","6548945375",'CSE','Btech','abhi@gmail.com','1999-01-17','Deoghar',303),
(18004,"Gautam","Baishya","6898462175",'CSE','Btech','gtm@gmail.com','1998-12-16','Assam',402);
insert into representatives values
('Prefect',18004),
('Assistant Prefect',18002),
('Mess Coordinator',18003),
('1st Floor Representative',18001);




/*View tables fully*/
select * from boarders;
select * from rooms;
select * from representatives;
















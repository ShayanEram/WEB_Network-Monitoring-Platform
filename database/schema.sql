-- schema.sql

-- Contains every SQL table.

CREATE TABLE devices (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ip_address VARCHAR(45),
    mac_address VARCHAR(50),
    hostname VARCHAR(255)
);

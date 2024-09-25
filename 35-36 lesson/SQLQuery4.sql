CREATE DATABASE Airportdb
GO

USE Airportdb

-- Створюємо таблицю Flights
CREATE TABLE Flights (
	flight_id INT PRIMARY KEY,
	flight_number NVARCHAR(10),
	departure_time DATETIME,
	arrival_time DATETIME,
	origin NVARCHAR(50),
	destination NVARCHAR(50),
	airline NVARCHAR(50)
);
GO

-- Додаємо нові записи в таблицю Flights
INSERT INTO Flights (flight_id, flight_number, departure_time, arrival_time, origin, destination, airline)
VALUES
(1, 'AZ101', '2024-10-01 06:45:00', '2024-10-01 09:30:00', 'Kyiv', 'Rome', 'Alitalia'),
(2, 'AF202', '2024-10-02 08:15:00', '2024-10-02 10:45:00', 'Odesa', 'Paris', 'Air France'),
(3, 'LH303', '2024-10-03 12:00:00', '2024-10-03 14:30:00', 'Lviv', 'Frankfurt', 'Lufthansa'),
(4, 'RY404', '2024-10-04 14:30:00', '2024-10-04 16:45:00', 'Dnipro', 'Warsaw', 'Ryanair'),
(5, 'BA505', '2024-10-05 18:00:00', '2024-10-05 20:30:00', 'Kharkiv', 'London', 'British Airways');
GO

-- Створюємо таблицю Passengers
CREATE TABLE Passengers (
    passenger_id INT PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    passport_number NVARCHAR(20) NOT NULL,
    nationality NVARCHAR(50) NOT NULL
);
GO

-- Додаємо нові записи в таблицю Passengers
INSERT INTO Passengers (passenger_id, first_name, last_name, passport_number, nationality)
VALUES
(1, 'Dmytro', 'Kovalenko', 'UA654321', 'Ukraine'),
(2, 'Sophia', 'Müller', 'DE789456', 'Germany'),
(3, 'Isabella', 'Rossi', 'IT456123', 'Italy'),
(4, 'John', 'Smith', 'GB987654', 'United Kingdom');
GO

-- Створюємо таблицю Tickets
CREATE TABLE Tickets (
    ticket_id INT PRIMARY KEY,
    flight_id INT NOT NULL,
    ticket_class NVARCHAR(20) NOT NULL,
    price MONEY NOT NULL,
    passenger_id INT,
    FOREIGN KEY (flight_id) REFERENCES Flights(flight_id),
    FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id)
);
GO

-- Додаємо нові записи в таблицю Tickets
INSERT INTO Tickets (ticket_id, flight_id, ticket_class, price, passenger_id)
VALUES
(1, 1, 'Economy', 180.00, 1),
(2, 1, 'Business', 500.00, 2),
(3, 2, 'Economy', 220.00, 3),
(4, 2, 'First Class', 800.00, 4),
(5, 3, 'Economy', 150.00, 1),
(6, 3, 'Business', 470.00, 2),
(7, 4, 'Economy', 190.00, 3),
(8, 5, 'First Class', 900.00, 4);
GO

-- Створюємо таблицю для логів квитків
CREATE TABLE Ticket_Log (
    log_id INT PRIMARY KEY IDENTITY(1, 1),
    ticket_id INT,
    flight_id INT,
    passenger_id INT,
    purchase_time DATETIME DEFAULT GETDATE()
);

-- Створюємо View для тривалості польотів
CREATE VIEW View_Flights_Duration AS
SELECT flight_id, flight_number, origin, destination,
    departure_time, arrival_time,
    DATEDIFF(HOUR, departure_time, arrival_time) AS duration_hours
FROM Flights;

-- Створюємо View для польотів сьогодні
CREATE VIEW View_Today_Flights AS
SELECT *
FROM Flights
WHERE CONVERT(DATE, departure_time) = CONVERT(DATE, GETDATE());

-- Створюємо тригер для логування після вставки квитка
CREATE TRIGGER trg_AfterInsertTicket
ON Tickets
AFTER INSERT
AS
BEGIN
    INSERT INTO Ticket_Log (ticket_id, flight_id, passenger_id)
    SELECT ticket_id, flight_id, passenger_id
    FROM inserted;
END;
GO

-- #1: Вибір рейсів до Лондона 1 вересня 2024 року
SELECT *
FROM Flights
WHERE destination = 'London' AND CONVERT(DATE, departure_time) = '2024-10-05'
ORDER BY departure_time;

-- #2: Вибір тривалості рейсів у хвилинах і сортування за спаданням тривалості
SELECT *, DATEDIFF(MINUTE, departure_time, arrival_time) AS duration
FROM Flights
ORDER BY DATEDIFF(MINUTE, departure_time, arrival_time) DESC;

-- #3: Вибір рейсів, тривалість яких більше ніж 2 години
SELECT *
FROM Flights
WHERE DATEDIFF(HOUR, departure_time, arrival_time) > 2;

-- #4: Підрахунок кількості рейсів за напрямками
SELECT destination, COUNT(*) AS flight_count
FROM Flights
GROUP BY destination;

-- #5: Напрямок з найбільшою кількістю рейсів
SELECT TOP 1 destination, COUNT(*) AS flight_count
FROM Flights
GROUP BY destination
ORDER BY COUNT(*) DESC;

-- #6: Підрахунок рейсів у червні 2024 року за напрямками та загальна кількість рейсів
SELECT destination, COUNT(*) AS flight_count
FROM Flights
WHERE MONTH(departure_time) = 6 AND YEAR(departure_time) = 2024
GROUP BY destination;

SELECT COUNT(*) AS total_flights
FROM Flights
WHERE MONTH(departure_time) = 6 AND YEAR(departure_time) = 2024;

-- #7: Вибір рейсів з квитками бізнес-класу без пасажира сьогодні
SELECT f.*
FROM Flights f
JOIN Tickets t ON f.flight_id = t.flight_id
WHERE t.ticket_class = 'Business' AND t.passenger_id IS NULL AND CONVERT(DATE, f.departure_time) = CONVERT(DATE, GETDATE());

-- #8: Підрахунок проданих квитків і доходу від рейсів 7 вересня 2024 року
SELECT f.flight_id, COUNT(t.ticket_id) AS tickets_sold, SUM(t.price) AS total_revenue
FROM Flights f
JOIN Tickets t ON f.flight_id = t.flight_id
WHERE CONVERT(DATE, f.departure_time) = '2024-10-05'
GROUP BY f.flight_id;

-- #9: Підрахунок проданих квитків для рейсів 4 вересня 2024 року
SELECT f.flight_id, f.flight_number, COUNT(t.ticket_id) AS ticket_sold
FROM Flights f
JOIN Tickets t ON f.flight_id = t.flight_id
WHERE CONVERT(DATE, f.departure_time) = '2024-10-04'
GROUP BY f.flight_id, f.flight_number;

-- #10: Вибір номерів рейсів і напрямків
SELECT flight_number, destination
FROM Flights;

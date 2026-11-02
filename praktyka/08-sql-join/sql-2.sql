-- Робота 8. SQL: обʼєднання і агрегація. База data/chinook.db
-- Під кожним рядком «-- N.» — ОДИН запит. Рядки з «--» — коментарі, їх можна дописувати.
-- Перевірка:  python praktyka/08-sql-join/perevir.py

-- 1. Треки гурту Queen: трек, альбом
SELECT t.Name, al.Title AS AlbumTitle
FROM Track t 
JOIN Album al ON t.AlbumId = al.AlbumId 
JOIN Artist ar ON al.ArtistId = ar.ArtistId 
WHERE ar.Name = 'Queen';

-- 2. Скільки треків у кожному жанрі: жанр, кількість; від найбільшого
SELECT g.Name, COUNT(*) AS TracksCount 
FROM Track t 
JOIN Genre g ON t.GenreId = g.GenreID 
GROUP BY g.GenreId, g.Name 
ORDER BY TracksCount DESC;

-- 3. Топ-10 клієнтів за сумою покупок: імʼя, прізвище, сума; від найбільшої
SELECT c.FirstName, c.LastName, SUM(i.TOTAL) AS sum 
FROM Customer c 
JOIN Invoice i ON c.CustomerId = i.CustomerID 
GROUP BY c.CustomerId, c.FirstName, c.LastName 
ORDER BY sum DESC 
LIMIT 10;

-- 4. Виконавці, у яких більше 5 альбомів: виконавець, альбомів; від найбільшого
SELECT ar.Name, COUNT(*) AS Albums 
FROM Artist ar 
JOIN Album al ON ar.ArtistId = al.ArtistId 
GROUP BY ar.ArtistId, ar.Name 
HAVING COUNT(*) > 5 
ORDER BY Albums DESC;

-- 5. Виконавці без жодного альбому
SELECT ar.Name 
FROM Artist ar 
LEFT JOIN Album al ON al.ArtistId = ar.ArtistId 
WHERE al.AlbumId IS NULL; 

-- 6. Середня тривалість треку по жанрах, у хвилинах з одним знаком: жанр, хвилин; від найдовшої
SELECT g.Name, ROUND(AVG(t.Milliseconds) / 60000.0, 1) AS Minutes 
FROM Track t 
JOIN Genre g ON t.GenreId = g.GenreId 
GROUP BY g.GenreId, g.Name 
ORDER BY Minutes DESC;

-- 7. Виторг за країнами (за рахунками): країна, сума; від найбільшого
SELECT BillingCountry, ROUND(SUM(Total), 2) AS Sum 
FROM Invoice 
GROUP BY BillingCountry 
ORDER BY Sum DESC; 

-- 8. Співробітники підтримки й скільки клієнтів у кожного: імʼя, прізвище, клієнтів; від найбільшого
SELECT e.FirstName, e.LastName, COUNT(*) AS NumberOfClients 
FROM Employee e 
JOIN Customer c ON e.EmployeeId = c.SupportRepId 
GROUP BY e.EmployeeId, e.FirstName, e.LastName 
ORDER BY NumberOfClients DESC; 

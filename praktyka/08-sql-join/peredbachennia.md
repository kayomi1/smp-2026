# Мої передбачення

| # | Запит | Передбачення |
| --- | --- | --- |
| A | `SELECT COUNT(*) FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId` | Покаже число 347 |
| B | `SELECT COUNT(*) FROM Artist LEFT JOIN Album ON Artist.ArtistId = Album.ArtistId` | Покаже число 347 + ?, якесь число виконавців з значенням NULL |
| C | `SELECT COUNT(*) FROM Artist, Album` | З'єднає кожен з кожним та покаже 347 x 275 |
| D | `SELECT COUNT(*) FROM Track WHERE GenreId = 1 GROUP BY AlbumId — скільки рядків?` | Покаже по рядку на кожен альбом, де є треки жанру 1 |
| E | `SELECT SUM(Total), COUNT(*) FROM Invoice WHERE BillingCountry = 'Ukraine'` | Якщо Україна є у базі, то має повернути суму всіх її рахунків і кількість цих рахунків. Якщо ні то поверне NULL і 0 |

A. Показав `347`. Я **Вгадав**
B. Показав `418`. Я **Вгадав**
C. Показав `95425`. Я **Вгадав**
D. Показав `Показав 117 рядків`. Я напевно **Вгадав**
E. Показав `NULL | 0`. Я **Вгадав**, але України не було у базі

-- შექმენით მონაცემთა ბაზა სახელად IT_STEP
CREATE DATABASE `IT_STEP`

-- 1. დაწერეთ SQL რომელიც შექმნის Author ცხრილს, რომელსაც ექნება პირველადი გასაღები
CREATE TABLE Author (
    AuthorID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(50) NOT NULL
);

-- 2. დაწერეთ SQL რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID 
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Year INT NOT NULL
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
);

-- 3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს
INSERT INTO Author (AuthorID, Name) VALUES
(1, 'Nodar Dumbadze'),
(2, 'Ilia Chavchavadze'),
(3, 'Vazha Pshavela'),
(4, 'George Bernard Shaw,'),
(5, 'Jules Verne'),
(6, 'Astrid Lindgren'),
(7, 'Erich Maria Remarque');

INSERT INTO Books (BookID, Title, Year, AuthorID) VALUES
(1, 'მე ვხედავ მზეს', 1962),
(2, 'კაცია-ადამიანი?!', 1858, 2),
(3, 'სტუმარ-მასპინძელი', 1893, 3),
(4, 'Pygmalion', 1912, 4),
(5, 'Around the World in Eighty Days', 1872, 5),
(6, 'The Adventures of Tom Sawyer', 1876, 6),
(7, 'Arch of Triumph', 1945, 7);


-- 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტულ ჩანაწერის ერთ-ერთ ველის მნიშვნელობას
UPDATE Books SET Title = 'მარადისობის კანონი' Year = 1978 WHERE BookID = 1;

-- 5. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან
DELETE FROM Author;

DELETE FROM Books;

-- 6. წაშალეთ Author და Books ცხრილები
DROP TABLE Author;

DROP TABLE Books;

# თითოეული ბრძანებისთვის გამოიყენეთ ლიმიტი 10

# 1. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მხოლოდ customerName, phone, city, country ველებს.(ლიმიტი 10)

SELECT customerName, phone, city, country FROM customers Limit 10;

# 2. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ ყველა იმ ჩანაწერს რომლის ფოსტის კოდი მეტია 1370ზე ან salesRepEmployeeNumber მეტია 150 (ლიმიტი 10)

SELECT * FROM customers WHERE postalCode > 1370 OR salesRepEmployeeNumber > 150 LIMIT 10;

# 3. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ ისეთ ჩანაწერს, რომელშიც customerName შეიცავს 'Mini' ტექსტს (ლიმიტი 10)

SELECT * FROM customers WHERE customerName LIKE '%Mini%' LIMIT 10;

# 4. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მონაცემებს, რომელსაც აქვს state 'CA' ან 'NY'(ლიმიტი 10)

SELECT * FROM customers WHERE state IN ('CA', 'NY') LIMIT 10;

# 5. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მონცემებს, რომელსაც აქვს creditLimit 10000-ზე მეტი (ლიმიტი 10)

SELECT * FROM customers WHERE creditLimit > 10000 LIMIT 10;

-- create an `expense` table that has `id`, `name`, `description` and `amount`
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    amount INTEGER
);

-- Create an `income` table that has `id`, `name`, `type` and `amount`
CREATE TABLE income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    amount INTEGER,    
);
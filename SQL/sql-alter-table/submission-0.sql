CREATE TABLE books (
  id INTEGER,
  title TEXT,
  author TEXT
);
-- Do not modify above this line --

-- Add a new column called published_year of type INTEGER to the table 
ALTER TABLE books ADD COLUMN published_year INTEGER;

-- Modify the id column to be called isbn instead
ALTER TABLE books RENAME COLUMN id TO isbn;

-- Drop the author column from the table
ALTER TABLE books DROP COLUMN author;









-- Do not modify below this line --
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'books'
ORDER BY column_name;

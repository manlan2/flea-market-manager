-- This file contains test data for the flea market app.
-- It can be loaded into the database via the sqlites command line interface
-- using the following commands:
--
-- `sqlite3 fleamarket.db`
-- `.read test_data.sql`
-- TODO: add time created to each items
-- TODO: add picture link for each items
-- TODO: add picture link for each booth

-- Booths
INSERT INTO booths (name) VALUES ("Brenda's Small Treasures");
INSERT INTO booths (name) VALUES ("Classic Furniture");
INSERT INTO booths (name) VALUES ("Todd's Toy Land");
INSERT INTO booths (name) VALUES ("China Express");
INSERT INTO booths (name) VALUES ("Timeless Tools");
INSERT INTO booths (name) VALUES ("Mantel Decor and More");

-- Items
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Chair", "19th Century Sitting Chair", "$350", "Furniture", 2);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Table", "1970's Laminated Dinning Room Table", "$50", "Furniture", 2);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Dresser", "20th Century IKEA Dresser", "$35", "Furniture", 2);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Necklace", "Silver Necklace with Diamond Pendant", "$150", "Jewelry", 1);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Potato Masher", "19th Century Hand Potato Masher", "$15", "Kitchen", 1);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Decorative Walking Stick", "Hand carved decorative walking stick", "$35", "Home Decor", 1);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Hot Wheels Corvette", "1980's Hot Wheels Red Corvette", "$10", "Toys", 3);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Train Set", "1950's Lionel Train Set", "$350", "Toys", 3);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Rubber Band Gun", "New Six Shooter Rubber Band Gun", "$5", "Toys", 3);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Tea Set", "19th Century American Made Tea Set", "$370", "China", 4);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Pitcher", "18th Century English Made Water Pitcher", "$90", "China", 4);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Glasses", "McDonald's Muppets Collectors Cup Set", "$1,350", "China", 4);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Hammer", "20th Century Claw Hammer", "$5", "Tools", 5);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Drill", "19th Century Hand Drill with One Bit", "$35", "Tools", 5);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Hand Plane", "19th Century Hand Plane", "$350", "Tools", 5);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Painting", "Crappy Painting by Unknown Local Artist", "$350", "Art", 6);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Clock", "20th Century Mantel Clock", "$35", "Decor", 6);
INSERT INTO items (name, description, price, category, booth_id) VALUES ("Candlesticks", "Cheap Lead Laden Chinese Candlesticks", "$30", "Decor", 6);

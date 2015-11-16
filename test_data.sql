-- This file contains test data for the flea market app.
-- It can be loaded into the database via the sqlites command line interface
-- using the following commands:
--
-- `sqlite3 fleamarket.db`
-- `.read test_data.sql`

-- Onwer
INSERT INTO owner (name, email, picture) VALUES ("Larry Tooley", "larry@larrytooley.com", "");


-- Booths
INSERT INTO booths (name, image, email, phone, owner_id) VALUES ("Brenda's Small Treasures", "https://upload.wikimedia.org/wikipedia/commons/5/55/Map_marker_icon_%E2%80%93_Nicolas_Mollet_%E2%80%93_Leaf_%E2%80%93_Nature_%E2%80%93_white.png", "brenda@smalltreasures.com", "317-555-5551", 1);
INSERT INTO booths (name, image, email, phone, owner_id) VALUES ("Classic Furniture", "https://upload.wikimedia.org/wikipedia/commons/4/4e/Map_marker_icon_%E2%80%93_Nicolas_Mollet_%E2%80%93_Home_center_%E2%80%93_Stores_%E2%80%93_classic.png", "dave@classicfurniture.com", "317-555-5552", 1);
INSERT INTO booths (name, image, email, phone, owner_id) VALUES ("Todd's Toy Land", "https://upload.wikimedia.org/wikipedia/commons/7/7b/Map_marker_icon_%E2%80%93_Nicolas_Mollet_%E2%80%93_Toys_%E2%80%93_Stores_%E2%80%93_default.png", "todd@toddstoyland.com", "317-555-5553", 1);
INSERT INTO booths (name, image, email, phone, owner_id) VALUES ("China Express", "https://upload.wikimedia.org/wikipedia/commons/e/e7/Farm-Fresh_glass_narrow.png", "sam@chinaexpress.com", "317-555-5554", 1);
INSERT INTO booths (name, image, email, phone, owner_id) VALUES ("Timeless Tools", "https://upload.wikimedia.org/wikipedia/commons/a/a1/Farm-Fresh_hammer.png", "tim@timelesstools.com", "317-555-5555", 1);
INSERT INTO booths (name, image, email, phone, owner_id) VALUES ("Mantel Decor and More", "https://upload.wikimedia.org/wikipedia/commons/0/02/Farm-Fresh_candle.png", "melissa@manteldecor.com", "317-555-5556", 1);

-- Items
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Chair", "19th Century Sitting Chair", "$350", "Furniture", 2, "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Streit_Shakespeare_chair_side_view.jpg/145px-Streit_Shakespeare_chair_side_view.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Table", "1970's Laminated Dinning Room Table", "$50", "Furniture", 2, "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Aalto_table.JPG/320px-Aalto_table.JPG", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Dresser", "20th Century IKEA Dresser", "$35", "Furniture", 2, "https://c2.staticflickr.com/4/3099/2437342499_30bf03e296.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Necklace", "Silver Necklace with Diamond Pendant", "$150", "Jewelry", 1, "https://upload.wikimedia.org/wikipedia/commons/8/8a/Marcasite_necklace.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Potato Masher", "19th Century Hand Potato Masher", "$15", "Kitchen", 1, "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Potato_masher_2.jpg/320px-Potato_masher_2.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Decorative Walking Stick", "Hand carved decorative walking stick", "$35", "Home Decor", 1, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Walking_stick_made_with_bamboo_cane.jpg/178px-Walking_stick_made_with_bamboo_cane.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Hot Wheels Corvette", "1980's Hot Wheels Red Corvette", "$10", "Toys", 3, "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Hot_Wheels_Second_Wind_1976.jpg/278px-Hot_Wheels_Second_Wind_1976.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Train Set", "1950's Lionel Train Set", "$350", "Toys", 3, "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/PostWarLionel.jpg/159px-PostWarLionel.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Rubber Band Gun", "New Six Shooter Rubber Band Gun", "$5", "Toys", 3, "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Final_product_of_the_chopstick_rubber_band_gun.jpg/320px-Final_product_of_the_chopstick_rubber_band_gun.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Tea Set", "19th Century American Made Tea Set", "$370", "China", 4, "https://upload.wikimedia.org/wikipedia/commons/8/87/Tea_set.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Pitcher", "18th Century English Made Water Pitcher", "$90", "China", 4, "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Vincennes_Porcelain_Manufactory_-_Bowl_and_Water_Pitcher_with_Putti_Playing_Music_in_a_Pastoral_Setting_-_Walters_48535%2C_48723_-_Three_Quarter.jpg/206px-Vincennes_Porcelain_Manufactory_-_Bowl_and_Water_Pitcher_with_Putti_Playing_Music_in_a_Pastoral_Setting_-_Walters_48535%2C_48723_-_Three_Quarter.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Glasses", "McDonald's Muppets Collectors Cup Set", "$1,350", "China", 4, "https://img1.etsystatic.com/062/0/10239180/il_570xN.776843587_dl7w.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Hammer", "20th Century Claw Hammer", "$5", "Tools", 5, "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Claw-hammer.jpg/320px-Claw-hammer.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Drill", "19th Century Hand Drill with One Bit", "$35", "Tools", 5, "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Drill004cropped.jpg/320px-Drill004cropped.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Hand Plane", "19th Century Hand Plane", "$350", "Tools", 5, "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Garrett_Wade_Paragon_No._4_Smoothing_Plane.jpg/320px-Garrett_Wade_Paragon_No._4_Smoothing_Plane.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Painting", "Crappy Painting by Unknown Local Artist", "$350", "Art", 6, "https://upload.wikimedia.org/wikipedia/commons/d/d4/Lyme-regis%2C_Dorsetshire%2C_England%2C_watercolor_painting_by_Joseph_Mallord_William_Turnerc_c._1834.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Clock", "20th Century Mantel Clock", "$35", "Decor", 6, "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Vienna_-_Vintage_Table_or_Mantel_Clock_-_0578.jpg/159px-Vienna_-_Vintage_Table_or_Mantel_Clock_-_0578.jpg", 1);
INSERT INTO items (name, description, price, category, booth_id, image, owner_id) VALUES ("Candlesticks", "Cheap Lead Laden Candlesticks", "$30", "Decor", 6, "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Pair_of_Steuben_gold_Aurene_candlesticks.jpg/201px-Pair_of_Steuben_gold_Aurene_candlesticks.jpg", 1);

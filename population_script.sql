INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Kellogs', 'https://1000logos.net/wp-content/uploads/2020/07/Kelloggs-Logo.png', '19-02-1906');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('General Mills', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/General_Mills_logo.svg/1200px-General_Mills_logo.svg.png', '20-06-1928');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Nestle', 'https://www.logolynx.com/images/logolynx/c3/c33a7cf5132cce86b3479b8c34a2e844.jpeg', '10-08-1866');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Quaker Oats Company', 'https://en.wikipedia.org/wiki/Quaker_Oats_Company#/media/File:Quaker_Oats_logo_2017.png', '04-09-1877');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Nature´s Path', 'https://en.wikipedia.org/wiki/Nature%27s_Path#/media/File:Nature', 's_Path_logo.png', '12-05-1985');

INSERT INTO cereal_cerealcategory (name) VALUES('Vegan');
INSERT INTO cereal_cerealcategory (name) VALUES('Wheat');
INSERT INTO cereal_cerealcategory (name) VALUES('Oats');
INSERT INTO cereal_cerealcategory (name) VALUES('Sugary');

INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Bran flakes', 'A 30g serving contains:
Energy 425kJ / 100kcal, 5.0% of your RI
Fat 0.7g, 1.0% of your RI
Saturates 0.1g, 1% of your RI
Sugars 6.3g, 7% of your RI
Salt 0.27g, 5% of your RI', 4.99, false, 1, 1);
INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Cornflakes', 'A 30g serving contains:
Energy 481kJ / 113kcal, 6.0 % of your RI
Fat 0.2g, 0% of your RI
Saturates <0.1g, 0% of your RI
Sugars 2.2g, 2% of your RI
Salt 0.13g, 2% of your RI', 1.99, true, 1, 4);
INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Muesli with added sugar', 'A 50g serving contains:
Energy 755kJ / 183kcal, 9% of your RI
Fat 3.1g, 5% of your RI
Saturates 0.7g, 3% of your RI
Sugars 10.6g, 12% of your RI
Salt 0.17, 3%', 2.49, false, 1, 3);
INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Sugar-frosted cornflakes', 'A 30g serving contains:
Energy 447kJ / 105kcal, 5% of your RI
Fat 0.2g, < 1% of your RI
Saturates <0.1, < 1% of your RI
Sugars 11.5g, 13% of your RI
Salt 0.2g, 4% of your RI', 2.99, true, 2, 2);
INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Granola with dried fruit, nuts or seeds', 'A 60g serving contains:
Energy 1135kJ / 270kcal, 14% of your RI
Fat 13.3g, 19% of your RI
Saturates 2.7g, 14% of your RI
Sugars 10.8g, 12% of your RI
Salt <0.01, < 1% of your RI', 1.59, false, 2, 2);
INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Granola with chocolate', 'A 50g serving contains:
Energy 924kJ / 220kcal, 11% RI
Fat 15g, 21% RI
Saturates 6.8g, 34% RI
Sugars 24g, 27% RI
Salt 0.5g, 8% RI', 3.49, false, 3, 2);
INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Shredded whole wheat cereal', 'A 45g serving contains:
Energy 688kJ / 163kcal, 8% of your RI
Fat 1.0g, 1% of your RI
Saturates 0.2g, 1% of your RI
Sugars 0.3g, <1% of your RI
Salt 0.02g, <1% of your RI', 2.55, false, 3, 5);
INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('No added sugar or salt muesli', 'A 50g Swiss-style no added sugar or salt muesli serving contains:
Energy 758kJ / 179kcal, 9% of your RI
Fat 2.9g, 4% of your RI
Saturates 0.6g, 3% of your RI
Sugars 6.5g, 7% of your RI
Salt 0.08g, 1%', 0.99, true, 4, 5);
INSERT INTO cereal_cereal (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Porridge', 'A 40g serving of oats (not made up) contains:
Energy  645kJ / 152kcal, 7.6% of your RI
Fat 3.2g, 5% of your RI
Saturates 0.5g, 2.6% of your RI
Sugars 0.1g, 0.1% of your RI
Salt <0.01g, <1% of your RI', 0.49, false, 4, 3);

INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/brankflakes-exp1119-620x400.jpg?la=en&rev=f150885812f14595a8e6035f4389d029&hash=1F42E4214C7AA6F0351FD634B568F98F62C8CCC7', 1);
INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/cornflakes-exp1119-620x400.jpg?la=en&rev=70db674274cf47b8bb4652cb4a3971d2&hash=97523649A7AE256922E20C3AFDAF5030A4B80804', 2);
INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/muesli-with-added-sugar-620x400.jpg?la=en&rev=2f7e8e72fb44414ca2c8b7bc2bb99576&hash=7F1B226BF21A6C8E823CBD551E2FCABE016A3572', 3);
INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/frosties-exp1119-620x400.jpg?la=en&rev=39bbfe33793d408082864edbbf888254&hash=606F6953882BDC241583BC1DD03598E7BA456237', 4);
INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/granola-exp-1119-620x400.jpg?la=en&rev=f2c96baeaee24dddb163fd73b5894f39&hash=3EB52F82B4F7DDD4782E0038F3C83408D658E433', 5);
INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/choc-granola-exp-1119-620x400.jpg?la=en&rev=f9819acb93914d5883bf7ab2cffe2031&hash=D55AF1E9B0C6E13F50504F08C3E14580AEF10C18', 6);
INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/shredded-wheat-exo1119-620x400.jpg?la=en&rev=59de02a4cbc34aa7a76042a3a94116ff&hash=BADD21F512306FB3272BEC31EEA2EF8775C5CB0B', 7);
INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/muesli-exp-1119-620x400.jpg?h=400&w=620&la=en&rev=b810f4a144dc494d8ed896b3c33739e5&hash=0540FE8C8ADFE5406CFBA31C306C80C4980F92A8', 8);
INSERT INTO cereal_cerealimage (image, cereal_id) VALUES('https://www.bhf.org.uk/-/media/images/heart-matters-magazine/oatmeal-exp-1119-620x400.jpg?h=400&w=620&la=en&rev=1dae0f4e075143b69a6a38fb88ac9434&hash=904740650F343B0D45B44B20411A9518F6AD9E5D', 9);
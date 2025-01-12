
class MovieFinder:
    def __init__(self):
        self.movies_bollywood = {
            # 2023 Movies
            'Pathaan': ['Shah Rukh Khan', 'Deepika Padukone', 'John Abraham', 'Dimple Kapadia'],
            'Jawan': ['Shah Rukh Khan', 'Nayanthara', 'Vijay Sethupathi', 'Sanya Malhotra', 'Sunil Grover'],
            'Kisi Ka Bhai Kisi Ki Jaan': ['Salman Khan', 'Pooja Hegde', 'Venkatesh Daggubati', 'Raghav Juyal'],
            'Rocky Aur Rani Ki Prem Kahani': ['Ranveer Singh', 'Alia Bhatt', 'Dharmendra', 'Shabana Azmi', 'Jaya Bachchan'],
            'Tu Jhoothi Main Makkar': ['Ranbir Kapoor', 'Shraddha Kapoor', 'Dimple Kapadia'],
            'Bholaa': ['Ajay Devgn', 'Tabu', 'Amala Paul', 'Deepak Dobriyal'],
            'Dharavi Bank': ['Suneil Shetty', 'Shilpa Shetty'],
            'Samrat Prithviraj': ['Akshay Kumar', 'Manushi Chhillar', 'Sanjay Dutt', 'Sonu Sood'],
            'Laal Singh Chaddha': ['Aamir Khan', 'Kareena Kapoor', 'Naga Chaitanya', 'Mona Singh'],
            'Rashtra Kavach Om': ['Aditya Roy Kapur', 'Sanjay Dutt', 'Shivaleeka Oberoi', 'Vijay Raaz'],
            'Govinda Naam Mera': ['Vicky Kaushal', 'Kiara Advani', 'Bhumi Pednekar'],
            'Cirkus': ['Ranveer Singh', 'Pooja Hegde', 'Jacqueline Fernandez', 'Varun Sharma'],
            'Mili': ['Janvhi Kapoor', 'Manoj Pahwa', 'Sunny Kaushal'],
            'Mughal-e-Azam (Remake)': ['Kangana Ranaut', 'Kartik Aaryan', 'Pankaj Tripathi'],
            
            # 2022 Movies
            'Gangubai Kathiawadi': ['Alia Bhatt', 'Ajay Devgn', 'Shantanu Maheshwari', 'Vijay Raaz'],
            'The Kashmir Files': ['Anupam Kher', 'Darshan Kumar', 'Mithun Chakraborty', 'Pallavi Joshi'],
            'Brahmastra: Part One – Shiva': ['Ranbir Kapoor', 'Alia Bhatt', 'Amitabh Bachchan', 'Mouni Roy', 'Nagarjuna'],
            'Drishyam 2': ['Ajay Devgn', 'Tabu', 'Shriya Saran', 'Rajat Kapoor'],
            'Bhool Bhulaiyaa 2': ['Kartik Aaryan', 'Kiara Advani', 'Tabu', 'Rajpal Yadav'],
            'Jersey': ['Shahid Kapoor', 'Mrunal Thakur', 'Pankaj Kapur', 'Shalini Pandey'],
            'Sooryavanshi': ['Akshay Kumar', 'Katrina Kaif', 'Ajay Devgn', 'Ranveer Singh'],
            'Laal Singh Chaddha': ['Aamir Khan', 'Kareena Kapoor', 'Naga Chaitanya', 'Mona Singh'],
            'Atrangi Re': ['Sara Ali Khan', 'Dhanush', 'Akshay Kumar', 'Nora Fatehi'],
            'Cirkus': ['Ranveer Singh', 'Pooja Hegde', 'Jacqueline Fernandez', 'Varun Sharma'],
            'Vikram Vedha': ['Hrithik Roshan', 'Saif Ali Khan', 'Radhika Apte', 'Ravi Kishan'],
            'Kgf Chapter 2': ['Yash', 'Sanjay Dutt', 'Raveen Tondon', 'Prakash Raj'],
            'Maja Ma': ['Madhuri Dixit', 'Gajraj Rao', 'Ritwik Bhowmik', 'Srishti Shrivastava'],
            'Raksha Bandhan': ['Akshay Kumar', 'Bhumi Pednekar', 'Sadia Khateeb', 'Deepika Khanna'],
            'An Action Hero': ['Ayushmann Khurrana', 'Jaideep Ahlawat', 'Zeenat Aman', 'Radhika Apte'],

            # 2021 Movies
            'Shershaah': ['Sidharth Malhotra', 'Kiara Advani', 'Shiv Pandit', 'Javed Jaffrey'],
            'Sooryavanshi': ['Akshay Kumar', 'Katrina Kaif', 'Ajay Devgn', 'Ranveer Singh'],
            'Bell Bottom': ['Akshay Kumar', 'Vaani Kapoor', 'Huma Qureshi', 'Lara Dutta'],
            'Roohi': ['Rajkummar Rao', 'Janvhi Kapoor', 'Varun Sharma'],
            'Ludo': ['Rajkummar Rao', 'Abhishek Bachchan', 'Pankaj Tripathi', 'Aditya Roy Kapur'],
            'Atrangi Re': ['Sara Ali Khan', 'Dhanush', 'Akshay Kumar', 'Nora Fatehi'],
            'Chehre': ['Amitabh Bachchan', 'Emraan Hashmi', 'Rhea Chakraborty'],
            'Mumbai Mafia': ['John Abraham', 'Emraan Hashmi'],

            # 2020 Movies
            'Tanhaji: The Unsung Warrior': ['Ajay Devgn', 'Kajol', 'Saif Ali Khan'],
            'Angrezi Medium': ['Irrfan Khan', 'Kareena Kapoor', 'Radhika Madan'],
            'Chhapaak': ['Deepika Padukone', 'Vikrant Massey', 'Madhurjeet Sarghi'],
            'Baaghi 3': ['Tiger Shroff', 'Shraddha Kapoor', 'Riteish Deshmukh'],
            'Street Dancer 3D': ['Varun Dhawan', 'Shraddha Kapoor', 'Prabhu Deva'],
            'Shubh Mangal Zyada Saavdhan': ['Ayushmann Khurrana', 'Jitendra Kumar', 'Neena Gupta', 'Gajraj Rao'],
            'Coolie No. 1': ['Varun Dhawan', 'Sara Ali Khan', 'Paresh Rawal'],
            'Gunjan Saxena: The Kargil Girl': ['Janvhi Kapoor', 'Pankaj Tripathi', 'Angad Bedi'],

            # 2019 Movies
            'Kabir Singh': ['Shahid Kapoor', 'Kiara Advani', 'Suresh Oberoi'],
            'Bharat': ['Salman Khan', 'Katrina Kaif', 'Disha Patani'],
            'War': ['Hrithik Roshan', 'Tiger Shroff', 'Vaani Kapoor'],
            'Housefull 4': ['Akshay Kumar', 'Riteish Deshmukh', 'Bobby Deol', 'Kriti Sanon'],
            'Street Dancer 3D': ['Varun Dhawan', 'Shraddha Kapoor', 'Prabhu Deva'],
            'Good Newwz': ['Akshay Kumar', 'Kareena Kapoor', 'Diljit Dosanjh', 'Kiara Advani'],
            'Chhichhore': ['Sushant Singh Rajput', 'Shraddha Kapoor', 'Varun Sharma'],
            'De De Pyaar De': ['Ajay Devgn', 'Tabu', 'Rakul Preet Singh'],

            # 2018 Movies
            'Dhadak': ['Ishaan Khatter', 'Janhvi Kapoor', 'Ashutosh Rana'],
            'Sanju': ['Ranbir Kapoor', 'Vicky Kaushal', 'Paresh Rawal'],
            'Stree': ['Rajkummar Rao', 'Shraddha Kapoor', 'Pankaj Tripathi'],
            'Batti Gul Meter Chalu': ['Shahid Kapoor', 'Shraddha Kapoor', 'Divyendu Sharma'],
            'Sui Dhaaga': ['Varun Dhawan', 'Anushka Sharma', 'Raghubir Yadav'],
            'Baaghi 2': ['Tiger Shroff', 'Disha Patani', 'Randeep Hooda'],
            'Race 3': ['Salman Khan', 'Jacqueline Fernandez', 'Bobby Deol'],
            'Gold': ['Akshay Kumar', 'Mouni Roy', 'Kunal Kapoor'],

            # 2017 Movies
            'Dangal': ['Aamir Khan', 'Fatima Sana Shaikh', 'Sanya Malhotra'],
            'Raees': ['Shah Rukh Khan', 'Mahira Khan', 'Nawazuddin Siddiqui'],
            'Tubelight': ['Salman Khan', 'Matin Rey Tangu', 'Zhu Zhu'],
            'Judwaa 2': ['Varun Dhawan', 'Jacqueline Fernandez', 'Taapsee Pannu'],
            'Baahubali 2: The Conclusion': ['Prabhas', 'Anushka Shetty', 'Rana Daggubati'],
            'Goliyon Ki Raasleela Ram-Leela': ['Ranveer Singh', 'Deepika Padukone', 'Priyanka Chopra'],

            # 2016 Movies
            'Ae Dil Hai Mushkil': ['Ranbir Kapoor', 'Anushka Sharma', 'Aishwarya Rai Bachchan'],
            'Dangal': ['Aamir Khan', 'Fatima Sana Shaikh', 'Sanya Malhotra'],
            'Sultan': ['Salman Khan', 'Anushka Sharma', 'Randeep Hooda'],
            'Housefull 3': ['Akshay Kumar', 'Abhishek Bachchan', 'Riteish Deshmuk'],
            'Kapoor & Sons': ['Sidharth Malhotra', 'Fawad Khan', 'Alia Bhatt'],

            # 2015 Movies
            'Bajirao Mastani': ['Ranveer Singh', 'Deepika Padukone', 'Priyanka Chopra'],
            'Dilwale': ['Shah Rukh Khan', 'Kajol', 'Varun Dhawan'],
            'Baahubali: The Beginning': ['Prabhas', 'Rana Daggubati', 'Anushka Shetty'],
            'Piku': ['Amitabh Bachchan', 'Deepika Padukone', 'Irrfan Khan'],
            'Tamasha': ['Ranbir Kapoor', 'Deepika Padukone', 'Piyush Mishra'],
        }

        self.web_series_bollywood = {
            # 2018
            'Sacred Games': ['Saif Ali Khan', 'Nawazuddin Siddiqui', 'Radhika Apte', 'Pankaj Tripathi', 'Surveen Chawla'],
            'Mirzapur': ['Pankaj Tripathi', 'Ali Fazal', 'Shweta Tripathi Sharma', 'Divyendu Sharma', 'Vikrant Massey', 'Rasika Dugal'],
            'Breathe': ['R. Madhavan', 'Amit Sadh', 'Sadhvani Singh', 'Sapna Pabbi'],
            'The Great Indian Dysfunctional Family': ['Barun Sobti', 'Shivani Tanksale', 'Rohit Chandel', 'Elli Avram'],
            
            # 2019
            'Made in Heaven': ['Sobhita Dhulipala', 'Arjun Mathur', 'Shashank Arora', 'Kalki Koechlin', 'Jim Sarbh'],
            'The Family Man': ['Manoj Bajpayee', 'Sharib Hashmi', 'Priyamani', 'Shreya Dhanwanthary', 'Sharib Hashmi'],
            'Mirzapur Season 2': ['Pankaj Tripathi', 'Ali Fazal', 'Divyendu Sharma', 'Vikrant Massey', 'Shweta Tripathi Sharma', 'Rasika Dugal'],
            'Delhi Crime': ['Shefali Shah', 'Rajesh Tailang', 'Rasika Dugal', 'Adil Hussain', 'Sandeep Shikhar'],
            'Bard of Blood': ['Emraan Hashmi', 'Sobhita Dhulipala', 'Vineet Kumar Singh', 'Jaideep Ahlawat'],
            'Panchayat': ['Jitendra Kumar', 'Raghubir Yadav', 'Neena Gupta', 'Fahad Mustafa', 'Chandan Roy'],
            
            # 2020
            'Special Ops': ['Kay Kay Menon', 'Vishal Jethwa', 'Karan Tacker', 'Saiyami Kher', 'Vinay Pathak'],
            'Scam 1992': ['Pratik Gandhi', 'Shreya Dhanwanthary', 'Hemant Kher', 'Nikhil Dwivedi', 'Raghubir Yadav'],
            'Aarya': ['Sushmita Sen', 'Chandrachur Singh', 'Ankur Bhatia', 'Nikitin Dheer'],
            'Panchayat': ['Jitendra Kumar', 'Raghubir Yadav', 'Neena Gupta', 'Fahad Mustafa', 'Chandan Roy'],
            'The Last Hour': ['Shivani Raghuvanshi', 'Shahnawaz Pradhan', 'Raghubir Yadav', 'Karma Takapa'],
            'Breathe: Into the Shadows': ['Abhishek Bachchan', 'Amit Sadh', 'Nithya Menen', 'Saiyami Kher'],
            'Criminal Justice': ['Vikrant Massey', 'Pankaj Tripathi', 'Anupriya Goenka', 'Mita Vashisht'],
            
            # 2021
            'The Family Man Season 2': ['Manoj Bajpayee', 'Sharib Hashmi', 'Priyamani', 'Shreya Dhanwanthary', 'Sharib Hashmi'],
            'The Empire': ['Kunal Kapoor', 'Shabana Azmi', 'Drashti Dhami', 'Dino Morea'],
            'Mumbai Mafia: Police vs The Underworld': ['Documentary'],
            'Tabbar': ['Pavan Malhotra', 'Sujata Kumar', 'Gagan Arora', 'Raghubir Yadav'],
            'Rocket Boys': ['Jim Sarbh', 'Ishwak Singh', 'Suhail Nayyar', 'Rajit Kapur'],
            'Tandav': ['Saif Ali Khan', 'Dimple Kapadia', 'Kareena Kapoor Khan', 'Sunil Grover'],
            'Aarya Season 2': ['Sushmita Sen', 'Chandrachur Singh', 'Ankur Bhatia', 'Nikitin Dheer', 'Vikas Kumar'],
            
            # 2022
            'The Kashmir Files (Web Version)': ['Anupam Kher', 'Mithun Chakraborty', 'Darshan Kumar', 'Pallavi Joshi'],
            'Mismatched Season 2': ['Prajakta Koli', 'Rohit Saraf', 'Rannvijay Singha', 'Vidya Malvade'],
            'Scooter': ['Rajkummar Rao', 'Sanya Malhotra', 'Vikram Singh', 'Shubham Jha'],
            'Delhi Crime Season 2': ['Shefali Shah', 'Rajesh Tailang', 'Rasika Dugal', 'Adil Hussain', 'Sandeep Shikhar'],
            'Escaype Live': ['Javed Jaffrey', 'Siddharth', 'Shweta Tripathi Sharma', 'Rohit Saraf'],
            'Class of 2009': ['Pratik Babbar', 'Nikita Dutta', 'Sanjay Kapoor', 'Anupriya Goenka', 'Madhurima Tuli'],
            'Taj: Divided by Blood': ['Naseeruddin Shah', 'Rahul Bose', 'Dharmendra', 'Aditi Rao Hydari'],
            
            # 2023
            'Farzi': ['Shahid Kapoor', 'Vijay Sethupathi', 'Raashii Khanna', 'Kay Kay Menon', 'Zeeshan Ayyub'],
            'The Night Manager (Indian Remake)': ['Aditya Roy Kapur', 'Sobhita Dhulipala', 'Anil Kapoor', 'Tillotama Shome'],
            'Taj: Divided by Blood': ['Naseeruddin Shah', 'Rahul Bose', 'Dharmendra', 'Aditi Rao Hydari'],
            'Guns & Gulaabs': ['Rajkummar Rao', 'Dulquer Salmaan', 'Gulshan Devaiah', 'Adarsh Gourav'],
            'Scam 2003: The Telgi Story': ['Shantanu Maheshwari', 'Mohan Agashe', 'Gagan Dev Riar', 'Raghubir Yadav'],
            'The Family Man Season 3': ['Manoj Bajpayee', 'Sharib Hashmi', 'Priyamani', 'Shreya Dhanwanthary', 'Sharib Hashmi'],
            'Mumbai Mafia: Police vs The Underworld': ['Documentary'],
            
            # 2024
            'The Night Manager': ['Aditya Roy Kapur', 'Sobhita Dhulipala', 'Anil Kapoor', 'Tillotama Shome', 'Rajat Kapoor'],
            'Farzi Season 2': ['Shahid Kapoor', 'Vijay Sethupathi', 'Raashii Khanna', 'Kay Kay Menon', 'Zeeshan Ayyub'],
            'Mirzapur Season 4': ['Pankaj Tripathi', 'Ali Fazal', 'Divyendu Sharma', 'Vikrant Massey', 'Shweta Tripathi Sharma', 'Rasika Dugal'],
            'The Family Man Season 3': ['Manoj Bajpayee', 'Sharib Hashmi', 'Priyamani', 'Shreya Dhanwanthary', 'Sharib Hashmi'],
            'Panchayat Season 3': ['Jitendra Kumar', 'Raghubir Yadav', 'Neena Gupta', 'Fahad Mustafa', 'Chandan Roy'],
            'Scam 2003: The Telgi Story': ['Shantanu Maheshwari', 'Mohan Agashe', 'Gagan Dev Riar', 'Raghubir Yadav'],
            'Taaza Khabar': ['Bhuvan Bam', 'Shivani Raghuvanshi', 'Deven Bhojani', 'Vijay Raaz', 'Zakir Hussain'],
            'The Great Indian Murder Season 2': ['Richa Chadha', 'Ashutosh Rana', 'Jatin Goswami', 'Vineet Kumar Singh', 'Raghubir Yadav'],
            'Made in Heaven Season 2': ['Sobhita Dhulipala', 'Arjun Mathur', 'Shashank Arora', 'Kalki Koechlin', 'Jim Sarbh'],
            'Delhi Crime Season 3': ['Shefali Shah', 'Rajesh Tailang', 'Rasika Dugal', 'Adil Hussain', 'Sandeep Shikhar'],
            'The Trial (Indian Remake of The Good Wife)': ['Kareena Kapoor Khan', 'Kubbra Sait', 'Shahnawaz Pradhan', 'Mackenzie Davis', 'Suchitra Pillai'],
            'Class of 2009': ['Pratik Babbar', 'Nikita Dutta', 'Sanjay Kapoor', 'Anupriya Goenka', 'Madhurima Tuli']
        }

        self.movies_Hollywood = {
            # 2018
            'Avengers: Infinity War': ['Robert Downey Jr.', 'Chris Hemsworth', 'Mark Ruffalo', 'Scarlett Johansson', 'Chris Evans'],
            'Black Panther': ['Chadwick Boseman', 'Michael B. Jordan', 'Lupita Nyong\'o', 'Danai Gurira', 'Martin Freeman'],
            'Bohemian Rhapsody': ['Rami Malek', 'Lucy Boynton', 'Ben Hardy', 'Joseph Mazzello', 'Gwilym Lee'],
            'A Star Is Born': ['Lady Gaga', 'Bradley Cooper', 'Sam Elliott', 'Dave Chappelle', 'Andrew Dice Clay'],
            'Mission: Impossible – Fallout': ['Tom Cruise', 'Henry Cavill', 'Simon Pegg', 'Rebecca Ferguson', 'Ving Rhames'],
            'Incredibles 2': ['Craig T. Nelson', 'Holly Hunter', 'Sarah Vowell', 'Samuel L. Jackson', 'Brad Bird'],
            'Venom': ['Tom Hardy', 'Michelle Williams', 'Riz Ahmed', 'Woody Harrelson', 'Jenny Slate'],
            'Spider-Man: Into the Spider-Verse': ['Shameik Moore', 'Jake Johnson', 'Hailee Steinfeld', 'Mahershala Ali', 'Liev Schreiber'],
            'Deadpool 2': ['Ryan Reynolds', 'Josh Brolin', 'Zazie Beetz', 'T.J. Miller', 'Morena Baccarin'],
            'Jurassic World: Fallen Kingdom': ['Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall', 'Toby Jones', 'Justice Smith'],

            # 2019
            'Avengers: Endgame': ['Robert Downey Jr.', 'Chris Hemsworth', 'Scarlett Johansson', 'Mark Ruffalo', 'Chris Evans'],
            'Joker': ['Joaquin Phoenix', 'Robert De Niro', 'Zazie Beetz', 'Frances Conroy', 'Brett Cullen'],
            'Once Upon a Time in Hollywood': ['Leonardo DiCaprio', 'Brad Pitt', 'Margot Robbie', 'Al Pacino', 'Kurt Russell'],
            'The Lion King': ['Donald Glover', 'Beyoncé', 'Seth Rogen', 'Chiwetel Ejiofor', 'Billy Eichner'],
            'Toy Story 4': ['Tom Hanks', 'Tim Allen', 'Annie Potts', 'Tony Hale', 'Keegan-Michael Key'],
            'Parasite': ['Song Kang-ho', 'Lee Sun-kyun', 'Cho Yeo-jeong', 'Choi Woo-shik', 'Park So-dam'],
            'It Chapter Two': ['James McAvoy', 'Jessica Chastain', 'Bill Hader', 'Isaiah Mustafa', 'Jay Ryan'],
            'John Wick: Chapter 3 – Parabellum': ['Keanu Reeves', 'Halle Berry', 'Ian McShane', 'Laurence Fishburne', 'Ruby Rose'],
            'Frozen II': ['Idina Menzel', 'Kristen Bell', 'Josh Gad', 'Evan Rachel Wood', 'Sterling K. Brown'],
            'Shazam!': ['Zachary Levi', 'Asher Angel', 'Jack Dylan Grazer', 'Mark Strong', 'Marta Milans'],

            # 2020
            'Tenet': ['John David Washington', 'Robert Pattinson', 'Elizabeth Debicki', 'Dimple Kapadia', 'Kenneth Branagh'],
            'Birds of Prey': ['Margot Robbie', 'Rosie Perez', 'Mary Elizabeth Winstead', 'Jurnee Smollett', 'Ewan McGregor'],
            'Wonder Woman 1984': ['Gal Gadot', 'Chris Pine', 'Kristen Wiig', 'Pedro Pascal', 'Robin Wright'],
            'Soul': ['Jamie Foxx', 'Tina Fey', 'Phylicia Rashad', 'Angela Bassett', 'Questlove'],
            'Mulan': ['Liu Yifei', 'Donnie Yen', 'Jason Scott Lee', 'Yoson An', 'Gong Li'],
            'The Invisible Man': ['Elisabeth Moss', 'Oliver Jackson-Cohen', 'Harriet Dyer', 'Aldis Hodge', 'Michael Dorman'],
            'The Trial of the Chicago 7': ['Eddie Redmayne', 'Sacha Baron Cohen', 'Mark Rylance', 'Joseph Gordon-Levitt', 'Jeremy Strong'],
            'The Way Back': ['Ben Affleck', 'Al Madrigal', 'Janina Gavankar', 'Glynn Turman', 'Michaela Watkins'],
            'Wonder Woman 1984': ['Gal Gadot', 'Chris Pine', 'Kristen Wiig', 'Pedro Pascal', 'Robin Wright'],
            'The Gentlemen': ['Matthew McConaughey', 'Charlie Hunnam', 'Michelle Dockery', 'Henry Golding', 'Hugh Grant'],

            # 2021
            'Spider-Man: No Way Home': ['Tom Holland', 'Zendaya', 'Benedict Cumberbatch', 'Jacob Batalon', 'Marisa Tomei'],
            'Dune': ['Timothée Chalamet', 'Zendaya', 'Oscar Isaac', 'Rebecca Ferguson', 'Jason Momoa'],
            'No Time to Die': ['Daniel Craig', 'Rami Malek', 'Ana de Armas', 'Ralph Fiennes', 'Naomie Harris'],
            'A Quiet Place Part II': ['Emily Blunt', 'Cillian Murphy', 'Millicent Simmonds', 'Noah Jupe', 'John Krasinski'],
            'Black Widow': ['Scarlett Johansson', 'Florence Pugh', 'David Harbour', 'Rachel Weisz', 'O-T Fagbenle'],
            'The Suicide Squad': ['Margot Robbie', 'Idris Elba', 'John Cena', 'Sylvester Stallone', 'Viola Davis'],
            'Eternals': ['Gemma Chan', 'Richard Madden', 'Angelina Jolie', 'Salma Hayek', 'Kit Harington'],
            'Jungle Cruise': ['Dwayne Johnson', 'Emily Blunt', 'Jack Whitehall', 'Paul Giamatti', 'Édgar Ramírez'],
            'Matrix Resurrections': ['Keanu Reeves', 'Carrie-Anne Moss', 'Yahya Abdul-Mateen II', 'Jessica Henwick', 'Jonathan Groff'],
            'The French Dispatch': ['Timothée Chalamet', 'Frances McDormand', 'Bill Murray', 'Benicio del Toro', 'Tilda Swinton'],

            # 2022
            'Avatar: The Way of Water': ['Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver', 'Kate Winslet', 'Stephen Lang'],
            'Doctor Strange in the Multiverse of Madness': ['Benedict Cumberbatch', 'Elizabeth Olsen', 'Benedict Wong', 'Xochitl Gomez', 'Chiwetel Ejiofor'],
            'Thor: Love and Thunder': ['Chris Hemsworth', 'Natalie Portman', 'Christian Bale', 'Tessa Thompson', 'Taika Waititi'],
            'Jurassic World: Dominion': ['Chris Pratt', 'Bryce Dallas Howard', 'Laura Dern', 'Jeff Goldblum', 'Sam Neill'],
            'The Batman': ['Robert Pattinson', 'Zoë Kravitz', 'Paul Dano', 'Colin Farrell', 'Jeffrey Wright'],
            'Black Panther: Wakanda Forever': ['Letitia Wright', 'Angela Bassett', 'Lupita Nyong\'o', 'Danai Gurira', 'Martin Freeman'],
            'Avatar 2': ['Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver', 'Stephen Lang', 'Kate Winslet'],
            'Scream': ['Neve Campbell', 'Courteney Cox', 'David Arquette', 'Jenna Ortega', 'Jack Quaid'],
            'Nope': ['Daniel Kaluuya', 'Keke Palmer', 'Steven Yeun', 'Brandon Perea', 'Michael Wincott'],
            'Everything Everywhere All at Once': ['Michelle Yeoh', 'Stephanie Hsu', 'Ke Huy Quan', 'Jamie Lee Curtis', 'James Hong'],

            # 2023
            'Guardians of the Galaxy Vol. 3': ['Chris Pratt', 'Zoe Saldana', 'Dave Bautista', 'Karen Gillan', 'Vin Diesel'],
            'Mission: Impossible – Dead Reckoning Part One': ['Tom Cruise', 'Hayley Atwell', 'Simon Pegg', 'Rebecca Ferguson', 'Ving Rhames'],
            'Barbie': ['Margot Robbie', 'Ryan Gosling', 'Simu Liu', 'Will Ferrell', 'Issa Rae'],
            'Oppenheimer': ['Cillian Murphy', 'Emily Blunt', 'Robert Downey Jr.', 'Matt Damon', 'Florence Pugh'],
            'The Flash': ['Ezra Miller', 'Michael Keaton', 'Ben Affleck', 'Sasha Calle', 'Michael Shannon'],
            'Indiana Jones and the Dial of Destiny': ['Harrison Ford', 'Phoebe Waller-Bridge', 'Mads Mikkelsen', 'Antonio Banderas', 'John Rhys-Davies'],
            'John Wick: Chapter 4': ['Keanu Reeves', 'Donnie Yen', 'Bill Skarsgård', 'Hiroyuki Sanada', 'Lance Reddick'],
            'Creed III': ['Michael B. Jordan', 'Jonathan Majors', 'Tessa Thompson', 'Wood Harris', 'Phylicia Rashad'],
            'The Marvels': ['Brie Larson', 'Iman Vellani', 'Teyonah Parris', 'Zawe Ashton', 'Park Seo-jun'],
            'Transformers: Rise of the Beasts': ['Anthony Ramos', 'Dominique Fishback', 'Ron Perlman', 'Peter Cullen', 'Michelle Yeoh'],

            # 2024
            'Deadpool 3': ['Ryan Reynolds', 'Hugh Jackman', 'Blake Lively', 'Morena Baccarin', 'Vanessa Hudgens'],
            'Mission: Impossible – Dead Reckoning Part Two': ['Tom Cruise', 'Hayley Atwell', 'Simon Pegg', 'Rebecca Ferguson', 'Ving Rhames'],
            'Dune: Part Two': ['Timothée Chalamet', 'Zendaya', 'Oscar Isaac', 'Rebecca Ferguson', 'Jason Momoa'],
            'Avengers: The Kang Dynasty': ['Robert Downey Jr.', 'Chris Hemsworth', 'Scarlett Johansson', 'Benedict Cumberbatch', 'Tom Holland'],
            'The Hunger Games: The Ballad of Songbirds and Snakes': ['Rachel Zegler', 'Tom Blyth', 'Hunter Schafer', 'Peter Dinklage', 'Jason Schwartzman'],
            'Fantastic Four (Reboot)': ['Unknown Cast', 'Unknown Cast', 'Unknown Cast', 'Unknown Cast'],
            'Captain America: New World Order': ['Anthony Mackie', 'Sebastian Stan', 'Harrison Ford', 'Shira Haas', 'Danny Ramirez'],
            'The Flash 2': ['Ezra Miller', 'Michael Keaton', 'Ben Affleck', 'Sasha Calle', 'Michael Shannon']
        }

        self.web_series_hollywood = {
            # 2018
            'The Haunting of Hill House': ['Michiel Huisman', 'Elisabeth Reaser', 'Oliver Jackson-Cohen', 'Victoria Pedretti', 'Carla Gugino'],
            'Narcos: Mexico': ['Diego Luna', 'Michael Peňa', 'Scoot McNairy', 'José María Yazpik', 'Fernanda Urrejola'],
            'Bodyguard': ['Richard Madden', 'Keeley Hawes', 'Ginny Holder', 'Stephanie Hyam', 'Diana Kent'],
            'The Punisher': ['Jon Bernthal', 'Ebon Moss-Bachrach', 'Deborah Ann Woll', 'Ben Barnes', 'Paul Schulze'],
            'You': ['Penn Badgley', 'Elizabeth Lail', 'Shay Mitchell', 'Zach Cherry', 'John Stamos'],
            'Altered Carbon': ['Joel Kinnaman', 'Martha Higareda', 'James Purefoy', 'Ato Essandoh', 'Chris Conner'],
            
            # 2019
            'The Witcher': ['Henry Cavill', 'Anya Chalotra', 'Freya Allan', 'Joey Batey', 'MyAnna Buring'],
            'Chernobyl': ['Jared Harris', 'Stellan Skarsgård', 'Emily Watson', 'Paul Ritter', 'Adam Nagaitis'],
            'The Mandalorian': ['Pedro Pascal', 'Gina Carano', 'Carl Weathers', 'Werner Herzog', 'Giancarlo Esposito'],
            'Watchmen': ['Regina King', 'Don Johnson', 'Tim Blake Nelson', 'Louis Gossett Jr.', 'Jeremy Irons'],
            'The Umbrella Academy': ['Elliot Page', 'Tom Hopper', 'David Castañeda', 'Robert Sheehan', 'Aidan Gallagher'],
            'Stranger Things 3': ['Winona Ryder', 'David Harbour', 'Millie Bobby Brown', 'Finn Wolfhard', 'Gaten Matarazzo'],
            'The Boys': ['Karl Urban', 'Jack Quaid', 'Erin Moriarty', 'Antony Starr', 'Chace Crawford'],
            'Fleabag': ['Phoebe Waller-Bridge', 'Sian Clifford', 'Olivia Colman', 'Bill Paterson', 'Andrew Scott'],
            'When They See Us': ['Aunjanue Ellis', 'Michael K. Williams', 'John Leguizamo', 'Caleel Harris', 'Jharrel Jerome'],
            
            # 2020
            'The Queen\'s Gambit': ['Anya Taylor-Joy', 'Bill Camp', 'Marielle Heller', 'Thomas Brodie-Sangster', 'Moses Ingram'],
            'The Mandalorian Season 2': ['Pedro Pascal', 'Gina Carano', 'Carl Weathers', 'Giancarlo Esposito', 'Temuera Morrison'],
            'The Boys Season 2': ['Karl Urban', 'Jack Quaid', 'Erin Moriarty', 'Antony Starr', 'Chace Crawford'],
            'Reacher': ['Alan Ritchson', 'Malcolm Goodwin', 'Willa Fitzgerald', 'Chris Webster', 'Maria Sten'],
            'Fargo (Season 4)': ['Chris Rock', 'Jason Schwartzman', 'Ben Whishaw', 'Jesse Buckley', 'Salvatore Esposito'],
            'The Outsider': ['Ben Mendelsohn', 'Cynthia Erivo', 'Bill Camp', 'Jason Bateman', 'Julianne Nicholson'],
            'Love Craft Country': ['Jonathan Majors', 'Jurnee Smollett', 'Courtney B. Vance', 'Michael K. Williams', 'Aunjanue Ellis'],
            'Ted Lasso': ['Jason Sudeikis', 'Hannah Waddingham', 'Brett Goldstein', 'Brendan Hunt', 'Jeremy Swift'],
            'The Trial of Chicago 7': ['Eddie Redmayne', 'Sacha Baron Cohen', 'Mark Rylance', 'Joseph Gordon-Levitt', 'Jeremy Strong'],
            
            # 2021
            'Squid Game': ['Lee Jung-jae', 'Park Hae-soo', 'Wi Ha-joon', 'Jung Ho-yeon', 'O Yeong-su'],
            'Loki': ['Tom Hiddleston', 'Owen Wilson', 'Sophia Di Martino', 'Gugu Mbatha-Raw', 'Wunmi Mosaku'],
            'Money Heist (Season 5)': ['Álvaro Morte', 'Úrsula Corberó', 'Itziar Ituño', 'Pedro Alonso', 'Miguel Herrán'],
            'Reacher (Season 1)': ['Alan Ritchson', 'Malcolm Goodwin', 'Willa Fitzgerald', 'Chris Webster', 'Maria Sten'],
            'The Witcher Season 2': ['Henry Cavill', 'Anya Chalotra', 'Freya Allan', 'Joey Batey', 'MyAnna Buring'],
            'Stranger Things 4': ['Winona Ryder', 'David Harbour', 'Millie Bobby Brown', 'Finn Wolfhard', 'Gaten Matarazzo'],
            'Hawkeye': ['Jeremy Renner', 'Hailee Steinfeld', 'Florence Pugh', 'Vera Farmiga', 'Tony Dalton'],
            'The Falcon and the Winter Soldier': ['Anthony Mackie', 'Sebastian Stan', 'Wyatt Russell', 'Daniel Brühl', 'Emily VanCamp'],
            'Mare of Easttown': ['Kate Winslet', 'Evan Peters', 'Julianne Nicholson', 'Jean Smart', 'Angourie Rice'],
            'WandaVision': ['Elizabeth Olsen', 'Paul Bettany', 'Kathryn Hahn', 'Teyonah Parris', 'Randall Park'],
            
            # 2022
            'Stranger Things 4': ['Winona Ryder', 'David Harbour', 'Millie Bobby Brown', 'Finn Wolfhard', 'Gaten Matarazzo'],
            'The Bear': ['Jeremy Allen White', 'Ebon Moss-Bachrach', 'Ayo Edebiri', 'Liza Colón-Zayas', 'Abby Elliott'],
            'House of the Dragon': ['Paddy Considine', 'Emma D’Arcy', 'Matt Smith', 'Olivia Cooke', 'Stefanie Martini'],
            'Reacher (Season 2)': ['Alan Ritchson', 'Malcolm Goodwin', 'Willa Fitzgerald', 'Chris Webster', 'Maria Sten'],
            'Andor': ['Diego Luna', 'Stellan Skarsgård', 'Adria Arjona', 'Fiona Shaw', 'Kyle Soller'],
            'Wednesday': ['Jenna Ortega', 'Catherine Zeta-Jones', 'Luis Guzmán', 'Riki Lindhome', 'Gwendoline Christie'],
            'The Sandman': ['Tom Sturridge', 'Gwendoline Christie', 'Vivienne Acheampong', 'Boyd Holbrook', 'Charles Dance'],
            'The White Lotus (Season 2)': ['Jennifer Coolidge', 'Aubrey Plaza', 'Theo James', 'Meghann Fahy', 'Adam DiMarco'],
            'Better Call Saul (Final Season)': ['Bob Odenkirk', 'Rhea Seehorn', 'Jonathan Banks', 'Giancarlo Esposito', 'Patrick Fabian'],
            'The Boys: Diabolical': ['Karl Urban', 'Jack Quaid', 'Erin Moriarty', 'Antony Starr', 'Chace Crawford'],
            
            # 2023
            'The Last of Us': ['Pedro Pascal', 'Bella Ramsey', 'Nico Parker', 'Murray Bartlett', 'Anna Torv'],
            'Reacher (Season 2)': ['Alan Ritchson', 'Malcolm Goodwin', 'Willa Fitzgerald', 'Chris Webster', 'Maria Sten'],
            'The Bear Season 2': ['Jeremy Allen White', 'Ebon Moss-Bachrach', 'Ayo Edebiri', 'Liza Colón-Zayas', 'Abby Elliott'],
            'Secret Invasion': ['Samuel L. Jackson', 'Ben Mendelsohn', 'Olivia Colman', 'Don Cheadle', 'Cobie Smulders'],
            'The Mandalorian Season 3': ['Pedro Pascal', 'Gina Carano', 'Carl Weathers', 'Giancarlo Esposito', 'Temuera Morrison'],
            'The Sandman Season 2': ['Tom Sturridge', 'Gwendoline Christie', 'Vivienne Acheampong', 'Boyd Holbrook', 'Charles Dance'],
            'The Boys Season 4': ['Karl Urban', 'Jack Quaid', 'Erin Moriarty', 'Antony Starr', 'Chace Crawford'],
            'Loki Season 2': ['Tom Hiddleston', 'Owen Wilson', 'Sophia Di Martino', 'Gugu Mbatha-Raw', 'Wunmi Mosaku'],
            'Jack Ryan (Season 4)': ['John Krasinski', 'Wendell Pierce', 'Abbie Cornish', 'Michael Kelly', 'Ali Suliman'],
            'The Fall of the House of Usher': ['Mark Hamill', 'Bruce Greenwood', 'Carla Gugino', 'Mary McDonnell', 'Henry Thomas'],
            
            # 2024
            'Reacher Season 3': ['Alan Ritchson', 'Malcolm Goodwin', 'Willa Fitzgerald', 'Chris Webster', 'Maria Sten'],
            'The Day of the Jackal': ['Unnamed Cast', 'Unnamed Cast', 'Unnamed Cast', 'Unnamed Cast', 'Unnamed Cast'],
            'Ahsoka': ['Rosario Dawson', 'Natasha Liu Bordizzo', 'Mary Elizabeth Winstead', 'Diana Lee Inosanto', 'David Tennant'],
            'The Mandalorian Season 4': ['Pedro Pascal', 'Gina Carano', 'Carl Weathers', 'Giancarlo Esposito', 'Temuera Morrison'],
            'Blade Runner 2099': ['Unnamed Cast', 'Unnamed Cast', 'Unnamed Cast', 'Unnamed Cast', 'Unnamed Cast'],
        }

        self.bhojpuri_movies = {
            # 2018
            'Satyam Shivam Sundaram': ['Khesari Lal Yadav', 'Priyanka Pandit', 'Rani Chatterjee', 'Amit Shukla'],
            'Bairagi': ['Khesari Lal Yadav', 'Kajal Raghwani', 'Ravi Kishan', 'Subhi Sharma'],
            'Nirahua Rickshawala 2': ['Dinesh Lal Yadav (Nirahua)', 'Amrapali Dubey', 'Sushil Singh', 'Anup Arora'],
            'Shubh Aarambh': ['Khesari Lal Yadav', 'Kajol Raghwani', 'Gaurav Jha', 'Sanjay Pandey'],
            'Sangharsh': ['Khesari Lal Yadav', 'Nirahua', 'Rani Chatterjee', 'Priyanka Pandit'],
            
            # 2019
            'Maine Dil Tujhko Diya': ['Khesari Lal Yadav', 'Priyanka Pandit', 'Anjana Singh', 'Amit Shukla'],
            'Dhadkan': ['Pawan Singh', 'Akshara Singh', 'Anjana Singh', 'Rani Chatterjee'],
            'Rakhwala': ['Pawan Singh', 'Kajal Raghwani', 'Nirahua', 'Rani Chatterjee'],
            'Gulabo Sitabo': ['Amitabh Bachchan', 'Ayushmann Khurrana', 'Farrukh Jaffar', 'Sujat Wagh'],
            'Raja Babu': ['Dinesh Lal Yadav (Nirahua)', 'Amrapali Dubey', 'Manoj Tiwari', 'Kajal Raghwani'],
            'Baazigar': ['Khesari Lal Yadav', 'Nidhi Jha', 'Priti Biswas', 'Yashika Verma'],
            
            # 2020
            'Shubh Aarambh': ['Khesari Lal Yadav', 'Kajal Raghwani', 'Gaurav Jha', 'Sanjay Pandey'],
            'Mera Vachan': ['Dinesh Lal Yadav (Nirahua)', 'Akshara Singh', 'Manoj Tiwari', 'Priyanka Pandit'],
            'Dulhan Chahi Pakistan Se': ['Pawan Singh', 'Kajal Raghwani', 'Anjana Singh', 'Khesari Lal Yadav'],
            'Didi Ke Pallu': ['Khesari Lal Yadav', 'Amrapali Dubey', 'Ravi Kishan', 'Kajal Raghwani'],
            'Babu Babu': ['Dinesh Lal Yadav (Nirahua)', 'Rani Chatterjee', 'Nidhi Jha', 'Kajal Raghwani'],
            
            # 2021
            'Gharwahi Ke Rakhwala': ['Pawan Singh', 'Akshara Singh', 'Amit Shukla', 'Anjana Singh'],
            'Pyaar Kiya To Darna Kya': ['Dinesh Lal Yadav (Nirahua)', 'Amrapali Dubey', 'Nidhi Jha', 'Rani Chatterjee'],
            'Dil Hai Ke Manta Nahin': ['Khesari Lal Yadav', 'Rani Chatterjee', 'Akshara Singh', 'Priyanka Pandit'],
            'Nirahua Hindustani 4': ['Dinesh Lal Yadav (Nirahua)', 'Amrapali Dubey', 'Shubhi Sharma', 'Manoj Tiwari'],
            'Mehndi Laga Ke Rakhna 3': ['Khesari Lal Yadav', 'Kajol Raghwani', 'Priyanka Pandit', 'Ravi Kishan'],
            
            # 2022
            'Khiladi': ['Pawan Singh', 'Kajal Raghwani', 'Anjana Singh', 'Ravi Kishan'],
            'Khesari Ke Dilwale': ['Khesari Lal Yadav', 'Amrapali Dubey', 'Ravi Kishan', 'Nidhi Jha'],
            'Dilwale': ['Dinesh Lal Yadav (Nirahua)', 'Amrapali Dubey', 'Akshara Singh', 'Ravi Kishan'],
            'Bhaiya Ke Sali': ['Khesari Lal Yadav', 'Priyanka Pandit', 'Rani Chatterjee', 'Kajal Raghwani'],
            'Pyar Ke Liye Kuch Bhi Karna': ['Pawan Singh', 'Kajal Raghwani', 'Anjana Singh', 'Manoj Tiwari'],
            
            # 2023
            'Patna Se Pakistan': ['Khesari Lal Yadav', 'Shubhi Sharma', 'Amrapali Dubey', 'Nidhi Jha'],
            'Mangal Pandey': ['Dinesh Lal Yadav (Nirahua)', 'Amrapali Dubey', 'Ravi Kishan', 'Shubhi Sharma'],
            'Jai Hind': ['Pawan Singh', 'Kajal Raghwani', 'Anjana Singh', 'Manoj Tiwari'],
            'Meri Jaan': ['Khesari Lal Yadav', 'Rani Chatterjee', 'Priyanka Pandit', 'Amit Shukla'],
            'Ziddi': ['Pawan Singh', 'Kajal Raghwani', 'Akshara Singh', 'Ravi Kishan'],
            
            # 2024
            'Duniya Ke Sabse Bada Rakhwala': ['Khesari Lal Yadav', 'Rani Chatterjee', 'Ravi Kishan', 'Anjana Singh'],
            'Dil Ke Duniya': ['Pawan Singh', 'Kajal Raghwani', 'Amrapali Dubey', 'Anjana Singh'],
            'Maa Ka Doodh': ['Khesari Lal Yadav', 'Nidhi Jha', 'Shubhi Sharma', 'Priyanka Pandit'],
            'Rakhwala 2': ['Dinesh Lal Yadav (Nirahua)', 'Amrapali Dubey', 'Ravi Kishan', 'Kajal Raghwani'],
            'Dhol Bhari': ['Pawan Singh', 'Rani Chatterjee', 'Anjana Singh', 'Kajal Raghwani'],
        }
    def find_movies_with_actors(self, actor_list):
        result = []
        
        # Check in Bollywood movies
        for movie, cast in self.movies_bollywood.items():
            if all(actor in cast for actor in actor_list):
                result.append(movie)

        # Check in Bollywood web series
        for movie, cast in self.web_series_bollywood.items():
            if all(actor in cast for actor in actor_list):
                result.append(movie)

        # Check in Hollywood movies
        for movie, cast in self.movies_Hollywood.items():
            if all(actor in cast for actor in actor_list):
                result.append(movie)

        # Check in Hollywood web series
        for movie, cast in self.web_series_hollywood.items():
            if all(actor in cast for actor in actor_list):
                result.append(movie)

        # Check in Bhojpuri movies
        for movie, cast in self.bhojpuri_movies.items():
            if all(actor in cast for actor in actor_list):
                result.append(movie)
        
        return result


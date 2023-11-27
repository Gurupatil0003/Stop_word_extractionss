Artificial Intelligence
🎓 Course Information
Subject Code : 203105322
Faculty: Mr Smaranjit Ghose (Assistant Professor)
Semester: 5
Year: 2023
Divisions (under direct tutelage): 5B5, 5B6, 5B7, 5B8, 5B17
📚 Study Material
Unit	Name	Lecture Material
1	Introduction to Artificial Intelligence	Unit 1 Material
2	Exploratory Data Analysis	Unit 2 Material
3	State Space Search	- Unit 3 Material
4	Knowledge Representation	Unit 4 Material
5	Fuzzy Logic	Unit 5 Material
6	Natural Language Processing	Unit 6 Material
7	Machine Learning	Discussed via hands on
8	Fundamentals of Neural Networks and Expert Systems	Unit 7 Material
EDA Hands-On

Sl no	Dataset	Solution
1	Iris	
2	Titanic	Titanic_EDA
3	IPL 2008-2022 matches dataset	IPL EDA
EDA Practice Problems

Sl No	Dataset	Solution
1	Boston Housing	
2	U.S. International Air Traffic 1990-2020 dataset	
3	Forbes Highest Paid Athletes 1990-2019 dataset	
4	Covid-19 Clinical Trials dataset	
5	Palmer Archipelago dataset	
6	PIMA Indians Diabetes	
7	Amazon Review for Sentiment Analysis	
Course Announcements 📢
Check here for the latest announcements

Pandas Exercise 2 Soln (Temp)

prices = [float(value[1 : -1]) for value in chipo.item_price]

# reassign the column with the cleaned prices
chipo.item_price = prices

# delete the duplicates in item_name and quantity
chipo_filtered = chipo.drop_duplicates(['item_name','quantity','choice_description'])

# chipo_filtered

# select only the products with quantity equals to 1
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
chipo_one_prod
👜 Supplementary Material
datetime module

Image Processing Mini Project

Assignment Submission EDA

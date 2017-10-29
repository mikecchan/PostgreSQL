<h1> Udacity Full Stack Nanodegree Project 3 "Logs Analysis Project" </h1>

In my third project, I built an internal reporting tool to answer certain questions
by accessing and querying a database.

The points of this project is to demonstrate my understanding of...

	1.	Python to connect to a database and display results.
	
	2.	SQL (in this project, particularly with Postgre) to access and extract data 
		from the database .  In my queries, I have utilized several different SQL
		methods to...
		
		i.	Display results
		
		ii.	Join two tables
		
		iii.	Convert different data types such as converting from string to integer.
		
		iv.	Subqueries
		
		v.	And other SQL methods such as grouping data together, performing arithmetics,
			displaying results in a certain order, limiting the number of results to
			display, and etc.


<h3>Instruction to run my project...</h3>

	1. 	My project will be ran in a virtual machine.  So if you have not already,
		download VirtualBox (https://www.virtualbox.org/wiki/Downloads)
		
		VirtualBox is the software that actually runs the virtual machine (VirtualBox in 
		this instance)
		
	2.	Next you would download Vagrant (https://www.vagrantup.com/downloads.html).
		Vagrant is the software that configures the Virtual Machine to let you share 
		files between your host computer and VirtualBox.
		
		Clone the Vagrant files (https://github.com/udacity/fullstack-nanodegree-vm).
		You would clone to a spot on your computer where you would want to my project 
		files to be in.
		
	3.	Download the database where we would access and extract data to answer some
		questions from: 
		
		https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
		
		Place the 'newsdata.sql' file in the 'Vagrant' folder
		
	4. 	Clone/download my 'index.py' file into the 'Vagrant' folder.
	
	5.	Go to your terminal and perform the following...
	
		i.	cd to the 'Vagrant' folder
			
		ii.	run 'Vagrant up'
		
		iii.	run 'Vagrant ssh'
		
		iv.	run 'cd /Vagrant'
		
		v.	run 'ls' to ensure you see my project files.
		
		vi.	run 'psql -d news -f newsdata.sql' to execute the SQL commands that are
		already in the 'newsdata.sql' file to create and populate the tables.
		
		vii.	run 'python index.py'
		
	6.	And you're done!  If you have come to an error somewhere along following the
		instructions, then please skip on down this README file to see what the output
		would look like.
		
		
<h3>These are the questions that I am trying to answer for my project...</h3>

	1.	What are the most popular three articles of all time?
		Which articles have been accessed the most?

	2.	Who are the most popular article authors of all time?

	3.	On which days (time) did more than 1% of requests lead to errors?
	
	
<h3>Here are the answers returned after performing different SQL queries...</h3>

	1.	What are the most popular three articles of all time?  
		Which articles have been accessed the most?
		
		Answer:
			
			Candidate is jerk, alleges rival - 338647 views
			Bears love berries, alleges bear - 253801 views
			Bad things gone, say good people - 170098 views
			

	2.	Who are the most popular article authors of all time?
	
		Answer:
			
			Markoff Chaney - 84557 views
			Ursula La Multa - 507594 views
			Rudolf von Treppenwitz - 423457 views
			Anonymous Contributor - 170098 views
			
	3.	On which days (time) did more than 1% of requests lead to errors?
		
		Answer:
			
			July, 17 2016 - 2.3% errors
			
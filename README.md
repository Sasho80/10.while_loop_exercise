01.Problem: Old books
Annie goes to her hometown after a very long period outside the country. On her way home, she sees her grandmother's old library and remembers her favorite book. 
Help Annie by writing a program in which she enters the book (text) she is looking for.
Until Annie finds her favorite book or checks out all the books in the library, the program must read each time on a new line the name of each subsequent book (text) she checks out.
The books in the library are out of stock once you get the "No More Books" text.
• If it does not find the requested book to be printed on two lines:
o "The book you are looking for is not here!"
o "You checked {number} books."
• If he finds his book, one line is printed:
o "You checked {number} books and found it."

input	     output
Troy	     You checked 2 books and found it.
Stronger
Life Style
Troy

input	         output
The Spot       No More Books	The book you search is not here!
Hunger Games   You checked 4 books.
Harry Potter
Torronto
Spotify

input	         output
Bourne         You checked 10 books and found it.
True Story
Forever
More Space
The Girl
Spaceship
Strongest
Profit
Tripple
Stella
The Matrix
Bourne

02.Problem: Exam preparation
Write a program in which Marin solves exam problems until he receives an "Enough" message from her lecturer. For each solved task he gets a grade. The program should stop reading data on the command "Enough" or if Marin receives the specified number of unsatisfactory marks. Any score less than or equal to 4 is unsatisfactory.
input
• First row - number of unsatisfactory grades - whole number;
• After that, two lines are repeatedly read:
o Task name – text;
o Score - an integer in the range [2…6]
output
• If Marin gets to the "Enough" command, print on 3 lines:
o "Average score: {average score}"
o "Number of problems: {number of all tasks}"
o "Last problem: {last problem name}"
• If he receives the specified number of failing grades:
o "You need a break, {number of unsatisfactory grades} poor grades."
Average grade to be formatted to the second decimal place.

Sample input and output
input       	output
3             Average score: 5.25
Money         Number of problems: 4
6             Last problem: Bus
Story
4
Spring Time
5
Bus
6
Enough	

input      	output
2           You need a break,
Income      2 poor grades.
3
Game Info
6
Best Player
4	

03.Problem: Vacation
Jessie has decided to raise money for a field trip and she wants you to help her find out if she will be able to raise the necessary amount. She saves or spends some of her money every day. If she wants to spend more than her available money, she will spend as much as she has and she will have BGN 0 left.
input
The console reads:
• Money needed for the excursion - a real number;
• Cash available - real number.
Then they are repeatedly read in two lines:
• Type of action – text with two options: "spend" or "save";
• The amount you will save/spend - a real number.
output
The program must be terminated in the following cases:
• If for 5 consecutive days Jesse only spends, the console should read:
o "You can't save the money."
o "{Total Days Elapsed}"
• If Jesse collects the vacation money, the console reads:
o "You saved the money for {total number of days passed} days."

Sample input and output







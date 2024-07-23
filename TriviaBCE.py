# "I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity policy of the CS department.”
#press play to run the code

#import neccasary items
import Draw
import random
import time

# always compile a list of max 5 questions to be displayed(approved)
MAX_QUESTIONS = 5

#master 2D list contianing a list of lists each made of sefer catagory, questions, and answer choices (correct answer begins with *)
QUESTIONS = [
    ['Berishis', 'On one day of creation God said something different. Which day was that, and what did He say?',
     'The third day; God said it was "very good"', '*The sixth day; God said it was "very good"',
     'The sixth day; God said it was "good"', 'The fourth day; God said it was "good"'],
    ['Berishis', 'After eating the fruit from the Tree of Knowledge what was the serpent\'s punishment?',
     '*Crawl on your belly and eat dust', 'A venomous bite', 'Scales'],
    ['Berishis', 'How long was the entire earth completely submerged during the Great Flood?', '75 days', '*150 days',
     '100 days', '40 days'],
    ['Berishis', 'What bird did Noach send out first', 'Dove', 'Eagle', 'Sparrow', '*Raven'],
    ['Berishis', 'Near what city did Lot settle?', 'Canaan', '*Sedom', 'Amora', 'Shechem'],
    ['Berishis', 'How many years passed between the time Avraham left Haran and Yitzhak\'s birth?', '*25', '50', '30', '20'],
    ['Berishis',
     'Lot was prepared to take his wife and daughters out of Sodom to save their lives. \nWhen he told his sons-in-law of the coming destruction, what was their reaction?',
     'They came along willingly', 'They came along once Lot convinced them',
     'They stayed in Sedom to take care of their children', '*They thought he was joking, so they stayed in Sodom'],
    ['Berishis', 'How much did Avraham pay for the Cave of Machpela?', '*400 shekels of silver', '100 shekels of silver',
     '4 shekels of silver', '1000 shekels of silver'],
    ['Berishis', 'How old was Yaakov when he came down to Egypt?', '100 years old', '*130 years old', '110 years old'],
    ['Berishis', 'How old was Yosef when he died?', '*110 years old', '120 years old', '130 years old'],
    ['Shemos', 'What were the names of the two midwives that Pharaoh dealt with?', 'Miriam and Chava', '*Shiphrah and Puah',
     'Sarah and Yocheved', 'Avigayil and Rachel'],
    ['Shemos', 'What were the names of Moshes mother and father?', 'Levi and Avigayil', 'Gershom and Shifrah',
     '*Yocheved and Amram'],
    ['Shemos', 'What was the name of Aaron\'s wife?', 'Tziporah', '*Elisheva', 'Tamar'],
    ['Shemos', 'How much older than Moshe was Aaron?', '5 years', '*3 years', '7 years', '10 years'],
    ['Shemos', 'How many plagues are there in Parshat Bo?', '*3', '2', '4'],
    ['Shemos', 'How did Bnai Yisrael know the way to travel?', 'They followed Moshe',
     '*Hashem provided a pillar of cloud by day and a pillar of fire by night for them to follow',
     'They followed the Tabernacle'],
    ['Shemos', 'How much is an omer?', '*A tenth of an ephah', 'Half of an ephah', 'One ephah'],
    ['Shemos', 'Through whose land did Hashem not lead Bnai Yisrael?', 'Amalek', 'Moavites', '*Philistines'],
    ['Shemos', 'Which two people were responsible for the building of the Tabernacle?', 'Moshe and Ahron',
     '*Betzalel and Ohaliav'],
    ['Shemos', 'What are the names of Aaron\'s sons?', '*Nadav, Abivhu, Eleazar, Ithamar', 'Gershom, Kahas, Marrari'],
    ['Vayikra', 'Whom may a priest not marry?', '*A divorced woman', 'A woman from a non Levite family'],
    ['Vayikra', 'When a peace offering was sacrificed, by when did it have to be eaten?', 'That same day',
     '*By the end of the second day'],
    ['Vayikra', 'In a judgment between a wealthy and a poor person, who should be favored?', 'The poor person',
     'The rich person', '*Neither'],
    ['Vayikra', 'When it appeared that a person might have leprosy, to whom was he taken to check it?', '*Priest', 'Leviite',
     'A doctor'],
    ['Vayikra', 'Two of Aaron\'s sons were killed by Hashem. Who were they?', 'Alazar & Itamar', '*Nadav & Abihu'],
    ['Vayikra',
     'Hashem describes to Moshe the two characteristics of an animal that make it \nacceptable for eating. What are they?',
     '*​​Chew their cud; parted and cloven hoof', 'Non-carnivorous; parted hooves', 'Spotted; Chew their cud'],
    ['Vayikra', 'Why were Aaron\'s sons killed?', '*They gave an inappropriate offering', 'They committed murder',
     'they  disrespected their father'],
    ['Vayikra', 'What items made up the meal offering?', '*Fine flour and oil', 'Leavened bread and honey', 'Barley and wine'],
    ['Vayikra', 'How many days of consecration were there during which Aaron and his sons remained \nin the tent of meeting?',
     '*7', '12', '3', '10'],
    ['Vayikra', 'How long was the burnt offering to last?', '*Continually', 'For one week', 'Only on Yom Kippur'],
    ['Bamidbar', 'What special duty was given to the Levites?',
     '*To do the service of the Tabernacle; to minister unto Aaron and his sons', ' To count Israel',
     'To teach Bnei Yisrael'],
    ['Bamidbar', 'How were the Levites counted?', 'Every male from age 30', 'Everyone',
     '*Every male from a month old and upward'],
    ['Bamidbar', 'What was Moshe told to do with lepers?', '*To put them outside the camp', 'To cut them off',
     'To purify them immediately'],
    ['Bamidbar', 'At what age were those performing this service in the Mishkan required to retire?', '*50', '65', '45', '30'],
    ['Bamidbar', 'At what age did the Levites begin to perform the service in the work of the tent of meeting?', '*25', '30',
     '20', '13'],
    ['Bamidbar', 'When the people were to be called together, how many silver trumpets were blown?', '*2', '5', '10', '7'],
    ['Bamidbar', 'How long was Miriam leprous for?', '*7 days', '3 days', '2 weeks', '3 weeks'],
    ['Bamidbar', 'What was the status of each of the 12 men sent out as spies?', 'They were priests', '*They were princes'],
    ['Bamidbar', 'Two of the spies dissented from the majority report. What were their names?', '*Caleb and Yehoshua',
     'Elazar and Eliyahu', 'Nachson and Eitamar'],
    ['Bamidbar', 'When the people heard the report of the spies, what was their reaction?', 'They rejoiced', '*They despaired'],
    ['Devarim',
     'Moshe was not allowed to enter the land because he failed to sanctify G-d \nin the midst of the Jewish people by doing what?',
     '*Hitting the rock', 'Sending the spies', 'Breaking the luchot'],
    ['Devarim', 'Who is exempt from battle?', '*A man who is afraid', 'An unmarried man', 'A man who is learning Torah'],
    ['Devarim', 'How many nations were cast out so that Israel could possess the Land of Israel?', '*7', '3', '10', '5'],
    ['Devarim', 'We are commanded not to plow with an ass and an ox together. Why?', 'They would fight with eachother',
     'No reason is given', '*They could not pull equally so would create a hardship for both'],
    ['Devarim', 'We are told not to hate an Edomite. Why is that?', 'Because they did not start a war with us in the desert',
     '*Because he is our brother'],
    ['Devarim', 'If a man\'s brother died and he as yet had no children, \nwhat was required of the living brother?',
     'He must bring an offering in the Temple', '*The living brother must marry the dead brother\'s widow',
     'He must commemorate his brothers death yearly'],
    ['Devarim', 'Which is the year of tithing?', '*3rd', '5th', '7th', '2nd'],
    ['Devarim',
     'Moshe charged the tribes to stand on two mountains facing each other. \nWhat were the names of the two mountains?',
     '*Gerizim and Ebal', 'Sinia and Arrat', 'Sedom and Gemora'],
    ['Devarim', 'How old was Moshe when he died?', '100', '*120', '130', '110'],
    ['Devarim', 'In Nitzavim, who did Moshe call together to enter the covenant with Hashem?', 'The Leviim', 'The women',
     'All of the people']
]

#list used for player to pick the sefer
book_list= ['Place holder', 'Pick a Sefer:', 'Berishis', 'Shemos', 'Vayikra', 'Bamidbar', 'Devarim']
#list used for player to pick to keep playing or end
play_again_list= ['place holder','Play again?', 'Done', 'Keep playing!']

def main():
    #set canvas and formating
    Draw.setCanvasSize(1400, 800)
    Draw.setFontSize(30)
    Draw.setFontFamily('Avenir')
    #display the instuctions
    displayinstruct()
    Done = False
    #until the player chooses to stop playing- play the game 
    while not Done:
        #play the whole game
        playGame()
        #get the players choice if they want to continue 
        ans = getchoice(play_again_list)
        #if they choose to be done then display an ending message and end the program (by stopping the loop)
        if ans == "Done":
            Draw.clear()
            Draw.string("Thank you for playing!", 500, 300)
            Draw.show()
            Done = True
            
#the progress of playing the game
def playGame():
    # get the choice of the book that the player chose
    book = getchoice(book_list)
    #compile a list of 5 question/answers lists based on the sefer they chose
    questions = getquestions(QUESTIONS, book)
    #initilize the score to 0
    score = 0
    #loop through each question/answer list in the compiled list 
    for eachq in questions:
        # get thier answer choice for each question
        clicked_ans = getchoice(eachq)
        Draw.setFontBold(True)
        # if thier choice starts with a * then increment thier score
        if clicked_ans[0]=="*":
            score += 1
            #if they chose the correct answer display on the screen that it was correct
            Draw.setColor(Draw.GREEN)
            Draw.filledOval(500, 250, 250, 200)
            Draw.setColor(Draw.BLACK)
            Draw.string('CORRECT!', 550, 325)
        else:
            #if they chose the wrong answer display on the screen that it was incorrect
            Draw.setColor(Draw.PINK)
            Draw.filledOval(500, 250, 250, 200)
            Draw.setColor(Draw.BLACK)
            Draw.string('INCORRECT', 545, 325) 
        Draw.setFontBold(False)
        Draw.show()
        time.sleep(1)
        #absorb clicks made while displaying correct/incorrect
        flushclicks()
    #after they finished the questions go to display the score
    displayscore(score)

#function to get the players choice for each question
#passing in a list of question/answers
def getchoice(pass_in):
    #absorb any extra clicks the player makes
    flushclicks()
    ytop = 100
    Draw.clear()
    Draw.setFontBold(True)
    Draw.string(pass_in[1], 10, 10) #draw question
    Draw.line(0,100,1800, 100)
    Draw.setFontBold(False)
    
    increment = 0
    #for each of the answers draw the answer, and a mark-off line, getting progressivley lower in the canvas
    for ans in pass_in[2:]: 
        if ans[0]=='*': #if the answer starts with a * cut it off
            Draw.string(ans[1:], 30, ytop+increment+25)
            Draw.line(0,ytop+increment+100,1800, ytop+increment+100)
        else:
            Draw.string(ans, 30, ytop+increment+25)
            Draw.line(0,ytop+increment+100,1800, ytop+increment+100)
        increment+=100 
    
    while True:
        #if the player clicks get the Y- location of the click
        if Draw.mousePressed():
            clicklocation = Draw.mouseY()
            numchoice= len(pass_in[2:])
            ansnum = clicklocation// 100
            #make sure the click was valid (not above the answer choices and not below)
            if clicklocation > ytop and clicklocation < ytop+ numchoice*100:
                #return the answer that the player chose from the list that was passed in 
                return pass_in[ansnum+1]
        Draw.show()    
        
#compiling a list of questions based on the sefer the player chose
def getquestions(QUESTIONS, book):
    #initilize a list that will hold all of the chosen sefer questions
    lists = []
    #initilize a list that will hold five questions from lists
    fivelist = []
    #if the sefer of the question list is what was chosen add to lists
    for question in QUESTIONS:
        if question[0] == book:
            lists.append(question)
    #randomize the list (so will always be a diffrent order of questions)
    random.shuffle(lists)
    #build and return the list of 5 questions you will use 
    for i in range (MAX_QUESTIONS): 
        fivelist.append(lists[i])
    return fivelist

#display the intuctions at the begining of the game
def displayinstruct():
    Draw.clear()
    Draw.setFontBold(True)
    Draw.string("Welcome to The Torah Quiz!", 450, 50)
    Draw.setFontBold(False)  
    inst = "Instructions: First, click to pick a Sefer. Then you will be given 5 questions; click on an answer for each"
    Draw.string(inst, 10, 150)
    Draw.string('Click anywhere to start', 500, 300)
    Draw.show()
    #get if they clicked
    while True:
        if Draw.mousePressed():
            locationY = Draw.mouseY()
            locationX = Draw.mouseX()
            return 
        
#display the score with the appropriate effect based on the score
def displayscore(score):
    #draw the score 
    Draw.clear()
    #make the text bigger than before
    Draw.setFontSize(60)
    #draw the players final score
    fscore = 'Final Score: '+ str(score) + '/5'
    Draw.string(fscore, 495, 100)
    
    if score== 5: #add dots and message if perfect score 
        for i in range(700):
            #random dot placement and size
            x = random.randint(0, 1500)
            y = random.randint(0, 1500)
            size = random.randint(5, 30)
            #choose a random dot color
            ballColor = random.choice([Draw.RED,Draw.BLUE,Draw.YELLOW,Draw.GREEN,Draw.CYAN, Draw.ORANGE, Draw.MAGENTA, Draw.VIOLET, Draw.PINK ])
            Draw.setColor(ballColor)
            Draw.filledOval(x, y, size, size)
            Draw.show()
        winning_message= 'You are a Torah Scholar!'
        Draw.setColor(Draw.BLACK)
        Draw.string(winning_message, 375, 300)
    
    elif score== 0: #display encouraging message if they get 0
        zero_message= 'Come to Stern College and learn some Torah!'
        Draw.setFontItalic(True)
        Draw.string(zero_message,70, 300)
        Draw.setFontItalic(False)
    
    elif score== 4 or score ==3: #add confetti and message if score of 3 or 4 
        for i in range (800):
            #randomly place the confetti on the Ycoord
            Ycoor= random.randint(0, 1500)
            #choose a random color for the confetti
            ballColor = random.choice([Draw.RED, Draw.ORANGE, Draw.MAGENTA, Draw.VIOLET, Draw.PINK])
            Draw.setColor(ballColor)
            Draw.filledOval(Ycoor,i,20,20)
            Draw.show()
        Draw.setColor(Draw.BLACK)
        Itermediate_message='Good Job!'
        Draw.string(Itermediate_message, 525, 300)
    
    elif score==1 or score== 2:  #display other encouraging message if they get 1 or 2 
        Draw.setBackground(Draw.PINK)
        low_message= 'Open a Chumash and try again'
        Draw.string(low_message, 275, 300)     
        Draw.show(100)
    #leave on screen for few sec      
    Draw.show(30)
    time.sleep(5)
    Draw.setFontSize(30)
    Draw.setBackground(Draw.WHITE)
    
def flushclicks():
    #consume any extra clicks
    while Draw.mousePressed():
        Draw.mouseX()
        Draw.mouseY()

#run the program 
main()
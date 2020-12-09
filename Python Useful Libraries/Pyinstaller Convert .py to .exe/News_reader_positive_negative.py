from tkinter import *

root = Tk() 
root.geometry("600x650") 
root.title("NEWS text details")
root.configure(bg='light grey')
#=====================================================
def Take_input():
    # answer string
    answer_string = ""
    # taking the input
    INPUT = str(inputtxt.get("1.0", END))
    # textblob
    from textblob import TextBlob
    obj = TextBlob(INPUT)
    # detect language
    answer_string = answer_string + "Detect Language is -"+str(obj.detect_language()) + "-, \n"
    if (obj.detect_language() == 'en'):
        pass
    else:
        INPUT = str(obj.translate(to="en"))
        obj = TextBlob(INPUT)
    # polarity
    # sentiment_analysis = obj.sentiment
    # polarity_str = str(sentiment_analysis)  +", \n 1 = More Subjective,\n 0 = More Objective\n"
    # answer_string = answer_string + polarity_str
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    vader = SentimentIntensityAnalyzer()
    x = vader.polarity_scores(INPUT)
    answer_string = answer_string + "Negative Score = " + str(x['neg']) + " ,Neutral Score = " + str(x['neu']) + " ,Positive Score = "+ str(x['pos']) + ",Polarity = "+str(x['compound']) + "\n"
    # no_of_words
    try:
        no_of_words = len(list(obj.words))
        no_of_words_str = "Number of Words "+str(no_of_words)
        answer_string = answer_string + no_of_words_str
    except:
        no_of_words_str = "Error while calculating the number of words ,"
        answer_string = answer_string + no_of_words_str
            
    # insert the string into answer box
    Output.delete("1.0",END)
    Output.insert(END, answer_string)
    # insert translated
    try:
        translated_output.insert(END,INPUT)
    except:
        pass

#=====================================================
def clear_text():
    inputtxt.delete("1.0",END)
    Output.delete("1.0",END)
    try:
        translated_output.delete("1.0",END)
    except:
        pass
#=====================================================

l = Label(text = "Paste NEWS below") 
inputtxt = Text(root, height = 10, 
		    width = 50, 
		    bg = "light yellow") 

Output = Text(root, height = 5, 
                                width = 45, 
                                bg = "light cyan") 
Clear = Button(root, height = 1, 
                                    width = 30,
                                    bg = "red",
                                    text ="Clear", 
                                    command = lambda:clear_text())
Display = Button(root, height = 2, 
                                    width = 20,
                                    bg = "light green",
                                    text ="Show", 
                                    command = lambda:Take_input())
Label_1 = Label(root, text="Polarity is between (-1,1),  0 to 1 is Positive news and -1 to 0 is negative")
# translated_output
Label_2 = Label(root, text="Translated text (!!! may not accurate)")
translated_output = Text(root, height = 5, 
                                width = 45, 
                                bg = "light blue")


l.pack() 
inputtxt.pack()
Display.pack()
Clear.pack()
Label_1.pack()
Output.pack()
Label_2.pack()
translated_output.pack()


mainloop() 

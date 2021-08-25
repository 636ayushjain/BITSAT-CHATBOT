# BITSAT-CHATBOT


#HOW TO RUN

1. Make a virtual  environment named "rasa-env" and install all packages from requirments.txt, using following command -> pip install -r requirements.txt

2. Open instances for the languages you want to run in terminal and activate "rasa-env" environment on all instances.

3. Go to 'Code/English/' in FIRST terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5005 "
   {English bot running on port:5005}

4. Go to 'Code/Hindi/' in the SECOND terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5006 "
   {Hindi bot running on port:5006}
   
5. Go to 'Code/Gujarati/' in THIRD terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5007 "
   {Gujarati bot running on port:5007}
6. Go to 'Code/Marathi/' in Fourth terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5008 "
   {Marathi bot running on port:5008}
7. Go to 'Code/Bengali/' in Fifth terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5009 "
   {Bengali bot running on port:5009}
8. Go to 'Code/Tamil/' in sixth terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5010 "
   {Tamil bot running on port:5010}
9. Go to 'Code/Telugu/' in seventh terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5011 "
   {Telugu bot running on port:5011}
10. Go to 'Code/Urdu/' in eighth terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5012 "
   {Urdu bot running on port:5012}       
11. Go to 'Code/Malayalam/'in ninth terminal profile and run the command -> " rasa run -m models --enable-api --cors "*" --debug --port 5013 "
   {Malayalam bot running on port:5013}       

. Now open 'index.html' in 'UI' folder on a browser (Chrome preferred) and use the bot as shown in video.

. Bot offers the functionality to type or voice recognition by pressing mic button. 

#Facebook integration

 
1. open 3 instances of terminal and Go to BITSAT_Chatbot. run ./ngrok http 5005 in one terminal,activate rasa-env in second and third  terminal and run command "rasa run" in second terminal and "rasa run actions" in third terminal.
2. Copy Https link from ngrok server.
3. Go to facebook for developers
4. create an app and make page there.
5. In callback URL put https link of ngrok in following format https://ab6eadc5e6ab.ngrok.io/webhooks/facebook/webhook
6. In Verify token write "Bitsat FAQ"
7. Click verify
8. open messenger
9. search Bitsat FAQ and start conversation.

#nlu_creator
1.open BITSAT_Chatbot in terminal and go to nlu_creator.
2. Fill all three csv files with proper format.
3. Run then 3 commands one after other:- python nlu.py, python domain.py, stories.py









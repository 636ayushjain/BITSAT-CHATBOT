import pandas as pd
q=1
df = pd.read_csv(r"/home/ayush/Desktop/BITSAT Chatbot/nlu_creator/storiesdata.csv".format(""))
file = open(r"/home/ayush/Desktop/BITSAT Chatbot/nlu_creator/stories.yml".format(""), "w")
file.write("version: \"2.0\"\n\nstories:\n\n")
intents = list(df.columns)
for item in intents:
    file.write("- story: {intent_name}\n  steps: \n".format(intent_name=item))
    for sent in df[item]:
        if (q == 1):
            q=0
            file.write("  - intent: {}\n".format(sent))     
            
        else:
            q=1    
            file.write("  - action: {}\n".format(sent))    
            
        
file.close()

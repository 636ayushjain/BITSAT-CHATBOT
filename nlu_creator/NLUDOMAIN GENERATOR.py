
# NLU.YML GENERATOR


import pandas as pd
df = pd.read_csv(r"{}".format("nludata.csv"))
file = open(r'{}nlu.yml'.format(""), "w")
file.write("version: \"2.0\"\n\nnlu:\n")
intents = list(df.columns)
for item in intents:
    file.write("- intent: {intent_name}\n  examples: |\n".format(intent_name=item))
    for sent in df[item]:
        file.write("   - {}\n".format(sent))
file.close()



# DOMAIN.YML GENERATOR




import pandas as pd
rf = pd.read_csv(r"{}".format("domaindata.csv"))
intents = list(rf.columns)
file = open(r'{}domain.yml'.format(""), "w")
file.write("version \"2.0\"\n\n")
file.write("intents:\n")
for intent_name in intents:
    file.write("  - {}\n".format(intent_name))
file.write("\n\n")
file.write("responses:\n")
for intent_name in intents:
    file.write("  utter_{}:\n".format(intent_name))
    for ans in rf[intent_name]:
        file.write("  {}\n".format(ans))
file.close()




# STORIES.YML GENERATOR


import pandas as pd
q=1
df = pd.read_csv(r"{}".format("stories.csv"))
file = open(r'{} stories.yml'.format(""), "w")
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

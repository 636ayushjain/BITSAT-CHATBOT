import pandas as pd
df = pd.read_csv(r"/home/ayush/Desktop/BITSAT Chatbot/nlu_creator/nludata.csv".format(""))
file = open(r"/home/ayush/Desktop/BITSAT Chatbot/nlu_creator/nlu.yml".format(""), "w")
file.write("version: \"2.0\"\n\nnlu:\n")
intents = list(df.columns)
for item in intents:
    file.write("- intent: {intent_name}\n  examples: |\n".format(intent_name=item))
    for sent in df[item]:
        file.write("   - {}\n".format(sent))
file.close()






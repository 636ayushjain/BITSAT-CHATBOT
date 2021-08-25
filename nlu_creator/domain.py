import pandas as pd
rf = pd.read_csv(r"/home/ayush/Desktop/BITSAT Chatbot/nlu_creator/domaindata.csv".format(""))
intents = list(rf.columns)
file = open(r"/home/ayush/Desktop/BITSAT Chatbot/nlu_creator/domain.yml".format(""), "w")
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

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

@csrf_exempt
def api(request):
  import json
  post_data = json.loads(request.body.decode("utf-8"))
  user_query = ""
  user_query = post_data.get("q")
  answer = ""
  if user_query != "" :
    
    import pandas as pd
    import numpy as np
    import pickle as pk
    from sklearn.preprocessing import LabelEncoder
    import re
    from nltk.stem.porter import PorterStemmer
    import keras
    from keras.utils import np_utils
    from keras.models import load_model

    def intent_label_map_fun():
      dataset = pd.read_csv('resources/datasets/intent.csv', names=["Query", "Intent"])
      y = dataset["Intent"]
      labelencoder_intent = LabelEncoder()
      y = labelencoder_intent.fit_transform(y)
      y = np_utils.to_categorical(y)
      res = {}
      for cl in labelencoder_intent.classes_:
        res.update({cl:labelencoder_intent.transform([cl])[0]})
      intent_label_map = res
      return intent_label_map

    intent_label_map = intent_label_map_fun()


    import json
    import random

    with open('resources/datasets/intents.json') as json_data:
      intents = json.load(json_data)

    loadedIntentClassifier = load_model('resources/saved_state/intent_model.h5')
    loaded_intent_CV = pk.load(open('resources/saved_state/IntentCountVectorizer.sav', 'rb'))    

    USER_INTENT = ""

    query = re.sub('[^a-zA-Z]', ' ', user_query)
    query = query.split(' ')
    ps = PorterStemmer()
    tokenized_query = [ps.stem(word.lower()) for word in query]
    processed_text = ' '.join(tokenized_query)
    processed_text = loaded_intent_CV.transform([processed_text]).toarray()
    predicted_Intent = loadedIntentClassifier.predict(processed_text)
    result = np.argmax(predicted_Intent, axis=1)    
    for key, value in intent_label_map.items():
      if value==result[0]:
        USER_INTENT = key
        break
        
    for i in intents['intents']:
      if i['tag'] == USER_INTENT:
        answer = random.choice(i['responses'])

    json_output = {"answer": answer}
    print(json_output)
    
  return JsonResponse(json_output)




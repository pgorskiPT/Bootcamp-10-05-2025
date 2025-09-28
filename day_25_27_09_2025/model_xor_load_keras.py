import os
import numpy as np

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # przed importowaniem kerasa
from tensorflow.keras.models import load_model

model = load_model("model_xor.keras")

# kompilacja modelu
model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
# Model: "sequential"
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
# ┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
# │ dense (Dense)                   │ (None, 4)              │            12 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ dense_1 (Dense)                 │ (None, 1)              │             5 │
# └─────────────────────────────────┴────────────────────────┴───────────────┘
#  Total params: 17 (68.00 B)
#  Trainable params: 17 (68.00 B)
#  Non-trainable params: 0 (0.00 B)

# dane wejściowe
X = np.array(
    [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]
)

# testowanie modelu
predictions = model.predict(X)
predictions = (predictions > 0.5).astype(int)

for i in range(len(X)):
    print(f"{X[i]} {predictions[i]}")

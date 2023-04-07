import cv2
import numpy as np
import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

model = tf.keras.models.load_model("Model/mdl_wt.hdf5")

# Write text with larger font size
st.markdown("<h1 style='text-align: left; color: black; margin-top: 0; font-size: 32px;'>🐶 Dog Breed Prediction 🐕‍🦺</h1>", unsafe_allow_html=True)

### load file
uploaded_file = st.file_uploader("Choose an image file🖼️", type=["jpg","png","jpeg"])

if uploaded_file:
    map_dict = {0: 'Affenpinscher',
                1: 'Afghan_hound',
                2: 'African_hunting_dog',
                3: 'Airedale',
                4: 'American_Staffordshire_terrier',
                5: 'Appenzeller',
                6: 'Australian_terrier',
                7: 'Basenji',
                8: 'Basset',
                9: 'Beagle',
                10: 'Bedlington_terrier',
                11: 'Bernese_mountain_dog',
                12: 'Blenheim_spaniel',
                13: 'Bloodhound',
                14: 'Bluetick',
                15: 'Border_collie',
                16: 'Border_terrier',
                17: 'Borzoi',
                18: 'Boston_bull',
                19: 'Bouvier_des_Flandres',
                20: 'Boxer',
                21: 'Brabancon_griffon',
                22: 'Briard',
                23: 'Brittany_spaniel',
                24: 'Bull_mastiff',
                25: 'Cairn',
                26: 'Cardigan',
                27: 'Chesapeake_Bay_retriever',
                28: 'Chihuahua',
                29: 'Chow',
                30: 'Clumber',
                31: 'Cocker_spaniel',
                32: 'Collie',
                33: 'Coonhound',
                34: 'Curly_coated_retriever',
                35: 'Dandie_Dinmont',
                36: 'Dhole',
                37: 'Dingo',
                38: 'Doberman',
                39: 'English_foxhound',
                40: 'English_setter',
                41: 'English_springer',
                42: 'EntleBucher',
                43: 'Eskimo_dog',
                44: 'Flat_coated_retriever',
                45: 'French_bulldog',
                46: 'German_shepherd',
                47: 'German_short_haired_pointer',
                48: 'Giant_schnauzer',
                49: 'Golden_retriever',
                50: 'Gordon_setter',
                51: 'Great_Dane',
                52: 'Great_Pyrenees',
                53: 'Greater_Swiss_Mountain_dog',
                54: 'Groenendael',
                55: 'Ibizan_hound',
                56: 'Irish_setter',
                57: 'Irish_terrier',
                58: 'Irish_water_spaniel',
                59: 'Irish_wolfhound',
                60: 'Italian_greyhound',
                61: 'Japanese_spaniel',
                62: 'Keeshond',
                63: 'Kelpie',
                64: 'Kerry_blue_terrier',
                65: 'Komondor',
                66: 'Kuvasz',
                67: 'Labrador_retriever',
                68: 'Lakeland_terrier',
                69: 'Leonberg',
                70: 'Lhasa',
                71: 'Malamute',
                72: 'Malinois',
                73: 'Maltese_dog',
                74: 'Mexican_hairless',
                75: 'Miniature_pinscher',
                76: 'Miniature_poodle',
                77: 'Miniature_schnauzer',
                78: 'Newfoundland',
                79: 'Norfolk_terrier',
                80: 'Norwegian_elkhound',
                81: 'Norwich_terrier',
                82: 'Old_English_sheepdog',
                83: 'Otterhound',
                84: 'Papillon',
                85: 'Pekinese',
                86: 'Pembroke',
                87: 'Pomeranian',
                88: 'Pug',
                89: 'Redbone',
                90: 'Rhodesian_ridgeback',
                91: 'Rottweiler',
                92: 'Saint_Bernard',
                93: 'Saluki',
                94: 'Samoyed',
                95: 'Schipperke',
                96: 'Scotch_terrier',
                97: 'Scottish_deerhound',
                98: 'Sealyham_terrier',
                99: 'Shetland_sheepdog',
                100: 'ShihTzu',
                101: 'Siberian_husky',
                102: 'Silky_terrier',
                103: 'Soft_coated_wheaten_terrier',
                104: 'Staffordshire_bullterrier',
                105: 'Standard_poodle',
                106: 'Standard_schnauzer',
                107: 'Sussex_spaniel',
                108: 'Tibetan_mastiff',
                109: 'Tibetan_terrier',
                110: 'Toy_poodle',
                111: 'Toy_terrier',
                112: 'Vizsla',
                113: 'Walker_hound',
                114: 'Weimaraner',
                115: 'Welsh_springer_spaniel',
                116: 'West_Highland_white_terrier',
                117: 'Whippet',
                118: 'Wire_haired_fox_terrier',
                119: 'Yorkshire_terrier'}
          
else: 
    st.subheader('☝️ Upload or drop an image file here')
    st.warning('.jpg .png .jpeg file')

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image, (224, 224))

    # Display the uploaded image
    st.image(opencv_image, channels="RGB")

    # Preprocess the image for prediction
    resized = mobilenet_v2_preprocess_input(resized)
    img_reshape = resized[np.newaxis, ...]

    # Generate prediction button
    generate_pred = st.button("🔮Predict")

    if generate_pred:
        # Get the prediction probabilities for the uploaded image
        prediction_probs = model.predict(img_reshape)[0]
        top3_idx = np.argsort(prediction_probs)[-3:][::-1]

        # Display the top 3 predicted labels and their probabilities
        st.write("**Top 3 predicted labels:**")
        for idx in top3_idx:
            st.write("🐾 {}: {:.2f}%".format(map_dict[idx], prediction_probs[idx] * 100))
            st.balloons()

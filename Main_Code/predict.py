import librosa
import numpy as np
import joblib


# ==========================================
# SCIENTIFIC NAME -> COMMON NAME
# ==========================================

bird_name = {

    "Grallaria_cochabambae":
    "Bolivian Antpitta",

    "Grallaria_saltuensis":
    "Perija Antpitta",

    "Grallaria_saturata":
    "Equatorial Antpitta",

    "Grallaria_spatiator":
    "Sierra Nevada Antpitta",

    "Penelope_bridgesi":
    "Yungas Guan",

    "Pyriglena_similis":
    "Tapajos Fire-eye",

    "Pyriglena_maura":
    "Western Fire-eye",

    "Sitta_insularis":
    "Bahama Nuthatch",

    "Basileuterus_delattrii":
    "Chestnut-capped Warbler",

    "Phylloscopus_nesophilus":
    "Sulawesi Leaf Warbler",

    "Pitta_concinna":
    "Ornate Pitta",

    "Larvivora_namiyei":
    "Okinawa Robin"

}


# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load(
    "../model/bird_model.pkl"
)


# ==========================================
# FEATURE EXTRACTION
# ==========================================

def extract_features(file_path):

    # Load Audio
    audio, sr = librosa.load(
        file_path,
        sr=22050
    )


    # Normalize Audio
    audio = librosa.util.normalize(audio)


    # Remove Silence
    audio, _ = librosa.effects.trim(
        audio
    )


    # MFCC (40 Features)
    mfcc = librosa.feature.mfcc(

        y=audio,
        sr=sr,
        n_mfcc=40

    )


    # Mean MFCC
    mfcc_mean = np.mean(

        mfcc.T,
        axis=0

    )


    return mfcc_mean


# ==========================================
# AUDIO TEST FILE
# ==========================================

audio_uji = "../test_audio/uji.mp3"


# ==========================================
# FEATURE EXTRACTION
# ==========================================

features = extract_features(
    audio_uji
)


# ==========================================
# PREDICTION
# ==========================================

prediction = model.predict(
    [features]
)

scientific_name = prediction[0]


# ==========================================
# CONFIDENCE SCORE
# ==========================================

probability = model.predict_proba(
    [features]
)

confidence = max(
    probability[0]
) * 100


# ==========================================
# OUTPUT
# ==========================================

print("\n==========================================")
print("       BIRD SPECIES RECOGNITION")
print("==========================================")


# Unknown Bird Detection

if confidence < 20:

    print("\nPrediction :")
    print("UNKNOWN BIRD SPECIES")

    print("\nConfidence Score :")
    print(f"{confidence:.2f}%")

else:

    print("\nScientific Name :")
    print(scientific_name)


    print("\nCommon Name :")
    print(
        bird_name[scientific_name]
    )


    print("\nPrediction Status :")
    print(
        "KNOWN BIRD SPECIES"
    )


    print("\nConfidence Score :")
    print(
        f"{confidence:.2f}%"
    )


print("\n==========================================")
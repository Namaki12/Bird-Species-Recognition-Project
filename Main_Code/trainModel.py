import os
import librosa
import numpy as np
import joblib

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ==========================================
# DATASET LOCATION
# ==========================================

DATASET_PATH = "../dataset"


# ==========================================
# LIST PENYIMPANAN DATASET
# ==========================================

X = []
y = []


# ==========================================
# FEATURE EXTRACTION FUNCTION
# ==========================================

def extract_features(file_path):

    # Load audio
    audio, sr = librosa.load(
        file_path,
        sr=22050
    )


    # Normalize audio
    audio = librosa.util.normalize(
        audio
    )


    # Remove silence
    audio, _ = librosa.effects.trim(
        audio
    )


    # MFCC (40 Features)
    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )


    # Mengambil rata-rata MFCC
    mfcc_mean = np.mean(
        mfcc.T,
        axis=0
    )


    return mfcc_mean


# ==========================================
# MEMBACA DATASET
# ==========================================

print("\n==========================================")
print("         READING DATASET")
print("==========================================\n")


for species in os.listdir(DATASET_PATH):

    species_folder = os.path.join(
        DATASET_PATH,
        species
    )


    # Pastikan merupakan folder
    if os.path.isdir(species_folder):

        print(
            f"Processing : {species}"
        )


        # Membaca seluruh file audio
        for file in os.listdir(species_folder):

            # Hanya membaca file MP3
            if file.endswith(".mp3"):

                file_path = os.path.join(
                    species_folder,
                    file
                )


                try:

                    # Feature Extraction
                    features = extract_features(
                        file_path
                    )


                    # Simpan fitur audio
                    X.append(
                        features
                    )


                    # Simpan label spesies
                    y.append(
                        species
                    )


                except Exception as e:

                    print(
                        f"ERROR : {file}"
                    )

                    print(e)



# ==========================================
# DATASET INFORMATION
# ==========================================

print("\n==========================================")
print("         DATASET INFORMATION")
print("==========================================")

print(
    f"\nTotal Dataset : {len(X)}"
)

print(
    f"Total Labels  : {len(y)}"
)


# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,
    random_state=42,
    stratify=y

)


# ==========================================
# RANDOM FOREST MODEL
# ==========================================

print("\nTraining Model...\n")


model = RandomForestClassifier(

    n_estimators=500,
    random_state=42

)


model.fit(
    X_train,
    y_train
)


print(
    "Training Model Successfully!"
)


# ==========================================
# PREDICTION
# ==========================================

prediction = model.predict(
    X_test
)


# ==========================================
# ACCURACY SCORE
# ==========================================

accuracy = accuracy_score(

    y_test,
    prediction

)


# ==========================================
# CROSS VALIDATION
# ==========================================

cv_score = cross_val_score(

    model,
    X,
    y,

    cv=5

)


# ==========================================
# CLASSIFICATION REPORT
# ==========================================

report = classification_report(

    y_test,
    prediction

)


# ==========================================
# CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(

    y_test,
    prediction

)


# ==========================================
# MODEL EVALUATION
# ==========================================

print("\n==========================================")
print("         MODEL EVALUATION")
print("==========================================\n")


print(
    f"Training Data : {len(X_train)}"
)

print(
    f"Testing Data  : {len(X_test)}"
)

print()

print(
    f"Accuracy Score : {accuracy*100:.2f}%"
)

print()

print(
    f"Cross Validation Score : {cv_score.mean()*100:.2f}%"
)

print()


print("Classification Report :\n")

print(
    report
)

print()


print("Confusion Matrix :\n")

print(
    cm
)


# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(

    model,
    "../model/bird_model.pkl"

)


# ==========================================
# SUCCESS INFORMATION
# ==========================================

print("\n==========================================")
print("         MODEL SAVED SUCCESSFULLY")
print("==========================================")

print(
    "\nModel Location :"
)

print(
    "../model/bird_model.pkl"
)

print("\n==========================================")
import os
import librosa


# ==========================================
# DATASET LOCATION
# ==========================================

DATASET_PATH = "../dataset"


# ==========================================
# INITIALIZATION
# ==========================================

total_species = 0
total_audio = 0

print("\n==========================================")
print("        BIRD DATASET CHECKER")
print("==========================================\n")


# ==========================================
# READ ALL SPECIES FOLDER
# ==========================================

for species in os.listdir(DATASET_PATH):

    species_folder = os.path.join(
        DATASET_PATH,
        species
    )


    # Make sure it is a folder
    if os.path.isdir(species_folder):

        total_species += 1
        audio_count = 0

        print(f"Species : {species}")
        print("-" * 50)


        # Read all audio files
        for file in os.listdir(species_folder):

            if file.endswith(".mp3"):

                file_path = os.path.join(
                    species_folder,
                    file
                )

                try:

                    # Read audio
                    audio, sr = librosa.load(
                        file_path,
                        sr=22050
                    )


                    # Duration in seconds
                    duration = librosa.get_duration(
                        y=audio,
                        sr=sr
                    )


                    audio_count += 1
                    total_audio += 1


                    print(f"Audio Name     : {file}")
                    print(f"Duration       : {duration:.2f} sec")
                    print(f"Sampling Rate  : {sr}")
                    print(f"Total Samples  : {len(audio)}")


                    # Warning if duration is too short
                    if duration < 0.5:

                        print(
                            "WARNING : Audio terlalu pendek!"
                        )


                    print()


                except Exception as e:

                    print(
                        f"ERROR : {file}"
                    )

                    print(e)
                    print()


        print(f"Total Audio : {audio_count}")


        # Recommendation
        if audio_count < 15:

            print(
                "WARNING : Jumlah audio kurang dari 15."
            )

        elif audio_count >= 15:

            print(
                "GOOD : Jumlah audio sudah memenuhi rekomendasi."
            )


        print("\n")


# ==========================================
# DATASET SUMMARY
# ==========================================

print("==========================================")
print("         DATASET SUMMARY")
print("==========================================")

print(f"\nTotal Species : {total_species}")
print(f"Total Audio   : {total_audio}")


# Average audio per species
if total_species > 0:

    average_audio = total_audio / total_species

    print(
        f"Average Audio per Species : "
        f"{average_audio:.2f}"
    )


print("\n==========================================")
print("DATASET CHECK COMPLETED SUCCESSFULLY!")
print("==========================================\n")
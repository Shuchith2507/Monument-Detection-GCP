import os
import io
from google.cloud import vision_v1
from google.cloud import texttospeech_v1
from google.cloud import translate_v2
import wikipedia

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp.json'
client = vision_v1.ImageAnnotatorClient()


def detect_landmark(file_path):    #Monument detection using 
    try:
        with io.open(file_path, 'rb') as image_file:
            content = image_file.read()

        image = vision_v1.types.Image(content=content)
        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations

        df = []
        for landmark in landmarks:
            df.append(landmark.description)
        return df
    except Exception as e:
        print(e)


places = detect_landmark("Image path/image.jpg")
print(places)
x = wikipedia.summary(places[0])
print(x)

client1 = texttospeech_v1.TextToSpeechClient()

synthesis_input = texttospeech_v1.SynthesisInput(text=x)

voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code='en-in',
    ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
)

audio_config = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3
)

reponse1 = client1.synthesize_speech(
    input=synthesis_input,
    voice=voice1,
    audio_config=audio_config
)

with open('audio1.mp3', 'wb') as output1:
    output1.write(reponse1.audio_content)

translate_client = translate_v2.Client()

target1 = 'kn'
target2 = 'hi'

output1 = translate_client.translate(
    x,
    target_language=target1
)

output2 = translate_client.translate(
    x,
    target_language=target2
)

kannada = output1['translatedText']
hindi = output2['translatedText']

print(kannada)
print(hindi)

synthesis_input1 = texttospeech_v1.SynthesisInput(text=kannada)

voice2 = texttospeech_v1.VoiceSelectionParams(
    language_code='kn-in',
    ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
)

audio_config1 = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3
)

reponse2 = client1.synthesize_speech(
    input=synthesis_input1,
    voice=voice2,
    audio_config=audio_config1
)

with open('audio2.mp3', 'wb') as output2:
    output2.write(reponse2.audio_content)


synthesis_input2 = texttospeech_v1.SynthesisInput(text=hindi)

voice3 = texttospeech_v1.VoiceSelectionParams(
    language_code='hi-in',
    ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
)

audio_config2 = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3
)

reponse3 = client1.synthesize_speech(
    input=synthesis_input2,
    voice=voice3,
    audio_config=audio_config2
)

with open('audio3.mp3', 'wb') as output3:
    output3.write(reponse3.audio_content)

# Monument-Detection-GCP
Monument Detection and Providing Information in Different Languages using GCP

## Pretrained APIs used:
• Cloud Vision

  To identify the landmarks present in the Image.
  
• Text to speech

  To convert the description of landmark we obtained from the image to an audio file.
  
• Translate

  To translate the description we obtained to any language chosen.

Enable these 3 API in your GCP account

## Steps to Run
• Create Service Account in GCP

• After creating click on 3 dots right side of service account, Click manage keys

• Click on Add Key and select new key.

• Download json format and save it in the same directory of your program(gcp.json)

• Run code.py

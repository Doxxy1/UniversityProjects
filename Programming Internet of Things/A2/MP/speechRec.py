import speech_recognition as sr
import subprocess
import speechRec
import surprise

MIC_NAME = "Microsoft® LifeCam HD-3000: USB Audio (hw:1,0)"
def speechSearch():
    # Set the device ID of the mic that we specifically want to use to avoid ambiguity
    for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
        if(microphone_name == MIC_NAME):
            device_id = i
            break

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index = device_id) as source:
        # clear console of errors
        subprocess.run("clear")

        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)

        print("Please say the title youd like to search for: ")
        try:
            audio = r.listen(source, timeout = 1.5)
        except sr.WaitTimeoutError:
            print("Listening timed out whilst waiting for phrase to start")
            quit()
    if(audio is None):
        return
    else:
        pass
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Did you say?  '{}'".format(r.recognize_google(audio)))
        title = r.recognize_google(audio)
        if(title == 'pikachu' or title == 'Pikachu'):
            surprise.printit()
            return
        selection = input('Is this what you want to search for? Y/n: ')
        if(selection == 'Y' or selection == 'y'):
            return title
        else:
            return
    except sr.UnknownValueError:
        print("We couldnt understand you.")
        return
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return

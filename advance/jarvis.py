import pyttsx3

# initialize the engine
engine = pyttsx3.init()

# get current rate
rate = engine.getProperty('rate')
print("Current rate:", rate)

# set new rate (higher = faster, lower = slower)
engine.setProperty('rate', 150)  # default is usually around 200

# say something
engine.say("hello chhanda marik")

# run and wait until speaking is finished
engine.runAndWait()

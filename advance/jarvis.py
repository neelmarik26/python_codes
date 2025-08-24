import pyttsx3

# initialize the engine
engine = pyttsx3.init()

# say something
engine.say("""hii chhanda marik kamon achen.""")

# run and wait until speaking is finished
engine.runAndWait()
#from pyAudioAnalysis import audioAnalysis
import os

def rename():
	i = 1

	address = "/home/ayush/all_venvs/SpeakerDiarization/pyAudioAnalysis-master/pyAudioAnalysis/data/test/HDFC"
	#address = "/home/ayush/Desktop/WishFin/Credit Card/CC"
	listOfAudio = os.listdir(address)
	for filename in listOfAudio:
		src = address + "/" + filename
		dst = address + "/HDFC_" + str(i) + ".wav"

		os.rename(src,dst)
		i+=1


def script():

	# TODO:
	# Don't know yet why complete path is not being accepted
	#directory = "/home/ayush/all_venvs/SpeakerDiarization/pyAudioAnalysis-master/pyAudioAnalysis/data/test/HDFC/HDFC_1.wav"
	directory = "/home/ayush/all_venvs/SpeakerDiarization/pyAudioAnalysis-master/pyAudioAnalysis/data/test/HDFC"
	#directory = "/home/ayush/all_venvs/SpeakerDiarization/pyAudioAnalysis-master/pyAudioAnalysis/data/test/random.wav"

	#for filename in os.listdir(directory):
	#address = directory + "/" + filename

	# counter = 0

	for filename in os.listdir(directory):
		# if(counter==5):
		# 	break

		command = "python audioAnalysis.py speakerDiarization -i " + directory + "/" + filename + " --num 2"
	#command = "python audioAnalysis.py speakerDiarization -i " + directory + " --num 2"
		print("/random.wav")
		os.system(command)

		# counter +=1


if __name__ == "__main__":
	#rename()
	script()
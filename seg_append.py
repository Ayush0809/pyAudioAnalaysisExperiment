from pydub import AudioSegment
import sys,os
from pydub.utils import which

AUDIO_FILE = '~/Desktop/WishFin/Speech\ to\ Text/1.mp3'

def readAudioFile(path):
    '''
    This function returns a numpy array that stores the audio samples of a specified WAV of AIFF file
    '''
    extension = os.path.splitext(path)[1]

    try:
        #if extension.lower() == '.wav':
            #[Fs, x] = wavfile.read(path)
        if extension.lower() == '.aif' or extension.lower() == '.aiff':
            s = aifc.open(path, 'r')
            nframes = s.getnframes()
            strsig = s.readframes(nframes)
            x = numpy.fromstring(strsig, numpy.short).byteswap()
            Fs = s.getframerate()
        elif extension.lower() == '.mp3' or extension.lower() == '.wav' or extension.lower() == '.au' or extension.lower() == '.ogg':            
            try:
                audiofile = AudioSegment.from_file(path)
            #except pydub.exceptions.CouldntDecodeError:
            except:
                print("Error: file not found or other I/O error. "
                      "(DECODING FAILED)")
                return (-1,-1)                

            if audiofile.sample_width==2:                
                data = numpy.fromstring(audiofile._data, numpy.int16)
            elif audiofile.sample_width==4:
                data = numpy.fromstring(audiofile._data, numpy.int32)
            else:
                return (-1, -1)
            Fs = audiofile.frame_rate
            x = []
            for chn in list(range(audiofile.channels)):
                x.append(data[chn::audiofile.channels])
            x = numpy.array(x).T
        else:
            print("Error in readAudioFile(): Unknown file type!")
            return (-1,-1)
    except IOError: 
        print("Error: file not found or other I/O error.")
        return (-1,-1)

    if x.ndim==2:
        if x.shape[1]==1:
            x = x.flatten()

    return (Fs, x)


def audio_segment(AUDIO_FILE):
	AudioSegment.converter = which("ffmpeg")
	sound = AudioSegment.from_file(AUDIO_FILE,format= 'mp3')

	Fs,sound = readAudioFile(AUDIO_FILE)

	mid = len(sound)//2

	first_half = sound[:mid]
	second_half = sound[mid+1:]

	first_half.export("/home/ayush/Desktop/WishFin/first_half.mp3",format = "mp3")
	second_half.export("/home/ayush/Desktop/WishFin/first_half.mp3",format = "mp3")


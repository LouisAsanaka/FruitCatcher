import winsound

class Sound:
    
    @staticmethod
    def play(name):
        print('Playing sound "' + name + '.wav"...')
        winsound.PlaySound('sound/' + name + '.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
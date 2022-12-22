#this class
class bmpg :
    lokasi = ""
    skala = 0
    ritcher = skala
    
    def __init__(cek, lokasi, skala): 
        cek.lokasi = lokasi
        cek.skala = skala
        if skala <= 2 :
            print("gempak tidak berasa, tidak ada dampak")
        elif skala <=4 :
            print("Bangunan akan retak-retak")
        elif skala <= 6:
            print("Bangunan akan roboh")
        else:
            print("Bangunan akan roboh dan berpotensi tsunami") 
            
    
        
    def cetak(cek) :
        print("di daerah", cek.lokasi, 
              "dengan skala", cek.skala, 
              "ritcher.")

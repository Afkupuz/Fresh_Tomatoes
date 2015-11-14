# import files from media for movie constructor and
# fresh_tomatoes for html build.

import media
import fresh_tomatoes

# create movie instances

rainbowrocks = media.Movie("MLP: Rainbow Rocks", "Friendship is magic!",
                           "http://vignette1.wikia.nocookie.net/equestriagirls/images/5/52/My_Little_Pony_Equestria_Girls_Rainbow_Rocks_DVD_cover_art.png/revision/latest?cb=20140818113535",
                           "https://www.youtube.com/watch?v=M-N2Fn1tP3Q")

princessbride = media.Movie("The Pricess Bride",
                            "Hallo, my name is Inigo Montoya",
                            "http://ecx.images-amazon.com/images/I/51CQK1J5sXL._SX940_.jpg",
                            "https://www.youtube.com/watch?v=VYgcrny2hRs")

spaceballs = media.Movie("SPACEBALLS", "I said across her nose; not up it!",
                         "https://slm-assets3.secondlife.com/assets/3291991/lightbox/Spaceballs%20The%20Movie%20MEGAPACK%20512px.jpg?1301467504",
                         "https://www.youtube.com/watch?v=0uzEgsHypgM")

rrrr = media.Movie("RRRrrrr!", "A l'age de pierre",
                   "http://ia.media-imdb.com/images/M/MV5BMTY2Mjg1MzA4OV5BMl5BanBnXkFtZTcwMzYxNDgyMQ@@._V1_UY1200_CR113,0,630,1200_AL_.jpg",
                   "https://www.youtube.com/watch?v=Q-_CtCpCpIQ")

missioncleo = media.Movie("Asterix et Obelix: Mission Cleopatre", "ISTU",
                          "http://www.quartierenmouvement.com/wp-content/uploads/2014/07/asterix-et-obelix-mission-cleopatre-a101-770x1024.jpg",
                          "https://www.youtube.com/watch?v=kCFrvuPpAoQ")

frozen = media.Movie("Frozen", "Let it go",
                     "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=L0MK7qz13bU")


# put movies in a list

movies = [rainbowrocks, princessbride, spaceballs, rrrr, missioncleo, frozen]

# call html creation script

fresh_tomatoes.open_movies_page(movies)

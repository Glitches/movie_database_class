#!/usr/bin/python
# -*- coding: utf-8-*-

# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

frankestein_junior = media.Movie("Frankenstein Junior",
								 "http://www.dietrolequinteonline.it/wp-content/uploads/2011/01/Frankenstein-Junior-1974-di-Mel-Brooks.jpg",
                                 "1974",
								 "Mel Brooks",
								 # "Di ritorno nel castello di famiglia, il barone Frederick Frankenstein, giovane nipote del dottor Frankenstein, si dedica anima e corpo alla sua passione per la scienza e decide di proseguire gli esperimenti iniziati dal nonno tanto tempo prima. Scoperto quindi un fluido magnetico, che permette di richiamare in vita i morti, decide di utilizzarlo per un esperimento.",
								 "https://www.youtube.com/watch?v=J8ghJ2oaZ7U")

kill_bill = media.Movie("Kill Bill",
						"http://2.bp.blogspot.com/-fzaSEUOzOYQ/UPKSCtqUeDI/AAAAAAAAoC0/qBE3GOgJtM4/s1600/kill-bill-vol-1-poster.jpg",
						"2003",
						"Quentin Tarantino",
						# "Una sposa ferita e coperta di sangue; passi di stivali su un pavimento di legno. Poche parole e poi uno sparo: l'uomo con gli stivali, Bill, ha sparato in testa alla sposa.",
						"https://www.youtube.com/watch?v=ot6C1ZKyiME")

giu_la_testa = media.Movie("Giu la testa",
						   "http://www.ossinotizie.it/wp-content/uploads/2014/09/Gi%C3%B9-la-testa.jpg",
						   "1971",
						   "Sergio Leone",
   						   # "Un fuorilegge messicano, Juan Miranda, associatosi a un irlandese, Sean Mallory, per svaligiare una banca, si ritrova a combattere al suo fianco con i rivoltosi di Villa e Zapata.",
						   "https://www.youtube.com/watch?v=S4ELWDFAZfs")

i_soliti_ignoti = media.Movie("I soliti ignoti",
							  "https://arenatoppeghen.files.wordpress.com/2015/03/i_soliti_ignoti.jpg",
							  "1958",
							  "Mario Monicelli",
							  # "Gassman è Peppe, un pugile balbuziente in disarmo, Mastroianni è Tiberio, che bada al pupo mentre la moglie è in prigione, Salvatori è Mario, perditempo bonaccione che si fa mantenere dalle vecchie zie, Murgia è Ferribotte, siciliano geloso della sorella Carmela, Pisacane è Capannelle, dalla storica fame arretrata. Poi c'è Totò, il 'maestro'. Si presenta l'occasione per un colpo facile: scassinare una cassaforte in tutta tranquillità, sfondando un sottile muro che divide un'abitazione privata dal monte dei pegni.",
							  "https://www.youtube.com/watch?v=lhTR_Ng2DKg")


movies = [frankestein_junior, kill_bill, giu_la_testa, i_soliti_ignoti]

animals = media.Vynil("Animals",
					  "http://assets.catawiki.nl/assets/2015/9/11/5/8/7/58752714-5871-11e5-93f7-1a1758b04f1b.jpg",
					  "1975",
					  "Pink Floyd",
					  "https://www.youtube.com/watch?v=gOqblSqx_VI")

ghost_of_tom = media.Vynil("The Ghost of Tom Joad",
						   "http://images.rapgenius.com/a83404d7598d06c52c694669defdad14.1000x1000x1.jpg",
						   "1995",
						   "Bruce Springsteen",
						   "https://www.youtube.com/watch?v=RHOGxHUTxaM")

albums = [animals, ghost_of_tom]

fresh_tomatoes.open_movies_page(movies, albums)

import tweepy,RetweetConcours,BypassAntiBot,time,random,sys,GestionFollow
tabname = []

###Constante Paramètre du bot ###
version = 2.9 #Version du bot
compte = {"1":["","","",""],"2":["","","",""]} #Liste des comptes avec les identifiants de connexion à l'api
NombreDeRetweet = 12 #Nombre de tweet que l'on recupère par recherche
listerecherchefr = ["#concours","#JeuConcours","RT & Follow","tenter de gagner","Gagnez rt + follow","concours pour gagner"]#Mot à retweeter pour un concours
BlackListCompte = ["gulzaarAvi","NistikConcours","WqveConcours","FlawyxC","Linyz_V1","FortniteVenox","TidaGameuse","YeastLeaks","CrashqConcours","Yanteh_","NistiKTV","BotSpotterBot","b0ttem","RealB0tSpotter","jflessauSpam","ConcoursCool","GamingCRewards"]#Blacklist pour compte à concours (très) bidon | Il faut metre le pseudo après le @
CompteTag = ["@j4rj4r_binks"]#Les comptes à utiliser pour tag. Si vous utilisez plusieurs comptes bot vous n'avez pas besoins d'ajouter de comptes dans ce tableau. Vous devez rentrer le compte avec son @ (@toto)
###


for cle,tabauth in compte.items():
    try :
        auth = tweepy.OAuthHandler(tabauth[0], tabauth[1]) #Authentification avec les valeurs du tableau trouvées dans le dictionnaire
        auth.set_access_token(tabauth[2], tabauth[3]) #Authentification avec les valeurs du tableau trouvées dans le dictionnaire
        api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True) #Authentification
        user = api.me()
        tabname.append("@" + user.screen_name)
        GestionFollow.CreateTables(user)
    except tweepy.TweepError as e:
        if e.api_code == 326 or e.api_code == 32 :
            print("Le compte " + cle + " a eu un probleme d'authentification !")
        else :
            print(e.reason)
tabname = tabname + CompteTag
 print("--------------------------------------")

while True :
    for tabauth in compte.values(): #Pour chaque compte on passe dans cette boucle
        try :
            auth = tweepy.OAuthHandler(tabauth[0], tabauth[1]) #Authentification avec les valeurs du tableau trouvées dans le dictionnaire
            auth.set_access_token(tabauth[2], tabauth[3]) #Authentification avec les valeurs du tableau trouvées dans le dictionnaire
            api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True) #Authentification
            user = api.me()
            print("Lancement du bot sur : " + user.screen_name)
            GestionFollow.Unfollow(user,api)
            RetweetConcours.retweet(user,api,NombreDeRetweet,listerecherchefr,tabname,BlackListCompte)#on retweet les concours
            BypassAntiBot.bypass(api)#On bypass l'anti bot
            print("Bot terminé pour ce compte.")
            print("--------------------------------------")
        except tweepy.TweepError as e :
            if e.api_code == 326 :
                pass
    nbrandom = random.randrange(2500,3000)
    try :
        print("Programme en attente de : " + str(nbrandom) + " s") #Temps d'attente en seconde avant une nouvelle boucle
        time.sleep(nbrandom)
    except tweepy.TweepError as e:
        if e.api_code == 326 :
            pass
    except KeyboardInterrupt : #On termine le programme proprement en cas de ctrl-c
        print("Programme terminé !")
        sys.exit()

#Thanks to ChatGPT and Naspa Cheat Sheet for word list  and W3schools for hex converter 
import streamlit as st
import random
import string

import numpy as np

three_letter_words = np.array("""
AAH AAL AAS ABA ABS ABY ACE ACK ACT ADD ADO ADS ADZ AFF AFT
AGA AGE AGO AGS AHA AHI AHS AID AIL AIM AIN AIR AIS AIT AJI
ALA ALB ALE ALL ALP ALS ALT AMA AMI AMP AMU ANA AND ANE ANI
ANT ANY APE APO APP APT ARB ARC ARE ARF ARK ARM ARO ARS ART
ASH ASK ASP ASS ATE ATS ATT AUK AVA AVE AVO AWA AWE AWL AWN
AXE AYE AYS AZO BAA BAD BAE BAG BAH BAL BAM BAN BAP BAR BAS
BAT BAY BED BEE BEG BEL BEN BES BET BEY BIB BID BIG BIN BIO
BIS BIT BIZ BOA BOB BOD BOG BOO BOP BOS BOT BOW BOX BOY BRA
BRO BRR BUB BUD BUG BUM BUN BUR BUS BUT BUY BYE BYS CAB CAD
CAF CAL CAM CAN CAP CAR CAT CAW CAY CEE CEL CEP CHI CIG CIS
COB COD COG COL CON COO COP COR COS COT COW COX COY COZ CRU
CRY CUB CUD CUE CUM CUP CUR CUT CUZ CWM DAB DAD DAG DAH DAK
DAL DAM DAN DAP DAS DAW DAY DEB DEE DEF DEL DEN DEP DEV DEW
DEX DEY DIB DID DIE DIF DIG DIM DIN DIP DIS DIT DOC DOE DOG
DOH DOL DOM DON DOR DOS DOT DOW DOX DRY DUB DUD DUE DUG DUH
DUI DUM DUN DUO DUP DYE EAR EAT EAU EBB ECO ECU EDH EDS EEK
EEL EEW EFF EFS EFT EGG EGO EKE ELD ELF ELK ELL ELM ELS EME
EMO EMS EMU END ENG ENS EON ERA ERE ERG ERN ERR ERS ESS EST
ETA ETH EVE EWE EYE FAB FAD FAG FAH FAM FAN FAR FAS FAT FAV
FAX FAY FED FEE FEH FEM FEN FER FES FET FEU FEW FEY FEZ FIB
FID FIE FIG FIL FIN FIR FIT FIX FIZ FLU FLY FOB FOE FOG FOH
FON FOO FOP FOR FOU FOX FOY FRO FRY FUB FUD FUG FUN FUR GAB
GAD GAE GAG GAL GAM GAN GAP GAR GAS GAT GAY GED GEE GEL GEM
GEN GET GEY GHI GIB GID GIE GIF GIG GIN GIP GIS GIT GNU GOA
GOB GOD GOO GOR GOS GOT GOX GOY GRR GUL GUM GUN GUT GUV GUY
GYM GYP HAD HAE HAG HAH HAJ HAM HAO HAP HAS HAT HAW HAY HEH
HEM HEN HEP HER HES HET HEW HEX HEY HIC HID HIE HIM HIN HIP
HIS HIT HMM HOB HOD HOE HOG HOM HON HOO HOP HOS HOT HOW HOY
HUB HUE HUG HUH HUM HUN HUP HUT HYP ICE ICH ICK ICY IDS IFF
IFS IGG ILK ILL IMP INK INN INS ION IRE IRK ISM ITS IVY JAB
JAG JAM JAR JAW JAY JEE JET JEU JIB JIG JIN JOB JOE JOG JOT
JOW JOY JUG JUN JUS JUT KAB KAE KAF KAS KAT KAY KEA KEF KEG
KEN KEP KEX KEY KHI KID KIF KIN KIP KIR KIS KIT KOA KOB KOI
KOP KOR KOS KUE KYE LAB LAC LAD LAG LAH LAM LAP LAR LAS LAT
LAV LAW LAX LAY LEA LED LEE LEG LEI LEK LET LEU LEV LEX LEY
LIB LID LIE LIN LIP LIS LIT LOB LOC LOG LOO LOP LOR LOT LOW
LOX LUD LUG LUM LUN LUV LUX LYE MAC MAD MAE MAG MAM MAN MAP
MAR MAS MAT MAW MAX MAY MED MEG MEH MEL MEM MEN MES MET MEW
MHO MIB MIC MID MIG MIL MIM MIR MIS MIX MMM MOA MOB MOC MOD
MOG MOI MOL MOM MON MOO MOP MOR MOS MOT MOW MUD MUG MUM MUN
MUS MUT MUX MYC NAB NAE NAG NAH NAM NAN NAP NAV NAW NAY NEB
NEE NEG NET NEW NIB NIL NIM NIP NIT NIX NOB NOD NOG NOH NOM
NOO NOR NOS NOT NOW NTH NUB NUG NUN NUS NUT OAF OAK OAR OAT
OBA OBE OBI OCA OCH ODA ODD ODE ODS OES OFF OFT OHM OHO OHS
OIK OIL OKA OKE OLD OLE OMA OMS ONE ONO ONS OOF OOH OOT OPA
OPE OPS OPT ORA ORB ORC ORE ORG ORS ORT OSE OUD OUR OUT OVA
OWE OWL OWN OWT OXO OXY PAC PAD PAH PAK PAL PAM PAN PAP PAR
PAS PAT PAW PAX PAY PEA PEC PED PEE PEG PEH PEN PEP PER PES
PET PEW PHI PHO PHT PIA PIC PIE PIG PIN PIP PIS PIT PIU PIX
PLY POD POH POI POL POM POO POP POS POT POW POX PRO PRY PSI
PST PUB PUD PUG PUL PUN PUP PUR PUS PUT PWN PYA PYE PYX QAT
QIS QUA RAD RAG RAH RAI RAJ RAM RAN RAP RAS RAT RAW RAX RAY
REB REC RED REE REF REG REI REM REP RES RET REV REX REZ RHO
RIA RIB RID RIF RIG RIM RIN RIP ROB ROC ROD ROE ROM ROO ROT
ROW RUB RUE RUG RUM RUN RUT RYA RYE RYU SAB SAC SAD SAE SAG
SAL SAN SAP SAT SAU SAW SAX SAY SEA SEC SEE SEG SEI SEL SEN
SER SET SEV SEW SEX SEZ SHA SHE SHH SHO SHY SIB SIC SIG SIM
SIN SIP SIR SIS SIT SIX SKA SKI SKY SLY SOB SOC SOD SOH SOL
SOM SON SOP SOS SOT SOU SOW SOX SOY SPA SPY SRI STY SUB SUE
SUK SUM SUN SUP SUQ SUS SYN TAB TAD TAE TAG TAJ TAM TAN TAO
TAP TAR TAS TAT TAU TAV TAW TAX TEA TEC TED TEE TEG TEL TEN
TES TET TEW THE THO THY TIC TIE TIL TIN TIP TIS TIT TIX TIZ
TOD TOE TOG TOM TON TOO TOP TOR TOT TOW TOY TRY TSK TUB TUG
TUI TUM TUN TUP TUT TUX TWA TWO TYE UDO UGH UKE ULU UMM UMP
UMS UNI UNS UPO UPS URB URD URN URP USE UTA UTE UTS VAC VAN
VAR VAS VAT VAU VAV VAW VAX VEE VEG VET VEX VIA VID VIE VIG
VIM VIN VIS VOE VOG VOW VOX VUG VUM WAB WAD WAE WAG WAN WAP
WAR WAS WAT WAW WAX WAY WEB WED WEE WEN WET WHA WHO WHY WIG
WIN WIS WIT WIZ WOE WOK WON WOO WOS WOT WOW WRY WUD WUZ WYE
WYN XED XIS YAG YAH YAK YAM YAP YAR YAS YAW YAY YEA YEH YEN
YEP YER YES YET YEW YEZ YIN YIP YOB YOD YOK YOM YON YOU YOW
YUK YUM YUP ZAG ZAP ZAS ZAX ZED ZEE ZEK ZEN ZEP ZIG ZIN ZIP
ZIT ZOA ZOO ZUZ ZZZ
""".split())

bingoes = np.array("""
ENTASIA
TAENIAS
BANTIES
BASINET
ACETINS
CINEAST
DESTAIN
DETAINS
INSTEAD
NIDATES
SAINTED
SATINED
STAINED
ETESIAN
FAINEST
EASTING
EATINGS
GENISTA
INGATES
INGESTA
SEATING
TAGINES
TEASING
SHEITAN
STHENIA
ISATINE
TAJINES
INTAKES
ELASTIN
ENTAILS
NAILSET
SALIENT
SALTINE
SLAINTE
TENAILS
ETAMINS
INMATES
TAMEINS
INANEST
STANINE
ATONIES
PANTIES
PATINES
SAPIENT
SPINATE
ANESTRI
ANTSIER
NASTIER
RATINES
RETAINS
RETINAS
RETSINA
STAINER
STEARIN
ENTASIS
NASTIES
SEITANS
SESTINA
TANSIES
TISANES
INSTATE
SATINET
AUNTIES
SINUATE
NAIVEST
NATIVES
VAINEST
TAWNIES
WANIEST
ANTISEX
SEXTAIN
ZANIEST
ZEATINS
ARISTAE
ASTERIA
ATRESIA
BAITERS
BARITES
REBAITS
TERBIAS
ATRESIC
CRISTAE
RACIEST
STEARIC
ARIDEST
ASTRIDE
DIASTER
DISRATE
STAIDER
TARDIES
TIRADES
AERIEST
SERIATE
FAIREST
AIGRETS
GAITERS
SEAGIRT
STAGIER
TRIAGES
HASTIER
AIRIEST
REALIST
RETAILS
SALTIER
SALTIRE
SLATIER
TAILERS
IMARETS
MAESTRI
MISRATE
SMARTIE
ANESTRI
ANTSIER
NASTIER
RATINES
RETAINS
RETINAS
RETSINA
STAINER
STEARIN
PARTIES
PASTIER
PIASTER
PIASTRE
PIRATES
PRATIES
TRAIPSE
ARTSIER
TARRIES
TARSIER
ARTSIES
SATIRES
ARTIEST
ARTISTE
ATTIRES
IRATEST
RATITES
STRIATE
TASTIER
RAVIEST
VASTIER
VERITAS
WAISTER
WAITERS
WARIEST
WASTRIE
CERATIN
CERTAIN
CREATIN
TACRINE
ANTIRED
DETRAIN
TRAINED
ARENITE
RETINAE
TRAINEE
FAINTER
GRANITE
GRATINE
INGRATE
TANGIER
TEARING
HAIRNET
INEARTH
THERIAN
INERTIA
KERATIN
LATRINE
RATLINE
RELIANT
RETINAL
TRENAIL
MINARET
RAIMENT
ENTRAIN
TRANNIE
PAINTER
PERTAIN
REPAINT
RETRAIN
TERRAIN
TRAINER
ANESTRI
ANTSIER
NASTIER
RATINES
RETAINS
RETINAS
RETSINA
STAINER
STEARIN
INTREAT
ITERANT
NATTIER
NITRATE
TERTIAN
RUINATE
TAURINE
URANITE
URINATE
TAWNIER
TINWARE
ACONITE
AEOLIAN
AERADIO
AEROSAT
AGONIES
AGONISE
AILERON
AIRDATE
AIRLINE
ALEURON
ALIENED
ALIENER
ALIENOR
ALINERS
ALUNITE
AMNIOTE
ANEROID
ANISEED
ANISOLE
ANODISE
ARANEID
ARENOSE
ARENOUS
ARIETTE
AROINTS
ATELIER
ATONERS
AUDIENT
AUDITEE
DARIOLE
DEARIES
DELAINE
DELATOR
DENARII
DIATRON
DILATER
DINEROS
DIORITE
DONATES
DOURINE
EARNEST
EASTERN
EDITION
EDITORS
ELATION
ELOINER
ELUTION
ENATION
ENTERAL
ENTIRES
ENTOILS
ENTRIES
ERASION
EROTICA
ESTRIOL
ETALONS
ETERNAL
GENITOR
GOATIER
GODETIA
IDEATES
INDORSE
INEDITA
INOSITE
IODATES
IONISER
IRONIES
IRONISE
ISOLATE
ISOLEAD
ITERATE
LADRONE
LEADIER
LENTOID
LEOTARD
LINEATE
LOANERS
LOITERS
MORAINE
NAILERS
NEAREST
NEGATOR
NEROLIS
NEUROID
NIOBATE
NITERIE
NOISIER
NORITES
OESTRIN
OLESTRA
ONLIEST
ORATION
ORDINES
ORIENTS
OUTDARE
OUTEARN
OUTLIER
OUTLINE
OUTREAD
OUTRIDE
RADIATE
RADIOES
RAINOUT
RANDIES
RATIONS
READIES
READOUT
REALISE
REDTAIL
REGINAE
RELOANS
RENAILS
RETINES
RETINOL
RETINUE
REUNITE
ROADIES
ROASTED
ROMAINE
RONDEAU
ROSEATE
ROSINED
ROUTINE
SANDIER
SANTERO
SARDINE
SENARII
SENATOR
SORDINE
SORTIED
SOUTANE
STERANE
STEROID
STONIER
STORIED
STOURIE
TAENIAE
TALONED
TELERAN
TIARAED
TOADIES
TOENAIL
TOILERS
TOLANES
TORSADE
TORULAE
TRAILED
TREASON
TRIALED
TRIENES
TRIODES
UNAIRED
URALITE
URANIDE
URINOSE
UTERINE
""".split())

if "score" not in st.session_state:
    st.session_state.score = 0

if "p" not in st.session_state:
    st.session_state.p = "Guest"

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.markdown("""
    <style>
    .stApp {
    background-color: #ecd9c6;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }

    .stButton {
    margin-bottom: 0.75vw;
    width: 700px;
    }
    </style>

    <div class = "divvy">Scrabblapp - Home</div>
    """, unsafe_allow_html = True)

    if st.button(" Word Checker"):
        st.session_state.page = "check"
        st.rerun()
    if st.button(" 3 Letter Quiz"):
        st.session_state.page = "quiz1"
        st.rerun()
    if st.button(" Vowel Dump Quiz"):
        st.session_state.page = "quiz2"
        st.rerun()
    if st.button("BINGO Quiz - HARD"):
        st.session_state.page = "quiz3"
        st.rerun()
    if st.button("Easy Bingo Checker"):
        st.session_state.page = "bingof"
        st.rerun()
    if st.button("BINGO Quiz - EASY"):
        st.session_state.page = "quiz4"
        st.rerun()
    if st.button("Contact Creators"):
        st.session_state.page = "cc"
        st.rerun()
    if st.button("Credits"):
        st.session_state.page = "c"
        st.rerun()
    if st.button("Helpful Videos"):
        st.session_state.page = "v"
        st.rerun()
    
    if st.button(" Stats"):
        st.session_state.page = "s"
        st.rerun()
    
    if st.button("Super 3s"):
        st.session_state.page = "super"
        st.rerun()

if st.session_state.page == "super":
    VOWELS = "AEIOU"
    CONSONANTS = "".join([c for c in string.ascii_uppercase if c not in VOWELS])

    def generate_fake_word():
        num_vowels = random.randint(1, 2)
        num_consonants = 3 - num_vowels
        
        letters = []
        for _ in range(num_vowels):
            letters.append(random.choice(VOWELS))
        for _ in range(num_consonants):
            letters.append(random.choice(CONSONANTS))
        
        random.shuffle(letters)
        return "".join(letters)

    def get_word():
        if random.random() < 0.5:
            word = random.choice(three_letter_words)
            is_real = True
        else:
            word = generate_fake_word()
            is_real = word in three_letter_words
        return word, is_real

    # session state
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "random_word" not in st.session_state:
        st.session_state.random_word, st.session_state.is_real = get_word()
    if "answered" not in st.session_state:
        st.session_state.answered = False

    # UI
    st.markdown("""
    <style>
    .stApp { background-color: #ecd9c6; }
    .divvy {
        color: #dfbf9f;
        background-color: #ffffff;
        padding-top: 1vw;
        padding-bottom: 1vw;
        text-align: center;
        font-size: 3vw;
        border-radius: 1.5vw;
        margin-bottom: 1.5vw;
    }
    </style>
    <div class="divvy">Scrabble Practice - Super 3s Challenge</div>
    """, unsafe_allow_html=True)

    st.write("Is", st.session_state.random_word, "a valid Scrabble word?")

    choice = st.radio("Choose one:", ["Yes", "No"])

    if st.button("Check Answer") and not st.session_state.answered:
        st.session_state.answered = True
        if (choice == "Yes" and st.session_state.is_real) or \
        (choice == "No" and not st.session_state.is_real):
            st.success("Yes, you got it right! 😎")
            st.session_state.score += 1
        else:
            st.error("Sorry, you got it wrong 😬")

    if st.button("Next Question"):
        st.session_state.random_word, st.session_state.is_real = get_word()
        st.session_state.answered = False
        st.rerun()

    st.write(f"Score: {st.session_state.score}")

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6d/Scrabble_2.jpg")

    if st.button("Back"):
        st.session_state.page = "home"

if st.session_state.page == "s":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Stats</div>
    """, unsafe_allow_html = True)
    
    st.write("Change name?")
    i = st.text_input("")

    st.write("Name : " , st.session_state.p)

    st.write("Delete the letters in the username box for the program to run - don't worry, your username will be saved! ")

    if i != "":
        st.session_state.p = i
        st.rerun()
    if st.session_state.score < 50:
        st.write("Your level : Beginner")
    if st.session_state.score >= 50:
        if st.session_state.score <= 100:
            st.write("Your level : Intermediate")
    if st.session_state.score > 100:
        if st.session_state.score <= 150:
            st.write("Your level : Advanced")
    if st.session_state.score > 150:
        st.write("Your level : Expert")    
    
    st.write("Your score : " , st.session_state.score)

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

if st.session_state.page == "v":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Videos</div>
    """, unsafe_allow_html = True)

    st.write("Courtesy of Will Anderson and no laws were broken :). Go to his channel to see more videos!")

    st.video("https://www.youtube.com/watch?v=NxizYoHaIf0")
    st.video("https://www.youtube.com/watch?v=nZdiSggMUsg")
    st.video("https://www.youtube.com/watch?v=wVoz8OSjlvo")
    st.video("https://www.youtube.com/watch?v=-MEy8TdWlPE")
    st.video("https://www.youtube.com/watch?v=2boBX9lAtS4")
    st.video("https://www.youtube.com/watch?v=AJIAlRSs214")
    st.video("https://www.youtube.com/watch?v=6ytmzCI27Kk")
    st.video("https://www.youtube.com/watch?v=j3udQk1XWBI")
    st.video("https://www.youtube.com/watch?v=qQ9NBmeOci4")
    st.video("https://www.youtube.com/watch?v=whLN4aF2xfE")
    st.video("https://www.youtube.com/watch?v=uOhBed1ujGc")
    st.video("https://www.youtube.com/watch?v=2erXTsAAhg0")
    st.video("https://www.youtube.com/watch?v=9120Php3Kh4")
    st.video("https://www.youtube.com/watch?v=EzbOrbWxliY")
    st.video("https://www.youtube.com/watch?v=TSZn-c3gUFU")
    st.video("https://www.youtube.com/watch?v=PeXLFwYmqv0")
    st.video("https://www.youtube.com/watch?v=vxAHFz90K34")
    st.video("https://www.youtube.com/watch?v=lSLS7tq4C2Y")
    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()
if st.session_state.page == "c":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Credits</div>
    """, unsafe_allow_html = True)

    st.write("Me - for making")
    st.write("ChatGPT - for helping with word lists and generator")
    st.write("NASPA - for Cheat Sheet Lists :)")
    st.write("Will Anderson for Scrabble videos")

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()    



if st.session_state.page == "cc":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Contact Creators</div>
    """, unsafe_allow_html = True)
    st.write("Any ideas, bugs, or word lists? Send them here!")

    st.write("Contact creators at : ")
    st.write("[REDACTED]@gmail.com")

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

if st.session_state.page == "check":
    st.markdown("""
   
    <style>
         .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Scrabble Word Checker - 3s</div>
    """, unsafe_allow_html = True)

    st.title("Valid 3 Letter Scrabble Word Checker for Naspa")
    st.write("Please note that this list is to be updated as it is missing 5 - 10 new words.")

    ans = st.text_input("Enter your 3 letter word (Type out in All Caps) :")

    if ans:
        if ans in three_letter_words:
            st.write("Allowed!")
        else:
            st.write("This is not a valid 3 letter word in Naspa.")

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

if st.session_state.page == "quiz1":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Scrabble Practice - Odd 3s</div>
    """, unsafe_allow_html = True)

    words = np.array(["Edh", "Kax", "Mux", "Lux", "Aji", "Tac", "Orc", "Mia", "Erg", "Por", "Mim", "Kib", "Que", "Oes", "Aux", "Vug", "Ken", "Kef", "Khi", "Lac", "Lor", "Rax", "Fiz", "Tux", "Gox", "Ric", "Tex", "Exe", "Rox", "Kew", "Loh", "Kew", "Lah", "Kee", "Bir", "Mir", "Cox", "Raz", "Daz", "Cuz", "Zuz", "Lix", "Mex", "Lol", "Dru"])
    wordsRight = np.array(["Edh", "Mux", "Lux", "Aji", "Orc", "Erg", "Por", "Mim", "Vug", "Khi", "Ken", "Kef", "Lac", "Lor", "Kue", "Lah", "Mir", "Cox", "Cuz", "Zuz", "Rax", "Fiz", "Tux", "Gox"])
    result = ""

    if "random_word" not in st.session_state:
        st.session_state.random_word = np.random.choice(words)

    st.write(" Is", st.session_state.random_word, "a valid Scrabble word?")


    if st.session_state.random_word in wordsRight:
        if st.checkbox("Yes"):
            result = " Yes, you got it right!"
            st.session_state.score += 1
        if st.checkbox("No"):
            result = " Sorry, you got it wrong!"
    else:
        if st.checkbox("Yes"):
            result = " Sorry, you got it wrong!"
        if st.checkbox(" No"):
            result = " Yes, you got it right!"

            st.session_state.score += 1

    if st.button("Check Answer"):
        st.write(result)

    if st.button("Next Question"):
        st.session_state.random_word = np.random.choice(words)

        st.rerun()

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6d/Scrabble_2.jpg")
    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

if st.session_state.page == "quiz2":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Scrabble Practice - Vowel Dumps</div>
    """, unsafe_allow_html = True)

    words2 = np.array(["aeon",  "awee", "akee", "ajee", "amee", "aurei", "aroai", "aecia", "ohiai", "oidia", "miaou", "paua", "omeia", "loui", "iona", "inia", "moue", "ouzo", "azoia", "zoeae", "aerie", "aeria", "naoi", "oaho", "eide"])
    wordsRight2 = np.array(["aeon", "awee", "akee", "ajee", "aurei", "aecia", "oidia", "miaou", "paua", "inia", "moue", "ouzo", "zoeae", "aerie", "naoi", "eide"])
    result2 = ""

    if "random_word2" not in st.session_state:
        st.session_state.random_word2 = np.random.choice(words2)

    st.write(" Is", st.session_state.random_word2, "a valid Scrabble word?")


    if st.session_state.random_word2 in wordsRight2:
        if st.checkbox(" Yes"):
            result2 = " Yes, you got it right!"

            st.session_state.score += 1
        if st.checkbox(" No"):
            result2 = " Sorry, you got it wrong!"
    else:
        if st.checkbox(" Yes"):
            result2 = " Sorry, you got it wrong!"
        if st.checkbox(" No"):
            result2 = " Yes, you got it right!"

            st.session_state.score += 1

    if st.button("Check Answer"):
        st.write(result2)

    if st.button("Next Question"):
        st.session_state.random_word2 = np.random.choice(words2)

        st.rerun()

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()



if st.session_state.page == "quiz3":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Scrabble Practice - HARD Bingos</div>
    """, unsafe_allow_html = True)

    #(AAH HE MADE SO MANY MISTAKES) Credit to ChatGPT for some bingo things, since it would be very tough to write out all the only one word inside bingo stems (or one obvious word)
    words3 = np.array(["AHURELS", "PIGCONO", "CROERAL", "AWCERLD", "MEGARAN",  "EONMSTR",  "ERACHTN",  "RELACIT", "RETISGN", "NAGARMA", "LACIGAM", "ERIMNOB", "UROFELD", "YORHMAN", "LIMOUTR", "DRNEDKI", "PLDNOIH", "KNPMUPI"])
    wordsRight3 = np.array(["HAULERS", "COOPING", "CAROLER", "CRAWLED", "MANAGER", "MONSTER", "CHANTER","ARTICLE", "RESTING", "ANAGRAM", "MAGICAL", "BROMINE", "FLOURED", "HARMONY", "TURMOIL", "KINDRED", "DOLPHIN", "PUMPKIN"])
    nums = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
    result3 = ""

    if "random_numm" not in st.session_state:
        st.session_state.random_numm = np.random.choice(nums)

    st.write(" Name a bingo with", words3[st.session_state.random_numm], "! ( PLEASE ANSWER IN ALL CAPS )")

    hh = st.text_input("")
    
    if hh == wordsRight3[st.session_state.random_numm]:
        result3 = "Correct!"

        st.session_state.score += 1
    else:
        result3 = "Incorrect Bingo!"

    if st.button("See Answer"):
        st.write(wordsRight3[st.session_state.random_numm])

    if st.button("Check Answer"):
        st.write(result3)

    if st.button("Next Question"):
        st.session_state.random_numm = np.random.choice(nums)

        st.rerun()

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

if st.session_state.page == "bingof":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Scrabble Practice - Easy Bingo Finder</div>
    """, unsafe_allow_html = True)
    st.write("Only for Hi Prob 7s and those in Top Bingo Stems. Please enter in ALL CAPS.")
    
    pp = st.text_input("Your Rack : ")
 
    for w in bingoes:
        if sorted(w) == sorted(pp):
            st.write(w)
    
    st.write("If nothing returns, there are no easy bingoes logged in our word finder.")

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

if st.session_state.page == "quiz4":
    st.markdown("""
    <style>
        .stApp {
    background-color: #ecd9c6;
    }
    body {
    background-color: #939393;
    }
    .divvy {
    color: #dfbf9f;
    background-color: #ffffff;
    padding-top: 1vw;
    padding-bottom: 1vw;

    text-align: center;
    font-size: 3vw;
    border-radius: 1.5vw;
    margin-bottom: 1.5vw;
    }
    </style>

    <div class = "divvy">Scrabble Practice - EASY Bingos</div>
    """, unsafe_allow_html = True)
    result4 = ""

    if "random_num" not in st.session_state:
        st.session_state.random_num = np.random.randint(0, Slen(bingoes))

    st.write(" Name a bingo with", sorted(bingoes[st.session_state.random_num]), "! ( PLEASE ANSWER IN ALL CAPS ) Want to find more bingoes? Use the EASY BINGO CHECKER.")

    hh = st.text_input("")
    
    if hh in bingoes:
        if sorted(hh) == sorted(bingoes[st.session_state.random_num]):
            result4 = "Correct!!"

            st.session_state.score += 1
        else:
            result4 = "Wrong answer, as bingo is not listed in our word list. As it may be missing a few, check in Zzyzzyva to be sure."
    else:
        result4 = "Wrong answer, as bingo is not listed in our word list. As it may be missing a few, check in Zzyzzyva to be sure."
    if st.button("See an answer"):
        st.write(bingoes[st.session_state.random_num])

    if st.button("Check Answer"):
        st.write(result4)

    if st.button("Next Question"):
        st.session_state.random_num = np.random.randint(0, len(bingoes))

        st.rerun()

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

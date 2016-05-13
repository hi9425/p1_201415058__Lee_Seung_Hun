All = [('content', 13.1, 37.1, 8.7, 1.5),
('method', 10.6, 34.6, 13.4, 1.9),
('strelation', 27.1, 40.0, 2.9, 1.5),
('prrelation', 16.2, 37.8, 6.8, 0.8),
('equipment', 11.4, 29.8, 14.8, 4.9),
('enviroment', 12.2, 26.5, 14.9, 4.4),
('subject', 13.5, 29.7, 11.1, 2.4),
('school', 13.7, 37.6, 4.1, 1.2)]

def data():
    best=list()
    for i in range(0,len(All)):
        best.append(All[i][1])
    good=list()
    for i in range(0,len(All)):
        good.append(All[i][2])
    nodbad=list()
    for i in range(0,len(All)):
        nodbad.append(All[i][3])
    verynodbad=list()
    for i in range(0,len(All)):
        verynodbad.append(All[i][4])
    sumvg=0
    for i in range(0,len(All)):
        sumvg = sumvg + best[i]
    sumg = 0
    for i in range(0,len(All)):
        sumg = sumg + good[i]
    goodsum = 0
    goodsum = sumvg + sumg
    print "good is ", goodsum
    average = 0
    gaverage = goodsum / len(All)
    print "Very good is ", gaverage

    sumb=0
    for i in range(0,len(All)):
        sumb = sumb + nodbad[i]
    sumvb = 0
    for i in range(0,len(All)):
        sumvb = sumvb + verynodbad[i]
    nodbadsum = 0
    nodbadsum = sumb + sumvb
    print "nodbad is ", nodbadsum

    baverage = 0
    baverage = nodbadsum / len(All)
    print "nodbad average is ", baverage

data()
raw_input("201415058 LEE SEUNG HUN")
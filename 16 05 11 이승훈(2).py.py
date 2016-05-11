lyrics=["when I find myself in times of trouble",
"mother Mary comes to me",
"speaking words of wisdom let it be",
"and in my hour of darkness",
"she is standing right in front of me",
"speaking words of wisdom let it be",
"let it be let it be let it be let it be",
"whisper words of wisdom let it be",
"and when the broken-hearted people",
"living in the world agree",
"there will be an answer let it be",
"for though they may be parted",
"there is still a chance that they will see",
"there will be an answer let it be",
"let it be let it be",
"let it be let it be",
"yeah there will be an answer let it be",
"let it be let it be let it be let it be",
"whisper words of wisdom let it be",
"let it be let it be ah let it be yeah let it be",
"whisper words of wisdom let it be",
"and when the night is cloudy",
"there is still a light that shines on me",
"shine on until tomorrow let it be",
"I wake up to the sound of music",
"mother Mary comes to me",
"speaking words of wisdom let it be",
"let it be let it be let it be yeah let it be",
"Oh there will be an answer let it be",
"let it be let it be let it be yeah let it be",
"whisper words of wisdom let it be"]


for i in range(0,len(lyrics)):
    print  lyrics[i].split()

d=dict()
for i in range(0,len(lyrics)):
    for c in lyrics[i].split():
        if c in d:
            d[c]=d[c]+1
            print d
        else:
            d[c]=1
for c in d:
    if d[c]>=20:
        print c

raw_input("201415058 LEE SEUNG HUN")
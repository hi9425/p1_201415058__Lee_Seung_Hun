@startuml

title Conditional - Activity Diagram 


start

:점수 입력; 


if (90<Score=<100) then (perfact)
  :A;
else if (80<Score<90) then(great)
  :B;
else if (70<Score<80) then(good)
  :C;
else if (60<Score<70) then(Not Bad)
  :D;

 
endif

:끝;

stop

@enduml
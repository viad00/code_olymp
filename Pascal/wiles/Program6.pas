var x,y:integer;
begin
Writeln('Таблица занчаний функции y=5-x*x/2');
for x:=-5 to 5 do begin
y:=5-sqr(x) div 2;
writeln('x=',x,' ','y=',y);
end;
end.

var 
x,y:real;
begin
Read(x,y);
if (y<=1) and (x>=0) and (y>=-1) and ((y>=x-1) or (1<=Sqr(x)+Sqr(y))) then
 print('принадлежит')
else
 Print('нет')
end.
var 
x,y:real;
begin
Read(x,y);
if ((y<=0) or (y>=x+1)) and (y<=3-Sqr(x)) then
 print('принадлежит')
else
 Print('нет')
end.
var 
x,y:real;
begin
Read(x,y);
if (y<=x+2) and (y<=x-2) and (y<=2) and (y>=0) and (y<=sqr(x)) then
 print('принадлежит')
else
 Print('нет')
end.
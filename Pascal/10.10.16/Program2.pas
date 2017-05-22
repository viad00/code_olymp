var 
x,y:real;
begin
Read(x,y);
if (y<=1) and (y>=0) and (x<=Pi/2) and (y>=Sin(x)) then
 print('принадлежит')
else
 Print('нет')
end.
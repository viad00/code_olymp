var even,odd,a:integer;
begin
write('Введите число: ');
readln(a);
while a>0 do begin
if a mod 2=0 then begin
even:=even+1;
end
else begin
odd:=odd+1;
end;
a:=a div 10;
end;
writeln('Четные - ', even);
write('Нечетные - ', odd);
end.
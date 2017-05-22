var m,i:integer;
begin
for m:=5 to 30 do begin
writeln('делители числа ',m,':');
for i:=2 to m-1 do begin
if m mod i = 0 then
write(i, ' ');
end;
writeln();
end;
end.
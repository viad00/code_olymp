var i:integer;
var A:array[1..20] of integer;
begin
Randomize;
for i:=1 to 20 do begin
A[i]:=Random(18)-9;
write(A[i], ' ');
end;
writeln;
for i:=1 to 20 do begin
if A[i] <0 then
write(A[i]);
end;
end.
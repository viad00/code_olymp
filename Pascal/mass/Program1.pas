var i:integer;
var A:array[1..10] of integer;
begin
Randomize;
for i:=1 to 10 do begin
A[i]:=Random(9);
write(A[i]);
end;
writeln;
for i:=1 to 10 do begin
if A[i] mod 2=0 then
write(A[i]);
end;
end.
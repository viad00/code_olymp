var 
a:array [1..10, 1..20] of integer;
i,j:integer;
sum:array [1..10] of integer;
max:integer;
begin
for i:=1 to 10 do begin
for j:=1 to 20 do begin
a[i,j]:=Random(10);
write(a[i,j], ' ');
end;
writeln;
end;
writeln;
for i:=1 to 10 do begin
sum[i]:=0;
end;
for i:=1 to 10 do begin
for j:=1 to 20 do begin
sum[i]:=sum[i] + a[i,j];
end;
end;
for i:=1 to 10 do begin
write(sum[i], ' ' );
end;
writeln;
max:=1;
for i:=1 to 10 do begin
if sum[i]<sum[max] then begin
max:=i;
end;
end;
write(max, ' ' , sum[max]);
end.
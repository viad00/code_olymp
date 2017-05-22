program project1;
var a:string;
    i:integer;
    b:array[1..50] of integer;
    s:integer;
begin
writeln('Число в Римской СИ');
readln(a);
for i:=1 to length(a) do
    begin
      if a[i]='I'then b[i]:=1;
      if a[i]='V'then b[i]:=5;
      if a[i]='X'then b[i]:=10;
      if a[i]='L'then b[i]:=50;
      if a[i]='C'then b[i]:=100;
      if a[i]='D'then b[i]:=500;
      if a[i]='M'then b[i]:=1000;
    end;
s:=0;
for i:=1 to length(a) do
   begin
     s:=s+b[i];
     if(i>1)and(b[i-1]<b[i]) then s:=s-2*b[i-1];
   end;
write(s);
end.


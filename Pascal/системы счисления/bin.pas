procedure dec2bin(N: integer);
begin
  if N >= 2 then
    dec2bin(N div 2);
  Write(N mod 2);
end;

function step(x:integer):integer;
 var i:integer; st:integer;
 begin
 if x=0 then step:=1 else begin
      st:=1;
      for i:=1 to x do begin
      st:=st*2;
      step:=st;
      end; end;
 end;
var k,a,b,d,s:integer;

begin
s:=0;
k:=0;
writeln('Выберите режим 1:bin2dec 2:dec2bin');
readln(a);
if a=1 then begin
writeln('Выбран режим bin2dec. Введите число');
readln(a);
repeat
      b:=a mod 10;
      d:=a div 10;
      s:=s+b*step(k); 
      k:=k+1;
      a:=d;
until d=0;
writeln(s);
end else begin 
writeln('Выбран режим dec2bin. Введите число');
readln(a);
dec2bin(a);
end;
end.
